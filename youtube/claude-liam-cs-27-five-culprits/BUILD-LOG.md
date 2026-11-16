# BUILD-LOG — claude-liam-cs-27-five-culprits

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **B03**: de-wordified SlateCard headline
  - OLD: "When every party was necessary to a failure and none was sufficient al"
  - NEW: "When every party was necessary and none sufficient, who is responsible?"
- **B06**: de-wordified SlateCard headline
  - OLD: "Distributed necessity: each party necessary, none sufficient — the net"
  - NEW: "Distributed necessity: each party necessary, none sufficient alone."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  B03 (SlateCard): verdict card → headline compressed to ≤12w: 'When every party was necessary and none sufficient'
  B06 (SlateCard): verdict card → headline compressed to ≤12w: 'Distributed necessity: each party necessary, none '
  B13 (SlateCard): verdict card → headline compressed to ≤12w: 'Responsibility in distributed systems is a distrib'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
