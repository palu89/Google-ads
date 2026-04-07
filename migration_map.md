# Migration Map: Repository Restructuring
Generated: 2026-04-06
Objective: Transform scattered knowledge assets into a unified GitHub repository with clear governance.

## Overview
Current state shows multiple directories containing Google Ads knowledge, skill definitions, project snapshots, and migration/handoff materials. Need to reorganize into canonical structure with GitHub as source of truth.

## Classification
- **Google Ads knowledge**: `/Users/palu/Google ADS/` (primary), plus references in `/Users/palu/codex交互中心/`
- **Skill assets**: Currently minimal in `/Users/palu/skills/` (empty), but skill definitions embedded in various migration documents.
- **Project snapshots**: `/Users/palu/openclaw-audit/`, `/Users/palu/openclaw-dashboard/`, `/Users/palu/manas 项目主线/`
- **Migration/handoff/archive materials**: `/Users/palu/codex交互中心/collaboration/`, `/Users/palu/codex交互中心/backups/`
- **Registry/configuration**: `/Users/palu/openclaw-audit/openclaw_current.json`, `/Users/palu/.openclaw/`

## Migration Map

| Old Path | New Path | Entity Type | Action | Rationale | Status |
|----------|----------|-------------|--------|-----------|--------|
| `/Users/palu/Google ADS/GOOGLE_ADS_FIELD_MANUAL.md` | `/knowledge/googleads/official/field_manual_v3.0.md` | knowledge | migrate | Core Google Ads operational manual | migrated |
| `/Users/palu/Google ADS/SKILL.md` | `/skills/googleads-field-operations/SKILL.md` | skill | migrate | Skill definition for Google Ads operations | migrated |
| `/Users/palu/Google ADS/account_deep_scanner.js` | `/archive/googleads/scripts/account_deep_scanner.js` | script | archive | Historical script, not active knowledge | archived |
| `/Users/palu/Google ADS/pro-tools/finance_navigator.md` | `/knowledge/googleads/internal/finance_navigator.md` | knowledge | migrate | Internal tool documentation | migrated |
| `/Users/palu/Google ADS/pro-tools/keyword_expert.md` | `/knowledge/googleads/internal/keyword_expert.md` | knowledge | migrate | Internal tool documentation | migrated |
| `/Users/palu/Google ADS/pro-tools/lp_auditor.md` | `/knowledge/googleads/internal/lp_auditor.md` | knowledge | migrate | Internal tool documentation | migrated |
| `/Users/palu/Google ADS/pro-tools/script_architect.md` | `/knowledge/googleads/internal/script_architect.md` | knowledge | migrate | Internal tool documentation | migrated |
| `/Users/palu/Google ADS/references/agents_backup.md` | `/knowledge/googleads/hybrid/agents_backup.md` | knowledge | migrate | Reference material with interpretation | migrated |
| `/Users/palu/Google ADS/references/google-ads-appealtxt.md` | `/knowledge/googleads/official/appeal_process.md` | knowledge | migrate | Official appeal process | migrated |
| `/Users/palu/Google ADS/references/google-ads-finance-stock.md` | `/knowledge/googleads/official/finance_compliance.md` | knowledge | migrate | Official financial compliance | migrated |
| `/Users/palu/Google ADS/references/google-ads-policies.md` | `/knowledge/googleads/official/policies.md` | knowledge | migrate | Official policies | migrated |
| `/Users/palu/codex交互中心/GOOGLEADS_ROOT_DOC_FINAL_MIGRATION_20260319.md` | `/archive/migration/GOOGLEADS_ROOT_DOC_FINAL_MIGRATION_20260319.md` | migration | archive | Historical migration document | archived |
| `/Users/palu/codex交互中心/GOOGLEADS_SKILL_TIERING_20260320.md` | `/archive/migration/GOOGLEADS_SKILL_TIERING_20260320.md` | migration | archive | Historical migration document | archived |
| `/Users/palu/codex交互中心/collaboration/GOOGLEADS_GITHUB_FIRST_GOVERNANCE.md` | `/archive/migration/GOOGLEADS_GITHUB_FIRST_GOVERNANCE.md` | migration | archive | Historical governance planning | archived |
| `/Users/palu/codex交互中心/collaboration/GOOGLEADS_HANDOVER_MAP.md` | `/archive/migration/GOOGLEADS_HANDOVER_MAP.md` | migration | archive | Historical handoff | archived |
| `/Users/palu/codex交互中心/collaboration/GOOGLEADS_SYNC_WORKFLOW.md` | `/archive/migration/GOOGLEADS_SYNC_WORKFLOW.md` | migration | archive | Historical workflow | archived |
| `/Users/palu/codex交互中心/SYSTEM_SKILLS_MIGRATION_COMMAND_CHECKLIST_20260319.md` | `/archive/migration/SYSTEM_SKILLS_MIGRATION_COMMAND_CHECKLIST_20260319.md` | migration | archive | Historical checklist | archived |
| `/Users/palu/openclaw-audit/openclaw_current.json` | `/registry/model-profiles.yaml` (transformed) | registry | migrate | Model profiles and agent configuration | migrated |
| `/Users/palu/openclaw-audit/openclaw_legacy.json` | `/archive/audit/openclaw_legacy.json` | audit | archive | Legacy audit data | archived |
| `/Users/palu/openclaw-audit/doctor.json` | `/archive/audit/doctor.json` | audit | archive | Diagnostic data | archived |
| `/Users/palu/openclaw-audit/agents_list.json` | `/archive/audit/agents_list.json` | audit | archive | Historical agents list | archived |
| `/Users/palu/.openclaw/` (config dir) | `/archive/.openclaw/` | configuration | archive | Runtime configuration archived | completed |
| `/Users/palu/openclaw-dashboard/` | `/projects/openclaw-dashboard/` | project | migrate | Active project migrated | completed |
| `/Users/palu/manas 项目主线/` | `/projects/manas-mainline/` | project | migrate | Active project migrated | completed |
| `/Users/palu/Therads平台运营/` | `/projects/therads-platform-operations/` | project | migrate | Active project migrated | completed |
| `/Users/palu/skills/` (empty) | `/skills/` | skill | keep | Target directory already exists | migrated |
| `/Users/palu/Desktop/FunASR/` | (outside scope) | external | ignore | Unrelated speech recognition project | verified |

## Notes
1. **Active vs Archive**: Migration documents, batch records, historical backups belong in `/archive/`.
2. **Frontmatter Required**: All active knowledge files must have YAML frontmatter with required fields.
3. **Registry Transformation**: JSON configuration files need conversion to YAML registry format.
4. **Skill Extraction**: Skill definitions embedded in migration docs need to be extracted into `/skills/<skill-name>/` structure.
5. **Project State**: Each project must have CURRENT_STATE.md reflecting actual current state.

## Next Steps
1. Create target skeleton structure (Phase 1)
2. Migrate Google Ads knowledge with frontmatter (Phase 2)
3. Extract and organize skills (Phase 3)
4. Migrate projects with proper state documentation (Phase 4)
5. Implement compilation and validation scripts (Phase 5)
6. Archive legacy materials (Phase 6)

## Risk Areas
- Some skill definitions may be implicit in migration documents and need explicit extraction.
- Project current state may not be documented; require manual review.
- Frontmatter dates need accurate timestamps; use `unknown` where unknown.