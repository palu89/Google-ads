# Threads 多 Persona 轮值排班模板

本文件用于在同一账号存在多个 persona 时，安排谁在什么时段、什么栏目、什么批次里出场，避免临时抢位。

## 一、适用场景

- 同一账号有 2 个以上可用 persona
- 一周内容需要多 persona 分工
- 想验证辅助 persona，但不想打乱主 persona 主线
- 某些栏目只允许特定 persona 承接

## 二、最小判断维度

1. 默认主 persona 是谁
2. 哪些时间槽位必须由主 persona 承接
3. 哪些栏目允许辅助 persona 轮值
4. 何时允许临时换班
5. 轮值失败时怎么回退

## 三、最小模板

```text
Threads 多 Persona 轮值排班：
- 当前周期：
- 默认主 persona：
- 参与轮值 persona：
- 主 persona 固定槽位：
- 辅助 persona 试运行槽位：
- 禁止混用栏目：
- 临时换班条件：
- 回退顺序：
- 本周期观察重点：
```

## 四、使用规则

- 同一时间槽位只能有一个当前负责 persona
- 主 persona 的核心栏目不得被辅助 persona 长期替代
- 轮值安排应同步更新 `threads-weekly-content-schedule.md`
- 若轮值导致风格混乱，应回到 `multi-persona-coexistence-governance.md`
- 若轮值出现抢槽位或抢栏目的情况，应同步 `threads-multi-persona-conflict-arbitration.md`
