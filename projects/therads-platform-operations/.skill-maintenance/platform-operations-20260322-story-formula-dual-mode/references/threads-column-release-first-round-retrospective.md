# Threads 栏目解封后首轮复盘模板

本文件用于在栏目完成解封后的第一轮恢复排期后，判断它是可以继续放开、继续限制，还是应该重新回到冷却状态。

## 一、适用场景

- 已执行 `threads-column-release-first-round-schedule.md`
- 首轮恢复排期已经结束
- 需要判断栏目能否从“首轮恢复”进入“稳定恢复”
- 想把首轮恢复结果沉淀为下一轮规则

## 二、复盘结论

- `re-cooldown`
- `keep-limited`
- `graduate`

## 三、最小判断维度

1. 首轮恢复是否达到原定成功信号
2. 首轮期间是否出现风险回潮
3. 当前栏目是否仍需限制角度和频次
4. 哪些表达和栏位仍然不能放开
5. 下一轮应进入什么强度

## 四、最小模板

```text
Threads 栏目解封后首轮复盘：
- 栏目名称：
- 首轮周期：
- 首轮执行情况：
- 首轮有效信号：
- 首轮风险信号：
- 当前仍需限制的点：
- 复盘结论：re-cooldown | keep-limited | graduate
- 下一轮建议：
- 回写文件：
```

## 五、使用规则

- 首轮复盘不是看“有没有发完”，而是看“是否稳定恢复”
- 若首轮恢复就出现风险回潮，应优先 `re-cooldown`
- 若只能维持低频和受限角度，应选择 `keep-limited`
- 若准备进入更稳定恢复，应同步 `threads-column-cooldown-release-checklist.md` 与 `threads-weekly-content-schedule.md`
- 若复盘结论为 `re-cooldown`，应同步 `threads-column-release-failure-recooldown-sop.md`
- 若首轮复盘要进入阶段结论，应同步 `threads-post-publish-retrospective.md`
