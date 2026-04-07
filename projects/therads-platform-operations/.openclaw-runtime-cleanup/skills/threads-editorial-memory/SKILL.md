---
name: threads-editorial-memory
description: "Legacy editorial memory disabled for current template1 runtime."
homepage: https://threads.net
metadata: {
  "openclaw": {
    "emoji": "🧠",
    "sources": ["workspace-platform-operations-palu"],
    "version": "3.0.0",
    "verified": true,
    "categories": ["threads", "memory", "disabled"]
  }
}
---

# Threads Editorial Memory Skill

当前运行中默认不要读取旧 editorial 记忆。

尤其不要默认读取：

- `CONTENT_HISTORY.md`
- `PERSONA_CONTINUITY_LEDGER.md`
- `SERIES_CONTINUITY_BOARD.md`
- `SUPERVISOR_LOG.md`

这些文件保留为历史存档，不作为当前 `模版1` 的默认输入。
