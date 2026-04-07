# Threads 高风险栏目冷却期规则

本文件用于处理“某栏目不是立刻退场，但短期内不该继续高频推进”的情况。

## 一、适用场景

- 同一栏目连续出现高风险表达
- 某栏目连续触发平台、审稿或声誉风险
- 某栏目需要先降频观察，而不是直接停用
- 想给高风险栏目设一个明确冷却期

## 二、冷却等级

- `soft`
- `hard`
- `freeze`

## 三、最小判断维度

1. 风险是否连续重复
2. 当前栏目是否仍有保留价值
3. 当前阶段是否允许继续试错
4. 冷却期间是否需要替代栏目
5. 是否存在需要进入表达黑名单的复发风险
6. 什么条件下可以解除冷却

## 四、最小模板

```text
Threads 高风险栏目冷却期：
- 栏目名称：
- 当前阶段：
- 当前风险信号：
- 冷却等级：soft | hard | freeze
- 冷却周期：
- 冷却期间允许动作：
- 冷却期间禁止动作：
- 替代栏目 / 替代动作：
- 解除条件：
```

## 五、使用规则

- 冷却期内不得把该栏目继续当正常主力推进
- `freeze` 状态下不得进入周排期
- 冷却决定应同步更新 `threads-weekly-content-schedule.md`
- 若冷却期间仍需承接原栏目目标，应同步 `threads-column-replacement-options-template.md`
- 若风险来自同类高风险表达连续复发，应同步 `threads-recurring-high-risk-expression-blacklist.md`
- 若栏目准备结束冷却或冻结，应同步 `threads-column-cooldown-release-checklist.md`
- 若冷却后仍重复出问题，应回到 `threads-column-lifecycle-assessment.md`
