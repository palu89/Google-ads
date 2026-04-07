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

## 二、可选内容模板包

以下模块保留，但默认不进入主链路：
- `references/p0-persona-branding.md`
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

## 三、实践收敛规则

- 若一个模块长期只在 `SKILL.md` 中被列出，但没有进入近期真实工作链路，不再继续默认扩张它的规则。
- 若需求本质是 skill 维护、校验、审稿或 persona 治理，就不要默认加载内容模板包。
- 若用户只是新增 persona，不要自动跳入 `P0-P5` 内容写作链路。
- 若后续某类内容模板连续多次进入真实使用，再考虑把它从“可选”提升回默认链路。

## 四、结构处理原则

- 不因“暂时少用”就直接删除模板文件，优先降级为可选模块。
- 任何从“默认启用”改为“可选内容模板包”的调整，属于高影响改动，必须同步更新：
  - `SKILL.md`
  - `references/skill-validation.md`
  - `scripts/validate_platform_operations.py`
  - `agents/openai.yaml`
  - `CHANGELOG.md`
