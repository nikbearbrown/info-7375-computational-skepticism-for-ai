Build a deep-explainer reel in the LIAM persona. The FRAME: Liam prompts Claude — "What feedback would Professor Bear give to this student on their Computational Skepticism final project idea?" — and the body IS that feedback. Source: books/computational-skepticism-for-ai/youtube/flashattention-triton-source.md. Use the deep-explainer skill, Liam persona (claude-liam, Kokoro am_onyx, free). Never publish.

FIRST NAME ONLY: refer to the student as "Neha" throughout — never the full name.

Build INTO: books/computational-skepticism-for-ai/youtube/<slug>/ (suggest slug claude-liam-flashattention-triton).

## The bookend frame (deep-explainer Claude-composer cold open, Liam voice)
- Cold open: Liam types the ask into the Claude composer — "what feedback would Professor Bear give Neha on their Computational Skepticism final project?" Claude answers; that answer is the reel.
- Verdict recap + YOUR TURN handoff at the close, as the skill specifies.

## Run mode: UNATTENDED until the full-length SLATE PREVIZ cut, then STOP
Do NOT stop at the intermediate gates (plan, GATE P) — audio is free Kokoro, so run straight
through: plan → factcheck → narration → Kokoro audio → audio-lock → compile the full-length
SLATE PREVIZ. Then STOP and open that slate cut for me to view. That previz is the first thing
I watch. Don't fill pantry stills or spend on anything paid before I see the slate cut.

## The body arc (from the source — guidance, not a substitute for your plan)
- Hook: it's a KERNEL project, not a data/causal one — but the same skepticism applies to a
  different failure surface: numerical correctness of a hand-rolled kernel + honest benchmarking.
  The trap: "it works" and "it's fast" asserted without rigor.
- Part 1 — correctness is not one pass/fail: forward vs naive across shapes (max abs + rel error);
  backward via gradcheck (analytical vs numerical, NOT reference-vs-reference); precision boundaries
  (online softmax accumulates FP error differently — report tolerances per dtype); causal-mask
  edge cases (silent off-by-one leaks).
- Part 2 — honest benchmarking: weak-baseline trap (naive attention too easy; the real baselines
  are F.scaled_dot_product_attention + official FlashAttention); GPU timing errors (synchronize,
  warm-up, distribution not single run); cherry-picked shape sweeps; memory claims need the
  empirical O(n) vs O(n²) peak-memory curve.
- Part 3 — robustness = kernel edge/stress tests: non-power-of-2 lengths, extreme head dims,
  large-logit softmax stability, padding-mask correctness under the running normalizer.
- Part 4 — honest visualization: variance not means; labeled axes/scales; full sweep incl. losses;
  distinguish "correct + slower" from "faster than baseline."
- The generous truth: for an educational from-scratch kernel, correct-but-slower-than-production
  is a legitimate, expected result — don't dress it up.
- Close: open questions handed back to Neha (scope backward to non-causal? mixed-precision accumulation?).

Strong Manim/animation beats: the shape×dtype correctness grid; analytical-vs-numerical gradient
(gradcheck) idea; GPU warm-up vs steady-state timing; the O(n) vs O(n²) memory curve; the benchmark
sweep showing wins/losses/ties. Code beats (Onda code-block) for the gradcheck/verify skeleton if a
beat wants it.

## Standing rules — enforce (violated earlier today)
- Audio-first / fit-to-beat: the COMPILER conforms every clip to its beat (slow-to-fit). NEVER
  hand-time, pre-cut, or pre-bake a clip to beat length. No content beat ships as a slate in the
  FINAL cut (slates are fine in the previz — that's the point of the previz).
- 14pt legibility floor (Standing Rule #5): no on-screen text below 14pt; if it won't fit, use a
  symbol. Applies to the benchmark/memory charts' axes and labels especially.
- Render Remotion ONLY via runtime/scripts/remotion_scenes.py <reel> (foreground); match props to
  each component's zod schema; verify by LOOKING at frames + qc-sheet.
- Log my feedback to BUILD-LOG.md first. Unlisted only — human flips public.
