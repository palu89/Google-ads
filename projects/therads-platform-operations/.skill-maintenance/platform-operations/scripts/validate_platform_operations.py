#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "CHANGELOG.md",
    "agents/openai.yaml",
    "references/content-output-enforcement.md",
    "references/viral-profit-template.md",
    "references/template-01-engine-map.md",
    "references/codex-content-creation-prompt.md",
    "references/skill-validation.md",
]

EXCLUDED_PATTERNS = [
    "persona-registry",
    "persona-governance",
    "p0-persona-branding",
    "p1-trading-psychology",
    "p2-morning-brief",
    "p3-intraday-tracker",
    "p4-postmarket-recap",
    "p5-evening-lessons",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_platform_operations.py /path/to/platform-operations")
        return 1

    root = Path(sys.argv[1]).resolve()
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).exists():
            errors.append(f"missing required file: {relative}")

    all_files = [str(path.relative_to(root)) for path in root.rglob("*") if path.is_file()]
    for excluded in EXCLUDED_PATTERNS:
        if any(excluded in relative for relative in all_files):
            errors.append(f"unexpected file pattern still exists: {excluded}")

    skill_path = root / "SKILL.md"
    if skill_path.exists():
        skill_text = read_text(skill_path)
        if "模版1" not in skill_text or "核心指令" not in skill_text:
            errors.append("SKILL.md must document the new minimal entry format")
        refs = sorted(set(re.findall(r"references/[A-Za-z0-9._/-]+\.md", skill_text)))
        for ref in refs:
            if not (root / ref).exists():
                errors.append(f"SKILL.md references missing file: {ref}")

    gate_path = root / "references/content-output-enforcement.md"
    if gate_path.exists():
        gate_text = read_text(gate_path)
        for needle in ["赚钱兑现", "随机替换规则", "交付形式", "输出前自检", "顺序要求"]:
            if needle not in gate_text:
                errors.append(f"content-output-enforcement.md missing `{needle}`")

    template_path = root / "references/viral-profit-template.md"
    if template_path.exists():
        template_text = read_text(template_path)
        for needle in ["主引擎", "固定骨架", "逻辑约束", "失败示例特征", "交付形式"]:
            if needle not in template_text:
                errors.append(f"viral-profit-template.md missing `{needle}`")

    engine_map_path = root / "references/template-01-engine-map.md"
    if engine_map_path.exists():
        engine_map_text = read_text(engine_map_path)
        for needle in ["模版1 结构地图", "全部可替换槽位", "绝对禁止复用", "当前线程污染规则"]:
            if needle not in engine_map_text:
                errors.append(f"template-01-engine-map.md missing `{needle}`")

    codex_prompt_path = root / "references/codex-content-creation-prompt.md"
    if codex_prompt_path.exists():
        codex_prompt_text = read_text(codex_prompt_path)
        for needle in ["Codex 内容创作提示词", "只负责输出 Threads 正文", "严格按模板把正文写出来"]:
            if needle not in codex_prompt_text:
                errors.append(f"codex-content-creation-prompt.md missing `{needle}`")

    changelog_path = root / "CHANGELOG.md"
    if changelog_path.exists():
        changelog_text = read_text(changelog_path)
        if "2026-03-22" not in changelog_text:
            errors.append("CHANGELOG.md must include a dated reset record")

    agent_path = root / "agents/openai.yaml"
    if agent_path.exists():
        agent_text = read_text(agent_path)
        if "viral-post writer" not in agent_text and "赚钱爆帖模板" not in agent_text:
            errors.append("agents/openai.yaml must describe the new minimal viral-post mode")

    if errors:
        print("FAIL: platform-operations skill validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: platform-operations skill validation succeeded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
