---
id: googleads-audit
entity_type: skill
name: googleads-audit
status: active
summary: Landing page audit and optimization for Google Ads.
description: Audits landing pages for quality score and conversion optimization.
depends_on:
  - knowledge/lp_auditor
used_by:
  - agent/googleads-audit
owner: palu
last_updated: 2026-02-08T01:19:00Z
---

## Landing Page Auditor Skill

### Overview
This skill provides landing page audit and optimization capabilities for Google Ads campaigns. It examines landing pages for quality score factors and conversion optimization opportunities.

### Key Capabilities
- Quality Score Analysis: Evaluate landing page quality and relevance factors
- Conversion Optimization: Identify conversion rate improvement opportunities
- Technical Audit: Check page speed, mobile responsiveness, and technical SEO
- Compliance Check: Verify compliance with Google Ads policies
- User Experience Review: Assess user experience elements

### Dependencies
- `knowledge/googleads/internal/lp_auditor.md`: Core landing page audit methodology

### Usage
Invoke this skill when:
- Analyzing landing page quality scores
- Optimizing pages for better conversion rates
- Conducting technical SEO audits
- Checking policy compliance

### Output Format
Returns audit reports with:
- Quality Score breakdown
- Identified issues and severity levels
- Optimization recommendations
- Implementation priority

### Related Skills
- googleads-field-operations: General Google Ads orchestration
- googleads-scripts: Can generate optimization scripts based on audit findings
