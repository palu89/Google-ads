# Threads 内容运营工作流

本文件用于把 `platform-operations` 从“只会维护规则”推进到“可以稳定承接内容运营强化”，但不直接跳成重自动化、多账号并发或全量日更流水线。

当前目标是先让 Threads 平台账户内容运营具备：

- 清晰的任务分类
- 稳定的排期与状态流
- 一致的审稿与发布前闸门
- 可复盘、可沉淀、可提升的学习闭环

## 一、适用范围

在以下场景进入本工作流：

- 用户明确说要开始或强化 Threads 平台账户内容运营
- 用户要做账号定位、栏目规划、内容排期、周计划、日更批次
- 用户要做单篇内容生产，但同时要考虑账号连续性
- 用户要做一批内容的审稿、排队、复盘与后续优化

以下场景不进入本工作流：

- 纯 skill 维护
- 纯 persona 治理
- 纯 Threads 合规问答
- 纯模板测试但不涉及真实运营节奏

## 二、当前阶段判断

当前 `平台账户运营` 项目仍属于规划态，不应过早进入：

- 多账号自动分发
- 自动发帖脚本
- 多 agent 同时编排执行
- 复杂 KPI 自动汇总系统

当前更适合先做：

- 单项目、单工作流、多人设可切换
- 批次化内容运营
- 审稿先行
- 复盘沉淀先行

若用户明确进入多账号或账号矩阵任务：

- 可以启用多账号增强链路
- 但当前 `Batch 01` 仍以组合治理、账号基线、钩子库、发布规格与 insights 回收为主
- 不直接进入 `10` 账户全自动并发

当前补充判断：

- Threads 内容运营强化第一阶段已完成
- 默认先用现有链路承接真实运营
- 若无真实运营痛点，不继续默认新增模板或扩默认主链

配套模板：

- `threads-account-baseline-card.md`
- `persona-lifecycle-switch-sop.md`
- `multi-persona-coexistence-governance.md`
- `threads-multi-persona-rotation-schedule.md`
- `threads-multi-persona-conflict-arbitration.md`
- `persona-content-pillar-map.md`
- `threads-account-primary-secondary-track-ratio.md`
- `threads-weekly-content-schedule.md`
- `threads-account-weekly-ops-report.md`
- `threads-column-lifecycle-assessment.md`
- `threads-content-queue-ledger.md`
- `threads-content-inventory-aging-rules.md`
- `threads-content-inventory-regeneration-rules.md`
- `threads-series-continuity-overview.md`
- `threads-multiweek-content-cadence-stress-test.md`
- `threads-cadence-runaway-rollback-checklist.md`
- `threads-high-risk-column-cooldown-rules.md`
- `threads-recurring-high-risk-expression-blacklist.md`
- `threads-high-risk-expression-replacement-library.md`
- `threads-high-risk-expression-variant-banlist.md`
- `threads-variant-trigger-auto-writeback-rules.md`
- `threads-auto-writeback-completion-checklist.md`
- `threads-column-replacement-options-template.md`
- `threads-column-cooldown-release-checklist.md`
- `threads-column-release-first-round-schedule.md`
- `threads-column-release-first-round-retrospective.md`
- `threads-column-release-failure-recooldown-sop.md`
- `threads-review-publish-package.md`
- `threads-content-experiment-log.md`
- `threads-account-monthly-phase-review.md`
- `threads-stage-transition-decision.md`
- `threads-stage-goal-tracker.md`
- `threads-risk-incident-log.md`
- `threads-account-recovery-risk-emergency-sop.md`
- `threads-account-recovery-observation-checklist.md`
- `threads-account-content-restart-threshold.md`
- `threads-content-restart-cadence-escalation-rules.md`
- `threads-cadence-escalation-column-stepup-order.md`
- `threads-cadence-escalation-persona-stepup-order.md`
- `threads-cadence-escalation-failure-rollback-threshold.md`
- `threads-content-asset-archiving-rules.md`
- `threads-archived-asset-reactivation-rules.md`
- `threads-account-stage-exit-checklist.md`
- `threads-account-stage-migration-retrospective.md`
- `threads-post-publish-retrospective.md`
- `threads-portfolio-operations-architecture.md`
- `threads-multi-account-skills-blueprint.md`
- `threads-multi-account-batch-01-plan.md`
- `threads-account-matrix-master-board.md`
- `threads-priority-account-activation-framework.md`
- `threads-shared-hook-library-framework.md`
- `threads-publish-writeback-spec.md`
- `threads-insights-collection-spec.md`

