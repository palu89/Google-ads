# System Skills Management Index

Last Updated: 2026-04-09

## Current System Tier Skills

| Skill Name | Path | Purpose |
|------------|------|---------|
| `skill-vetter` | [skills/system/skill-vetter/SKILL.md](skills/system/skill-vetter/SKILL.md) | Vet new external skills before installation or sync. |
| `web-search` | [skills/system/web-search/SKILL.md](skills/system/web-search/SKILL.md) | Perform live web lookups for current information, news, and competitor research. |
| `cocoloop` | [skills/system/cocoloop/SKILL.md](skills/system/cocoloop/SKILL.md) | Install, update, retire, and classify skills across system, runtime, and project layers. |
| `summarize` | [skills/system/summarize/SKILL.md](skills/system/summarize/SKILL.md) | Summarize URLs, PDFs, exports, and long documents before deeper analysis. |
| `google-analytics-api` | [skills/system/google-analytics-api/SKILL.md](skills/system/google-analytics-api/SKILL.md) | Query GA4 properties, data streams, and reports for measurement workflows. |
| `self-improving-agent` | [skills/self-improving-agent/SKILL.md](skills/self-improving-agent/SKILL.md) | Meta-reflection, error logging, and repository memory consolidation. |

## Installation Rules

1. Vet every external skill with `skill-vetter` first.
2. Put cross-project reusable skills under `skills/system/`.
3. Put Google Ads execution skills under `skills/`.
4. After installation, update `registry/skills.yaml`, `knowledge/googleads/TASK_ROUTER.yaml`, and this index.
5. Push the repo only after YAML and path validation pass.
