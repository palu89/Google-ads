# Threads 账号恢复后观察清单

本文件用于在风险应急后进入观察期，不把“暂时恢复”误判成“彻底恢复”。

适合处理：

- 风险事件后的 24 小时观察
- 风险事件后的 72 小时观察
- 高风险恢复后的 7 天观察
- 恢复后内容节奏是否可以逐步放开

## 一、适用场景

- 已执行 `threads-account-recovery-risk-emergency-sop.md`
- 账号表面恢复，但仍需观察平台与分发信号
- 需要判断是继续保守、逐步恢复还是重新收紧

## 二、观察窗口

- `24h`：止损后初步信号
- `72h`：恢复是否稳定
- `7d`：是否可以退出观察期

## 三、最小观察维度

1. 账号状态信号
2. 内容分发信号
3. 风险重复信号
4. 队列恢复节奏
5. 是否需要继续收紧

## 四、最小模板

```text
Threads 账号恢复后观察：
- 关联事件：
- 观察窗口：24h | 72h | 7d
- 当前状态：
- 已恢复信号：
- 未恢复信号：
- 当前保守动作：
- 当前可恢复动作：
- 再次升级条件：
- 观察结论：continue-observe | gradually-resume | re-tighten
```

## 五、使用规则

- 未完成观察窗口前，不恢复高风险节奏
- 若再次触发异常，应回到 `threads-account-recovery-risk-emergency-sop.md`
- `L3` 事件默认至少覆盖一次 `7d` 观察
- 若观察结论准备进入恢复发布，应同步 `threads-account-content-restart-threshold.md`
- 若恢复发布后已稳定一个观察窗口且准备提频，应同步 `threads-content-restart-cadence-escalation-rules.md`
