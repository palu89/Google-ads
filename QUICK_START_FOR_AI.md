# Quick Start For AI

Updated: 2026-04-09

## Zero-Ambiguity Onboarding (Required)

Do not start from README summaries or generic repo scans.
Do this exact order:

1. Read `AGENT_BOOTSTRAP.md`
2. Read `registry/repo.yaml`
3. Read `knowledge/googleads/TASK_ROUTER.yaml`
4. Match the task to one route
5. Load only the listed knowledge files and skills

If any required file is missing or cannot be parsed, stop and report the missing file.

## Copy-Paste Prompt For New AI Tools

Use this exact prompt when onboarding any new AI tool:

```text
You are onboarding to the Google Ads OS repository.

Mandatory sequence (no skipping):
1) Read AGENT_BOOTSTRAP.md
2) Read registry/repo.yaml
3) Read knowledge/googleads/TASK_ROUTER.yaml

Then execute this task: "我需要做金融牌照验证与G2准备".

Output requirements:
A. Initialization Proof:
- List 6 key protocol rules you extracted.

B. Routing Proof:
- Route name selected
- Pattern hits
- Exact knowledge_files to load
- Exact skills to load

C. Execution Proof:
- Respond in this format:
	Mechanism -> Judgment -> Action -> Risks -> Missing Data -> Evidence Map

D. Compliance Proof:
- State you did not scan the whole repository
- State you only loaded routed files
- If missing files exist, stop and report instead of guessing

Pass criteria:
- Must select a concrete route from TASK_ROUTER.yaml
- Must name concrete skills and knowledge files
- Must include Evidence Map with real file paths
- Must not answer with only quick-start summary
```

## Why Previous Onboarding Failed

Running only:
- `git pull origin main`
- `cat QUICK_START_FOR_AI.md`

proves repository access and sync only. It does not prove protocol initialization, route selection, or skill execution.

## One-Minute Acceptance Checklist

- Read all 3 required files in sequence
- Selected one concrete route in `knowledge/googleads/TASK_ROUTER.yaml`
- Loaded only route-listed knowledge and skills
- Produced `Evidence Map` with real file paths
- Explicitly confirmed no full-repo scan

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
