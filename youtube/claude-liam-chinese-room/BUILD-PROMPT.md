# BUILD-PROMPT — claude-liam-chinese-room

Paste-ready end-to-end build prompt for the deep-explainer pipeline.

## What this is
A ~5.9-min **deep-explainer** episode, "The Chinese Room," for the
**computational-skepticism-for-ai** book. Claude bookends + documentary vox
body. Channel **claude-liam** (Liam in for Bear, Kokoro `am_onyx`, free).
Plan + factcheck are DONE and approved; `beat_sheet.json` is the heart.

## RENDERING RULE — 4K (base rule, non-negotiable)
EVERY beat is native 4K (3840×2160, 30fps). Author ALL compositions —
Remotion illustrations, Manim fragments, cards, bookends — at **1920×1080**
so `--scale=2` yields 3840×2160 natively. **No 1280×720 compositions. No
ffmpeg bicubic upscaling of any beat.** At VISUAL QC, `ffprobe` every beat and
reject any whose native stream is not 3840×2160 (a 1440p stream stretched into
a 4K container is a FAIL, not a pass).

## Build steps (local toolkit, in the book's youtube/ folder)
1. Place this folder at
   `books/computational-skepticism-for-ai/youtube/claude-liam-chinese-room/`.
2. **Audio (GATE P → lock):** generate Kokoro `am_onyx` mp3s for all 33 beats
   into `mp3/`; measure durations; run align for the word clock. Measured
   audio is the only clock.
3. **Gate D2 — `SHOPPING.md`:** after audio lock, write the tier-tagged,
   duration-locked shopping list for the 6 pantry stills (A2, A3, A7, A8,
   A25, A28). Do NOT write it before durations are real.
4. **Gate D1 — slate previz:** `./art run claude-liam-chinese-room` — vox
   slots render as slates, Manim/Remotion render for real, `--review` burn-in.
   Watch it for pacing.
5. **Pantry fill:** drop the 6 stills into `pantry/` (`<BID>.png`), run the
   `pantry` intake (treats + renames to `media/`), set `shot.focus`, fill
   `.source.txt` sidecars (archival) / disclosure sidecars (AI). Rerun — only
   changed slots recompile.
6. **Review cut → VISUAL QC LAW pass → `./art final`.** Closing block is the
   your-turn standard (verdict → your-turn → title outro).

## CONTENT RULES (hard — a review cut violated these; do not repeat)
- **No text slides.** No beat may put a sentence of narration on screen as a
  caption card. Concept beats are **DOODLE** (rough.js sketch, via the `doodle`
  skill) or **VOX** (pantry still). Narration is voiceover only.
- **Remotion = Claude UI bookends ONLY** (B00, C1, C2, C3). Never a body beat.
- **Manim only for real data/math** (A16, A20, A29) and **every Manim scene
  must be authored** in `scenes.py`. Never ship the toolkit default scene or
  any placeholder text ("Claude Code Manim", default slate titles). An
  unauthored Manim beat FAILS QC — it does not ship as a stub.
- **QC scan:** grep every rendered beat for placeholder/template text; any hit
  is a FAIL.

## Lane mix (body) after re-plan
- CARD 5 (act titles) · VOX 6 · MANIM 3 (data only) · DOODLE 15 (concepts).
  Intentionally deviates from the default deep-explainer Remotion mix per Bear's
  no-text-slide rule.
- Vox runs only: R1 (A2→A3), R2 (A7→A8), ≤3 beats, never crossing an act.
- 20 body beats changed lane from the first cut (9 Remotion + 6 Manim cards →
  doodle). Re-render the doodle beats + author the 3 real Manim scenes; bookends
  and vox stills are unchanged.
- No model/vendor names; no "as of" dates (DOUBLE-CHECK LAW).
- A12 / A26 are labeled paraphrase — no fabricated quotes from Searle/Turing.
- Bear's contested claims (Searle "predicted" LLMs; LLMs "passed" Turing) are
  voiced explicitly as his claim, not as fact.
- Bookends per ai-explainer laws; closing per your-turn skill; never publish
  (public is a human Studio flip).

## Pantry shopping (detail in SHOPPING.md after audio lock)
| BID | Asset | Tier | Notes |
|---|---|---|---|
| A2 | Alan Turing portrait | 3 | archival photo; rights check to human |
| A3 | teletype / paper-tape terminal | 1 | generic; stock or AI |
| A7 | John Searle portrait | 3 | archival photo; rights check to human |
| A8 | "Minds, Brains, and Programs" (1980) | 2 | object; verify item rights |
| A25 | person at a terminal | 1 | generic; AI ok + disclosure |
| A28 | vast compute / scale | 1 | generic; AI ok + disclosure |
