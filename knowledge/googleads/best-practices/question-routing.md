---
id: question-routing
domain: googleads
layer: best-practices
task_types: [routing, retrieval, question_optimization]
priority: tier_1
source: internal-governance
last_verified: 2026-04-08
depends_on:
  - /registry/task-router.yaml
  - /knowledge/googleads/TASK_ROUTER.yaml
  - /knowledge/googleads/internal/knowledge-retrieval-framework.md
status: active
---

# Question Routing: How to Route Your Question Before Asking

## Purpose

Before you ask a question, you should route it to the correct knowledge files.
This document teaches the routing decision tree.

---

## Quick Routing Decision Tree

```
Start: "What is my question about?"

├─ Is it about official Google policy or mechanism?
│  ├─ YES: Route to OFFICIAL layer
│  └─ NO: Continue
│
├─ Is it about system interpretation or signal behavior?
│  ├─ YES: Route to HYBRID layer
│  └─ NO: Continue
│
├─ Is it about our internal workflow or project state?
│  ├─ YES: Route to INTERNAL layer
│  └─ NO: Continue
│
└─ Is it about how to ask a better question?
   ├─ YES: Route to BEST-PRACTICES layer
   └─ NO: Unclear routing → Ask clarification
```

---

## Routing by Task Type

Each task type maps to specific knowledge files.

### Routing 1: Audit / Compliance Task
```
Question category: "Is this compliant? Does this violate policy?"

Primary route: OFFICIAL
Load:
  - appeal_process.md
  - policies.md
  - finance_compliance.md

Secondary route: HYBRID
Load:
  - agents_backup.md (if field interpretation needed)

Stop condition: When you've cited the official policy and audit steps
```

### Routing 2: Explanation / Mechanism Task
```
Question category: "Why does the system do this? How do signals work?"

Primary route: HYBRID
Load:
  - agents_backup.md (system interpretation)

Secondary route: OFFICIAL
Load:
  - field_manual_v3.0.md (if official docs needed)

Stop condition: When you've explained the signal matrix and behavior
```

### Routing 3: Execution / Workflow Task
```
Question category: "How do we do this? What's the SOP?"

Primary route: INTERNAL
Load:
  - field_manual_v3.0.md (our playbook)
  - keyword_expert.md (our keyword SOP)
  - lp_auditor.md (our audit checklist)
  - script_architect.md (our script patterns)

Stop condition: When you've given step-by-step instructions
```

### Routing 4: Optimization / Query Task
```
Question category: "How should I ask this? How do I get better answers?"

Primary route: BEST-PRACTICES
Load:
  - question-framework.md
  - prompt-engineering-guide.md
  - question-routing.md (this file)

Stop condition: When you've optimized the question or demonstrated routing
```

### Routing 5: Decision Support
```
Question category: "What should we do? Which option is best?"

Primary route: INTERNAL
Load:
  - CURRENT_STATE.md (project state)
  - DECISIONS.md (precedent decisions)
  - field_manual_v3.0.md (our playbook)

Secondary route: OFFICIAL
Load:
  - policies.md (if decision affects compliance)

Stop condition: When you've given a specific recommendation
```

### Routing 6: API / Technical Question
```
Question category: "How do I use the API? What field is this?"

Primary route: OFFICIAL
Load:
  - field_manual_v3.0.md (official mechanism reference)
  - API documentation (external)

Secondary route: INTERNAL
Load:
  - script_architect.md (our code examples)

Stop condition: When you've shown the API call structure and constraints
```

---

## Routing by Keyword

Scan your question for keywords. They indicate the correct route:

| Keyword | Layer | Why |
|---------|-------|-----|
| "official"<br>"policy"<br>"violat"<br>"suspension"<br>"documented" | OFFICIAL | You want authoritative source |
| "mechanism"<br>"why"<br>"how does"<br>"signal"<br>"behavior" | HYBRID | You want system interpretation |
| "workflow"<br>"checklist"<br>"SOP"<br>"internal"<br>"step" | INTERNAL | You want operational guidance |
| "ask"<br>"prompt"<br>"question"<br>"optimize"<br>"route" | BEST-PRACTICES | You want meta-guidance |

