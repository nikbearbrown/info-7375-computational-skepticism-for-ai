# BUILD-LOG — tldr-a-claim-that-cannot-be-wrong

## Executive summary
A `tldr` film of INFO 7375 Computational Skepticism, chapter 1, section S1, "A Claim That Cannot Be Wrong Is Not a Claim" (Popper's falsifiability). It has two TL;DR cards, the hesitant writer ("prove it right" → "prove it wrong"), four prerequisite terms, ten pure-Manim LEARN beats on the 3Blue1Brown template and the your-turn close. Liam narrates, in for Bear (Kokoro `am_onyx`, greeting Vanakkam). The master is 5:15 and passed every gate. Verdict pending; not staged, not published.

## Decision log
- **GATE S:** S1 picked 2026-09-23 (Bear, the 13 first picks). A previous attempt was cut off before writing anything, so this build started from an empty folder.
- **The representation:** an outcome axis with the claim drawn as the region of outcomes it forbids (a dim-filled band labelled "forbidden"). "Robust" shades nothing. "< 2% over 30 days" carves a band on the right. "Recall ≥ 0.88" carves one on the left (B12 shows the band sliding to the other side).
- **The collision (B16):** two threads meet. One is the swan count (the five favorable checks, which push a confidence bar that never reaches certain). The other is the forbidden region. The Michigan result drops to recall ≈ 1/3, inside the band, and the bar falls to zero.
- **Illustrative choices, all captioned on screen:** the three error-axis observations are constructed. The confidence bar is schematic. The sepsis claim borrows the table's recall floor (0.88); the chapter never says the vendor claimed it. The refutation holds for any floor above one third, which is asserted in code.
- **No equations** in the chapter or the film, so there is no TANGENT. The tenth LEARN slot is B17, a post-shift INSTANCE (the four table rows).
- **Not named:** "Epic" (the film says "a sepsis model"). **Left out:** the 18% alert share (true, but not needed); PSI's definition (named only).
- **Greeting:** Tamil (Vanakkam). tldr films have used Ciao, Hola, Hej, Merhaba, Sawubona, Jambo and Wagwan.
- **Merge conflicts:** everything this film uses lies outside the chapter's three conflict blocks.
- **B19 narration revised after audio:** "never refuted vs never at risk" became "survived a real test vs never at risk", to match the twin PASS tiles. Only B19 was regenerated (`--only B19`).

## Gate history
- `bookend_check.py`: PASS.
- Audio: 17 mp3s. B00/B01/B03 `durationSeconds` set from `actual_duration_s`, and their cues scaled proportionally. The scaled cues match the clause character positions within 0.3 s. BOUT was padded 1.0 s; `actual_duration_s` = 5.181 (ffprobe).
- Pre-audit: Gate A and Gate W were clean ×10. The layout audit flagged B12/B13 (a two-line claim transformed into a one-line claim collapses its two lines onto each other). Fixed with a FadeOut/FadeIn swap.
- Low-res contact sheets (two rounds), with fixes:
  - B10 question moved off the tally line.
  - B13 rows spaced out.
  - B16 "refuted" moved beside the claim.
  - B17 rows spaced.
  - B19 twin tiles held on the spoken sentence.
  - Regions now grow along one axis (they had been scaling from a corner).
- `art run` #1: Gate B clean; Gate V had 11 MAJOR `low-contrast` findings on B11/B12/B14/B15/B16/B19. The dim band at 0.22 opacity counted as "ink" and pulled the mean ink luminance toward the background. The fill went down to 0.17 opacity, which is under the INK_DELTA threshold but still visible. This was verified with `final_frame_check.analyze_frame` on 720p frames. The eight affected scenes were deleted and re-rendered.
- `art run` #2: Gate A/W clean, 17/17 slots, **Gate V 0 BLOCKER / 0 MAJOR**.
- `art final`: **GATE T PASS**. §8.10 advisories (B00/B01/BVDT narration close to the card text) are advisory by design for TL;DR cards. The SKIN LINT note about ClaudeTldrWhat vs the composer is expected for tldr (bookend_check accepts it).
- Frame check on the master:
  - B00 at ~50%: only the question is on screen.
  - B00 at ~90%: all three lines, numeral 3 in terracotta.
  - B01 at ~50%: dash 1 only.
  - B01 at ~90%: all three dashes.
  - B02 at ~90%: "What result would prove it wrong?" is on screen.

## Manuscript notes (for Bear)
- The chapter's table recall floor is generic. The chapter never states what the sepsis vendor claimed, so the film's Popperian form of the sepsis claim is borrowed and is labelled as borrowed.
- The chapter's three unresolved merge-conflict blocks are still there (not touched here).

## Master — 2026-09-23 12:40
`exports/landscape/tldr-a-claim-that-cannot-be-wrong.mp4`: 3840×2160, 24 fps, H.264 + AAC, 315.0 s (5:15), sha256 889110c54e04c659…. Verdict pending. Not staged, not published. To stage (Bear's word only): `stage_publish.py` → `build_srt.py` → `art post --no-topaz`.


## Published — 2026-09-24
Bear: "Looks great" + publish runbook. Staged via `art post --no-topaz` (full-text SRT first), TOPOST gate + sha assert PASS, uploaded **unlisted** → https://youtu.be/N7U8T_nMQF8, playlist Claude & Agentic AI, captions attached. Logged in `books/youtube/PUBLISH-LOG.md`. Public flip: Bear, in Studio.
