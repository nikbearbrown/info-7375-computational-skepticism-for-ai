# BUILD-LOG — claude-liam-deep-07-fairness-metrics

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`. NOT produced (downstream of this gate): audio, previz, SHOPPING.md (Gate D2 is after audio lock), render.

## Decisions
- Genre fit: the chapter is genuinely multi-act (three definitions → the proof → COMPAS → values claims → three exits → the defense) → deep-explainer is the correct skill, not ai-explainer.
- Register: Teardown (deep-explainer default) — the chapter is a skepticism argument; narration judges the metrics and their exits, it does not parrot them.
- Beat mix landed VOX 24% / MANIM 28% / REMOTION 32% / CARD 16%. Lint PASS; est ~489s (~8m9s).
- CARD kept lean (4): Acts III and VI open on a spark-line content beat (A3V1, A6R) rather than a separate SlateCard.
- Only one vox run (R1, the COMPAS "theorem in public") — the chapter's one place a continuous camera move earns drama. All other lane changes hard-cut per the vox-run contract.
- Manim carries the math (Bayes/PPV identity with equation tangent, the two subgroup-rate tables, Lipschitz condition with equation tangent, causal paths + counterfactual, GE decomposition). Remotion carries the rhetorical/structural beats (three-definitions ChipGrid, impossibility-triangle branch DeckPattern, values-claim + toolkit + six-step ClaudeWindow artifacts, exit-relocation SourceFlow, construct-gap threshold).
- Two asks (A2K before the proof render, A5K before the causal render) per ASK→RESULT LAW; both exempt from the body mix.

## MISSING / TODO (post-approval)
- MISSING: `anim.json` classification pass for the DeckPattern beats (A2R branch, A6R3 threshold) — author before build per animated-deck gate.
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`).
- MISSING: FACTCHECK verification pass (Gate F) — impossibility-theorem dating, COMPAS FPR direction/magnitude, and the illustrative table numbers flagged VERIFY.
- MISSING: pantry stills (6) — briefs in each beat's `pantry_brief`; SHOPPING.md written after audio lock (Gate D2). Two Tier-3 assets (COMPAS run, Mill) need rights/disclosure handling.

## Gate signatures
- PLAN: ____________ (human)   ·   FACTCHECK: ____________   ·   GATE P (narration→audio): ____________

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **A2M**: de-wordified SlateCard headline
  - OLD: "v/(1−v) = p/(1−p) · t/f — the base rate does all the work here."
  - NEW: "v/(1−v) = p/(1−p) · t/f — base rate does all the work."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  A1C (SlateCard): verdict card → headline compressed to ≤12w: 'Three Reasonable Definitions'
  A1R (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A1M (SlateCard): verdict card → headline compressed to ≤12w: 'Same matrix — three different cells'
  A1V (SlateCard): verdict card → headline compressed to ≤12w: 'Each one is defensible — alone'
  A2C (SlateCard): verdict card → headline compressed to ≤12w: 'The Four Lines'
  A2M (SlateCard): verdict card → headline compressed to ≤12w: 'v/(1−v) = p/(1−p) · t/f — base rate does all the w'
  A2M2 (SlateCard): verdict card → headline compressed to ≤12w: 'Keep calibration OR equalized odds — never both'
  A2R (DeckPattern): deck note → compressed to ≤12w: ''
  A3V1 (SlateCard): verdict card → headline compressed to ≤12w: 'A risk score walks into a courtroom'
  A3V2 (SlateCard): verdict card → headline compressed to ≤12w: 'Both were right about the numbers'
  A3R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A3M (SlateCard): verdict card → headline compressed to ≤12w: 'The FPR disparity was true — and still not the who'
  A4C (SlateCard): verdict card → headline compressed to ≤12w: 'Each Metric Is a Values Claim'
  A4R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A4V (SlateCard): verdict card → headline compressed to ≤12w: 'Fairness was never one quantity'
  A5C (SlateCard): verdict card → headline compressed to ≤12w: 'The Three Exits'
  A5M (SlateCard): verdict card → headline compressed to ≤12w: 'D(M(x),M(y)) ≤ d(x,y) — everything hinges on d'
  A5V (SlateCard): verdict card → headline compressed to ≤12w: 'Same applicants — the metric decides'
  A5M2 (SlateCard): verdict card → headline compressed to ≤12w: 'Direct, indirect, spurious — you must declare whic'
  A5M3 (SlateCard): verdict card → headline compressed to ≤12w: 'GE = within-group + between-group — measured, not '
  A6R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A6R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A6V (SlateCard): verdict card → headline compressed to ≤12w: 'Someone always decides — the question is whether t'
  A6R3 (DeckPattern): deck note → compressed to ≤12w: 'a perfect re-arrest predictor is still measuring t'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
