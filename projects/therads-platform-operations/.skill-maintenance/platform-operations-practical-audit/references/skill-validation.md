# Skill 校验规则

本文件用于校验 `platform-operations` skill 的结构完整性、规则一致性和可维护性。

每次修改 `SKILL.md`、`references/`、`persona-registry.md`、审稿模板或 Threads 合规规则后，都要跑一次本校验。

## 一、自动校验

运行：

```bash
python3 scripts/validate_platform_operations.py /path/to/platform-operations
```

自动校验至少覆盖：
- `SKILL.md` 中引用的 `references/*.md` 是否真实存在
- `persona-registry.md` 的 `active` 人设是否含占位符
- 人设状态值是否在允许范围内
- `CHANGELOG.md` 是否存在且包含日期化记录
- Threads 审稿与校验 reference 是否存在
- `references/usage-scope.md` 与 `agents/openai.yaml` 是否存在
- skill 是否已明确“默认维护核心、内容模板按需启用”

## 二、人工校验

### 1. 结构完整性
- `SKILL.md` 的路由规则和资源导航是否一致
- 新规则是否放进合适的 reference，而不是继续堆在 `SKILL.md`

### 2. 实际使用对齐
- `SKILL.md` 是否已明确默认入口是维护核心，而不是默认进入 `P0-P5`
- `references/usage-scope.md` 是否把默认核心与可选内容模板包分开
- `agents/openai.yaml` 的描述与默认 prompt 是否与当前实际使用一致
- 若某模块长期只在 `SKILL.md` 中声明，却未进入真实工作链路，是否已降级为可选而不是继续默认扩张

### 3. Threads 证据完整性
- 平台、账号、文案规则是否优先引用官方来源
- 跨平台推断是否都标了 `Inference`
- 若更新了规则判断，是否同步更新“已核对日期”或来源说明

### 4. 人设治理完整性
- 自动匹配是否只面向 `active`
- 若当前刻意不保留 `active` 人设，规则里是否明确写了“不自动兜底”
- 有无把未补齐高风险字段的人设误设为 `active`
- 新字段是否和 `persona-governance.md` 保持一致

### 5. 审稿流程完整性
- 发布前审稿是否仍覆盖平台、账号、文案、人设、去重、连续性六层
- 输出模板是否仍保留结论、分级、依据和改写建议

### 6. 变更记录
- 是否更新 `CHANGELOG.md`
- 若属于高影响改动，是否写清影响范围

## 三、高影响改动

以下改动属于高影响，必须在变更记录中写明影响范围：
- Threads 平台规则判断口径变化
- 账号合规高风险项变化
- 文案风险分级变化
- 人设自动匹配门槛变化
- `active` / `draft` 状态定义变化
- 发布前审稿模板变化
- 默认使用边界变化：维护核心与可选内容模板包的划分变化

## 四、通过标准

### `pass`
- 自动校验无错误
- 人工校验无未解释风险

### `fail`
- 任一引用文件缺失
- 任一 `active` 人设含未解决占位符
- 当前无 `active` 人设，但规则未明确禁止自动兜底
- Threads 规则更新但无来源说明
- 高影响改动未记录
- `SKILL.md` 仍把 `P0-P5` 日更内容生产描述为默认入口
- `agents/openai.yaml` 与 `SKILL.md` 的实际使用定位不一致

## 五、校验输出模板

```text
skill 校验结果：
- 结构完整性：
- 实际使用对齐：
- 人设注册表：
- Threads 证据：
- 审稿流程：
- 变更记录：
- 结论：pass | fail
- 待修复项：
```
