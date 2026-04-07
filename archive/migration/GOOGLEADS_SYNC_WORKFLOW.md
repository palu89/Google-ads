# Google Ads KB Sync Workflow Documentation

**Status:** Operational as of 2026-03-29
**Model:** Three-layer sync (GitHub → Local → Runtime)
**Maintained by:** Claude Haiku (knowledge), Codex (architecture)

---

## Overview

The Google Ads KB operates a documented three-layer sync architecture:

```
┌─────────────────────────────────┐
│  GitHub Authority (Source)      │
│  palu89/googleads-ops-kb.git    │
└────────────┬────────────────────┘
             │ (git pull/push)
             ↓
┌─────────────────────────────────┐
│  Local Working Copy (Editorial) │
│  /Users/palu/Claude code/       │
└────────────┬────────────────────┘
             │ (Batch promotion)
             ↓
┌─────────────────────────────────┐
│  OpenClaw Runtime (Promoted)    │
│ /.openclaw/.../reference/...    │
└─────────────────────────────────┘
```

---

## Layer 1: GitHub Authority

### Role
- Canonical source of truth for all Google Ads knowledge
- Immutable audit trail via git history and tags
- Public backup and reference repository

### Location
```
Remote: git@github-codex-backup:palu89/googleads-ops-kb.git
Web: https://github.com/palu89/googleads-ops-kb
Branch: main (single-branch strategy)
Tags: Semantic versioning (v1.x.y)
```

### Characteristics
- All knowledge changes originate from or sync through GitHub
- No local-only secrets or credentials (enforced)
- Versioned releases tied to batch promotions
- Audit trail: commit history + git tags

### What Lives Here
- `/00_shared/` — Foundational documentation
- `/01_account-structure/` — Account setup and structure
- `/02_bidding-strategy/` — Bidding and pacing logic
- `/03_creative-quality/` — Creative and landing page guidance
- `/04_analytics-report/` — Reporting and analysis
- `/05_attribution-conv/` — Attribution and conversion tracking
- `/06_feedback-iteration/` — Feedback and iteration processes
- `VERSION` file with semantic version number
- `README.md` with index and structure documentation

---

## Layer 2: Local Working Copy

### Role
- Editorial and staging layer for knowledge revisions
- Testing ground before batch promotion
- Interface for Claude Haiku knowledge work

### Location
```
Local path: /Users/palu/Claude code/
Git remote: origin = git@github-codex-backup:palu89/googleads-ops-kb.git
Local branch: main (tracking origin/main)
```

### Sync Frequency
**GitHub → Local:**
- Rate: Manual, intentional (not continuous)
- Trigger: Before starting batch revision session
- Command: `git pull origin main`
- Purpose: Ensure local copy reflects any changes made by other roles

**Local → GitHub:**
- Rate: After batch revisions complete + validated
- Trigger: Explicit push decision by Claude Haiku
- Command: `git commit` + `git push origin main` + `git push origin --tags`
- Purpose: Publish revised knowledge to canonical repository

### Workflow in Layer 2

#### 1. Pre-Revision Setup

```bash
cd /Users/palu/Claude\ code

# Ensure working tree is clean
git status                    # Should show: "On branch main, nothing to commit"

# Sync with GitHub authority
git pull origin main          # Fetch latest from GitHub

# Verify sync complete
git log -1 --oneline          # Shows HEAD commit
git remote -v                 # Verify remote configuration
```

#### 2. Local Revision Process

```bash
# Edit files locally
# Example: Revise glossary.md, gaql-schema.md, error-codes.md
nano 00_shared/glossary.md    # Make revisions
nano 00_shared/gaql-schema.md  # Make revisions
nano 00_shared/error-codes.md  # Make revisions

# Validate cross-references locally
# (Run markdown linter, check links, etc.)

# Test changes with local tools
# (Verify wrappers can resolve, policy compliance, etc.)

# Stage changes
git add 00_shared/glossary.md
git add 00_shared/gaql-schema.md
git add 00_shared/error-codes.md

# Verify staging
git status                    # Should show 3 files ready to commit
git diff --cached             # Review staged changes
```

