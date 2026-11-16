# REPO-VERIFY — claude-liam-lm-watermarking-walkthrough

Repo: `jwkirchenbauer/lm-watermarking` · branch `main` · HEAD `8292251` (2025-09-17, John Kirchenbauer, "update hf space demo")
Local clone: `/Users/bear/Documents/CoWork/bear-textbooks/books/lm-watermarking`
Verified: 2026-08-12

Every GitHub scene below is Rung 1 — computed from the repo, no hand-authored counts. Each row gives the command that produced the data and the assertion the scene's props must satisfy.

---

## Scene 1 — `GitHubRepoHero`

```
git remote -v ; git log -1 --format='%H %ad %an %s' ; git rev-list --count HEAD ; sed -n '1,24p' README.md
```

| Prop | Value |
|---|---|
| `owner/repo` | `jwkirchenbauer/lm-watermarking` |
| headline | Official implementation of *A Watermark for Large Language Models* (arXiv:2301.10226) |
| tagline | Built on the HuggingFace `transformers` **LogitsProcessor** abstraction |
| commits | 16 |
| HEAD | `8292251` · 2025-09-17 · "update hf space demo" |

**Assertion:** `git rev-list --count HEAD` == 16. Tagline is a paraphrase of README line 24 ("Implementation is based on the 'logit processor' abstraction provided by the huggingface/transformers library") — flagged as paraphrase, not quoted as code.

---

## Scene 2 — `GitHubStructureMap`

```
wc -l *.py | sort -rn
for d in experiments hf_hub_space_demo watermark_reliability_release homoglyph_data; do
  git ls-files "$d" | tr '\n' '\0' | xargs -0 wc -l | tail -1
done
```

Root modules — the mechanism:

| File | LOC | `hi` |
|---|---|---|
| `demo_watermark.py` | 701 | |
| `extended_watermark_processor.py` | 625 | |
| `watermark_processor.py` | **282** | **hotspot** |
| `homoglyphs.py` | 265 | |
| `normalizers.py` | 208 | |
| `alternative_prf_schemes.py` | 184 | |
| `app.py` | 52 | |
| **total** | **2,317** | |

Subdirectories — the evidence:

| Dir | Tracked files | LOC |
|---|---|---|
| `watermark_reliability_release/` | 210 | 252,512 |
| `hf_hub_space_demo/` | 13 | 44,191 |
| `homoglyph_data/` | 4 | 42,351 |
| `experiments/` | 9 | 5,336 |

**Assertion:** root `.py` LOC sum == 2,317 per `wc -l`.
**Honesty note for the beat:** the subdirectory LOC figures count **data files, not source** — `homoglyph_data/` is four Unicode lookup tables, and much of `hf_hub_space_demo/` and `watermark_reliability_release/` is JSON/experiment output. The narration must say "lines of file," not "lines of code," for those four rows, or the scene overstates the engineering mass. The honest framing is the ratio: the idea is 282 lines; everything around it is apparatus.

---

## Scene 3 — `GitHubCallChain`

```
for f in *.py; do grep -nE "^(from|import) +(watermark_processor|extended_watermark_processor|normalizers|homoglyphs|alternative_prf_schemes|demo_watermark)" "$f"; done
for m in watermark_processor extended_watermark_processor normalizers homoglyphs alternative_prf_schemes; do git grep -lE "(from|import) +$m\b" -- '*.py'; done
```

Real edges:

```
app.py ──► demo_watermark.py ──► watermark_processor.py ──► normalizers.py ──► homoglyphs.py
extended_watermark_processor.py ──► normalizers.py
extended_watermark_processor.py ──► alternative_prf_schemes.py
```

Imported-by counts, repo-wide:

| Module | Imported by | Files |
|---|---|---|
| `watermark_processor` | **4** | `demo_watermark.py`, `hf_hub_space_demo/demo_watermark.py`, `watermark_reliability_release/generation_pipeline.py`, `watermark_reliability_release/utils/evaluation.py` |
| `normalizers` | 4 | `extended_watermark_processor.py`, `watermark_processor.py`, `hf_hub_space_demo/watermark_processor.py`, `watermark_reliability_release/watermark_processor.py` |
| `homoglyphs` | 3 | the three `normalizers.py` copies |
| `alternative_prf_schemes` | 2 | `extended_watermark_processor.py`, `watermark_reliability_release/watermark_processor.py` |
| `extended_watermark_processor` | **0** | — |

**Load-bearing file: `watermark_processor.py`** — 282 LOC, four importers, the only path from the demo to the mechanism.

**The caption, and it is the reel's best beat:** `extended_watermark_processor.py` is 625 LOC, the README explicitly calls it "Extended implementation (recommended)" in the 9/23/23 update, and **nothing in the repository imports it**. The recommended implementation is an orphan. `git log` shows it was touched by exactly one commit, ever.

