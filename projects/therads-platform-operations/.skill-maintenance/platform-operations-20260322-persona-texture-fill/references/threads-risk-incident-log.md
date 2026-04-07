# Threads 风险事件处理记录

本文件用于记录内容运营中的风险事件，而不是只靠记忆处理。

风险事件包括：

- 平台风险
- 账号异常
- 审稿事故
- 发布失误
- 节奏事故

## 一、适用场景

- 账号被限流或出现异常提醒
- 高风险文案误进入排期
- 已发布内容出现明显合规或声誉风险
- 周排期、审稿或 persona 切换造成事故

## 二、事件等级

- `L1`：轻微，可当天修正
- `L2`：中等，影响本周节奏
- `L3`：高，影响账号可信度或平台安全

## 三、最小记录维度

1. 事件名称
2. 事件等级
3. 触发时间
4. 影响范围
5. 临时处置
6. 根因判断
7. 后续预防动作

## 四、最小模板

```text
Threads 风险事件记录：
- 事件名称：
- 事件等级：L1 | L2 | L3
- 触发时间：
- 影响范围：
- 临时处置：
- 根因判断：
- 需更新的文件：
- 后续预防动作：
- 当前状态：open | mitigated | closed
```

## 五、使用规则

- `L2` 和 `L3` 必须进入周报或月报
- `L2` 和 `L3` 默认再补一份 `threads-account-recovery-risk-emergency-sop.md`
- 若事件根因是 persona 问题，回到 `persona-lifecycle-switch-sop.md`
- 若事件根因是内容结构实验，回到 `threads-content-experiment-log.md`
- 若事件连续来自同一栏目，应同步 `threads-high-risk-column-cooldown-rules.md`
- 若事件连续来自同类高风险表达，应同步 `threads-recurring-high-risk-expression-blacklist.md`
- 若黑名单表达需要统一换法，应同步 `threads-high-risk-expression-replacement-library.md`
- 若高风险表达开始靠近义变体绕行，应同步 `threads-high-risk-expression-variant-banlist.md`
- 若近义变体已实际命中并需补回系统规则，应同步 `threads-variant-trigger-auto-writeback-rules.md`
- 若栏目已进入冷却但当前阶段仍需承接原目标，应同步 `threads-column-replacement-options-template.md`
- 若解封栏目首轮恢复就再次出问题，应同步 `threads-column-release-first-round-schedule.md`
- 若事件根因是流程缺口，应考虑提升到正式 reference
