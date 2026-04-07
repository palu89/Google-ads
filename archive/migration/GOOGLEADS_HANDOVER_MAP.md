# Google Ads Handover Map

Last updated: 2026-03-30
Owner: Codex
Status: active

## Purpose

This file is the current Google Ads keep / revise / promote / retire map for Codex takeover.

It exists so future work does not regress into:

- treating `/Users/palu/Claude code` as live truth
- reviving retired naming or retired governance shells
- promoting historical text directly into runtime without Codex gate

## Authority Layers

1. Codex canonical source:
   - `/Users/palu/.codex/skills/googleads`
2. OpenClaw runtime promoted subset:
   - `/Users/palu/.openclaw/workspace-googleads-palu/docs/reference/palu-ops-kb`
3. Historical asset source:
   - `/Users/palu/Claude code`
4. Historical GitHub repo:
   - `palu89/googleads-ops-kb`

Rule:

- GitHub and `/Users/palu/Claude code` can supply salvage material.
- Only `/Users/palu/.codex/skills/googleads` is allowed to become current source truth.
- Runtime promotion is always downstream from Codex canonical source.

## Keep

Keep as live Codex mainline:

- `/Users/palu/.codex/skills/googleads/SKILL.md`
- `/Users/palu/.codex/skills/googleads/GOOGLE_ADS_FIELD_MANUAL.md`
- `/Users/palu/.codex/skills/googleads/references/GOOGLEADS_REFERENCE_GOVERNANCE.md`
- `/Users/palu/.codex/skills/googleads/references/GOOGLEADS_MAINLINE_FINAL_STATE.md`
- `/Users/palu/.codex/skills/googleads/references/official-google-ads-policies.md`
- `/Users/palu/.codex/skills/googleads/references/official-financial-services-verification.md`
- `/Users/palu/.codex/skills/googleads/references/official-destination-requirements.md`
- `/Users/palu/.codex/skills/googleads/references/official-google-ads-code-repos.md`
- `/Users/palu/.codex/skills/googleads/references/official-search-ai-features.md`
- `/Users/palu/.codex/skills/googleads/references/ads-account-governance.md`
- `/Users/palu/.codex/skills/googleads/references/consent-privacy-minimum.md`
- `/Users/palu/.codex/skills/googleads/references/gtm-ga4-ads-event-spec.md`
- `/Users/palu/.codex/skills/googleads/references/geo-metrics-dashboard-template.md`
- `/Users/palu/.codex/skills/googleads/references/wa-clickid-bridge-sop.md`
- `/Users/palu/.codex/skills/googleads/references/whatsapp-oci-playbook.md`
- `/Users/palu/.codex/skills/googleads/references/internal-google-ads-appeal-template.md`
- `/Users/palu/.codex/skills/googleads/references/community-landing-page-playbook.md`
- `/Users/palu/.codex/skills/googleads/references/community-geo-notes.md`
- `/Users/palu/.codex/skills/googleads/references/real-time-guardrails.md`
- `/Users/palu/.codex/skills/googleads/references/refactor-protocol.md`
- `/Users/palu/.codex/skills/googleads/references/routing-priority.md`

Keep as runtime surfaces:

- `/Users/palu/.openclaw/agents/googleads-team`
- `/Users/palu/.openclaw/agents/googleads-antigravity-core`
- `/Users/palu/.openclaw/agents/googleads-t1-us-compliance`
- `/Users/palu/.openclaw/agents/googleads-t2-eastasia-growth`
- `/Users/palu/.openclaw/agents/googleads-t3-india-traffic`
- `/Users/palu/.openclaw/workspace-googleads-palu`

## Revise

Historical assets worth revision before any promotion:

- `/Users/palu/Claude code/00_shared/glossary.md`
- `/Users/palu/Claude code/01_account-architecture/gaql-schema.md`
- `/Users/palu/Claude code/06_feedback-iteration/error-codes.md`
- `/Users/palu/Claude code/04_appeal-communication/account-appeal-sop.md`
- `/Users/palu/Claude code/01_account-architecture/account-environment-sop.md`
- `/Users/palu/Claude code/03_landing-page-compliance/lp-compliance-audit.md`
- `/Users/palu/Claude code/02_campaign-structure/smart-bidding.md`

Revision rule:

- revise into Codex language
- collapse duplicates into existing canonical files where possible
- do not promote old folder structure itself
- prefer mechanism-first, checklist-light documentation

## Promote

Promotion candidates are allowed only through Codex source canonical layer.

Current likely promote queue after revision:

- glossary fragments that clarify terms used by the current field manual
- GAQL / schema fragments that are still missing from current canonical reference set
- stable appeal process fragments not already covered by `internal-google-ads-appeal-template.md`
- landing page audit heuristics that remain policy-aligned

Promotion path:

1. salvage from `/Users/palu/Claude code`
2. rewrite into `/Users/palu/.codex/skills/googleads`
3. verify against `GOOGLEADS_REFERENCE_GOVERNANCE.md`
4. only then promote selected subset into OpenClaw runtime reference layer

## Retire

Do not revive:

- old `googleads-palu` shell naming
- legacy pseudo-official file names
- historical sync / alignment / backup docs as live references
- direct Claude-to-runtime promotion
- the idea that GitHub is the current live truth for Google Ads
- old learning shells and duplicated retired batches

Historical files may remain on disk, but they are not live authority.

## Operational Rules

- Answer from current canonical reference first.
- Use `/Users/palu/Claude code` only as salvage source.
- Runtime teams should not silently become source-of-truth writers.
- New permanent Google Ads knowledge should land in Codex canonical source first.
