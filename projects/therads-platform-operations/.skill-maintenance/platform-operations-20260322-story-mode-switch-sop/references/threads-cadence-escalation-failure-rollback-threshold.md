# Threads 节奏升级失败回退阈值

本文件用于在节奏升级过程中，提前定义什么信号一出现就必须回退，避免“再撑一下”把恢复期又拖回失控。

## 一、适用场景

- 已进入 `threads-content-restart-cadence-escalation-rules.md`
- 正在从低频恢复到更高频
- 需要明确升级失败的红线
- 想让团队在失控前就执行回退

## 二、阈值结论

- `watch-threshold`
- `rollback-threshold`

## 三、最小判断维度

1. 哪些信号一出现就说明升级过快
2. 审稿、排期、风险事件各自的失衡阈值是什么
3. 哪些栏目 / persona 优先回退
4. 回退后要回到哪个节奏级别
5. 什么时候才能重新尝试升级

## 四、最小模板

```text
Threads 节奏升级失败回退阈值：
- 关联升级方案：
- 当前节奏级别：
- 观察窗口：
- watch 阈值：
- rollback 阈值：
- 优先回退栏目 / persona：
- 回退后目标节奏：
- 重新尝试升级条件：
- 需同步更新的文件：
```

## 五、使用规则

- 回退阈值要在升级前就定义，不是出事后补写
- 只要命中 `rollback-threshold`，应立即执行回退
- 回退后应同步 `threads-weekly-content-schedule.md` 与 `threads-account-weekly-ops-report.md`
- 若回退后仍持续恶化，应回到 `threads-account-content-restart-threshold.md`
- 若跨到多周频率升级，应和 `threads-multiweek-content-cadence-stress-test.md` 一起使用
