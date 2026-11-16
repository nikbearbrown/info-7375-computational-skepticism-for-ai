# BUILD-PROMPT — claude-liam-lm-watermarking-walkthrough

**Skill:** `git-explainer` (descends from `code-walkthrough`; Claude bookends from `ai-explainer`)
**Channel:** `claude-liam` — Liam in for Bear, Kokoro `am_onyx`, free
**Title:** The Watermark Is One Line of Code
**Reel folder:** `computational-skepticism-for-ai/youtube/claude-liam-lm-watermarking-walkthrough/`
**Book:** `computational-skepticism-for-ai`

---

## Prompt used to commission this build

```
Work in /Users/bear/Documents/CoWork/bear-textbooks/books.

Build the git-explainer reel at:
  computational-skepticism-for-ai/youtube/claude-liam-lm-watermarking-walkthrough/

Six steps:

STEP 1 — Author beat_sheet.json against runtime/schema/beat_sheet.schema.json.
Six GitHub skin scenes in fixed order (RepoHero, StructureMap, CallChain, Churn,
CodeViewer×3, CodeDiff). Four Manim beats. Data only from REPO-VERIFY.md.

STEP 2 — Assert CodeViewer slices are byte-identical to
  git show main:watermark_processor.py
output for those line ranges.

STEP 3 — Apply three prohibitions from REPO-VERIFY.md:
  (a) No claim that Anthropic's watermark is KGW.
  (b) No frozen:true on churn bars. No "abandoned" narration.
      2023/2024/2025 = 12/2/2; every year has commits.
  (c) For homoglyph_data/, hf_hub_space_demo/, watermark_reliability_release/:
      narration says "lines of file", not "lines of code".

STEP 4 — Factcheck pass. Every mechanism claim (gamma 0.5, delta 2.0,
hash_key 15485863, seeding_scheme simple_1, z_threshold 4.0) cites its line
number in watermark_processor.py. Paper attribution is Kirchenbauer et al.,
ICML 2023, arXiv:2301.10226, from README line 1. Write FACTCHECK.md. STOP.

STEP 5 — GATE T. Run scripts/type_check.py over every beat. Zero FAILs.
Write TYPECHECK.md.

STEP 6 — GATE P. Run art run for full-length slate previz. Spend nothing on
audio. Extract frames. STOP.

Constraints:
- Do not stage to TOPOST. Do not run art post. Do not upload.
- If any beat's data cannot be produced from the repo, write MISSING: in
  BUILD-LOG.md and stop that thread. No fabrication.
- HARD GLOBAL RULE: YouTube uploads come ONLY from books/youtube/TOPOST/.
```

---

## Key source documents

- `PLAN.md` — act map, locked narration lines, Manim specs, gates
- `REPO-VERIFY.md` — all six GitHub-scene props pre-verified from local clone
- `beat_sheet.schema.json` — the shared beat-sheet contract
- `brutalist-art/CLAUDE.md` → `AGENTS.md` — all production rules
- `CLAUDE.md` (books/) — HARD GLOBAL RULE + voice defaults

---

## Decisions made during build

1. **Slice A** started at L62 (not L54) — L61 assert line is 135 chars, overflows GitHubCodeViewer panel. See BUILD-LOG.md.
2. **Slice B** started at L95 (not L94) — L94 function definition is 128 chars, overflows. The first visible line is the named one-line watermark. See BUILD-LOG.md.
3. **Orphan visualization** (B13) — single-node GitHubCallChain with no arrows, one node highlighted. Zero-importer state represented as isolation, not absence.
4. **ASK→RESULT micro-beats** placed at B08 (before B09 Manim), B22 (before B23 Manim), B26 (before B27 Manim), B30 (before B31 Manim) — one ClaudeComposerAsk per Manim fragment, per ai-explainer law.
5. **B39 verdict narration** includes explicit KGW/Anthropic disclaimer: "This repo is the reference implementation for one family of watermarks. Anthropic's algorithm, if they have one, isn't published."
