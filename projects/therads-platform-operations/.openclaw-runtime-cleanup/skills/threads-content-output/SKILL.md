---
name: threads-content-output
description: "Threads 内容输出运行包装。当前只保留模版1赚钱兑现型爆帖。"
homepage: https://threads.net
metadata: {
  "openclaw": {
    "emoji": "✍️",
    "sources": ["codex-platform-operations", "workspace-platform-operations-palu"],
    "version": "3.0.0",
    "verified": true,
    "categories": ["threads", "content", "template1"]
  }
}
---

# Threads Content Output Skill

## 当前角色

这里只有一件事：

`按模版1直接输出正文`

## 必读源头

- `/Users/palu/.codex/skills/platform-operations/SKILL.md`
- `/Users/palu/.codex/skills/platform-operations/references/content-output-enforcement.md`
- `/Users/palu/.codex/skills/platform-operations/references/viral-profit-template.md`
- `/Users/palu/.codex/skills/platform-operations/references/template-01-engine-map.md`
- `/Users/palu/.codex/skills/platform-operations/references/codex-content-creation-prompt.md`

## 默认输入

最小输入：

```text
模版1
```

可选补充：

```text
人设：<任意标签>
日期：YYYY-MM-DD
事件：<热点事件>
方向：<真正赚钱方向>
```

## 默认行为

1. 识别是否为 `模版1`
2. 读取 Codex live 的执行闸门、模板、结构地图和 Codex 提示词
3. 严格按 `模版1` 的功能位和槽位替换执行
4. 只输出正文

## 边界限制

- 不读取 persona 文档
- 不读取 P0-P5 旧模块
- 不读取高表现版/合规发布版旧逻辑
- 不把 `模版1` 写成方法课、摘要帖、晚间教育帖或情绪安慰文
- 不附任何外壳
