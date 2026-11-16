# BUILD-LOG — claude-liam-deep-03-data-validation

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`. NOT produced (downstream of this gate): audio, previz, SHOPPING.md (Gate D2 is after audio lock), render.

## Linter (self-check)
```
== claude-liam-deep-03-data-validation
   beats=36 body=30 est=511s (~8m31s) jsonOK dupIDs=none
   VOX=20.0%(6) MANIM=26.7%(8) REMOTION=30.0%(9) CARD=23.3%(7)
   vox_lint=PASS  spine=OK  same-lane-warns=none
```

## Decisions
- Genre fit: chapter is genuinely multi-act (composite failure → procedural pass & its blind spot → marks/channels → six assumptions → access boundary → six-step reconstruction → delegation line) → deep-explainer is the correct skill, not ai-explainer.
- Register: Teardown (deep-explainer default) — the chapter is a skepticism argument; narration judges procedural EDA, doesn't parrot it.
- Beat mix landed VOX 20% / MANIM 27% / REMOTION 30% / CARD 23%. Lint PASS. Identical split to the ep-04 exemplar by design.
- One vox run only (R1, the access-boundary "story about an agent") — the chapter's one place a continuous camera move earns drama. All other lane changes hard-cut per the vox-run contract.
- Manim carries mechanism/quant (silent join, MNAR taxonomy, channel ranking, Pearson-linear equation tangent, sampling geometry, Plato's cave, prediction-lock gap, solve–verify). Remotion carries structure/rhetoric (join SourceFlow, pass artifact + blind-spot threshold, chart-omission artifact, six-failure ChipGrid + label divergence, six-step SourceFlow, delegation artifact + competence/understanding divergence).
- Composite opening handled per DOUBLE-CHECK LAW: kept as illustration of a mechanism; specific composite row counts softened out of narration (see FACTCHECK).

## MISSING / TODO (post-approval)
- MISSING: `anim.json` classification pass for the DeckPattern beats (A2R2 threshold, A4R2 divergence, A7R2 divergence) — author before build per animated-deck gate.
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`).
- MISSING: FACTCHECK verification pass (Gate F) — Cleveland–McGill ordering, Agents of Chaos citation, composite-case framing flagged VERIFY.
- MISSING: pantry stills (6) — Tier 1, briefs in beat `pantry_brief` fields; SHOPPING.md written after audio lock (Gate D2), NOT at this gate.

## Gate signatures
- PLAN: ____________ (human)   ·   FACTCHECK: ____________   ·   GATE P (narration→audio): ____________

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  A1C (SlateCard): verdict card → headline compressed to ≤12w: 'The Dataset That Destroyed a Deployment'
  A1V (SlateCard): verdict card → headline compressed to ≤12w: 'They blamed the model. It wasn't the model.'
  A1M (SlateCard): verdict card → headline compressed to ≤12w: 'The drop wasn't spread evenly — it had a shape'
  A2C (SlateCard): verdict card → headline compressed to ≤12w: 'What the Pass Cannot See'
  A2R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A2M (SlateCard): verdict card → headline compressed to ≤12w: 'The hard case is invisible to the tool that names '
  A2R2 (DeckPattern): deck note → compressed to ≤12w: 'everything above the line is 'the data as written''
  A2V (SlateCard): verdict card → headline compressed to ≤12w: 'No blank to find — they were never on the page'
  A3C (SlateCard): verdict card → headline compressed to ≤12w: 'A Chart Is an Argument'
  A3M (SlateCard): verdict card → headline compressed to ≤12w: 'Position outranks color — measured, not taste'
  A3M2 (SlateCard): verdict card → headline compressed to ≤12w: 'r ≈ 0, perfectly dependent — the color lied'
  A3R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A4C (SlateCard): verdict card → headline compressed to ≤12w: 'Six Ways to Fail Silently'
  A4R (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A4M (SlateCard): verdict card → headline compressed to ≤12w: 'Train on the reachable — deploy against the world'
  A4R2 (DeckPattern): deck note → compressed to ≤12w: ''
  A5C (SlateCard): verdict card → headline compressed to ≤12w: 'The Boundary Isn't the Schema'
  A5V1 (SlateCard): verdict card → headline compressed to ≤12w: 'They drew the boundary at the corpus'
  A5V2 (SlateCard): verdict card → headline compressed to ≤12w: 'It surfaced what lay beyond the line'
  A5V3 (SlateCard): verdict card → headline compressed to ≤12w: 'The schema plus everything its contents touch'
  A5M (SlateCard): verdict card → headline compressed to ≤12w: 'EDA measures the shadow — the work is turning arou'
  A6C (SlateCard): verdict card → headline compressed to ≤12w: 'Reconstructing the Frame'
  A6V (SlateCard): verdict card → headline compressed to ≤12w: 'Follow it home — it will surprise you'
  A6M (SlateCard): verdict card → headline compressed to ≤12w: 'No lock, no gap — no gap, no learning'
  A7C (SlateCard): verdict card → headline compressed to ≤12w: 'What to Delegate, What to Keep'
  A7R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A7M (SlateCard): verdict card → headline compressed to ≤12w: 'Competence is cheap. Understanding is the work.'
  A7R2 (DeckPattern): deck note → compressed to ≤12w: ''
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
