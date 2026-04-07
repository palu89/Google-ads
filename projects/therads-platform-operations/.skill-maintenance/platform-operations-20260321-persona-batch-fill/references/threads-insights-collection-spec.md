# Threads Insights 回收规格

本文件用于定义多账号运营下的 insights 回收字段。

## 一、账号层指标

- `followers_count`
- `profile_visits`
- `period_start`
- `period_end`

## 二、帖子层指标

- `views`
- `likes`
- `replies`
- `reposts`
- `quotes`
- `clicks`

## 三、组合层比较字段

- `account_id`
- `post_id`
- `content_module`
- `content_track`
- `persona_id`
- `hook_id`
- `publish_date`
- `priority_tier`
- `experiment_tag`

## 四、回写原则

- 账号层和帖子层必须能关联
- 组合层比较必须能追到 persona、module 和 hook
- 没有统一字段，就无法做组合级学习

## 五、Batch 01 目标

`Batch 01` 只要求把字段和比较口径定下来。

不要求：

- 自动化 KPI 面板
- 复杂预测模型
- 大规模实验统计
