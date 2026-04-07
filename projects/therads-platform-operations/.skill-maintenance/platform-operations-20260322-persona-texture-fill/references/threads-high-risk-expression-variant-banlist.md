# Threads 高风险表达近义变体禁用表

本文件用于把已经确认高风险的表达扩展到近义词、变体句式和轻微改写版本，避免团队用“换几个字”绕开黑名单。

## 一、适用场景

- 原表达已经进入 `replace` 或 `block`
- 团队开始用近义说法反复碰同一类风险
- 同类风险表达在不同 persona 之间换壳复发
- 需要把禁止边界写得比单一原句更清楚

## 二、禁用等级

- `watch-variant`
- `ban-variant`

## 三、最小判断维度

1. 原表达与变体之间的语义距离
2. 变体是否仍保留原来的刺激、承诺或误导效果
3. 变体是否只做了表面替换
4. 哪些近义写法必须一并禁用
5. 哪些替代表达是允许保留的

## 四、最小模板

```text
Threads 高风险表达近义变体禁用：
- 原表达：
- 关联黑名单 / 替代表达：
- 禁用变体：
- 禁用等级：watch-variant | ban-variant
- 禁用原因：
- 允许保留的安全表达：
- 适用 persona / 栏目：
- 再次出现时处理动作：
```

## 五、使用规则

- 近义变体禁用不是词库游戏，重点看风险是否本质相同
- `ban-variant` 的写法不得继续进入审稿或排期
- 允许保留的表达应和 `threads-high-risk-expression-replacement-library.md` 保持一致
- 若近义变体已实际命中，应同步 `threads-variant-trigger-auto-writeback-rules.md`
- 若近义变体仍不断扩散，应回到 `threads-recurring-high-risk-expression-blacklist.md`
- 若禁用边界开始影响某栏目正常表达，应同步 `threads-column-lifecycle-assessment.md`
