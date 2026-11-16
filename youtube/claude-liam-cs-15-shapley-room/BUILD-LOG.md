# BUILD-LOG — claude-liam-cs-15-shapley-room

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **B03**: de-wordified SlateCard headline
  - OLD: "Is there one correct way to split credit among features in a machine-l"
  - NEW: "Is there one correct way to split credit among model features?"
- **B13**: de-wordified SlateCard headline
  - OLD: "Shapley values: average marginal contributions over all orderings of t"
  - NEW: "Shapley: average marginal contributions across all feature orderings."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  B03 (SlateCard): verdict card → headline compressed to ≤12w: 'Is there one correct way to split credit among mod'
  B06 (SlateCard): verdict card → headline compressed to ≤12w: 'The Shapley solution: average across all orderings'
  B13 (SlateCard): verdict card → headline compressed to ≤12w: 'Shapley: average marginal contributions across all'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
