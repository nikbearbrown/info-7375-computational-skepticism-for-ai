# Professor Bear's feedback — Neha's Computational Skepticism final project
_Source for a deep-explainer reel. FIRST NAME ONLY: "Neha." The reel is Bear's feedback
on the project idea below._

## The student's proposal (Neha)
Title: "Implementation of FlashAttention Forward and Backward in Triton from Scratch."
Implement the FlashAttention forward and backward passes from first principles in Triton
(not an existing library) to build hands-on GPU programming, memory-efficient computation,
and kernel-optimization skill — a portfolio piece for AI-infrastructure / LLM-inference-
engineering roles.

## The core problem (how to review it)
This is a systems/kernel-engineering project, not a data-and-causal-claims project. The
course's skeptical instruments (robustness testing, honest visualization, source grading)
still apply — but they map onto a DIFFERENT failure surface: **numerical correctness of a
hand-rolled kernel** and **honest performance benchmarking**, not causal inference or data
grading. The risk isn't ambition — implementing FlashAttention fwd+bwd in Triton is a
legitimately hard, well-scoped task with a clear ground truth (naive attention, official
kernels). The risk is that "it works" and "it's fast" get ASSERTED without the rigor the
course demands elsewhere: a kernel that passes a spot-check on one shape isn't verified; a
benchmark that beats naive attention 5× isn't automatically meaningful. Push Neha to treat
her own kernel's correctness and performance claims with the same skepticism she'd apply to
a dataset or a causal model.

## Part 1 — numerical correctness is NOT a single pass/fail check
- **Forward:** compare the Triton kernel to naive PyTorch attention (`softmax(QK^T/√d)@V`,
  full FP32) across MULTIPLE shapes; report max absolute AND relative error, not "outputs match."
- **Backward (the harder half):** use `torch.autograd.gradcheck` (analytical vs numerical
  finite-difference gradients) — NOT Triton-backward vs a reference backward, since both could
  share the same bug.
- **Precision boundaries:** online softmax + tiling accumulate floating-point error differently
  than a single full softmax even when both are "correct." Report tolerance thresholds explicitly
  (e.g. "matches naive to 1e-3 in FP16, 1e-5 in FP32"), not a binary correct/incorrect.
- **Causal-masking edge cases:** verify sequence boundaries (first token attends only to itself)
  and that masked positions don't leak through the online-softmax accumulation — a classic place
  for off-by-one bugs to hide silently (output "looks reasonable" but is subtly wrong).
Feedback angle: require a correctness section with gradcheck results, per-dtype error tolerances,
and at least one deliberately adversarial test (e.g. a sequence length that doesn't divide evenly
into the tile size) — not a demo that outputs "look right" on a standard shape.

## Part 2 — honest benchmarking against the RIGHT baselines
- **Weak-baseline trap:** beating naive unfused attention is easy and uninformative (O(n²),
  never competitive). The meaningful comparison is `torch.nn.functional.scaled_dot_product_attention`
  (fused FlashAttention backend) and ideally the official FlashAttention-2/3 kernels. If Neha's
  kernel is slower than these, that's a legitimate, expected finding for an educational from-scratch
  build — but the write-up must SAY SO, not omit the comparison.
- **GPU timing errors:** missing `torch.cuda.synchronize()` around timed regions; no warm-up
  (first-call compile/autotune counted as steady-state); a single run instead of mean ± variance.
  The three most common ways GPU benchmarks quietly lie.
- **Cherry-picked shape sweeps:** reporting speedup only at the config where the kernel looks best.
  Honest version reports a grid (seq len × batch × head dim) showing where it wins, loses, and ties.
- **Memory claims need the same rigor:** FlashAttention's selling point is O(n) not O(n²) memory.
  Report actual peak memory (`torch.cuda.max_memory_allocated()`) across increasing sequence
  lengths — the empirical curve, not a theoretical complexity argument.
Feedback angle: require a benchmarking-methodology section (baselines, shapes, #runs, warm-up,
sync) WRITTEN AND REVIEWED before results are generated — not reverse-engineered to justify
results already obtained.

## Part 3 — robustness testing (translated to a kernel)
1. **Non-power-of-2 / boundary sequence lengths** — test 1, tile_size−1, tile_size+1, a large
   prime-ish length (tile kernels bug at lengths that don't divide the tile).
2. **Extreme head dimensions** — very small (16) and larger (128, 256) expose different
   register-pressure / shared-memory tradeoffs; check correctness AND performance across the range.
3. **Numerical edge cases** — all-zero inputs, very large logits (stresses softmax stability — the
   exact thing the online-softmax max-subtraction exists to handle, so test it's implemented right),
   mixed precision.
4. **Masking under padding** — if variable-length + padding masks are in scope, test that padded
   positions genuinely don't influence outputs (mask applied to scores but not excluded from the
   running normalizer = close-but-quietly-wrong).
Feedback angle: ask for a small explicit table — shape × dtype × edge-case-flag → pass/fail — not
prose that "the kernel was tested extensively."

## Part 4 — honest visualization for performance claims
- Show variance, not just means (error bars / std across repeated runs).
- Label axes and scales clearly, especially log scales (an unlabeled log axis makes a modest gain
  look dramatic).
- Show the FULL shape sweep, including where the kernel underperforms.
- Distinguish "correct and slower" from "correct and faster than baseline" explicitly — for an
  educational from-scratch kernel, correct-and-somewhat-slower is respectable and expected, and
  shouldn't be visually dressed up as a speedup.

## Close: open questions (not prescriptions)
End with one or two questions for Neha to resolve herself — e.g. whether to scope the backward
pass to non-causal attention given time constraints, or how to handle mixed-precision accumulation.
Tone: encouraging but exacting — a strong, well-scoped systems project with a clear ground truth,
and the throughline is applying the course's skepticism to her OWN kernel's claims.

## Reference lineage
Dao et al., FlashAttention (2022) + FlashAttention-2 (2023) — the algorithm being reimplemented;
OpenAI Triton docs/tutorials (incl. the official Triton FlashAttention tutorial) — compare
architecture against, don't copy; `torch.autograd.gradcheck` docs — the backward-verification
tool (cite its tolerance params); PyTorch `scaled_dot_product_attention` backend docs — the fair
production baseline; the course's skeptical-instruments framework — same robustness/honest-viz
lens as the other finals, translated from data/causal claims to numerical-correctness and
performance claims (name it so Neha sees the throughline, not a different rubric).
