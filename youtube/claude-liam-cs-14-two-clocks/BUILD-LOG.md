# BUILD-LOG — claude-liam-cs-14-two-clocks

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **B03**: de-wordified SlateCard headline
  - OLD: "Why does the method that feels worst produce the most durable learning"
  - NEW: "Why does the harder method produce the more durable learning curve?"
- **B06**: de-wordified SlateCard headline
  - OLD: "The two curves start at the same point — and diverge as time and forge"
  - NEW: "Two curves, same start — they diverge as decay accumulates."
- **B13**: de-wordified SlateCard headline
  - OLD: "Fluent curves spike and decay. Frictional curves hold. The cost of the"
  - NEW: "Fluent curves spike and decay. Frictional curves hold. Choose friction."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  B03 (SlateCard): verdict card → headline compressed to ≤12w: 'Why does the harder method produce the more durabl'
  B06 (SlateCard): verdict card → headline compressed to ≤12w: 'Two curves, same start — they diverge as decay acc'
  B13 (SlateCard): verdict card → headline compressed to ≤12w: 'Fluent curves spike and decay. Frictional curves h'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
