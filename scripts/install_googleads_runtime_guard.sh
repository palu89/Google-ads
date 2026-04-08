#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HOOK_FILE="$ROOT_DIR/.git/hooks/pre-commit"
MARK_BEGIN="# >>> googleads-runtime-guard >>>"
MARK_END="# <<< googleads-runtime-guard <<<"

mkdir -p "$(dirname "$HOOK_FILE")"

if [[ -f "$HOOK_FILE" ]]; then
  existing="$(cat "$HOOK_FILE")"
else
  existing='#!/bin/bash
set -e
'
fi

block="$MARK_BEGIN
if [ -x \"./scripts/check_googleads_requires_sync.sh\" ]; then
    echo \"🧭 检查 Google Ads requires.files 门禁...\"
    ./scripts/check_googleads_requires_sync.sh
fi
$MARK_END"

if [[ "$existing" == *"$MARK_BEGIN"* ]] && [[ "$existing" == *"$MARK_END"* ]]; then
  updated="$(printf '%s' "$existing" | perl -0pe "s/\Q$MARK_BEGIN\E.*?\Q$MARK_END\E/$block/s")"
else
  updated="$existing

$block
"
fi

printf '%s\n' "$updated" > "$HOOK_FILE"
chmod +x "$HOOK_FILE"

echo "Installed Google Ads runtime guard into .git/hooks/pre-commit"
