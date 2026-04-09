#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HOOKS_DIR="$ROOT_DIR/.githooks"

if [[ ! -d "$HOOKS_DIR" ]]; then
  echo "FAIL: missing versioned hooks directory at $HOOKS_DIR"
  exit 1
fi

chmod +x "$HOOKS_DIR/pre-commit" "$HOOKS_DIR/pre-push"
git -C "$ROOT_DIR" config core.hooksPath .githooks

echo "Installed Google Ads runtime guard via core.hooksPath=.githooks"
