# Changelog

## 2026-03-21

### Added
- 新增 `references/threads-portfolio-operations-architecture.md`，用于定义 Threads 多账号矩阵的层级架构、账户分工与 Codex/OpenClaw/TG 分层。
- 新增 `references/threads-multi-account-skills-blueprint.md`，用于定义 Threads 多账号运营所需项目层 skills 蓝图。
- 新增 `references/threads-multi-account-batch-01-plan.md`，用于定义 Threads 多账号运营第一批落地计划、交付物与验收标准。
- 新增 `references/threads-account-matrix-master-board.md`，用于正式填写 `10` 账户矩阵总表。
- 新增 `references/threads-priority-account-activation-framework.md`，用于决定首批 `2-3` 个优先运营账号。
- 新增 `references/threads-shared-hook-library-framework.md`，用于定义多账号共享钩子库骨架与去重规则。
- 新增 `references/threads-publish-writeback-spec.md`，用于定义发帖、回写与失败记录字段。
- 新增 `references/threads-insights-collection-spec.md`，用于定义账号、帖子和组合层 insights 回收字段。

### Changed
- 更新 `SKILL.md`，增加 Threads 多账号矩阵、统一发帖/回复/增长任务的正式入口。
- 更新 `references/usage-scope.md`，增加“可选多账号运营增强链路”，明确其为显式触发链路而非默认主链。
- 更新 `references/threads-content-operations-workflow.md`，把组合层 / 矩阵层任务纳入正式工作流。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，把多账号运营增强链路纳入校验。
- 更新多账号增强链路，把 `Batch 01` 的 `5` 个交付物提升为正式模板与规格，而不再只停留在抽象蓝图层。
- 新增 `lige-data-driven-veteran` 作为“股海老司機-李哥”的 `active` persona，并将 `xy0446`、`數據驅動決策`、`官方帳號` 与 `勿輕信假消息` 纳入窄匹配信号。
- 更新 `references/persona-registry.md` 的当前 `active` 人设清单，纳入 `lige-data-driven-veteran`。
- 新增 `main-force-operator` 作为“主力操盤手”的 `draft` persona；因含“前券商自營部操盤人”与“現任XX證券投顧老師”等强背书且仍有占位符，本次按高风险占位人设管理。
- 新增 `amingbo-taiwan-stock-teahouse` 作为“阿明伯的台股茶館”的 `draft` persona；因含“聯發科退休員工”这类强企业背景且当前未核对，本次按高风险企业背书草案管理。
- 为 `amingbo-taiwan-stock-teahouse` 增加 `200-300字` 的内容输出区间；该限制仅适用于该 persona，不作为其他人设的默认规则。
- 按用户提供的人设清单补建 `15` 个缺失 persona，分别为 `soaring-stock-logician`、`far-sighted-aming`、`single-mom-investment-diary`、`taiwan-stock-big-brother`、`lao-xie-retirement-notes`、`accountant-sis-compound-notes`、`xinjie-single-mom-survival`、`jeffrey-tang-market-veteran`、`market-navigator`、`dark-horse-catcher`、`stock-picker-hunter`、`not-a-stock-god`、`ringing-stocks-no-hammer`、`taiwan-stock-air-defense-egg`、`axun-taiwan-stock-notebook`；本次统一按 `draft` 管理，待与现有人设重叠度及风险边界复核后再决定是否激活。

### Impact
- `platform-operations` 现在已经具备“单账号内容运营主链 + 显式多账号增强链路”的双层结构；多账号任务有正式入口，但仍不会默认升级成全自动并发。
- 后续如果要做 `10` 账户矩阵，默认先走“架构 -> skills 蓝图 -> Batch 01”链路，而不是直接进入自动分发。
- 后续如果要真正开始 `10` 账户运营，已经可以直接填写矩阵总表、优先启动名单、共享钩子库、发布回写规格和 insights 规格。
- “股海老司機 / 李哥 / xy0446 / 數據驅動決策 / 官方帳號 / 勿輕信假消息” 相关输入会优先命中 `lige-data-driven-veteran`；本次未用泛化的“耐心 / 智慧 / 長期遊戲”单词单独兜底，以降低与其他资深人设串线风险。
- “主力操盤手” 已进入注册表，但当前仅可用于模板、测试或内部草稿；在 `XX` 对应机构任职信息补齐并核对前，不会进入自动匹配或对外发布链路。
- “阿明伯的台股茶館 / qaz88.990” 已进入注册表，但当前仅可用于模板、测试或内部草稿；在“聯發科退休員工”背景可核对前，不会进入自动匹配或对外发布链路。
- `amingbo-taiwan-stock-teahouse` 现已明确建议输出长度为 200-300 字；该限制仅对该 persona 生效，不影响其他人设。
- 本轮补建后，用户清单中的已存在人设与缺失人设已被统一对齐；新增的 `15` 个条目不会影响当前 `active` 池与自动匹配结果，后续需再逐个做激活审核与去重复核。

