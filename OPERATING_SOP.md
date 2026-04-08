# Operating SOP

Updated: 2026-04-09

## Fixed Delivery Flow

All durable work in this repository follows one fixed lifecycle:

`Intel -> Promotion -> GitHub PR -> Runtime Sync -> Notion Merged`

This sequence is not optional.

## System Boundary

- `Notion` is the front door for intake, queueing, review status, and merged-state reporting.
- `GitHub` is the single execution source of truth for all durable assets, including knowledge, skills, routing, scripts, prompts, and project state.
- `Local` is a synchronized working mirror and runtime bridge. It is not an independent truth source.

If `Notion`, `GitHub`, and local runtime disagree, use this order:

1. Merged GitHub state
2. Current PR branch state
3. Notion planning or reporting state
4. Local draft or unsynced state

## Stage Definition

### 1. Intel

Capture the opportunity, issue, or new operating knowledge in Notion.

Required outputs:
- task title
- owner
- scope
- evidence links
- promotion decision status

### 2. Promotion

Decide whether the intel becomes durable repository state.

Promotion means the work must move into GitHub-tracked assets such as:
- `knowledge/`
- `skills/`
- `registry/`
- `projects/`
- `scripts/`
- operating docs

If it will not become durable state, keep it in Notion only and mark it as not promoted.

### 3. GitHub PR

All durable changes are implemented and reviewed through GitHub.

Required outputs:
- branch
- commit trail
- changed files
- validation evidence
- PR or merge reference

No durable operating truth may exist only in Notion.

### 4. Runtime Sync

After GitHub merge, sync the merged state into local runtime and any dependent operational environment.

Required outputs:
- sync target
- sync time
- runtime validation result
- failure or rollback note if sync did not complete

Runtime must follow merged GitHub state, not pre-merge drafts.

### 5. Notion Merged

Only after GitHub merge and runtime sync should Notion be updated to merged or complete.

Required Notion update fields:
- merged commit or PR link
- runtime sync status
- last verified time
- operator note if the runtime is still pending

## Sync Rules

- Do not mark work as complete in Notion before GitHub merge.
- Do not treat local-only edits as operational truth.
- Do not let Notion requirements override merged GitHub files.
- If GitHub changes invalidate an older Notion plan, Notion must be updated to match GitHub.
- If runtime differs from merged GitHub state, record the gap explicitly and keep Notion in a non-merged runtime state.

## AI Execution Rule

Any AI connecting to this repository must interpret the system like this:

- start from `AGENT_BOOTSTRAP.md`
- route work using repository registries
- treat GitHub-tracked files as execution truth
- treat Notion as intake and reporting
- treat local runtime as a synchronized execution surface

## Non-Negotiable Rules

- Never create a second durable truth outside GitHub.
- Never close the loop in Notion before GitHub and runtime are aligned.
- Never use local-only drafts as the final reference state.
- Never bypass the fixed lifecycle for durable changes.
