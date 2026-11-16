#!/usr/bin/env bash
# compile_remaining.sh — compile reels that had de-wordify fixes but no slate cut
# Run from books/ directory: bash computational-skepticism-for-ai/youtube/compile_remaining.sh

set -e
cd "$(dirname "$0")/../.."
BOOKS="$(pwd)"
ART="$BOOKS/brutalist-art/art"
export ART_STRICT=0
export ART_QC=0

REELS=(
  # cs-* series (have mp3s, need Remotion re-render of fixed SlateCard beats)
  computational-skepticism-for-ai/youtube/claude-liam-cs-01-base-rate-trap
  computational-skepticism-for-ai/youtube/claude-liam-cs-02-confident-and-wrong
  computational-skepticism-for-ai/youtube/claude-liam-cs-03-three-way-split
  computational-skepticism-for-ai/youtube/claude-liam-cs-04-clean-but-broken
  computational-skepticism-for-ai/youtube/claude-liam-cs-06-agent-said-done
  computational-skepticism-for-ai/youtube/claude-liam-cs-08-same-net-twice
  computational-skepticism-for-ai/youtube/claude-liam-cs-09-heavy-tail-yank
  computational-skepticism-for-ai/youtube/claude-liam-cs-10-calibration-curve
  computational-skepticism-for-ai/youtube/claude-liam-cs-11-fluency-trap
  computational-skepticism-for-ai/youtube/claude-liam-cs-12-bias-pipe
  computational-skepticism-for-ai/youtube/claude-liam-cs-13-prediction-lock
  computational-skepticism-for-ai/youtube/claude-liam-cs-14-two-clocks
  computational-skepticism-for-ai/youtube/claude-liam-cs-15-shapley-room
  computational-skepticism-for-ai/youtube/claude-liam-cs-16-language-game
  computational-skepticism-for-ai/youtube/claude-liam-cs-17-panda-proxy
  computational-skepticism-for-ai/youtube/claude-liam-cs-18-chart-lie
  computational-skepticism-for-ai/youtube/claude-liam-cs-19-injection-wall
  computational-skepticism-for-ai/youtube/claude-liam-cs-20-error-cascade
  computational-skepticism-for-ai/youtube/claude-liam-cs-21-vigilance-decay
  computational-skepticism-for-ai/youtube/claude-liam-cs-22-calibration-useless
  computational-skepticism-for-ai/youtube/claude-liam-cs-23-subgroup-hidden
  computational-skepticism-for-ai/youtube/claude-liam-cs-24-mnar-bias
  computational-skepticism-for-ai/youtube/claude-liam-cs-25-proxy-column
  computational-skepticism-for-ai/youtube/claude-liam-cs-26-channel-reset
  computational-skepticism-for-ai/youtube/claude-liam-cs-27-five-culprits
  computational-skepticism-for-ai/youtube/claude-liam-cs-28-conformal-wrap
  computational-skepticism-for-ai/youtube/claude-liam-cs-n1-check-the-world
  computational-skepticism-for-ai/youtube/claude-liam-cs-n2-gate-not-vote
  computational-skepticism-for-ai/youtube/claude-liam-cs-n3-number-source
  computational-skepticism-for-ai/youtube/claude-liam-cs-n4-break-your-build
  # deep-* reels that need audio gen + compile
  computational-skepticism-for-ai/youtube/claude-liam-deep-01-skeptics-toolkit
  computational-skepticism-for-ai/youtube/claude-liam-deep-02-probability-confidence
  computational-skepticism-for-ai/youtube/claude-liam-deep-03-data-validation
  computational-skepticism-for-ai/youtube/claude-liam-deep-04-robustness
  computational-skepticism-for-ai/youtube/claude-liam-deep-05-explainability
  computational-skepticism-for-ai/youtube/claude-liam-deep-06-bias
  computational-skepticism-for-ai/youtube/claude-liam-deep-07-fairness-metrics
  computational-skepticism-for-ai/youtube/claude-liam-deep-10-visualization
  computational-skepticism-for-ai/youtube/claude-liam-deep-11-communicating-uncertainty
  computational-skepticism-for-ai/youtube/claude-liam-deep-12-accountability
  computational-skepticism-for-ai/youtube/claude-liam-deep-13-limits-of-ai
  # bs-* series (need audio gen + compile)
  computational-skepticism-for-ai/youtube/claude-liam-bs-01-pick-and-scope
  computational-skepticism-for-ai/youtube/claude-liam-bs-02-five-component-spec
  computational-skepticism-for-ai/youtube/claude-liam-bs-03-adapt-and-justify
  computational-skepticism-for-ai/youtube/claude-liam-bs-04-run-and-attack
  computational-skepticism-for-ai/youtube/claude-liam-bs-05-failure-modes-and-ship
  # cb-* series
  computational-skepticism-for-ai/youtube/claude-liam-cb-01-pebble-and-predict
  computational-skepticism-for-ai/youtube/claude-liam-cb-02-four-moves
  computational-skepticism-for-ai/youtube/claude-liam-cb-03-choose-and-run-a-lens
  computational-skepticism-for-ai/youtube/claude-liam-cb-04-more-lenses-and-the-case
  computational-skepticism-for-ai/youtube/claude-liam-cb-05-attest-and-decide
  computational-skepticism-for-ai/youtube/claude-liam-cb-06-assemble-and-ship
  # gru-* series
  computational-skepticism-for-ai/youtube/claude-liam-gru-01-what-is-gru
  computational-skepticism-for-ai/youtube/claude-liam-gru-02-five-capacities
  computational-skepticism-for-ai/youtube/claude-liam-gru-03-v0-gate
  computational-skepticism-for-ai/youtube/claude-liam-gru-04-command-library
  computational-skepticism-for-ai/youtube/claude-liam-gru-05-boondoggle-score
  computational-skepticism-for-ai/youtube/claude-liam-gru-06-recipe-pipeline
  # standalone
  computational-skepticism-for-ai/youtube/claude-liam-ranfei-visa-risk-runway
)

