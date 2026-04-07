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
    "references/persona-expression-variance.md",
    "references/story-structure-formula-library.md",
    "references/story-mode-switch-sop.md",
    "references/persona-governance.md",
    "references/persona-registry.md",
    "references/threads-review-workflow.md",
    "references/skill-validation.md",
    "references/usage-scope.md",
    "references/threads-account-baseline-card.md",
    "references/persona-lifecycle-switch-sop.md",
    "references/multi-persona-coexistence-governance.md",
    "references/threads-multi-persona-rotation-schedule.md",
    "references/threads-multi-persona-conflict-arbitration.md",
    "references/persona-content-pillar-map.md",
    "references/threads-account-primary-secondary-track-ratio.md",
    "references/threads-weekly-content-schedule.md",
    "references/threads-account-weekly-ops-report.md",
    "references/threads-column-lifecycle-assessment.md",
    "references/threads-content-queue-ledger.md",
    "references/threads-content-inventory-aging-rules.md",
    "references/threads-content-inventory-regeneration-rules.md",
    "references/threads-series-continuity-overview.md",
    "references/threads-multiweek-content-cadence-stress-test.md",
    "references/threads-cadence-runaway-rollback-checklist.md",
    "references/threads-high-risk-column-cooldown-rules.md",
    "references/threads-recurring-high-risk-expression-blacklist.md",
    "references/threads-high-risk-expression-replacement-library.md",
    "references/threads-high-risk-expression-variant-banlist.md",
    "references/threads-variant-trigger-auto-writeback-rules.md",
    "references/threads-auto-writeback-completion-checklist.md",
    "references/threads-column-replacement-options-template.md",
    "references/threads-column-cooldown-release-checklist.md",
    "references/threads-column-release-first-round-schedule.md",
    "references/threads-column-release-first-round-retrospective.md",
    "references/threads-column-release-failure-recooldown-sop.md",
    "references/threads-review-publish-package.md",
    "references/threads-content-experiment-log.md",
    "references/threads-account-monthly-phase-review.md",
    "references/threads-stage-transition-decision.md",
    "references/threads-stage-goal-tracker.md",
    "references/threads-risk-incident-log.md",
    "references/threads-account-recovery-risk-emergency-sop.md",
    "references/threads-account-recovery-observation-checklist.md",
    "references/threads-account-content-restart-threshold.md",
    "references/threads-content-restart-cadence-escalation-rules.md",
    "references/threads-cadence-escalation-column-stepup-order.md",
    "references/threads-cadence-escalation-persona-stepup-order.md",
    "references/threads-cadence-escalation-failure-rollback-threshold.md",
    "references/threads-content-asset-archiving-rules.md",
    "references/threads-archived-asset-reactivation-rules.md",
    "references/threads-account-stage-exit-checklist.md",
    "references/threads-account-stage-migration-retrospective.md",
    "references/threads-post-publish-retrospective.md",
    "references/threads-portfolio-operations-architecture.md",
    "references/threads-multi-account-skills-blueprint.md",
    "references/threads-multi-account-batch-01-plan.md",
    "references/threads-account-matrix-master-board.md",
    "references/threads-priority-account-activation-framework.md",
    "references/threads-shared-hook-library-framework.md",
    "references/threads-publish-writeback-spec.md",
    "references/threads-insights-collection-spec.md",
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

    if "内容运营强化链路" not in usage_text:
        errors.append("usage-scope.md must define content operations strengthening layer")

    if "可选内容模板包" not in usage_text:
        errors.append("usage-scope.md must define optional content templates")

    if "可选多账号运营增强链路" not in usage_text:
        errors.append("usage-scope.md must define optional multi-account operations layer")

    if "第一阶段已完成" not in usage_text or "真实运营痛点" not in usage_text:
        errors.append("usage-scope.md must define phase-complete freeze rules")

    if "maintain and audit" not in agent_text:
        errors.append("agents/openai.yaml must describe maintenance-first usage")

    for relative in [
        "references/threads-account-baseline-card.md",
        "references/persona-lifecycle-switch-sop.md",
        "references/multi-persona-coexistence-governance.md",
        "references/threads-multi-persona-rotation-schedule.md",
        "references/threads-multi-persona-conflict-arbitration.md",
        "references/persona-content-pillar-map.md",
        "references/threads-account-primary-secondary-track-ratio.md",
        "references/threads-weekly-content-schedule.md",
        "references/threads-account-weekly-ops-report.md",
        "references/threads-column-lifecycle-assessment.md",
        "references/threads-content-queue-ledger.md",
        "references/threads-content-inventory-aging-rules.md",
        "references/threads-content-inventory-regeneration-rules.md",
        "references/threads-series-continuity-overview.md",
        "references/threads-multiweek-content-cadence-stress-test.md",
        "references/threads-cadence-runaway-rollback-checklist.md",
        "references/threads-high-risk-column-cooldown-rules.md",
        "references/threads-recurring-high-risk-expression-blacklist.md",
        "references/threads-high-risk-expression-replacement-library.md",
        "references/threads-high-risk-expression-variant-banlist.md",
        "references/threads-variant-trigger-auto-writeback-rules.md",
        "references/threads-auto-writeback-completion-checklist.md",
        "references/threads-column-replacement-options-template.md",
        "references/threads-column-cooldown-release-checklist.md",
        "references/threads-column-release-first-round-schedule.md",
        "references/threads-column-release-first-round-retrospective.md",
        "references/threads-column-release-failure-recooldown-sop.md",
        "references/threads-review-publish-package.md",
        "references/threads-content-experiment-log.md",
        "references/threads-account-monthly-phase-review.md",
        "references/threads-stage-transition-decision.md",
        "references/threads-stage-goal-tracker.md",
        "references/threads-risk-incident-log.md",
        "references/threads-account-recovery-risk-emergency-sop.md",
        "references/threads-account-recovery-observation-checklist.md",
        "references/threads-account-content-restart-threshold.md",
        "references/threads-content-restart-cadence-escalation-rules.md",
        "references/threads-cadence-escalation-column-stepup-order.md",
        "references/threads-cadence-escalation-persona-stepup-order.md",
        "references/threads-cadence-escalation-failure-rollback-threshold.md",
        "references/threads-content-asset-archiving-rules.md",
        "references/threads-archived-asset-reactivation-rules.md",
        "references/threads-account-stage-exit-checklist.md",
        "references/threads-account-stage-migration-retrospective.md",
        "references/threads-post-publish-retrospective.md",
        "references/threads-portfolio-operations-architecture.md",
        "references/threads-multi-account-skills-blueprint.md",
        "references/threads-multi-account-batch-01-plan.md",
        "references/threads-account-matrix-master-board.md",
        "references/threads-priority-account-activation-framework.md",
        "references/threads-shared-hook-library-framework.md",
        "references/threads-publish-writeback-spec.md",
        "references/threads-insights-collection-spec.md",
    ]:
        if relative.replace("references/", "") not in usage_text and relative not in usage_text:
            errors.append(f"usage-scope.md must reference {relative}")


