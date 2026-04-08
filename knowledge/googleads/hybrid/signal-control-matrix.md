---
id: signal-control-matrix
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
  - /knowledge/googleads/internal/knowledge-retrieval-framework.md
  - /knowledge/googleads/official/field_manual_v3.0.md
status: active
summary: Defines the core signal categories advertisers can control, shape, or inherit inside Google Ads optimization.
---

# Google Ads Signal Control Matrix

## Core Principle

Google Ads optimization is best understood as **signal engineering**.

The advertiser does not directly control the black-box model.
The advertiser controls:
- what signals enter the system
- how clean those signals are
- how the feedback loop is trained
- how the search space is constrained

The correct optimization question is not:
- "How do I force the algorithm to do X?"

The correct optimization question is:
- "Which signals can I control, which signals can I shape, and which signals are Google-controlled?"

---

## Signal Categories

### Advertiser-Controlled
Signals the advertiser can directly define or modify.

Examples:
- primary conversion definitions
- conversion value rules
- offline conversion imports
- merchant feed structure
- keyword / search theme structure
- negative keywords / brand exclusions
- campaign segmentation
- geo / language / device / schedule settings

### Partially Controllable
Signals the advertiser cannot fully define, but can influence.

Examples:
- audience signals
- creative semantics
- landing page semantics
- historical account performance
- consent quality
- first-party data completeness
- attribution window design
- data delay

### Google-Controlled
Signals generated or decided by Google at auction time or in the model.

Examples:
- auction-time query intent
- predicted CTR
- predicted conversion probability
- predicted conversion value
- cross-network delivery allocation
- modeled conversions
- auction dynamics under competition

---

## Priority Logic

### Highest Priority
Optimize first:
- primary conversion definition
- conversion value design
- offline conversion feedback
- feed / keyword / search theme structure
- negatives / exclusions
- campaign segmentation

These signals directly shape what the system learns.

### Secondary Priority
Optimize next:
- audience signals
- creative quality
- landing page semantics
- device / geo / time settings
- account stability

These signals can improve system direction, but they do not replace core signal quality.

### Low Priority
Avoid over-optimizing:
- minor copy changes
- small device bid tweaks
- short-term budget oscillation
- guessing internal PMax budget splits

These usually have low leverage compared with signal quality and feedback structure.

---

## System-Specific Application

### Broad Match
Broad Match is not primarily a keyword problem.
It is a signal-retrieval problem.

Control the system through:
- strong conversion definitions
- clean negatives
- high-quality landing page semantics
- stable feedback signals

Do not assume you can directly command exact query interpretation.

### Smart Bidding
Smart Bidding optimizes the objective function you define.

Control the system through:
- correct primary conversions
- conversion value quality
- offline feedback
- stable data flow

If the conversion signal is wrong, the bidding model will optimize the wrong target.

### PMax
PMax is a high-dimensional signal distribution system.

Control the system through:
- feed quality
- conversion value
- asset quality
- exclusions
- audience signals
- landing page alignment

Do not assume you can manually control exact network allocation.

---

## Optimization Rules

1. Start with controllable inputs.
2. Use partial-control signals as direction setters.
3. Do not chase black-box outputs directly.
4. Train the system with better inputs.

---

## Signal Control Heuristic

Evaluate each signal using four dimensions:
- Control Force
- Impact Force
- Feedback Speed
- Observability

Recommended priority is highest when all four are strong.

### High-priority signals usually have:
- direct control
- strong model impact
- fast feedback
- easy measurement

### Low-priority signals usually have:
- weak control
- indirect impact
- slow feedback
- low observability

---

## Risks / Red Lines

- Do not confuse Google-controlled signals with advertiser-controlled signals.
- Do not treat audience signals as hard targeting in PMax or Broad Match.
- Do not optimize shallow events as primary conversions.
- Do not overload the system with conflicting conversion definitions.
- Do not assume small UI tweaks can fix a signal-quality problem.
- Do not attempt to manage PMax by guessing exact network splits.

---

## Practical Use Cases

Use this matrix when:
- diagnosing poor lead quality
- building campaign architecture
- designing conversion tracking
- structuring PMax feeds and assets
- writing strategy prompts
- deciding what to fix first in RCA

This matrix is a prioritization framework, not a Google official policy.
