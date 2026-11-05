#!/usr/bin/env bash
# consulting_daily.sh — the day's run of the consulting search: read the consulting firms' boards, judge them, post what is new to #consulting-firm.
# Professor Bear, 2026-11-05: "go" for #consulting-firm, with a daily schedule for the consulting collector (Rule 9 in ../CLAUDE.md).
#
#   ./ops/consulting_daily.sh             # read the 16 boards (about a request a second, titles and places only), post the NEW matches
#   ./ops/consulting_daily.sh --no-post   # the same, but a dry run: nothing is sent and no webhook is read
#
# What keeps it safe: the rules say consulting_rule.posting is "on" (set it to "off" to stop every post); a first send with no memory of earlier
# posts is refused (the baseline of 2026-11-05 made that memory: runs/posted-consulting-to-discord.json); a posted id is never posted twice;
# a board that fails to load costs nothing (it is not read as closed); nothing is committed or pushed here.
# The Mac must be the ONLY place that posts to this channel. The webhook stays in ~/.discord-webhooks/consulting-firm and is never printed.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/.."        # the lectern/ folder (this file is lectern/ops/consulting_daily.sh)
SEND="--send"
[[ "${1:-}" == "--no-post" ]] && SEND=""
echo "== consulting $(date +%F)"
python3 publish/consulting_feed.py --read $SEND
code=$?
echo "consulting_feed exited $code (0 = read, judged and, if there was something new, posted; 3 = a lock held: posting off or no memory of earlier posts)"
exit $code