def check_content_ops_workflow(root: Path, errors: list[str]) -> None:
    workflow_text = read_text(root / "references/threads-content-operations-workflow.md")
    if "第一阶段已完成" not in workflow_text or "真实运营痛点" not in workflow_text:
        errors.append("threads-content-operations-workflow.md must define phase-complete freeze rules")

    for relative in [
        "threads-portfolio-operations-architecture.md",
        "threads-multi-account-skills-blueprint.md",
        "threads-multi-account-batch-01-plan.md",
        "threads-account-matrix-master-board.md",
        "threads-priority-account-activation-framework.md",
        "threads-shared-hook-library-framework.md",
        "threads-publish-writeback-spec.md",
        "threads-insights-collection-spec.md",
        "threads-account-baseline-card.md",
        "persona-lifecycle-switch-sop.md",
        "multi-persona-coexistence-governance.md",
        "threads-multi-persona-rotation-schedule.md",
        "threads-multi-persona-conflict-arbitration.md",
        "persona-content-pillar-map.md",
        "threads-account-primary-secondary-track-ratio.md",
        "threads-weekly-content-schedule.md",
        "threads-account-weekly-ops-report.md",
        "threads-column-lifecycle-assessment.md",
        "threads-content-queue-ledger.md",
        "threads-content-inventory-aging-rules.md",
        "threads-content-inventory-regeneration-rules.md",
        "threads-series-continuity-overview.md",
        "threads-multiweek-content-cadence-stress-test.md",
        "threads-cadence-runaway-rollback-checklist.md",
        "threads-high-risk-column-cooldown-rules.md",
        "threads-recurring-high-risk-expression-blacklist.md",
        "threads-high-risk-expression-replacement-library.md",
        "threads-high-risk-expression-variant-banlist.md",
        "threads-variant-trigger-auto-writeback-rules.md",
        "threads-auto-writeback-completion-checklist.md",
        "threads-column-replacement-options-template.md",
        "threads-column-cooldown-release-checklist.md",
        "threads-column-release-first-round-schedule.md",
        "threads-column-release-first-round-retrospective.md",
        "threads-column-release-failure-recooldown-sop.md",
        "threads-review-publish-package.md",
        "threads-content-experiment-log.md",
        "threads-account-monthly-phase-review.md",
        "threads-stage-transition-decision.md",
        "threads-stage-goal-tracker.md",
        "threads-risk-incident-log.md",
        "threads-account-recovery-risk-emergency-sop.md",
        "threads-account-recovery-observation-checklist.md",
        "threads-account-content-restart-threshold.md",
        "threads-content-restart-cadence-escalation-rules.md",
        "threads-cadence-escalation-column-stepup-order.md",
        "threads-cadence-escalation-persona-stepup-order.md",
        "threads-cadence-escalation-failure-rollback-threshold.md",
        "threads-content-asset-archiving-rules.md",
        "threads-archived-asset-reactivation-rules.md",
        "threads-account-stage-exit-checklist.md",
        "threads-account-stage-migration-retrospective.md",
        "threads-post-publish-retrospective.md",
    ]:
        if relative not in workflow_text:
            errors.append(f"threads-content-operations-workflow.md must reference {relative}")


