#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-pre-commit}"
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"

if [[ -z "$REPO_ROOT" ]]; then
  echo "FAIL: not inside a Git repository"
  exit 1
fi

cd "$REPO_ROOT"

CURRENT_BRANCH="$(git branch --show-current)"
if [[ -z "$CURRENT_BRANCH" ]]; then
  echo "FAIL: detached HEAD is not allowed for Google Ads execution work"
  exit 1
fi

if [[ ! -f "$REPO_ROOT/AGENT_BOOTSTRAP.md" ]] || [[ ! -f "$REPO_ROOT/registry/repo.yaml" ]]; then
  echo "FAIL: repository root does not contain required Google Ads bootstrap files"
  exit 1
fi

if [[ "$MODE" == "pre-push" ]]; then
  if [[ -n "$(git status --porcelain)" ]]; then
    echo "FAIL: working tree is not clean before push"
    exit 1
  fi
fi

echo "googleads execution boundary gate: OK ($MODE, branch=$CURRENT_BRANCH)"
