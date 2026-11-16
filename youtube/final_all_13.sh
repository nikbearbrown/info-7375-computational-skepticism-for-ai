#!/usr/bin/env bash
# Compile clean masters for all 13 Computational Skepticism CLI videos.
# B08 is intentionally optional extra b-roll — --allow-slates skips the gate.
# Run from: books/

set -euo pipefail

BOOKS_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
BOOK="computational-skepticism-for-ai"
ART="$BOOKS_DIR/brutalist-art/art"

SLUGS=(
  "claude-liam-cli-calibration-curve-auditor"
  "claude-liam-cli-base-rate-bayes-calculator"
  "claude-liam-cli-fairness-impossibility-demonstrator"
  "claude-liam-cli-adversarial-perturbation-detector"
  "claude-liam-cli-agent-self-verification-failure"
  "claude-liam-cli-distribution-shift-detector"
  "claude-liam-cli-confusion-matrix-audit"
  "claude-liam-cli-llm-prompt-sensitivity-tester"
  "claude-liam-cli-gate-behavior-test-harness"
  "claude-liam-cli-entity-resolution-matcher"
  "claude-liam-cli-verified-data-output-linter"
  "claude-liam-cli-reliability-diagram-own-model"
  "claude-liam-cli-prediction-lock-harness"
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
  echo "▶  FINAL  $SLUG"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  if ART_FACTS=0 ART_QC=0 "$ART" final --allow-slates "$REEL" 2>&1 | tee -a "$REEL/BUILD-LOG.md"; then
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
echo ""
echo "Clean masters at: <slug>/<slug>-cut.mp4"
