# Changelog

## 2026-03-18

### Added
- 新增 `references/persona-governance.md`，把多人设的字段、状态、占位符和启停机制独立出来治理。
- 新增 `references/threads-review-workflow.md`，作为 Threads 发布前审稿的统一入口。
- 新增 `references/skill-validation.md`，定义 skill 维护后的自动校验与人工校验要求。
- 新增 `scripts/validate_platform_operations.py`，用于结构与人设状态的自动校验。

### Changed
- 更新 `SKILL.md`，加入维护与校验链路、发布前强制审稿链路，以及新 reference 导航。
- 更新 `references/persona-registry.md`，扩展状态模型与字段模板，并将未补齐的人设改为 `draft` 管理。
- 更新 `references/p0-persona-branding.md`，把人设激活状态纳入发布前判断。
- 更新 `references/threads-platform-rules.md`、`references/threads-account-compliance.md`、`references/threads-copy-compliance.md`，补充证据分级与审稿衔接说明。
- 物理删除 12 个预置 `active` 人设，仅保留 `draft` 人设与人设治理机制。
- 更新人设匹配规则，当前无 `active` 人设时不再自动兜底。

### Impact
- `persona-01-zhang-shyi-chang` 在补齐运营字段前不再参与自动匹配，避免实名背书与占位符混用。
- 后续所有 Threads 规则口径调整都必须同步更新来源说明，并通过校验脚本。
- 当前 skill 不再内置可直接执行的预置人设；未新增并激活新 persona 前，不进行人设自动匹配。

### Validation
- `python3 scripts/validate_platform_operations.py /path/to/platform-operations`
- 预期结果：`pass`
