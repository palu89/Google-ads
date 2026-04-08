#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

status=0

while IFS= read -r file; do
  block="$(awk '
    /^requires:/ { in_requires=1; next }
    in_requires && /^  files:/ { in_files=1; next }
    in_requires && in_files && /^[^[:space:]]/ { in_files=0; in_requires=0 }
    in_files && /^    - / { sub(/^    - /, ""); print }
  ' "$file")"

  [ -z "$block" ] && continue

  count=0
  while IFS= read -r path; do
    [ -z "$path" ] && continue
    count=$((count + 1))

    if [[ "$path" == /* ]]; then
      echo "FAIL [$file]: absolute path not allowed in requires.files -> $path"
      status=1
      continue
    fi

    if [[ "$path" == .codex/* ]]; then
      echo "FAIL [$file]: .codex path not allowed in runtime preload -> $path"
      status=1
      continue
    fi

    if [[ "$path" == skills/docs/reference/* ]] || [[ "$path" == *"googleads-modules.md" ]] || [[ "$path" == *"googleads-field-manual.md" ]]; then
      echo "FAIL [$file]: legacy/invalid preload path -> $path"
      status=1
      continue
    fi

    allowed=0
    if [[ "$path" == docs/reference/* ]] || [[ "$path" == docs/playbooks/* ]] || [[ "$path" == docs/research/* ]]; then
      allowed=1
    else
      skill_dir="$(dirname "$file")"
      if [[ "$path" == "$skill_dir/"* ]]; then
        allowed=1
      fi
    fi

    if [[ $allowed -eq 0 ]]; then
      echo "FAIL [$file]: requires.files path outside GitHub-synced gate -> $path"
      status=1
      continue
    fi

    if [[ ! -f "$ROOT_DIR/$path" ]]; then
      echo "FAIL [$file]: referenced preload file not found -> $path"
      status=1
      continue
    fi
  done <<< "$block"

  if [[ $count -gt 12 ]]; then
    echo "WARN [$file]: requires.files has $count entries (consider low-token preload)"
  fi
done < <(find skills -maxdepth 2 -type f -name SKILL.md -path "*/googleads-*/*" | sort)

if [[ $status -ne 0 ]]; then
  exit 1
fi

echo "googleads requires.files gate: OK"