## 三、默认执行链

每次进入内容运营任务时，按以下顺序推进：

1. 判断任务层级
- 这是组合层 / 矩阵层、账号层、周计划层、单篇层、批次层，还是复盘层任务
- 组合层 / 矩阵层优先使用 `threads-portfolio-operations-architecture.md`
- 多账号技能设计层优先使用 `threads-multi-account-skills-blueprint.md`
- 多账号落地批次层优先使用 `threads-multi-account-batch-01-plan.md`
- 多账号矩阵总表层优先使用 `threads-account-matrix-master-board.md`
- 多账号优先启动层优先使用 `threads-priority-account-activation-framework.md`
- 多账号钩子治理层优先使用 `threads-shared-hook-library-framework.md`
- 多账号发布回写规格层优先使用 `threads-publish-writeback-spec.md`
- 多账号 insights 规格层优先使用 `threads-insights-collection-spec.md`
- 账号层优先使用 `threads-account-baseline-card.md`
- 账号层涉及人设启停或切换时，使用 `persona-lifecycle-switch-sop.md`
- 账号层涉及多个 persona 共存时，使用 `multi-persona-coexistence-governance.md`
- 多 persona 轮值层优先使用 `threads-multi-persona-rotation-schedule.md`
- 多 persona 冲突仲裁层优先使用 `threads-multi-persona-conflict-arbitration.md`
- 账号层涉及栏目边界时，再用 `persona-content-pillar-map.md`
- 主线 / 副线配比层优先使用 `threads-account-primary-secondary-track-ratio.md`
- 周计划层优先使用 `threads-weekly-content-schedule.md`
- 周会/周报层优先使用 `threads-account-weekly-ops-report.md`
- 栏目生命周期层优先使用 `threads-column-lifecycle-assessment.md`
- 批次层和单篇层需要登记时，使用 `threads-content-queue-ledger.md`
- 内容库存老化层优先使用 `threads-content-inventory-aging-rules.md`
- 内容库存再生层优先使用 `threads-content-inventory-regeneration-rules.md`
- 系列连续性层优先使用 `threads-series-continuity-overview.md`
- 多周节奏压力测试层优先使用 `threads-multiweek-content-cadence-stress-test.md`
- 节奏失控回退层优先使用 `threads-cadence-runaway-rollback-checklist.md`
- 高风险栏目冷却层优先使用 `threads-high-risk-column-cooldown-rules.md`
- 高风险表达复发黑名单层优先使用 `threads-recurring-high-risk-expression-blacklist.md`
- 高风险表达替代表达层优先使用 `threads-high-risk-expression-replacement-library.md`
- 高风险表达近义变体禁用层优先使用 `threads-high-risk-expression-variant-banlist.md`
- 近义变体触发后的自动回写层优先使用 `threads-variant-trigger-auto-writeback-rules.md`
- 自动回写完成度核对层优先使用 `threads-auto-writeback-completion-checklist.md`
- 栏目替代方案层优先使用 `threads-column-replacement-options-template.md`
- 栏目冷却期解封检查层优先使用 `threads-column-cooldown-release-checklist.md`
- 栏目解封后首轮排期层优先使用 `threads-column-release-first-round-schedule.md`
- 栏目解封后首轮复盘层优先使用 `threads-column-release-first-round-retrospective.md`
- 解封栏目首轮失败重新冷却层优先使用 `threads-column-release-failure-recooldown-sop.md`
- 单篇层进入审稿或交付时，使用 `threads-review-publish-package.md`
- 需要验证新写法、新栏目或新人设时，使用 `threads-content-experiment-log.md`
- 月报 / 阶段层优先使用 `threads-account-monthly-phase-review.md`
- 阶段切换 / 决议层优先使用 `threads-stage-transition-decision.md`
- 阶段目标追踪层优先使用 `threads-stage-goal-tracker.md`
- 风险事件层优先使用 `threads-risk-incident-log.md`
- 风险恢复 / 应急层优先使用 `threads-account-recovery-risk-emergency-sop.md`
- 恢复后观察层优先使用 `threads-account-recovery-observation-checklist.md`
- 账号异常后内容重启门槛层优先使用 `threads-account-content-restart-threshold.md`
- 内容重启后节奏升级层优先使用 `threads-content-restart-cadence-escalation-rules.md`
- 提频阶段分栏目升级顺序层优先使用 `threads-cadence-escalation-column-stepup-order.md`
- 提频阶段分 persona 升级顺序层优先使用 `threads-cadence-escalation-persona-stepup-order.md`
- 节奏升级失败回退阈值层优先使用 `threads-cadence-escalation-failure-rollback-threshold.md`
- 资产归档层优先使用 `threads-content-asset-archiving-rules.md`
- 资产再启用层优先使用 `threads-archived-asset-reactivation-rules.md`
- 阶段退出层优先使用 `threads-account-stage-exit-checklist.md`
- 阶段迁移回顾层优先使用 `threads-account-stage-migration-retrospective.md`
- 复盘层优先使用 `threads-post-publish-retrospective.md`

