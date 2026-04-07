# Threads 提频阶段分 Persona 升级顺序

本文件用于在账号已经允许继续提频时，判断不同 `persona` 应该按什么顺序升级，避免同一轮提频把所有人设一起放大。

## 一、适用场景

- 已执行 `threads-content-restart-cadence-escalation-rules.md`
- 当前节奏允许继续提频
- 同一账号下存在多个 `persona`
- 需要明确谁先升级、谁暂缓升级、谁只能继续观察

## 二、升级结论

- `primary-first`
- `staggered-stepup`
- `hold-secondary`

## 三、最小判断维度

1. 当前哪一个 `persona` 最稳定、最能承接升级
2. 哪些 `persona` 仍存在审稿、合规或表达风险
3. 当前栏目升级顺序与 `persona` 升级顺序是否一致
4. 哪些 `persona` 只能维持当前频率或继续观察
5. 若升级失败，先回退哪一个 `persona`

## 四、最小模板

```text
Threads 提频阶段分 Persona 升级顺序：
- 当前节奏级别：
- 当前主 persona：
- 候选升级 personas：
- 第一顺位升级：
- 第二顺位升级：
- 暂缓升级：
- 升级观察窗口：
- 失败回退顺序：
- 升级结论：primary-first | staggered-stepup | hold-secondary
- 关联文件：
```

## 五、使用规则

- 在多人设场景下，先定 `threads-cadence-escalation-column-stepup-order.md`，再定本文件
- 未通过近期审稿或仍在风险观察的人设，不进入第一顺位升级
- 若提频会影响轮值排班，应同步 `threads-multi-persona-rotation-schedule.md`
- 若提频会引发人设抢位，应同步 `threads-multi-persona-conflict-arbitration.md`
- 升级结论应同步 `threads-weekly-content-schedule.md` 与 `threads-stage-goal-tracker.md`
