---
id: knowledge-retrieval-framework
entity_type: knowledge
domain: googleads
layer: internal
task_types: [routing, retrieval, governance, prompt_engineering, project_state]
priority: 1
source: internal-governance
last_verified: 2026-04-08
source_checked_at: 2026-04-08T00:00:00Z
content_updated_at: 2026-04-09T00:00:00Z
depends_on:
  - /registry/repo.yaml
  - /registry/model-profiles.yaml
  - /knowledge/googleads/TASK_ROUTER.yaml
  - /knowledge/googleads/ACTIVE_INDEX.yaml
status: active
summary: Defines how Google Ads knowledge should be routed, loaded, and governed for accurate low-token retrieval.
---

# Google Ads Knowledge Retrieval Framework

## 1. Purpose

This document defines how the Google Ads knowledge base must be structured and called so that both AI agents and human operators can retrieve the correct information quickly, precisely, and consistently.

The framework is designed to prevent:
- full-repository scanning
- wrong-layer reading
- unnecessary token consumption
- routing confusion
- stale or contradictory answers
- mixing official mechanisms with heuristics or internal SOPs

---

## 2. Core Principle

**The repository must be called by behavior, not by theme.**

That means every question must first be classified by task type, then routed to the correct knowledge layer, and only then should the relevant files be loaded.

The system must always follow this order:

1. Classify the task
2. Read registry state
3. Route to the correct layer
4. Load only required files
5. Stop when enough evidence is available
6. Output with evidence mapping

---

## 3. Knowledge Layers

The Google Ads knowledge base is divided into four operational layers.

### 3.1 Official Layer
Contains official Google Ads documentation, help pages, API references, policy pages, and official release notes.

Use this layer when the question is:
- What does Google officially say?
- How does a specific API or policy work?
- What is the documented boundary or constraint?

### 3.2 Hybrid Layer
Contains system-level interpretation, signal analysis, matrix frameworks, and mechanism-to-strategy bridges.

Use this layer when the question is:
- Why does the system behave this way?
- Which signals are controllable?
- How do multiple Google mechanisms interact?
- What is the operational interpretation of a black-box system?

### 3.3 Internal Layer
Contains SOPs, project governance, operational playbooks, audit checklists, and internal decision logic.

Use this layer when the question is:
- How do we operate internally?
- What is the project state?
- What is the approved workflow?
- How should this task be executed in our system?

### 3.4 Best-Practices Layer
Contains question frameworks, prompt engineering guides, query optimization guidance, and retrieval patterns.

Use this layer when the question is:
- How should I ask the question?
- How do I get the best answer from AI or Google?
- What is the best query structure?
- How should I route the request?

---

## 4. Retrieval Rules

### Rule 1: Do not scan the full repository
AI agents must not read the whole repository by default.

They must first read:
- `/registry/repo.yaml`
- `/registry/model-profiles.yaml`
- `/knowledge/googleads/TASK_ROUTER.yaml`
- `/knowledge/googleads/ACTIVE_INDEX.yaml`

### Rule 2: Load by route, not by guess
The task router must determine which files are loaded.

The AI must not guess which files are relevant based on folder names alone.

### Rule 3: Use packs for common tasks
Frequently used task bundles should be stored as knowledge packs.

Examples:
- `lp-audit-pack`
- `keyword-intent-pack`
- `pmax-bidding-pack`
- `question-optimization-pack`
- `tracking-attribution-pack`

### Rule 4: Stop when enough evidence is available
The AI must stop loading more content once:
- the answer can be produced with sufficient confidence
- the token budget is approaching the configured limit
- additional files would not materially improve the result

### Rule 5: Never treat tier_3 as mandatory full-text
Tier 3 files are reference material.
They may be summarized or selectively loaded only when necessary.

---

## 5. Standard Call Flow

All tasks must follow this flow:

```
User question
↓
Task classification
↓
Registry lookup
↓
Task router selection
↓
Active index lookup
↓
Pack loading
↓
Tiered file loading
↓
Stop check
↓
Answer output
```

---

## 6. Required Metadata for Every File

Every knowledge file must include frontmatter.

Minimum required fields:

- `id`
- `domain`
- `layer`
- `task_types`
- `priority`
- `source`
- `last_verified`
- `depends_on`
- `status`

Recommended generated fields:
- `token_estimate`
- `embedding_hash`
- `pack_memberships`
- `reverse_dependencies`

---

## 7. File Classification Rules

### 7.1 Official files
Must contain:
- official URLs
- policy text
- documented constraints
- direct citations

### 7.2 Hybrid files
Must contain:
- signal interpretation
- system models
- operational frameworks
- supported inference

### 7.3 Internal files
Must contain:
- SOPs
- workflows
- decision trees
- project state logic

### 7.4 Best-practices files
Must contain:
- question patterns
- prompt frameworks
- retrieval strategies
- routing guidance

---

## 8. Task Routing Principles

Each task type should map to a minimal reading set.

### Example: LP audit
Load:
- official destination requirements
- official misrepresentation policy
- hybrid LP quality vs policy risk
- internal LP checklist

### Example: keyword intent analysis
Load:
- official keyword matching docs
- hybrid semantic vs lexical matching
- internal negative keyword workflow

### Example: PMax / bidding analysis
Load:
- official Smart Bidding docs
- hybrid signal control matrix
- internal bidding playbook

### Example: question optimization
Load:
- best-practices question framework
- best-practices prompt engineering guide
- best-practices routing doc

---

## 9. Stop Rules

The system must stop loading additional knowledge when any of the following is true:

- the task can be answered with current evidence
- the next file would only repeat prior content
- the confidence level is already sufficient
- token budget is below the configured threshold
- the request requires a missing file that does not exist

If a required file is missing, the correct output is:
- `Missing data`
- `Assumption`
- or `Need clarification`

The system must not silently substitute unrelated files.

---

## 10. Evidence Map Requirement

Every output must include an evidence map.

The evidence map must show:
- which file supported which claim
- which claims were official
- which claims were inference
- which claims were operational judgment

If the evidence map cannot be populated, the answer is incomplete.

---

## 11. Retrieval Priorities

In case of conflict, use this order:

1. Official Google documentation
2. Registry and routing state
3. Hybrid mechanism files
4. Internal SOPs
5. Best-practices guidance
6. Archived materials only if explicitly requested

---

## 12. Forbidden Behaviors

The AI must not:
- read the entire repository by default
- confuse official mechanisms with heuristics
- treat archived content as active truth
- invent missing routes
- silently use unrelated files as substitutes
- continue loading once enough evidence is available

---

## 13. Operational Goal

The goal of this framework is not to make the repository larger.

The goal is to make the repository:
- faster to call
- easier to route
- safer for AI usage
- less prone to hallucination
- more consistent across tools and operators

---

## 14. Final Rule

If a question can be answered from a smaller, more specific set of files, the system must choose the smaller set.

More reading is not automatically better.
Correct reading is better.