#### 3. Commit & Tag for Batch Promotion

```bash
# Update VERSION file to reflect new version
echo "1.24.1" > VERSION
git add VERSION

# Commit with batch semantics
git commit -m "feat: v1.24.1 — Batch 12 — glossary + gaql-schema + error-codes revisions"

# Create semantic version tag
git tag v1.24.1

# Verify tag
git tag -l                    # List all tags
git show v1.24.1              # Show tag details
```

#### 4. Push to GitHub Authority

```bash
# Push commits to GitHub
git push origin main

# Push tags to GitHub
git push origin --tags

# Verify push success
git log -1 --oneline          # Local HEAD should match origin/main
git tag -l --merged           # Tags should include v1.24.1
```

---

## Layer 3: OpenClaw Runtime

### Role
- Active knowledge accessible to agent wrappers
- Read-only for Claude Haiku
- Curated subset of Layer 2 (only promoted content)

### Location
```
Runtime path: /Users/palu/.openclaw/workspace-googleads-palu/docs/reference/palu-ops-kb/
Structure: Mirrors GitHub structure
Permissions: Claude Haiku = Read-only, Codex = Read-write (promotion)
```

### What Lives Here
- Only Codex-approved batches (Batch 01-11 currently live)
- Mirror of GitHub at promotion time (snapshot)
- No secrets, credentials, or runtime-specific configurations

### Promotion Gate Process

#### Prerequisite: Batch Preparation in Layer 2

1. ✅ Local revisions complete and tested
2. ✅ Batch promotion checklist created (e.g., `GOOGLEADS_BATCH_12_PROMOTION.md`)
3. ✅ Dependency validation passed (all cross-references verified)
4. ✅ Content validation passed (policy compliance, formatting)
5. ✅ Changes committed and pushed to GitHub
6. ✅ Git tags created and pushed

#### Promotion Decision by Codex

**Codex Reviews:**
1. Batch promotion checklist (e.g., `GOOGLEADS_BATCH_12_PROMOTION.md`)
2. GitHub commit history (batch changes)
3. Dependency validation results
4. Content Quality assessment

**Codex Decision Options:**
- ✅ **APPROVED** → Promote to runtime (execute promotion command)
- 🔄 **NEEDS CHANGES** → Provide feedback (Claude Haiku revises in Layer 2)
- ❌ **REJECTED** → Explain reason (document in checklist)

#### Promotion Execution (by Codex)

```bash
# Codex executes promotion after approval
cp /Users/palu/Claude\ code/00_shared/glossary.md \
   /Users/palu/.openclaw/workspace-googleads-palu/docs/reference/palu-ops-kb/00_shared/glossary.md

cp /Users/palu/Claude\ code/00_shared/gaql-schema.md \
   /Users/palu/.openclaw/workspace-googleads-palu/docs/reference/palu-ops-kb/00_shared/gaql-schema.md

cp /Users/palu/Claude\ code/00_shared/error-codes.md \
   /Users/palu/.openclaw/workspace-googleads-palu/docs/reference/palu-ops-kb/00_shared/error-codes.md

# Verify promotion
ls -la /Users/palu/.openclaw/workspace-googleads-palu/docs/reference/palu-ops-kb/00_shared/

# Test wrapper resolution
/Users/palu/.openclaw/agents/googleads-team/skills/googleads-knowledge/test.sh

# Document in TRIAD_EXCHANGE.md
# "2026-03-30: Batch 12 promoted to runtime by Codex"
```

#### Post-Promotion Verification

1. ✅ Files exist in runtime path
2. ✅ File permissions allow wrapper read access
3. ✅ Cross-references resolve correctly
4. ✅ Agent tests confirm knowledge accessibility
5. ✅ No wrapper errors on first execution

---

## Sync Boundaries & Constraints

### What Syncs Between Layers

**GitHub ↔ Local (Manual Git Operations):**
- ✅ Knowledge content (markdown files)
- ✅ Directory structure
- ✅ VERSION file
- ✅ README.md and documentation
- ✅ Git history and tags

