#!/usr/bin/env python3
"""
compile_knowledge.py
Scans active Google Ads knowledge files, validates frontmatter, estimates token size,
computes freshness status, and generates ACTIVE_INDEX.yaml.
"""

import os
import sys
import yaml
import re
from datetime import datetime, timezone
from pathlib import Path

# Configuration
KNOWLEDGE_ROOT = Path(__file__).parent.parent / "knowledge"
OUTPUT_INDEX = KNOWLEDGE_ROOT / "googleads" / "ACTIVE_INDEX.yaml"
REQUIRED_FIELDS = [
    "id", "entity_type", "domain", "layer", "task_types", 
    "priority", "status", "source", "source_checked_at",
    "content_updated_at", "depends_on", "summary"
]

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not frontmatter_match:
        return None
    try:
        return yaml.safe_load(frontmatter_match.group(1))
    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")
        return None

def estimate_tokens(content):
    """Simple token estimation: 1 token ≈ 4 characters for English/Chinese mix."""
    return len(content) // 4

def check_freshness(frontmatter):
    """Check if content is fresh based on source_checked_at."""
    if not frontmatter:
        return "unknown"
    
    checked_at = frontmatter.get("source_checked_at")
    if not checked_at or checked_at == "unknown":
        return "unknown"
    
    try:
        if isinstance(checked_at, str):
            checked_date = datetime.fromisoformat(checked_at.replace('Z', '+00:00'))
        else:
            return "unknown"
        
        days_old = (datetime.now(timezone.utc) - checked_date).days
        if days_old > 30:
            return "stale"
        elif days_old > 7:
            return "warning"
        else:
            return "fresh"
    except Exception:
        return "unknown"

def validate_frontmatter(frontmatter, filepath):
    """Validate required fields in frontmatter."""
    if not frontmatter:
        return False, ["No frontmatter found"]
    
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(f"Missing required field: {field}")
        elif frontmatter[field] in [None, "", "unknown"]:
            errors.append(f"Field '{field}' has empty or unknown value")
    
    # Validate specific field formats
    if "id" in frontmatter and not isinstance(frontmatter["id"], str):
        errors.append("Field 'id' must be a string")
    
    if "task_types" in frontmatter:
        if not isinstance(frontmatter["task_types"], list):
            errors.append("Field 'task_types' must be a list")
    
    return len(errors) == 0, errors

def scan_knowledge_files():
    """Scan all knowledge files and collect metadata."""
    knowledge_files = []
    
    for root, dirs, files in os.walk(KNOWLEDGE_ROOT):
        for file in files:
            if file.endswith('.md'):
                filepath = Path(root) / file
                relative_path = filepath.relative_to(KNOWLEDGE_ROOT.parent)
                
                try:
                    content = filepath.read_text(encoding='utf-8')
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    continue
                
                frontmatter = extract_frontmatter(content)
                is_valid, errors = validate_frontmatter(frontmatter, filepath)
                token_estimate = estimate_tokens(content)
                freshness = check_freshness(frontmatter)
                
                knowledge_files.append({
                    "path": str(relative_path),
                    "frontmatter": frontmatter or {},
                    "is_valid": is_valid,
                    "validation_errors": errors,
                    "token_estimate": token_estimate,
                    "freshness": freshness,
                    "content_length": len(content)
                })
    
    return knowledge_files

def generate_index(knowledge_files):
    """Generate ACTIVE_INDEX.yaml from scanned knowledge files."""
    index = {
        "version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_files": len(knowledge_files),
        "valid_files": sum(1 for f in knowledge_files if f["is_valid"]),
        "total_tokens": sum(f["token_estimate"] for f in knowledge_files),
        "freshness_summary": {},
        "knowledge_files": []
    }
    
    # Count freshness status
    freshness_counts = {}
    for f in knowledge_files:
        status = f["freshness"]
        freshness_counts[status] = freshness_counts.get(status, 0) + 1
    index["freshness_summary"] = freshness_counts
    
    # Add file entries
    for f in knowledge_files:
        if not f["frontmatter"]:
            continue
            
        file_entry = {
            "id": f["frontmatter"].get("id", "unknown"),
            "path": f["path"],
            "layer": f["frontmatter"].get("layer", "unknown"),
            "task_types": f["frontmatter"].get("task_types", []),
            "priority": f["frontmatter"].get("priority", 99),
            "status": f["frontmatter"].get("status", "unknown"),
            "freshness": f["freshness"],
            "token_estimate": f["token_estimate"],
            "is_valid": f["is_valid"],
            "validation_errors": f["validation_errors"]
        }
        index["knowledge_files"].append(file_entry)
    
    # Sort by priority then layer
    index["knowledge_files"].sort(key=lambda x: (x["priority"], x["layer"]))
    
    return index

def main():
    print("Compiling Google Ads knowledge index...")
    
    if not KNOWLEDGE_ROOT.exists():
        print(f"Error: Knowledge root not found at {KNOWLEDGE_ROOT}")
        sys.exit(1)
    
    knowledge_files = scan_knowledge_files()
    print(f"Scanned {len(knowledge_files)} knowledge files")
    
    # Validate files
    invalid_files = [f for f in knowledge_files if not f["is_valid"]]
    if invalid_files:
        print(f"\n⚠️  Found {len(invalid_files)} invalid files:")
        for f in invalid_files:
            print(f"  - {f['path']}: {', '.join(f['validation_errors'])}")
    
    # Generate index
    index = generate_index(knowledge_files)
    
    # Write to file
    OUTPUT_INDEX.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_INDEX, 'w', encoding='utf-8') as f:
        yaml.dump(index, f, default_flow_style=False, allow_unicode=True)
    
    print(f"\n✅ Generated ACTIVE_INDEX.yaml at {OUTPUT_INDEX}")
    print(f"   - Total files: {index['total_files']}")
    print(f"   - Valid files: {index['valid_files']}")
    print(f"   - Total tokens: {index['total_tokens']:,}")
    print(f"   - Freshness: {index['freshness_summary']}")
    
    if invalid_files:
        print(f"\n❌ Validation failed for {len(invalid_files)} files")
        if "--strict" in sys.argv:
            sys.exit(1)
    else:
        print("\n✅ All files passed validation")

if __name__ == "__main__":
    main()