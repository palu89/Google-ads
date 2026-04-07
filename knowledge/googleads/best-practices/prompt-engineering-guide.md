---
id: prompt-engineering-guide
domain: googleads
layer: best-practices
task_types: [prompt_engineering, ai_interaction, knowledge_optimization]
priority: tier_2
source: internal-governance
last_verified: 2026-04-08
depends_on:
  - /knowledge/googleads/internal/knowledge-retrieval-framework.md
  - /knowledge/googleads/best-practices/question-framework.md
status: active
---

# Prompt Engineering Guide for Google Ads Questions

## Purpose

This guide teaches how to structure prompts to AI agents so they retrieve and answer Google Ads questions with maximum accuracy and minimum hallucination.

---

## Core Principles

1. **Tell the AI what layer to use** — official / hybrid / internal / best-practices
2. **Tell the AI what task type** — audit / explain / modify / update_state
3. **Tell the AI what you already know** — so it doesn't repeat it
4. **Tell the AI what you don't know** — so it doesn't guess
5. **Tell the AI when to stop** — "Stop when you have answered the core question"

---

## Prompt Template v1: Simple Question

```
[LAYER] [TASK TYPE]:

Question: [Your question]
Context: [Why you're asking]
Evidence required: [What kind of source do you want?]
Stop condition: [When is the answer complete?]
```

### Example
```
OFFICIAL POLICY + AUDIT:

Question: What are the official Google Ads policies on landing page misrepresentation?
Context: We're auditing a client's landing page and need to know what violations are automatic suspensions
Evidence required: Direct quotes from official policy documentation only
Stop condition: When you've listed all automatic suspension triggers
```

---

## Prompt Template v2: Complex Multi-Layer Question

```
[PRIMARY LAYER] + [SECONDARY LAYER]:

Primary question: [Main inquiry]
Sub-question 1: [Officially, what happens?]
Sub-question 2: [Why? (mechanism)]
Sub-question 3: [How do we handle internally?]

Evidence required: [Official / Hybrid / Internal]
Stop condition: [You've answered all three sub-questions]
```

### Example
```
HYBRID + INTERNAL:

Primary question: How do we handle keyword intent mismatches in our client accounts?
Sub-question 1: What is the official keyword matching mechanism?
Sub-question 2: What are the signals that determine broad vs exact match behavior?
Sub-question 3: What is our internal negative keyword workflow?

Evidence required: Hybrid (mechanism explanation), then Internal (our SOP)
Stop condition: When you've shown the signal matrix and our checklist
```

---

## Prompt Template v3: Hypothesis Testing

```
[LAYER] + HYPOTHESIS VALIDATION:

Hypothesis: [What you think is true]
Evidence I have: [What you already know]
Evidence I need: [What would prove/disprove the hypothesis]

Question: Is my hypothesis correct according to [layer]?
Stop condition: When you've confirmed or refuted the hypothesis with evidence
```

### Example
```
OFFICIAL + HYPOTHESIS VALIDATION:

Hypothesis: Google's Smart Bidding system uses conversion window data to adjust bids
Evidence I have: I know Smart Bidding uses conversion history
Evidence I need: Official documentation of the conversion window role

Question: Does Google officially state that conversion window impacts Smart Bidding behavior?
Stop condition: When you've found or confirmed the official position
```

---

## Prompt Template v4: Decision Support

```
[INTERNAL] + DECISION SUPPORT:

Situation: [What's actually happening]
Options: [Possible actions A, B, C]
Constraints: [Limitations you face]
Goal: [What outcome you want]

Question: According to our internal SOP, which option should we choose?
If no SOP exists, what do the official mechanisms suggest?
Stop condition: When you've recommended an option with justification
```

