# BUILD-LOG — claude-liam-cs-10-calibration-curve

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **B03**: de-wordified SlateCard headline
  - OLD: "What does it mean for a model to be honest about how sure it actually "
  - NEW: "What does it mean for a model to be honest about uncertainty?"
- **B13**: de-wordified SlateCard headline
  - OLD: "Accuracy tells you how often the model lands. Calibration tells you wh"
  - NEW: "Accuracy: how often right. Calibration: how honest about confidence."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  B03 (SlateCard): verdict card → headline compressed to ≤12w: 'What does it mean for a model to be honest about u'
  B06 (SlateCard): verdict card → headline compressed to ≤12w: 'Here is how you build the curve that reveals the l'
  B13 (SlateCard): verdict card → headline compressed to ≤12w: 'Accuracy: how often right. Calibration: how honest'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
