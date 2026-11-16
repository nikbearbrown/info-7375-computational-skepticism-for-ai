# BUILD-LOG — claude-liam-deep-10-visualization

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`. NOT produced (downstream of this gate): audio, previz, SHOPPING.md (Gate D2 is after audio lock), render.

## Decisions
- Genre fit: chapter is genuinely multi-act (demo → McLuhan reframe → grammar → catalog → four cases → two-faces-of-doubt → living deck / no-neutral) → deep-explainer is the correct skill, not ai-explainer.
- Register: Teardown (deep-explainer default) — the chapter is a skepticism argument; narration judges the toolkit and the charts, it doesn't parrot them.
- Beat mix landed VOX 20% / MANIM 27% / REMOTION 30% / CARD 23%. Lint PASS. Est ~560s (~9m20s).
- **Manim is the star of this cut** (visualization chapter): five Manim beats animate the SAME data drawn honestly vs misleadingly and animate the transform between them — two-dashboard split (A1M), length-vs-area ink inflation (A3M2), truncated-axis floor climbing (A4M), same-pixels-two-morals (A4M2), and the Reuters axis-inversion flip (A5M, the real named misleading chart). Remotion carries the rhetorical/structural beats (two-beliefs divergence, McLuhan lens artifact, FT ChipGrid, catalog ChipGrid, uncertainty divergence, equal-weight artifact, trade-off divergence, living-deck SourceFlow).
- Only one vox run (R1 = Snow's cholera map, 3 beats) — the chapter's one place a continuous camera move earns drama (zoom in to the pump, pull back to reveal all the pumps). All other historical stills (Challenger, GDELT/Nigeria, Du Bois) are standalone VOX beats, hard-cut, per the vox-run contract.
- ASK→RESULT law honored: two ClaudeComposerAsk micro-beats (A1K before the two-dashboard render, A6K before the quantile-dotplot render). Claude UI appears ONLY at cold open / asks / verdict / handoff / outro (ILLUSTRATE LAW).

## MISSING / TODO (post-approval)
- MISSING: `anim.json` classification pass for the DeckPattern beats (A1R divergence, A4-area threshold A5R, A6R divergence, A7R divergence) — author before build per animated-deck gate.
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`).
- MISSING: FACTCHECK verification pass (Gate F) — Reuters Florida counts, Challenger "13 charts," GDELT attribution flagged VERIFY; El País kept illustrative only.
- MISSING: pantry stills (6): Snow map ×3 (Tier 1), Challenger gantry / GDELT map / Du Bois plate (Tier 2, flagged illustrative). SHOPPING.md written after audio lock (Gate D2), tier-tagged + duration-locked.

## Gate signatures
- PLAN: ____________ (human)   ·   FACTCHECK: ____________   ·   GATE P (narration→audio): ____________

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  A1C (SlateCard): verdict card → headline compressed to ≤12w: 'Two Dashboards, One CSV'
  A1M (SlateCard): verdict card → headline compressed to ≤12w: 'One CSV → two arguments — not a digit changed'
  A1R (DeckPattern): deck note → compressed to ≤12w: ''
  A2C (SlateCard): verdict card → headline compressed to ≤12w: 'The Medium Is the Message'
  A2R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A2M (SlateCard): verdict card → headline compressed to ≤12w: 'The argument lands before the number does'
  A3C (SlateCard): verdict card → headline compressed to ≤12w: 'The Grammar of an Honest Chart'
  A3R (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A3M (SlateCard): verdict card → headline compressed to ≤12w: 'Position > length > angle > area > volume > color'
  A3M2 (SlateCard): verdict card → headline compressed to ≤12w: 'Double the value, quadruple the ink'
  A4C (SlateCard): verdict card → headline compressed to ≤12w: 'The Catalog of Misleading Choices'
  A4R (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A4M (SlateCard): verdict card → headline compressed to ≤12w: 'A 2-point gap, drawn as a landslide'
  A4M2 (SlateCard): verdict card → headline compressed to ≤12w: 'The choice isn't in the pixels'
  A5C (SlateCard): verdict card → headline compressed to ≤12w: 'Charts That Lied — and One That Told the Truth'
  A5V1 (SlateCard): verdict card → headline compressed to ≤12w: 'The evidence was there — the chart was never drawn'
  A5M (SlateCard): verdict card → headline compressed to ≤12w: 'A spike drawn as a decline — every number correct'
  A5R (DeckPattern): deck note → compressed to ≤12w: 'illustrative'
  A5V2 (SlateCard): verdict card → headline compressed to ≤12w: 'Every death mapped to its address'
  A5V3 (SlateCard): verdict card → headline compressed to ≤12w: 'The cluster centers on the Broad Street pump'
  A5V4 (SlateCard): verdict card → headline compressed to ≤12w: 'He showed every pump — that's what made it evidenc'
  A6C (SlateCard): verdict card → headline compressed to ≤12w: 'Two Faces of Doubt'
  A6R (DeckPattern): deck note → compressed to ≤12w: ''
  A6V1 (SlateCard): verdict card → headline compressed to ≤12w: 'A map of news stories, titled as a map of crime'
  A6M (SlateCard): verdict card → headline compressed to ≤12w: 'Four of twenty lands where 20% doesn't'
  A6R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A7C (SlateCard): verdict card → headline compressed to ≤12w: 'The Living Deck & No Neutral'
  A7R (DeckPattern): deck note → compressed to ≤12w: ''
  A7V (SlateCard): verdict card → headline compressed to ≤12w: 'Deliberate choices, politics visible — and honest '
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
