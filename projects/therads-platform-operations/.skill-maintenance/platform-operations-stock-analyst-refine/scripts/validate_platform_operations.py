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
    "references/persona-governance.md",
    "references/persona-registry.md",
    "references/threads-review-workflow.md",
    "references/skill-validation.md",
    "references/usage-scope.md",
    "references/threads-platform-rules.md",
    "references/threads-account-compliance.md",
    "references/threads-copy-compliance.md",
]

ALLOWED_STATUS = {"draft", "active", "inactive", "archived"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (root / relative).exists():
            errors.append(f"missing required file: {relative}")


def check_skill_references(root: Path, errors: list[str]) -> None:
    skill_text = read_text(root / "SKILL.md")
    refs = sorted(set(re.findall(r"references/[A-Za-z0-9._/-]+\.md", skill_text)))
    for ref in refs:
        if not (root / ref).exists():
            errors.append(f"SKILL.md references missing file: {ref}")


def parse_persona_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    matches = list(re.finditer(r"^### \d+\. ([^\n]+)$", text, re.MULTILINE))
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        persona_id = match.group(1).strip()
        sections.append((persona_id, text[start:end]))
    return sections


def check_persona_registry(root: Path, errors: list[str]) -> None:
    registry_path = root / "references/persona-registry.md"
    text = read_text(registry_path)

    sections = parse_persona_sections(text)
    if not sections:
        errors.append("persona-registry.md contains no persona sections")
        return

    seen: set[str] = set()
    active_count = 0
    for persona_id, section in sections:
        if persona_id in seen:
            errors.append(f"duplicate persona id heading: {persona_id}")
        seen.add(persona_id)

        status_match = re.search(r"^- status:\s*([a-z-]+)\s*$", section, re.MULTILINE)
        if not status_match:
            errors.append(f"{persona_id}: missing status")
            continue

        status = status_match.group(1)
        if status not in ALLOWED_STATUS:
            errors.append(f"{persona_id}: invalid status `{status}`")

        if status == "active" and "{{" in section and "}}" in section:
            errors.append(f"{persona_id}: active persona contains unresolved placeholders")
        if status == "active":
            active_count += 1

    if active_count == 0 and "当前 `active` 人设：无" not in text:
        errors.append("persona-registry.md has no active personas but does not document that state")


def check_threads_docs(root: Path, errors: list[str]) -> None:
    workflow = read_text(root / "references/threads-review-workflow.md")
    if "Inference" not in workflow:
        errors.append("threads-review-workflow.md must define Inference usage")

    for relative in [
        "references/threads-platform-rules.md",
        "references/threads-account-compliance.md",
        "references/threads-copy-compliance.md",
    ]:
        text = read_text(root / relative)
        if "官方参考" not in text and "已按 `" not in text:
            errors.append(f"{relative} is missing official source notes")


def check_usage_scope(root: Path, errors: list[str]) -> None:
    skill_text = read_text(root / "SKILL.md")
    usage_text = read_text(root / "references/usage-scope.md")
    agent_text = read_text(root / "agents/openai.yaml")

    if "references/usage-scope.md" not in skill_text:
        errors.append("SKILL.md must reference references/usage-scope.md")

    if "可选内容模板包" not in skill_text:
        errors.append("SKILL.md must mark optional content templates explicitly")

    if "默认启用的维护核心" not in usage_text:
        errors.append("usage-scope.md must define default maintenance core")

    if "可选内容模板包" not in usage_text:
        errors.append("usage-scope.md must define optional content templates")

    if "maintain and audit" not in agent_text:
        errors.append("agents/openai.yaml must describe maintenance-first usage")


def check_content_enforcement(root: Path, errors: list[str]) -> None:
    skill_text = read_text(root / "SKILL.md")
    if "references/content-output-enforcement.md" not in skill_text:
        errors.append("SKILL.md must reference references/content-output-enforcement.md")

    for relative in [
        "references/p0-persona-branding.md",
        "references/p1-trading-psychology.md",
        "references/p2-morning-brief.md",
        "references/p3-intraday-tracker.md",
        "references/p4-postmarket-recap.md",
        "references/p5-evening-lessons.md",
        "references/macro-news-synthesizer.md",
        "references/single-stock-deepdive.md",
    ]:
        text = read_text(root / relative)
        if "content-output-enforcement.md" not in text:
            errors.append(f"{relative} must link to content-output-enforcement.md")


def check_changelog(root: Path, errors: list[str]) -> None:
    text = read_text(root / "CHANGELOG.md")
    if not re.search(r"^## \d{4}-\d{2}-\d{2}$", text, re.MULTILINE):
        errors.append("CHANGELOG.md must contain at least one dated entry")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 scripts/validate_platform_operations.py /path/to/platform-operations")
        return 2

    root = Path(sys.argv[1]).expanduser().resolve()
    errors: list[str] = []

    if not root.exists():
        print(f"error: path does not exist: {root}")
        return 2

    check_required_files(root, errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    check_skill_references(root, errors)
    check_persona_registry(root, errors)
    check_threads_docs(root, errors)
    check_usage_scope(root, errors)
    check_content_enforcement(root, errors)
    check_changelog(root, errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: platform-operations skill validation succeeded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
