---
name: platform-operations
description: 台股 Threads 运营规则维护 skill。以 persona 治理、审稿合规、校验与变更记录为默认核心；内容模板仅在明确要求时启用。
---

# 台股平台运营

用于围绕台湾股票市场账号维护可复用的运营规则与审稿体系。当前默认不是进入整套日更写作，而是先处理：

`persona 治理 -> Threads 审稿 -> 校验脚本 -> 变更记录`

`P0-P5`、宏观整合、单股深挖等内容模板仍保留，但只在用户明确进入内容生产或模板验证时启用。

## 何时使用
- 用户要维护或重构这个 skill 本身。
- 用户要新增、修改、停用或审查 persona。
- 用户要调整 Threads 平台规则、账号合规、文案合规或发布前审稿流程。
- 用户要开始或强化 Threads 平台账户内容运营、内容排期、内容工作流或发布闭环。
- 用户要校验 skill、审查影响范围或更新变更记录。
- 用户要搭建或运营台股财经账号。
- 用户明确要求用现有模板做人物包装、方法论内容、早评、盘中、盘后、晚课或单股分析测试。

## 总原则
- 默认先走“维护核心”，不默认进入 `P0-P5` 内容模板链路。
- 任何内容输出一旦启动，必须先读 `references/content-output-enforcement.md`
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
- Threads 内容运营强化第一阶段已完成；若无真实运营痛点，不默认继续新增 reference 或扩默认主链

## 实际使用边界
- 先读 `references/usage-scope.md`
- 默认只加载“维护核心”相关 reference
- 若用户明确进入 Threads 内容运营强化，先读 `references/threads-content-operations-workflow.md`
- `P0-P5`、宏观整合、单股深挖属于 `可选内容模板包`，只有在用户明确要求内容生产、模板验证或测试样稿时才进入

