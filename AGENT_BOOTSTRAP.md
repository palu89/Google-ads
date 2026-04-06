# AGENT_BOOTSTRAP.md
**Version**: 1.0.0
**Last Updated**: 2026-04-06
**Purpose**: Defines bootstrapping sequence, task classification, and routing rules for AI agents interacting with this repository.

## 1. Bootstrap Read Order
Agents MUST load resources in this exact order:

1. **Registry First**: `registry/repo.yaml` → `registry/task-router.yaml` → `registry/model-profiles.yaml`
2. **Domain Routing**: `registry/googleads.yaml` → `registry/skills.yaml` → `registry/projects.yaml`
3. **Knowledge Index**: `knowledge/googleads/TASK_ROUTER.yaml` → `knowledge/googleads/ACTIVE_INDEX.yaml`
4. **Skill Manifests**: `/skills/<skill-name>/skill.yaml` (on-demand)
5. **Project State**: `/projects/<project-name>/CURRENT_STATE.md` (on-demand)

## 2. Task Classification
All incoming tasks MUST be classified into one of these categories before any processing:

- **Google Ads Knowledge Query**: Requests about Google Ads policies, scripts, compliance, optimization.
- **Skill Execution**: Requests to apply a specific skill (e.g., keyword audit, script generation).
- **Project State Update**: Requests that affect project status, decisions, or assets.
- **Registry Maintenance**: Updates to registry files, index regeneration, validation.
- **Archive Reference**: Historical lookups only; must not affect active state.

## 3. Tier Loading (Cold Start Protection)
To prevent unnecessary token consumption, apply tiered loading:

### Gate 0: Classification Confidence
- **Rule**: If classification confidence < 80%, ask clarifying questions.
- **Stop Condition**: Cannot proceed without clear classification.

### Gate 1: Tier 1 Sufficiency Stop
- **Resources**: `registry/task-router.yaml` + `knowledge/googleads/TASK_ROUTER.yaml`
- **Goal**: Answer using router mappings only.
- **Stop Condition**: If answer can be provided with router mappings alone, stop loading further resources.

### Gate 2: Tier 2 Contradiction Resolution Stop
- **Resources**: Add relevant `knowledge/googleads/{layer}/` files based on router.
- **Goal**: Resolve contradictions between router mapping and actual content.
- **Stop Condition**: If contradiction resolved, stop loading further resources.

### Gate 3: Tier 3 Summary-Only Rule
- **Resources**: Load full domain knowledge only if explicit request for deep analysis.
- **Constraint**: Summarize findings from loaded resources; do not load entire knowledge base.

## 4. Hard Stop Gates
- **No Full Repo Scan**: Never scan the entire repository. Use indexes and routers.
- **Evidence Map Requirement**: Every answer must cite specific file paths and line ranges.
- **Id-Based Routing**: Prefer referencing entities by ID over path-based routing.
- **Freshness Check**: If `content_updated_at` > 30 days, mark as "stale" in response.

## 5. Task-Specific Protocols

### Google Ads Tasks
1. Match against `knowledge/googleads/TASK_ROUTER.yaml`
2. Load corresponding knowledge file from `official`, `hybrid`, or `internal`
3. Apply skill if referenced (check `skills.yaml`)
4. Update `ACTIVE_INDEX.yaml` if content modified

### Skill Execution
1. Locate skill in `registry/skills.yaml`
2. Load `/skills/<skill-name>/skill.yaml`
3. Execute according to `SKILL.md`
4. Log execution in skill's `CHANGELOG.md`

### Project Updates
1. Load `project.yaml` from `/projects/<project-name>/`
2. Verify `CURRENT_STATE.md` reflects actual state
3. Make changes, update `CURRENT_STATE.md` and `CHANGELOG.md`
4. Update `registry/projects.yaml`

## 6. Evidence Map Requirement
Every response must include an evidence map:

```
**Evidence Map**:
- `registry/task-router.yaml`#L12-15: Task classification mapping
- `knowledge/googleads/official/field_manual_v3.0.md`#L45-52: Script deployment SOP
```

## 7. Change Propagation Rules
- Any change to active knowledge must trigger `ACTIVE_INDEX.yaml` regeneration.
- Any change to project state must update `CURRENT_STATE.md`.
- Any change to skill definition must update `registry/skills.yaml`.
- Use `scripts/check_atomic_updates.py` to validate atomic updates.

## 8. Emergency Procedures
- **Router Missing**: If router file not found, fall back to `registry/task-router.yaml` only.
- **Index Stale**: If `ACTIVE_INDEX.yaml` > 7 days old, regenerate using `scripts/compile_knowledge.py`.
- **Contradiction**: If registry and actual content contradict, flag for manual review.

## 9. Initialization Command
Agents should run this validation on first load:
```bash
python scripts/compile_knowledge.py --validate
python scripts/check_atomic_updates.py --strict