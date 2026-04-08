# Google Ads Operating System

> AI agents: your instructions are auto-loaded via `.github/copilot-instructions.md` and `.cursorrules`.
> If not auto-loaded, read `AGENT_BOOTSTRAP.md` first.

## Entry Protocol

1. Read `AGENT_BOOTSTRAP.md` first. It is the single authoritative entry protocol.
2. Follow the files and routing order defined there.
3. Do not scan the repository or preload knowledge outside routed scope.

## Structure

```
/
├── AGENT_BOOTSTRAP.md              # Agent entry protocol (single authority)
├── README.md                       # This file
├── migration_map.md                # Architecture migration record
│
├── registry/                       # Central registries (read first)
│   ├── repo.yaml                   # Repository metadata
│   ├── task-router.yaml            # Global task routing
│   ├── googleads.yaml              # Google Ads domain registry
│   ├── skills.yaml                 # Skills registry
│   ├── projects.yaml               # Projects registry
│   └── model-profiles.yaml         # AI model profiles
│
├── knowledge/googleads/            # Google Ads knowledge base
│   ├── TASK_ROUTER.yaml            # Domain task → knowledge mapping
│   ├── ACTIVE_INDEX.yaml           # Auto-generated knowledge index
│   ├── official/                   # Platform facts, official policy
│   ├── hybrid/                     # Official + operator interpretation
│   └── internal/                   # SOP, workflow, heuristic
│
├── skills/                         # Executable skill definitions
│   ├── googleads-field-operations/ # Orchestrator — main entry skill
│   ├── googleads-audit/            # Landing page audit
│   ├── googleads-keyword-expert/   # Keyword analysis
│   └── googleads-scripts/          # Script generation
│
├── projects/                       # Registered projects
│   ├── therads-platform-operations/
│   ├── manas-mainline/
│   ├── japan-google-ads/
│   └── openclaw-dashboard/         # Local-only, not GitHub-actionable
│
├── scripts/                        # Maintenance scripts
├── .github/                        # CI + AI agent instructions
│   ├── copilot-instructions.md     # Auto-loaded by Copilot/VS Code
│   └── workflows/validate.yml     # CI/CD validation
│
├── generated/                      # Auto-generated (do not edit)
└── archive/                        # Historical only (not primary truth)
```

## Rules

1. **Route before read** — use TASK_ROUTER.yaml, don't scan the repo
2. **Separate fact from inference** — label [Official Mechanism] vs [Architectural Inference]
3. **Include Evidence Map** — cite source files in every output
4. **Atomic updates** — registry changes must update CURRENT_STATE.md
5. **Archive is read-only** — never use archive/ as primary truth

## How to Add

**Knowledge**: Create md in `knowledge/googleads/<layer>/` → update `registry/googleads.yaml` → run `scripts/compile_knowledge.py`

**Skill**: Create `skills/<name>/` with `SKILL.md`, `skill.yaml`, `CHANGELOG.md` → update `registry/skills.yaml`

**Project**: Create `projects/<name>/` with `project.yaml`, `CURRENT_STATE.md`, `DECISIONS.md`, `CHANGELOG.md` → update `registry/projects.yaml`