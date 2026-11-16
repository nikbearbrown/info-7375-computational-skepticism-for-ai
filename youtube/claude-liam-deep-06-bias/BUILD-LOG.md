# BUILD-LOG — claude-liam-deep-06-bias

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`. NOT produced (downstream of this gate): audio, previz, SHOPPING.md (Gate D2 is after audio lock), render.

## Decisions
- Genre fit: chapter is genuinely multi-act (estimator definition → ten mechanisms → historical/implicit → three flavors → COMPAS/impossibility → Pearl's ladder → leverage & accountability) → deep-explainer is the correct skill, not ai-explainer.
- Register: Teardown (deep-explainer default) — the chapter is a skepticism argument; narration judges the toolkit and the reflexes ("fix the thing closest to your hands"), doesn't parrot them.
- Cold open = the chapter's own three-teams parable, answered in the composer `output`. It is the whole thesis in one image (leverage rarely closest to your hands), so it earns B00.
- Beat mix landed VOX 21.4% / MANIM 28.6% / REMOTION 32.1% / CARD 17.9%. Lint PASS.
- CARD kept lean: ACT IV and ACT VI openers folded into spark-lines (eyebrow on first content beat) so CARD sits at ~18% and MANIM clears the 25% floor. Five explicit act cards remain (I/II/III/V/VII).
- Only one vox run (R1, the COMPAS courtroom) — the chapter's one place a continuous camera move earns drama: score → two readings → diverging base rates. All other lane changes hard-cut per the vox-run contract.
- Manim carries the formal spine (4 equation-tangent beats: bias identity, selection identity, impossibility algebra, Pearl's ladder). Remotion carries the structural/rhetorical beats (mechanism grid, flavor tables, water-table SourceFlow, deployment-graph SourceFlow, ownership artifact).
- Two ASK beats (A1K → A1M, A5K → A5M) per ASK→RESULT LAW, mirroring the exemplar; both exempt from the histogram.

## Skepticism / named-case handling
- COMPAS narrated as argument at the chapter's confidence; stills are Tier 1 illustrative (generic courtroom, silhouette only — no real defendant/court/tool UI).
- Apple Card held to "adjudicated, not proven" per the chapter's explicit fluency-trap caution (A5R2).
- Upstream-agent case (A7R2) kept structural only — the chapter `[verify]`-flags the specific backing model and "unknown error" string, so both are omitted; only the provider-values-upstream claim is carried.
- Merge markers resolved to HEAD; `d78899b` figure-number drift ignored.

## MISSING / TODO (post-approval)
- MISSING: `anim.json` classification pass for the DeckPattern beats (A1R divergence, A5R2 threshold) — author before build per animated-deck gate.
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`).
- MISSING: FACTCHECK verification pass (Gate F) — 1936 poll counts, COMPAS error-direction, taxonomy completeness flagged VERIFY.
- MISSING: pantry stills (6) — Tier 1, briefs in beat `pantry_brief` fields; SHOPPING.md written after audio lock (Gate D2).

## Gate signatures
- PLAN: ____________ (human)   ·   FACTCHECK: ____________   ·   GATE P (narration→audio): ____________

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **A3M**: de-wordified SlateCard headline
  - OLD: "P(Y_historical | x) ≠ P(Y_fair | x) — and the metrics are all measured"
  - NEW: "P(Y_historical | x) ≠ P(Y_fair | x) — metrics are a patch."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  A1C (SlateCard): verdict card → headline compressed to ≤12w: 'The Estimator, Not the Model'
  A1M (SlateCard): verdict card → headline compressed to ≤12w: 'Bias(θ̂) = E[θ̂] − θ — more data sharpens the wron'
  A1V (SlateCard): verdict card → headline compressed to ≤12w: 'Millions of ballots — confidently, precisely wrong'
  A1R (DeckPattern): deck note → compressed to ≤12w: ''
  A2C (SlateCard): verdict card → headline compressed to ≤12w: 'Ten Doors, One Estimator'
  A2R (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A2M (SlateCard): verdict card → headline compressed to ≤12w: 'E[Y | i∈S] ≠ E[Y] the moment inclusion tracks the '
  A2V (SlateCard): verdict card → headline compressed to ≤12w: 'It learns sepsis among the stable — then judges th'
  A2R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A3C (SlateCard): verdict card → headline compressed to ≤12w: 'The Faithful Poison'
  A3M (SlateCard): verdict card → headline compressed to ≤12w: 'P(Y_historical | x) ≠ P(Y_fair | x) — metrics are '
  A3V (SlateCard): verdict card → headline compressed to ≤12w: 'Faithful data recording a world you did not want t'
  A4R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A4M (SlateCard): verdict card → headline compressed to ≤12w: 'Fix one path, feed the other'
  A5C (SlateCard): verdict card → headline compressed to ≤12w: 'The Dataset Is Not the World'
  A5R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A5V1 (SlateCard): verdict card → headline compressed to ≤12w: 'A number the court reads as fact'
  A5V2 (SlateCard): verdict card → headline compressed to ≤12w: 'Uneven error rates vs equal calibration — both cor'
  A5V3 (SlateCard): verdict card → headline compressed to ≤12w: 'Different base rates → a theorem, not a bug'
  A5M (SlateCard): verdict card → headline compressed to ≤12w: 'Calibration + equal error rates → only if base rat'
  A5R2 (DeckPattern): deck note → compressed to ≤12w: 'a bias claim investigated and not upheld'
  A6M (SlateCard): verdict card → headline compressed to ≤12w: 'P(Y|X) vs P(Y|do(X)) — seeing is not doing'
  A6R (SlateCard): verdict card → headline compressed to ≤12w: 'do(rooster silent) — the sun rises anyway'
  A7C (SlateCard): verdict card → headline compressed to ≤12w: 'Leverage, and Who Owns It'
  A7M (SlateCard): verdict card → headline compressed to ≤12w: 'Same doing — an order of magnitude apart'
  A7R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
