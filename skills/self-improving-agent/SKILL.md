# Self-Improving Agent (System Layer)

Enables AI agents to evaluate their own work, catch mistakes, and improve permanently through structured memory.

## Architecture

Memory is managed within the repository at `/memories/` (User/Session/Repo scopes).

## Triggers for Improvement

### 1. Correction Patterns
- "No, that's not right..."
- "Actually, it should be..."
- "I prefer X, not Y"

### 2. Preference Signals
- "I like when you..."
- "Always do X for me"
- "For [project], use..."

## Self-Reflection Protocol
After completing significant work, AI MUST evaluate:
1. **Did it meet expectations?** — Compare outcome vs intent.
2. **What could be better?** — Identify improvements.
3. **Is this a pattern?** — If yes, propose a change to a relevant Knowledge file.

## Execution
Use this skill during the `Self-Evolution` phase defined in `AGENT_BOOTSTRAP.md`.
