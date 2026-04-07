# Google Ads KB → GitHub-First Governance Model

**Status:** Effective 2026-03-29
**Model:** GitHub-first canonical authority with three-layer sync
**Maintained by:** Claude Haiku (knowledge strategy), Codex (architecture approval)

---

## 1. Three-Layer Architecture

### Layer 1: GitHub Authority (Source of Truth)

**Repository:** `git@github-codex-backup:palu89/googleads-ops-kb.git`
**Web Access:** `https://github.com/palu89/googleads-ops-kb`
**Role:** Canonical knowledge base for all Google Ads operations

**Characteristics:**
- Single main branch (`main`) — no feature branches
- All knowledge changes originate here
- Semantic versioning (v1.x.0) tied to batch promotions
- Git history serves as audit trail for knowledge evolution

**Governance:**
- Branch protection: Main branch requires Codex approval for merges
- Commit message format: `feat/fix/chore: message (Batch N)`
- Tag format: `v1.x.y` (e.g., `v1.24.1`)

---

### Layer 2: Local Working Copy (Editorial/Staging)

**Location:** `/Users/palu/Claude code/`
**Role:** Editorial and revision layer for batch preparation

**Characteristics:**
- Working directory for content improvements
- Revisions tested and validated locally before GitHub push
- Clean pull from GitHub remains canonical state
- Local changes must eventually sync back to GitHub

**Workflow:**
1. Pull latest from GitHub: `git pull origin main`
2. Create revisions locally (files in `00_shared/`, `01_*/`, etc.)
3. Validate content (cross-references, formatting)
4. Commit with batch semantics: `feat: Batch 12 — glossary + gaql-schema + error-codes revisions`
5. Push to GitHub: `git push origin main`

---

### Layer 3: OpenClaw Runtime (Promoted Subset)

**Location:** `/Users/palu/.openclaw/workspace-googleads-palu/docs/reference/palu-ops-kb/`
**Role:** Active runtime knowledge accessible to agent wrappers

**Characteristics:**
- Only Codex-approved content deployed here
- Mirrors GitHub content after batch promotion gates
- Read-only for Claude Haiku (Codex-only modifications)
- Strict dependency resolution (all cross-references must resolve)

**Promotion Gate:**
- Batch preparation document created (e.g., `GOOGLEADS_BATCH_12_PROMOTION.md`)
- Dependency validation: `missing = 0` (all wrapper references verified)
- Content validation: Policy alignment, formatting standards
- Codex explicit approval: "Batch 12 promoted to runtime"

---

## 2. Versioning Strategy

**Approach:** Semantic Versioning (Major.Minor.Patch)

| Component | Trigger | Example |
|-----------|---------|---------|
| **Major (0.x.0)** | Architectural restructuring (rare) | 2.0.0 [future] |
| **Minor (1.x.0)** | Batch promotions + new modules | 1.24.0 (Batch 24), 1.25.0 (Batch 25) |
| **Patch (1.x.y)** | Bug fixes, refinements within released batch | 1.24.1, 1.24.2 |

**Current State:** v1.24.1 (next after current e94e2ad)

**Implementation:**
- VERSION file at `/Users/palu/Claude code/VERSION` contains current version
- Git tag creates immutable release points
- Commit message includes version: `feat: v1.24.1 — Batch 24 refinements`

---

## 3. Sync Workflow: GitHub ↔ Local ↔ Runtime

### GitHub → Local Sync (Editorial Phase)

**Frequency:** Before each batch revision session
**Command:** `git pull origin main` in `/Users/palu/Claude code/`
**Trigger:** Explicit (manual, not automated)

**Purpose:** Keep local working copy synchronized with canonical GitHub state

**Validation:**
- Check working tree clean: `git status` shows nothing uncommitted
- Verify HEAD points to latest main: `git log -1 --oneline`
- Review incoming changes: `git log origin/main..main` (should be empty after pull)

---

### Local → GitHub Sync (Publication Phase)

