# AGENT BOOTSTRAP v2

You are operating inside a governed repository.
Your job is not to scan the repository.
Your job is to enter through the correct gate.

## Hard Prohibitions

You must NOT:

* scan the whole repository
* open files randomly
* read `knowledge/`, `skills/`, or `projects/` before routing
* guess the task type
* load more than the minimum required files
* treat archived files as active sources of truth

If any of the above happens, stop and report protocol violation.

---

## Mandatory Entry Order

You must follow this exact order.

### Gate 0 — Bootstrap

Read:

* `AGENT_BOOTSTRAP.md`

If not read, stop immediately.

### Gate 1 — Repository Truth

Read:

* `registry/repo.yaml`

Goal:

* identify active modules
* identify archive modules
* identify canonical repository purpose

If repository structure is unclear, stop.

### Gate 2 — Task Declaration

Before reading any domain knowledge, you must declare:

* current task
* task_type
* target domain
* expected output type

If task_type is unknown, stop and ask for clarification.

### Gate 3 — Routing

Read:

* `registry/task-router.yaml`
* domain router if applicable, for example:

  * `knowledge/googleads/TASK_ROUTER.yaml`

Goal:

* map task_type to knowledge files
* map task_type to skills
* determine whether project context is required

If no route exists, stop.

### Gate 4 — Controlled Knowledge Selection

Read:

* `knowledge/googleads/ACTIVE_INDEX.yaml` if task domain is Google Ads

Only load files that are:

* routed
* active
* relevant
* within token budget
* not stale unless explicitly needed

You must prefer:

1. official
2. hybrid
3. internal

Do not load all knowledge files.

### Gate 5 — Execution Context

Only after routing is complete may you read:

* required `skills/*`
* required `projects/*`

You may only read:

* the exact skill needed
* the exact project needed

Do not browse all skills or all projects.

---

## Max Read Budget

Before execution begins:

* maximum total files opened: 10
* maximum knowledge files opened without explicit approval: 4
* maximum project files opened without explicit approval: 4
* maximum skill files opened without explicit approval: 2

If you exceed these limits, stop and report:
`READ_BUDGET_EXCEEDED`

---

## Stop Conditions

You must stop immediately if:

* task_type is not declared
* router not consulted
* ACTIVE_INDEX not consulted before loading knowledge
* archive content is being used as active content
* more than 10 files are opened before task execution begins
* multiple competing sources of truth are detected

When stopping, output:

* violation detected
* files already read
* why execution was halted

---

## Required Pre-Execution Output

Before doing any real work, you must output this block:

### Entry Report

* current task:
* task_type:
* domain:
* files read so far:
* router used:
* knowledge files selected:
* skills selected:
* projects selected:
* files intentionally not read:
* reason not read:

If this block is missing, execution is invalid.

---

## Active Source Priority

When facts conflict, use this priority:

1. `registry/*`
2. routed active knowledge
3. selected skill
4. selected project state
5. archive only for historical reference

Archive is never primary truth.

---

## Output Rule

All outputs must distinguish:

* fact
* inference
* operational heuristic

Do not merge them into one undifferentiated answer.

---

## Final Rule

If you do not know where to start, the answer is always:

1. `AGENT_BOOTSTRAP.md`
2. `registry/repo.yaml`
3. task declaration
4. router
5. active index
6. minimal execution context

Never start anywhere else.