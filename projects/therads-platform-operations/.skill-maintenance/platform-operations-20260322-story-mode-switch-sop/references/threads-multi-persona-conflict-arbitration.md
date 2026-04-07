# Threads 多 Persona 冲突仲裁模板

本文件用于处理多个 persona 在同一账号里抢栏目、抢时段、抢主线时的冲突，而不是临时拍脑袋决定。

## 一、适用场景

- 两个 persona 抢同一栏目
- 两个 persona 抢同一时间槽位
- 主 persona 与辅助 persona 的边界开始重叠
- 同一批次里出现“谁来讲这篇”争议

## 二、仲裁优先级

1. 当前阶段主线优先
2. 默认主 persona 优先
3. 栏目原始归属优先
4. 风险更低、边界更清晰的表达优先

## 三、最小模板

```text
Threads 多 Persona 冲突仲裁：
- 当前冲突：
- 涉及 persona：
- 涉及栏目 / 时间槽位：
- 当前阶段主线：
- 默认主 persona：
- 原始归属：
- 风险比较：
- 仲裁结论：
- 临时生效期：
- 回退条件：
```

## 四、使用规则

- 每个冲突必须有一个当前唯一结论
- 仲裁结论若影响轮值安排，应同步更新 `threads-multi-persona-rotation-schedule.md`
- 若冲突连续重复出现，应回到 `multi-persona-coexistence-governance.md`