---

## Multi-Layer Routing Example

### Example: Landing Page Audit

Your question: "I'm auditing a landing page and found [issue]. Is this a violation? How should we fix it?"

Routing breakdown:
1. **"Is this a violation?"** → OFFICIAL (policy definition)
2. **"How should we fix it?"** → INTERNAL (our audit SOP)
3. **"Why is this a violation?"** → HYBRID (system interpretation)

Load order:
1. Load `policies.md` (OFFICIAL)
2. Load `appeal_process.md` (OFFICIAL)
3. Load `lp_auditor.md` (INTERNAL - our audit checklist)
4. Load `agents_backup.md` if needed for interpretation (HYBRID)

Stop condition: When you've identified the violation, cited the policy, and given the audit steps to fix it

---

## Routing Mistakes to Avoid

### Mistake 1: Single-Layer Assumption
```
❌ "Just load the official docs" (misses why the system acts that way)
❌ "Just load internal SOP" (misses official boundaries)
✅ Route to multiple layers in priority order
```

### Mistake 2: Skipping Official
```
❌ Load HYBRID or INTERNAL without checking OFFICIAL first
✅ Always check OFFICIAL first if policy or compliance is involved
```

### Mistake 3: Wrong Layer Priority
```
❌ Load all layers equally
✅ Load primary layer fully, secondary layer conditionally
```

### Mistake 4: No Stop Signal
```
❌ "Keep loading files until something answers"
✅ Define stop condition before loading
```

---

## How to Verify Your Routing

After you've decided which files to load, ask:

1. **Is the primary layer correct?**
   - "Does my question require [official / hybrid / internal / best-practices] knowledge?"

2. **Is the priority order correct?**
   - "Should I load this file first, or does it depend on prior files?"

3. **Is the stop signal clear?**
   - "When should I stop loading more files?"

4. **Have I avoided full-repository scans?**
   - "Am I loading exactly the files needed, or am I over-loading?"

5. **Does this routing make sense to someone else?**
   - "Could another person understand my routing logic?"

---

## Routing Decision Support Matrix

| Scenario | Primary Layer | Secondary | Files to Load | Stop When |
|----------|---|---|---|---|
| "Is this compliant?" | OFFICIAL | INTERNAL | policies, appeal_process | You've cited policy and audit steps |
| "Why does system do X?" | HYBRID | OFFICIAL | agents_backup, field_manual | You've explained the signal matrix |
| "How do we do X?" | INTERNAL | OFFICIAL | (SOP file), field_manual | You've given step-by-step instructions |
| "How ask better?" | BEST-PRACTICES | INTERNAL | question-framework, question-routing | You've optimized the question |
| "Should we do X?" | INTERNAL | OFFICIAL | CURRENT_STATE, DECISIONS, policies | You've given a recommendation |
| "API syntax?" | OFFICIAL | INTERNAL | field_manual, script_architect | You've shown the API structure |

---

## Routing Output Format

When you've routed a question, output:

```
ROUTING ANALYSIS:

Your question: [Restate it]
Primary layer: [OFFICIAL/HYBRID/INTERNAL/BEST-PRACTICES]
Reason: [Why this layer?]

Files to load:
  1. [File] - [Why]
  2. [File] - [Why]
  
Secondary files (if needed):
  3. [File] - [Conditional: when/if]

Stop condition:
  When [specific success criteria]

Expected answer scope:
  Approximately [brief description]
```

---

## Final Rule

**Routing is better than searching.**

A well-routed question loads exactly the files needed.
A badly routed question wastes tokens on irrelevant files.

Always route before you ask.