2. 确认 persona
- 先读 `persona-governance.md`
- 再读 `persona-registry.md`
- 未确认 `active` persona 前，不直接进入可发布正文

3. 明确内容模块
- `P0` 人设包装
- `P1` 方法论 / 交易心理
- `P2` 早评
- `P3` 盘中跟踪
- `P4` 盘后复盘
- `P5` 晚间教育
- `单股深挖`
- `宏观 / 新闻整合`

4. 明确本篇角色
- 引流
- 建立信任
- 提供方法
- 促进互动
- 串联系列内容

5. 进入生成前闸门
- 强制执行 `content-output-enforcement.md`

6. 生成后进入发布前审稿
- 强制执行 `threads-review-workflow.md`

7. 形成发布包
- 使用 `threads-review-publish-package.md`
- 统一输出审稿包或发布包
- 更新 `threads-content-queue-ledger.md`

8. 记录复盘素材
- 需要沉淀到 persona、合规规则、内容模板还是连续性规则

## 四、任务类型

### 组合层 / 矩阵层任务

适用：

- 要管理 `3` 个以上账号
- 要设计 `10` 账户矩阵
- 要统一发帖、钩子、回复和涨粉节奏
- 要定义组合级周报、组合级实验和资源倾斜

推荐模板：

- `threads-portfolio-operations-architecture.md`
- `threads-multi-account-skills-blueprint.md`
- `threads-multi-account-batch-01-plan.md`
- `threads-account-matrix-master-board.md`
- `threads-priority-account-activation-framework.md`
- `threads-shared-hook-library-framework.md`
- `threads-publish-writeback-spec.md`
- `threads-insights-collection-spec.md`

最小输出：

- 当前判断
- 账户矩阵
- 优先启动账号
- 组合层角色分工
- 统一钩子规则
- 发布回写方式
- 数据回收方式
- 风险点
- Batch 01 动作

### 1. 账号层任务

适用：

- 账号定位
- persona 启停
- Bio / Link / 头像 / 名称合规
- 栏目结构
- 内容支柱设计

