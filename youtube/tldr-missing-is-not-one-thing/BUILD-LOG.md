# BUILD-LOG — tldr-missing-is-not-one-thing

## Executive summary
A `tldr` film of chapter 3 of INFO 7375 Computational Skepticism for AI, section S2 "Missing Is Not One Thing". Two income columns, each 18% blank, look identical. A random wipe fills safely. Table A's blanks are the under-25s, so the average lands high until you fill within the age group. Table B's blanks never line up under any recorded column, until the rows are sorted by the value nobody wrote down; the nine blanks are the nine highest earners. Only then do the names arrive: MCAR, MAR, MNAR. There are two TL;DR cards, the hesitant writer ("how much is missing" → "why it is missing") and TERMS, then ten pure-Manim LEARN beats on a constructed, seeded table, then the your-turn standard. Liam narrates, in for Bear (Kokoro `am_onyx`, greeting *Vanakkam*, Tamil). Master: 4:42, all gates PASS. Not staged, not published; verdict pending.

## Decision log
- **Resumed build.** An earlier attempt was cut off by a usage limit and left only `world.py`. It was sound: seeded, with every relation asserted. It was kept and extended (rev 2, below).
- **The one representation:** sort the missingness-matrix rows by a column and watch whether the blanks line up. A block means the blanks depend on that column. This is Figure 3.2's caption question ("does missingness depend on something we can see, or something we can't?") turned into motion. The chapter's PNG is not in `images/`, so the figure was rebuilt from its caption (REBUILD LAW).
- **Constructed table, direction only.** The chapter gives one number (18%) and no income values, so the film shows no dollar figure. The income axis has no numbers (lower / higher / truth). "constructed" is captioned on screen in B10 and B18.
- **Key case:** exercise 8 (18% blank, co-occurring with age < 25 → MAR) against the chapter's MNAR example (high earners suppress their income). MCAR (random wipe) is the baseline instance.
- **No equation lands** (the sections card: the taxonomy is stated in words), so there is no TANGENT. B18 is a post-shift INSTANCE (template stage 5): the chapter's study-dropout example in the same shape, which lands the chapter's detection claim ("who would not report this, and why?").
- **Rubin attribution:** spoken as "Donald Rubin's work", shown as "after Rubin (1976)". The chapter's own footnote says the three labels were consolidated in 1987.
- **Greeting:** Vanakkam (Tamil). No tldr film had used it; Wagwan rule: slug char-sum mod 10 = 2.
- **Course credit** is spoken in B00 and shown on the cards' course line.

## Gate history
- `make_sheet.py` → 17 beats; `bookend_check.py` PASS.
- Paperwork set written before any render. Audio: 17 mp3s, 281.95 s (Kokoro). Card durations and cues were written from measured audio. BOUT was padded by 1.0 s → 4.115 s.
- **Process slip:** a mid-build re-run of `make_sheet.py` wiped the audio-lock fields from the sheet. Narration was unchanged, so the mp3s stayed valid. Added `lock_audio.py` to reapply the lock and wired it into BUILD-PROMPT.
- Gate A / Gate W / layout audit (`--curve-strict`): all 10 clean after two fixes, a terracotta dot overlapping "commit" (B15) and "MNAR" (B17).
- **Low-res contact sheet, round 1:** stripe headers collided ("cityincome"), and a stray gap dash sat under the B12 axis. **Substantive problem:** in world rev 1, all nine top earners were aged 46+, so "sort B by age" visibly bunched its blanks at the bottom. That would have made B14's "still scattered" false on screen. **World rev 2:** a gentler age slope and an age-independent high-earner tail (seed 118). The top nine now sit at age ranks 8–41. The direction claims are re-checked over 2,000 fresh random draws (`ROBUST`): MCAR unbiased; MAR column fill high in every draw; MAR band fill unbiased. FACTCHECK was updated.
- Round 2: column pitch widened to 1.05; the "true income" labels moved under the bars; B17 columns re-spaced.
- `art run` #1: Gate A failed in `run.sh`'s isolated copy, which copies only scenes.py, so `import world` failed. Fix: scenes.py falls back to the reel's own world.py.
- `art run` #2 (4K): Gate B clean; **Gate V 17 × low-contrast + 1 underfill.** The mean ink luminance was dominated by the light recorded cells (#D3CCBC). Recorded cells were darkened to #BFB7A5 (young, imputed and bar shades adjusted to match). B18 got an early right-side note (underfill at 50%). A pre-check with `final_frame_check.py --frames-dir` on 20 frames came back 0/0 before spending the run.
- `art run` #3: Gate W ×10 clean, Gate B clean, **Gate V 0/0**.
- `art final` #1: **GATE T FAIL, B18 §8.1 (36 px text run).** The mid-clip sample landed mid-sort, with the label mid-letter-morph. Labels now cross-fade (`FadeTransform`, affecting B14/B18/B19), and B18's second sort now settles before the clip midpoint. B14/B18/B19 were re-rendered (partial-movie cache cleared first).
- `art run` #4: Gate B clean ×3, Gate V 0/0. `art final` #2: **GATE T PASS** (0 FAIL; §8.10 advisory only on B00/B01, where the cards recite the narration by design). SKIN LINT advisory: "cold open is ClaudeTldrWhat". Expected for tldr; bookend_check accepts it.
- Frame check of the master: B00 at 50% shows line 1 only, at 90% all three lines. B01 at 50% shows dash 1, at 90% all three. B02 at 90% shows the correction on screen ("why it is missing?").

## MISSING / open
- Figure 3.2's image file is absent from `images/`. The figure was rebuilt from its caption.
- Human sign-offs pending: FACTCHECK (GATE F), watch-the-cut verdict.

## MASTER — 2026-09-23 12:57
`exports/landscape/tldr-missing-is-not-one-thing.mp4` — 3840×2160 · 24 fps · h264 + AAC · 282.25 s (4:42) · sha256 c23a8030dcdee039… Sent to Bear. Not staged, not published. To stage (on Bear's word only): `stage_publish.py` → `build_srt.py` (full-text captions) → `art post --no-topaz`.


## Published — 2026-09-24
Bear: "Looks great" + publish runbook. Staged via `art post --no-topaz` (full-text SRT first), TOPOST gate + sha assert PASS, uploaded **unlisted** → https://youtu.be/-FZsJZmFYPo, playlist Claude & Agentic AI, captions attached. Logged in `books/youtube/PUBLISH-LOG.md`. Public flip: Bear, in Studio.
