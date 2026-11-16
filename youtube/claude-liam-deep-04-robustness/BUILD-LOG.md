# BUILD-LOG — claude-liam-deep-04-robustness

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`. NOT produced (downstream of this gate): audio, previz, SHOPPING.md (Gate D2 is after audio lock), render.

## Decisions
- Genre fit: chapter is genuinely multi-act (demo → reframe → two accounts → taxonomy → toolkit → cross-domain → Rung 3) → deep-explainer is the correct skill, not ai-explainer.
- Register: Teardown (deep-explainer default) — the chapter is a skepticism argument; narration judges the toolkit, doesn't parrot it.
- Beat mix landed VOX 20% / MANIM 27% / REMOTION 30% / CARD 23%. Lint PASS.
- Only one vox run (R1, owner-spoofing) — the chapter's one place a continuous camera move earns drama. All other lane changes hard-cut per the vox-run contract.
- Manim carries the math beats (linearity accumulation w/ equation tangent, boundary tilting, randomized-smoothing vote, scaling plateau, Pearl's ladder). Remotion carries the rhetorical/structural beats (two-diagnoses divergence, taxonomy ChipGrid, profile threshold, cross-domain + disclosure artifacts, governance SourceFlow).

## MISSING / TODO (post-approval)
- MISSING: `anim.json` classification pass for the C2 DeckPattern beats (A2R divergence, A4R2 threshold) — author before build per animated-deck gate.
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`).
- MISSING: FACTCHECK verification pass (Gate F) — several source numbers flagged VERIFY.
- MISSING: pantry stills (6) — Tier 1, briefs in beat `pantry_brief` fields; SHOPPING.md written after audio lock (Gate D2).

## Gate signatures
- PLAN: ____________ (human)   ·   FACTCHECK: ____________   ·   GATE P (narration→audio): ____________

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  A1C (SlateCard): verdict card → headline compressed to ≤12w: 'The Panda That Became a Gibbon'
  A1M (SlateCard): verdict card → headline compressed to ≤12w: 'Panda 94% → Gibbon 99.3% — the image never moved'
  A1V (SlateCard): verdict card → headline compressed to ≤12w: 'It only looked like seeing…'
  A1R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A2C (SlateCard): verdict card → headline compressed to ≤12w: 'Fragile, or Honest?'
  A2R (DeckPattern): deck note → compressed to ≤12w: ''
  A2M (SlateCard): verdict card → headline compressed to ≤12w: 'Hardening moves the surface — not the gap'
  A2V (SlateCard): verdict card → headline compressed to ≤12w: 'Real, predictive, invisible — and the model bet on'
  A3C (SlateCard): verdict card → headline compressed to ≤12w: 'Why They Exist'
  A3M (SlateCard): verdict card → headline compressed to ≤12w: 'Δf = ε‖w‖₁ — tiny per-coordinate, decisive in sum'
  A3M2 (SlateCard): verdict card → headline compressed to ≤12w: 'Tangent to the manifold where training gave no sig'
  A3R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A4C (SlateCard): verdict card → headline compressed to ≤12w: 'Robust Against What?'
  A4R (ChipGrid): chip grid (structured display, individual chips were already ≤12w)
  A4V (SlateCard): verdict card → headline compressed to ≤12w: 'A sticker the size of a coaster'
  A4M (SlateCard): verdict card → headline compressed to ≤12w: 'Adversarial ≠ distribution shift'
  A4R2 (DeckPattern): deck note → compressed to ≤12w: 'one word standing in for a table of evidence it do'
  A5C (SlateCard): verdict card → headline compressed to ≤12w: 'The Toolkit and Its Costs'
  A5R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A5M (SlateCard): verdict card → headline compressed to ≤12w: 'A proof, paid for in thousands of votes'
  A5M2 (SlateCard): verdict card → headline compressed to ≤12w: 'The plateau is semantic, not computational'
  A6C (SlateCard): verdict card → headline compressed to ≤12w: 'The Same Shape Everywhere'
  A6R (ClaudeWindow): artifact/terminal display (labels, not sentences)
  A6V1 (SlateCard): verdict card → headline compressed to ≤12w: 'The agent reads identity off a display name'
  A6V2 (SlateCard): verdict card → headline compressed to ≤12w: 'Right signals → access granted'
  A6V3 (SlateCard): verdict card → headline compressed to ≤12w: 'The same flip — the real feature untouched'
  A7C (SlateCard): verdict card → headline compressed to ≤12w: 'The Question You Can't Close'
  A7M (SlateCard): verdict card → headline compressed to ≤12w: 'A counterfactual the toolkit can't reach'
  A7R2 (ClaudeWindow): artifact/terminal display (labels, not sentences)
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
