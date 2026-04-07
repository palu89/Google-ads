# Changelog

## 2026-03-22

### Reset
- 从零重建极简 skill，只保留单一赚钱爆帖入口。
- 新增 `references/viral-profit-template.md` 作为唯一模板。
- 新增 `references/content-output-enforcement.md` 作为唯一执行闸门。
- 重写 `SKILL.md`、`agents/openai.yaml` 与 `scripts/validate_platform_operations.py`。
- 收紧入口格式为 `人设：任意标签/模版1/日期`，并规定后续只要出现 `模版1` 就默认走唯一模板；若补 `事件` 与 `方向`，则优先按用户给定内容写。
- 进一步收窄为：`模版1` 是唯一核心指令；`人设`、`日期` 只作为可选上下文。
- 新增 `模版1` 顺序硬规则、外壳清理与输出前自检，避免正文回退成旧包装或乱序稿。
- 锁定 `template-01-golden-sample.md` 为唯一主样本，明确“第一版为什么对、后面为什么歪”，后续只能做槽位替换，不能再自由改写。
- 新增 `references/codex-content-creation-prompt.md`，明确 Codex 中直接进行内容创作时的执行提示词。
- 删除 `template-01-golden-sample.md`，改为 `template-01-engine-map.md`，不再保留主样本锁定思路，只保留结构地图、槽位替换和反复用边界。
- 把 `模版1` 的替换强度提升为至少替换 8 项关键槽位，并增加当前会话污染规避。

### Impact
- 后续只要发送 `模版1`，就按唯一模板直接起稿；`人设`、`日期`、`事件`、`方向` 都只是附加参数。

### Validation
- `python3 scripts/validate_platform_operations.py /path/to/platform-operations`
