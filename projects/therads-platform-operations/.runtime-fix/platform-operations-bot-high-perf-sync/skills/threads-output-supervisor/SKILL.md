---
name: threads-output-supervisor
description: "Threads 输出监督器。对拟输出内容执行 persona 一致性、去重、连续性、合规和发布级别判定，并给出 BLOCK / REWRITE / REVISE / PASS。"
homepage: https://threads.net
metadata: {
  "openclaw": {
    "emoji": "🛡️",
    "sources": ["codex-platform-operations", "workspace-platform-operations-palu"],
    "version": "1.0.0",
    "verified": true,
    "categories": ["threads", "supervision", "quality"]
  }
}
---

# Threads Output Supervisor Skill

## 1. 运行角色

`threads-output-supervisor` 是 Threads 项目的输出监督层。

它的职责是：

- 对拟交付内容做最终人设、去重、连续性和合规判级
- 决定这篇内容是 `BLOCK`、`REWRITE`、`REVISE` 还是 `PASS`
- 不让“看起来像能发”的内容绕过正式审查

它不是：

- 纯内容生成器
- 系统层审核中心
- 可替代 `threads-content-output` 的写作 skill

## 2. 上游源头

当前 Codex 源端依据来自：

- `/Users/palu/.codex/skills/platform-operations/references/content-output-enforcement.md`
- `/Users/palu/.codex/skills/platform-operations/references/content-performance.md`
- `/Users/palu/.codex/skills/platform-operations/references/persona-expression-variance.md`
- `/Users/palu/.codex/skills/platform-operations/references/story-structure-formula-library.md`
- `/Users/palu/.codex/skills/platform-operations/references/story-mode-switch-sop.md`
- `/Users/palu/.codex/skills/platform-operations/references/content-dedup-audit.md`
- `/Users/palu/.codex/skills/platform-operations/references/content-continuity.md`
- `/Users/palu/.codex/skills/platform-operations/references/threads-review-workflow.md`
- `/Users/palu/.codex/skills/platform-operations/references/threads-copy-compliance.md`
- `/Users/palu/.codex/skills/platform-operations/references/threads-account-compliance.md`
- `/Users/palu/.codex/skills/platform-operations/references/persona-registry.md`
- `/Users/palu/.openclaw/workspace-platform-operations-palu/editorial/CONTENT_HISTORY.md`
- `/Users/palu/.openclaw/workspace-platform-operations-palu/editorial/PERSONA_CONTINUITY_LEDGER.md`
- `/Users/palu/.openclaw/workspace-platform-operations-palu/editorial/SERIES_CONTINUITY_BOARD.md`

## 3. 默认监督顺序

每次监督按以下顺序进行：

1. 人设一致性
- 当前 persona 是否 `active`
- 权威来源、语气、受众和禁区是否一致

1.5 persona 本地约束校验
- 读取当前 persona 的 `output_limit`（如有），检查内容字数是否超限
- 读取当前 persona 的 `interaction_patterns`（如有），检查结尾互动是否使用人设专属句型（或在其基础上变体）
- 若违反本地约束（如 stock‑analyst 超过 100 字），直接判 `REWRITE`，理由：“违反 persona 本地约束”

1.8 结构模式校验
- 若内容声明为 `高表现版`，必须同时看到：
  - 明确的强开头类型：反差、异常、痛点投射、反常识或具体案例之一
  - 至少一个清晰的 `误判 -> 反转` 或 `痛点 -> 提醒` 转换
  - 与标题、开头、收尾不重复的结构分工
- 若内容声明为 `高表现版`，但正文仍然是整齐说明文、泛化解释稿或只会列 `1/2/3` 的解释稿，应直接判 `REWRITE`，理由：“声明为高表现版，但结构不符合当前模式”
- 若内容声明为 `高表现版`，但前两段仍然主要停留在泛共情、泛背景交代，没有尽快进入 `异常信号 / 误判点 / 反常识问题 / 具体案例`，应判 `REWRITE`，理由：“声明为高表现版，但开头未进入有效场景”
- 若内容声明为 `高表现版`，却同时出现两个及以上教学清单、编号段落或“先解释再给清单”的晚间结构，应判 `REWRITE`，理由：“声明为高表现版，但主拆解过多”
- 若内容声明为 `高表现版`，却把正文写成“生活锚点 + 教学拆解 + 自助清单”这类高度对称结构，应优先认定为不符合当前模式，不得直接 `PASS`
- 若内容声明为 `P5`，却没有落在 `p5-evening-lessons-high-performance.md` 的当前结构要求上，应直接判 `REWRITE`
- 若内容声明为 `P5 + 高表现版`，却先抛抽象心理术语，再补通用解释，应判 `REWRITE`，理由：“声明为高表现版，但抽象术语未落地”
- 若内容声明为 `P5 + 高表现版`，正文主要解决方式仍是带编号的自助清单，应判 `REWRITE`，理由：“声明为高表现版，但仍落回自助清单”
- 若内容声明为 `P5 + 高表现版`，抽象术语没有立刻落到一个具体动作、一个卡住的念头或一个盘后瞬间，也应优先判定为不符合当前结构
- 若正文仍保留 `第一段 / 第二段 / 第三段`、`开头 / 转折 / 收尾` 等脚手架标签，应判 `REVISE`；若同时伴随结构失衡，则判 `REWRITE`
- 若未被用户要求展示内部检查，却把 `内部记录`、`最小执行记录`、监督结果原样输出给用户，应判 `REVISE`
- 若内容声明为 `合规发布版`，则不得残留明显内幕感、收益炫耀或过猛戏剧化
- 若内容明确从 `高表现版` 收口而来，再按 `story-mode-switch-sop.md` 检查是否既保留张力、又完成风险收口

2. 去重检查
- 是否与最近 7 天、30 天或当天相邻内容过度重复
- 是否只是换了名字和句式

3. 连续性检查
- 是否承接上一篇
- 是否在当天内容链里扮演明确角色
- 是否为下一篇留下钩子

4. 合规检查
- 是否有收益承诺、喊单、误导性背书、过度煽动
- 是否存在平台或账号层高风险表达

5. 最终判级
- `BLOCK`
- `REWRITE`
- `REVISE`
- `PASS`

## 4. 默认输出协议

至少给出：

- 监督结论
- 人设连续性
- 去重结果
- 连续性结果
- 合规结果
- 处理级别
- 下一步动作

若用户只是要成稿：

- `PASS` 时不必展开长审稿说明
- `REVISE` 时应直接告诉用户要改哪里
- `BLOCK` 或 `REWRITE` 时不得伪装成可发布版

## 5. 监督后动作

- 若结果为 `BLOCK` 或 `REWRITE`，先停在监督结论
- 若结果为 `REVISE` 或 `PASS`，同步写入 `SUPERVISOR_LOG.md`
- 只有在 `REVISE` 或 `PASS` 后，才允许交给 `threads-editorial-memory` 做历史回写

## 6. 边界限制

- 不在没有历史基线时假装“去重已通过”
- 不在没有连续性依据时假装“系列已接上”
- 不把高风险表达包装成“只是风格问题”
