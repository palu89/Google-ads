# Threads 栏目冷却期解封检查清单

本文件用于在栏目经过冷却或冻结后，判断它是否真的能恢复，而不是时间到了就自动解封。

## 一、适用场景

- 某栏目已完成既定冷却周期
- 团队想判断栏目能否恢复到周排期
- 栏目曾因平台、审稿或声誉风险进入冻结
- 需要在“继续冻结 / 限制恢复 / 正式解封”之间做决定

## 二、解封结论

- `extend-cooldown`
- `limited-release`
- `release`

## 三、最小判断维度

1. 冷却周期是否真正完成
2. 原风险信号是否明显下降
3. 高风险表达是否已清理或替换
4. 当前阶段是否允许该栏目重新进入主线
5. 解封后第一轮的节奏和限制是什么

## 四、最小模板

```text
Threads 栏目冷却期解封检查：
- 栏目名称：
- 原冷却等级：
- 冷却周期完成情况：
- 原风险信号：
- 当前剩余风险：
- 已清理表达 / 已替换方案：
- 解封结论：extend-cooldown | limited-release | release
- 解封后第一轮限制：
- 回退条件：
- 需同步更新的文件：
```

## 五、使用规则

- 未完成冷却周期，不进入 `release`
- `limited-release` 默认先走一轮低频观察，不直接恢复主力位置
- 解封前应确认 `threads-recurring-high-risk-expression-blacklist.md` 中相关表达已处理
- 解封结论应同步 `threads-weekly-content-schedule.md`
- 若解封结论是 `limited-release` 或 `release`，应同步 `threads-column-release-first-round-schedule.md`
- 若解封后再次重复出问题，应回到 `threads-high-risk-column-cooldown-rules.md`
