# Threads 账户矩阵总表

本文件用于正式定义 `10` 账户矩阵。

## 一、使用规则

- 不允许 `10` 个账户定位完全重复
- 每个账户必须有清晰角色
- 每个账户必须有主线与副线
- 每个账户必须明确当前阶段状态

## 二、建议矩阵

| slot | account_id | account_type | role | primary_persona | backup_persona | primary_track | secondary_track | target_frequency | growth_goal | priority_tier | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | brand-core-01 | 主品牌号 | 总定位 / 信任背书 |  |  |  |  |  |  | P1 | draft |
| 2 | vertical-ai-01 | 垂类号 | AI 主线深耕 |  |  |  |  |  |  | P1 | draft |
| 3 | vertical-semi-01 | 垂类号 | 半导体主线深耕 |  |  |  |  |  |  | P1 | draft |
| 4 | vertical-macro-01 | 垂类号 | 宏观 / 产业主线 |  |  |  |  |  |  | P2 | draft |
| 5 | persona-veteran-01 | 人设号 | 老兵 / 经验型叙事 |  |  |  |  |  |  | P1 | draft |
| 6 | persona-data-01 | 人设号 | 数据 / 理性框架 |  |  |  |  |  |  | P2 | draft |
| 7 | persona-hotblood-01 | 人设号 | 情绪 / 热点感受 |  |  |  |  |  |  | P2 | draft |
| 8 | fastreact-news-01 | 快反号 | 新闻快反 |  |  |  |  |  |  | P2 | draft |
| 9 | fastreact-market-01 | 快反号 | 盘面快反 |  |  |  |  |  |  | P3 | draft |
| 10 | experiment-lab-01 | 实验号 | 新钩子 / 新栏目实验 |  |  |  |  |  |  | P3 | draft |

## 三、字段说明

- `account_type`：主品牌号 / 垂类号 / 人设号 / 快反号 / 实验号
- `role`：该号存在的唯一理由
- `primary_persona`：当前主 persona
- `backup_persona`：需要回退时使用
- `primary_track`：当前主线
- `secondary_track`：当前副线
- `target_frequency`：建议周发帖频率
- `growth_goal`：该号最主要增长目标
- `priority_tier`：`P1 / P2 / P3`
- `status`：`draft / ready / active / paused`

## 四、通过标准

通过前必须满足：

- 所有 `10` 个 slot 都有明确 `account_type`
- 所有 `P1` 账号都有明确 `primary_track`
- 没有两个账号的 `role + primary_track` 完全相同
- 至少 `2-3` 个账号可进入 `ready`
