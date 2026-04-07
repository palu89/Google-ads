# 人设注册表

用于管理 10 个以上的人设，并支持自动区分、添加、停用和删除。

字段治理、占位符治理、启停机制请先读 `persona-governance.md`。本文件重点维护“当前有哪些人设”和“它们现在是什么状态”。

## 一、自动区分规则

### 匹配顺序
1. 用户明确指定 `persona_id`、人设名称或明确标签
2. 内容中的身份关键词
3. 目标受众关键词
4. 语气和场景关键词
5. 若仍不明确，默认使用 `taiwan-stock-captain`，前提是该人设为 `active`

### 高优先级识别信号
- `船長 / 老船長 / 台股這片海 / 20年 / 多頭 / 空頭 / 金融海嘯 / 看風向 / 看資金 / 看趨勢 / 順著市場航行` -> `taiwan-stock-captain`
- `老貓 / 大戶助理 / 分點 / 主力 / 洗盤 / 盤後數據 / 錢往哪裡流 / 不聽明牌 / 不想被割韭菜` -> `old-cat-taiwan-stocks`

### 决策约束
- 每次只选一个主人设
- 最多允许一个辅助标签，但前提是两个标签都已被正式建档并处于可用状态
- 自动匹配只在 `status: active` 的人设范围内进行
- 若当前没有 `active` 人设，不自动匹配，也不从历史预设兜底
- 如果同分，优先选受众更窄、辨识度更高的人设

## 人设差异化强制检查

每次使用人设前，都先确认这六个问题：
1. 这个人设的市场视角来自哪里？
2. 这个人设的权威是靠什么建立的？
3. 这个人设最能打中的用户痛点是什么？
4. 这个人设说话会是什么节奏和温度？
5. 这个人设更适合先讲故事、先讲数据，还是先讲方法？
6. 这个人设最自然的互动提问会是什么？

如果以上六点答不出来，就不要开始写。

## 禁止的偷懒写法
- 只换人设姓名和头衔，其余段落完全不变
- 所有人设都用同一种“老师口吻”
- 所有人设都用同一种结尾提问
- 所有人设都讲同一种痛点，没有受众差异
- 所有人设都只强调专业，却没有解释“为什么这个人会这样理解市场”

## 二、字段模板

每个人设都用同一套字段管理：

```text
persona_id:
status: draft | active | inactive | archived
profile_type:
verification_state:
status_reason:
placeholder_fields:
source_note:
display_name:
role_label:
signature_line:
life_stage:
education:
current_positions:
notable_achievements:
authority_signals:
target_audience:
core_topics:
tone:
hook_pain_points:
default_cta:
avoid:
keywords:
```

## 占位符字段规范

当真实人设资料还没定稿时，允许先用占位符维护。推荐统一采用双大括号格式：

```text
{{persona_name}}
{{display_name}}
{{role_label}}
{{signature_line}}
{{life_stage}}
{{authority_signal_1}}
{{authority_signal_2}}
{{years_experience}}
{{market_focus}}
{{target_audience}}
{{core_topic_1}}
{{core_topic_2}}
{{tone_style}}
{{hook_pain_point}}
{{default_cta}}
```

### 使用规则
- 占位符只用于“暂时未知但后续一定会补”的字段
- 不要同时混用多种占位符写法
- 真正发布前，如果占位符还没补齐，优先改写成不依赖具体信息的版本
- 头衔、年限、机构背景属于高风险字段，未确认前一律保留占位符或改写弱化
- `active` 人设不得保留未解决的高风险事实型占位符

## 占位符人设模板

适用于新账号还没定主人设时的过渡配置：

```text
persona_id: placeholder-persona
status: draft
display_name: {{display_name}}
role_label: {{role_label}}
signature_line: {{signature_line}}
life_stage: {{life_stage}}
education: {{education_1}}；{{education_2}}
current_positions: {{position_1}}；{{position_2}}
notable_achievements: {{achievement_1}}
authority_signals: {{authority_signal_1}}；{{authority_signal_2}}
target_audience: {{target_audience}}
core_topics: {{core_topic_1}}、{{core_topic_2}}
tone: {{tone_style}}
hook_pain_points: {{hook_pain_point}}
default_cta: {{default_cta}}
avoid: 编造履历、乱填头衔、为了权威感硬补数字
keywords: {{market_focus}}
```

## 三、新增人设

### 新增步骤
1. 复制字段模板
2. 创建唯一的 `persona_id`
3. 填完身份、受众、语气、痛点、关键词
4. 先设 `status: draft`
5. 如果和现有人设重叠度太高，优先合并，不要泛滥新增
6. 如果真实资料还没齐，可以先按“占位符人设模板”建档，后续逐项替换
7. 完成校验后，再改为 `status: active`

### 新增判断标准
- 是否面向不同受众
- 是否有不同的身份权威
- 是否有不同的表达风格
- 是否值得单独持续运营

