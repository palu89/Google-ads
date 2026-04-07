---
name: threads-content-output
description: "Threads 内容输出运行包装。按 persona、日期和内容类型直接产出可发文案，并执行最小审稿闸门。"
homepage: https://threads.net
metadata: {
  "openclaw": {
    "emoji": "✍️",
    "sources": ["codex-platform-operations", "workspace-platform-operations-palu"],
    "version": "1.0.0",
    "verified": true,
    "categories": ["threads", "content", "copywriting"]
  }
}
---

# Threads Content Output Skill

## 1. 运行角色

`threads-content-output` 在当前项目里承担的是直接产文角色。

它的职责是：

- 按 persona 与模式产出 Threads 文案
- 自动写出明确日期，不只写“今天”
- 判断内容属于早评、盘中、盘后、方法论、人设包装还是单股
- 识别 `高表现版 / 合规发布版`，不把两者混成同一套写法
- 在交付前执行完整内容闸门，而不是裸写正文

它不是：

- 股票喊单工具
- 无脑模板堆叠器
- 不做审稿的纯文案生成器

## 2. 上游源头

当前 Codex 源端定义来自：

- `/Users/palu/.codex/skills/platform-operations/SKILL.md`
- `/Users/palu/.codex/skills/platform-operations/references/content-output-enforcement.md`
- `/Users/palu/.codex/skills/platform-operations/references/content-performance.md`
- `/Users/palu/.codex/skills/platform-operations/references/persona-registry.md`
- `/Users/palu/.codex/skills/platform-operations/references/persona-expression-variance.md`
- `/Users/palu/.codex/skills/platform-operations/references/story-structure-formula-library.md`
- `/Users/palu/.codex/skills/platform-operations/references/story-mode-switch-sop.md`
- `/Users/palu/.codex/skills/platform-operations/references/threads-copy-compliance.md`
- `/Users/palu/.codex/skills/platform-operations/references/threads-account-compliance.md`
- `/Users/palu/.codex/skills/platform-operations/references/p0-persona-branding.md`
- `/Users/palu/.codex/skills/platform-operations/references/p1-trading-psychology.md`
- `/Users/palu/.codex/skills/platform-operations/references/p2-morning-brief.md`
- `/Users/palu/.codex/skills/platform-operations/references/p3-intraday-tracker.md`
- `/Users/palu/.codex/skills/platform-operations/references/p4-postmarket-recap.md`
- `/Users/palu/.codex/skills/platform-operations/references/p5-evening-lessons-high-performance.md`
- `/Users/palu/.codex/skills/platform-operations/references/macro-news-synthesizer.md`
- `/Users/palu/.codex/skills/platform-operations/references/single-stock-deepdive.md`

当前运行端协同 skills：

- `/Users/palu/.openclaw/workspace-platform-operations-palu/skills/threads-editorial-memory/SKILL.md`
- `/Users/palu/.openclaw/workspace-platform-operations-palu/skills/threads-output-supervisor/SKILL.md`
- `/Users/palu/.openclaw/workspace-platform-operations-palu/skills/threads-openai-summarize/SKILL.md`

## 3. 默认行为

### 3.1 先定 persona

- 若用户明确指定 persona，就用指定 persona
- 若未指定，按 `persona-registry.md` 自动匹配
- 若仍不明确，默认使用 `taiwan-stock-captain`
- 若命中的是非 `active` persona，只能输出测试版或草稿版

在真正写正文前，还要先从 `threads-editorial-memory` 读取：

- 同一 persona 最近 7 天内容
- 同一 persona 最近 30 天同主题内容
- 当天同组内容链位置
- 当前系列是否有未接上的节点

如果输入材料包含以下任一内容，还要先走 `threads-openai-summarize`：

- 长链接
- 长新闻
- 长报告
- 长网页
- 长草稿

### 3.2 再定内容模块

按以下顺序判断：

