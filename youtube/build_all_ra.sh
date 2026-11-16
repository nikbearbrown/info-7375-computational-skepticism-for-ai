#!/usr/bin/env bash
# Build all 6 episodes of "The Tool That Doubts Itself — The Reallocation Engine, Audited"
# (claude-liam-ra series, INFO 7375 — Computational Skepticism for AI).
# Run from: books/  (or anywhere — BOOKS_DIR resolves relative to this script)
# Logs each reel to BUILD-LOG.md in its folder.

set -euo pipefail

BOOKS_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
BOOK="computational-skepticism-for-ai"
ART="$BOOKS_DIR/brutalist-art/art"

SLUGS=(
  "claude-liam-ra-01-dangerous-shape-and-domain"
  "claude-liam-ra-02-engine-and-gigo-gate"
  "claude-liam-ra-03-bias-and-explanation"
  "claude-liam-ra-04-pearls-ladder"
  "claude-liam-ra-05-fragility-and-hard-stop"
  "claude-liam-ra-06-disclosure-and-ship"
)

PASS=0; FAIL=0; SKIP=0

for SLUG in "${SLUGS[@]}"; do
  REEL="$BOOKS_DIR/$BOOK/youtube/$SLUG"
  if [[ ! -d "$REEL" ]]; then
    echo "SKIP  $SLUG  (folder missing)"
    ((SKIP++))
    continue
  fi

  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "▶  $SLUG"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  if ART_FACTS=0 ART_QC=0 "$ART" run "$REEL" 2>&1 | tee -a "$REEL/BUILD-LOG.md"; then
    echo "✓  PASS  $SLUG"
    ((PASS++))
  else
    echo "✗  FAIL  $SLUG"
    ((FAIL++))
  fi
done

echo ""
echo "═══════════════════════════════"
echo "  PASS=$PASS  FAIL=$FAIL  SKIP=$SKIP"
echo "═══════════════════════════════"