**Frequency:** After batch revisions complete and validated
**Commands:**
```bash
git add .                                    # Stage revisions
git commit -m "feat: v1.24.1 — Batch 24..."  # Commit with batch semantics
git tag v1.24.1                              # Tag release
git push origin main                         # Push commits
git push origin --tags                       # Push tags
```

**Trigger:** Explicit (after local validation, before Codex promotion decision)

**Purpose:** Publish revised knowledge to canonical GitHub repository

**Pre-push Checklist:**
- ✓ All file revisions complete and tested locally
- ✓ Cross-references validated (no broken links)
- ✓ Policy compliance verified
- ✓ Batch list documented in commit message
- ✓ README.md updated if structure changed

---

### Local → Runtime Sync (Promotion Phase)

**Frequency:** Per-batch (Batch 12, 13, 14...)
**Trigger:** Codex approval after batch validation
**Direction:** Codex-initiated copy from local to runtime workspace

**Promotion Gate Checklist:**
1. **Batch Documentation:** `GOOGLEADS_BATCH_N_PROMOTION.md` created and reviewed
2. **Dependency Validation:** All wrapper dependencies resolved (`missing = 0`)
3. **Content Validation:** Policy alignment, formatting, cross-references
4. **Codex Approval:** Explicit written approval in TRIAD_EXCHANGE.md
5. **Promotion Command:** Codex executes copy to `/Users/palu/.openclaw/workspace-googleads-palu/docs/reference/palu-ops-kb/`

**Example Approval Log Entry:**
```
2026-03-30 [Codex Decision Log]
- Batch 12 promotion approved
- Files: glossary.md + gaql-schema.md + error-codes.md
- Validation: All dependencies resolved, policy verified
- Command: cp /Users/palu/Claude\ code/00_shared/{glossary,gaql-schema,error-codes}.md <runtime-path>/
```

---

## 4. Batch Promotion System

### Batch Numbering

- **Batch 01-11:** Already complete (66 files in runtime)
- **Batch 12:** Foundation + Core References (v1.24.1)
  - glossary.md → glossary revisions (KPI formulas)
  - gaql-schema.md → API field validation
  - error-codes.md → decision tree testing
- **Batch 13+:** Future promotions (on demand)

### Batch Promotion Document Template

**File Format:** `GOOGLEADS_BATCH_N_PROMOTION.md`
**Location:** `/Users/palu/codex交互中心/collaboration/`

**Required Sections:**

```markdown
# Batch N Promotion Checklist

## Files Included
- [ ] file1.md (status: created/revised/unchanged)
- [ ] file2.md (status: created/revised/unchanged)

## Revision Summary
- Describe what changed and why for each file
- Link to related issues or decisions

## Dependency Validation
- [ ] All cross-references verified (grep for missing files)
- [ ] Wrapper dependencies resolved (wrapper can locate knowledge)
- [ ] No circular dependencies detected

## Content Validation
- [ ] Policy compliance verified against official sources
- [ ] Formatting consistent with existing files
- [ ] No broken links or references

## Codex Decision Gate
- [ ] Ready for review by Codex
- [ ] Codex approval status: [pending/approved/rejected]
- [ ] Date approved: [if approved]

## Runtime Promotion Status
- [ ] Promoted to runtime queue (pending Codex decision)
- [ ] Promoted to runtime (by Codex)
- [ ] Date promoted: [if promoted]
```

---

## 5. Multi-AI Role Boundaries

### Codex Role
**Authority:** Merge approval, runtime promotion, reference governance
**Responsibility:**
- Approve batch promotions before runtime deployment
- Maintain reference layer (`/Users/palu/.codex/skills/googleads`)
- Architecture decisions and policy alignment
- Runtime integration verification

**Tools Access:**
- Read: All knowledge files
- Write: Runtime promotion layer only
- Decision: All promotion gates

---

### Claude Haiku (Current Session) Role
**Authority:** Knowledge strategy, content revisions, GitHub publishing
**Responsibility:**
- Batch preparation and local revisions
- GitHub push (after local validation)
- Dependency validation scripts
- TRIAD documentation updates
- Promotion checklist completion