### Validation
- `python3 scripts/validate_platform_operations.py /path/to/platform-operations`

## 2026-03-20

### Added
- 新增 `references/threads-content-operations-workflow.md`，把 Threads 平台账户内容运营强化收敛为正式工作流。
- 新增 `references/threads-account-baseline-card.md`，用于账号起盘、重定位与边界确认。
- 新增 `references/persona-lifecycle-switch-sop.md`，用于 persona 的启停、切换与回退。
- 新增 `references/multi-persona-coexistence-governance.md`，用于多 persona 并行时的边界与冲突处理。
- 新增 `references/persona-content-pillar-map.md`，用于约束 persona 与栏目之间的映射关系。
- 新增 `references/threads-weekly-content-schedule.md`，用于一周内容批次规划。
- 新增 `references/threads-account-weekly-ops-report.md`，用于账号周会与运营周报。
- 新增 `references/threads-content-queue-ledger.md`，用于追踪选题、状态、审稿与发布时间。
- 新增 `references/threads-review-publish-package.md`，用于统一审稿包与发布包交付。
- 新增 `references/threads-content-experiment-log.md`，用于记录实验假设、变量和结果。
- 新增 `references/threads-account-monthly-phase-review.md`，用于账号月报、阶段复盘与方向判断。
- 新增 `references/threads-risk-incident-log.md`，用于记录和处理平台、账号与流程风险事件。
- 新增 `references/threads-post-publish-retrospective.md`，用于发布后复盘与规则提升。
- 新增 `references/threads-stage-transition-decision.md`，用于阶段切换、收口、升级与暂停的正式决议。
- 新增 `references/threads-account-recovery-risk-emergency-sop.md`，用于账号恢复、风险应急与发布事故处置。
- 新增 `references/threads-content-asset-archiving-rules.md`，用于旧内容、历史批次与阶段素材的分层归档。
- 新增 `references/threads-stage-goal-tracker.md`，用于阶段目标、检查点与偏离信号的持续追踪。
- 新增 `references/threads-account-recovery-observation-checklist.md`，用于风险应急后的恢复观察期管理。
- 新增 `references/threads-archived-asset-reactivation-rules.md`，用于归档资产回流前的复核与再启用判断。
- 新增 `references/threads-column-lifecycle-assessment.md`，用于栏目 keep、expand、merge、pause、retire 的正式判断。
- 新增 `references/threads-series-continuity-overview.md`，用于追踪内容系列的进度、断点与下一节点。
- 新增 `references/threads-account-stage-exit-checklist.md`，用于阶段正式结束前的栏目、系列、风险与资产收口。
- 新增 `references/threads-account-primary-secondary-track-ratio.md`，用于账号主线与副线内容投入比例的正式判断。
- 新增 `references/threads-multiweek-content-cadence-stress-test.md`，用于扩周频和拉长节奏前的承压测试。
- 新增 `references/threads-account-stage-migration-retrospective.md`，用于阶段切换后的迁移质量回顾。
- 新增 `references/threads-content-inventory-aging-rules.md`，用于旧选题、旧草稿与久拖未发内容的老化处理。
- 新增 `references/threads-multi-persona-rotation-schedule.md`，用于同一账号下多个 persona 的轮值排班。
- 新增 `references/threads-cadence-runaway-rollback-checklist.md`，用于节奏扩张失控后的快速减载与回退。
- 新增 `references/threads-content-inventory-regeneration-rules.md`，用于老库存重写、重组和重新入列的再生规则。
- 新增 `references/threads-multi-persona-conflict-arbitration.md`，用于多人设抢栏目、抢时段和抢主线时的正式仲裁。
- 新增 `references/threads-high-risk-column-cooldown-rules.md`，用于高风险栏目短期降频、冷却与冻结。
- 新增 `references/threads-recurring-high-risk-expression-blacklist.md`，用于把重复触发风险的表达与叙事拉入黑名单。
- 新增 `references/threads-column-replacement-options-template.md`，用于冷却或冻结栏目后的替代承接方案。
- 新增 `references/threads-account-content-restart-threshold.md`，用于异常恢复后判断内容能恢复到什么强度。
- 新增 `references/threads-high-risk-expression-replacement-library.md`，用于给 `replace` / `block` 表达提供统一替换口径。
- 新增 `references/threads-column-cooldown-release-checklist.md`，用于判断栏目何时能限制恢复或正式解封。
- 新增 `references/threads-content-restart-cadence-escalation-rules.md`，用于稳定恢复后的逐级提频判断。
- 新增 `references/threads-high-risk-expression-variant-banlist.md`，用于防止通过近义改写绕开黑名单。
- 新增 `references/threads-column-release-first-round-schedule.md`，用于解封栏目恢复后的首轮低频排期。
- 新增 `references/threads-cadence-escalation-failure-rollback-threshold.md`，用于给节奏升级设定失败回退红线。
- 新增 `references/threads-variant-trigger-auto-writeback-rules.md`，用于近义变体命中后的自动回写和同步收口。
- 新增 `references/threads-column-release-first-round-retrospective.md`，用于解封栏目首轮恢复后的正式复盘。
- 新增 `references/threads-cadence-escalation-column-stepup-order.md`，用于提频阶段确定哪些栏目和 persona 先升级。
- 新增 `references/threads-auto-writeback-completion-checklist.md`，用于核对近义变体自动回写是否真正完成闭环。
- 新增 `references/threads-column-release-failure-recooldown-sop.md`，用于解封栏目首轮失败后的重新冷却处置。
- 新增 `references/threads-cadence-escalation-persona-stepup-order.md`，用于提频阶段明确不同 persona 的升级顺位。

