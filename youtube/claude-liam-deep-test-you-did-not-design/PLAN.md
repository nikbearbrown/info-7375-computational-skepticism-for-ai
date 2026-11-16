# PLAN — claude-liam-deep-test-you-did-not-design

**Title:** The Test You Did Not Design.
**Source:** Bear's skepticism.ai essay "The Limits of AI: What the Tools Cannot Do — The Test You Did Not Design" (Apr 28, 2026) — verbatim in `SOURCE.md`
**Channel:** claude-liam (Liam in for Bear · Kokoro `am_onyx` · free) · Register: Teardown · Greeting: *Hallo, Liam*
**Genre fit:** multi-act (the sequence → three limits → Turing/Searle → where they bite → the authority to refuse → the practice) → deep-explainer, not ai-explainer.
**Runtime:** measured after audio lock (see BUILD-LOG.md); planning estimate ~9–10 min, 40 beats (33 body).

## The spine
```
B00   cold open — ClaudeComposerAsk (the system that passed every test; answered; "Liam, in for Bear")
B01   executive summary — BrutalistHesitantWriter ("tools that will improve" → "the test you did not design")
ACT I    The Sequence Is the Argument     two questions · the battery (Manim) · the composite ward (VOX) · not an anomaly (Manim)
ACT II   Three Limits Scaling Cannot Fix  chips · meaning (Manim) · the objection · the kettle run R1 (VOX×2) · data<world tangent (Manim) · six percent (Manim)
ACT III  Two Famous Arguments             Turing (VOX, Tier 3) · settles/doesn't · Searle page (VOX, Tier 2) · settles/doesn't · both moves (Manim)
ACT IV   Where the Limits Bite            exposure spectrum (Manim) · bedside (VOX) · engineering response (chips) · the limits section as a real file (code beat)
ACT V    The Authority to Say No          refusal assumed away · Apollo 10 MCC (VOX) · the limit case (Manim) · "not a safety practice" (threshold)
ACT VI   What the Work Looks Like         ask → calibration gap (Manim) · the practice (chips) · the structure of the next failure (Manim)
BVDT verdict → BHTF your-turn (prompt read aloud + two checks; "Liam, in for Bear") → BOUT title outro (silent, OUTRO-LOCK)
```

## Lane histogram (body beats only — bookends, asks, closing exempt)
| Lane | Count | Share | Target |
|---|---|---|---|
| VOX | 7 | 21.2% | 20–25% ✅ |
| MANIM | 10 | 30.3% | 25–40% ✅ |
| REMOTION | 10 | 30.3% | 30–45% ✅ |
| CARD | 6 | 18.2% | remainder ✅ |
**Lint: PASS** — no >2 consecutive same-lane beats outside the R1 vox run (`beat_lint.py`: 0 defects, 6 staging advisories on 5-second act cards, each carrying a motion_claim).

## Vox run (the only frame-continuity in the film)
- **R1 — the kettle** (A2V1 → A2V2): tight on the lid and spout (scale 1.35 at [0.5, 0.42]) → eases out to the whole kettle as the claim widens from "you do the pointing" to "someone must supply the pointing." Handoff block authored on A2V1. One plate serves both beats. Never crosses the act boundary.
- All other VOX beats are standalone hard cuts.

## Manim carries the argument
- **A2M2 — the equation tangent** (load-bearing): WORLD ⊃ DATA; competence(DATA) ≠ competence(WORLD); the deployment dot crosses the edge.
- A1M battery · A1M2 structure · A2M symbols/referents · A2M3 six-at-the-boundary · A3M both moves · A4M exposure spectrum · A5M limit case · A6M calibration gap (shape only) · A6M2 the next failure.

## Remotion carries the rhetoric
DeckPattern divergence ×5 (two questions · the objection · Turing · Searle · refusal assumed away), threshold ×1 (not a safety practice), ChipGrid ×3 (three limits · engineering response · the practice), ClaudeCodeBeat ×1 (the limits section, real file), FormACard act cards ×6.

## Pantry (Gate D2 — see SHOPPING.md, written after audio lock)
- **In pantry, rights-cleared by the record:** A1V NLM ward · A2V1/A2V2 Smithsonian kettle (CC0) · A4V NLM bedside · A5V NASA Apollo 10 MCC.
- **Human:** A3V1 Turing portrait (Tier 3) · A3V2 Searle first page (Tier 2). Both slate in the previz; fallbacks named in PROMPTS.md.

## Decisions for Bear at the slate
1. The kettle run (R1) is the one continuity move; the stock compiler zooms each STILL from 1.0 (STILL FIT LAW), so the handoff is authored as data but A2V2's first frame will not pixel-match A2V1's last until the run is rendered as one composition. Keep, or hard-cut?
2. A3V1/A3V2: source the two plates, or take the drawn fallbacks in PROMPTS.md.
3. Runtime: if the locked cut runs past ten minutes, the candidates to shed are A1M2 (structure) and A3R2 (Searle settles) — each folds into its neighbour without re-authoring.