## 路由规则
1. skill 维护、校验、升级建议、变更记录：读取 `references/usage-scope.md`、`references/skill-validation.md`、`references/persona-governance.md`、`references/persona-registry.md`、`CHANGELOG.md`；如涉及 Threads 规则，再补读 `references/threads-review-workflow.md`、`references/threads-platform-rules.md`、`references/threads-account-compliance.md`、`references/threads-copy-compliance.md`
2. 人设系统维护：新增、修改、停用、占位符治理、字段治理、自动匹配门槛调整时，读取 `references/usage-scope.md`、`references/persona-governance.md`、`references/persona-registry.md`、`references/skill-validation.md`、`CHANGELOG.md`；如涉及可发布性或高风险叙事，再补读 `references/threads-account-compliance.md` 与 `references/threads-copy-compliance.md`
3. Threads 平台规则、账号合规、文案违规审查、发布前审稿：读取 `references/usage-scope.md`、`references/threads-review-workflow.md`、`references/threads-platform-rules.md`、`references/threads-account-compliance.md`、`references/threads-copy-compliance.md`；如文案已经成型，再补读 `references/persona-governance.md`、`references/persona-registry.md`
4. 内容运营强化：当用户明确要开始或强化 Threads 平台账户内容运营时，先读取 `references/usage-scope.md`、`references/threads-content-operations-workflow.md`、`references/persona-governance.md`、`references/persona-registry.md`、`references/threads-review-workflow.md`、`references/threads-copy-compliance.md`；如涉及账号资料、Bio、实名背书、外链，再补读 `references/threads-account-compliance.md`
   - 若处于账号起盘或重新定位阶段，优先使用 `references/threads-account-baseline-card.md`
   - 若需要做人设启停、切换或回退，优先使用 `references/persona-lifecycle-switch-sop.md`
   - 若需要管理多个 persona 共存、分工与边界，优先使用 `references/multi-persona-coexistence-governance.md`
   - 若同一账号需要多个 persona 轮值排班，优先使用 `references/threads-multi-persona-rotation-schedule.md`
   - 若多个 persona 在同一栏目、时段或主线上发生冲突，优先使用 `references/threads-multi-persona-conflict-arbitration.md`
   - 若需要判断人设与栏目边界，优先使用 `references/persona-content-pillar-map.md`
   - 若需要判断账号主线和副线该如何分配，优先使用 `references/threads-account-primary-secondary-track-ratio.md`
   - 若进入周计划或批次规划，优先使用 `references/threads-weekly-content-schedule.md`
   - 若进入账号周会或运营周报，优先使用 `references/threads-account-weekly-ops-report.md`
   - 若需要判断栏目该保留、放大、合并、暂停还是退场，优先使用 `references/threads-column-lifecycle-assessment.md`
   - 若需要追踪选题、状态、审稿与发布时间，优先使用 `references/threads-content-queue-ledger.md`
   - 若需要判断库存内容是否老化、过时或该退出队列，优先使用 `references/threads-content-inventory-aging-rules.md`
   - 若旧库存仍有价值但需要重新包装后再进入队列，优先使用 `references/threads-content-inventory-regeneration-rules.md`
   - 若需要管理内容系列的推进、断点和后续节点，优先使用 `references/threads-series-continuity-overview.md`
   - 若准备拉长到多周节奏或提高周频，优先使用 `references/threads-multiweek-content-cadence-stress-test.md`
   - 若节奏扩张后开始失控，优先使用 `references/threads-cadence-runaway-rollback-checklist.md`
   - 若某高风险栏目需要短期降频、冷却或冻结，优先使用 `references/threads-high-risk-column-cooldown-rules.md`
   - 若同类高风险表达连续复发，优先使用 `references/threads-recurring-high-risk-expression-blacklist.md`
   - 若黑名单表达需要统一替换口径，优先使用 `references/threads-high-risk-expression-replacement-library.md`
   - 若高风险表达开始出现近义变体绕行，优先使用 `references/threads-high-risk-expression-variant-banlist.md`
   - 若近义变体已触发且需要同步收口规则，优先使用 `references/threads-variant-trigger-auto-writeback-rules.md`
   - 若需要核对自动回写是否真的完成闭环，优先使用 `references/threads-auto-writeback-completion-checklist.md`
   - 若栏目进入冷却或冻结后仍需承接原目标，优先使用 `references/threads-column-replacement-options-template.md`
   - 若栏目准备从冷却或冻结中恢复，优先使用 `references/threads-column-cooldown-release-checklist.md`
   - 若解封栏目准备进入恢复期首轮排期，优先使用 `references/threads-column-release-first-round-schedule.md`
   - 若解封栏目已经跑完首轮恢复，优先使用 `references/threads-column-release-first-round-retrospective.md`
   - 若解封栏目首轮恢复失败且需要重新冷却，优先使用 `references/threads-column-release-failure-recooldown-sop.md`
   - 若需要统一整理审稿结论与发布前交付，优先使用 `references/threads-review-publish-package.md`
   - 若需要记录实验假设、变量和结果，优先使用 `references/threads-content-experiment-log.md`
   - 若进入月报、阶段复盘或阶段性调仓，优先使用 `references/threads-account-monthly-phase-review.md`
   - 若需要做阶段切换、阶段收口或阶段升级决议，优先使用 `references/threads-stage-transition-decision.md`
   - 若需要追踪阶段目标、检查点、偏离信号和下个里程碑，优先使用 `references/threads-stage-goal-tracker.md`
   - 若发生平台风险、账号异常、审稿事故或节奏事故，优先使用 `references/threads-risk-incident-log.md`
   - 若进入账号恢复、风险应急或发布事故处置，优先使用 `references/threads-account-recovery-risk-emergency-sop.md`
   - 若风险应急后进入观察期，优先使用 `references/threads-account-recovery-observation-checklist.md`
   - 若需要判断账号异常后何时恢复正常内容节奏，优先使用 `references/threads-account-content-restart-threshold.md`
   - 若内容已经重启且准备逐步提频，优先使用 `references/threads-content-restart-cadence-escalation-rules.md`
   - 若提频阶段需要明确分栏目升级顺序，优先使用 `references/threads-cadence-escalation-column-stepup-order.md`
   - 若提频阶段需要明确分 persona 升级顺序，优先使用 `references/threads-cadence-escalation-persona-stepup-order.md`
   - 若需要提前定义节奏升级失败的回退红线，优先使用 `references/threads-cadence-escalation-failure-rollback-threshold.md`
   - 若需要处理旧内容、过期资产、历史批次或归档分层，优先使用 `references/threads-content-asset-archiving-rules.md`
   - 若需要把归档资产重新投入使用，优先使用 `references/threads-archived-asset-reactivation-rules.md`
   - 若需要正式结束一个阶段并做完整收口，优先使用 `references/threads-account-stage-exit-checklist.md`
   - 若需要回顾新阶段迁移质量，优先使用 `references/threads-account-stage-migration-retrospective.md`
   - 若进入发布后复盘，优先使用 `references/threads-post-publish-retrospective.md`
