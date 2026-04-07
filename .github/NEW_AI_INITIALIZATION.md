# New AI Initialization Protocol

**Send this message to every new AI tool before creating any task.**

---

## ⚠️ YOU MUST READ THIS FIRST

You are operating inside a governed repository.
Your job is not to scan the repository.
Your job is to enter through the correct gate.

---

## Mandatory Entry Protocol

Use this repository only:

* Local path: `/Users/palu/Google-ads`
* Remote repo: `https://github.com/palu89/Google-ads.git`
* Branch: `main`

**You must NOT begin by scanning files.**

**Start with the governed entry protocol:**

1. Read `AGENT_BOOTSTRAP.md` — **This defines your operational constraints.**
2. Read `registry/repo.yaml` — **This identifies the canonical repository structure.**
3. Declare your task before reading anything else:
   * current task
   * task_type (Google Ads Knowledge Query / Skill Execution / Project State Update / Registry Maintenance / Archive Reference)
   * domain (googleads / projects / registry / archive)
4. Read routing files:
   * `registry/task-router.yaml` (global router)
   * relevant domain router, for example:
     * `knowledge/googleads/TASK_ROUTER.yaml` (if task domain is googleads)
5. Read active index only after routing:
   * `knowledge/googleads/ACTIVE_INDEX.yaml` (if domain is googleads)
6. Load only minimum required files — prefer official > hybrid > internal

---

## Before Doing Any Real Work, Output This Block

### Entry Report

```
**Task Entry Report**

* current task: [what you are being asked to do]
* task_type: [one of: Google Ads Knowledge Query / Skill Execution / Project State Update / Registry Maintenance / Archive Reference]
* domain: [googleads / projects / registry / archive / other]
* files read so far: [list all files opened]
* router used: [which router file was consulted]
* knowledge files selected: [which knowledge files are relevant]
* skills selected: [which skill files will be used]
* projects selected: [which project files will be used]
* files intentionally NOT read: [what you decided not to open and why]
* reason not read: [explain the decision to skip files]
```

---

## Hard Stop Rules

Stop immediately if any of these are true:

* task_type is unclear — ask for clarification
* router file is missing — stop
* you are about to scan the entire repository — stop
* you exceed 10 opened files before execution begins — stop and report `READ_BUDGET_EXCEEDED`
* you are loading knowledge without consulting ACTIVE_INDEX first — stop

---

## Read Budget Limits

Before execution begins:

* max total files: 10
* max knowledge files: 4
* max project files: 4
* max skill files: 2

If you exceed these, stop and report the violation.

---

## Source of Truth Priority

When facts conflict, use this order:

1. `registry/*` files
2. routed active knowledge files
3. selected skill files
4. selected project state files
5. archive files (reference only, never primary truth)

**Archive is never primary truth.**

---

## If You Don't Know Where to Start

The answer is always:

```
1. AGENT_BOOTSTRAP.md
2. registry/repo.yaml
3. Task declaration
4. Routing (registry/task-router.yaml + domain router)
5. Active index (if applicable)
6. Minimal execution context
```

**Never start anywhere else.**

---

## Now You Are Ready

Once you have completed the Entry Report above, you are cleared to begin actual work.

Good luck.