**Second verified finding:** there are three divergent copies of `watermark_processor.py` in the tree.

```
diff watermark_processor.py hf_hub_space_demo/watermark_processor.py          # 32 differing lines, 280 LOC
diff watermark_processor.py watermark_reliability_release/watermark_processor.py  # 592 differing lines, 672 LOC
```

**Assertion:** every edge above is a literal `from X import` / `import X` line present in the named file. No inferred or "conceptual" edges.

---

## Scene 4 — `GitHubChurn`

```
git log --date=format:'%Y' --pretty=%ad | sort | uniq -c
```

| Year | Commits | Flag |
|---|---|---|
| 2023 | 12 | **peak** |
| 2024 | 2 | |
| 2025 | 2 | |

**Assertion:** counts sum to 16 == `git rev-list --count HEAD`. **No `frozen: true` on any bar** — every year since first release has at least one commit, so the scene must not render a frozen year. Sixteen commits across three years for the reference implementation of a technique now being deployed at industry scale is the observation; "abandoned" is not supported by the data and must not be narrated.

---

## Scene 5 — `GitHubCodeViewer` — THE READ GATE

File: `watermark_processor.py` · branch `main` · lang `python`. Three byte-exact slices, in this order. Do not paraphrase, do not re-indent, do not elide.

**Slice A — L54–80: the key seeds an RNG, the RNG partitions the vocabulary**

```
git show main:watermark_processor.py | sed -n '54,80p'
```

Carries: `self.rng.manual_seed(self.hash_key * prev_token)` — the secret key times the previous token. Then `torch.randperm(self.vocab_size, ...)` and `vocab_permutation[:greenlist_size]`. The green list is a fresh random half of the vocabulary at every position, reproducible only by someone holding `hash_key`.

**Slice B — L94–117: the entire watermark is one line**

```
git show main:watermark_processor.py | sed -n '94,117p'
```

Carries: `scores[greenlist_mask] = scores[greenlist_mask] + greenlist_bias`. That is the mechanism. Everything else in the file is bookkeeping around that addition.

**Slice C — L153–164: detection is a hypothesis test**

```
git show main:watermark_processor.py | sed -n '153,164p'
```

Carries: `numer = observed_count - expected_count * T`, `denom = sqrt(T * expected_count * (1 - expected_count))`, and `scipy.stats.norm.sf(z)`. A z-test against a binomial null, returning a p-value.

Defaults to quote on screen, verified at `watermark_processor.py` L34–53 and L125:

| Param | Default | Meaning |
|---|---|---|
| `gamma` | `0.5` | half the vocabulary is green at each step |
| `delta` | `2.0` | logit boost added to green tokens |
| `hash_key` | `15485863` | the secret — "just a large prime" per the source comment |
| `seeding_scheme` | `"simple_1"` | hash on the single previous token |
| `z_threshold` | `4.0` | detector's decision boundary |

**Assertion:** each rendered line must be byte-identical to `git show main:watermark_processor.py` at the stated range.

---

## Scene 6 — `GitHubCodeDiff` — the payoff

```
git show bbe1fb8 -- watermark_processor.py
```

Commit `bbe1fb8` · Jonas Geiping · 2023-08-10 · message: **"Documentation Updates"** · badge **+17 −15**.

Most of the diff is genuine cosmetics — a blank line, PEP8 comment spacing, a removed empty line. Buried in it, at the `WatermarkDetector.__init__` signature:

```
-        ignore_repeated_bigrams: bool = False,
+        ignore_repeated_bigrams: bool = True,
```

That is not documentation. It changes the detector's default scoring rule — whether repeated bigrams get counted once or every time they occur — which changes `observed_count`, which changes the z-score, which changes the p-value. A commit labelled "Documentation Updates" silently flipped a default in the detection statistic.

**Assertion:** the rendered gutters and ± lines equal `git show bbe1fb8 -- watermark_processor.py` exactly. The `+17 −15` badge equals the commit's `--stat` for that path.

This is the scene that earns the READ gate: the key line is where the error hides, and here it hid inside a commit message that told you not to look.

---

## Scripting gaps — none

All six scenes have real data. Nothing was invented. No beat requires a pantry still; the shopping list is expected to be empty.

## Data that was deliberately NOT used

- `experiments/` and `watermark_reliability_release/` internals — 260k lines of experiment apparatus, out of scope for a mechanism walkthrough.
- Any claim about Anthropic's scheme. The repo is KGW. Anthropic has not published its algorithm; asserting that Claude's watermark is KGW-derived would be fabrication. The reel may say what this repo does and what the family shares, and must stop there.
