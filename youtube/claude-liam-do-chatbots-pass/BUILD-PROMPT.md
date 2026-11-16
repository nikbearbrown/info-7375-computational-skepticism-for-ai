# BUILD-PROMPT — claude-liam-do-chatbots-pass

Paste-ready end-to-end build prompt for the deep-explainer pipeline.

## What this is
A ~6.1-min **deep-explainer** episode, "Do Chatbots Pass the Turing Test?", for the
**computational-skepticism-for-ai** book. Claude bookends + documentary body.
Channel **claude-liam** (Liam in for Bear, Kokoro `am_onyx`, free). Empirical/historical
companion to `claude-liam-chinese-room`. `beat_sheet.json` is the heart.
**Plan is at the PLAN gate — do not spend audio until Bear approves.**

## RENDERING RULE — 4K (base rule, non-negotiable)
EVERY beat is native 4K (3840×2160, 30fps). Author ALL compositions at **1920×1080**
so `--scale=2` yields 3840×2160 natively. **No 1280×720 comps. No ffmpeg bicubic
upscaling.** At VISUAL QC, `ffprobe` every beat and reject any whose native stream is
not 3840×2160.

## Build steps (local toolkit, in the book's youtube/ folder)
1. Folder lives at
   `books/computational-skepticism-for-ai/youtube/claude-liam-do-chatbots-pass/`.
2. **Gate F lock:** confirm `FACTCHECK.md` (all verified at plan time).
3. **Audio (GATE P → lock):** generate Kokoro `am_onyx` mp3s for all 33 beats into
   `mp3/`; measure durations; run align for the word clock. Measured audio is the only clock.
4. **Gate D2 — `SHOPPING.md`:** after audio lock, write the tier-tagged, duration-locked
   shopping list for the **7 pantry stills** (A2, A7, A9, A10, A16, A21, A29). Do NOT write
   it before durations are real.
5. **Gate D1 — slate previz:** `./art run claude-liam-do-chatbots-pass` — vox slots render
   as slates, Manim/Remotion render for real, `--review` burn-in. Watch it for pacing.
6. **Pantry fill:** drop the 7 stills into `pantry/` (`<BID>.png`), run `pantry` intake
   (treats + renames to `media/`), set `shot.focus`, fill `.source.txt` / disclosure sidecars.
   Rerun — only changed slots recompile.
7. **Review cut → VISUAL QC LAW pass → `./art final`.** Closing is the your-turn standard.

## CONTENT RULES (hard — house rules from the Chinese Room build)
- **No text slides.** No beat puts a sentence of narration on screen as a caption. Concept
  beats are **DOODLE** (rough.js, via the `doodle` skill) or **VOX** (pantry still). VO only.
- **Remotion = Claude UI bookends ONLY** (B00, C1, C2, C3). Never a body beat.
- **Manim only for real data** (A5, A11, A17, A26 — the fool-rate meter + the PARRY bar) and
  **every Manim scene must be authored** in `scenes.py`. No default scene, no placeholder text.
  An unauthored Manim beat FAILS QC — it does not ship as a stub.
- **QC scan:** grep every rendered beat for placeholder/template text; any hit is a FAIL.

## Lane mix (body, 29 beats)
- DOODLE 13 (concepts) · VOX 7 (stills) · MANIM 4 (data only) · CARD 5 (act titles).
  Follows this book's no-text-slide house pattern (same as claude-liam-chinese-room).
- Vox run only: **R1** (A9→A10, Weizenbaum→Colby), ≤3 beats, within Act II.
- **No current model/vendor names in narration** (DOUBLE-CHECK LAW). Historical years stay.
- Eugene Goostman "passed" is voiced as the **organizers' claim** and debunked (A18).
- The 73% result (A26) is a **specific study's finding**, model named only in FACTCHECK/SOURCES.
- Bear's skeptic claim (A28) is voiced explicitly as his view.
- Bookends per ai-explainer laws; closing per your-turn skill; **never publish** (public is a
  human Studio flip).

## The fool-rate meter (recurring MANIM)
Author one meter component reused across A5 / A17 / A26 (plus the standalone PARRY bar A11):
| Beat | Value | Reference | Point |
|---|---|---|---|
| A5 | — | dashed 30% "Turing line" + 5-min clock | establish the bar |
| A11 | 48% | dashed 50% "coin flip" line | psychiatrists ≈ chance on PARRY |
| A17 | 33% | 30% Turing line | Goostman *just* clears it (2014) |
| A26 | 73% | 30% line + ~50% "actual human" marker | passes, above the human |

## Pantry shopping (detail in SHOPPING.md after audio lock)
| BID | Asset | Tier | Notes |
|---|---|---|---|
| A2 | Alan Turing portrait | 3 | archival; rights check to human; reusable from chinese-room |
| A7 | 1960s mainframe / teletype | 1 | generic; stock or AI + disclosure |
| A9 | Joseph Weizenbaum portrait | 3 | archival; rights check to human |
| A10 | Kenneth Colby portrait | 3 | archival, scarce; AI fallback labeled |
| A16 | Goostman-era chat / boyish avatar | 1 | generic; NOT a copyrighted screenshot |
| A21 | modern fluent chat window | 1 | generic, unbranded; stock or AI + disclosure |
| A29 | person absorbed at a screen | 1 | generic; stock or AI + disclosure |
