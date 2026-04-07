---
id: googleads-keyword-expert
entity_type: skill
name: googleads-keyword-expert
status: active
summary: Keyword intent analysis expert for Google Ads. Distinguishes between high-intent conversion keywords and low-intent informational queries.
description: Keyword auditing and intent analysis.
depends_on:
  - knowledge/keyword_expert
used_by:
  - agent/googleads-keyword-expert
owner: palu
last_updated: 2026-02-08T02:26:00Z
---

## Keyword Intent Analysis Expert

### Overview
This skill specializes in keyword intent analysis and auditing for Google Ads campaigns. It distinguishes between high-intent conversion keywords and low-intent informational queries to optimize ad spend and relevance.

### Key Capabilities
- Intent Classification: Categorize keywords by user intent (research, navigation, transactional)
- Conversion Prediction: Estimate conversion likelihood based on keyword intent
- Keyword Audit: Identify underperforming or irrelevant keywords
- Geo-Intent Analysis: Understand location-specific keyword variations
- Seasonal Trend Analysis: Detect seasonal keyword performance patterns
- Competitor Keyword Analysis: Benchmark against competitor keyword strategies

### Intent Classification Framework
1. **High-Intent Keywords**: Clearly signal purchase or conversion intent
2. **Medium-Intent Keywords**: Mixed signals; require context analysis
3. **Low-Intent Keywords**: Primarily informational; may not drive conversions
4. **Brand Keywords**: Contain brand mentions; typically high-intent
5. **Long-tail Keywords**: Specific variations; often high-intent but lower volume

### Dependencies
- `knowledge/googleads/internal/keyword_expert.md`: Core keyword analysis methodology

### Usage
Invoke this skill when:
- Analyzing keyword performance and relevance
- Building new keyword lists
- Optimizing bid strategies by intent
- Identifying wasted ad spend from low-intent keywords
- Conducting keyword audits

### Output Format
Returns keyword analysis with:
- Intent classification matrix
- Conversion probability estimates
- Performance recommendations
- Bid adjustment suggestions
- Keyword grouping recommendations

### Related Skills
- googleads-field-operations: General Google Ads orchestration
- googleads-scripts: Can generate automation scripts for keyword management
