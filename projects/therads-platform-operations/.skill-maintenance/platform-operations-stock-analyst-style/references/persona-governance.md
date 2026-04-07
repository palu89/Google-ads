# 人设治理规则

本文件定义多人设的字段治理、占位符治理、启停机制和自动匹配边界。

`persona-registry.md` 负责“当前有哪些人设”，本文件负责“这些人设怎么管”。

## 一、使用顺序

涉及人设判断、增加、停用、审稿时，按以下顺序执行：
1. 先看 `status`
2. 再看是否有未解决占位符
3. 再看是否满足自动匹配条件
4. 最后才开始写作或发布前审稿

## 二、状态模型

### `draft`
- 已建立结构，但还没满足对外发布条件
- 允许存在未补齐字段、未确认风格或未完成验证的实名信息
- 不参与自动匹配
- 只可用于模板、测试、内部讨论稿

### `active`
- 可参与自动匹配
- 可用于对外发布内容
- 不允许保留未解决的高风险事实型占位符
- 必须具备完整的受众、语气、痛点、CTA 等运营字段

### `inactive`
- 暂停使用，但保留历史记录
- 不参与自动匹配
- 适合季节性、阶段性或暂时停更的人设

### `archived`
- 历史归档
- 不参与自动匹配
- 仅用于追溯旧内容或做结构参考

## 三、字段分层

### 所有人设最低必填
- `persona_id`
- `status`
- `display_name`
- `role_label`
- `target_audience`
- `core_topics`
- `tone`
- `hook_pain_points`
- `default_cta`
- `avoid`
- `keywords`

### 建议补齐
- `life_stage`
- `authority_signals`
- `signature_line`

### 实名或强背书人设建议增加
- `profile_type`
- `verification_state`
- `status_reason`
- `placeholder_fields`
- `source_note`

## 四、字段解释

### `profile_type`
- `composite`：复合型运营人设，不指向唯一真实人物
- `real-person`：直接绑定真实人物或真实公开身份
- `placeholder`：明确处于占位阶段
- `fictionalized`：允许风格化表达，但不能冒充真实不可证实身份

### `verification_state`
- `verified`：关键实名或履历信息已核对
- `partially-verified`：有公开依据，但仍有未补齐或未确认字段
- `unverified`：尚未核对，不得作为实名背书对外使用

## 五、占位符治理

### 可接受的占位符场景
- 新人设刚立项，结构先行
- 用户明确要求先保留变量
- 只做模板测试，不直接产出成稿

### 高风险事实型字段
以下字段一旦未确认，不得在 `active` 人设中保留占位符：
- `display_name`
- `role_label`
- `education`
- `current_positions`
- `notable_achievements`
- `authority_signals`
- `years_experience`

### 运营关键字段
以下字段若为空或仍是占位符，不宜进入 `active`：
- `target_audience`
- `core_topics`
- `tone`
- `hook_pain_points`
- `default_cta`
- `keywords`

### 强制规则
- `active` 人设不能含未解决的高风险事实型占位符
- `active` 人设应避免含未解决的运营关键字段占位符
- `draft` 人设若被明确指定，只能输出模板版、测试版，或先提醒“该人设未激活”

## 六、自动匹配门槛

- 自动匹配只在 `status: active` 的人设范围内进行
- `draft`、`inactive`、`archived` 一律不参与默认选择
- 若当前 `active` 人设数量为 0，停止自动匹配，不从历史预设兜底
- 若当前 `active` 人设数量为 0，只能返回“需先创建并激活人设”或输出模板版
- 若最接近的人设是 `draft`，也不能自动补成 `active`
- 若候选分数接近，优先选受众更窄、定位更清晰的 `active` 人设

## 七、生命周期

### 新增
1. 先建 `draft`
2. 补齐最低必填字段
3. 若为实名或强背书人设，补 `verification_state` 与 `source_note`
4. 满足激活条件后再改为 `active`

### 停用
1. 优先改为 `inactive`
2. 记录停用原因
3. 确认历史内容不再依赖后，再考虑 `archived`

### 重新激活
1. 先检查字段是否仍完整
2. 再检查近期内容定位是否冲突
3. 确认无占位符风险后，才可改回 `active`

## 八、与审稿的关系

- 若文案使用了 `draft` 人设，默认不能直接给“可发布”
- 若当前没有 `active` 人设，默认不能给“按既有人设可直接发布”的结论
- 若实名人设为 `partially-verified` 或 `unverified`，必须在审稿结论里写明
- 若人设字段与文案中的头衔、经历、受众不一致，按人设不一致处理，至少判为“需重写”
