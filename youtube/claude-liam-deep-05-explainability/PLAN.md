# PLAN — claude-liam-deep-05-explainability

**Title:** It Explained the Model. Not the World.
**Source:** `chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md`
**Channel:** claude-liam (Liam in for Bear · Kokoro `am_onyx` · free) · Register: Teardown
**Runtime (estimated):** ~8m36s (33 beats; 28 body) — *estimate only; measured audio is the clock*
**Gate:** PLAN — awaiting human approval. No factcheck, no audio, no render.

## The spine
```
B00  cold open — ClaudeComposerAsk (radiologist ask, answered; Liam signs in)
ACT I    The Explanation That Made It Worse   (radiologist · fluency trap · shortcut learning)
ACT II   What SHAP Is, and What It Isn't       (the core divergence: model's accounting vs the world · Rung 1)
ACT III  The Mathematics of a Shapley Value    (value fn · formula · four axioms · worked example · the zip-code sentence)
ACT IV   LIME and the Counterfactual           (LIME instability/off-manifold · three families · counterfactual Rung 2)
ACT V    Three Words That Aren't Synonyms      (transparency/explainability/interpretability · explainable to whom · signed off wrong)
ACT VI   The Language Game                     (Wittgenstein · Ash "deleted" vox run · the audience question · two reports)
ACT VII  What Honesty Looks Like               (Reichenbach discovery vs justification · the trade-off · supervisory territory)
BVDT verdict → BHTF your-turn → BOUT title outro   (your-turn closing standard)
```

## Lane histogram (body beats only — bookends/ask/closing exempt)
| Lane | Count | Share | Target |
|---|---|---|---|
| VOX | 7 | 25.0% | 20–25% ✅ (at ceiling) |
| MANIM | 8 | 28.6% | 25–40% ✅ |
| REMOTION | 9 | 32.1% | 30–45% ✅ |
| CARD | 4 | 14.3% | remainder · ≤~18% ✅ |
**Lint: PASS** — vox in the 15–30% band; spine present; no >2 consecutive same-lane beats outside the R1 vox run.

## CARD discipline (LEAN — 4 cards, half the acts folded to spark-lines)
Only 4 acts carry a standalone SlateCard opener (I, III, V, VII). Three acts open on a **spark-line** — the act label rides the first content beat instead of a card:
- **ACT II** opens on `A2R` (DeckPattern divergence — title `ACT II · Faithful to the Model, Silent on the World`).
- **ACT IV** opens on `A4M` (Manim LIME — eyebrow `ACT IV · LIME`).
- **ACT VI** opens on `A6R` (DeckPattern divergence — title `ACT VI · Same Words, Two Language Games`).
This keeps CARD at 14.3% (below the ~18% ceiling) and lifts MANIM/REMOTION share.

## The core tension (the chapter's spine, rendered)
"An explanation of the model's internal accounting vs a true account of the world" is carried as a **DeckPattern divergence** twice — `A2R` (SHAP: model's accounting | the world) and `A6R` (same words, two language games) — bracketing the math and the Ash case. This is the single idea the whole episode turns on.

## Manim carries the math, Remotion carries the argument
- **Manim** (8): shortcut correlation (A1M), force-sum/Efficiency (A2M), Rung-1 ceiling (A2M2), Shapley formula w/ equation tangent (A3M), four axioms w/ equation tangent (A3M2), LIME local fit + instability (A4M), counterfactual nearest-flip (A4M2), Reichenbach discovery-vs-justification (A7M).
- **Remotion** (9): decision-artifact ClaudeWindow (A1R), the two divergences (A2R, A6R), worked-example ClaudeWindow (A3R), three-families ChipGrid (A4R), three-words ClaudeWindow (A5R), wrong-property threshold (A5R2), two-reports ClaudeWindow (A6R2), honest-posture ClaudeWindow (A7R).

## Vox run (the only frame-continuity in the film)
- **R1 — Ash's "deleted" report** (A6V1 → A6V2 → A6V3): pull back from the four-word report → the local commands that make it locally true → the provider servers that make it globally false. `handoff` blocks authored on A6V1/A6V2. Length 3 (max); never crosses an act boundary. Every other lane change is a hard cut per the vox-run contract.

## Pantry shopping (Gate D2 preview — NOT locked; written properly only after audio lock)
- **Tier 1** (generic/illustrative, no real referent): A1V radiologist-at-lightbox, A3V zip-block/loan-file, A5V person-with-dense-printout, A6V1/2/3 agent-chat owner-report run.
- **Tier 3** (real named person → rights escalation): **A7V — Hans Reichenbach portrait.** AI-generated from a public-domain Wikimedia photo; provenance/disclosure sidecar REQUIRED at pantry-fill; see FACTCHECK. This is the only rights-flagged asset in the episode.

## ASK→RESULT
One mid-film ask (`A3K`, narration "") precedes the generated Shapley-formula Manim (`A3M`), per the ASK→RESULT LAW. ILLUSTRATE LAW respected: Claude composer/verdict/outro UI appears only at cold open (B00), ask (A3K), verdict (BVDT), handoff (BHTF), outro (BOUT). ClaudeWindow *artifact* surfaces are used as content in the body (matching the exemplar).

## Open decisions for the human at this gate
1. Approve the 7-act cut, or tighten — Act IV (LIME + counterfactual, 3 beats) could merge into Act II if you want a ~7-minute cut.
2. CARD share is already lean (4). If you want the segment markers louder, restore standalone cards for Acts II/IV/VI (raises CARD toward the exemplar's 23%).
3. **A7V Reichenbach (Tier 3):** approve the AI-generated-portrait-from-PD-photo treatment, or drop the portrait and keep A7V as a Tier 1 abstract still (removes the only rights escalation).
4. Voice: default is free Kokoro Liam. Bear's ElevenLabs is opt-in and would pass GATE P.
