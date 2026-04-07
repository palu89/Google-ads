# Changelog

## 2026-03-18

### Added
- 新增 `references/persona-governance.md`，把多人设的字段、状态、占位符和启停机制独立出来治理。
- 新增 `references/threads-review-workflow.md`，作为 Threads 发布前审稿的统一入口。
- 新增 `references/skill-validation.md`，定义 skill 维护后的自动校验与人工校验要求。
- 新增 `scripts/validate_platform_operations.py`，用于结构与人设状态的自动校验。
- 新增 `references/usage-scope.md`，定义默认维护核心与可选内容模板包的实际使用边界。
- 新增 `references/content-output-enforcement.md`，把内容生成前检查、生成后复核和最小执行记录收敛成强制闸门。

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
- 新增 `retired-ajie-taiwan-veteran` 作为“退休阿傑｜15年台股老兵”的 `active` persona，并为其补充较窄的自动识别信号。
- 新增 `laozhou-kline-veteran` 作为“老周｜K線老兵”的 `active` persona，并把 `tina065547` 与其老兵叙事纳入窄匹配信号。
- 新增 `comeback-trader-15y` 作为“翻身交易者 📈｜股市15年”的 `active` persona，并将低谷、债务与重建叙事纳入识别信号。
- 新增 `master-di-short-swing` 作为“帝師”的 `active` persona，并把其短線波段、離場紀律与資產目标叙事纳入窄匹配信号。
- 新增 `laowang-taiwan-rebuild` 作为“台股老汪”的 `active` persona，并将其从赌徒心态走向交易修正的叙事纳入识别信号。
- 新增 `stock-analyst-placeholder` 作为“股票分析师”的 `draft` persona；因仅提供通用名称，当前按占位人设管理。
- 调整 `SKILL.md` 的默认定位：从“默认全栈内容生产”收敛为“默认维护核心 + 可选内容模板包按需启用”。
- 更新 `agents/openai.yaml`，使 implicit invocation 也优先落在维护、审稿、校验与变更记录，而不是默认日更内容生产。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，新增“实际使用对齐”校验，避免继续默认扩张长期闲置模块。
- 更新 `SKILL.md`、`references/p0-persona-branding.md`、`references/p1-trading-psychology.md`、`references/p2-morning-brief.md`、`references/p3-intraday-tracker.md`、`references/p4-postmarket-recap.md`、`references/p5-evening-lessons.md`、`references/macro-news-synthesizer.md` 与 `references/single-stock-deepdive.md`，要求内容输出先读 `content-output-enforcement.md`。
- 更新 `references/skill-validation.md` 与 `scripts/validate_platform_operations.py`，新增“内容模板必须挂接执行闸门”的校验。

### Impact
- `persona-01-zhang-shyi-chang` 在补齐运营字段前不再参与自动匹配，避免实名背书与占位符混用。
- 后续所有 Threads 规则口径调整都必须同步更新来源说明，并通过校验脚本。
- 旧预置执行人设已清空，当前启用中的 `active` personas 为 `taiwan-stock-captain`、`old-cat-taiwan-stocks`、`laoqiu-88`、`retired-ajie-taiwan-veteran`、`laozhou-kline-veteran`、`comeback-trader-15y`、`master-di-short-swing` 与 `laowang-taiwan-rebuild`。
- 在用户未明确指定其他 persona 时，默认仍以 `taiwan-stock-captain` 作为兜底执行人设。
- 当前 `active` personas 已扩展为 `taiwan-stock-captain`、`old-cat-taiwan-stocks`、`laoqiu-88`、`retired-ajie-taiwan-veteran`、`laozhou-kline-veteran`、`comeback-trader-15y`、`master-di-short-swing` 与 `laowang-taiwan-rebuild`；其中“老貓 / 分點 / 主力 / 洗盤 / 盤後數據”相关输入会优先命中 `old-cat-taiwan-stocks`。
- `laoqiu.88 / 老丘 / 股票知識這裡都有 / 記得點關注哦` 等品牌识别语会优先命中 `laoqiu-88`，但不会以泛化的“选股策略/股票知识”单词强制兜底。
- `amei-exchange-retirement-journal` 当前仅作为内部草案保存，不改变现有 `active` persona 池；任何带有“證交所退休”式机构背景的对外使用，都需先完成核对后再激活。
- “退休阿傑 / 15年台股老兵 / 提早登出職場 / 股市不缺英雄，缺的是老兵 / 過來人的避坑指南”会优先命中 `retired-ajie-taiwan-veteran`；本次未用泛化的“財務自由 / 產業趨勢 / 籌碼”单词做强匹配，以降低串人设风险。
- “老周 / K線老兵 / tina065547 / 市場如戰場 / 活到最後的人才是贏家”会优先命中 `laozhou-kline-veteran`；本次未用泛化的“K 線 / 紀律 / 順勢”单词单独兜底。
- “翻身交易者 / 股市15年 / 曾經跌入低谷 / 背負債務 / 人生重新開始”会优先命中 `comeback-trader-15y`；本次未把“交易 / 學習 / 生活”这类泛词设为强匹配。
- “帝師 / 56歲 / 交易股票31年 / 進場有賺可自行離場 / 存股人生 / 資產達到5000萬”会优先命中 `master-di-short-swing`；本次未把“短線 / 波段 / 存股”单词单独设为强匹配，以降低串人设风险。
- “台股老汪 / 老汪 / 曾沉迷賭博 / 人生低谷 / 研究股市 / 財富自由”会优先命中 `laowang-taiwan-rebuild`；本次未把“家破人亡 / 股市秘密 / 財富自由”直接固化为默认可复用表达，而是收敛为反赌徒心态与交易修正叙事。
- `stock-analyst-placeholder` 当前只作为占位草案保存，不改变现有 `active` persona 池；若后续补齐定位、受众与语气字段后，再决定是否激活。
- 审计发现 `p1-trading-psychology.md`、`p2-morning-brief.md`、`p3-intraday-tracker.md`、`p4-postmarket-recap.md`、`p5-evening-lessons.md`、`macro-news-synthesizer.md` 与 `single-stock-deepdive.md` 目前主要停留在 `SKILL.md` 声明层，未进入近期真实维护主链路。
- 现在默认只加载 persona 治理、Threads 审稿、校验与变更记录相关模块；内容模板仍保留，但仅在用户明确要求内容运营或模板验证时启用。
- 本轮进一步确认：规则未执行的根因不是文件缺失，而是内容模板长期只有“写法说明”，没有“生成前必须检查、生成后必须复核”的执行闸门。
- 现在内容输出若未接入 `content-output-enforcement.md`，会在结构与校验层同时失败，避免再次出现“规则存在但实际没跑”。

### Validation
- `python3 scripts/validate_platform_operations.py /path/to/platform-operations`
- 预期结果：`pass`