def check_review_workflow(root: Path, errors: list[str]) -> None:
    review_text = read_text(root / "references/threads-review-workflow.md")
    if "threads-review-publish-package.md" not in review_text:
        errors.append("threads-review-workflow.md must reference threads-review-publish-package.md")


def check_content_enforcement(root: Path, errors: list[str]) -> None:
    skill_text = read_text(root / "SKILL.md")
    variance_text = read_text(root / "references/persona-expression-variance.md")
    story_text = read_text(root / "references/story-structure-formula-library.md")
    story_switch_text = read_text(root / "references/story-mode-switch-sop.md")
    p0_text = read_text(root / "references/p0-persona-branding.md")
    enforcement_text = read_text(root / "references/content-output-enforcement.md")
    performance_text = read_text(root / "references/content-performance.md")
    if "references/content-output-enforcement.md" not in skill_text:
        errors.append("SKILL.md must reference references/content-output-enforcement.md")
    if "references/persona-expression-variance.md" not in skill_text:
        errors.append("SKILL.md must reference references/persona-expression-variance.md")
    if "references/story-structure-formula-library.md" not in skill_text:
        errors.append("SKILL.md must reference references/story-structure-formula-library.md")
    if "references/story-mode-switch-sop.md" not in skill_text:
        errors.append("SKILL.md must reference references/story-mode-switch-sop.md")
    if "persona-expression-variance.md" not in p0_text:
        errors.append("references/p0-persona-branding.md must link to persona-expression-variance.md")
    if "persona-expression-variance.md" not in enforcement_text:
        errors.append("references/content-output-enforcement.md must link to persona-expression-variance.md")
    if "story-structure-formula-library.md" not in enforcement_text:
        errors.append("references/content-output-enforcement.md must link to story-structure-formula-library.md")
    if "story-mode-switch-sop.md" not in enforcement_text:
        errors.append("references/content-output-enforcement.md must link to story-mode-switch-sop.md")
    if "story-structure-formula-library.md" not in performance_text:
        errors.append("references/content-performance.md must link to story-structure-formula-library.md")
    if "story-mode-switch-sop.md" not in story_text:
        errors.append("references/story-structure-formula-library.md must link to story-mode-switch-sop.md")
    for needle in [
        "错别字",
        "空格代标点",
        "生活锚点",
        "纹理簇",
    ]:
        if needle not in variance_text:
            errors.append(f"references/persona-expression-variance.md must define {needle} rules")
    for needle in [
        "标题公式",
        "开头公式",
        "转折公式",
        "收尾公式",
        "高表现版",
        "合规发布版",
    ]:
        if needle not in story_text:
            errors.append(f"references/story-structure-formula-library.md must define {needle}")
    for needle in [
        "高表现版",
        "合规发布版",
        "六步转换法",
        "最小执行记录",
    ]:
        if needle not in story_switch_text:
            errors.append(f"references/story-mode-switch-sop.md must define {needle}")

    for relative in [
        "references/p0-persona-branding.md",
        "references/p1-trading-psychology.md",
        "references/p2-morning-brief.md",
        "references/p3-intraday-tracker.md",
        "references/p4-postmarket-recap.md",
        "references/p5-evening-lessons-high-performance.md",
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

    for needle in [
        "threads-portfolio-operations-architecture.md",
        "threads-multi-account-skills-blueprint.md",
        "threads-multi-account-batch-01-plan.md",
        "threads-account-matrix-master-board.md",
        "threads-priority-account-activation-framework.md",
        "threads-shared-hook-library-framework.md",
        "threads-publish-writeback-spec.md",
        "threads-insights-collection-spec.md",
    ]:
        if needle not in text:
            errors.append(f"CHANGELOG.md must record {needle}")


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
    check_content_ops_workflow(root, errors)
    check_review_workflow(root, errors)
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