**Tools Access:**
- Read: All knowledge files
- Write: `/Users/palu/Claude code/` (local working copy)
- Git: Pull from GitHub, push revisions, create tags
- Decision: None (waits for Codex approval)

---

### OpenClaw Role
**Authority:** Runtime execution, verification
**Responsibility:**
- Runtime deployment after Codex approval
- Agent wrapper integration
- Health checks and dependency resolution
- Session-level execution

**Tools Access:**
- Read: Runtime knowledge layer
- Write: Session state only (not knowledge)
- Decision: None (executes Codex decisions)

---

## 6. Non-Negotiable Boundaries

### ✅ DO:

1. **GitHub as Authority:** All knowledge changes originate from or sync through GitHub
2. **Batch Semantics:** Use consistent batch naming and version numbers
3. **Codex Gates:** Wait for explicit Codex approval before runtime promotion
4. **TRIAD Logging:** Update TRIAD_EXCHANGE.md after important changes
5. **Dependency Validation:** Run cross-reference checks before promotion

### ❌ DON'T:

1. **Direct Runtime Modification:** Never edit `/Users/palu/.openclaw/...` without Codex
2. **Deviate from Sync Flow:** Don't skip GitHub → Local → Runtime layers
3. **Mix Concerns:** Keep knowledge separate from secrets/runtime-config
4. **Unversioned Changes:** All knowledge updates must have semantic version + batch
5. **Skip Approval:** Don't promote batches without explicit Codex decision

---

## 7. Common Workflows

### Workflow 1: Revise & Promote Batch 12

```bash
# 1. Ensure local copy is clean
cd /Users/palu/Claude\ code
git status                              # Should show clean working tree
git pull origin main                    # Sync with GitHub authority

# 2. Revise files locally
# (Edit: 00_shared/glossary.md, gaql-schema.md, error-codes.md)
# (Test: validate cross-references, policy compliance)

# 3. Create promotion checklist
cat > /Users/palu/codex交互中心/collaboration/GOOGLEADS_BATCH_12_PROMOTION.md <<EOF
# Batch 12 Promotion Checklist
[See template above]
EOF

# 4. Commit & push to GitHub
git add .
git commit -m "feat: v1.24.1 — Batch 12 — glossary + gaql-schema + error-codes revisions"
git tag v1.24.1
git push origin main
git push origin --tags

# 5. Update TRIAD_EXCHANGE.md
# (Add: "2026-03-30: Batch 12 revision complete, awaiting Codex approval")

# 6. Wait for Codex approval in GOOGLEADS_BATCH_12_PROMOTION.md

# 7. Codex executes promotion (after approval)
```

### Workflow 2: Respond to Codex Feedback

```bash
# 1. Pull any Codex-pushed changes or feedback
git pull origin main

# 2. Review feedback in promotion checklist
# (e.g., GOOGLEADS_BATCH_12_PROMOTION.md "Codex Decision Gate" section)

# 3. Make requested revisions locally
# (Edit files based on feedback)

# 4. Re-validate and commit
git add .
git commit -m "fix: Batch 12 — address Codex feedback [description]"
git push origin main

# 5. Update promotion checklist and wait for re-approval
```

---

## 8. Success Criteria

✓ GitHub repo is authoritative source for all Google Ads knowledge
✓ Local working copy stays synchronized with GitHub
✓ Batch promotions follow explicit approval gates
✓ Version numbers align with batch semantics
✓ TRIAD roles clearly defined and enforced
✓ No direct runtime modifications without Codex
✓ All changes logged in TRIAD_EXCHANGE.md

---

## 9. Related Documents

- **TRIAD_STATUS.md:** Multi-AI collaboration model and mandatory rules
- **TRIAD_EXCHANGE.md:** Coordination log (check before/after important work)
- **CODEX_SELF_HANDOFF.md:** Handoff context for all roles
- **GOOGLEADS_BATCH_TEMPLATE.md:** Reusable batch promotion template
- **GOOGLEADS_KNOWLEDGE_HANDOVER_MAP.md:** Inventory of files and promotion status

---

_Last Updated: 2026-03-29 by Claude Haiku_
