# BUILD-LOG — claude-liam-deep-01-skeptics-toolkit

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`, `BUILD-LOG.md`. NOT produced (downstream of this gate): audio, previz slate, SHOPPING.md (Gate D2 is after audio lock), render.

## Decisions
- Genre fit: the chapter is genuinely multi-act (two failures → four philosophical moves → verify asymmetry → five capacities → fluency trap) → deep-explainer is the correct skill, not ai-explainer.
- Register: Teardown (deep-explainer default) — the chapter is a skepticism argument; narration narrates each move's mechanism, then judges it (doubt→checklist, induction→confidence-is-not-the-world, falsifiability→rhetoric-vs-engineering, cave→artifact/world/relationship).
- Title "The Metrics Passed. The Patient Didn't." — two-sentence poster line drawn from the chapter's sepsis spine and its returning composite patient (the "labeled stand-in" the chapter builds the toolkit around).
- Beat mix landed VOX 20.0% / MANIM 26.7% / REMOTION 36.7% / CARD 16.7%. Lint PASS; est 518s (~8m38s).
- Exactly one vox run (R1, the composite patient: score → category → consequence) — the one place a continuous camera move earns the drama, and the chapter's own emotional anchor. All other lane changes hard-cut per the vox-run contract.
- Lane assignment: Manim carries the mechanism/quant beats (sepsis scoreboard, doubt-checklist, turkey timeline, distribution shift, black-swan asymmetry, fluency two-stage, verify inversion, two-questions). Remotion carries the rhetorical/structural beats (two-failures shape, the four moves as artifacts, rhetoric→engineering table, cave divergence, unverified-at-scale, five capacities, individual→institutional). Vox carries the three "sit with it" human-scale stills.
- ILLUSTRATE LAW honored: the Claude UI appears only at B00, the A2K ask micro-beat, BVDT verdict, BHTF handoff, BOUT outro. Every body beat illustrates its concept.
- ASK→RESULT LAW: A2K (ClaudeComposerAsk) precedes its Manim RESULT (A2M, the doubt checklist).
- Rough-draft handling: read HEAD side of every merge marker (kept the Knight Capital and COVID-X-ray/COMPAS paragraphs); ignored the non-HEAD "AI Wayback Machine" / "Prompts" apparatus.

## MISSING / TODO (post-approval)
- MISSING: FACTCHECK verification pass (Gate F) — several source numbers flagged VERIFY (sepsis 2/3, Agents-of-Chaos case, Knight Capital 45-min window, Zillow/Google Flu figures, DeGrave shortcut characterization).
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`).
- MISSING: `anim.json` classification pass for the DeckPattern beats (A5R divergence, A6R attrition, A7R2 branch) — author before build per the animated-deck gate.
- MISSING: pantry stills (6, Tier 1) — briefs in each beat's `pantry_brief`; SHOPPING.md written after audio lock (Gate D2), NOT at this gate.

## Gate signatures
- PLAN: ____________ (human)   ·   FACTCHECK: ____________   ·   GATE P (narration→audio): ____________

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  A1C (SlateCard): verdict card → headline compressed to ≤12w: 'Two Failures That Passed'
  A1M (SlateCard): verdict card → headline compressed to ≤12w: 'Every metric passed — two in three still slipped t'
  A1R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A1V1 (SlateCard): verdict card → headline compressed to ≤12w: 'The score is the artifact — not her'
  A1V2 (SlateCard): verdict card → headline compressed to ≤12w: 'The model saw a category — not the clot'
  A1V3 (SlateCard): verdict card → headline compressed to ≤12w: 'What one missed case looks like from the inside'
  A2R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A2M (SlateCard): verdict card → headline compressed to ≤12w: 'Three conditions you can actually check'
  A2V (SlateCard): verdict card → headline compressed to ≤12w: ''Returned success' ≠ 'doing what we intend''
  A3C (SlateCard): verdict card → headline compressed to ≤12w: 'The Turkey With a Spreadsheet'
  A3M (SlateCard): verdict card → headline compressed to ≤12w: 'The turkey knew the correlation, not the mechanism'
  A3R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A3M2 (SlateCard): verdict card → headline compressed to ≤12w: 'The world moves; the confidence line does not'
  A3R2 (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A4R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A4M (SlateCard): verdict card → headline compressed to ≤12w: 'Confirmations never certain — one refutation is'
  A4R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A4V (SlateCard): verdict card → headline compressed to ≤12w: 'Unrefuted is not the same as validated'
  A5C (SlateCard): verdict card → headline compressed to ≤12w: 'The Shadow Is Not the Thing'
  A5R (DeckPattern): deck note → compressed to ≤12w: ''
  A5V (SlateCard): verdict card → headline compressed to ≤12w: 'It read the corner — never the lungs'
  A5M (SlateCard): verdict card → headline compressed to ≤12w: 'Fluency boosts wrong evaluations as readily as rig'
  A5R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A6C (SlateCard): verdict card → headline compressed to ≤12w: 'Cheap to Produce, Expensive to Verify'
  A6M (SlateCard): verdict card → headline compressed to ≤12w: 'Producing is cheap; verifying is dear'
  A6R (DeckPattern): deck note → compressed to ≤12w: 'every unchecked output looks like a success until '
  A7R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A7M (SlateCard): verdict card → headline compressed to ≤12w: 'The wrong question, answered well'
  A7R2 (DeckPattern): deck note → compressed to ≤12w: 'encode the moves into the workflow, or they will n'
  A7SRC (SlateCard): verdict card → headline compressed to ≤12w: 'Documented cases — check them yourself'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