5. 可选内容模板包：只有在用户明确进入内容运营对话、要求测试模板或验证样稿时，才读取 `references/threads-content-operations-workflow.md`、`references/p0-persona-branding.md`、`references/tone-style-tw.md`、`references/content-performance.md`、`references/content-dedup-audit.md`、`references/content-continuity.md`、`references/p1-trading-psychology.md`、`references/p2-morning-brief.md`、`references/p3-intraday-tracker.md`、`references/p4-postmarket-recap.md`、`references/p5-evening-lessons.md`、`references/macro-news-synthesizer.md`、`references/single-stock-deepdive.md`
   - 在进入任何内容模板前，先读 `references/content-output-enforcement.md`
   - 生成正文后，必须回到 `references/content-performance.md`、`references/content-dedup-audit.md`、`references/content-continuity.md`、`references/threads-copy-compliance.md` 做复核

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
- `references/usage-scope.md`：默认维护核心与可选内容模板包的边界
- `references/content-output-enforcement.md`：内容生成前后必须执行的闸门与最小执行记录
- `references/persona-governance.md`：多人设字段治理、占位符规则、启停机制与自动匹配门槛
- `references/threads-review-workflow.md`：Threads 发布前审稿顺序、分级与统一输出模板
- `references/threads-platform-rules.md`：Threads 平台规则与 Meta 官方政策映射
- `references/threads-account-compliance.md`：账号层合规与违规排查
- `references/threads-copy-compliance.md`：文案层合规、违规、降推荐与改写方案
- `references/persona-registry.md`：当前人设清单、状态与基础资料
- `references/skill-validation.md`：skill 结构、规则、状态与变更记录的校验标准
- `references/threads-content-operations-workflow.md`：Threads 内容运营强化的工作流、排期状态与最小交付要求
- `references/threads-account-baseline-card.md`：账号基线卡模板，用于起盘、重定位和账号边界定义
- `references/persona-lifecycle-switch-sop.md`：人设启停与切换 SOP，用于 persona 的启用、停用、切换与回退
- `references/multi-persona-coexistence-governance.md`：多 persona 共存治理规则，用于多人设并行时的边界、分工与冲突处理
- `references/threads-multi-persona-rotation-schedule.md`：多 persona 轮值排班模板，用于同一账号内的时段、栏目与批次分工
- `references/threads-multi-persona-conflict-arbitration.md`：多 persona 冲突仲裁模板，用于栏目、时段和主线冲突时的正式裁决
- `references/persona-content-pillar-map.md`：人设与栏目映射表，用于限制人设发散和栏目混乱
- `references/threads-account-primary-secondary-track-ratio.md`：账号主线 / 副线配比规则，用于明确当前阶段的内容重心和投入比例
- `references/threads-weekly-content-schedule.md`：周内容排期模板，用于 3 到 7 篇批次规划
- `references/threads-account-weekly-ops-report.md`：账号周会与运营周报模板，用于周状态同步、风险汇总和下周动作
- `references/threads-column-lifecycle-assessment.md`：栏目生命周期评估模板，用于 keep、expand、merge、pause、retire 的正式判断
- `references/threads-content-queue-ledger.md`：内容队列台账，用于追踪选题、状态、发布时间与处理结论
- `references/threads-content-inventory-aging-rules.md`：内容库存老化规则，用于判断旧选题、旧草稿和久拖未发内容的处理动作
- `references/threads-content-inventory-regeneration-rules.md`：内容库存再生规则，用于判断老库存如何重写、重组和重新入列
- `references/threads-series-continuity-overview.md`：内容系列连续性总表，用于管理系列进度、断点与下一节点
- `references/threads-multiweek-content-cadence-stress-test.md`：多周内容节奏压力测试模板，用于扩周频和扩节奏前的承压判断
- `references/threads-cadence-runaway-rollback-checklist.md`：节奏失控回退清单，用于扩节奏失败后的快速减载与回退
- `references/threads-high-risk-column-cooldown-rules.md`：高风险栏目冷却期规则，用于连续出问题栏目在冷却期内的降频与冻结
- `references/threads-recurring-high-risk-expression-blacklist.md`：高风险表达复发黑名单，用于把重复出问题的句式、钩子和叙事拉入黑名单
- `references/threads-high-risk-expression-replacement-library.md`：高风险表达替代表达库，用于给 `replace` / `block` 表达提供安全替换口径
- `references/threads-high-risk-expression-variant-banlist.md`：高风险表达近义变体禁用表，用于防止通过近义改写绕开黑名单
- `references/threads-variant-trigger-auto-writeback-rules.md`：近义变体触发后的自动回写规则，用于把一次命中快速回写回治理链
- `references/threads-auto-writeback-completion-checklist.md`：自动回写完成度核对清单，用于确认治理链是否真正闭环
- `references/threads-column-replacement-options-template.md`：栏目替代方案模板，用于冷却或冻结栏目后的低风险替代承接
- `references/threads-column-cooldown-release-checklist.md`：栏目冷却期解封检查清单，用于判断栏目何时能限制恢复或正式解封
- `references/threads-column-release-first-round-schedule.md`：栏目解封后首轮排期模板，用于限制恢复期的第一轮排期
- `references/threads-column-release-first-round-retrospective.md`：栏目解封后首轮复盘模板，用于判断首轮恢复后是继续限制、稳定恢复还是重新冷却
- `references/threads-column-release-failure-recooldown-sop.md`：解封栏目首轮失败重新冷却 SOP，用于把失败恢复快速拉回冷却治理
- `references/threads-review-publish-package.md`：统一审稿包与发布包模板，用于单篇和批次交付
- `references/threads-content-experiment-log.md`：内容实验记录模板，用于记录假设、变量、结果与是否推广
- `references/threads-account-monthly-phase-review.md`：账号月报与阶段复盘模板，用于月度判断、阶段收口与下一阶段主线
- `references/threads-stage-transition-decision.md`：阶段切换决议模板，用于 continue、tighten、switch、pause 的正式决议
- `references/threads-stage-goal-tracker.md`：阶段目标追踪面板，用于跟踪检查点、偏离信号与下个里程碑
- `references/threads-risk-incident-log.md`：风险事件处理记录，用于平台、账号、审稿与节奏事故的登记和处置
- `references/threads-account-recovery-risk-emergency-sop.md`：账号恢复 / 风险应急 SOP，用于高风险场景下的快速止损、恢复与回退
- `references/threads-account-recovery-observation-checklist.md`：账号恢复后观察清单，用于风险应急后的 24h / 72h / 7d 观察
- `references/threads-account-content-restart-threshold.md`：账号异常后内容重启门槛，用于判断观察期后能恢复到什么内容强度
- `references/threads-content-restart-cadence-escalation-rules.md`：内容重启后节奏升级规则，用于稳定恢复后的逐级提频
- `references/threads-cadence-escalation-column-stepup-order.md`：提频阶段分栏目升级顺序，用于确定哪些栏目和 persona 先升级
- `references/threads-cadence-escalation-persona-stepup-order.md`：提频阶段分 persona 升级顺序，用于确定不同人设的提频顺位
- `references/threads-cadence-escalation-failure-rollback-threshold.md`：节奏升级失败回退阈值，用于给提频失败设定即时回退红线
- `references/threads-content-asset-archiving-rules.md`：内容资产归档规则，用于旧内容、历史批次与阶段收口素材的分层归档
- `references/threads-archived-asset-reactivation-rules.md`：归档资产再启用规则，用于历史资产回流前的复核与再启用判断
- `references/threads-account-stage-exit-checklist.md`：账号阶段退出清单，用于阶段正式结束前的栏目、系列、风险与资产收口
- `references/threads-account-stage-migration-retrospective.md`：账号阶段迁移回顾模板，用于阶段切换后的迁移质量判断
- `references/threads-post-publish-retrospective.md`：发布后复盘模板，用于保留、放大、停用和提升规则
- `CHANGELOG.md`：skill 升级记录、影响范围与校验结论
- `references/p0-persona-branding.md`：可选内容模板包，人物包装与账号定位
- `references/tone-style-tw.md`：可选内容模板包，台湾口语与平台表达风格
- `references/content-performance.md`：可选内容模板包，痛点、利他、互动标准
- `references/content-dedup-audit.md`：可选内容模板包，内容去重审核规则
- `references/content-continuity.md`：可选内容模板包，内容连续性规则
- `references/p1-trading-psychology.md`：可选内容模板包，交易心理与方法论内容
- `references/p2-morning-brief.md`：可选内容模板包，每日早评早报模板
- `references/p3-intraday-tracker.md`：可选内容模板包，盘中跟踪模板
- `references/p4-postmarket-recap.md`：可选内容模板包，盘后复盘模板
- `references/p5-evening-lessons.md`：可选内容模板包，晚间教育内容模板
- `references/macro-news-synthesizer.md`：可选内容模板包，宏观和新闻归纳方法
- `references/single-stock-deepdive.md`：可选内容模板包，单股基本面与技术面拆解框架
