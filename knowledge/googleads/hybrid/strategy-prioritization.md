---
id: strategy-prioritization
entity_type: knowledge
domain: googleads
layer: hybrid
task_types: [strategy_engineering, performance_diagnosis, campaign_build]
priority: 1
source: internal-framework
last_verified: 2026-04-08
source_checked_at: 2026-04-08T00:00:00Z
content_updated_at: 2026-04-09T00:00:00Z
depends_on:
  - /knowledge/googleads/hybrid/signal-control-matrix.md
  - /knowledge/googleads/hybrid/signal-priority-method.md
status: active
summary: Converts signal analysis into an execution order for what to fix first, later, or not at all.
---

# Google Ads Strategy Prioritization

## Purpose

This document converts signal analysis into operational prioritization.

It answers:
- what to fix first
- what to fix later
- what not to over-optimize
- what is likely to matter most for account performance

---

## Core Strategy Logic

### Stage 1 — Protect the Learning Loop
Before scaling, ensure the system learns from correct signals.

Focus on:
- primary conversion definition
- conversion value design
- offline conversion imports
- consistent feedback flow

### Stage 2 — Constrain the Search Space
Reduce irrelevant traffic before trying to improve efficiency.

Focus on:
- negatives
- brand exclusions
- campaign segmentation
- geo / language / device boundaries

### Stage 3 — Improve Signal Quality
Increase the quality of the signals the model sees.

Focus on:
- feed quality
- landing page semantics
- creative relevance
- audience signal quality
- consent completeness

### Stage 4 — Optimize for Scale
Only after the system is stable should you optimize for expansion.

Focus on:
- Broad Match expansion
- PMax scaling
- Smart Bidding target tuning
- budget allocation across valid segments

---

## Operational Priority Rules

1. Protect signal integrity first.
2. Protect feedback integrity second.
3. Protect segmentation integrity third.
4. Scale only after the first three are stable.

---

## What Not to Do

- Do not scale a broken feedback loop.
- Do not expand traffic before conversion definitions are correct.
- Do not treat weak signals as structural fixes.
- Do not optimize cosmetics before fixing model inputs.
- Do not assume PMax or Smart Bidding can rescue bad data.

---

## Strategy by System

### Broad Match
Use Broad Match only when:
- conversion tracking is correct
- negatives are in place
- feedback quality is stable
- search intent boundaries are understood

### Smart Bidding
Use Smart Bidding only when:
- conversion data is trustworthy
- value feedback is meaningful
- learning is not constantly reset
- account structure is stable

### PMax
Use PMax only when:
- feed structure is clean
- assets are relevant
- conversion goals are aligned
- exclusions are in place
- control signals are sufficiently strong

---

## Decision Principle

If a signal has:
- high control
- high impact
- fast feedback
- clear observability

it should be prioritized first.

If not, it should be treated as secondary.
