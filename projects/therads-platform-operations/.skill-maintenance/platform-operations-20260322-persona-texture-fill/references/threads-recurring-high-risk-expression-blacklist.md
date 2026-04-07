# Threads 高风险表达复发黑名单

本文件用于把已经重复触发风险的表达、句式和叙事钩子拉入黑名单，避免同类问题在不同帖子、不同 persona 或不同栏目里反复出现。

## 一、适用场景

- 同一表达在不同帖子里连续出问题
- 审稿、平台或声誉风险连续指向同类句式
- 某 persona 容易反复回到同一高风险钩子
- 需要给团队一个明确的“这类表达先别再碰”清单

## 二、黑名单级别

- `watch`
- `replace`
- `block`

## 三、最小判断维度

1. 复发次数与时间窗口
2. 风险类型是什么
3. 是否跨 persona / 栏目复发
4. 是否存在安全替代表达
5. 在什么条件下可以降级或解除

## 四、最小模板

```text
Threads 高风险表达复发黑名单：
- 表达 / 句式：
- 关联事件：
- 风险类型：
- 复发窗口：
- 涉及 persona / 栏目：
- 黑名单级别：watch | replace | block
- 允许替代表达：
- 禁止用法说明：
- 解除 / 降级条件：
- 责任回写文件：
```

## 五、使用规则

- 进入 `block` 的表达不得继续进入周排期或发布包
- 进入 `replace` 的表达必须先补替代表达，再继续内容生产
- 进入 `replace` 的表达应同步 `threads-high-risk-expression-replacement-library.md`
- 若同类表达开始通过近义变体绕行，应同步 `threads-high-risk-expression-variant-banlist.md`
- 若黑名单来自同一栏目，应同步 `threads-high-risk-column-cooldown-rules.md`
- 若多次复发且无安全替代，应回到 `threads-column-lifecycle-assessment.md`
- 黑名单结论若影响当前发布稿，应同步 `threads-review-publish-package.md`
