Build a deep-explainer reel in the LIAM persona. The FRAME: Liam prompts Claude — "What feedback would Professor Bear give to this student on their Computational Skepticism final project idea?" — and the body IS that feedback. Source: books/computational-skepticism-for-ai/youtube/financial-stress-index-source.md. Use the deep-explainer skill, Liam persona (claude-liam, Kokoro am_onyx, free). Never publish.

FIRST NAME ONLY: refer to the student as "Mickey" throughout — never the full name.

Build INTO: books/computational-skepticism-for-ai/youtube/<slug>/ (suggest slug claude-liam-financial-stress-index).

## The bookend frame (deep-explainer Claude-composer cold open, Liam voice)
- Cold open: Liam types the ask into the Claude composer — "what feedback would Professor Bear give Mickey on their Computational Skepticism final project?" Claude answers; that answer is the reel.
- Verdict recap + YOUR TURN handoff at the close, as the skill specifies.

## Run mode: UNATTENDED until the full-length SLATE PREVIZ cut, then STOP
Do NOT stop at the intermediate gates (plan, GATE P) — audio is free Kokoro, so run straight
through: plan → factcheck → narration → Kokoro audio → audio-lock → compile the full-length
SLATE PREVIZ. Then STOP and open that slate cut for me to view. That previz is the first thing
I watch. Don't fill pantry stills or spend on anything paid before I see the slate cut.

## The body arc (from the source — guidance, not a substitute for your plan)
- Hook: one headline stress number hides six very different drivers — and the project wants to
  look inside. Good question; the trap is that the index's CONSTRUCTION makes clean attribution
  structurally hard.
- Part 1 — attribution is structural, not a modeling choice: collinear inputs (in a crisis
  "everything correlates to 1") mean NO single correct decomposition. SHAP vs regression give
  different answers because they define "contribution" differently. Lead with a VIF diagnostic —
  a VIF spike in crises is itself the finding.
- Part 2 — small-N crisis problem: "importance changes during crises" is really estimated on ~3
  data points (2008, 2020, 2022). Perturb the crisis-window boundaries ±1 month; if the ranking
  reorders, that instability IS the result.
- Part 3 — TDA needs its own sensitivity sweep: persistence diagrams are artifacts of embedding
  dim / window length unless shown robust across a range; cross-validate against Part 1.
- Part 4 — descriptive vs causal language: "accounts for 40% of variance" (ok) vs "caused the
  spike" (none of the three methods support it). Audit the causal verbs.
- Part 5 — honest visualization under collinearity: banded not crisp contributions; small-multiple
  persistence diagrams; show where the three methods agree AND disagree.
- Close: the publication note (reviewers WILL probe collinearity + crisis-N, so build the checks in
  now) + open questions handed back to Mickey.

Strong Manim/animation beats: the collinearity → "no unique decomposition" idea (two 0.9-correlated
bars splitting credit); the VIF-spikes-in-crisis time series; the ~3-crisis small-N point; the
TDA parameter-sensitivity small multiples; a Shapley-vs-regression-vs-TDA agree/disagree panel.
Code beats (Onda code-block) for the VIF diagnostic skeleton if a beat wants it.

## Standing rules — enforce (violated earlier today)
- Audio-first / fit-to-beat: the COMPILER conforms every clip to its beat (slow-to-fit). NEVER
  hand-time, pre-cut, or pre-bake a clip to beat length. No content beat ships as a slate in the
  FINAL cut (slates are fine in the previz — that's the point of the previz).
- 14pt legibility floor (Standing Rule #5): no on-screen text below 14pt; if it won't fit, use a
  symbol. Applies to the VIF/contribution/persistence charts' axes and labels especially.
- Render Remotion ONLY via runtime/scripts/remotion_scenes.py <reel> (foreground); match props to
  each component's zod schema; verify by LOOKING at frames + qc-sheet.
- Log my feedback to BUILD-LOG.md first. Unlisted only — human flips public.
