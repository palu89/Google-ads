# Google Ads Repository — AI Agent Instructions

## MANDATORY: Read before any action

This repository is a Google Ads operating system, not a general codebase.

### Step 1: Bootstrap (always first)
Before answering any question or making any change, read:
- /registry/repo.yaml
- /knowledge/googleads/TASK_ROUTER.yaml

### Step 2: Route your task
Use TASK_ROUTER.yaml to identify:
- Which knowledge files to load
- Which skill to activate
- Which output format to use

### Step 3: Hard rules
- NEVER load from /archive or /generated
- NEVER edit ACTIVE_INDEX.yaml directly
- NEVER modify /registry without updating CURRENT_STATE.md
- ALWAYS separate [Official Mechanism] from [Architectural Inference]
- ALWAYS include Evidence Map in output

### Active projects
See /registry/projects.yaml for current active projects.

### Output format
Mechanism → Judgment → Action → Risks → Missing Data → Evidence Map
