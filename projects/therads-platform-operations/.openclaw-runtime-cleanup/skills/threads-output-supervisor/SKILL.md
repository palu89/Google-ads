---
name: threads-output-supervisor
description: "Threads 输出监督器。只检查模版1正文是否贴错旧稿、结构是否成立、赚钱兑现是否完整。"
homepage: https://threads.net
metadata: {
  "openclaw": {
    "emoji": "🛡️",
    "sources": ["codex-platform-operations", "workspace-platform-operations-palu"],
    "version": "3.0.0",
    "verified": true,
    "categories": ["threads", "supervision", "template1"]
  }
}
---

# Threads Output Supervisor Skill

## 当前角色

这里只检查三件事：

1. `模版1` 结构是否成立
2. 是否过度贴近旧稿/原帖
3. 赚钱兑现闭环是否完整

## 正式依据

- `/Users/palu/.codex/skills/platform-operations/references/content-output-enforcement.md`
- `/Users/palu/.codex/skills/platform-operations/references/viral-profit-template.md`
- `/Users/palu/.codex/skills/platform-operations/references/template-01-engine-map.md`

## 检查顺序

1. 结构
- 是否按功能位推进
- 是否一开头就先报结果
- 是否缺私密入口 / 大众误判 / 提前下手 / 回头来问

2. 反复用
- 是否复用了旧稿特征词
- 是否复用了旧场景链
- 是否当前会话里已出现原帖，却还沿用同类人物入口、同类钉子词、同类回问句型

3. 兑现
- 是否真的有先下手
- 是否真的有过程型兑现
- 是否真的有人后来回头来问

## 判级

- `REWRITE`：结构不成立，或过度贴近旧稿
- `REVISE`：结构成立，但兑现太弱或替换不够
- `PASS`：可交付

## 输出协议

- 监督结论
- 结构结果
- 反复用结果
- 兑现结果
- 下一步动作
