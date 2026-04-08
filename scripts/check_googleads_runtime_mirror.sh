#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MIRROR_ROOT="${2:-/Users/palu/.openclaw/workspace-googleads-palu}"
RELATIVE_FILE="${1:-knowledge/googleads/official/india_financial_verification_scope.md}"

SOURCE_FILE="$ROOT_DIR/$RELATIVE_FILE"
MIRROR_FILE="$MIRROR_ROOT/$RELATIVE_FILE"

if [[ ! -f "$SOURCE_FILE" ]]; then
  echo "FAIL: source file not found -> $SOURCE_FILE"
  exit 1
fi

if [[ ! -d "$MIRROR_ROOT" ]]; then
  echo "FAIL: runtime mirror root not found -> $MIRROR_ROOT"
  exit 1
fi

if [[ ! -f "$MIRROR_FILE" ]]; then
  echo "FAIL: runtime mirror missing file -> $MIRROR_FILE"
  exit 1
fi

source_hash="$(shasum -a 256 "$SOURCE_FILE" | awk '{print $1}')"
mirror_hash="$(shasum -a 256 "$MIRROR_FILE" | awk '{print $1}')"

if [[ "$source_hash" != "$mirror_hash" ]]; then
  echo "FAIL: runtime mirror file differs from source"
  echo "  source: $SOURCE_FILE"
  echo "  mirror: $MIRROR_FILE"
  echo "  source_sha256: $source_hash"
  echo "  mirror_sha256: $mirror_hash"
  exit 1
fi

echo "googleads runtime mirror gate: OK"
