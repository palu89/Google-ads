# Skill 校验规则

这个 skill 已从零重建为极简版。

自动校验只检查：
- `SKILL.md`
- `CHANGELOG.md`
- `agents/openai.yaml`
- `references/content-output-enforcement.md`
- `references/viral-profit-template.md`
- `references/template-01-engine-map.md`
- `references/codex-content-creation-prompt.md`
- `references/skill-validation.md`

同时强制检查：
- 目录只保留当前最小文件集
- `SKILL.md` 只保留 `模版1` 核心指令入口

运行：

```bash
python3 scripts/validate_platform_operations.py /path/to/platform-operations
```
