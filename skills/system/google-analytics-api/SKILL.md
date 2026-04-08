---
name: google-analytics-api
description: Query and configure Google Analytics properties, data streams, and reports through managed OAuth. Use when the task needs GA4 admin actions or reporting instead of Google Ads execution.
---

# Google Analytics API

Use this skill when the user needs GA4 reporting, property inspection, data-stream checks, or configuration support.

## Use this for
- Listing accounts, properties, and data streams
- Running GA4 reports for sessions, users, page views, and conversions
- Auditing analytics setup that affects Ads attribution or landing-page measurement
- Checking whether a property or stream exists before implementation work

## Operating rules
1. Confirm whether the task is Admin API or Data API.
2. Prefer read operations before making changes.
3. Separate analytics facts from Ads inference.
4. If credentials or OAuth are missing, report the blocker instead of guessing.
5. When this is supporting a Google Ads diagnosis, feed the result back into the Ads mechanism explanation.

## Output format
Current state -> report/config result -> impact on measurement -> next action -> evidence map
