# Skill 使用边界

本文件用于定义 `platform-operations` 在真实使用中的默认工作链路，避免 `SKILL.md` 长期保留大量“写了但默认不会进入”的模块。

## 一、默认启用的维护核心

以下模块属于当前默认工作链路：
- `references/persona-governance.md`
- `references/persona-registry.md`
- `references/skill-validation.md`
- `CHANGELOG.md`
- `references/threads-review-workflow.md`
- `references/threads-platform-rules.md`
- `references/threads-account-compliance.md`
- `references/threads-copy-compliance.md`

默认启用场景：
- 新增、修改、停用、归档 persona
- 调整自动匹配门槛、字段模板、占位符规则
- 审 Threads 平台规则、账号合规、文案合规
- 维护校验脚本、结构完整性与变更记录

## 二、内容运营强化链路

以下模块用于“开始做内容运营，但先不直接堆大量模板”：
- `references/threads-content-operations-workflow.md`
- `references/threads-account-baseline-card.md`
- `references/persona-lifecycle-switch-sop.md`
- `references/multi-persona-coexistence-governance.md`
- `references/threads-multi-persona-rotation-schedule.md`
- `references/threads-multi-persona-conflict-arbitration.md`
- `references/persona-content-pillar-map.md`
- `references/threads-account-primary-secondary-track-ratio.md`
- `references/threads-weekly-content-schedule.md`
- `references/threads-account-weekly-ops-report.md`
- `references/threads-column-lifecycle-assessment.md`
- `references/threads-content-queue-ledger.md`
- `references/threads-content-inventory-aging-rules.md`
- `references/threads-content-inventory-regeneration-rules.md`
- `references/threads-series-continuity-overview.md`
- `references/threads-multiweek-content-cadence-stress-test.md`
- `references/threads-cadence-runaway-rollback-checklist.md`
- `references/threads-high-risk-column-cooldown-rules.md`
- `references/threads-recurring-high-risk-expression-blacklist.md`
- `references/threads-high-risk-expression-replacement-library.md`
- `references/threads-high-risk-expression-variant-banlist.md`
- `references/threads-variant-trigger-auto-writeback-rules.md`
- `references/threads-auto-writeback-completion-checklist.md`
- `references/threads-column-replacement-options-template.md`
- `references/threads-column-cooldown-release-checklist.md`
- `references/threads-column-release-first-round-schedule.md`
- `references/threads-column-release-first-round-retrospective.md`
- `references/threads-column-release-failure-recooldown-sop.md`
- `references/threads-review-publish-package.md`
- `references/threads-content-experiment-log.md`
- `references/threads-account-monthly-phase-review.md`
- `references/threads-stage-transition-decision.md`
- `references/threads-stage-goal-tracker.md`
- `references/threads-risk-incident-log.md`
- `references/threads-account-recovery-risk-emergency-sop.md`
- `references/threads-account-recovery-observation-checklist.md`
- `references/threads-account-content-restart-threshold.md`
- `references/threads-content-restart-cadence-escalation-rules.md`
- `references/threads-cadence-escalation-column-stepup-order.md`
- `references/threads-cadence-escalation-persona-stepup-order.md`
- `references/threads-cadence-escalation-failure-rollback-threshold.md`
- `references/threads-content-asset-archiving-rules.md`
- `references/threads-archived-asset-reactivation-rules.md`
- `references/threads-account-stage-exit-checklist.md`
- `references/threads-account-stage-migration-retrospective.md`
- `references/threads-post-publish-retrospective.md`
- `references/persona-governance.md`
- `references/persona-registry.md`
- `references/threads-review-workflow.md`
- `references/threads-copy-compliance.md`

启用场景：
- 用户明确说要开始或强化 Threads 平台账户内容运营
- 用户要做账号定位、内容支柱、周计划、批次规划
- 用户要把单篇写作收敛成持续内容工作流

