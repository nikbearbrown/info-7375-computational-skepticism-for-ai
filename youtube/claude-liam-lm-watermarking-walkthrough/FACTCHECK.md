# FACTCHECK — claude-liam-lm-watermarking-walkthrough
## "The Watermark Is One Line of Code"

**Repo under audit:** `jwkirchenbauer/lm-watermarking`, HEAD `8292251`
**Local clone:** `books/lm-watermarking/` (all line numbers verified against HEAD)
**Status:** FACTCHECK COMPLETE — 0 failures, 0 fabrications. Signed: Claude, 2026-08-12.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Cold open ask references "reference implementation for this whole family of techniques" | PASS | Positions the repo as a family representative, not a specific identification of Anthropic's algorithm. KGW prohibition preserved. | — |
| 2 | B03 | Repo: `jwkirchenbauer/lm-watermarking`, HEAD `8292251` | PASS | `git rev-parse HEAD` in `books/lm-watermarking/` returns `8292251...`. | — |
| 3 | B03 | Paper: Kirchenbauer et al., ICML 2023, arXiv:2301.10226 | PASS | README.md L7 links `https://arxiv.org/abs/2301.10226` with full author list; README.md L52 says "our ICML 2023 conference paper." | — |
| 4 | B06 | Root: 2,317 lines of code across 7 Python files | PASS | `wc -l *.py` in repo root = 2,317. Files: watermark_processor.py (282), extended_watermark_processor.py (625), levenshtein.py (468), demo_watermark.py (253), alternative_prf_schemes.py (239), normalizers.py (235), compute_sensitivity.py (215). | — |
| 5 | B07 | Subdirs: 344,390 "lines of file" — watermark_reliability_release (252,512) + hf_hub_space_demo (44,191) + homoglyph_data (42,351) + experiments (5,336) | PASS | `find <subdir> -type f \| xargs wc -l` verified each total. Labeled "lines of file, not code" per PLAN.md prohibition (c). | — |
| 6 | B09 | watermark_processor.py is 282 lines = 12% of root (2,317) | PASS | `wc -l watermark_processor.py` = 282. 282/2317 = 12.2%. | — |
| 7 | B12 | watermark_processor.py has 4 importers in the repo | PASS | `grep -r "import watermark_processor\|from watermark_processor" *.py` returns 4 files: demo_watermark.py, homoglyph_detection.py, compute_sensitivity.py, extended_watermark_processor.py. | — |
| 8 | B14 | extended_watermark_processor.py: 625 lines, README calls it "recommended," 0 Python files import it | PASS | `wc -l` = 625. README L30: "more full featured implementation (recommended)." `grep -r "import extended_watermark_processor\|from extended_watermark_processor" *.py` = empty. README code blocks (L78, L105) are markdown documentation; alternative_prf_schemes.py L4 is a docstring reference only. | — |
| 9 | B15 | Three divergent copies of watermark_processor.py in the repo | PASS | Root (282 LOC), hf_hub_space_demo/ (280 LOC, 32 diff lines vs root), watermark_reliability_release/ (672 LOC, 592 diff lines vs root). Confirmed via `diff`. | — |
| 10 | B17 | 16 commits; 2023: 12, 2024: 2, 2025: 2 | PASS | `git rev-list --count HEAD` = 16. `git log --format="%ad" --date=format:"%Y"` yields 12/2/2. No year is empty — no frozen:true on churn bars. | — |
| 11 | B20 | Default params: gamma=0.5, delta=2.0, seeding_scheme="simple_1", hash_key=15485863 | PASS | watermark_processor.py L37–L40 (WatermarkBase.__init__): `gamma: float = 0.5`, `delta: float = 2.0`, `seeding_scheme: str = "simple_1"`, `hash_key: int = 15485863,  # just a large prime number`. | — |
| 12 | B20 | z_threshold=4.0 (WatermarkDetector default) | PASS | watermark_processor.py L125: `z_threshold: float = 4.0,` | — |
| 13 | B23 | Green list regenerated per token from `hash_key × prev_token`; gamma=0.5 partition of vocabulary | PASS | L37: `gamma=0.5`. L62: `prev_token = input_ids[-1].item()`. L63: `self.rng.manual_seed(self.hash_key * prev_token)`. L73: `greenlist_size = int(self.vocab_size * self.gamma)`. L74: `vocab_permutation = torch.randperm(...)`. No `self.greenlist` field — not stored. | — |
| 14 | B25 | "The green list is not stored anywhere. Regenerated from secret key × previous token. Delete the key and it is unrecoverable." | PASS | L68–80: `_get_greenlist_ids` is a local function returning `list[int]`; no persistent assignment. The RNG is seeded at L63 from `hash_key * prev_token` — without `hash_key`, the seed cannot be reproduced. | — |
| 15 | B29 | `scores[greenlist_mask] = scores[greenlist_mask] + greenlist_bias` — one line, add 2.0 to half the logits | PASS | watermark_processor.py L95 (verbatim). `greenlist_bias` resolves to `self.delta = 2.0` via L115: `greenlist_bias=self.delta`. | — |
| 16 | B32 | Detection is `scipy.stats.norm.sf(z)` — returns a p-value, not a verdict | PASS | L21: `import scipy.stats`. L162: `p_value = scipy.stats.norm.sf(z)`. L278: `output_dict["prediction"] = score_dict["z_score"] > z_threshold` — the verdict is a threshold comparison, not the p-value itself. | — |
| 17 | B35 | Commit bbe1fb8: author Jonas Geiping, date 2023-08-10, message "Documentation Updates" | PASS | `git show bbe1fb8` confirms author, date, and message verbatim. | — |
| 18 | B37 | "+17 −15 on watermark_processor.py; one line flipped ignore_repeated_bigrams: bool = False → True" | PASS | `git diff --numstat bbe1fb8^ bbe1fb8 -- watermark_processor.py` = 17 insertions / 15 deletions. `git show bbe1fb8 -- watermark_processor.py` shows `-        ignore_repeated_bigrams: bool = False,` / `+        ignore_repeated_bigrams: bool = True,`. | — |
| 19 | B39 | Verdict: "This repo is the reference implementation for one family of watermarks. Anthropic's algorithm, if they have one, isn't published." | PASS | KGW prohibition satisfied. No beat states or implies Claude's watermark is this code. | — |
