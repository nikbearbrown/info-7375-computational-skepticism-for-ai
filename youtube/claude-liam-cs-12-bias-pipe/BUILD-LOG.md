# BUILD-LOG — claude-liam-cs-12-bias-pipe

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **B03**: de-wordified SlateCard headline
  - OLD: "Why does fixing the model or the data often fail to fix the downstream"
  - NEW: "Why does fixing the model often fail to fix the outcome?"
- **B06**: de-wordified SlateCard headline
  - OLD: "Leverage means finding the path carrying the most flow — and blocking "
  - NEW: "Find the path carrying most flow — block it at the source."
- **B13**: de-wordified SlateCard headline
  - OLD: "Bias flows through paths. Block one, the flow reroutes. Leverage is ho"
  - NEW: "Bias flows through paths. Block one, it reroutes. Leverage matters."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  B03 (SlateCard): verdict card → headline compressed to ≤12w: 'Why does fixing the model often fail to fix the ou'
  B06 (SlateCard): verdict card → headline compressed to ≤12w: 'Find the path carrying most flow — block it at the'
  B13 (SlateCard): verdict card → headline compressed to ≤12w: 'Bias flows through paths. Block one, it reroutes. '
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
