Build a deep-explainer reel in the LIAM persona. The FRAME: Liam prompts Claude — "What feedback would Professor Bear give to this student on their Computational Skepticism final project idea?" — and the body IS that feedback. Source: books/computational-skepticism-for-ai/youtube/wage-adjustment-layer-source.md. Use the deep-explainer skill, Liam persona (claude-liam, Kokoro am_onyx, free). Never publish.

FIRST NAME ONLY: refer to the student as "Atharva" throughout — never the full name.

Build INTO: books/computational-skepticism-for-ai/youtube/<slug>/ (suggest slug claude-liam-wage-adjustment-layer).

## The bookend frame (deep-explainer Claude-composer cold open, Liam voice)
- Cold open: Liam types the ask into the Claude composer — "what feedback would Professor Bear give Atharva on their Computational Skepticism final project?" Claude answers; that answer is the reel.
- Verdict recap + YOUR TURN handoff at the close, as the skill specifies.

## Run mode: UNATTENDED until the full-length SLATE PREVIZ cut, then STOP
Do NOT stop at the intermediate gates (plan, GATE P) — audio is free Kokoro, so run straight
through: plan → factcheck → narration → Kokoro audio → audio-lock → compile the full-length
SLATE PREVIZ. Then STOP and open that slate cut for me to view. That previz is the first thing
I watch. Don't fill pantry stills or spend on anything paid before I see the slate cut.

## The body arc (from the source — guidance, not a substitute for your plan)
- Hook: this is the most methodologically self-aware proposal of the term — Atharva already built in
  break-testing, an honest-failure requirement, and a scope disclaimer. So the feedback isn't "add
  skepticism" — it's pointing at the TWO places the proposal's own "every number traces to a real
  record" rule could be quietly violated without the tool ever technically lying.
- Part 1 — BLS + BEA measure DIFFERENT things: BLS OEWS = nominal metro wages; BEA's relevant product
  is Regional Price Parities (RPP), not occupation wages. Nominal wage vs cost-of-living-adjusted
  "real" wage (nominal ÷ local RPP) are materially different CONCEPTS that can rank metros differently.
  State explicitly in the card which one the tool outputs — or show both, labeled. Extend "honest
  missing" to the RPP step: if RPP is missing, null the adjusted field — don't relabel nominal as adjusted.
- Part 2 (the sharper issue) — the O*NET crosswalk risks being dominated by GENERIC skills: "Critical
  Thinking," "Complex Problem Solving," etc. sit on nearly every professional occupation. Full-vector
  overlap inflates because of near-universal categories, not anything specifically transferable about
  ERP. Split the vector into TIERS — generic professional vs role-specific technical/knowledge
  (Programming, Mathematics, Database) — and report overlap SEPARATELY per tier. Flag O*NET's update
  lag for newer SOC codes (Data Scientist, ML Engineer) as a stated limitation.
- Part 3 — stratify the coverage metric, don't just aggregate: an 80% aggregate can hide that sparsity
  concentrates in the small/mid-size metros where the ERP workforce actually lives. Report coverage
  STRATIFIED by metro-size tier, not one blended number.
- Part 4 — data VINTAGE, not just presence: BLS OEWS lags ~6–12 months; a number can be real, present,
  and stale without ever triggering "missing." Each figure should carry its own visible "as of" date;
  silently mixing vintages across a single metro comparison is another way honest numbers mislead.
- Part 5 — what's already strong (preserve, don't re-litigate): the deliberate break-testing and the
  explicit scope disclaimer are exactly right — just EXTEND the break-testing instinct to Parts 1 and 4
  (test RPP-missing-but-wage-present; test data-exists-but-several-releases-old).
- Close: hand back one or two open questions to Atharva — how to define metro-size strata; whether to
  surface both nominal and adjusted wages by default or via a toggle.

Strong Manim/animation beats: the nominal-vs-RPP-adjusted split (same $120K reading differently in a
high-RPP vs low-RPP metro); the generic-vs-specific O*NET tier split (a "92% overlap" bar decomposing
into a tall generic slab + a short technical sliver); the stratified-coverage idea (one 80% aggregate
bar splitting into strong-hub / weak-mid-metro bars); the vintage timeline (two figures on one
comparison carrying different "as of" dates). Onda code-block for the adjusted_wage() skeleton if a beat wants it.

## Standing rules — enforce (violated earlier today)
- Audio-first / fit-to-beat: the COMPILER conforms every clip to its beat (slow-to-fit). NEVER
  hand-time, pre-cut, or pre-bake a clip to beat length. No content beat ships as a slate in the
  FINAL cut (slates are fine in the previz — that's the point of the previz).
- 14pt legibility floor (Standing Rule #5): no on-screen text below 14pt; if it won't fit, use a
  symbol. Applies to the coverage/overlap/vintage charts' axes and labels especially.
- Render Remotion ONLY via runtime/scripts/remotion_scenes.py <reel> (foreground); match props to
  each component's zod schema; verify by LOOKING at frames + qc-sheet.
- Log my feedback to BUILD-LOG.md first. Unlisted only — human flips public.
