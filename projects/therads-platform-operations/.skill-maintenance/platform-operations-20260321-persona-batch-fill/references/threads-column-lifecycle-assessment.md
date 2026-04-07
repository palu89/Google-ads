# Threads 栏目生命周期评估模板

本文件用于判断一个栏目该继续、放大、合并、暂停还是退场，而不是长期挂着不动。

## 一、适用场景

- 某栏目连续多周表现失真
- 某栏目准备扩大投入
- 两个栏目边界开始重叠
- 阶段切换前要清理栏目结构

## 二、处理结论

- `keep`
- `expand`
- `merge`
- `pause`
- `retire`

## 三、最小判断维度

1. 当前栏目目标是否仍成立
2. 当前栏目是否仍适配主 persona
3. 当前栏目是否和其他栏目重叠
4. 当前栏目是否还能形成稳定系列
5. 当前栏目是否值得继续占用排期

## 四、最小模板

```text
Threads 栏目生命周期评估：
- 栏目名称：
- 当前阶段：
- 当前主要 persona：
- 当前状态：
- 有效信号：
- 失效信号：
- 与其他栏目重叠点：
- 处理结论：keep | expand | merge | pause | retire
- 生效时间：
- 下一步动作：
```

## 五、使用规则

- `merge` 与 `retire` 必须说明原栏目的后续去向
- 若栏目判断影响内容支柱，应同步更新 `persona-content-pillar-map.md`
- 若栏目进入退场，应同步检查 `threads-account-stage-exit-checklist.md`
- 若栏目暂不退场但连续高风险，应同步 `threads-high-risk-column-cooldown-rules.md`
- 若栏目冷却后仍需承接原目标，应同步 `threads-column-replacement-options-template.md`
- 若栏目风险重复来自同类表达，应同步 `threads-recurring-high-risk-expression-blacklist.md`