**Local → Runtime (Codex-Gated Promotion):**
- ✅ Batch-approved knowledge files
- ✅ Only after dependency validation
- ✅ Only after content validation
- ✅ Only after Codex explicit approval

### What Does NOT Sync

**Never Sync to GitHub:**
- ❌ `.env` or `runtime-secrets.env` files
- ❌ API keys, credentials, tokens
- ❌ Session-specific state
- ❌ Personal configuration
- ❌ LLM/Agent internal state

**Never Sync to Runtime Without Approval:**
- ❌ Unreviewed content
- ❌ Files with unresolved dependencies
- ❌ Policy-non-compliant content
- ❌ Anything bypassing Codex gate

---

## Workflow Scenarios

### Scenario 1: Normal Batch Revision Cycle

```
Step 1: GitHub → Local
  claude-haiku$ cd /Users/palu/Claude\ code
  claude-haiku$ git pull origin main

Step 2: Local Revisions
  claude-haiku$ [edit files]
  claude-haiku$ [validate locally]

Step 3: Commit & Push
  claude-haiku$ git add .
  claude-haiku$ git commit -m "feat: v1.24.1 — Batch 12 — ..."
  claude-haiku$ git tag v1.24.1
  claude-haiku$ git push origin main
  claude-haiku$ git push origin --tags

Step 4: Codex Review
  codex$ [review GOOGLEADS_BATCH_12_PROMOTION.md]
  codex$ [approve/reject/request-changes in TRIAD_EXCHANGE.md]

Step 5: Codex Promotion (if approved)
  codex$ cp [...files to runtime]
  codex$ [verify in TRIAD_EXCHANGE.md]

Step 6: Claude Haiku Documents
  claude-haiku$ [update TRIAD_EXCHANGE.md with completion note]
```

### Scenario 2: Codex Requests Changes

```
Step 1-4: Same as Scenario 1, but Codex requests changes

Step 5: Feedback to Claude Haiku
  codex$ [comments in GOOGLEADS_BATCH_12_PROMOTION.md]
  codex$ [updates TRIAD_EXCHANGE.md: "Batch 12 needs changes"]

Step 6: Claude Haiku Revises
  claude-haiku$ git pull origin main  # Get any feedback updates
  claude-haiku$ [edit files based on feedback]
  claude-haiku$ git add .
  claude-haiku$ git commit -m "fix: Batch 12 — address Codex feedback [description]"
  claude-haiku$ git push origin main

Step 7: Codex Re-reviews
  codex$ [review updated checklist]
  codex$ [approve in TRIAD_EXCHANGE.md]
  codex$ [execute promotion]
```

### Scenario 3: Continuous Improvement (Patch Updates)

```
# After Batch 12 promoted to runtime, refinements emerge

Step 1: Pull Latest
  claude-haiku$ git pull origin main

Step 2: Make Minor Refinements
  claude-haiku$ [edit glossary.md for clarification]

Step 3: Patch Tag & Push
  claude-haiku$ git commit -m "fix: v1.24.2 — glossary clarification"
  claude-haiku$ git tag v1.24.2
  claude-haiku$ git push origin main --tags

Step 4: Notify Codex (optional)
  claude-haiku$ [update TRIAD_EXCHANGE.md: "v1.24.2 patch published"]

Step 5: Codex Decides on Promotion
  codex$ [evaluate if patch warrants runtime update]
  codex$ [promote if needed, or hold for next batch]
```

---

## Synchronization Checklist

### Before Each Revision Session

- [ ] Working tree is clean: `git status`
- [ ] Fetch latest: `git fetch origin`
- [ ] Review incoming changes: `git log main..origin/main`
- [ ] Pull updates: `git pull origin main`
- [ ] Verify local HEAD matches remote: `git log -1 --oneline`

### Before Committing Revisions

- [ ] All changes tested locally
- [ ] Cross-references validated
- [ ] Policy compliance verified
- [ ] Batch promotion checklist prepared
- [ ] VERSION file updated
- [ ] Git staging reviewed: `git diff --cached`

