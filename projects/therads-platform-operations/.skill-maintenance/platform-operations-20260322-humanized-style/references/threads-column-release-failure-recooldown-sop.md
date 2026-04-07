# Threads 解封栏目首轮失败重新冷却 SOP

本文件用于在栏目通过解封检查并完成首轮恢复后，若首轮表现失败或风险回潮，快速把栏目拉回重新冷却，而不是继续勉强推进。

## 一、适用场景

- 已执行 `threads-column-release-first-round-retrospective.md`
- 首轮复盘结论为 `re-cooldown`
- 解封栏目在恢复首轮出现风险回潮、表达失控或节奏承接失败
- 需要明确重新冷却的强度、周期和替代承接方案

## 二、重新冷却结论

- `short-recooldown`
- `hard-freeze`
- `retire-candidate`

## 三、最小判断维度

1. 首轮失败的直接触发点是什么
2. 当前栏目是否还能保留部分受限表达空间
3. 需要重新冷却多久，还是直接进入硬冻结
4. 冷却期间由哪个替代栏目或低风险承接方案接手
5. 下次允许重新进入解封检查的门槛是什么

## 四、最小模板

```text
Threads 解封栏目首轮失败重新冷却：
- 栏目名称：
- 首轮失败信号：
- 当前风险等级：
- 重新冷却结论：short-recooldown | hard-freeze | retire-candidate
- 冷却周期：
- 冷却期间允许范围：
- 替代承接方案：
- 下次解封前置门槛：
- 必须回写文件：
- 负责人 / 复核时间：
```

## 五、使用规则

- 一旦进入 `re-cooldown`，应同步 `threads-high-risk-column-cooldown-rules.md`
- 若重新冷却会影响当前周排期，应同步 `threads-weekly-content-schedule.md`
- 若需要替代承接，应同步 `threads-column-replacement-options-template.md`
- 若同一栏目在同一阶段二次重新冷却，应同步 `threads-column-lifecycle-assessment.md`
- 下次重新尝试恢复前，必须重新执行 `threads-column-cooldown-release-checklist.md`