### Changed
- 更新 `SKILL.md`，新增“内容运营强化”入口，并要求在进入内容模板前先走内容运营工作流。
- 更新 `SKILL.md`，把账号基线卡、周排期和发布后复盘模板挂入内容运营强化链路。
- 更新 `SKILL.md`，把内容队列台账、统一审稿/发布包与 persona-栏目映射表挂入内容运营强化链路。
- 更新 `SKILL.md`，把 persona 启停 SOP、周会/周报模板与实验记录模板挂入内容运营强化链路。
- 更新 `SKILL.md`，把月报、风险事件与多 persona 共存治理挂入内容运营强化链路。
- 更新 `SKILL.md`，把阶段切换决议、风险应急 SOP 与内容资产归档规则挂入内容运营强化链路。
- 更新 `SKILL.md`，把阶段目标追踪、恢复后观察与归档资产再启用挂入内容运营强化链路。
- 更新 `SKILL.md`，把栏目生命周期、系列连续性与阶段退出清单挂入内容运营强化链路。
- 更新 `SKILL.md`，把主线 / 副线配比、多周节奏压力测试与阶段迁移回顾挂入内容运营强化链路。
- 更新 `SKILL.md`，把内容库存老化、多人设轮值排班与节奏失控回退挂入内容运营强化链路。
- 更新 `SKILL.md`，把内容库存再生、多人设冲突仲裁与高风险栏目冷却期挂入内容运营强化链路。
- 更新 `SKILL.md`，把高风险表达复发黑名单、栏目替代方案与账号异常后内容重启门槛挂入内容运营强化链路。
- 更新 `SKILL.md`，把高风险表达替代表达库、栏目冷却期解封检查与内容重启后节奏升级挂入内容运营强化链路。
- 更新 `SKILL.md`，把高风险表达近义变体禁用表、栏目解封后首轮排期与节奏升级失败回退阈值挂入内容运营强化链路。
- 更新 `SKILL.md`，把近义变体触发后的自动回写、首轮解封栏目复盘与提频阶段分栏目升级顺序挂入内容运营强化链路。
- 更新 `SKILL.md`，把自动回写完成度核对、首轮失败重新冷却与提频阶段分 persona 升级顺序挂入内容运营强化链路。
- 更新 `SKILL.md`、`references/usage-scope.md`、`references/threads-content-operations-workflow.md` 与 `agents/openai.yaml`，明确 Threads 内容运营强化第一阶段已完成，若无真实运营痛点不再默认扩默认主链。
- 更新 `references/threads-content-operations-workflow.md`，把基线卡、周排期和复盘模板挂接到账号层、周计划层与复盘层任务。
- 更新 `references/threads-content-operations-workflow.md`，把内容队列、统一审稿/发布包和 persona-栏目映射表挂进默认执行链。
- 更新 `references/threads-content-operations-workflow.md`，加入周会/周报层、实验层和 persona 切换入口。
- 更新 `references/threads-content-operations-workflow.md`，加入月报/阶段层、风险事件层和多 persona 共存入口。
- 更新 `references/threads-content-operations-workflow.md`，加入阶段切换 / 决议层、风险恢复 / 应急层与资产归档层。
- 更新 `references/threads-content-operations-workflow.md`，加入阶段目标追踪层、恢复后观察层与资产再启用层，并清理旧重复段落。
- 更新 `references/threads-content-operations-workflow.md`，加入栏目生命周期层、系列连续性层与阶段退出层。
- 更新 `references/threads-content-operations-workflow.md`，加入主线 / 副线配比层、多周节奏压力测试层与阶段迁移回顾层。
- 更新 `references/threads-content-operations-workflow.md`，加入内容库存老化层、多 persona 轮值层与节奏失控回退层。
- 更新 `references/threads-content-operations-workflow.md`，加入内容库存再生层、多 persona 冲突仲裁层与高风险栏目冷却层。
- 更新 `references/usage-scope.md`，明确内容运营强化链路先基线、再排期、再复盘。
- 更新 `references/usage-scope.md`，把内容队列、统一审稿/发布包和 persona-栏目映射表纳入强化层。
- 更新 `references/usage-scope.md`，把周会/周报、实验记录和 persona 启停 SOP 纳入强化层。
- 更新 `references/usage-scope.md`，把月报、风险事件和多 persona 共存治理纳入强化层。
- 更新 `references/usage-scope.md`，把阶段切换、风险应急和资产归档纳入强化层的收口链。
- 更新 `references/usage-scope.md`，把阶段追踪、恢复观察与资产再启用纳入强化层的跟进链。
- 更新 `references/usage-scope.md`，把栏目生命周期、系列连续性与阶段退出纳入强化层的中线治理。
- 更新 `references/usage-scope.md`，把主线 / 副线配比、多周节奏压力测试与阶段迁移回顾纳入强化层的节奏治理。
- 更新 `references/usage-scope.md`，把内容库存老化、多人设轮值排班与节奏失控回退纳入强化层的库存与稳定性治理。
- 更新 `references/usage-scope.md`，把内容库存再生、多人设冲突仲裁与高风险栏目冷却期纳入强化层的再生与冷却治理。
- 更新 `references/usage-scope.md`，把高风险表达替代表达库、栏目冷却期解封检查与内容重启后节奏升级纳入强化层的恢复升级治理。
- 更新 `references/usage-scope.md`，把高风险表达近义变体禁用、栏目解封后首轮排期与节奏升级失败回退阈值纳入强化层的恢复后执行治理。
- 更新 `references/usage-scope.md`，把近义变体自动回写、首轮解封栏目复盘与提频阶段分栏目升级顺序纳入强化层的恢复后收口治理。
- 更新 `references/usage-scope.md`，把“内容运营强化链路”从纯模板包中单独分层，避免一上来就进入散乱写作。
- 更新 `agents/openai.yaml`，让隐式调用在用户明确要求开始或强化内容运营时，先进入工作流，而不是直接跳模板。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，让新模板进入正式校验口径。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，把阶段追踪、恢复观察与再启用规则纳入正式校验口径。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，把栏目生命周期、系列连续性与阶段退出清单纳入正式校验口径。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，把主线 / 副线配比、多周节奏压力测试与阶段迁移回顾纳入正式校验口径。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，把高风险表达替代表达库、栏目冷却期解封检查与内容重启后节奏升级纳入正式校验口径。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，把高风险表达近义变体禁用、栏目解封后首轮排期与节奏升级失败回退阈值纳入正式校验口径。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，把近义变体自动回写、首轮解封栏目复盘与提频阶段分栏目升级顺序纳入正式校验口径。
- 更新 `references/threads-review-workflow.md`、`references/threads-recurring-high-risk-expression-blacklist.md` 与 `references/threads-post-publish-retrospective.md`，把替代表达库接回审稿与复盘链。
- 更新 `references/threads-high-risk-column-cooldown-rules.md`、`references/threads-column-replacement-options-template.md` 与 `references/threads-weekly-content-schedule.md`，把栏目解封检查接回冷却与排期链。
- 更新 `references/threads-account-recovery-observation-checklist.md`、`references/threads-account-content-restart-threshold.md`、`references/threads-account-weekly-ops-report.md` 与 `references/threads-stage-goal-tracker.md`，把节奏升级规则接回恢复和跟踪链。
- 更新 `references/threads-review-workflow.md`、`references/threads-high-risk-expression-replacement-library.md` 与 `references/threads-recurring-high-risk-expression-blacklist.md`，把近义变体禁用表接回黑名单与审稿链。
- 更新 `references/threads-column-cooldown-release-checklist.md`、`references/threads-weekly-content-schedule.md` 与 `references/threads-post-publish-retrospective.md`，把栏目解封后首轮排期接回排期与复盘链。
- 更新 `references/threads-content-restart-cadence-escalation-rules.md`、`references/threads-account-weekly-ops-report.md`、`references/threads-stage-goal-tracker.md` 与 `references/threads-risk-incident-log.md`，把节奏升级失败回退阈值接回跟踪与事故链。
- 更新 `references/threads-review-workflow.md`、`references/threads-high-risk-expression-variant-banlist.md` 与 `references/threads-risk-incident-log.md`，把近义变体自动回写接回审稿、事故与治理链。
- 更新 `references/threads-column-release-first-round-schedule.md`、`references/threads-weekly-content-schedule.md` 与 `references/threads-post-publish-retrospective.md`，把首轮解封栏目复盘接回排期与复盘链。
- 更新 `references/threads-content-restart-cadence-escalation-rules.md`、`references/threads-account-weekly-ops-report.md` 与 `references/threads-stage-goal-tracker.md`，把提频阶段分栏目升级顺序接回升级和跟踪链。
- 更新 `references/threads-content-operations-workflow.md`，加入自动回写完成度核对层、解封栏目首轮失败重新冷却层与提频阶段分 persona 升级顺序层。
- 更新 `references/usage-scope.md`，把自动回写完成度核对、首轮失败重新冷却与提频阶段分 persona 升级顺序纳入强化层，并加入阶段封板规则。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，新增最终三项模板与“阶段完成后默认封板”的校验。
- 更新 `references/threads-variant-trigger-auto-writeback-rules.md`、`references/threads-column-release-first-round-retrospective.md` 与 `references/threads-content-restart-cadence-escalation-rules.md`，补齐与最终三项模板的衔接。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，把内容库存老化、多人设轮值排班与节奏失控回退纳入正式校验口径。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，把内容库存再生、多人设冲突仲裁与高风险栏目冷却期纳入正式校验口径。
- 更新 `references/threads-review-workflow.md`、`references/threads-account-baseline-card.md`、`references/threads-weekly-content-schedule.md` 与 `references/threads-post-publish-retrospective.md`，让新模板与现有工作流形成闭环。
- 更新 `references/persona-lifecycle-switch-sop.md`、`references/threads-account-weekly-ops-report.md` 与 `references/threads-content-experiment-log.md`，让新模板与现有工作流形成闭环。
- 更新 `references/threads-account-monthly-phase-review.md`、`references/threads-risk-incident-log.md` 与 `references/threads-post-publish-retrospective.md`，让阶段决议、风险恢复与资产归档挂回原有模板。
- 更新 `references/threads-stage-transition-decision.md`、`references/threads-account-recovery-risk-emergency-sop.md`、`references/threads-content-asset-archiving-rules.md` 与 `references/threads-account-weekly-ops-report.md`，让阶段追踪、恢复观察与资产再启用挂回原有模板。
- 更新 `references/threads-weekly-content-schedule.md`、`references/threads-content-queue-ledger.md`、`references/threads-stage-goal-tracker.md` 与 `references/threads-post-publish-retrospective.md`，让栏目生命周期、系列连续性与阶段退出挂回原有模板。
- 更新 `references/threads-account-weekly-ops-report.md`、`references/threads-account-monthly-phase-review.md`、`references/threads-stage-transition-decision.md`、`references/threads-account-stage-exit-checklist.md` 与 `references/threads-stage-goal-tracker.md`，让主线 / 副线配比、多周节奏压力测试与阶段迁移回顾挂回原有模板。
- 更新 `references/multi-persona-coexistence-governance.md`、`references/threads-weekly-content-schedule.md`、`references/threads-content-queue-ledger.md`、`references/threads-account-weekly-ops-report.md` 与 `references/threads-multiweek-content-cadence-stress-test.md`，让库存老化、多人设轮值排班与节奏失控回退挂回原有模板。
- 更新 `references/threads-content-inventory-aging-rules.md`、`references/threads-multi-persona-rotation-schedule.md`、`references/threads-column-lifecycle-assessment.md`、`references/threads-risk-incident-log.md` 与 `references/threads-account-weekly-ops-report.md`，让库存再生、冲突仲裁与高风险栏目冷却期挂回原有模板。
- 更新 `references/threads-content-operations-workflow.md`，加入高风险表达复发黑名单层、栏目替代方案层与账号异常后内容重启门槛层。
- 更新 `references/threads-review-workflow.md`，把高风险表达黑名单接入发布前审稿结论。
- 更新 `references/threads-high-risk-column-cooldown-rules.md`、`references/threads-weekly-content-schedule.md` 与 `references/threads-column-lifecycle-assessment.md`，把栏目冷却后的替代承接接回排期与治理链。
- 更新 `references/threads-risk-incident-log.md` 与 `references/threads-post-publish-retrospective.md`，把复发风险表达黑名单接回事故与复盘链。
- 更新 `references/threads-account-recovery-risk-emergency-sop.md` 与 `references/threads-account-recovery-observation-checklist.md`，把异常恢复后的内容重启门槛接回恢复链。

