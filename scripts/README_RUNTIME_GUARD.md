# Google Ads Runtime Guard

Date: 2026-04-09

## Purpose

This guard enforces preload hygiene for `googleads-*` wrappers.

It blocks `requires.files` drift to:

- absolute local paths
- `.codex/` source-side paths
- legacy invalid preload files
- unsynced or out-of-scope files

## Files

- `scripts/check_googleads_requires_sync.sh`
- `scripts/install_googleads_runtime_guard.sh`

## Install

From repository root:

```bash
./scripts/install_googleads_runtime_guard.sh
```

This installs a local pre-commit hook that runs the guard before each commit.

## Verify

```bash
./scripts/check_googleads_requires_sync.sh
```

Expected:

```text
googleads requires.files gate: OK
```

## Scope Gate

Allowed preload roots:

- `docs/reference/*`
- `docs/playbooks/*`
- `docs/research/*`
- current wrapper-local files under `skills/<wrapper>/`

Rejected preload paths include:

- absolute paths like `/Users/...`
- `.codex/...`
- `skills/docs/reference/...`
- legacy `googleads-modules.md` / `googleads-field-manual.md`