- `P0` 人设包装
- `P1` 方法论
- `P2` 早评
- `P3` 盘中
- `P4` 盘后
- `P5` 晚间教育
- 单股分析

### 3.2.5 再定结构模式

若输入中出现以下任一信号，视为显式模式要求：

- `/高表现版/`
- `/合规发布版/`
- `类型：...（高表现版）`
- `类型：...（合规发布版）`
- `模式：高表现版`
- `模式：合规发布版`

默认规则：

- 若用户明确写了 `高表现版`，必须读取 `story-structure-formula-library.md`，按 `高表现版` 分支生成
- 若用户明确写了 `合规发布版`，必须按 `合规发布版` 分支生成
- 若用户没有写模式，默认按 `合规发布版`
- 若用户先给出一版高张力草稿又要求“可发版”，必须再读 `story-mode-switch-sop.md`
- 若当前模块是 `P5`，统一读取 `p5-evening-lessons-high-performance.md`
- 若当前模块是 `P5` 且模式是 `合规发布版`，必须再读 `story-mode-switch-sop.md` 做收口

### 3.3 完整执行闸门

当前运行端不是只执行“最小闸门”，而是完整继承 Codex 源端
`content-output-enforcement.md` 的执行链。

生成前，至少完成以下 8 项：

1. 任务归类
- 判断当前是不是内容产出，而不是 skill 维护或纯运营治理

2. 人设确认
- 明确当前 `persona_id`
- 若 persona 不是 `active`，只能输出测试版、模板版或草稿版

3. 模块确认
- 明确属于 `P0 / P1 / P2 / P3 / P4 / P5 / 单股分析`
- 不允许把多个模块硬混成一篇

4. 目标确认
- 明确目标受众
- 明确主痛点
- 明确用户最终会带走什么判断、方法或提醒

5. 连续性定位
- 判断与上一篇内容的关系
- 判断在当天内容链中的角色
- 若没有历史上下文，至少按单篇自洽处理

6. 风险预判
- 先检查是否存在收益承诺、机构背书滥用、翻身叙事、过度煽动等高风险表达
- 必要时回读 `threads-copy-compliance.md` 与 `threads-account-compliance.md`

7. 表达纹理计划
- 回读 `persona-expression-variance.md`
- 确认情绪底色、生活锚点、句子粗糙度与口头纹理
- 若当前 persona 属于稳重理性簇，不要硬塞错字、乱标点或空格错位

8. 结构模式与公式计划
- 若是 `高表现版` 或明确要高张力钩子，必须读 `story-structure-formula-library.md`
- 至少先定：`标题公式`、`开头公式`、`是否使用转折公式`、`收尾公式`
- 若要把高表现稿交付成可发布稿，必须读 `story-mode-switch-sop.md`
- 若是 `P5`，必须读 `p5-evening-lessons-high-performance.md`
- 若是 `P5 + 合规发布版`，必须再读 `story-mode-switch-sop.md`

正文完成后，必须继续完成以下 7 项复核：

1. 表现力复核
- 是否具备 `痛点切入`、`利他价值`、`互动收尾`

2. 去重复核
- 做内部去重检查，不把旧结构换词重发

3. 连续性复核
- 确认这篇是否和上下文、自身结构、系列关系一致

4. 合规复核
- 至少过一次 `threads-copy-compliance.md`
- 涉及账号身份、履历、机构或实名时，再过 `threads-account-compliance.md`

5. 人设一致性复核
- 检查权威来源、语气、受众和禁区是否真的匹配该 persona

6. 去 AI 与人类纹理复核
- 检查是否太顺、太满、太像模板填空
- 检查生活锚点是否具体
- 检查口癖、停顿和句子毛边是否真的符合该 persona

