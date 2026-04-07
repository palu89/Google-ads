---
id: api-query-best-practices
domain: googleads
layer: best-practices
task_types: [api_query, technical_question, script_generation]
priority: tier_2
source: internal-governance
last_verified: 2026-04-08
depends_on:
  - /knowledge/googleads/official/field_manual_v3.0.md
  - /knowledge/googleads/internal/knowledge-retrieval-framework.md
status: active
---

# API Query Best Practices

## Purpose

This guide explains how to structure questions about Google Ads API when seeking accurate technical answers.

---

## Query Structure for API Questions

When asking about Google Ads API behavior, include:

1. **API Version** — Which version (v16, v17, etc.)?
2. **Object Type** — Campaign, Ad Group, Ad, etc.?
3. **Operation Type** — GET, SET, CREATE, UPDATE?
4. **Specific Field** — Which field is in question?
5. **Expected Behavior** — What should happen?
6. **Observed Behavior** — What actually happens?

### Example Good Query
```
Google Ads API v17, Campaign object, SET operation:
Field: bidding_strategy_type
Expected: Can set directly on campaign create
Observed: Throws deprecation error
Question: What is the correct way to set bidding strategy on new campaigns?
```

### Example Bad Query
```
"How do I use the API?"
```

---

## Common API Question Patterns

### Pattern 1: Field Availability
```
Is field [X] available in API v[Y] for object [Z]?
If yes, what are the constraints?
If no, what is the deprecation timeline?
What is the recommended alternative?
```

### Pattern 2: Operation Availability
```
Can I [CREATE/UPDATE/SET] [field] on [object] via API?
If yes, what are the constraints?
If no, what is the workaround?
```

### Pattern 3: Behavior Confirmation
```
When I [operation], does the system [expected behavior]?
Or does it [observed behavior]?
Which is correct according to official documentation?
```

### Pattern 4: Bulk Operation
```
Can I perform [operation] on [count] items in one request?
What is the batch size limit?
What is the rate limit?
What error handling should I implement?
```

---

## Where to Find Answers

Different API questions map to different knowledge layers:

| Question Type | Layer | Primary Source |
|---|---|---|
| "Is field X documented?" | official | Google Ads API reference |
| "Why does the API behave this way?" | hybrid | Signal interpretation |
| "What's our internal API script pattern?" | internal | SOP and code examples |
| "How should I ask the API question?" | best-practices | This file |

---

## Query Debugging Checklist

Before asking an API question, verify:

- [ ] I have specified the API version
- [ ] I have specified the resource/object type
- [ ] I have specified the operation (GET/SET/CREATE)
- [ ] I have specified the exact field name
- [ ] I have shown expected vs. observed behavior
- [ ] I have checked the official documentation myself first
- [ ] I have provided error messages (if applicable)
- [ ] I have specified the use case or context

---

## Common Mistakes

### Mistake 1: Vague Field Names
**Bad:** "How do I set the bid?"
**Good:** "How do I set campaign.manual_cpc_setting.enhanced_cpc_enabled in API v17?"

### Mistake 2: No Version Specification
**Bad:** "Does the API support X?"
**Good:** "In API v16, v17, and v18, does the Campaign resource support X?"

### Mistake 3: Mixing Layers
**Bad:** "Why doesn't the API do what I want?"
**Good:** "According to official docs, field X should do Y. But my code shows Z. What am I missing?"

### Mistake 4: No Context
**Bad:** "How do I query campaigns?"
**Good:** "I need to query campaigns where status=ENABLED and bidding_strategy_type=MANUAL_CPC, filtered by performance_max_campaign=FALSE. What's the GAQL syntax?"

---

## Getting the Best API Answer

AI will give the most accurate answer when you provide:

1. **Exact field/object names** — copy/paste from the official docs
2. **Version number** — API v16, v17, v18, etc.
3. **Error messages** — verbatim from your logs
4. **Expected vs. observed** — what should happen vs. what happens
5. **Code snippet** — show relevant code (within privacy limits)
6. **Use case** — why you're doing this

---

## Evidence Requirement

For API queries, insist on evidence from:

1. **Official Google Ads API documentation** (primary)
2. **API error messages** (secondary)
3. **Our internal API SOPs** (tertiary)
4. **Inferred behavior** (lowest — only if not documented)

If the answer cannot cite one of the above, it's speculation.

---

## Follow-Up Questions

After getting an API answer, clarify:

- "Is this documented in the official API reference?"
- "What is the exact field path in [version]?"
- "What error should I expect if this operation is not allowed?"
- "What is the internal SOP for handling this case?"
