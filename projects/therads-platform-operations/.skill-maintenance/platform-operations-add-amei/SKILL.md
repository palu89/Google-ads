---
name: platform-operations
description: 台股平台运营全流程 skill。用于人物包装、交易心理教育、每日早评、盘中跟踪、盘后复盘、晚间课程，以及宏观新闻整合、单股深度分析和 Threads 平台合规审核。
---

# 台股平台运营

用于围绕台湾股票市场账号做整套内容生产与分析。这个 skill 不是单一写作模板，而是一套连续工作流：

`P0 人设包装 -> P1 方法论内容 -> P2 每日早评 -> P3 盘中跟踪 -> P4 盘后复盘 -> P5 晚间课程`

## 何时使用
- 用户要搭建或运营台股财经账号。
- 用户要写人物包装、简介、置顶文、个人理念。
- 用户要产出交易心理、趋势判断、选股方法等教育内容。
- 用户要做每日早评、盘中跟踪、盘后总结、次日预判。
- 用户提到某个热点板块或单一股票，需要深入到基本面、技术面、成交量和价位。
- 用户要分析 Threads 平台规则、账号合规风险、文案违规风险，或想做发布前审稿。

## 总原则
- 默认语气为台湾本地口语化、温暖、有金融历练，但不油滑。
- 先讲逻辑，再讲观点；先讲条件，再讲价位。
- 不写机械喊单句式，统一使用：`观察区间`、`分批布局区间`、`突破确认价`、`失效位`。
- 任何涉及“今天、最新、实时、盘中、当日新闻”的内容，都要先核实最新信息与具体日期。
- 盘面分析统一遵循：`宏观 -> 大盘 -> 板块 -> 龙头 -> 个股 -> 价位 -> 风险`
- 所有帖文都必须具备：`痛点切入`、`利他价值`、`互动收尾`
- 任何输出都不能写成“看了和没看一样”的信息搬运；必须让用户带走一个判断、方法、提醒或讨论点
- 不同人设必须体现不同的底层逻辑，不能只替换姓名、头衔或少量措辞就复用同一篇结构
- 写作前先明确该人设的：`身份出发点`、`权威来源`、`目标受众`、`核心痛点`、`语气风格`、`互动方式`
- 每篇内容输出前，必须执行一次 `内容去重审核`
- 每篇内容都必须通过 `内容连续性检查`，确保与前文、当日其他帖文和下一步内容形成链路
- 所有面向 Threads 的成稿，在发布前都要区分：`会被移除的违规`、`不会移除但会降推荐的内容`、`平台允许但有商业/声誉风险的表达`
- 任何合规判断都要优先引用官方规则；如果依据来自跨 Meta 平台的推断，必须标记为 `Inference`
- 所有面向 Threads 的成稿，在交付“可发布”结论前，都要执行一次 `发布前强制链路`
- 任何对 skill 本身的维护，都优先写入合适的 `references/*.md` 或校验脚本，不把细碎规则堆进 `SKILL.md`
- 每次维护 skill 后，都要运行 `scripts/validate_platform_operations.py` 并更新 `CHANGELOG.md`
- 涉及 Threads 规则口径、人设自动匹配门槛、审稿模板的改动，视为高影响改动，必须说明影响范围

## 路由规则
1. skill 维护、校验、升级建议、变更记录：读取 `references/skill-validation.md`、`references/persona-governance.md`、`CHANGELOG.md`；如涉及 Threads 规则，再补读 `references/threads-review-workflow.md`、`references/threads-platform-rules.md`、`references/threads-account-compliance.md`、`references/threads-copy-compliance.md`
2. 人设、简介、置顶文、价值观：读取 `references/p0-persona-branding.md`、`references/persona-governance.md`、`references/persona-registry.md`、`references/tone-style-tw.md`、`references/content-performance.md`、`references/content-dedup-audit.md`、`references/content-continuity.md`、`references/threads-copy-compliance.md`
3. 交易心理、趋势判断、选股教学：读取 `references/p1-trading-psychology.md`、`references/tone-style-tw.md`、`references/content-performance.md`、`references/content-dedup-audit.md`、`references/content-continuity.md`、`references/threads-copy-compliance.md`
4. 每日早评早报：读取 `references/p2-morning-brief.md`、`references/macro-news-synthesizer.md`、`references/content-performance.md`、`references/content-dedup-audit.md`、`references/content-continuity.md`、`references/threads-copy-compliance.md`，如提到个股再读 `references/single-stock-deepdive.md`
5. 盘中跟踪：读取 `references/p3-intraday-tracker.md`、`references/content-performance.md`、`references/content-dedup-audit.md`、`references/content-continuity.md`、`references/threads-copy-compliance.md`，必要时加读 `references/macro-news-synthesizer.md` 与 `references/single-stock-deepdive.md`
6. 盘后复盘：读取 `references/p4-postmarket-recap.md`、`references/content-performance.md`、`references/content-dedup-audit.md`、`references/content-continuity.md`、`references/threads-copy-compliance.md`，必要时加读 `references/macro-news-synthesizer.md` 与 `references/single-stock-deepdive.md`
7. 晚间课程：读取 `references/p5-evening-lessons.md`、`references/content-performance.md`、`references/content-dedup-audit.md`、`references/content-continuity.md`、`references/threads-copy-compliance.md`，并优先衔接白天盘面案例
8. Threads 平台规则、账号合规、文案违规审查、发布前审稿：读取 `references/threads-review-workflow.md`、`references/threads-platform-rules.md`、`references/threads-account-compliance.md`、`references/threads-copy-compliance.md`、`references/content-dedup-audit.md`、`references/content-continuity.md`

