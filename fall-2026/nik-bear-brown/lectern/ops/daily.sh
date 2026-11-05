#!/usr/bin/env bash
# daily.sh — the daily recipe for the board watch: collect, find what is new, post it, find the faculty listings.
# Standing rule (Professor Bear, 2026-10-19): new possible listings go to the public #professor-bear Discord channel
# automatically, so he can see them without asking. This script is where that happens. It does NOT commit or push:
# pushing a day's delta needs his word (CLAUDE.md), and `publish_delta.py --commit` is the step for that.
#
#   ./ops/daily.sh            # collect the watched boards, post the new listings, then the faculty feed
#   ./ops/daily.sh --no-post  # the same, but post nothing (a test)
#
# The big-four collectors (Google, Microsoft, ...) take hours and run separately:
#   (cd collect && python3 -m collectors.run_daily --only google --text-out ../runs/text)
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/.."        # the lectern/ folder (this file is lectern/ops/daily.sh)
DATE="$(date +%F)"
POST="--post"; SEND="--send"
[[ "${1:-}" == "--no-post" ]] && { POST=""; SEND=""; }

echo "== collect $DATE"
mkdir -p "runs/$DATE"
python3 collect/collect.py --out "runs/$DATE" || { echo "collect failed; nothing posted"; exit 1; }

echo "== what is new, and post it"
python3 publish/publish_delta.py --write $POST || echo "publish_delta stopped (a run already published today, or an error above)"

echo "== churn"
python3 audit/churn.py --write 2>/dev/null || echo "churn needs at least two snapshots; skipped"

echo "== faculty listings"
python3 collect/faculty_feed.py $SEND

echo "== consulting listings (#consulting-firm; ops/consulting_daily.sh, added 2026-11-05)"
bash ops/consulting_daily.sh $([[ -z "$SEND" ]] && echo --no-post) || echo "consulting stopped (see above); the rest of the day is unaffected"

echo "done $DATE. Nothing was committed or pushed."