推荐模板：

- `threads-account-baseline-card.md`
- `persona-lifecycle-switch-sop.md`
- `multi-persona-coexistence-governance.md`
- `persona-content-pillar-map.md`

最小输出：

- 当前判断
- 建议 persona
- 栏目结构
- persona 与栏目映射
- 内容边界
- 合规风险
- 下一个批次动作

### 2. 主线 / 副线配比层任务

适用：

- 当前阶段要定主线和副线
- 主副线开始抢排期
- 账号重心需要重新收口

推荐模板：

- `threads-account-primary-secondary-track-ratio.md`

最小输出：

- 当前阶段
- 主线定义
- 副线定义
- 推荐配比
- 偏离信号

### 3. 多 Persona 轮值层任务

适用：

- 同一账号有多个 persona
- 一周内容需要轮值分工
- 想试运行辅助 persona

推荐模板：

- `threads-multi-persona-rotation-schedule.md`

最小输出：

- 当前周期
- 默认主 persona
- 轮值槽位
- 换班条件
- 回退顺序

### 4. 多 Persona 冲突仲裁层任务

适用：

- 多个 persona 抢同一栏目
- 多个 persona 抢同一时间槽位
- 主 persona 与辅助 persona 冲突

推荐模板：

- `threads-multi-persona-conflict-arbitration.md`

最小输出：

- 当前冲突
- 涉及 persona
- 仲裁结论
- 生效期
- 回退条件

### 5. 周计划层任务

适用：

- 周主题安排
- 每周 3 到 7 篇内容规划
- 栏目分配与节奏设计

推荐模板：

- `threads-weekly-content-schedule.md`
- `threads-content-queue-ledger.md`
- `threads-account-weekly-ops-report.md`

最小输出：

- 本周目标
- 本周内容支柱
- 每篇内容的模块、persona、主痛点、目标动作
- 哪些篇互相串联
- 队列登记顺序

### 6. 周会 / 周报层任务

适用：

- 账号周会
- 运营周报
- 周状态同步
- 风险汇总和下周动作确认

推荐模板：

- `threads-account-weekly-ops-report.md`
- `threads-stage-goal-tracker.md`

最小输出：

- 本周目标完成度
- 本周有效内容与失效内容
- 当前风险与阻塞
- 当前 persona 状态
- 下周优先动作

### 7. 栏目生命周期层任务

适用：

- 栏目去留判断
- 栏目边界重叠
- 栏目需要放大或退场

推荐模板：

- `threads-column-lifecycle-assessment.md`

最小输出：

- 栏目名称
- 有效信号
- 失效信号
- 处理结论
- 下一步动作

### 8. 高风险栏目冷却层任务

适用：

- 某栏目连续高风险
- 某栏目需要短期降频或冻结
- 某栏目暂不退场但不能继续高频推进

推荐模板：

- `threads-high-risk-column-cooldown-rules.md`

最小输出：

- 栏目名称
- 当前风险信号
- 冷却等级
- 冷却周期
- 解除条件

### 9. 高风险表达复发黑名单层任务

适用：

- 同类高风险表达连续复发
- 不同 persona 反复踩到同一类句式风险
- 需要明确哪些表达进入禁用或替换清单

推荐模板：

- `threads-recurring-high-risk-expression-blacklist.md`

最小输出：

- 当前表达 / 句式
- 关联事件
- 黑名单级别
- 允许替代表达
- 解除条件

### 10. 高风险表达替代表达层任务

适用：

- 黑名单表达已经进入 `replace`
- 需要为同类风险句式建立统一替换口径
- 想保留内容价值，但不能继续沿用原钩子

推荐模板：

- `threads-high-risk-expression-replacement-library.md`

最小输出：

- 原表达
- 风险点
- 推荐替代表达
- 适用 persona / 栏目
- 替换后复核动作

### 11. 高风险表达近义变体禁用层任务