7. 结构模式复核
- 若标为 `高表现版`，检查是否真的使用了强开头、误判/反转或清晰收尾，而不是整齐说明文换词
- 若标为 `高表现版`，但开头仍停留在泛共情或背景交代，没有尽快进入具体异常、痛点或误判，应直接重写
- 若标为 `高表现版`，但正文出现两个及以上教学编号清单、检查表或带编号的自助结构，应直接重写
- 若标为 `P5 + 高表现版`，但正文先用抽象心理术语起势，再补抽象解释，应直接重写
- 若标为 `P5 + 高表现版`，正文最终仍落成带编号的自助清单，应直接重写
- 若标为 `合规发布版`，检查是否已经收掉内幕感、收益刺激和过猛戏剧化
- 若本次从高表现稿转成可发版，再按 `story-mode-switch-sop.md` 复核一次

### 3.4 最小执行记录

每次内容输出，内部至少保留：

- 使用的人设
- 使用的模式：`高表现版 | 合规发布版`
- 当前模块
- 主痛点
- 使用的纹理簇
- 是否使用生活锚点
- 是否使用结构公式
- 是否做了去重
- 是否做了连续性检查
- 是否做了合规检查
- 最终处理级别：`BLOCK | REWRITE | REVISE | PASS`

除非用户明确要求，这些记录不必全部展示给用户。

### 3.5 监督与回写

正文草稿完成后，不直接宣称“可发”。

必须继续执行：

1. 交给 `threads-output-supervisor` 做最终判级
2. 若结果为 `BLOCK` 或 `REWRITE`，先返回修订或阻断结论
3. 若结果为 `REVISE` 或 `PASS`，再把本次内容写回 `threads-editorial-memory`

## 4. 固定输出格式

默认按以下顺序输出：

- `人设：...`
- `日期：YYYY-MM-DD`
- `类型：...`
- `标题：...`
- `正文：...`
- `互动收尾：...`
- 若用户显式要求模式，可在 `类型` 中写成：`P5 晚间教育（高表现版）`

默认不要把以下调试性结构直接展示给用户：
- `第一段 / 第二段 / 第三段`
- `开头 / 转折 / 收尾` 这类模板脚手架标签
- `内部记录 / 执行记录 / 审稿记录`

只有在用户明确要求看结构拆解、过程记录或内部检查时，才允许展示这些标签。

如果用户要求更短：

- 可以省略标题
- 但 `人设`、`日期`、`正文` 不能省

## 5. 适用场景

适合：

- 群里 @ 机器人直接要一条文案
- 基于主题、新闻、链接、草稿、股票名产出内容
- 要写今日文案、早评、盘中、盘后、方法论或单股内容

不适合：

- 只讨论账号运营结构而不需要产文
- 系统层技能安装与治理
- 任何保证收益、明确喊单或诱导交易表达

## 6. 边界限制

- 不把不同 persona 写成只换名字的同一篇文案
- 不把 `高表现版` 写成整齐解释稿，也不把 `合规发布版` 写成残留内幕感的半收口稿
- 不把 `高表现版` 写成“生活锚点 + 教学拆解 + 自助清单”的对称晚课稿
- 不把 `高表现版` 写成前半段泛共情、后半段编号解释的分段说明稿
- 不把模板脚手架标签直接留在成稿里
- 不在用户未要求时把 `内部记录`、`最小执行记录` 或监督结论原样贴进正文输出
- 遇到“今天、最新、盘中、当日新闻、即时行情”必须写出具体日期
- 若信息不足，先给最合理版本，再简短说明还缺什么
- 需要整理长资料时，不直接裸调用全局 `summarize`
- 当前项目统一通过 `threads-openai-summarize` 锁定到 DeepSeek 推理摘要链
- 不把运营治理说明塞进正文里替代内容本体
- 若未确认 persona，不得直接写正文
- 若未做去重，不得直接给“可发版”
- 若未做连续性检查，不得直接给系列内容
- 若未做合规检查，不得直接给 Threads 可发布结论
- 若结果为 `BLOCK` 或 `REWRITE`，不得伪装成已通过
- 若未读取内容记忆基线，不得宣称连续性已检查