### Example
```
INTERNAL + DECISION SUPPORT:

Situation: Client's campaign has high conversion volume but very high CPA
Options: 
  A) Switch to ECPC instead of Manual CPC
  B) Increase bid by 10% and monitor
  C) Enable Performance Max on subset of budget

Constraints: Client wants to stay on Manual CPC if possible

Goal: Lower CPA while maintaining control

Question: What does our internal playbook say for this scenario?
Stop condition: When you've given a clear recommendation with rationale
```

---

## Anti-Patterns in Prompt Engineering

### Anti-Pattern 1: Forcing AI to Confabulate
```
❌ "I need the answer in 1 sentence"
❌ "Make it sound official"
❌ "Guess what I'm really asking"
✅ "Stop when you've answered the core question, even if it takes 5 sentences"
```

### Anti-Pattern 2: Vague Boundaries
```
❌ "Tell me everything about landing pages"
❌ "I need comprehensive information"
✅ "I need the official LP policy, and stop when you've listed all suspension triggers"
```

### Anti-Pattern 3: Layer Confusion
```
❌ "Is this a good idea?" (mixes all layers)
❌ "What should we do?" (unclear which SOP to use)
✅ "Officially, can we do X? And internally, how have we handled this?"
```

### Anti-Pattern 4: No Stopping Rule
```
❌ "Keep answering until I say stop"
❌ "More information is always better"
✅ "Stop when the question is answered. More files ≠ better answer"
```

---

## Effective Stop Signals

Tell the AI to stop when:

- "Stop after you've cited 2-3 files"
- "Stop when your token estimate exceeds 2000"
- "Stop when you've answered the core question"
- "Stop if you cannot find the answer in official sources"
- "Stop when you need to ask a clarifying question"

---

## Layer Specification Keywords

### Official Layer
- "officially"
- "according to Google"
- "in the documentation"
- "the policy says"
- "the API reference states"

### Hybrid Layer
- "the mechanism is"
- "why the system"
- "how signals interact"
- "the interpretation is"
- "the black-box behavior suggests"

### Internal Layer
- "our SOP is"
- "our workflow is"
- "we decided to"
- "our playbook says"
- "our project state is"

### Best-Practices Layer
- "how to ask"
- "optimize this question"
- "what's the best way to retrieve"
- "routing guidance"
- "prompt engineering"

---

## Validation Checklist

After you write a prompt, check:

- [ ] Does it specify the layer (official / hybrid / internal / best-practices)?
- [ ] Does it specify the task type (audit / explain / modify / update_state)?
- [ ] Does it have a clear stop signal?
- [ ] Does it show what you already know?
- [ ] Does it show what you don't know?
- [ ] Would a different person understand what you're asking?
- [ ] Could the AI interpret it multiple ways?

---

## Examples of Good Prompts

### Good Prompt 1
```
OFFICIAL + AUDIT:
I'm reviewing a landing page for compliance. 
What are the official Google Ads policies on [specific policy area]?
Load only official policy documentation.
Stop after listing all automatic suspension triggers for this area.
```

### Good Prompt 2
```
HYBRID + EXPLAIN:
I want to understand how Google's keyword matching actually works.
Question: What are the signals that determine broad vs exact match behavior?
Load the signal interpretation and control matrix.
Stop when you've explained the decision tree.
```

### Good Prompt 3
```
INTERNAL + DECISION:
We have a client with [situation].
What does our internal SOP say to do?
If no SOP exists, cite the official mechanism instead.
Load: knowledge/googleads/internal/ files tagged with [task_type]
Stop with a clear recommendation.
```

---

## Measuring Prompt Quality

A prompt is high-quality when the answer:

1. ✅ Uses exactly 1-3 files (not more)
2. ✅ Includes an evidence map
3. ✅ Separates official / hybrid / internal
4. ✅ States what it doesn't know
5. ✅ Answers in the scope you specified
6. ✅ Cites sources explicitly
7. ✅ Matches the layer you requested

A prompt needs work when the answer:
- ❌ Uses 5+ files without justification
- ❌ Has no evidence map
- ❌ Confuses the layers
- ❌ Continues past the stop signal
- ❌ Includes information you didn't ask for
