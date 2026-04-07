# AI Error Prevention System Architecture

**Last Updated**: 2026-04-08  
**Purpose**: Prevent new AI agents from repeating common mistakes (random repository scanning, token waste, protocol violations)

---

## Problem Statement

Previous AI agents (like the current session's Claude Haiku) made the following errors:

1. **Random Repository Scanning** — Used `grep`, `find`, and `ls` to scan entire repository instead of using routers and indexes
2. **No Task Declaration** — Didn't declare task_type before reading knowledge files
3. **No Entry Report** — Didn't output Entry Report, made decisions invisibly  
4. **File Budget Exceeded** — Opened many unnecessary files, wasting tokens
5. **Wrong File Priority** — Loaded files based on intuition instead of routing rules

**Root Cause**: Lack of forced protocol enforcement at entry point.

---

## Solution Architecture

### Layer 1: Visual Deterrent (README.md)

**File**: `README.md` (lines 1-20)

**Content**: Large ⚠️ warning at the very top, before any other text.

**Effect**: Every new AI sees this immediately, before they understand the repository structure.

**Example**:
```
⚠️ MANDATORY: READ FIRST
You are not allowed to read this repository randomly...
```

---

### Layer 2: Strict Entry Protocol (AGENT_BOOTSTRAP.md v2)

**File**: `AGENT_BOOTSTRAP.md` 

**Content**: 
- Five mandatory entry gates (Gate 0-5)
- Hard prohibitions (NO scanning, NO random opens)
- Max read budget (10 files total, 4 knowledge, 4 project, 2 skill)
- Stop conditions (explicit list of violations that trigger abort)
- Required pre-execution output (Entry Report block)

**Effect**: Defines operational constraints as hard rules, not suggestions.

**Key Addition in v2**: 
- Hard `READ_BUDGET_EXCEEDED` stop condition
- Explicit file count limits
- Mandatory Entry Report output format

---

### Layer 3: New AI Initialization (NEW_AI_INITIALIZATION.md)

**File**: `NEW_AI_INITIALIZATION.md`

**Content**: 
- Paste this to every new AI tool before giving them a task
- Step-by-step entry procedure
- Mandatory Entry Report template
- Hard stop conditions with explicit messages

**Effect**: Sets immediate expectations before the AI touches any files.

**Usage**: 
```
"Use this repository only: /Users/palu/Google-ads
Before any task, you must:
1. Read AGENT_BOOTSTRAP.md
2. Read registry/repo.yaml
3. Declare your task...
"
```

---

### Layer 4: Entry Report Template (ENTRY_REPORT_TEMPLATE.md)

**File**: `ENTRY_REPORT_TEMPLATE.md`

**Content**: 
- Copy-paste template for Entry Report
- All required fields pre-formatted
- Field descriptions
- Budget tracker

**Effect**: Makes it easy for AI to comply (lower friction), and makes violations obvious (filled-in report cannot hide violations).

**Key Fields**:
- current_task
- task_type (one of 5 predefined types)
- domain (one of 5 predefined domains)
- files_read_so_far (with checkmarks)
- router_consulted (explicit)
- knowledge_files_selected (max 4)
- skills_selected (max 2)
- projects_selected (max 4)
- files_intentionally_not_opened (explicit blacklist)
- token_budget_status (explicit counts)

---

### Layer 5: Skill-Level Constraints (SKILL.md)

**File**: `skills/googleads-field-operations/SKILL.md` and all other skill files

**Content**:
```yaml
entry_protocol_required: true
entry_protocol_files:
  - AGENT_BOOTSTRAP.md
  - NEW_AI_INITIALIZATION.md
  - registry/repo.yaml
  - registry/task-router.yaml
  - knowledge/googleads/TASK_ROUTER.yaml
  - knowledge/googleads/ACTIVE_INDEX.yaml
```

Plus Entry Checklist:
- [x] Executed AGENT_BOOTSTRAP.md
- [x] Executed registry/repo.yaml
- [x] Declared task, task_type, domain
- [x] Consulted routers
- [x] Generated Entry Report
- [x] Token budget ≤ 10

**Effect**: Every skill explicitly states "do not invoke me without these preconditions."

---

### Layer 6: Automated Validation (scripts/validate_entry_report.py)

**File**: `scripts/validate_entry_report.py`

**Content**: Python script that validates an Entry Report text.

**Checks**:
- All required fields present
- task_type is one of 5 valid types
- domain is one of 5 valid domains
- AGENT_BOOTSTRAP.md listed as read
- NEW_AI_INITIALIZATION.md listed as read
- registry/repo.yaml listed as read
- router (task-router.yaml) was consulted
- Token budget is explicitly stated
- Files NOT opened are explicitly listed

**Usage**:
```bash
python3 scripts/validate_entry_report.py "$(cat entry_report.txt)"
# Output: ✅ Entry Report is VALID. You are cleared to proceed.
# OR
# Output: ❌ Entry Report FAILED validation. [list of failures]
```

**Effect**: Provides objective yes/no validation. AI cannot "sort of" follow protocol.

---

## Enforcement Strategy

### For Human Users (like you, palu)

When giving task to a new AI agent:

1. **Initial Message**:
   ```
   Use this repository: /Users/palu/Google-ads
   
   [COPY-PASTE entire NEW_AI_INITIALIZATION.md]
   
   After you've generated your Entry Report, I'll give you the actual task.
   ```

2. **After Entry Report**:
   ```
   Let me validate your report:
   python3 /Users/palu/Google-ads/scripts/validate_entry_report.py "[PASTE ENTRY REPORT TEXT]"
   ```

3. **After Validation Passes**:
   - Give the actual task
   - AI is now properly configured

### For AI Agents (like next Claude, GPT, etc.)

When entering this repository:

1. Check README.md first (see warning)
2. Read AGENT_BOOTSTRAP.md (understand constraints)
3. Read NEW_AI_INITIALIZATION.md (understand entry procedure)
4. Declare your task in writing (task_type, domain)
5. Consult routers (registry/task-router.yaml + domain router)
6. Read ACTIVE_INDEX before loading knowledge
7. Output Entry Report using template
8. Get Entry Report validated (optional but recommended)
9. Only THEN proceed with actual work

---

## Expected Behavior Changes

### Before (What Went Wrong)

```
AI joins → reads README → sees AGENT_BOOTSTRAP 
→ thinks "oh sure" but doesn't actually follow it
→ starts scanning with grep/find
→ reads random files
→ tries to find "向谷歌AI提问模版"
→ searches entire /knowledge/ directory
→ Read_Budget_Exceeded errors
→ Takes 30 minutes to find something that should take 2 minutes
```

### After (What Should Happen)

```
AI joins → reads README (sees urgent ⚠️)
→ reads AGENT_BOOTSTRAP.md (understands Five Gates)
→ reads NEW_AI_INITIALIZATION.md (given exact procedure)
→ declares task: "Find template for Google AI prompts"
→ task_type: "Google Ads Knowledge Query"
→ domain: "knowledge/googleads"
→ consults registry/task-router.yaml (maps to related skills)
→ consults knowledge/googleads/TASK_ROUTER.yaml (maps to specific files)
→ consults knowledge/googleads/ACTIVE_INDEX.yaml (lists available files)
→ outputs Entry Report (shows why each file was/wasn't opened)
→ Opens skill/googleads-field-operations/SKILL.md
→ Finds agents_backup.md reference
→ Locates answer in ~2 minutes, 3 files opened, 0 waste
```

---

## Files Created/Modified

| File | Action | Purpose |
|------|--------|---------|
| `AGENT_BOOTSTRAP.md` | **Modified** | Upgraded from v1 to v2 with strict Five-Gate protocol |
| `NEW_AI_INITIALIZATION.md` | **Created** | New AI entry procedure (paste to new agents) |
| `ENTRY_REPORT_TEMPLATE.md` | **Created** | Template for mandatory Entry Report output |
| `README.md` | **Modified** | Added urgent ⚠️ warning at top, updated quick links |
| `scripts/validate_entry_report.py` | **Created** | Automated Entry Report validator |
| `skills/googleads-field-operations/SKILL.md` | **Modified** | Added entry_protocol_required declaration + checklist |

---

## How to Use This System

### Scenario 1: Giving a task to new AI

```markdown
# Task for New AI Session

Use this repository: /Users/palu/Google-ads

**BEFORE DOING ANYTHING:**

[PASTE entire NEW_AI_INITIALIZATION.md here]

Generate your Entry Report following the template, then I will give you the actual task.
```

### Scenario 2: Validating an Entry Report (optional)

```bash
# AI sends their Entry Report
# You run this:
python3 /Users/palu/Google-ads/scripts/validate_entry_report.py "<<ENTRY REPORT TEXT>>"

# If it passes: ✅ Entry Report is VALID. Proceed.
# If it fails: ❌ Fix these issues before proceeding.
```

### Scenario 3: Preventing specific errors

If you notice an AI doing something wrong:
1. Check which protocol layer they violated
2. Point them to that document
3. Ask them to reread and declare why it's wrong
4. If needed, regenerate Entry Report

---

## Success Metrics

After implementing this system, you should see:

- ✅ **No more repository scanning** — AI consults routers instead
- ✅ **No more random file opens** — AI declares selections upfront  
- ✅ **Fewer token wasted** — Max 10 files opened before execution
- ✅ **Faster task resolution** — Entry Report makes decisions transparent
- ✅ **Clear explanation trail** — Every decision is documented in Entry Report
- ✅ **Reproducible behavior** — Different AIs follow same path

---

## Next Steps

1. **Commit these changes**: 
   ```bash
   git add AGENT_BOOTSTRAP.md NEW_AI_INITIALIZATION.md ENTRY_REPORT_TEMPLATE.md README.md scripts/validate_entry_report.py
   git commit -m "feat: Deploy AI Error Prevention System (5-layer architecture)"
   git push origin main
   ```

2. **Test with next AI agent**: Use NEW_AI_INITIALIZATION.md template

3. **Review Entry Reports**: Keep track of which files different task types actually need

4. **Refine based on usage**: Adjust read budgets / file limits as you learn

---

## Appendix: Protocol Violation Examples

### ❌ Violation 1: No Task Declaration

```
AI: "I'll read the repository to understand it."
System: STOP. You must declare task_type before reading knowledge.
```

### ❌ Violation 2: Skipping Router

```
AI: "I'll open /knowledge/googleads/official/field_manual_v3.0.md directly."
System: STOP. You must consult TASK_ROUTER.yaml first to validate this is routed.
```

### ❌ Violation 3: Excessive File Opens

```
AI: Opens files 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11...
System: STOP. READ_BUDGET_EXCEEDED at file 11. Maximum is 10.
```

### ✅ Correct: Follows Five-Gate Protocol

```
1. Gate 0: "Read AGENT_BOOTSTRAP.md" ✓
2. Gate 1: "Read registry/repo.yaml" ✓
3. Gate 2: "Task: ... Task Type: ... Domain: ..." ✓
4. Gate 3: "Consulted registry/task-router.yaml and knowledge/googleads/TASK_ROUTER.yaml" ✓
5. Gate 4: "Read ACTIVE_INDEX.yaml, selected files..." ✓
6. Gate 5: "Opened 7/10 files, 3/4 knowledge, 0/4 project, 1/2 skill" ✓
7. Output: Full Entry Report with all decisions explained
8. Proceed: Now safe to execute actual task
```

---

**System Deployed**: 2026-04-08
**Designed to Prevent**: Random scanning, token waste, protocol violations
**Expected Impact**: 10x faster repository navigation for new AI agents
