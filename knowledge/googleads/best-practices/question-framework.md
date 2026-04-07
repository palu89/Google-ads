---
id: question-framework
domain: googleads
layer: best-practices
task_types: [prompt_engineering, knowledge_retrieval, question_optimization]
priority: tier_2
source: internal-governance
last_verified: 2026-04-08
depends_on:
  - /knowledge/googleads/internal/knowledge-retrieval-framework.md
status: active
---

# Question Framework: How to Ask for Best Results

## Purpose

This guide defines how to structure questions so that AI agents can retrieve and answer with maximum accuracy and minimum token waste.

---

## Question Structure

All questions should follow this pattern:

```
[CONTEXT] + [LAYER REQUEST] + [TASK TYPE] + [SPECIFIC QUESTION] + [CONSTRAINTS]
```

### Example 1: Official Mechanism
```
Context: We need to optimize landing page quality score compliance
Layer: official
Task: Understand policy
Question: What are the official requirements for misrepresentation in Google Ads?
Constraint: I need official documented policy only, not interpretation
```

### Example 2: Operational Workflow
```
Context: We're auditing a landing page for one of our clients
Layer: internal
Task: Execute audit
Question: What steps should I follow according to our internal LP audit checklist?
Constraint: Use our SOPs, not general best practices
```

### Example 3: System Understanding
```
Context: We're trying to improve keyword intent matching
Layer: hybrid
Task: Understand mechanism
Question: How do Google's semantic and lexical matching work together in keyword matching?
Constraint: I need the technical interpretation, not official docs
```

### Example 4: Question Optimization
```
Context: I'm about to ask a complex question about PMax bidding
Layer: best-practices
Task: Optimize question
Question: How should I structure my question to get the most accurate answer about PMax signal control?
Constraint: Help me figure out what to ask before I ask it
```

---

## Layer Selection Decision Tree

Use this tree to pick the correct layer:

1. **Do I need the official Google policy or documented behavior?**
   - YES → Load `official/`
   - NO → Continue to 2

2. **Do I need to understand how the system actually works or interprets policy?**
   - YES → Load `hybrid/`
   - NO → Continue to 3

3. **Do I need our internal SOP, workflow, or operational state?**
   - YES → Load `internal/`
   - NO → Continue to 4

4. **Do I need help asking a better question or optimizing my query?**
   - YES → Load `best-practices/`
   - NO → No match found

---

## Question Anti-Patterns

**Do NOT ask:**
- "Just give me all the information about X" (causes full-file loading)
- "I'm not sure what I need" (requires clarification first)
- "What do you think about X?" (mixes official with opinion)
- "Show me everything in the knowledge base" (violates Rule 1)

**DO ask:**
- "From the official policy, what is the constraint on X?"
- "Show me the internal SOP for X and tell me the step-by-step workflow"
- "Why does the system behave this way? Show me the signal interpretation"
- "How should I ask this question to get the best answer?"

---

## Metadata-Based Retrieval

Every file in the repository has metadata tags:

- `id` — unique file identifier
- `layer` — official | hybrid | internal | best-practices
- `task_types` — what types of tasks this file supports
- `priority` — tier_1 (must load) | tier_2 (conditional) | tier_3 (reference)
- `pack_memberships` — what knowledge packs this file belongs to
- `depends_on` — what other files must be loaded first

When constructing a question, you can also specify:
```
Load files tagged: layer=internal, task_types=audit, priority=tier_1
```

---

## Effective Question Templates

### Template 1: Policy Question
```
[Layer] question: What is the official [Google Ads/policy/documented] [mechanism]?
Context: [Why am I asking]
Evidence I need: [Direct quotes / policy reference / enforcement definition]
```

### Template 2: Mechanism Question
```
[Layer] question: How does [system behavior] work?
Context: [Operational situation]
Evidence I need: [Signal interpretation / control matrix / mechanism explanation]
```

### Template 3: Workflow Question
```
[Layer] question: What is the approved workflow for [task]?
Context: [What I'm trying to accomplish]
Evidence I need: [SOP / checklist / decision tree]
```

### Template 4: Query Optimization
```
[Layer] question: Help me optimize my question about [topic]
Current phrasing: [Your original question]
Target: [What kind of answer would be most useful]
Constraint: [Official / mechanism / workflow / optimization]
```

---

## Stop Signal

The AI is answering correctly when:

1. ✅ The answer cites exactly 1-3 files, not more
2. ✅ The answer includes an evidence map
3. ✅ The answer separates official / hybrid / internal / best-practice advice
4. ✅ The answer states what it does NOT know
5. ✅ The answer suggests a follow-up question if needed

The AI is overcomplicating when:
- ❌ The answer loads 5+ files without justification
- ❌ The answer has no evidence map
- ❌ The answer conflates different layers
- ❌ The answer continues after the question is answered
