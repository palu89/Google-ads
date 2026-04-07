# Google Ads Root Doc Final Migration

最后更新: 2026-03-19

## 当前判断

Google Ads `skills/` 根目录中的知识 markdown 已完成最终迁移。

## 本轮完成项

- `googleads-field-manual.md` 已迁入 `skills/docs/reference/`
- `googleads-modules.md` 已迁入 `skills/docs/reference/`
- 所有活跃 `SKILL.md`、知识节点、工作流配置和模型配置中的引用已改到新路径

## 当前根目录状态

`skills/` 根目录当前只保留：

- `INSTALLATION_REMINDER.sh`
- `SIMPLE_REMINDER.sh`
- `SYSTEM_LAYER_SKILLS_BOUNDARY_NOTICE_20260319.md`
- `skill_dispatcher.py`

## 当前 reference 层状态

`skills/docs/reference/` 当前承接全部非运行时参考 markdown，包括：

- `ads-compliance.md`
- `googleads-orchestrator.md`
- `googleads-ai-audit.md`
- `googleads-workflow.md`
- `googleads-knowledge-system.md`
- `skills-summary.md`
- `googleads-field-manual.md`
- `googleads-modules.md`

## 结果

Google Ads `skills/` 目录的分层现在已经清晰：

1. 正式项目 skill 目录
2. `docs/` 文档与 reference 层
3. `verified/` 核验层
4. 根目录轻量脚本与边界说明层
