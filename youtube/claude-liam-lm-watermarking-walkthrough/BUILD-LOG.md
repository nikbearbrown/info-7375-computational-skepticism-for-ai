# BUILD-LOG — claude-liam-lm-watermarking-walkthrough

## Session 1 — Beat sheet authoring (STEP 1–3)

### Beat sheet written
`beat_sheet.json` authored: 42 beats, B00–B41. Structure matches PLAN.md act map exactly.
All data sourced from `REPO-VERIFY.md` and the local clone at `books/lm-watermarking/`.

### Code slice range adjustments (overflow constraint)

GitHubCodeViewer renders lines in a 1600px panel at 26px monospace. Maximum safe line length
is approximately 95 characters. Lines beyond that clip at the right edge.

**Slice A — original intent L54–80, adjusted to L62–80**

- L61: `assert input_ids.shape[-1] >= 1, f"seeding_scheme={seeding_scheme} requires at least a 1 token prefix sequence to seed rng"` — 135 characters. Egregious overflow; would hide most of the error message in a visually confusing way. Starting the slice at L62 begins cleanly at `prev_token = input_ids[-1].item()`, which is the mechanistically relevant line.
- L74: `vocab_permutation = torch.randperm(self.vocab_size, device=input_ids.device, generator=self.rng)` — 104 characters. Clips ~9 chars. Essential (this is the per-position shuffle). Logged; not removable.
- L78: `greenlist_ids = vocab_permutation[(self.vocab_size - greenlist_size) :]  # legacy behavior` — 102 characters. Clips ~7 chars. Essential (legacy-path contrast). Logged; not removable.

Decision: shorten the range; never re-indent, re-wrap, or elide code to make it fit. L74 and L78 clip slightly at the right edge and that is acceptable — the key content is on the left side.

**Slice B — original intent L94–117, adjusted to L95–117**

- L94: `    def _bias_greenlist_logits(self, scores: torch.Tensor, greenlist_mask: torch.Tensor, greenlist_bias: float) -> torch.Tensor:` — 128 characters. Overflows the panel substantially. Starting the slice at L95 begins at `scores[greenlist_mask] = scores[greenlist_mask] + greenlist_bias`, which is THE line the reel is named after.
- L98: `        batched_greenlist_ids = list(map(self._get_greenlist_ids, input_ids_shifted))` — 88 characters (fits). OK.
- L113: `            green_tokens_mask = self._calc_greenlist_mask(scores=scores, greenlist_token_ids=batched_greenlist_ids)` — 114 characters. Clips ~19 chars. Essential (connects mask to main loop). Logged; not removable.
- L115: `            scores = self._bias_greenlist_logits(scores=scores, greenlist_mask=green_tokens_mask, greenlist_bias=self.delta)` — 125 characters. Clips ~30 chars. The call site of the one-line watermark; the `greenlist_bias=self.delta` argument that ties it to δ=2.0 may clip. Logged; not removable.

Decision: start slice at L95; accept L113/L115 edge clipping as tolerable for essential content.

**Slice C — L153–164 — no adjustments needed**

All lines under 90 characters. No clipping expected.

---

### Three-copy verification
Three divergent copies of `watermark_processor.py` confirmed:
- Root: 282 LOC
- `hf_hub_space_demo/`: 280 LOC, 32 diff lines vs root
- `watermark_reliability_release/`: 672 LOC, 592 diff lines vs root
B15 FormACard uses "three divergent copies" — VERIFIED.

### Commit bbe1fb8 verification
`git show bbe1fb8 --stat`: watermark_processor.py 32 ++++++++++++++--------------
`git diff --numstat`: 17 insertions / 15 deletions. Message "Documentation Updates."
`ignore_repeated_bigrams: bool = False` → `True` confirmed in diff output.
B36 GitHubCodeDiff props use `badge="+17 −15"`. VERIFIED.

---

## Session 1 — STEP 4: Factcheck (complete)

`FACTCHECK.md` written. 0 failures, 0 fabrications.
All mechanism claims trace to `watermark_processor.py` line numbers.
Paper attribution traces to `README.md:7`.

---

## Open items

- `scenes.py` — 4 Manim classes (`B09_LocHotspot`, `B23_VocabPartition`, `B27_LogitBars`, `B31_BinomialNull`) not yet written. Blocking art run for B09, B23, B27, B31 beats.
- STEP 5 (GATE T — type_check.py) — pending.
- STEP 6 (GATE P — art run slate previz) — pending. Spend nothing on audio.
- Do not stage to TOPOST. Do not run art post. Do not upload.
