# Threads 运行入口

当前 workspace 只保留一条主线：

`模版1 内容输出`

## 现在只做什么

- 读取 Codex live 的 `platform-operations`
- 按 `模版1` 写一篇赚钱兑现型爆帖
- 只交付正文

## 默认源头

优先读取：

- `/Users/palu/.codex/skills/platform-operations/SKILL.md`
- `/Users/palu/.codex/skills/platform-operations/references/content-output-enforcement.md`
- `/Users/palu/.codex/skills/platform-operations/references/viral-profit-template.md`
- `/Users/palu/.codex/skills/platform-operations/references/template-01-engine-map.md`
- `/Users/palu/.codex/skills/platform-operations/references/codex-content-creation-prompt.md`

## 默认路由

命中以下任一信号时，直接走 `threads-content-output`：

- `模版1`
- 直接写帖
- 写一条 Threads
- 给事件和方向直接起稿

如果材料很长：

1. 先走 `threads-openai-summarize`
2. 再走 `threads-content-output`

如果用户明确要求“检查这条是否符合模版1”：

3. 再走 `threads-output-supervisor`

## 不再做什么

不要再默认走：

- persona
- P0 / P1 / P2 / P3 / P4 / P5
- 高表现版 / 合规发布版
- 账户运营
- 排期
- 旧 editorial 记忆
- 旧 temp 文件

## 输出要求

- 只交付正文
- 不附人设
- 不附日期
- 不附类型
- 不附互动收尾
- 不附审稿结论
- 不附任何壳子
