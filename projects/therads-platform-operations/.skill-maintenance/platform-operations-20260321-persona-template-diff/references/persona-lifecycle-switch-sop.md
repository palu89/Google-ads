# Persona 启停与切换 SOP

本文件用于处理一个高影响动作：`persona` 的启用、停用、切换与回退。

如果不先定义这套 SOP，后面很容易出现：

- 主 persona 还没稳定就频繁换人设
- 内容已经按旧 persona 批量产出，却突然切到新 persona
- 旧 persona 停用了，但队列和排期还在沿用

## 一、适用场景

- 准备新增并启用新 persona
- 准备停用当前 persona
- 准备切换主 persona
- 准备把 `draft` persona 提升为 `active`
- 准备把 `active` persona 回退为 `inactive`

## 二、基本原则

1. `draft` 不直接变成对外主 persona
- 先完成字段、风险和适配检查

2. 主 persona 不频繁切换
- 若只是测试表达方式，优先走实验记录，不急着切换主 persona

3. 切换前先看影响范围
- 周排期
- 内容队列
- 已过审未发布内容
- 账号基线卡

4. 停用优先于删除
- 默认改 `inactive`
- 不直接删历史配置

## 三、启用流程

1. 检查 `persona-registry.md`
- 字段是否完整
- 是否仍有高风险占位符

2. 检查适配性
- 是否有清晰受众
- 是否有稳定权威来源
- 是否有可持续栏目

3. 小范围验证
- 优先用 `threads-content-experiment-log.md` 做 1 到 3 次样本验证

4. 通过后再启用
- 从 `draft` 改为 `active`
- 同步更新账号基线卡和栏目映射
- 如存在多个 `active` persona，再同步更新 `multi-persona-coexistence-governance.md`

## 四、切换流程

1. 先判断是“表达测试”还是“主 persona 切换”
- 若只是风格测试，不做主 persona 切换

2. 评估影响范围
- 哪些排期内容需要重写
- 哪些队列内容还能继续用
- 哪些审稿包需要失效

3. 更新主线文件
- `threads-account-baseline-card.md`
- `persona-content-pillar-map.md`
- `threads-weekly-content-schedule.md`
- `threads-content-queue-ledger.md`

4. 明确切换策略
- 立即切换
- 下周切换
- 仅在某栏目试运行
- 若切换后仍保留多个 `active` persona，则必须同步更新 `multi-persona-coexistence-governance.md`

## 五、停用与回退流程

1. 先改 `inactive`
2. 说明停用原因
3. 清点是否仍有未发布内容依赖该 persona
4. 如有，决定：
- 重写
- 延后
- 废弃

## 六、最小 SOP 模板

```text
Persona 启停 / 切换 SOP：
- 当前 persona：
- 目标 persona：
- 动作类型：activate | switch | deactivate | rollback
- 触发原因：
- 当前风险：
- 影响范围：
- 需要更新的文件：
- 队列受影响内容：
- 审稿受影响内容：
- 建议切换时间：
- 回退条件：
- 下一步动作：
```

## 七、常见错误

- 看到某篇效果好，就立刻切整号 persona
- `draft` 还没验证就当主 persona 上线
- 切换后没有同步周排期和内容队列
- 停用了 persona，但历史待发内容还按旧 persona 继续发
