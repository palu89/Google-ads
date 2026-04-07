---
name: threads-orchestrator
description: "Threads 运行端极简总路由。当前只保留模版1内容输出。"
homepage: https://threads.net
metadata: {
  "openclaw": {
    "emoji": "🧭",
    "sources": ["codex-platform-operations", "workspace-platform-operations-palu"],
    "version": "3.0.0",
    "verified": true,
    "categories": ["threads", "orchestrator", "template1"]
  }
}
---

# Threads Orchestrator Skill

## 当前角色

你只负责判断：

- 直接写 `模版1`
- 或先摘要再写 `模版1`
- 或对现成正文做 `模版1` 监督检查

## 正式源头

- `/Users/palu/.codex/skills/platform-operations/SKILL.md`
- `/Users/palu/.codex/skills/platform-operations/references/content-output-enforcement.md`
- `/Users/palu/.codex/skills/platform-operations/references/viral-profit-template.md`
- `/Users/palu/.codex/skills/platform-operations/references/template-01-engine-map.md`
- `/Users/palu/.codex/skills/platform-operations/references/codex-content-creation-prompt.md`

## 默认路由

### 1. 模版1 内容输出

命中以下任一信号时，走 `threads-content-output`：

- `模版1`
- 直接写帖
- 写一条 Threads
- 给 `事件`、`方向` 要求起稿

### 2. 长材料摘要

如果用户先给：

- 长链接
- 长报告
- 长草稿
- 长新闻

先走 `threads-openai-summarize`，再交给 `threads-content-output`

### 3. 监督检查

如果用户明确要求：

- 检查这条
- 看看是否符合模版1
- 判断有没有贴旧稿

走 `threads-output-supervisor`

## 边界限制

- 不再默认走账户运营
- 不再默认走 persona
- 不再默认走 P0-P5
- 不再默认走高表现版 / 合规发布版
- 不再默认走旧 editorial 记忆