适用：

- 高风险表达开始用近义改写绕行
- 替代表达库已经建立，但仍出现变体回流
- 想把“不能只换几个字继续发”写成正式禁用边界

推荐模板：

- `threads-high-risk-expression-variant-banlist.md`

最小输出：

- 原表达
- 禁用变体
- 禁用等级
- 允许保留的安全表达
- 再次出现时处理动作

### 12. 近义变体触发后的自动回写层任务

适用：

- 近义变体已在审稿、排期或已发布内容中命中
- 需要明确哪些规则文件必须同步更新
- 想把一次命中快速沉淀回系统

推荐模板：

- `threads-variant-trigger-auto-writeback-rules.md`

最小输出：

- 触发变体
- 当前触发阶段
- 必须回写文件
- 建议回写文件
- 当前处置动作

### 13. 栏目替代方案层任务

适用：

- 某栏目进入冷却或冻结
- 某栏目需要暂时退场但周目标不能空窗
- 想用更稳妥的栏目承接原目标

推荐模板：

- `threads-column-replacement-options-template.md`

最小输出：

- 原栏目
- 推荐替代栏目
- 风险下降依据
- 生效周期
- 回切条件

### 14. 栏目冷却期解封检查层任务

适用：

- 某栏目冷却周期将满
- 想判断栏目能否限制恢复或正式解封
- 需要确认原风险是否已经下降

推荐模板：

- `threads-column-cooldown-release-checklist.md`

最小输出：

- 栏目名称
- 冷却周期完成情况
- 当前剩余风险
- 解封结论
- 回退条件

### 15. 栏目解封后首轮排期层任务

适用：

- 栏目已经通过解封检查
- 栏目准备重新进入周排期
- 需要给首轮恢复设低频限制和观察窗口

推荐模板：

- `threads-column-release-first-round-schedule.md`

最小输出：

- 栏目名称
- 首轮周期
- 首轮允许篇数 / 时段
- 首轮观察窗口
- 首轮失败回退动作

### 16. 栏目解封后首轮复盘层任务

适用：

- 栏目首轮恢复排期已经结束
- 需要判断是否继续限制、稳定恢复或重新冷却
- 想把首轮恢复结果写成下一轮规则

推荐模板：

- `threads-column-release-first-round-retrospective.md`

最小输出：

- 栏目名称
- 首轮有效信号
- 首轮风险信号
- 复盘结论
- 下一轮建议

### 17. 月报 / 阶段层任务

适用：

- 账号月报
- 阶段复盘
- 月度方向判断
- 阶段性收口与转向

推荐模板：

- `threads-account-monthly-phase-review.md`
- `threads-stage-transition-decision.md`
- `threads-stage-goal-tracker.md`

最小输出：

- 本月目标完成度
- 本月有效模式与失效模式
- 本月 persona / 栏目判断
- 当前阶段结论
- 下阶段主线

### 18. 阶段切换 / 决议层任务

适用：

- 阶段切换
- 阶段收口
- 阶段升级
- 阶段暂停

推荐模板：

- `threads-stage-transition-decision.md`

最小输出：

- 当前阶段判断
- 切换理由
- 影响范围
- 生效条件
- 回退条件

### 19. 阶段目标追踪层任务

适用：

- 阶段进行中的检查点同步
- 阶段目标是否偏离
- 下个里程碑与阻塞梳理

推荐模板：

- `threads-stage-goal-tracker.md`

最小输出：

- 当前阶段
- 当前检查点
- 领先信号
- 当前阻塞
- 下次检查点

### 20. 单篇层任务

适用：

- 单篇 Threads 帖文
- 某篇文案重写
- 某篇样稿审稿

最小输出：

- persona
- 模块
- 主痛点
- 正文
- 审稿结论：`BLOCK | REWRITE | REVISE | PASS`
- 审稿包或发布包