### Before Pushing to GitHub

- [ ] Commit message follows conventions: `feat/fix/chore: message (Batch N)`
- [ ] VERSION file reflects new semantic version
- [ ] Tag created: `git tag vX.X.Y`
- [ ] All changes staged: `git status` shows nothing uncommitted
- [ ] Local history clean: `git log --graph --oneline origin/main..main`

### After Pushing to GitHub

- [ ] Remote has new commits: `git log origin/main -1`
- [ ] Tags synced: `git tag -l --merged`
- [ ] TRIAD_EXCHANGE.md updated with coordination note
- [ ] Batch promotion checklist status updated
- [ ] Await Codex review and promotion decision

---

## Emergency Procedures

### If Local Changes Conflict with GitHub

```bash
# Scenario: You pushed changes but GitHub repo was updated elsewhere

cd /Users/palu/Claude\ code

# Fetch latest from GitHub
git fetch origin

# Check for conflicts
git log --graph --oneline main origin/main

# If behind: Pull and rebase
git rebase origin/main main

# If diverged: Merge (not recommended for knowledge repo)
# OR Create new feature branch and prepare pull request
```

### If Push Fails

```bash
# Common causes & solutions

# 1. Authentication failure
ssh -T git@github-codex-backup  # Test SSH key

# 2. Network issues
git push origin main --verbose  # See detailed output

# 3. Remote has diverged
git fetch origin
git log main origin/main --graph --oneline  # Analyze divergence

# 4. Branch protection violation
# Contact Codex (branch protection may require PR)
```

### If Batch Promotion Fails

```bash
# If runtime promotion encounters errors

# 1. Verify files exist in Layer 2
ls -la /Users/palu/Claude\ code/00_shared/{glossary,gaql-schema,error-codes}.md

# 2. Check wrapper resolution
/Users/palu/.openclaw/agents/googleads-team/skills/googleads-knowledge/test.sh

# 3. Contact Codex with details
# [Document blockers in TRIAD_EXCHANGE.md]
```

---

## Monitoring & Health Checks

### Regular Sync Status Check

```bash
#!/bin/bash
# Run periodically to verify sync health

cd /Users/palu/Claude\ code

echo "=== Local Status ==="
git status

echo "=== Remote Status ==="
git fetch origin
git log main origin/main --oneline | head -5

echo "=== Version Check ==="
cat VERSION
git tag -l | tail -5

echo "=== File Integrity ==="
find 00_shared -name "*.md" | wc -l
echo "files in 00_shared"
```

### Cross-Reference Validation

```bash
#!/bin/bash
# Verify all cross-references are resolvable

cd /Users/palu/Claude\ code

# Extract all reference IDs from Batch 12 files
grep -o '\[.*\]' 00_shared/{glossary,gaql-schema,error-codes}.md | sort -u > /tmp/refs.txt

# Verify each reference exists
missing=0
while read ref; do
  if ! find . -name "*.md" -exec grep -l "^## $ref" {} \; | grep -q .; then
    echo "MISSING: $ref"
    ((missing++))
  fi
done < /tmp/refs.txt

echo "Missing references: $missing"
exit $missing  # Exit with count of missing refs
```

---

## Documentation & References

**Related Documents:**
- GOOGLEADS_GITHUB_FIRST_GOVERNANCE.md — Governance rules and boundaries
- GOOGLEADS_BATCH_TEMPLATE.md — Template for batch promotion checklists
- GOOGLEADS_BATCH_12_PROMOTION.md — Current Batch 12 status and checklist
- TRIAD_STATUS.md — Multi-AI collaboration rules and boundaries
- TRIAD_EXCHANGE.md — Coordination log (check before/after work)

**GitHub References:**
- Remote: `git@github-codex-backup:palu89/googleads-ops-kb.git`
- Web: `https://github.com/palu89/googleads-ops-kb`
- Documentation: `/Users/palu/Claude code/README.md`

---

_Last Updated: 2026-03-29 by Claude Haiku_
_Sync Model Status: ✅ Operational_
