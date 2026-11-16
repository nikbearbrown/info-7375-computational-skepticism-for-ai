# BUILD-LOG — claude-liam-cs-02-confident-and-wrong

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **B06**: de-wordified SlateCard headline
  - OLD: "Bias is a structural offset — data shrinks the scatter but not the off"
  - NEW: "Bias is structural. More data shrinks scatter, not the offset."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  B03 (SlateCard): verdict card → headline compressed to ≤12w: 'What does adding more data do to a biased estimato'
  B06 (SlateCard): verdict card → headline compressed to ≤12w: 'Bias is structural. More data shrinks scatter, not'
  B13 (SlateCard): verdict card → headline compressed to ≤12w: 'Scale buys precision. It never buys correction.'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
