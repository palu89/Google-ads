# Threads 内容队列台账

本文件用于把内容运营从“想到什么写什么”推进到“有明确队列和状态管理”。

它不负责决定写什么，而是负责追踪：

- 哪些选题已入列
- 当前在哪个状态
- 卡在哪个环节
- 哪些篇应优先推进或暂停

## 一、适用场景

- 周内容批次执行
- 单篇较多、容易混乱
- 多个选题同时推进
- 需要统一看草稿、审稿与发布时间

## 二、使用顺序

1. 先完成 `threads-account-baseline-card.md`
2. 再完成 `threads-weekly-content-schedule.md`
3. 然后把每篇内容登记到本台账
4. 审稿与发布时，结合 `threads-review-publish-package.md`
5. 若内容属于长期系列，再同步 `threads-series-continuity-overview.md`
6. 若库存内容堆积过久，再同步 `threads-content-inventory-aging-rules.md`
7. 若旧库存准备重做再用，再同步 `threads-content-inventory-regeneration-rules.md`

## 三、状态定义

- `idea`
- `selected`
- `drafting`
- `review`
- `revise`
- `approved`
- `scheduled`
- `published`
- `recycle`
- `blocked`

## 四、最小台账模板

```text
Threads 内容队列台账：

1.
- 内容编号：
- 主题：
- persona：
- 模块：
- 本篇角色：
- 当前状态：
- 优先级：
- 计划日期：
- 审稿状态：
- 发布状态：
- 风险备注：
- 下一步动作：

2.
- 内容编号：
- 主题：
- persona：
- 模块：
- 本篇角色：
- 当前状态：
- 优先级：
- 计划日期：
- 审稿状态：
- 发布状态：
- 风险备注：
- 下一步动作：
```

## 五、使用规则

- 每篇内容只保留一个当前状态
- `review` 与 `revise` 之间来回时，要写清原因
- `blocked` 不能默默停着，必须写阻塞原因
- `published` 后若需要继续放大，应交给 `threads-post-publish-retrospective.md`
- 若内容属于某个系列，状态变化后应同步更新 `threads-series-continuity-overview.md`
- 若内容长期停在 `idea`、`selected`、`approved`，应进入 `threads-content-inventory-aging-rules.md`
- 若内容经过再生后重新入列，应在台账里体现新的入口状态

## 六、优先级建议

- `P0`：账号风险、平台风险、必须当天处理
- `P1`：当周核心支柱内容
- `P2`：辅助内容、互动内容、可顺延内容

## 七、常见错误

- 周排期写了，但没有落到台账
- 状态很多，但没人维护
- 审稿结论和发布状态分不清
- 已发布内容没有回流到复盘