### 21. 批次层任务

适用：

- 一次性产出 3 到 5 篇
- 一次性审 3 到 5 篇
- 为一个主题做成组内容

最小输出：

- 批次主题
- 每篇内容的角色分工
- 去重检查
- 连续性关系
- 发布顺序建议
- 队列状态更新

### 22. 内容库存老化层任务

适用：

- 队列里有很多旧内容
- `approved` 很久没发
- 想清理老旧库存

推荐模板：

- `threads-content-inventory-aging-rules.md`

最小输出：

- 内容编号
- 老化层级
- 当前风险
- 处理动作
- 下次复核点

### 23. 内容库存再生层任务

适用：

- 老库存值得救回
- 旧内容需要换角度重做
- 想把旧内容重组进新系列

推荐模板：

- `threads-content-inventory-regeneration-rules.md`

最小输出：

- 内容编号
- 可保留部分
- 必须重写部分
- 再生方式
- 再生后入口

### 24. 系列连续性层任务

适用：

- 系列连发规划
- 系列断点检查
- 系列是否继续推进

推荐模板：

- `threads-series-continuity-overview.md`

最小输出：

- 系列名称
- 当前进度
- 待发布节点
- 连续性风险
- 下一节点

### 25. 多周节奏压力测试层任务

适用：

- 准备扩到多周排期
- 准备提高周频
- 想判断团队是否扛得住更快节奏

推荐模板：

- `threads-multiweek-content-cadence-stress-test.md`

最小输出：

- 测试窗口
- 当前周频
- 预计周频
- 过载信号
- 调整动作

### 26. 节奏失控回退层任务

适用：

- 节奏扩张后明显积压
- 审稿过载
- 主线被副线挤压

推荐模板：

- `threads-cadence-runaway-rollback-checklist.md`

最小输出：

- 当前失控信号
- 立即暂停项
- 立即保留项
- 回退后周频
- 下一次检查点

### 27. 实验层任务

适用：

- 测试新开头
- 测试新栏目
- 测试新人设表达
- 测试不同 CTA 或结构

推荐模板：

- `threads-content-experiment-log.md`

最小输出：

- 实验假设
- 变量
- 风险边界
- 观察结果
- 是否推广

### 28. 风险事件层任务

适用：

- 平台风险
- 账号异常
- 审稿事故
- 发布失误

推荐模板：

- `threads-risk-incident-log.md`
- `threads-account-recovery-risk-emergency-sop.md`

最小输出：

- 当前事件等级
- 当前影响范围
- 当前处置状态
- 临时止损动作
- 后续预防动作

### 29. 风险恢复 / 应急层任务

适用：

- 账号恢复
- 风险应急
- 发布事故
- 应急回退

推荐模板：

- `threads-account-recovery-risk-emergency-sop.md`

最小输出：

- 当前事件等级
- 当前处置状态
- 恢复动作
- 回退动作
- 复盘入口

### 30. 恢复后观察层任务

适用：

- 风险应急后的观察期
- 恢复后的 24h / 72h / 7d 跟踪
- 逐步恢复节奏前的确认

推荐模板：

- `threads-account-recovery-observation-checklist.md`

最小输出：

- 当前观察窗口
- 已恢复信号
- 未恢复信号
- 当前保守动作
- 观察结论

### 31. 账号异常后内容重启门槛层任务

适用：

- 观察期后准备恢复发文
- 需要判断恢复到什么内容强度
- 需要明确当前允许和禁止的内容范围

推荐模板：

- `threads-account-content-restart-threshold.md`

最小输出：

- 关联事件
- 已完成观察窗口
- 当前允许内容范围
- 当前允许节奏上限
- 重启结论

### 32. 内容重启后节奏升级层任务

适用：

- 内容已经完成保守恢复
- 准备从当前重启级别继续提频
- 需要判断能不能从低频走回稳定频率

推荐模板：

