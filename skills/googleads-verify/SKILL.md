---
name: googleads-verify
description: Financial-services verification and regulator-alignment workflow for Google Ads. Use when the task is G2 verification, license evidence, regulator mapping, or financial policy readiness.
---

# Google Ads Verify

Use this skill for financial-services verification and pre-launch compliance packaging.

## Use this for
- G2 / advertiser verification readiness
- FCA, ASIC, CySEC, or equivalent regulator alignment
- License number, entity, and domain consistency checks
- Packaging evidence before submission or re-review

## Required inputs
- target geo
- legal entity name
- license or registration number
- promoted domain
- current policy or verification blocker

## Workflow
1. Identify the regulator and verification path.
2. Check whether entity name, domain, legal docs, and license evidence align.
3. List missing evidence and submission blockers.
4. Produce a copy-ready remediation checklist.
5. If appeal text is needed, hand off to `googleads-appealtxt`.

## Output format
Current judgment -> verification status -> missing evidence -> submission steps -> risks -> evidence map
