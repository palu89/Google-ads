# Google Ads Skill Tiering

Last updated: 2026-03-20

## Current Judgment

The Google Ads project now uses a formal tiering result instead of treating every skill directory as equal.

## Final Tiering Result

| Skill | Tier | Current Decision |
|---|---|---|
| `googleads-orchestrator` | Production Core | Default Google Ads routing wrapper |
| `ads-compliance` | Production Core | Default copy-level compliance preview wrapper |
| `googleads-knowledge` | Production Core | Default project knowledge navigation wrapper |
| `googleads-script-doctor` | Formal Extension | Formal script troubleshooting and deployment-governance wrapper |
| `googleads-appeal` | Formal Extension | Formal rejection, suspension, and appeal-package wrapper |
| `googleads-audit` | Formal Extension | Formal landing-page and destination audit wrapper |
| `conversion-chain-health` | Formal Extension | Formal GTM-to-GA4-to-Ads chain diagnosis wrapper |
| `budget-guard` | Formal Extension | Formal budget pacing and guardrail wrapper |
| `script-conflict-check` | Formal Extension | Formal multi-script conflict detection wrapper |
| `googleads-verify` | Formal Extension | Formal finance-verification navigation wrapper |
| `googleads-scripts` | Formal Extension | Formal Google Ads scripts generation wrapper |
| `googleads-keyword-expert` | Formal Extension | Formal keyword-intent audit wrapper |
| `googleads-playbook` | Formal Extension | Formal standard strategy and playbook lookup wrapper |
| `googleads-csv` | Formal Extension | Formal local CSV parsing and mapping wrapper |
| `googleads-copy` | Formal Extension | Formal copy-safe export and formatting wrapper |
| `googleads-indexshell` | Formal Extension | Formal workspace shell and iframe-navigation wrapper |
| `googleads-checklist` | Formal Extension | Formal checklist progress and export wrapper |
| `googleads-exclude` | Formal Extension | Formal exclude-item and SOP wrapper |
| `googleads-engine` | Formal Extension | Formal scoring and recommendation-logic wrapper |
| `googleads-qa` | Formal Extension | Formal validation and regression-summary wrapper |
| `googleads-workflow` | Formal Extension | Keep as workflow-definition and organization layer, now aligned to active runtime routes |
| `googleads-ai-audit` | Prototype / Candidate | Keep as AI-audit prototype line only |
| `ads-compliance-checker` | Archive Candidate | Keep out of the default production route and retain only as historical experimental code |

## Short Rationale

- `googleads-orchestrator`
  - accepted as production core because its current claimed role is routing and packaging, and the evidence matches that role
- `ads-compliance`
  - accepted as production core because the project wrapper points to a real execution layer in `/Users/palu/.openclaw/skills/ads-compliance`
- `googleads-knowledge`
  - accepted as production core because it matches the current docs-layer reality and formal knowledge index
- `googleads-script-doctor`
  - kept as a formal extension because Codex source route intent is clear and the runtime wrapper can now safely absorb script-failure triage without claiming execution access
- `googleads-appeal`
  - kept as a formal extension because it is operationally important, but still depends on human evidence quality and should not be overstated as an automated appeal system
- `googleads-audit`
  - kept as a formal extension because Codex source exists and the runtime wrapper role is clear, but it is not yet promoted into default production core
- `conversion-chain-health`
  - kept as a formal extension because the source-side chain diagnosis is clear and current runtime docs provide enough evidence to expose it as a bounded diagnosis route
- `budget-guard`
  - kept as a formal extension because the source-side pacing guidance is clear, but it remains a guardrail and recommendation layer rather than a proven automatic optimizer
- `script-conflict-check`
  - kept as a formal extension because the source-side conflict-detection checklist is clear and runtime packaging can safely expose it as a bounded governance route
- `googleads-verify`
  - kept as a formal extension because Codex source exists and it cleanly fills the finance-verification route gap
- `googleads-scripts`
  - kept as a formal extension because Codex source exists and it provides a bounded script-generation route without replacing script-doctor
- `googleads-keyword-expert`
  - kept as a formal extension because Codex source exists and it provides a bounded keyword-intent route
- `googleads-playbook`
  - kept as a formal extension because it narrows strategy and process lookup into a reusable route without replacing the broader `googleads-knowledge` navigation role
- `googleads-csv`
  - kept as a formal extension because it exposes a bounded local data-cleanup and mapping route without claiming a full data platform
- `googleads-copy`
  - kept as a formal extension because it exposes copy-safe formatting and export packaging without claiming direct clipboard control
- `googleads-indexshell`
  - kept as a formal extension because Codex source route intent is clear and the runtime wrapper can safely absorb shell-level navigation and iframe issues without pretending to own the whole UI stack
- `googleads-checklist`
  - kept as a formal extension because it exposes a bounded progress, save/restore, and export surface without claiming to be a full task platform
- `googleads-exclude`
  - kept as a formal extension because it exposes bounded exclude-item and SOP maintenance while keeping scoring logic separate from policy-risk interpretation
- `googleads-engine`
  - kept as a formal extension because it gives the runtime a bounded scoring and recommendation route without claiming to be an autonomous optimizer
- `googleads-qa`
  - kept as a formal extension because it provides bounded validation and regression guidance without overstating itself as a full automated testing platform
- `googleads-workflow`
  - kept as a formal extension because it has real workflow definitions and has now been aligned to active runtime route names, but it still is not a verified live executor
- `googleads-ai-audit`
  - retained as prototype because it has meaningful implementation assets but not enough production proof
- `ads-compliance-checker`
  - downgraded to archive candidate because it is not formally integrated and current finance-sensitive smoke behavior is not trustworthy enough for production use

## Operating Rule

Default project route:

- `googleads-orchestrator`
- `ads-compliance`
- `googleads-knowledge`

Extension only:

- `googleads-script-doctor`
- `googleads-appeal`
- `googleads-audit`
- `conversion-chain-health`
- `budget-guard`
- `script-conflict-check`
- `googleads-verify`
- `googleads-scripts`
- `googleads-keyword-expert`
- `googleads-playbook`
- `googleads-csv`
- `googleads-copy`
- `googleads-indexshell`
- `googleads-checklist`
- `googleads-exclude`
- `googleads-engine`
- `googleads-qa`
- `googleads-workflow`

Prototype only:

- `googleads-ai-audit`

Not on default route:

- `ads-compliance-checker` (archive candidate)

Operational note:

- archive candidates may still retain historical directories, but they must be excluded from active formal project skill counting