- `threads-content-restart-cadence-escalation-rules.md`

最小输出：

- 当前重启级别
- 已稳定窗口
- 候选升级节奏
- 升级结论
- 回退触发条件

### 33. 提频阶段分栏目升级顺序层任务

适用：

- 准备从当前节奏继续提频
- 需要决定哪些栏目和 persona 先升级
- 想避免一轮提频时全线同升

推荐模板：

- `threads-cadence-escalation-column-stepup-order.md`

最小输出：

- 当前节奏级别
- 第一顺位升级
- 第二顺位升级
- 暂缓升级
- 回退优先级

### 34. 节奏升级失败回退阈值层任务

适用：

- 准备给节奏升级设失败红线
- 担心提频后出现审稿、排期或风险失衡
- 需要明确什么信号一出现就必须回退

推荐模板：

- `threads-cadence-escalation-failure-rollback-threshold.md`

最小输出：

- 当前节奏级别
- watch 阈值
- rollback 阈值
- 回退后目标节奏
- 重新尝试升级条件

### 35. 自动回写完成度核对层任务

适用：

- 已执行自动回写规则
- 需要确认治理链是否真的完成闭环
- 想判断这次回写能否正式关闭

推荐模板：

- `threads-auto-writeback-completion-checklist.md`

最小输出：

- 触发变体
- must-write 完成情况
- should-write 完成情况
- 尚未完成项
- 核对结论

### 36. 解封栏目首轮失败重新冷却层任务

适用：

- 首轮复盘结论为 `re-cooldown`
- 栏目恢复首轮已经失败
- 需要把栏目重新拉回冷却或硬冻结

推荐模板：

- `threads-column-release-failure-recooldown-sop.md`

最小输出：

- 栏目名称
- 首轮失败信号
- 重新冷却结论
- 冷却周期
- 替代承接方案

### 37. 提频阶段分 Persona 升级顺序层任务

适用：

- 当前节奏允许继续提频
- 账号下存在多个 persona
- 需要决定谁先升级、谁暂缓升级

推荐模板：

- `threads-cadence-escalation-persona-stepup-order.md`

最小输出：

- 当前节奏级别
- 当前主 persona
- 第一顺位升级
- 暂缓升级
- 失败回退顺序

### 38. 资产归档层任务

适用：

- 旧内容归档
- 历史批次归档
- 阶段收口归档
- 已失效素材清理

推荐模板：

- `threads-content-asset-archiving-rules.md`

最小输出：

- 归档对象
- 归档原因
- 归档层级
- 可回用性
- 后续引用规则

### 39. 资产再启用层任务

适用：

- 旧高表现内容重启
- 历史栏目恢复
- 归档素材回流
- 参考资产重新进入队列

推荐模板：

- `threads-archived-asset-reactivation-rules.md`

最小输出：

- 资产名称
- 再启用理由
- 处理方式
- 风险点
- 验证步骤

### 40. 阶段退出层任务

适用：

- 当前阶段正式结束
- 当前阶段暂停
- 当前阶段准备切主线

推荐模板：

- `threads-account-stage-exit-checklist.md`

最小输出：

- 当前阶段
- 退出原因
- 已完成收口项
- 未完成收口项
- 下一阶段入口

### 41. 阶段迁移回顾层任务

适用：

- 新阶段已运行 1 到 2 个检查点
- 需要确认迁移是否稳定
- 需要判断这次阶段切换是不是要返工

推荐模板：

- `threads-account-stage-migration-retrospective.md`

最小输出：

- 来源阶段
- 目标阶段
- 当前稳定项
- 当前未稳定项
- 回顾结论

### 42. 复盘层任务

适用：

- 单篇发布后复盘
- 周批次结束后的复盘
- 阶段结束后的经验收口

推荐模板：

