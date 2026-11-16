# PLAN — claude-liam-lm-watermarking-walkthrough

**Title:** The Watermark Is One Line of Code
**Skill:** `git-explainer` (descends from `code-walkthrough`; Claude bookends from `ai-explainer`)
**Channel:** `claude-liam` — Liam in for Bear, Kokoro `am_onyx`, free
**Reel:** `computational-skepticism-for-ai/youtube/claude-liam-lm-watermarking-walkthrough/`
**Repo:** `jwkirchenbauer/lm-watermarking` @ `main` / `8292251`
**Register:** Teardown — describe the mechanism → judge it → name the constraint
**Estimated runtime:** 6:45–7:30 · ~42 beats

**Owning book:** `computational-skepticism-for-ai`. Not asked, decided — the film's spine is *detection is a z-test against a binomial null, and it returns a p-value, not a verdict*, which is chapter 02 (probability, uncertainty and the confidence illusion) almost verbatim. Override if you want it in `irreducibly-human-book` next to the context-engineering reel.

---

## Sourcing

**Rung 1 throughout.** Every scene renders from `REPO-VERIFY.md` data through the GitHub skin, plus Manim for the four quantitative beats. **No vox beats, no pantry, no gen-AI, no doodle, no bare slates.** Expected shopping list: empty. Expected rights escalations: zero.

## The walk (order is fixed — each step earns the next)

| Act | Beats | Scene | Question answered |
|---|---|---|---|
| — | B00 | `ClaudeComposerAsk` | cold open, ask lands answered |
| **I — What** | B01–B05 | `GitHubRepoHero` + Manim | What is this repo, and why is "watermark" the wrong word? |
| **II — Shape** | B06–B10 | `GitHubStructureMap` | Where does the code concentrate? |
| **III — Path** | B11–B16 | `GitHubCallChain` | What routes through what — and what routes through nothing? |
| **IV — History** | B17–B20 | `GitHubChurn` | 16 commits, three years. What does that mean and not mean? |
| **V — Read** | B21–B33 | `GitHubCodeViewer` ×3 + Manim ×3 | **THE GATE.** The key, the one line, the z-test. |
| **VI — Change** | B34–B38 | `GitHubCodeDiff` | A commit that said "Documentation Updates" and wasn't. |
| — | B39–B41 | verdict / your turn / outro | |

## The narration spine — the lines that carry the argument

These are locked. Everything between them is authored from `REPO-VERIFY.md`.

- **B00 ask:** *"Anthropic says Claude's text carries a watermark. I cloned the reference implementation for this whole family of techniques. Can you walk me through what the mark actually is?"*
- **B02:** The word watermark comes from images, where there is a thing in the file you could point at. There is no such thing in the text. Nothing here is embedded.
- **B14** (the orphan): 625 lines, the README calls it "recommended," and not one file in this repository imports it.
- **B25** (Slice A lands): The green list is not stored anywhere. It's regenerated from scratch at every token, from the secret key times the previous token. Delete the key and it is unrecoverable.
- **B29** (Slice B lands): `scores[greenlist_mask] = scores[greenlist_mask] + greenlist_bias`. That is the watermark. One line. Add two to half the logits.
- **B32** (Slice C lands): Detection is `scipy.stats.norm.sf(z)`. It returns a p-value. A p-value is not a verdict, and asking to *see* the watermark is like asking to see the loadedness of a single die roll.
- **B37** (the diff): Seventeen lines added, fifteen removed, message "Documentation Updates." One of them flipped a detector default from False to True. The key line is where the error hides.

## Manim beats (the only non-skin visuals)

| Beat | Fragment | Data |
|---|---|---|
| B09 | LOC hotspot map | 2,317 root LOC vs 344,390 subdirectory lines — the ratio, labelled "lines of file" for the data dirs |
| B23 | Vocabulary partition | 50,257-cell grid, γ=0.5, reshuffling at each of ~6 token steps — shows the green list is per-position, not fixed |
| B27 | Logit bars + δ | candidate distribution, `+2.0` applied to green bars, resample; run once at high entropy (choice flips) and once at low entropy (choice holds — the "Barack → Obama" case) |
| B31 | Binomial null vs observed | γT expectation, observed green count, the z statistic, the p-value; then the same test on a 40-token passage where it has no power |

## What this reel must NOT say

`REPO-VERIFY.md` lists the deliberate exclusions. The load-bearing one: **this repo is KGW. Anthropic has not published its algorithm.** The reel explains what this family does and stops. Any sentence implying Claude's watermark is this code is fabrication, and in a film about detection standards it is the failure the film is criticising.

Second: no `frozen: true` on any churn bar, and no "abandoned" narration. 2024 and 2025 both have commits. Sixteen commits is an observation, not a verdict.

Third: for `homoglyph_data/`, `hf_hub_space_demo/` and `watermark_reliability_release/`, say **lines of file**, not lines of code. Those totals are mostly Unicode tables and experiment JSON.

## Gates

1. `REPO-VERIFY.md` — **done**, in the reel folder, all six scenes verified, zero scripting gaps.
2. Author `beat_sheet.json` mapping the six steps to the GitHub scenes with verified props.
3. Factcheck pass — the mechanism claims (γ, δ, hash_key, z_threshold, the seeding scheme) all trace to cited line numbers in `watermark_processor.py`; the paper attribution (Kirchenbauer et al., ICML 2023, arXiv:2301.10226) traces to README L1.
4. **GATE P** — full-length slate previz. Spend nothing on audio until it's signed.
5. Hand back. Never publish.
