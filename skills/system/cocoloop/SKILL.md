---
name: cocoloop
description: Install, update, uninstall, and govern skills across Codex, OpenClaw, and GitHub repositories. Use when the task is about adding skills, comparing sources, deciding installation layer, or managing skill lifecycle safely.
---

# Cocoloop

Use this skill when the job is skill management rather than business execution.

## What it does
- Decides whether a skill belongs in `Codex`, `OpenClaw`, a project repository, or should remain experimental.
- Installs or updates skills from trusted sources.
- Removes or archives skills that should not stay active.
- Normalizes registry, routing, and documentation after installation.

## Mandatory governance
1. Vet external skills before installation.
2. Classify the skill layer first:
   - `system` for cross-project reusable capability
   - `project` for repository-specific execution logic
   - `runtime` for local-only operational wrappers
   - `experimental` for probationary skills
3. If the skill should be shared on GitHub, install it inside the repository and update:
   - `registry/skills.yaml`
   - `skills/system/SYSTEM_SKILLS_INDEX.md` when applicable
   - `knowledge/googleads/TASK_ROUTER.yaml` if routing is needed
   - `README.md` / onboarding docs if discoverability changes
4. If the skill is local-only, keep it out of the repository.

## Output format
Current judgment -> target layer -> install action -> sync action -> risks -> verification
