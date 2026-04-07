# Threads 自动回写完成度核对清单

本文件用于在近义变体命中并执行自动回写后，核对治理链是否真的完成闭环，避免只改了一处文件就误判为“已经收口”。

## 一、适用场景

- 已执行 `threads-variant-trigger-auto-writeback-rules.md`
- 高风险表达近义变体已经真实命中
- 需要确认 `must-write`、`should-write`、`context-write` 是否都已落地
- 需要判断这次回写能否正式关闭，还是必须继续补写

## 二、核对结论

- `complete`
- `partial`
- `reopen`

## 三、最小判断维度

1. `must-write` 文件是否全部更新
2. 替代表达、黑名单和近义变体禁用表是否已经对齐
3. 若影响排期、栏目或阶段目标，关联文件是否同步更新
4. 若发生在已发布阶段，事故记录与复盘是否已补齐
5. 下一轮观察点和责任人是否已明确

## 四、最小模板

```text
Threads 自动回写完成度核对：
- 触发变体：
- 关联原表达：
- 当前阶段：review | schedule | published
- must-write 完成情况：
- should-write 完成情况：
- context-write 完成情况：
- 尚未完成项：
- 核对结论：complete | partial | reopen
- 下次复核点：
- 负责人 / 下一步：
```

## 五、使用规则

- `must-write` 只要缺一项，就不能判为 `complete`
- 若命中发生在已发布内容，至少同步 `threads-risk-incident-log.md`
- 若命中影响当前排期或栏目边界，至少同步 `threads-weekly-content-schedule.md` 或 `threads-column-lifecycle-assessment.md`
- 若核对结论为 `partial` 或 `reopen`，应回到 `threads-variant-trigger-auto-writeback-rules.md` 补全回写动作
- 若已完成并会长期影响表达治理，应同步 `threads-post-publish-retrospective.md`