PASS=0; FAIL=0; SKIP=0

for reel in "${REELS[@]}"; do
  slug=$(basename "$reel")

  # Skip if already compiled
  if ls "${reel}"/*-slate.mp4 2>/dev/null | head -1 | grep -q .; then
    echo "[SKIP] $slug — already has slate cut"
    SKIP=$((SKIP+1))
    continue
  fi

  echo ""
  echo "========================================"
  echo "COMPILING: $slug"
  echo "========================================"

  if "$ART" run "$reel" 2>&1; then
    echo "[OK] $slug compiled"
    PASS=$((PASS+1))

    # Log to BUILD-LOG.md
    blog="$reel/BUILD-LOG.md"
    echo "" >> "$blog"
    echo "## $(date +%Y-%m-%d) — COMPILE (PASS 1 DE-WORDIFY)" >> "$blog"
    echo "Compiled after §8.5 de-wordify fixes. Slate cut generated." >> "$blog"

    # Open the cut
    slate=$(ls "${reel}"/*-slate.mp4 2>/dev/null | head -1)
    [ -n "$slate" ] && open "$slate"
  else
    echo "[FAIL] $slug — compile failed"
    FAIL=$((FAIL+1))
    echo "" >> "$reel/BUILD-LOG.md"
    echo "## $(date +%Y-%m-%d) — COMPILE FAILED (PASS 1)" >> "$reel/BUILD-LOG.md"
    echo "art run failed — see stderr above." >> "$reel/BUILD-LOG.md"
  fi
done

echo ""
echo "========================================"
echo "COMPILE BATCH DONE"
echo "PASS=$PASS FAIL=$FAIL SKIP=$SKIP"
echo "========================================"
