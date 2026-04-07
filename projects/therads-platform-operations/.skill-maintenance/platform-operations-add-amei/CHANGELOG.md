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
- 新增 `taiwan-stock-captain` 作为当前启用中的台股复合型 persona，并恢复默认自动匹配入口。
- 新增 `old-cat-taiwan-stocks` 作为主打分點、主力、洗盤與盤後數據拆解的 `active` persona。
- 新增 `laoqiu-88` 作为主打炒股技巧、操盘指标、選股策略与股票知識入口的 `active` persona。
- 新增 `amei-exchange-retirement-journal` 作为“阿美/證交所退休日誌”的 `draft` persona；因含机构履历式背书且未核对，暂不进入自动匹配与对外成稿。

### Impact
- `persona-01-zhang-shyi-chang` 在补齐运营字段前不再参与自动匹配，避免实名背书与占位符混用。
- 后续所有 Threads 规则口径调整都必须同步更新来源说明，并通过校验脚本。
- 旧预置执行人设已清空，当前启用中的 `active` personas 为 `taiwan-stock-captain`、`old-cat-taiwan-stocks` 与 `laoqiu-88`。
- 在用户未明确指定其他 persona 时，默认仍以 `taiwan-stock-captain` 作为兜底执行人设。
- 当前 `active` personas 已扩展为 `taiwan-stock-captain`、`old-cat-taiwan-stocks` 与 `laoqiu-88`；其中“老貓 / 分點 / 主力 / 洗盤 / 盤後數據”相关输入会优先命中 `old-cat-taiwan-stocks`。
- `laoqiu.88 / 老丘 / 股票知識這裡都有 / 記得點關注哦` 等品牌识别语会优先命中 `laoqiu-88`，但不会以泛化的“选股策略/股票知识”单词强制兜底。
- `amei-exchange-retirement-journal` 当前仅作为内部草案保存，不改变现有 `active` persona 池；任何带有“證交所退休”式机构背景的对外使用，都需先完成核对后再激活。

### Validation
- `python3 scripts/validate_platform_operations.py /path/to/platform-operations`
- 预期结果：`pass`
