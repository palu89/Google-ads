# Threads 内容重启后节奏升级规则

本文件用于在账号已经进入 `guarded-restart`、`phased-restart` 或初步恢复后，判断节奏怎么一级一级往上加，而不是直接跳回旧强度。

## 一、适用场景

- 已完成 `threads-account-content-restart-threshold.md`
- 内容已经恢复，但需要判断是否继续提频
- 想从保守恢复进入稳定恢复
- 需要给周排期一个可执行的升级边界

## 二、升级结论

- `hold-current`
- `step-up`
- `maintain-watch`
- `rollback`

## 三、最小判断维度

1. 当前重启级别是否已稳定跑完一个观察窗口
2. 当前节奏下是否仍有风险回潮
3. 审稿和排期是否能承接更高节奏
4. 哪些栏目 / persona 允许先升级
5. 升级失败时如何快速回退

## 四、最小模板

```text
Threads 内容重启后节奏升级：
- 关联事件：
- 当前重启级别：
- 已稳定窗口：
- 当前周频 / 节奏：
- 候选升级节奏：
- 允许先升级的栏目 / persona：
- 当前剩余风险：
- 升级结论：hold-current | step-up | maintain-watch | rollback
- 回退触发条件：
- 下次复核点：
```

## 五、使用规则

- 未跑完一个稳定窗口，不进入 `step-up`
- 每次只升一级，不直接从保守恢复跳到高频
- 升级结论应同步 `threads-weekly-content-schedule.md` 与 `threads-stage-goal-tracker.md`
- 升级前应同步 `threads-cadence-escalation-column-stepup-order.md`
- 多 persona 场景下，升级前应同步 `threads-cadence-escalation-persona-stepup-order.md`
- 升级前应同步 `threads-cadence-escalation-failure-rollback-threshold.md`
- 若准备跨到更长周期或更高周频，应补 `threads-multiweek-content-cadence-stress-test.md`
- 若升级后再次失控，应回到 `threads-cadence-runaway-rollback-checklist.md`
