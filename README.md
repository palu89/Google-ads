# Google Ads Operating System

> AI agents: your instructions are auto-loaded via `.github/copilot-instructions.md` and `.cursorrules`.
> If not auto-loaded, read `AGENT_BOOTSTRAP.md` first.

## Entry Protocol

1. Read `AGENT_BOOTSTRAP.md` first. It is the single authoritative entry protocol.
2. Follow the files and routing order defined there.
3. Do not scan the repository or preload knowledge outside routed scope.

This README is only a repository summary.
Canonical execution rules live in `AGENT_BOOTSTRAP.md` and `OPERATING_SOP.md`.

## System Boundary

- `Notion` is the front door for intake, queueing, and merged-state reporting.
- `GitHub` is the single execution source of truth.
- `Local` is a synchronized working mirror and runtime bridge.

If these layers disagree, merged GitHub state wins.

## Operating Flow

This repository uses one fixed durable-change lifecycle:

`Intel -> Promotion -> GitHub PR -> Runtime Sync -> Notion Merged`

Reference: `OPERATING_SOP.md`

## Structure

```
/
├── AGENT_BOOTSTRAP.md              # Agent entry protocol (single authority)
├── README.md                       # This file
├── AI启动模块.md                     # Fast orientation for new AI tools
├── OPERATING_SOP.md                # Fixed Notion -> GitHub -> runtime operating flow
│
├── registry/                       # Central registries (read first)
│   ├── repo.yaml
│   ├── task-router.yaml
│   ├── googleads.yaml
│   ├── skills.yaml
│   ├── projects.yaml
│   └── model-profiles.yaml
│
├── knowledge/googleads/            # Google Ads knowledge base
│   ├── TASK_ROUTER.yaml            # Domain task -> knowledge/skill routing
│   ├── ACTIVE_INDEX.yaml
│   ├── official/
│   ├── hybrid/
│   └── internal/
│
├── skills/                         # Project and system skills
│   ├── googleads-field-operations/
│   ├── googleads-audit/
│   ├── googleads-keyword-expert/
│   ├── googleads-scripts/
│   ├── googleads-verify/
│   ├── googleads-appeal/
│   ├── googleads-appealtxt/
│   ├── google-trends/
│   ├── self-improving-agent/
│   └── system/
│       ├── skill-vetter/
│       ├── web-search/
│       ├── cocoloop/
│       ├── summarize/
│       └── google-analytics-api/
│
├── projects/
├── scripts/
├── .github/
├── generated/
└── archive/
```

## Rules

1. Route before read. Use `knowledge/googleads/TASK_ROUTER.yaml`, not blind repo scans.
2. Separate fact from inference. Label official mechanism vs operator inference.
3. Include an evidence map in substantive answers.
4. Keep registry and skill paths synchronized.
5. Archive is read-only and never primary truth.
6. Durable operating changes must flow through GitHub before Notion is marked merged.

## How To Add

**Knowledge**: Create `knowledge/googleads/<layer>/<file>.md` -> update `registry/googleads.yaml` -> run `scripts/compile_knowledge.py`

**Project Skill**: Create `skills/<name>/` with `SKILL.md`, `skill.yaml`, `CHANGELOG.md` -> update `registry/skills.yaml` and `knowledge/googleads/TASK_ROUTER.yaml`

**System Skill**: Create `skills/system/<name>/` with `SKILL.md`, `skill.yaml`, `CHANGELOG.md` -> update `registry/skills.yaml`, `skills/system/SYSTEM_SKILLS_INDEX.md`, and any relevant routes

**Project**: Create `projects/<name>/` with `project.yaml`, `CURRENT_STATE.md`, `DECISIONS.md`, `CHANGELOG.md` -> update `registry/projects.yaml`

## Runtime Guard (Google Ads Wrappers)

For preload hygiene checks on `googleads-*` wrappers:

```bash
./scripts/install_googleads_runtime_guard.sh
./scripts/check_googleads_requires_sync.sh
```

Reference:

- `scripts/README_RUNTIME_GUARD.md`
- `archive/audit_reports/RUNTIME_GUARD_AUDIT_2026-04-09.md`