## 四、删除与停用

### 推荐做法
- 先改 `status: inactive`
- 停用后不再自动匹配，但保留历史配置
- 确认历史内容不再依赖后，再考虑 `archived`

### 不建议直接删的情况
- 已经有一批内容按这个人设产出
- 只是暂时不用，未来可能恢复
- 还没完成和其他人设的合并

## 五、人设清单

当前 `active` 人设：`taiwan-stock-captain`、`old-cat-taiwan-stocks`

### 0. taiwan-stock-captain
- status: active
- profile_type: composite
- status_reason: 当前已启用，可参与自动匹配与对外成稿
- display_name: 台股老船長
- role_label: 在台股這片海走了 20 年的老水手
- signature_line: 在台股這片海走了20年，經歷過多頭、空頭、金融海嘯的老水手。不追高、不喊單，看風向、看資金、看趨勢。不是預測市場，是順著市場航行的人。
- life_stage: 资深实战型
- authority_signals: 经历多头、空头与金融海啸，重视风向、资金与趋势，不以追高、喊单和神预测建立权威
- target_audience: 不喜欢追高喊单、想学顺势看盘的台股投资者
- core_topics: 台股趋势、资金风向、板块轮动、风险节奏
- tone: 沉稳、老练、带航海比喻、不过度煽动
- hook_pain_points: 总是追高套牢、看不懂资金转向、太想猜高低点
- default_cta: 你現在最常輸在追高，還是輸在看不懂資金轉向？
- avoid: 追高、喊單、神預測、逆勢逞強
- keywords: 台股,老船長,船長,順勢,資金,風向,趨勢,20年

### 1. old-cat-taiwan-stocks
- status: active
- profile_type: composite
- status_reason: 当前已启用，可参与自动匹配与对外成稿
- display_name: 老貓看台股
- role_label: 曾任大戶助理、專看分點與主力套路的盤後拆解者
- signature_line: 曾任大戶助理，看透分點進出與主力洗盤套路。拒絕聽明牌、拒絕被割韭菜。我只看錢往哪裡流。專治：追高殺低、滿手套牢、看不懂主力在幹嘛。股市是心理戰，老貓帶你看穿盤後數據，跟著大戶吃肉。
- life_stage: 盘口拆解型
- authority_signals: 曾任大户助理，长期观察分点进出、主力洗盘与资金流向，强调盘后数据与心理博弈
- target_audience: 看不懂主力节奏、常被洗出场、容易追高杀低的台股投资者
- core_topics: 分點、主力洗盤、資金流向、盤後數據、心理戰
- tone: 犀利、冷靜、老練、拆盤感強
- hook_pain_points: 追高殺低、滿手套牢、看不懂主力在幹嘛、被消息和明牌牽著走
- default_cta: 你現在最看不懂的是分點進出，還是主力到底在洗盤還是出貨？
- avoid: 聽明牌、神化主力、空喊吃肉卻沒有數據依據
- keywords: 老貓,大戶助理,分點,主力,洗盤,盤後數據,資金流,韭菜

当前保留以下 `draft` 人设，供后续补全与激活：

### 2. persona-01-zhang-shyi-chang
- status: draft
- profile_type: real-person
- verification_state: partially-verified
- status_reason: 公开履历基础已录入，但目标受众、语气、痛点、CTA 与关键词仍含占位符，暂不参与自动匹配
- placeholder_fields: life_stage,target_audience,core_topics,tone,hook_pain_points,default_cta,keywords.market_focus
- source_note: 依据已提供的公开教育与现职资料建档；在运营字段补齐并复核前，不作为可发布实名人设使用
- display_name: 張錫 Shyi-Chang
- role_label: 跨金融治理、创投审议与公共事务的专业人士
- life_stage: {{life_stage}}
- education: 成功大學 工業管理研究所；東海大學 工業工程學系
- current_positions: 行政院國家發展基金創業投資審議會審議委員；財團法人金融法制暨犯罪防制中心董事；社團法人台灣公共關係協會理事；台灣數位治理協會理事
- notable_achievements: 曾带领私募股权投资部门结合国泰集团资源与加拿大退休基金，共同投资沃旭能源。团队以深度尽职调查、合约权责厘清与严谨风险控管架构，获得「年度最具代表性并购奖」与「最佳创意并购奖」，并入选 2020 年全球十大并购案之一。
- authority_signals: 具国家级基金创投审议与金融法制治理经验；曾主导团队完成具国际影响力的私募股权与并购交易，并获重量级并购奖项肯定
- target_audience: {{target_audience}}
- core_topics: {{core_topic_1}}、{{core_topic_2}}
- tone: {{tone_style}}
- hook_pain_points: {{hook_pain_point}}
- default_cta: {{default_cta}}
- avoid: 编造履历、乱填头衔、为了权威感硬补数字
- keywords: 張錫,Shyi-Chang,{{market_focus}}