### Impact
- `platform-operations` 现在不再只有“规则维护”与“模板输出”两种模式，中间新增了“内容运营强化”层。
- `platform-operations` 现在具备“账号基线 -> 周批次 -> 发布后复盘”的最小生产闭环。
- `platform-operations` 现在进一步具备“栏目映射 -> 队列台账 -> 审稿/发布包”的运营控制层。
- `platform-operations` 现在进一步具备“persona 切换 -> 周会/周报 -> 实验记录”的管理层模板。
- `platform-operations` 现在进一步具备“月报 / 阶段复盘 -> 风险事件记录 -> 多 persona 共存治理”的阶段治理层。
- `platform-operations` 现在进一步具备“阶段切换决议 -> 风险应急恢复 -> 内容资产归档”的收口层。
- `platform-operations` 现在进一步具备“阶段目标追踪 -> 恢复后观察 -> 归档资产再启用”的跟进层。
- `platform-operations` 现在进一步具备“栏目生命周期 -> 系列连续性 -> 阶段退出清单”的中线治理层。
- `platform-operations` 现在进一步具备“主线 / 副线配比 -> 多周节奏压力测试 -> 阶段迁移回顾”的节奏治理层。
- `platform-operations` 现在进一步具备“内容库存老化 -> 多 persona 轮值排班 -> 节奏失控回退”的稳定性治理层。
- `platform-operations` 现在进一步具备“内容库存再生 -> 多 persona 冲突仲裁 -> 高风险栏目冷却期”的再生与防过热治理层。
- `platform-operations` 现在进一步具备“高风险表达复发黑名单 -> 栏目替代方案 -> 异常后内容重启门槛”的持续止损与恢复闸门。
- `platform-operations` 现在进一步具备“高风险表达替代表达库 -> 栏目冷却期解封检查 -> 内容重启后节奏升级”的恢复后细化治理层。
- `platform-operations` 现在进一步具备“高风险表达近义变体禁用 -> 栏目解封后首轮排期 -> 节奏升级失败回退阈值”的恢复后执行约束层。
- `platform-operations` 现在进一步具备“近义变体自动回写 -> 首轮解封栏目复盘 -> 提频阶段分栏目升级顺序”的恢复后收口与推进层。
- `platform-operations` 现在进一步具备“自动回写完成度核对 -> 首轮失败重新冷却 -> 提频阶段分 persona 升级顺序”的最终收口层。
- Threads 内容运营强化第一阶段现已封板；后续默认不再继续扩默认主链，只有出现真实运营痛点时才开新批次。
- Threads 平台账户内容运营可以先按批次化方式推进，不必一开始就进入重自动化。
- 后续进入真实内容运营时，默认先定边界与顺序，再进入单篇生产与审稿。

