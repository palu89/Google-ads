---
name: summarize
description: Summarize URLs, PDFs, documents, exports, and media with type-first handling. Use when the task needs fast, reliable condensation of long content before analysis or delivery.
---

# Summarize

Use this skill when the task is to compress long content without losing the signal.

## Best-use cases
- Long URLs, docs, PDFs, meeting notes, exports, issue threads, and review material
- First-pass reduction before deeper analysis
- Turning large attachments into an evidence map or action summary

## Execution rules
1. Inspect the real file type first. Do not trust filename extension or chat metadata alone.
2. If the file is text-like, read and summarize it directly.
3. If the file is true audio or video, transcribe first, then summarize the transcript.
4. Keep the first output short and decision-oriented unless the user explicitly asks for depth.
5. Preserve dates, owners, blockers, and irreversible decisions.

## Output format
Summary -> key decisions -> risks -> missing data -> evidence map
