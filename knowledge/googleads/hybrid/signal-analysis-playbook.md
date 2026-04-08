---
id: signal-analysis-playbook
entity_type: knowledge
domain: googleads
layer: hybrid
task_types: [signal_analysis, performance_diagnosis, rca]
priority: 1
source: internal-framework
last_verified: 2026-04-08
source_checked_at: 2026-04-08T00:00:00Z
content_updated_at: 2026-04-09T00:00:00Z
depends_on:
  - /knowledge/googleads/hybrid/signal-control-matrix.md
  - /knowledge/googleads/hybrid/signal-priority-method.md
status: active
summary: Provides a signal-based troubleshooting sequence for diagnosing Google Ads performance issues.
---

# Google Ads Signal Analysis Playbook

## Purpose

This playbook shows how to analyze a Google Ads issue through the signal lens.

The question is not:
- "What setting should I change?"

The question is:
- "Which signal is broken, weak, misrouted, or over-weighted?"

---

## Analysis Sequence

### Step 1 — Identify the broken signal
Determine whether the issue is caused by:
- bad conversion definition
- weak value feedback
- poor feed quality
- bad negatives
- weak segmentation
- poor landing page alignment
- poor consent / attribution completeness

### Step 2 — Classify the signal
Decide whether the signal is:
- advertiser-controlled
- partially controllable
- Google-controlled

### Step 3 — Locate the system layer
Identify where the signal is used:
- matching
- prediction
- auction
- delivery
- feedback

### Step 4 — Decide the intervention
Choose the highest-leverage intervention:
- fix tracking
- fix conversion definition
- fix value design
- fix feed structure
- fix segmentation
- fix exclusions
- fix semantic alignment

### Step 5 — Stop when the signal is good enough
Do not continue tuning low-leverage variables if the core signal problem remains unsolved.

---

## Common Signal Failures

### Failure 1: Garbage conversion input
The model learns from meaningless events.

Fix:
- correct primary conversion definitions
- remove shallow events from optimization

### Failure 2: Weak value differentiation
The system cannot distinguish high-value from low-value outcomes.

Fix:
- improve conversion value design
- add offline value feedback

### Failure 3: Noise pollution
The system sees too much irrelevant traffic.

Fix:
- negatives
- exclusions
- segmentation
- tighter boundaries

### Failure 4: Partial-control overreaction
The operator overestimates what can be changed with creative or micro-settings.

Fix:
- move up the signal hierarchy
- fix the stronger levers first

---

## Recommended RCA Order

1. Conversion definition
2. Value feedback
3. Offline feedback
4. Negatives / exclusions
5. Segmentation
6. Feed / theme structure
7. Landing page semantics
8. Audience signals
9. Creative changes
10. Micro-optimizations

---

## Output Standard

When using this playbook, the answer should always specify:
- what signal is broken
- what layer it affects
- what level of control exists
- what should be fixed first
- what should not be over-optimized
