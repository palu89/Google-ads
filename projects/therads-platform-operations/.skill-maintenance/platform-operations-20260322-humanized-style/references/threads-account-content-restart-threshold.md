# Threads 账号异常后内容重启门槛

本文件用于在账号异常、平台提醒或高风险应急之后，判断内容什么时候能重新启动、能恢复到什么强度，而不是凭感觉“差不多可以发了”。

## 一、适用场景

- 已执行 `threads-account-recovery-risk-emergency-sop.md`
- 已完成至少一个观察窗口
- 需要判断能否从保守状态回到稳定发布
- 需要给团队一个可执行的内容重启边界

## 二、重启结论

- `hold`
- `guarded-restart`
- `phased-restart`
- `normal-restart`

## 三、最小判断维度

1. 观察窗口是否完成
2. 账号与分发信号是否恢复
3. 高风险栏目和高风险表达是否已收紧
4. 当前允许恢复的内容范围和节奏是多少
5. 再次升级或回退条件是什么

## 四、最小模板

```text
Threads 账号异常后内容重启门槛：
- 关联事件：
- 已完成观察窗口：
- 当前账号信号：
- 当前分发信号：
- 已冻结栏目 / 禁用表达：
- 当前允许内容范围：
- 当前允许节奏上限：
- 重启结论：hold | guarded-restart | phased-restart | normal-restart
- 再次升级条件：
- 下次复核点：
```

## 五、使用规则

- 未完成观察窗口前，不进入 `normal-restart`
- `L3` 事件默认不能一步恢复到 `normal-restart`
- 重启结论应同步 `threads-weekly-content-schedule.md` 与 `threads-content-queue-ledger.md`
- 若重启后已稳定运行一个观察窗口，应同步 `threads-content-restart-cadence-escalation-rules.md`
- 若恢复后再次异常，应回到 `threads-account-recovery-risk-emergency-sop.md`
- 若恢复后仍需长期保守，应同步 `threads-stage-transition-decision.md`
