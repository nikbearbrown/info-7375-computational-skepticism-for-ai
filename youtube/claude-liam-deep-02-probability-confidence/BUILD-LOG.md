# BUILD-LOG — claude-liam-deep-02-probability-confidence

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`. NOT produced (downstream of this gate): audio, previz, SHOPPING.md (Gate D2 is after audio lock), render.

## Linter (self-check, PASS)
```
== claude-liam-deep-02-probability-confidence
   beats=35 body=29 est=574s (~9m34s) jsonOK dupIDs=none
   VOX=24.1%(7) MANIM=31.0%(9) REMOTION=34.5%(10) CARD=10.3%(3)
   vox_lint=PASS  spine=OK  same-lane-warns=none
```

## Decisions
- Genre fit: the chapter is genuinely multi-act (degrees of belief → conditioning → chains/partitions → the base-rate demo → distribution shift → calibration → heavy tails + synthesis) → deep-explainer is the correct skill, not ai-explainer.
- Register: Teardown — the chapter is a skepticism argument ("confident numbers are not correct numbers"); narration judges the number, doesn't parrot the math.
- Cold open uses the chapter's signature demo (99%-accurate test → ~1%) as the one-question hook, mirroring the exemplar's panda→gibbon structure.
- Manim carries the probability/calibration spine (9 beats: axioms, conditioning, chain rule, total probability, count-the-bodies, Hume/drift, calibration curve, temperature scaling, heavy-tail mean). Remotion carries the rhetorical/structural beats (Boolean-vs-probabilistic, the two divergences, false-positive ChipGrid, drift SourceFlow, rejection-condition threshold, four-questions artifact).
- CARD deliberately lean (3, 10.3%): only Acts I/IV/VI carry a slate; Acts II/III/V/VII spark-open on the first content beat's SlateCard eyebrow.
- Exactly one vox run (R1, alert fatigue, A4V1→3) — the chapter's one place a continuous camera move earns drama (the on-call engineer learning to ignore the alarms, then missing the real one). All other lane changes hard-cut per the vox-run contract.
- Beat mix landed VOX 24.1% / MANIM 31.0% / REMOTION 34.5% / CARD 10.3%. Lint PASS.

## MISSING / TODO (post-approval)
- MISSING: FACTCHECK verification pass (Gate F) — Casscells 95%, Wong sepsis 18%/33%, DeGrave imaging, Ramsey biography all flagged VERIFY.
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`).
- MISSING: `anim.json` classification pass for the C2 DeckPattern beats (A2R/A3R divergence, A6R/A7R threshold+scale) — author before build per animated-deck gate.
- MISSING: pantry stills (7) — 6 Tier 1 + 1 Tier 3 (A7V Ramsey, rights escalation); briefs in beat `pantry_brief` fields; SHOPPING.md written after audio lock (Gate D2).
- RIGHTS: A7V Ramsey portrait — confirm public-domain source photo + attach AI-generated disclosure sidecar before fill.

## Gate signatures
- PLAN: ____________ (human)   ·   FACTCHECK: ____________   ·   GATE P (narration→audio): ____________

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  A1C (SlateCard): verdict card → headline compressed to ≤12w: 'Degrees of Belief'
  A1R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A1V (SlateCard): verdict card → headline compressed to ≤12w: 'Different priors — both correct'
  A1M (SlateCard): verdict card → headline compressed to ≤12w: 'Three axioms — everything else is derived'
  A2M (SlateCard): verdict card → headline compressed to ≤12w: 'Given what I already know'
  A2R (DeckPattern): deck note → compressed to ≤12w: ''
  A3M (SlateCard): verdict card → headline compressed to ≤12w: 'One report, a product of shrinking conditionals'
  A3R (DeckPattern): deck note → compressed to ≤12w: ''
  A3M2 (SlateCard): verdict card → headline compressed to ≤12w: '3.2% — a rate no single model reports'
  A4C (SlateCard): verdict card → headline compressed to ≤12w: 'The Test That's 99% Accurate'
  A4M (SlateCard): verdict card → headline compressed to ≤12w: '1 true positive, ~100 false — 1 in 101'
  A4R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A4V1 (SlateCard): verdict card → headline compressed to ≤12w: 'A rare-event detector fires mostly false'
  A4V2 (SlateCard): verdict card → headline compressed to ≤12w: 'Within a week, the alarms mean nothing'
  A4V3 (SlateCard): verdict card → headline compressed to ≤12w: 'The real one scrolls past, unread'
  A4R2 (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A5R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A5M (SlateCard): verdict card → headline compressed to ≤12w: 'Training is the past. Deployment is the future.'
  A5V (SlateCard): verdict card → headline compressed to ≤12w: 'Confident into a world that had moved'
  A6C (SlateCard): verdict card → headline compressed to ≤12w: 'Calibration'
  A6M (SlateCard): verdict card → headline compressed to ≤12w: 'Calibrated = stated probabilities come true'
  A6M2 (SlateCard): verdict card → headline compressed to ≤12w: 'softmax(z / T) — one parameter, honesty restored'
  A6V (SlateCard): verdict card → headline compressed to ≤12w: 'Your 90% intervals hold about half the time'
  A6R (DeckPattern): deck note → compressed to ≤12w: 'trust a stated probability only against its calibr'
  A7M (SlateCard): verdict card → headline compressed to ≤12w: 'When the average never settles'
  A7R (DeckPattern): deck note → compressed to ≤12w: 'one-in-a-thousand catastrophic error dominates a h'
  A7V (SlateCard): verdict card → headline compressed to ≤12w: 'Probability is a property of belief'
  A7R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
