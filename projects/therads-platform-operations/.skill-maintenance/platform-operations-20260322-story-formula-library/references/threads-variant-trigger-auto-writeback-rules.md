# Threads 近义变体触发后的自动回写规则

本文件用于在高风险表达近义变体被命中后，明确哪些文件必须同步更新、按什么顺序回写，避免风险只在当次审稿里被看到，却没有沉淀回系统。

## 一、适用场景

- `threads-high-risk-expression-variant-banlist.md` 命中后
- 审稿、排期或已发布内容里出现黑名单近义变体
- 团队需要把一次命中快速回写成长期规则
- 需要明确“先更新什么，再更新什么”

## 二、回写优先级

1. `must-write`
2. `should-write`
3. `context-write`

## 三、最小判断维度

1. 变体是在审稿阶段还是已发布阶段被发现
2. 当前命中的是哪个原表达和哪组替代表达
3. 哪些规则文件必须立刻更新
4. 哪些排期或栏目文件要跟着收紧
5. 哪些复盘或事故记录要补证据

## 四、最小模板

```text
Threads 近义变体触发后的自动回写：
- 触发变体：
- 关联原表达：
- 当前触发阶段：review | schedule | published
- 必须回写文件：
- 建议回写文件：
- 情境回写文件：
- 当前处置动作：
- 回写完成标准：
- 负责人 / 下一步：
```

## 五、使用规则

- 只要命中近义变体禁用表，就至少回写黑名单、替代表达库和变体禁用表之一
- 若命中发生在已发布内容，应同步 `threads-risk-incident-log.md`
- 若命中影响当前周排期，应同步 `threads-weekly-content-schedule.md`
- 若命中说明某栏目表达空间已明显收窄，应同步 `threads-column-lifecycle-assessment.md`
- 回写动作完成后，应同步 `threads-auto-writeback-completion-checklist.md`
- 若回写后仍连续命中，应回到 `threads-recurring-high-risk-expression-blacklist.md`
