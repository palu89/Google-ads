# Unified GitHub Repository

This repository serves as the canonical source of truth for:
1. Google Ads knowledge system
2. Skills capability system
3. Projects system
4. Registry and governance

## Structure

```
/
├── AGENT_BOOTSTRAP.md          # Bootstrap and routing rules
├── README.md                   # This file
├── migration_map.md            # Migration history and mapping
├── knowledge/                  # Google Ads knowledge base
│   └── googleads/
│       ├── official/           # Platform facts, official policy
│       ├── hybrid/             # Official + operator interpretation
│       ├── internal/           # SOP, workflow, heuristic
│       ├── playbooks/          # Step-by-step execution guides
│       ├── indexes/            # Generated indexes
│       ├── TASK_ROUTER.yaml    # Task-to-knowledge mapping
│       └── ACTIVE_INDEX.yaml   # Auto-generated knowledge index
├── registry/                   # Central registries
│   ├── repo.yaml               # Repository metadata
│   ├── model-profiles.yaml     # AI model profiles
│   ├── task-router.yaml        # Global task routing
│   ├── googleads.yaml          # Google Ads domain registry
│   ├── skills.yaml             # Skills registry
│   └── projects.yaml           # Projects registry
├── skills/                     # Skill definitions
│   └── <skill-name>/
│       ├── SKILL.md            # Skill documentation
│       ├── skill.yaml          # Skill metadata
│       └── CHANGELOG.md        # Change history
├── projects/                   # Active projects
│   └── <project-name>/
│       ├── project.yaml        # Project metadata
│       ├── CURRENT_STATE.md    # Current state snapshot
│       ├── DECISIONS.md        # Key decisions
│       ├── CHANGELOG.md        # Change history
│       ├── assets/             # Project assets
│       └── refs/               # Reference materials
├── generated/                  # Auto-generated content
├── archive/                    # Historical and migration materials
│   ├── migration/              # Migration documents
│   ├── audit/                  # Audit logs
│   └── googleads/scripts/      # Archived scripts
├── scripts/                    # Maintenance scripts
│   ├── compile_knowledge.py    # Knowledge compilation
│   └── check_atomic_updates.py # Atomic update validation
└── .github/workflows/
    └── validate.yml            # CI/CD validation workflow
```

## Governance Rules

1. **GitHub as Source of Truth**: All active knowledge, skills, and projects must be committed here.
2. **Frontmatter Required**: All active knowledge files must have YAML frontmatter with required fields.
3. **Atomic Updates**: Changes to active state must update registry/state files.
4. **No Full Repo Scans**: Agents must use registries and indexes, not scan entire repository.
5. **Archive Historical**: Migration documents, batch records, and historical backups belong in `/archive/`.

## Bootstrap Process

Agents should follow `AGENT_BOOTSTRAP.md` for:
- Classification confidence gates
- Tier loading (Tier 1, Tier 2, Tier 3)
- Evidence map requirements
- Cold start protection

## Validation

Run validation locally:
```bash
# Check structure and atomic updates
python3 scripts/check_atomic_updates.py

# Compile knowledge index
python3 scripts/compile_knowledge.py
```

## Adding New Knowledge

1. Create markdown file in appropriate knowledge layer (`official`, `hybrid`, `internal`)
2. Add required YAML frontmatter
3. Update `registry/googleads.yaml`
4. Run `scripts/compile_knowledge.py` to regenerate index

## Adding New Skills

1. Create skill directory in `/skills/<skill-name>/`
2. Add `SKILL.md`, `skill.yaml`, `CHANGELOG.md`
3. Update `registry/skills.yaml`

## Adding New Projects

1. Create project directory in `/projects/<project-name>/`
2. Add required project files (`project.yaml`, `CURRENT_STATE.md`, etc.)
3. Update `registry/projects.yaml`