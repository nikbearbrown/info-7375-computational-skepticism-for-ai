Build a deep-explainer reel in the LIAM persona. The FRAME: Liam prompts Claude — "What feedback would Professor Bear give to this student on their Computational Skepticism final project idea?" — and the body IS that feedback. Source: books/computational-skepticism-for-ai/youtube/research-like-roles-source.md. Use the deep-explainer skill, Liam persona (claude-liam, Kokoro am_onyx, free). Never publish.

FIRST NAME ONLY: refer to the student as "Zening" throughout — never the full name.

Build INTO: books/computational-skepticism-for-ai/youtube/<slug>/ (suggest slug claude-liam-research-like-roles).

## The bookend frame (deep-explainer Claude-composer cold open, Liam voice)
- Cold open: Liam types the ask into the Claude composer — "what feedback would Professor Bear give Zening on their Computational Skepticism final project?" Claude answers; that answer is the reel.
- Verdict recap + YOUR TURN handoff at the close, as the skill specifies.

## Run mode: UNATTENDED until the full-length SLATE PREVIZ cut, then STOP
Do NOT stop at the intermediate gates (plan, GATE P) — audio is free Kokoro, so run straight
through: plan → factcheck → narration → Kokoro audio → audio-lock → compile the full-length
SLATE PREVIZ. Then STOP and open that slate cut for me to view. That previz is the first thing
I watch. Don't fill pantry stills or spend on anything paid before I see the slate cut.

## The body arc (from the source — guidance, not a substitute for your plan)
- Hook: the dev job is quietly becoming research-like — problem definition + experimentation for
  humans, implementation for the LLM, PhD-advisor-style supervision. Great thesis; the trap is the
  method (a search filter on an undefended construct + a causal claim it can't test).
- Part 1 — operationalize BEFORE looking: finalize a checkable coding scheme first, or the
  characteristics become a post-hoc description of the postings you picked (circularity). Inter-rater
  agreement is the first deliverable; low agreement is itself a finding.
- Part 2 — LANGUAGE vs PRACTICE (biggest risk): postings are recruiter marketing; buzzwords inflate.
  Split "postings USE research-like language" (testable) from "jobs ARE structured that way" (needs
  non-posting evidence). Scope claims to what the data supports.
- Part 3 — the causal claim needs a comparison: flat/research-like teams predate LLMs by decades.
  Add a time (pre/post ~2022) or cross-section (high vs low AI-adoption firms) comparison, else
  soften "LLMs cause this" to a hypothesis.
- Part 4 — Engine architecture: this is a NEW NLP layer, not an extension of the visa/funding
  scoring — state whether it's a standalone classifier or a new scored dimension.
- Part 5 — robustness + honest viz: inter-rater reliability; keyword sensitivity; base-rate honesty
  (sample sizes/CIs per period — small early samples fake trends); co-occurrence labeled as
  co-occurrence, not causation.
- Close: open questions handed back to Zening (what non-posting source validates real structure?
  what's a defensible pre-LLM baseline?).

Strong Manim/animation beats: the circularity loop (define → select → redefine); the language-vs-
practice split (same buzzword posting → two very different real jobs); the missing-comparison idea
(one snapshot can't show a trend — add a before/after or A/B); the small-early-sample fake-trend
chart. Onda code-block for the coding-scheme criteria if a beat wants it.

## Standing rules — enforce (violated earlier today)
- Audio-first / fit-to-beat: the COMPILER conforms every clip to its beat (slow-to-fit). NEVER
  hand-time, pre-cut, or pre-bake a clip to beat length. No content beat ships as a slate in the
  FINAL cut (slates are fine in the previz — that's the point of the previz).
- 14pt legibility floor (Standing Rule #5): no on-screen text below 14pt; if it won't fit, use a
  symbol. Applies to the trend/base-rate charts' axes and labels especially.
- Render Remotion ONLY via runtime/scripts/remotion_scenes.py <reel> (foreground); match props to
  each component's zod schema; verify by LOOKING at frames + qc-sheet.
- Log my feedback to BUILD-LOG.md first. Unlisted only — human flips public.
