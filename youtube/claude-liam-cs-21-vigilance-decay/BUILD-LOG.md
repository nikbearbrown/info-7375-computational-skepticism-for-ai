# BUILD-LOG — claude-liam-cs-21-vigilance-decay

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **B03**: de-wordified SlateCard headline
  - OLD: "What failure mode does a long correct streak create for the human oper"
  - NEW: "What failure mode does a long correct streak create for the operator?"
- **B06**: de-wordified SlateCard headline
  - OLD: "Vigilance decays as trust grows — the error arrives when checking has "
  - NEW: "Vigilance decays as trust grows — the error arrives unchecked."
- **B13**: de-wordified SlateCard headline
  - OLD: "Design for decaying vigilance — the streak is a risk, not a reason to "
  - NEW: "Design for decaying vigilance. The streak is a risk, not a guarantee."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  B03 (SlateCard): verdict card → headline compressed to ≤12w: 'What failure mode does a long correct streak creat'
  B06 (SlateCard): verdict card → headline compressed to ≤12w: 'Vigilance decays as trust grows — the error arrive'
  B13 (SlateCard): verdict card → headline compressed to ≤12w: 'Design for decaying vigilance. The streak is a ris'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
