#!/usr/bin/env python3
"""
validate_entry_report.py
Validates that an AI agent has followed the Entry Protocol before execution.
"""

import sys
import re

REQUIRED_FIELDS = [
    "current task",
    "task type",
    "domain",
    "files read so far",
    "router consulted",
    "knowledge files selected",
    "skills selected",
    "projects selected",
    "files intentionally not opened",
    "reason for decisions",
    "token budget status",
]

TASK_TYPES = [
    "Google Ads Knowledge Query",
    "Skill Execution",
    "Project State Update",
    "Registry Maintenance",
    "Archive Reference",
]

DOMAINS = [
    "googleads",
    "projects",
    "registry",
    "archive",
    "other",
]

def validate_entry_report(report_text: str) -> tuple[bool, list]:
    """
    Validate a proposed Entry Report text.
    
    Returns:
        (is_valid, list_of_failures)
    """
    failures = []
    
    # Check for Entry Report header
    if "Entry Report" not in report_text:
        failures.append("MISSING: 'Entry Report' header not found")
        return (False, failures)
    
    # Check for all required fields
    for field in REQUIRED_FIELDS:
        if field not in report_text.lower().replace("_", " "):
            failures.append(f"MISSING: {field} not present in report")
    
    # Check for valid task_type
    task_type_found = False
    for valid_type in TASK_TYPES:
        if valid_type in report_text:
            task_type_found = True
            break
    if not task_type_found:
        failures.append(f"INVALID: task_type must be one of: {TASK_TYPES}")
    
    # Check for valid domain
    domain_found = False
    for valid_domain in DOMAINS:
        if valid_domain in report_text.lower():
            domain_found = True
            break
    if not domain_found:
        failures.append(f"INVALID: domain must be one of: {DOMAINS}")
    
    # Check that AGENT_BOOTSTRAP.md was read
    if "AGENT_BOOTSTRAP.md" not in report_text:
        failures.append("PROTOCOL VIOLATION: AGENT_BOOTSTRAP.md not listed as read")
    
    # Check that registry/repo.yaml was read
    if "registry/repo.yaml" not in report_text:
        failures.append("PROTOCOL VIOLATION: registry/repo.yaml not listed as read")
    
    # Check router was consulted
    if "task_router.yaml" not in report_text.lower():
        failures.append("PROTOCOL VIOLATION: Task Router (TASK_ROUTER.yaml) not consulted")
    
    # Check token budget is stated
    if "/10" not in report_text and "/4" not in report_text and "/2" not in report_text:
        failures.append("MISSING: token budget status (e.g., '3 / 10 max')")
    
    # Check that files NOT opened are explicitly stated
    if "intentionally" not in report_text.lower():
        failures.append("MISSING: files intentionally NOT opened should be explicitly listed")
    
    is_valid = len(failures) == 0
    return (is_valid, failures)

def main():
    """CLI interface for validating Entry Report."""
    if len(sys.argv) < 2:
        print("Usage: python validate_entry_report.py <report_text>")
        print("  or pipe from stdin: echo '...report...' | python validate_entry_report.py")
        sys.exit(1)
    
    # Read from argument or stdin
    report_text = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    
    is_valid, failures = validate_entry_report(report_text)
    
    if is_valid:
        print("✅ Entry Report is VALID. You are cleared to proceed.")
        sys.exit(0)
    else:
        print("❌ Entry Report FAILED validation.")
        print("\nFailures:")
        for i, failure in enumerate(failures, 1):
            print(f"  {i}. {failure}")
        print("\nFix these issues before proceeding. Use ENTRY_REPORT_TEMPLATE.md as a guide.")
        sys.exit(1)

if __name__ == "__main__":
    main()
