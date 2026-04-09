#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PRE_COMMIT_HOOK="$ROOT_DIR/.git/hooks/pre-commit"
PRE_PUSH_HOOK="$ROOT_DIR/.git/hooks/pre-push"
MARK_BEGIN="# >>> googleads-runtime-guard >>>"
MARK_END="# <<< googleads-runtime-guard <<<"

mkdir -p "$(dirname "$PRE_COMMIT_HOOK")"

install_block() {
  local hook_file="$1"
  local block="$2"
  local existing
  local cleaned
  local tmp_file

  if [[ -f "$hook_file" ]]; then
    existing="$(cat "$hook_file")"
  else
    existing='#!/bin/bash
set -e
'
  fi

  cleaned="$(printf '%s\n' "$existing" | awk -v begin="$MARK_BEGIN" -v end="$MARK_END" '
    $0 == begin { skip=1; next }
    $0 == end { skip=0; next }
    !skip { print }
  ')"

  tmp_file="$(mktemp)"
  printf '%s\n\n%s\n' "$cleaned" "$block" > "$tmp_file"
  mv "$tmp_file" "$hook_file"
  chmod +x "$hook_file"
}

pre_commit_block="$MARK_BEGIN
if [ -x \"./scripts/check_googleads_execution_boundary.sh\" ]; then
    echo \"🧭 检查 Google Ads 仓库边界...\"
    ./scripts/check_googleads_execution_boundary.sh pre-commit
fi
if [ -x \"./scripts/check_googleads_requires_sync.sh\" ]; then
    echo \"🧭 检查 Google Ads requires.files 门禁...\"
    ./scripts/check_googleads_requires_sync.sh
fi
$MARK_END"

pre_push_block="$MARK_BEGIN
if [ -x \"./scripts/check_googleads_execution_boundary.sh\" ]; then
    echo \"🧭 检查 Google Ads push 前边界...\"
    ./scripts/check_googleads_execution_boundary.sh pre-push
fi
$MARK_END"

install_block "$PRE_COMMIT_HOOK" "$pre_commit_block"
install_block "$PRE_PUSH_HOOK" "$pre_push_block"

echo "Installed Google Ads runtime guard into .git/hooks/pre-commit and .git/hooks/pre-push"