### Validation
- `python3 scripts/validate_platform_operations.py /path/to/platform-operations`

## 2026-03-18

### Added
- 新增 `references/persona-governance.md`，把多人设的字段、状态、占位符和启停机制独立出来治理。
- 新增 `references/threads-review-workflow.md`，作为 Threads 发布前审稿的统一入口。
- 新增 `references/skill-validation.md`，定义 skill 维护后的自动校验与人工校验要求。
- 新增 `scripts/validate_platform_operations.py`，用于结构与人设状态的自动校验。
- 新增 `references/usage-scope.md`，定义默认维护核心与可选内容模板包的实际使用边界。
- 新增 `references/content-output-enforcement.md`，把内容生成前检查、生成后复核和最小执行记录收敛成强制闸门。

### Changed
- 更新 `SKILL.md`，加入维护与校验链路、发布前强制审稿链路，以及新 reference 导航。
- 更新 `references/persona-registry.md`，扩展状态模型与字段模板，并将未补齐的人设改为 `draft` 管理。
- 更新 `references/p0-persona-branding.md`，把人设激活状态纳入发布前判断。
- 更新 `references/threads-platform-rules.md`、`references/threads-account-compliance.md`、`references/threads-copy-compliance.md`，补充证据分级与审稿衔接说明。
- 物理删除 12 个预置 `active` 人设，仅保留 `draft` 人设与人设治理机制。
- 更新人设匹配规则，当前无 `active` 人设时不再自动兜底。
- 新增 `taiwan-stock-captain` 作为当前启用中的台股复合型 persona，并恢复默认自动匹配入口。
- 新增 `old-cat-taiwan-stocks` 作为主打分點、主力、洗盤與盤後數據拆解的 `active` persona。
- 新增 `laoqiu-88` 作为主打炒股技巧、操盘指标、選股策略与股票知識入口的 `active` persona。
- 新增 `amei-exchange-retirement-journal` 作为“阿美/證交所退休日誌”的 `draft` persona；因含机构履历式背书且未核对，暂不进入自动匹配与对外成稿。
- 新增 `retired-ajie-taiwan-veteran` 作为“退休阿傑｜15年台股老兵”的 `active` persona，并为其补充较窄的自动识别信号。
- 新增 `laozhou-kline-veteran` 作为“老周｜K線老兵”的 `active` persona，并把 `tina065547` 与其老兵叙事纳入窄匹配信号。
- 新增 `comeback-trader-15y` 作为“翻身交易者 📈｜股市15年”的 `active` persona，并将低谷、债务与重建叙事纳入识别信号。
- 新增 `master-di-short-swing` 作为“帝師”的 `active` persona，并把其短線波段、離場紀律与資產目标叙事纳入窄匹配信号。
- 新增 `laowang-taiwan-rebuild` 作为“台股老汪”的 `active` persona，并将其从赌徒心态走向交易修正的叙事纳入识别信号。
- 新增 `stock-analyst` 作为“股票分析师”的 `active` 风格 persona；用于尝试不同的人设风格，不再按占位条目管理。
- 细化 `stock-analyst` 的人设定义：明确其本质是“专注股票与盘面”的 persona，不走小故事起手的内容结构。
- 为 `stock-analyst` 增加 `100字以内` 的默认输出限制，明确其为短讯型股票分析师风格；该限制仅适用于 `stock-analyst`，不作为其他 persona 的默认规则。
- 调整 `SKILL.md` 的默认定位：从“默认全栈内容生产”收敛为“默认维护核心 + 可选内容模板包按需启用”。
- 更新 `agents/openai.yaml`，使 implicit invocation 也优先落在维护、审稿、校验与变更记录，而不是默认日更内容生产。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，新增“实际使用对齐”校验，避免继续默认扩张长期闲置模块。
- 更新 `SKILL.md`、`references/p0-persona-branding.md`、`references/p1-trading-psychology.md`、`references/p2-morning-brief.md`、`references/p3-intraday-tracker.md`、`references/p4-postmarket-recap.md`、`references/p5-evening-lessons.md`、`references/macro-news-synthesizer.md` 与 `references/single-stock-deepdive.md`，要求内容输出先读 `content-output-enforcement.md`。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，新增“内容模板必须挂接执行闸门”的校验。

