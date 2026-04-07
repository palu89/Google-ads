# Threads 共享钩子库框架

本文件用于定义多账号共享钩子库的骨架。

## 一、分类

必须至少包含：

- `观点钩子`
- `冲突钩子`
- `利益钩子`
- `悬念钩子`

## 二、字段

| hook_id | hook_type | opening | suitable_accounts | suitable_personas | suitable_modules | risk_level | duplication_tag | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HK-001 | 观点钩子 |  |  |  |  | low |  |  |
| HK-002 | 冲突钩子 |  |  |  |  | medium |  |  |
| HK-003 | 利益钩子 |  |  |  |  | low |  |  |
| HK-004 | 悬念钩子 |  |  |  |  | medium |  |  |

## 三、治理规则

- 同一周内，不让多个账号大量复用同一 `duplication_tag`
- 风险等级至少分：`low / medium / high`
- `high` 风险钩子必须经过更强审稿
- 每个钩子要标明适配账号类型和 persona

## 四、最小目标

`Batch 01` 只要求：

- 每种类型至少 `5` 条骨架
- 至少为 `P1` 账号预留专用钩子
- 把最容易撞车的开头先分开
