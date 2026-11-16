# BUILD-LOG — claude-liam-cs-23-subgroup-hidden

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **B03**: de-wordified SlateCard headline
  - OLD: "What does a clean aggregate calibration number tell you about the subg"
  - NEW: "What does clean aggregate calibration hide about subgroups?"
- **B06**: de-wordified SlateCard headline
  - OLD: "A small subgroup's failure dissolves into a large group's good calibra"
  - NEW: "Small subgroup failure dissolves into a large group's good average."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  B03 (SlateCard): verdict card → headline compressed to ≤12w: 'What does clean aggregate calibration hide about s'
  B06 (SlateCard): verdict card → headline compressed to ≤12w: 'Small subgroup failure dissolves into a large grou'
  B13 (SlateCard): verdict card → headline compressed to ≤12w: 'Aggregate calibration hides subgroup failure — com'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
