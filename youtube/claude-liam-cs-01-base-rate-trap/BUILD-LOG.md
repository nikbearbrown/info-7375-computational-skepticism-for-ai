# BUILD-LOG — claude-liam-cs-01-base-rate-trap

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **B06**: de-wordified SlateCard headline
  - OLD: "The base rate multiplies the error — even great tests drown in false a"
  - NEW: "Base rate multiplies error — great tests drown in false alarms."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  B03 (SlateCard): verdict card → headline compressed to ≤12w: 'What does a positive result actually tell you?'
  B06 (SlateCard): verdict card → headline compressed to ≤12w: 'Base rate multiplies error — great tests drown in '
  B13 (SlateCard): verdict card → headline compressed to ≤12w: 'Rarity manufactures noise faster than accuracy can'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
