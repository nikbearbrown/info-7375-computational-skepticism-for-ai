Build a deep-explainer reel in the LIAM persona. The FRAME: Liam prompts Claude — "What feedback would Professor Bear give to this student on their Computational Skepticism final project idea?" — and the body IS that feedback. Source: books/computational-skepticism-for-ai/youtube/silent-sql-failures-source.md. Use the deep-explainer skill, Liam persona (claude-liam, Kokoro am_onyx, free). Never publish.

FIRST NAME ONLY: refer to the student as "Zhenhao" throughout — never the full name.

Build INTO: books/computational-skepticism-for-ai/youtube/<slug>/ (suggest slug claude-liam-silent-sql-failures).

## The bookend frame (deep-explainer Claude-composer cold open, Liam voice)
- Cold open: Liam types the ask into the Claude composer — "what feedback would Professor Bear give Zhenhao on their Computational Skepticism final project?" Claude answers; that answer is the reel.
- Verdict recap + YOUR TURN handoff at the close, as the skill specifies.

## Run mode: UNATTENDED until the full-length SLATE PREVIZ cut, then STOP
Do NOT stop at the intermediate gates (plan, GATE P) — audio is free Kokoro, so run straight
through: plan → factcheck → narration → Kokoro audio → audio-lock → compile the full-length
SLATE PREVIZ. Then STOP and open that slate cut for me to view. That previz is the first thing
I watch. Don't fill pantry stills or spend on anything paid before I see the slate cut.

## The body arc (from the source — guidance, not a substitute for your plan)
- The hook: the query that runs clean and returns a wrong number — gross-received vs current
  balance in a UTXO model. Nothing in the output signals the error.
- Loud failure vs quiet failure — why quiet is the hard one (surface plausibility is compromised).
- Bitcoin as testbed: two independent paths (SQL vs RPC/UTXO) → disagreement detection, no human oracle.
- The 5-type error taxonomy (semantic misinterpretation, silent aggregation, temporal/state,
  null-swallowing, reference-frame) — build empirically.
- The 4-tier benchmark (difficulty = # of implicit domain assumptions).
- Three detection strategies: cross-validation (backbone; naive RPC can share the same bug),
  self-consistency (the LIKELY NEGATIVE RESULT — the model fails consistently, so agreement is
  false; report it as a finding), differential testing on synthetic DBs (3 outputs, 2 spent →
  gross 10.0 vs balance 2.0 diverge by construction; property-based testing for SQL semantics).
- Calibration BY TIER — is it overconfident specifically on state-tracking, not just in aggregate.
- What makes it strong vs competent (negative results as findings; name one adjacent domain for
  the generalization claim; justify the tolerance threshold).

Strong Manim/animation beats to consider: the two-path disagreement diagram; the synthetic-DB
divergence (10.0 vs 2.0); a reliability diagram / calibration-by-tier chart. Code beats (Onda
code-block) for the differential-DB skeleton if a beat wants it.

## Standing rules — enforce (violated earlier today)
- Audio-first / fit-to-beat: the COMPILER conforms every clip to its beat (slow-to-fit). NEVER
  hand-time, pre-cut, or pre-bake a clip to beat length. No content beat ships as a slate in the
  FINAL cut (slates are fine in the previz — that's the point of the previz).
- 14pt legibility floor (Standing Rule #5): no on-screen text below 14pt; if it won't fit, use a
  symbol. Applies to the calibration chart's axis/labels especially.
- Render Remotion ONLY via runtime/scripts/remotion_scenes.py <reel> (foreground); match props to
  each component's zod schema; verify by LOOKING at frames + qc-sheet.
- Log my feedback to BUILD-LOG.md first. Unlisted only — human flips public.
