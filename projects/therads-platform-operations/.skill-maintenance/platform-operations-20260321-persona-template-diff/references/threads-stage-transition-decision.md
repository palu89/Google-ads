# Threads 阶段切换决议模板

本文件用于把“感觉该换阶段了”变成正式决议，而不是口头判断。

适合处理：

- 是否继续当前阶段
- 是否收紧
- 是否切换主线
- 是否暂停

## 一、适用场景

- 月报后要正式下结论
- 阶段目标明显完成或明显失真
- persona 或栏目需要整体转向
- 风险事件导致阶段策略要重置

## 二、决议类型

- `continue`
- `tighten`
- `switch`
- `pause`

## 三、最小判断维度

1. 当前阶段目标是否仍成立
2. 当前有效模式是否还能放大
3. 当前失效模式是否已足够明显
4. 当前风险是否允许继续
5. 若切换，影响范围有多大

## 四、最小模板

```text
Threads 阶段切换决议：
- 当前阶段：
- 决议类型：continue | tighten | switch | pause
- 触发原因：
- 当前有效模式：
- 当前失效模式：
- 影响范围：
- 生效时间：
- 回退条件：
- 下一步动作：
```

## 五、使用规则

- 决议必须有生效时间
- `switch` 和 `pause` 必须写回退条件
- 若影响 persona 或栏目，必须同步更新对应治理文件
- 决议生效后，应同步新建或更新 `threads-stage-goal-tracker.md`
- 若当前决议意味着旧阶段正式结束，应同步 `threads-account-stage-exit-checklist.md`
- 若新阶段会改变内容投入重心，应同步 `threads-account-primary-secondary-track-ratio.md`
- 若新阶段准备提高周频或拉长节奏，应同步 `threads-multiweek-content-cadence-stress-test.md`
