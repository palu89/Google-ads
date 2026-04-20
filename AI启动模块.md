# AI启动模块

Updated: 2026-04-10

This file is a fast onboarding wrapper.

Canonical execution rules live in:
- `AGENT_BOOTSTRAP.md` for routing and loading discipline
- `OPERATING_SOP.md` for lifecycle and system-boundary rules

If any summary in this file ever conflicts with those two files, follow the canonical documents.

## Zero-Ambiguity Onboarding (Required)

Do not start from README summaries or generic repo scans.
Do this exact order:

1. Read `AGENT_BOOTSTRAP.md`
2. Read `registry/repo.yaml`
3. Read `knowledge/googleads/TASK_ROUTER.yaml`
4. Match the task to one route
5. Load only the listed knowledge files and skills

Knowledge-file resolution rule (mandatory):

6. Resolve each `knowledge_files` ID using `registry/googleads.yaml`
7. Load by the resolved `path` (official/hybrid/internal), not by guessed folder
8. Never assume all route knowledge files live under `knowledge/googleads/official/`

If any required file is missing or cannot be parsed, stop and report the missing file.

## Canonical Boundary

For system boundary and lifecycle rules, read:
- `AGENT_BOOTSTRAP.md`
- `OPERATING_SOP.md`

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
- Exact resolved file paths from `registry/googleads.yaml`
- Exact skills to load

C. Execution Proof:
- Respond in this format:
	Mechanism -> Judgment -> Action -> Risks -> Missing Data -> Evidence Map

D. Compliance Proof:
- State you did not scan the whole repository
- State you only loaded routed files
- If missing files exist, stop and report instead of guessing
- State which lifecycle stage the current task is in: Intel / Promotion / GitHub PR / Runtime Sync / Notion Merged
- If the lifecycle stage cannot be proven from repository state or task state, output `Unknown` and list the missing evidence instead of guessing

Pass criteria:
- Must select a concrete route from TASK_ROUTER.yaml
- Must name concrete skills and knowledge files
- Must resolve each `knowledge_files` ID to real paths via `registry/googleads.yaml` (no folder guessing)
- Must include Evidence Map with real file paths
- Must not answer with only quick-start summary
- Lifecycle stage must be evidence-backed; otherwise output `Unknown`
```

## Why Previous Onboarding Failed

Running only:
- `git pull origin main`
- `cat AI启动模块.md`

proves repository access and sync only. It does not prove protocol initialization, route selection, or skill execution.

## One-Minute Acceptance Checklist

- Read all 3 required files in sequence
- Selected one concrete route in `knowledge/googleads/TASK_ROUTER.yaml`
- Loaded only route-listed knowledge and skills
- Resolved each route `knowledge_files` ID via `registry/googleads.yaml` to concrete paths
- Produced `Evidence Map` with real file paths
- Explicitly confirmed no full-repo scan
- Reported an evidence-backed lifecycle stage, or `Unknown` with missing evidence

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

- Scripts / automation -> route `script_generation` -> `googleads-scripts`
- Keyword / negatives -> route `keyword_audit` -> `googleads-keyword-expert`
- Landing page / quality score -> route `landing_page_audit` -> `googleads-audit`
- Financial verification / G2 / regulator -> route `financial_compliance` -> `googleads-verify`
- India financial verification / SEBI / G2RS -> route `india_financial_verification` -> `googleads-verify`
- Suspension / rejection / appeal -> route `appeal_process` -> `googleads-appeal`
- Appeal letter / comments box -> route `appeal_text_generation` -> `googleads-appealtxt`
- Onboarding / protocol / repo governance audit -> route `system_governance` -> `system/skill-vetter`
- Skill install / update / governance -> route `skill_management` -> `system/cocoloop`
- Summaries of long material -> route `document_summarization` -> `system/summarize`
- GA4 / measurement / reporting -> route `analytics_measurement` -> `system/google-analytics-api`

## GitHub Handoff Rule

If a skill is present in this repository and registered in `registry/skills.yaml`, other AI tools should be able to use it immediately after reading `AGENT_BOOTSTRAP.md` and `knowledge/googleads/TASK_ROUTER.yaml`.

## System Truth Rule

- Do not treat Notion notes as merged execution truth.
- Do not treat local-only edits as final state.
- Do not claim completion until GitHub and runtime are synchronized.