## 发布前强制链路
1. 先读 `references/threads-review-workflow.md`
2. 判断平台底线：`references/threads-platform-rules.md`
3. 涉及头像、名称、Bio、Link、实名权威背书时，补读 `references/threads-account-compliance.md`
4. 审文案本身：`references/threads-copy-compliance.md`
5. 做去重：`references/content-dedup-audit.md`
6. 做连续性检查：`references/content-continuity.md`

## 多人设管理
- 多人设场景下，先读取 `references/persona-governance.md`，再读取 `references/persona-registry.md`
- 默认只选择 `1 个主人设`，最多叠加 `1 个辅助标签`，避免风格混乱
- 自动区分顺序：`用户明确指定的人设 id/名称` -> `内容中的身份关键词` -> `目标受众与语气信号` -> `最接近的 active 人设`
- 自动匹配只在 `status: active` 的人设范围内进行；`draft`、`inactive`、`archived` 不参与默认选择
- 若当前没有 `active` 人设，不自动从旧预设兜底；只输出结构版、测试版，或先建立新 persona
- 若两个候选人设分数接近，优先选择受众更窄、定位更清晰的那个
- 新增人设时，先按注册表模板补全字段并设为 `status: draft`，完成校验后再激活
- 删除人设时，优先改为 `status: inactive`，确认历史内容不再依赖后再考虑归档
- 若用户要求“先用占位符”，则保留占位符，不擅自编造履历、头衔、年限、公司背景
- 当占位符仍未补全时，优先输出“结构完整但可后填”的版本，并把高风险信息写成变量
- 若指定人设不是 `active`，只能输出模板版、测试版或内部草稿，不直接给“可发布”结论

## 固定分析链路
1. 全球宏观：美股、费半、美债收益率、美元指数、原油、黄金、联准会预期、地缘政治
2. 台湾宏观：台币汇率、台湾经济数据、政策变化、台指期、ADR
3. 新闻主线：前一日与当日新闻，区分宏观、产业、公司
4. 大盘结构：加权指数、OTC、成交额、涨跌家数、法人、权值股
5. 热点板块：板块强弱、扩散还是集中、持续性
6. 龙头与热点股：龙头、跟涨、补涨、情绪股
7. 个股深挖：基本面、消息面、技术面、量价面、筹码面
8. 交易计划：观察区间、分批布局区间、突破确认价、失效位

## 输出约束
- 人设内容先建立可信度，再输出具体文案。
- 教育内容先讲错误，再讲修正方法。
- 早评、盘中、盘后都要明确：主线、变动、风险、下一步看点。
- 单股分析必须说明“为什么是它”，不能只列指标。
- 第一段优先抓痛点、误区、损失感或错失感，让用户一眼知道“这和我有关”。
- 中段必须提供可带走的方法、判断框架或可执行提醒。
- 结尾优先留下互动钩子，推动评论、转发、二次讨论。
- 避免纯资讯罗列、空泛鸡汤、只有观点没有方法、只有情绪没有结论。
- 生成人设文案前，先检查是否真的符合该人设的经历、视角和用户关系；如果换成人设名后仍然成立，说明区分度不够，需要重写
- 若和近期内容在开头、主痛点、案例、核心结论、互动问题上高度相似，必须换角度重写
- 同一天多篇内容必须分工明确、层层递进；如果删掉其中一篇不影响整体叙事，说明连续性不足
- 若观点发生变化，必须明确说明“为什么调整判断”，不能无痕切换立场
- 若使用 `draft` 人设或存在未解决高风险占位符，不输出像已核实名背书一样的成稿
- 涉及账号合规或文案审核时，输出必须区分：
  - `违规高风险`：可能触发移除、限制、封禁
  - `推荐受限风险`：内容可存在，但可能影响推荐与增长
  - `低风险优化项`：规则允许，但不利于信任、转化或品牌
- 对财经文案，`不构成投资建议` 不是免责护身符；如果正文承诺收益、制造误导或鼓励冲动交易，仍应判为高风险

## 资源导航
- `references/tone-style-tw.md`：台湾口语、成熟金融前辈语气、平台表达风格
- `references/content-performance.md`：痛点、利他、互动与避免低流量空帖的内容标准
- `references/content-dedup-audit.md`：内容去重审核规则，避免重复开头、结构、案例和互动
- `references/content-continuity.md`：内容连续性规则，确保前后文衔接、同日分工和系列推进
- `references/persona-governance.md`：多人设字段治理、占位符规则、启停机制与自动匹配门槛
- `references/threads-review-workflow.md`：Threads 发布前审稿顺序、分级与统一输出模板
- `references/threads-platform-rules.md`：Threads 平台规则与 Meta 官方政策映射
- `references/threads-account-compliance.md`：账号层合规与违规排查
- `references/threads-copy-compliance.md`：文案层合规、违规、降推荐与改写方案
- `references/p0-persona-branding.md`：人物包装与账号定位
- `references/persona-registry.md`：当前人设清单、状态与基础资料
- `references/p1-trading-psychology.md`：交易心理、趋势判断、选股教学
- `references/p2-morning-brief.md`：每日早评早报模板
- `references/p3-intraday-tracker.md`：盘中跟踪模板
- `references/p4-postmarket-recap.md`：盘后复盘模板
- `references/p5-evening-lessons.md`：晚间教育内容模板
- `references/macro-news-synthesizer.md`：宏观和新闻归纳方法
- `references/single-stock-deepdive.md`：单股基本面与技术面拆解框架
- `references/skill-validation.md`：skill 结构、规则、状态与变更记录的校验标准
- `CHANGELOG.md`：skill 升级记录、影响范围与校验结论
