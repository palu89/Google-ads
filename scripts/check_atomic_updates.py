#!/usr/bin/env python3
"""
check_atomic_updates.py
Detects atomic update violations in the repository.
Checks for changes to active knowledge without index regeneration,
stateful project changes without CURRENT_STATE update, and router changes without registry sync.
"""

import os
import sys
import re
import subprocess
from pathlib import Path
from datetime import datetime, timezone

# Configuration
REPO_ROOT = Path(__file__).parent.parent
KNOWLEDGE_DIR = REPO_ROOT / "knowledge"
PROJECTS_DIR = REPO_ROOT / "projects"
REGISTRY_DIR = REPO_ROOT / "registry"
ACTIVE_INDEX = KNOWLEDGE_DIR / "googleads" / "ACTIVE_INDEX.yaml"
TASK_ROUTER = KNOWLEDGE_DIR / "googleads" / "TASK_ROUTER.yaml"
GOOGLEADS_REGISTRY = REGISTRY_DIR / "googleads.yaml"

def check_knowledge_index_freshness():
    """Check if knowledge files have changed without index regeneration."""
    if not ACTIVE_INDEX.exists():
        return False, "ACTIVE_INDEX.yaml does not exist"
    
    try:
        import yaml
        with open(ACTIVE_INDEX, 'r', encoding='utf-8') as f:
            index_data = yaml.safe_load(f)
        
        generated_at = index_data.get("generated_at")
        if not generated_at:
            return False, "ACTIVE_INDEX.yaml missing generated_at timestamp"
        
        # Parse timestamp
        try:
            if isinstance(generated_at, str):
                index_time = datetime.fromisoformat(generated_at.replace('Z', '+00:00'))
            else:
                return False, "Invalid timestamp format in ACTIVE_INDEX.yaml"
        except ValueError:
            return False, "Could not parse timestamp in ACTIVE_INDEX.yaml"
        
        # Use Git commit timestamps instead of filesystem mtimes so CI checkouts
        # do not falsely mark every knowledge file as newer than the index.
        latest_file = None
        latest_time = None

        for root, dirs, files in os.walk(KNOWLEDGE_DIR):
            for file in files:
                if not file.endswith('.md'):
                    continue

                filepath = Path(root) / file
                relpath = str(filepath.relative_to(REPO_ROOT))

                result = subprocess.run(
                    ["git", "log", "-1", "--format=%cI", "--", relpath],
                    cwd=REPO_ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )

                timestamp = result.stdout.strip()
                if not timestamp:
                    continue

                try:
                    file_time = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                except ValueError:
                    continue

                if latest_time is None or file_time > latest_time:
                    latest_time = file_time
                    latest_file = filepath

        if latest_file and latest_time and latest_time > index_time:
            return False, f"Knowledge file {latest_file.name} modified after index generation"
        
        return True, "Knowledge index is fresh"
    except Exception as e:
        return False, f"Error checking knowledge index: {e}"

def check_project_state_updates():
    """Check if project files have changed without CURRENT_STATE updates."""
    violations = []
    
    if not PROJECTS_DIR.exists():
        return True, "No projects directory"
    
    for project_dir in PROJECTS_DIR.iterdir():
        if project_dir.is_dir():
            project_yaml = project_dir / "project.yaml"
            current_state = project_dir / "CURRENT_STATE.md"
            
            if project_yaml.exists():
                if current_state.exists():
                    # Check modification times
                    yaml_mtime = project_yaml.stat().st_mtime
                    state_mtime = current_state.stat().st_mtime
                    
                    # Allow 5-minute grace period for concurrent edits
                    if yaml_mtime > state_mtime + 300:
                        violations.append(f"{project_dir.name}: project.yaml modified without CURRENT_STATE.md update")
                else:
                    violations.append(f"{project_dir.name}: Missing CURRENT_STATE.md")
    
    if violations:
        return False, f"Project state violations: {', '.join(violations)}"
    return True, "All projects have current state files"

def check_registry_sync():
    """Check if router changes are reflected in registry."""
    try:
        import yaml
        
        if not TASK_ROUTER.exists() or not GOOGLEADS_REGISTRY.exists():
            return True, "Missing router or registry files"
        
        with open(TASK_ROUTER, 'r', encoding='utf-8') as f:
            router_data = yaml.safe_load(f)
        
        with open(GOOGLEADS_REGISTRY, 'r', encoding='utf-8') as f:
            registry_data = yaml.safe_load(f)
        
        # Check if TASK_ROUTER exists in registry
        router_path = registry_data.get("task_router")
        if router_path != str(TASK_ROUTER.relative_to(REPO_ROOT)):
            return False, "Registry task_router path does not match actual TASK_ROUTER.yaml location"
        
        # Check if knowledge files in router are in registry
        router_files = set()
        if "task_mappings" in router_data:
            for mapping in router_data["task_mappings"].values():
                if "knowledge_files" in mapping:
                    router_files.update(mapping["knowledge_files"])
        
        registry_files = set()
        if "knowledge_files" in registry_data:
            for file_entry in registry_data["knowledge_files"]:
                if "id" in file_entry:
                    registry_files.add(file_entry["id"])
        
        missing_in_registry = router_files - registry_files
        if missing_in_registry:
            return False, f"Knowledge files in router missing from registry: {missing_in_registry}"
        
        return True, "Registry is in sync with router"
    except Exception as e:
        return False, f"Error checking registry sync: {e}"

def main():
    print("Checking atomic update violations...")
    
    checks = [
        ("Knowledge Index Freshness", check_knowledge_index_freshness()),
        ("Project State Updates", check_project_state_updates()),
        ("Registry Sync", check_registry_sync()),
    ]
    
    all_passed = True
    violations = []
    
    for check_name, (passed, message) in checks:
        if passed:
            print(f"✅ {check_name}: {message}")
        else:
            print(f"❌ {check_name}: {message}")
            all_passed = False
            violations.append(f"{check_name}: {message}")
    
    print()
    
    if all_passed:
        print("✅ All atomic update checks passed")
        sys.exit(0)
    else:
        print("❌ Atomic update violations detected:")
        for violation in violations:
            print(f"   - {violation}")
        print("\nRemediation steps:")
        print("1. Run scripts/compile_knowledge.py to regenerate index")
        print("2. Update CURRENT_STATE.md for modified projects")
        print("3. Sync registry/googleads.yaml with knowledge/googleads/TASK_ROUTER.yaml")
        sys.exit(1)

if __name__ == "__main__":
    main()
