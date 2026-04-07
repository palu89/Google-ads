# Agent Bootstrap — Two-Step Protocol

You are inside a Google Ads operating system. Not a general codebase.

---

## Step 1: Read Registry

Read these 2 files. Do not read anything else first.

1. `registry/repo.yaml` → repo version, active modules, structure
2. `knowledge/googleads/TASK_ROUTER.yaml` → task-to-knowledge routing

## Step 2: Route and Execute

Match your task to a route in TASK_ROUTER.yaml.

Load **only** the knowledge files and skills listed for that route.

If no route matches, ask the user:
> "Task type unclear. Specify: audit / explain / modify / update_state"

---

## Hard Rules

- NEVER scan the whole repository
- NEVER open files before routing
- NEVER load from `/archive` or `/generated` as primary truth
- NEVER edit `ACTIVE_INDEX.yaml` directly
- NEVER present inference as official fact
- ALWAYS separate: [Official Mechanism] vs [Architectural Inference]
- ALWAYS include Evidence Map in output

## Source Priority (when facts conflict)

1. `registry/*`
2. Routed active knowledge (`knowledge/googleads/official/` → `hybrid/` → `internal/`)
3. Selected skill (`skills/`)
4. Project state (`projects/*/CURRENT_STATE.md`)
5. Archive (historical reference only)

## Output Format

Mechanism → Judgment → Action → Risks → Missing Data → Evidence Map

## If lost, start here

1. `registry/repo.yaml`
2. `knowledge/googleads/TASK_ROUTER.yaml`
3. Route → load → execute

Never start anywhere else.