# Quick Start For AI

Updated: 2026-04-09

## Start Here

1. Read `AGENT_BOOTSTRAP.md`
2. Read `registry/repo.yaml`
3. Read `knowledge/googleads/TASK_ROUTER.yaml`
4. Match the task to one route
5. Load only the listed knowledge files and skills

## Project Skills

| Skill | Use When |
|------|----------|
| `googleads-field-operations` | broad Google Ads operations, routing, field-manual questions |
| `googleads-audit` | landing page, policy, quality-score, and compliance reviews |
| `googleads-keyword-expert` | keyword intent, negatives, search-term cleanup |
| `googleads-scripts` | scripts, automation, monitoring, guardrails |
| `googleads-verify` | licensing, G2, regulator alignment, finance verification |
| `googleads-appeal` | suspension/rejection remediation and appeal packaging |
| `googleads-appealtxt` | final comments-box text and appeal letters |

## System Skills

| Skill | Use When |
|------|----------|
| `system/skill-vetter` | vetting new external skills before install or sync |
| `system/web-search` | current web facts, competitor checks, live research |
| `system/cocoloop` | installing, updating, retiring, and classifying skills |
| `system/summarize` | summarizing URLs, PDFs, exports, and long docs |
| `system/google-analytics-api` | GA4 reporting, properties, data streams, analytics state |
| `self-improving-agent` | reflection, learning capture, and error consolidation |

## Fast Routes

- Scripts / automation -> `googleads-scripts`
- Keyword / negatives -> `googleads-keyword-expert`
- Landing page / quality score -> `googleads-audit`
- Financial verification / G2 / regulator -> `googleads-verify`
- Suspension / rejection / appeal -> `googleads-appeal`
- Appeal letter / comments box -> `googleads-appealtxt`
- Skill install / update / governance -> `system/cocoloop`
- Summaries of long material -> `system/summarize`
- GA4 / measurement / reporting -> `system/google-analytics-api`

## GitHub Handoff Rule

If a skill is present in this repository and registered in `registry/skills.yaml`, other AI tools should be able to use it immediately after reading `AGENT_BOOTSTRAP.md` and `knowledge/googleads/TASK_ROUTER.yaml`.
