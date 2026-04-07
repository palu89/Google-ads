# Threads 栏目解封后首轮排期模板

本文件用于在栏目经过冷却并通过解封检查后，给它安排第一轮恢复排期，避免一解封就直接回到旧强度。

## 一、适用场景

- 栏目已通过 `threads-column-cooldown-release-checklist.md`
- 栏目准备重新进入周排期
- 需要明确第一轮只恢复到什么强度
- 需要给解封栏目设置首轮观察窗口和限制

## 二、最小判断维度

1. 当前解封结论是 `limited-release` 还是 `release`
2. 第一轮允许发布几篇、在哪些时段
3. 哪些表达和角度仍然禁用
4. 第一轮观察窗口是什么
5. 第一轮失败时如何立即回退

## 三、最小模板

```text
Threads 栏目解封后首轮排期：
- 栏目名称：
- 当前解封结论：
- 首轮周期：
- 首轮允许篇数 / 时段：
- 首轮允许角度：
- 首轮禁止角度：
- 配套 persona：
- 观察窗口：
- 首轮成功信号：
- 首轮失败回退动作：
- 需同步更新的文件：
```

## 四、使用规则

- 首轮排期默认低于该栏目历史主力强度
- 首轮排期不等于正式恢复主力位置
- 首轮排期应同步 `threads-weekly-content-schedule.md`
- 首轮结束后应同步 `threads-column-release-first-round-retrospective.md`
- 首轮结束后应回到 `threads-post-publish-retrospective.md`
- 若首轮即再次出问题，应回到 `threads-high-risk-column-cooldown-rules.md`