- `threads-post-publish-retrospective.md`
- `threads-content-asset-archiving-rules.md`
- `threads-archived-asset-reactivation-rules.md`
- `threads-column-lifecycle-assessment.md`
- `threads-account-stage-migration-retrospective.md`
- `threads-high-risk-column-cooldown-rules.md`
- `threads-recurring-high-risk-expression-blacklist.md`
- `threads-high-risk-expression-replacement-library.md`
- `threads-high-risk-expression-variant-banlist.md`
- `threads-variant-trigger-auto-writeback-rules.md`
- `threads-auto-writeback-completion-checklist.md`
- `threads-column-replacement-options-template.md`
- `threads-column-release-first-round-schedule.md`
- `threads-column-release-first-round-retrospective.md`
- `threads-column-release-failure-recooldown-sop.md`

最小输出：

- 复盘对象
- 有效点
- 无效点
- 处理结论
- 下一步动作

## 五、内容队列状态

为避免“有想法但没有推进顺序”，内容项目统一使用以下状态：

- `idea`：只有选题或方向
- `selected`：已纳入本轮计划
- `drafting`：正在写
- `review`：进入审稿
- `revise`：需修改
- `approved`：通过审稿，可发布
- `scheduled`：已排定发布时间
- `published`：已发布
- `recycle`：暂不发，但可重写再用
- `blocked`：因合规、定位或事实问题暂缓

## 六、默认强化顺序

开始一个新账号或新批次时，默认按以下顺序推进：

1. 先定 persona 与账号边界
2. 若涉及多个 persona，再定轮值排班
3. 再定主线 / 副线配比
4. 再定内容支柱与栏目
5. 再做一周内容计划
6. 若要用旧库存，先做库存老化检查；值得救的再做库存再生
7. 若表达已进入黑名单，先补替代表达库；若开始靠近义变体绕行，再补近义变体禁用表；若变体已实际命中，再补自动回写规则与完成度核对清单
8. 若栏目进入冷却或冻结，先判断是否需要替代栏目；准备恢复时先走解封检查，通过后再做首轮排期；首轮结束后再做首轮复盘；若首轮失败，再走重新冷却 SOP
9. 若要跨多周推进，先做节奏压力测试
10. 若账号刚从异常中恢复，先完成观察，再判断内容重启门槛
11. 若内容已稳定重启，再判断能否节奏升级；提频前先定分栏目升级顺序，再定分 persona 升级顺序，最后定义失败回退阈值
12. 再进入单篇生产
13. 若出现明显过载，优先走节奏回退清单
14. 最后做审稿与发布后复盘

不要倒过来做。不要在 persona 未稳时大量产文。

当前 Threads 内容运营强化第一阶段已完成；若无真实运营痛点，默认停在现有主链，不继续扩默认模板。

## 七、发布前最低要求

任何要交付“可发布”结论的 Threads 内容，至少满足：

- persona 已确认且可用
- 模块已确认
- 已执行去重
- 已执行连续性检查
- 已执行 Threads 审稿
- 若涉及最新、当日、盘中、新闻、即时行情，已核实具体日期与信息时效

## 八、风险控制

- 不把 `draft` persona 直接包装成对外可发布实名内容
- 不把平台允许但明显损害推荐资格的表达当成“可放心发”
- 不把已进入高风险表达黑名单的句式换壳重发
- 不在未完成解封检查前把冷却栏目重新抬回主力位置
- 不在未完成节奏升级判断前把恢复中的账号直接拉回高频
- 不把收益承诺、夸大经历、伪装权威、赌徒翻身刺激叙事当成增长捷径
- 不为了日更而牺牲连续性、可信度和可验证性
- 不在项目仍处于规划态时提前堆自动化执行层

## 九、默认交付格式

若用户没有指定格式，内容运营任务默认输出：

- 当前判断
- 当前属于哪个层级
- 当前使用的人设
- 当前模块
- 建议动作
- 审稿结论或待审稿项
- 风险点
- 下一篇或下一批建议