### Impact
- `persona-01-zhang-shyi-chang` 在补齐运营字段前不再参与自动匹配，避免实名背书与占位符混用。
- 后续所有 Threads 规则口径调整都必须同步更新来源说明，并通过校验脚本。
- 旧预置执行人设已清空，当前启用中的 `active` personas 为 `taiwan-stock-captain`、`old-cat-taiwan-stocks`、`laoqiu-88`、`retired-ajie-taiwan-veteran`、`laozhou-kline-veteran`、`comeback-trader-15y`、`master-di-short-swing`、`laowang-taiwan-rebuild` 与 `stock-analyst`。
- 在用户未明确指定其他 persona 时，默认仍以 `taiwan-stock-captain` 作为兜底执行人设。
- 当前 `active` personas 已扩展为 `taiwan-stock-captain`、`old-cat-taiwan-stocks`、`laoqiu-88`、`retired-ajie-taiwan-veteran`、`laozhou-kline-veteran`、`comeback-trader-15y`、`master-di-short-swing`、`laowang-taiwan-rebuild` 与 `stock-analyst`；其中“老貓 / 分點 / 主力 / 洗盤 / 盤後數據”相关输入会优先命中 `old-cat-taiwan-stocks`。
- `laoqiu.88 / 老丘 / 股票知識這裡都有 / 記得點關注哦` 等品牌识别语会优先命中 `laoqiu-88`，但不会以泛化的“选股策略/股票知识”单词强制兜底。
- `amei-exchange-retirement-journal` 当前仅作为内部草案保存，不改变现有 `active` persona 池；任何带有“證交所退休”式机构背景的对外使用，都需先完成核对后再激活。
- “退休阿傑 / 15年台股老兵 / 提早登出職場 / 股市不缺英雄，缺的是老兵 / 過來人的避坑指南”会优先命中 `retired-ajie-taiwan-veteran`；本次未用泛化的“財務自由 / 產業趨勢 / 籌碼”单词做强匹配，以降低串人设风险。
- “老周 / K線老兵 / tina065547 / 市場如戰場 / 活到最後的人才是贏家”会优先命中 `laozhou-kline-veteran`；本次未用泛化的“K 線 / 紀律 / 順勢”单词单独兜底。
- “翻身交易者 / 股市15年 / 曾經跌入低谷 / 背負債務 / 人生重新開始”会优先命中 `comeback-trader-15y`；本次未把“交易 / 學習 / 生活”这类泛词设为强匹配。
- “帝師 / 56歲 / 交易股票31年 / 進場有賺可自行離場 / 存股人生 / 資產達到5000萬”会优先命中 `master-di-short-swing`；本次未把“短線 / 波段 / 存股”单词单独设为强匹配，以降低串人设风险。
- “台股老汪 / 老汪 / 曾沉迷賭博 / 人生低谷 / 研究股市 / 財富自由”会优先命中 `laowang-taiwan-rebuild`；本次未把“家破人亡 / 股市秘密 / 財富自由”直接固化为默认可复用表达，而是收敛为反赌徒心态与交易修正叙事。
- “股票分析師 / 股票分析师 / 盤前快訊 / 盤中更新 / 記憶體族群 / 題材觀察”会优先命中 `stock-analyst`；本次按“尝试不同人设风格”处理，不再保留占位态。
- `stock-analyst` 已进入 `active` persona 池，但样本中的目标价承诺、收益刺激、点赞公开与未核实合作消息仍被明确列为禁区，不作为默认可发布表达。
- `stock-analyst` 当前在人设层面已明确：输出重点是股票、题材、盘面与节奏，不需要用小故事包装。
- `stock-analyst` 现已明确默认输出长度上限为 100 字以内，适合盘前快讯、盘中更新与题材短讯；该限制仅对 `stock-analyst` 生效，不影响其他人设。
- 审计发现 `p1-trading-psychology.md`、`p2-morning-brief.md`、`p3-intraday-tracker.md`、`p4-postmarket-recap.md`、`p5-evening-lessons.md`、`macro-news-synthesizer.md` 与 `single-stock-deepdive.md` 目前主要停留在 `SKILL.md` 声明层，未进入近期真实维护主链路。
- 现在默认只加载 persona 治理、Threads 审稿、校验与变更记录相关模块；内容模板仍保留，但仅在用户明确要求内容运营或模板验证时启用。
- 本轮进一步确认：规则未执行的根因不是文件缺失，而是内容模板长期只有“写法说明”，没有“生成前必须检查、生成后必须复核”的执行闸门。
- 现在内容输出若未接入 `content-output-enforcement.md`，会在结构与校验层同时失败，避免再次出现“规则存在但实际没跑”。

### Validation
- `python3 scripts/validate_platform_operations.py /path/to/platform-operations`
- 预期结果：`pass`
