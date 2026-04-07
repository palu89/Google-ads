# Threads 发帖与回写规格

本文件用于定义多账号运营下的发帖输入、输出和失败回写字段。

## 一、发帖输入字段

- `account_id`
- `persona_id`
- `content_module`
- `content_track`
- `hook_id`
- `title`
- `body`
- `cta`
- `review_status`
- `scheduled_at`
- `operator`

## 二、发帖输出字段

- `publish_status`
- `published_at`
- `thread_post_id`
- `thread_url`
- `final_persona_id`
- `final_hook_id`

## 三、失败回写字段

- `failure_stage`
- `failure_reason`
- `retryable`
- `retry_after`
- `manual_action_required`
- `incident_log_ref`

## 四、前置条件

发帖前必须满足：

- 已通过审稿
- persona 已确认
- hook 已确认
- 账号状态不是 `paused`
- 同批次无明显去重冲突

## 五、Batch 01 目标

`Batch 01` 只定义字段与边界，不直接做 API 批量自动发帖。