使用原则：
- 先用工作流约束内容运营，再进入具体模板
- 先用账号基线卡、人设启停 SOP、多 persona 治理、轮值排班、冲突仲裁和人设栏目映射定边界，再用主线 / 副线配比规则定当前重心，再用周排期模板定顺序
- 再用栏目生命周期评估与内容系列连续性总表把栏目和系列的中线结构定清楚
- 再用内容库存老化规则判断旧库存该保留、刷新还是退出；值得救的再走库存再生规则
- 若准备跨到多周节奏，先用节奏压力测试模板验证承载能力
- 若高风险栏目连续出问题，先设冷却期；若同类高风险表达连续复发，再补表达黑名单；若黑名单需要统一替换口径，再补替代表达库；若近义变体开始绕行，再补近义变体禁用表；若已命中变体，再补自动回写规则
- 若变体已命中并执行回写，再补自动回写完成度核对清单
- 若栏目冷却后仍需承接目标，再补栏目替代方案；若栏目准备恢复，再补解封检查清单；若栏目已允许恢复，再补首轮排期模板；首轮结束后再补首轮复盘；若首轮失败，再补重新冷却 SOP
- 若节奏扩张后失控，优先用回退清单减载，不继续硬撑
- 再用内容队列台账和统一审稿/发布包推进执行
- 用周会/周报模板做阶段同步，用实验记录模板沉淀测试结果
- 用月报/阶段复盘模板先形成阶段判断，再用阶段切换决议模板正式落结论，并用阶段目标追踪面板盯执行进度
- 用风险事件记录追踪异常和处置，用风险应急 SOP 管高风险止损与恢复，再用恢复后观察清单盯观察期，先用内容重启门槛判断能恢复到什么强度，再用节奏升级规则判断能否继续提频；提频前先定分栏目升级顺序，再定分 persona 升级顺序，最后定义升级失败回退阈值
- 最后用发布后复盘模板做提升，用内容资产归档规则处理阶段收口后的旧内容和历史批次，再用归档资产再启用规则管理回流，并在阶段退出前走退出清单；新阶段稳定后再补迁移回顾
- 先把 persona、栏目、排期和审稿链路定清楚，再扩张产量
- 当前项目仍属于规划态，不默认进入多账号自动化或重执行编排
- 当前 Threads 内容运营强化第一阶段已完成；若无真实运营痛点，不默认继续新增模板或扩默认主链

## 三、可选多账号运营增强链路

以下模块用于“明确进入多账号、账号矩阵、组合增长与统一执行编排”时的增强链路：
- `references/threads-portfolio-operations-architecture.md`
- `references/threads-multi-account-skills-blueprint.md`
- `references/threads-multi-account-batch-01-plan.md`
- `references/threads-account-matrix-master-board.md`
- `references/threads-priority-account-activation-framework.md`
- `references/threads-shared-hook-library-framework.md`
- `references/threads-publish-writeback-spec.md`
- `references/threads-insights-collection-spec.md`

启用场景：
- 用户明确说要运营 `3` 个以上账号
- 用户明确说要做 `10` 账户矩阵、统一发帖、统一钩子、统一回复或组合涨粉
- 用户明确说要把 Threads 从单账号内容运营升级到组合运营

使用原则：
- 这是显式增强链路，不是默认主链
- 先做账号矩阵与账户分工，再做统一发帖与增长实验
- 先做组合治理、账号基线、钩子库和数据回收，再考虑 API 自动发帖
- `Batch 01` 只做“矩阵结构 + 运行蓝图 + 首批交付”，不直接进入 `10` 账户全自动并发
- `Batch 01` 的首批交付物固定为：矩阵总表、优先启动框架、共享钩子库框架、发布回写规格、insights 回收规格
- 多账号链路仍必须复用现有单账号审稿、连续性、去重和复盘规则，不另起一套内容治理标准

## 四、可选内容模板包

以下模块保留，但默认不进入主链路：
- `references/p0-persona-branding.md`
- `references/persona-expression-variance.md`
- `references/story-structure-formula-library.md`
- `references/tone-style-tw.md`
- `references/content-performance.md`
- `references/content-dedup-audit.md`
- `references/content-continuity.md`
- `references/p1-trading-psychology.md`
- `references/p2-morning-brief.md`
- `references/p3-intraday-tracker.md`
- `references/p4-postmarket-recap.md`
- `references/p5-evening-lessons.md`
- `references/macro-news-synthesizer.md`
- `references/single-stock-deepdive.md`

仅在以下情况启用：
- 用户明确进入“内容运营对话”
- 用户明确要求做模板验证、测试样稿或内容结构演练
- 需要验证某个内容模板是否仍可复用，而不是继续维护 skill 结构本身

## 五、实践收敛规则

- 若一个模块长期只在 `SKILL.md` 中被列出，但没有进入近期真实工作链路，不再继续默认扩张它的规则。
- 若需求本质是 skill 维护、校验、审稿或 persona 治理，就不要默认加载内容模板包。
- 若用户只是新增 persona，不要自动跳入 `P0-P5` 内容写作链路。
- 若后续某类内容模板连续多次进入真实使用，再考虑把它从“可选”提升回默认链路。
- 若 Threads 内容运营强化第一阶段已完成，后续默认先用现有主链解决真实运营问题，而不是继续预扩模板。
- 若用户明确进入多账号运营，允许启用“可选多账号运营增强链路”，但仍不把多账号自动化升级为默认主链。

## 六、结构处理原则

- 不因“暂时少用”就直接删除模板文件，优先降级为可选模块。
- 任何从“默认启用”改为“可选内容模板包”的调整，属于高影响改动，必须同步更新：
  - `SKILL.md`
  - `references/skill-validation.md`
  - `scripts/validate_platform_operations.py`
  - `agents/openai.yaml`
  - `CHANGELOG.md`
