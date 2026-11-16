# BUILD-LOG — tldr-where-the-axis-starts

## Executive summary
A `tldr` film of chapter 10 of INFO 7375 Computational Skepticism for AI, section S4 "Where the Axis Starts". The key case is the chapter's Exercise 1, a constructed exercise captioned as such on screen. A chart runs from 91 to 96, and Model A (92.1%) and Model B (94.3%) look three to one.

The film has two TL;DR cards, the hesitant writer ("Is B three times better?" → "Where does the axis start?") and three terms. Then come ten pure-Manim LEARN beats on one persistent chart whose only moving value is the axis floor:
- braces from the floor (1.1 and 3.3);
- the floor slides to zero (×3.0 → ×1.02);
- every label passes a fact-check while the eye still reads ×3;
- the cut at 91: the same 91 is thrown away from both bars and the slivers are stretched;
- a commit ("where must the floor go for ×2?");
- one sweep of the floor 91 → 89.9 (×2) → 80 → 0 → 92 (×23);
- only then the name and the rule: a truncated axis, looks = (B − floor)/(A − floor), plus its tangent;
- the hook chart returns with "+2.2 points".

The film closes on the your-turn standard (Exercise 3's mismatched panels). Liam narrates, in for Bear (Kokoro `am_onyx`, greeting Swahili "Jambo", assigned). The master is 5:22 and every gate passes. Not staged, not published; verdict pending.

## Decision log
- **GATE S:** Bear signed the pick 2026-09-23 (the 13 first picks).
- **Representation:** every bar = a shared part below the floor (thrown away) + a sliver above it (stretched to fill the frame). The persistent object is a `_Chart` state factory driven by one `ValueTracker` (the floor). Every changing label is an `always_redraw` Text, so any sampled frame is crisp (the sibling lesson: GATE T samples the 50% frame).
- **Numbers:** only Exercise 1's three inputs (92.1, 94.3, the 91 floor; top 96). Every derived ratio is exact-fraction asserted in `make_sheet.py` and `scenes.py`: 3.0, 1.02, 2 at 89.9, 1.18 at 80, 23 at 92. The ×23 and the ×2-at-89.9 are recomputations, not chapter statements (FACTCHECK rows 8, 10).
- **Top held at 96 throughout.** Only the floor moves (change one thing). The zero-floor view is therefore a 0–96 axis, not 0–100.
- **Stock prices** (the chapter's honest-use example) are spoken only. The chapter gives no stock data, so no chart was invented. This deviates from the sections card, which suggested a second slide on stock data.
- **No lie factor.** Tufte's lie factor is not in the chapter and was left out.
- **YOUR TURN:** Exercise 3 recast as predict-then-check. At equal bar fractions, B (floor 85) > A (70) > C (60). This is asserted in `make_sheet.py`.
- **Greeting:** "Jambo" was assigned by the orchestrator. Other books' tldr sheets (the PE course, Coursera 6205) also use it; no film in this book does.
- **Merge conflicts:** nothing the film uses sits inside the chapter's four conflict blocks.
- **Helpers:** `lock_cards.py` comes from tldr-robust-against-what (new anchors) and `_until` from tldr-both-audits-were-right. Re-run `lock_cards.py` after any `make_sheet.py`.

## Gate history
- `bookend_check.py`: PASS at sheet time and after the final.
- Paperwork set (FACTCHECK 20 rows, SHOTLIST, PROMPTS, CHECKS-REPORT with the Gate-1 table, SOURCES, README, BUILD-PROMPT, build_srt.py) was written before any render. `factcheck_check.py`: 0 blockers, FC-4 coverage complete.
- Audio: 17 mp3s. B02 first measured 8.73 s, under the 9 s writer window, so one clause was added and it re-measured 10.18 s. BOUT was apad-padded by 1.0 s, so `actual_duration_s` = 4.11 (ffprobe). `lock_cards.py`:
  - B00 cues 1.5 / 9.15 / 14.59 / 18.16;
  - B01 cues 0.8 / 6.04 / 10.21 / 13.36;
  - B00/B01/B03 `durationSeconds` from the measured audio.
- Pre-audit: Gate A ×10 clean, Gate W ×10 clean. The layout audit (`--curve-strict`) first flagged three things:
  - B11: the "1.1" brace label sat on the brace;
  - B19: the "+2.2 points" label sat on the brace, and two rows ran past the safe edge;
  - B13: a crash, because FadeOut of `always_redraw` text ran concurrently with the floor tween, so the text's glyph count changed mid-animation (the panel fade is now a separate play).

  All 10 were CLEAN after fixes.
- Low-res contact sheets (25/60/92%), two rounds, with fixes:
  - the floor label collided with "Model A" when it read 78.8, so it moved left of the axis, right-aligned;
  - the chart was enlarged (H 4.4, bars 1.0 wide, spread);
  - B14's "91" cut label was left floating after the cut, so it now fades with the line;
  - B18's worked fractions stacked tight, so they were re-spaced;
  - B10's readout panel now lands with the axis (the early frames had been sparse);
  - MathTex `Write` was swapped for `FadeIn`, because a mid-Write "= ?" was on the 50% frame.
- `art run` #1: **Gate A FAILED on B12** inside run.sh's isolated copy. There is no beat_sheet.json there, so `_until` is a no-op, the new shape existed before the first snapshot, and the stub saw "shapes never change". Fix: a `self.wait(0.3)` before the first new shape in B12 and B15, verified by running Gate A on an isolated copy of scenes.py for all ten scenes.
- `art run` #2 (4K): Gate A/W clean, layout audit clean, 17/17 slots, **Gate V 34 frames, 0 BLOCKER / 0 MAJOR**.
- `art final` #1: **GATE T PASS** (0 FAIL). The §8.10 advisories (B01 0.90, BVDT 0.97: narration recites the card) are expected for TL;DR and verdict cards. SKIN LINT notes that ClaudeTldrWhat is not the composer, which is expected for tldr.
- Frame check on the master:
  - B00 at 50% (10.7 s): only line 1 is on screen.
  - B00 at 90%: all three lines, numeral 3 in terracotta.
  - B01 at 90%: all three dashes.
  - B02 at 90% (48.05 s): "Where does the axis start?" is on screen. The correction completes at about 46.7 s, 2.4 s before the cut; that was accepted and not re-rendered.
- Process note: the 4K `art run`/`art final` were launched as single backgrounded commands (one at a time, never concurrent), because the 10-minute foreground tool limit would otherwise kill them.

## Manuscript notes for Bear (not fixed in the chapter)
- Exercise 1 asks for "the ratio of the visual difference to the actual difference", which has two readings. One is the height ratio (3.0 visual vs 1.024 actual, which the film uses). The other is Tufte's lie factor, (3.3 − 1.1)/1.1 ÷ (2.2/92.1) ≈ 84. A student can defensibly answer either. Consider naming which one is wanted.
- "Roughly three times" is exactly 3.0 on the exercise's own numbers. "Roughly" could go.
- The catalog's truncated-axis entry uses a floor of 80. On Exercise 1's numbers that floor gives ×1.18, a mild amplification. The chapter's point holds, but the 80 example is weaker than the 91 one.
- The chapter still carries four unresolved merge-conflict blocks (HEAD 10.x vs d78899b 11.x figure numbers and the closing sections). They were untouched.

## MASTER — 2026-09-23 15:05
`exports/landscape/tldr-where-the-axis-starts.mp4` — 3840×2160 · 24 fps · H.264 + AAC · 321.75 s (5:22) · sha256 d689ba992034f50c… Verdict pending. Not staged, not published. To stage (Bear's word only): `stage_publish.py` → `build_srt.py` → `art post --no-topaz`.
