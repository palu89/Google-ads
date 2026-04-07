# Threads 阶段目标追踪面板

本文件用于把阶段目标变成持续跟踪，而不是只在月报或阶段复盘时回头看。

## 一、适用场景

- 阶段已经启动，需要持续看是否偏离
- 阶段切换决议已经落地，需要跟进执行效果
- 需要给周会、月报提供稳定检查点

## 二、最小追踪维度

1. 当前阶段
2. 阶段目标
3. 当前检查点
4. 领先信号
5. 滞后信号
6. 当前阻塞
7. 当前风险
8. 下次检查点

## 三、最小模板

```text
Threads 阶段目标追踪：
- 当前阶段：
- 阶段目标：
- 起始时间：
- 当前检查点：
- 领先信号：
- 滞后信号：
- 当前阻塞：
- 当前风险：
- 是否偏离：yes | no | watch
- 下次检查点：
- 下一步动作：
```

## 四、使用规则

- 每次阶段切换决议后，都应新建或更新一次本面板
- 若连续两个检查点出现明显偏离，应回到 `threads-stage-transition-decision.md`
- 周会 / 周报与月报 / 阶段复盘应优先引用本面板中的当前状态
- 若当前阶段正在做恢复后提频，应同步 `threads-content-restart-cadence-escalation-rules.md`
- 若当前阶段正在做恢复后提频，应同时确认 `threads-cadence-escalation-failure-rollback-threshold.md`
- 若当前阶段正在做恢复后提频，应同步 `threads-cadence-escalation-column-stepup-order.md`
- 若当前阶段已明确准备退出，应同步 `threads-account-stage-exit-checklist.md`
- 若新阶段已经跑过至少一个检查点，应判断是否需要 `threads-account-stage-migration-retrospective.md`
