---
id: signal-priority-method
entity_type: knowledge
domain: googleads
layer: hybrid
task_types: [strategy_engineering, performance_diagnosis, rca, campaign_build, signal_analysis]
priority: 1
source: internal-framework
last_verified: 2026-04-08
source_checked_at: 2026-04-08T00:00:00Z
content_updated_at: 2026-04-09T00:00:00Z
depends_on:
  - /knowledge/googleads/hybrid/signal-control-matrix.md
status: active
summary: Explains how to rank Google Ads optimization work by leverage, control, impact, and feedback speed.
---

# Google Ads Signal Priority Method

## Purpose

This document defines how to prioritize optimization work in Google Ads.

The goal is not to optimize everything.
The goal is to optimize the highest-leverage signals first.

---

## Priority Formula

Use this heuristic to rank signals:

**Priority Score = Control Force × Impact Force × Feedback Speed × Observability**

Each dimension can be scored from 1 to 5.

### Dimension Definitions

#### Control Force
How directly the advertiser can change the signal.

#### Impact Force
How strongly the signal affects learning, prediction, bidding, or delivery.

#### Feedback Speed
How quickly the system reflects the signal change in performance data.

#### Observability
How easy it is to see whether the signal change worked.

---

## Priority Bands

### Band 1 — Highest Priority
Signals with:
- direct control
- high model impact
- fast feedback
- clear observability

Examples:
- primary conversion definition
- conversion value design
- offline conversion imports
- feed quality
- negatives / exclusions
- campaign segmentation

### Band 2 — Medium Priority
Signals with:
- partial control
- meaningful influence
- moderate feedback speed
- decent observability

Examples:
- audience signals
- creative semantics
- landing page semantics
- device / geo / time settings
- consent quality

### Band 3 — Lower Priority
Signals with:
- low control
- weak direct impact
- slow feedback
- low observability

Examples:
- minor copy changes
- tiny bid modifier changes
- speculative PMax split analysis
- guessing internal model weights

---

## Prioritization Rules

1. Fix input quality before fixing model behavior.
2. Fix feedback quality before touching bidding strategy.
3. Fix signal boundaries before expanding traffic.
4. Fix structural issues before cosmetic issues.
5. Fix conversion integrity before optimization tuning.

---

## Common Mistakes

- Optimizing creatives before fixing conversion definitions
- Editing budget before cleaning feedback signals
- Changing many variables at once
- Treating weak signals as primary levers
- Confusing partial control with full control

---

## Use Cases

Use this method when:
- performance suddenly drops
- lead quality degrades
- PMax begins to drift
- Smart Bidding optimizes the wrong outcome
- Broad Match expands into bad intent
- RCA needs a fix order

---

## Recommended Decision Order

When diagnosing a problem, inspect signals in this order:

1. Primary conversion integrity
2. Value feedback integrity
3. Offline feedback quality
4. Negatives / exclusions
5. Campaign segmentation
6. Feed / search theme structure
7. Audience and semantic signals
8. Creative and page semantics
9. Device / geo / time adjustments
10. Micro-tuning
