# BUILD-LOG — tldr-the-boundary-scaling-cannot-cross

## Executive summary
This is a `tldr` film of INFO 7375 Computational Skepticism, chapter 13, section S1, "The Boundary Scaling Cannot Cross". It teaches the chapter's central move: the data-world gap is categorical, not a frequency. Every enlargement of a sample is still a region with an edge, and the edge is where the gap lives (Figure 13.1, rebuilt from its caption).

The film has two TL;DR cards, the hesitant writer ("Can enough data close the gap?" → "…cross its own edge?"), three prerequisite terms (sample · in-distribution · distribution shift), ten pure-Manim LEARN beats and the your-turn close. The LEARN beats run:
- the turkey's confidence curve rides to day 1,000, with day 1,001 just past the axis;
- the chapter's 99.7% system on 10,000 routine cases, drawn as a sample inside the world;
- the sample grown twice, with the edge still there;
- the critic's "scale it enough" trend line, broken by the turkey's gap of 1 morning in 1,001;
- the edge as the place where the gap lives;
- a commit beat;
- the collision: the curve's mornings fly into the world as a flat sample, day 1,001 lands outside, and more mornings stretch the sample along the routine without ever reaching it;
- the name, "the data-world gap", after Hume (1748);
- the chapter's composite clinic (94%, three patients harmed outside the edge);
- back to the turkey: "is tomorrow inside?".

Liam narrates, in for Bear (Kokoro `am_onyx`, greeting Hawaiian "Aloha"). The master is 4:57 and all gates PASS. Verdict pending; not staged, not published.

## Decision log
- **GATE S:** Bear signed the pick on 2026-09-23 (the 13 first picks).
- **Greeting:** Aloha (Hawaiian), assigned by the coordinator.
- **The one representation (B14):** a sample region inside an unshaded world. The excluded part is its complement, and the edge is defined by where the data stopped. Figure 13.1's PNG is not in `images/`, so the figure was rebuilt from its caption (REBUILD LAW).
- **Collision (B16):** the turkey's curve IS a sample. Its 22 mornings fly into the world and become a long, flat region along the routine. Day 1,001 lands off that axis, and stretching the sample with more mornings never reaches it. This follows the sections card: "the event sitting off the axis the curve was fitted on".
- **NAIVE (B13):** the chapter's functionalist, who says the gap is a frequency and scale will shrink it to nothing. The objection is walked to a dashed extrapolation to zero and broken with the chapter's own numbers: the turkey's gap was 1 morning in 1,001, under 0.1% (recomputed), and it was the only morning that mattered. This lines up with the chapter's "I will not argue from frequency".
- **Turkey scope:** kept on chapter 13's argument (the edge that more data inside it cannot cross), not on falsifiability, which is chapter 1's film `tldr-a-claim-that-cannot-be-wrong`.
- **Composite:** B18 uses the chapter's labelled composite opener (94%, three patients). It is said aloud as "a composite case, not a single incident" and captioned "a composite, not one incident" on screen. B18 takes one line of S2's material (the chapter's own "ninety-four percent and three harmed patients" sentence in §Skepticism as safety mechanism). S2 still owns the two-deployment contrast.
- **Schematic:** the confidence curve has no scale ("confidence: schematic, no scale") and the region areas are illustrative ("regions: schematic"). No number is read off either.
- **Left out:** both `[verify]` flags (the *Irreducibly Human* dependency, the calibration ranges), Epic Sepsis (S3), Turing/Searle (S4) and the five-component practice. Meaning and intentionality are the boundary caption.
- **No equation lands** (the sections card states complementarity in words), so there is no TANGENT. B18 is a post-shift INSTANCE.
- **Merge conflicts:** none of the film's material sits inside the chapter's three conflict blocks. Where figure numbers matter, the HEAD side governs.
- **Helpers reused:** `lock_cards.py` (from tldr-where-the-human-steps-fall, with new anchors) and the `_until(phrase)` pacing helper. `lock_cards.py` must be re-run after any `make_sheet.py` run.

## Gate history
- `bookend_check.py`: PASS at sheet time and after the final.
- Paperwork was written before any render: FACTCHECK (27 rows), SHOTLIST, PROMPTS, CHECKS-REPORT (Gate-1 table), SOURCES, README, BUILD-PROMPT and build_srt.py.
- Audio: 17 mp3s, 292.6 s. The BOUT mp3 was apad-padded by 1.0 s, so `actual_duration_s` = 4.71 (ffprobe). `lock_cards.py` set:
  - B00 cues 1.5 / 10.16 / 13.76 / 17.42;
  - B01 cues 0.8 / 4.43 / 9.56 / 12.69;
  - B00/B01/B03 `durationSeconds` from the measured audio.
- Pre-audit: Gate A ×10 clean, Gate W ×10 clean, layout audit (`--curve-strict`) ×10 CLEAN.
- Low-res contact sheet (25/50/60/92%), round 1, fixes made:
  - B15's "more mornings: does it move in?" overflowed the world box, so it became "more mornings: in?".
  - B15's question was mid-fade at 50%, so it moved earlier, onto "Put the turkey's".
  - The turkey's morning rows touched the sample edge, so the sample was made taller (b 0.62 → 0.8, centre y −0.8).
  - B17's "complementary by construction" was mid-fade at 50%, so it now lands 1.4 s early.
  - B18's left side was empty until late, so the two questions now land with the first images.

  Round 2 was clean.
- 4K `art run` #1: 17/17 slots, **Gate V 0 BLOCKER / 0 MAJOR**. The review cut's B00/B01 cards landed on their clauses, and B02 had the correction on screen by about 60%.
- `art final` #1: **GATE T FAIL** on B16 and B19, §8.6b bbox overlap 100%. The ink morning-dot rows inside the flat ink ellipse fused into one "text run". Fix: once the mornings land in the sample they turn DIM, like the generic case-dots.
- `art final` #2: **GATE T FAIL** again on B16/B19. At 4K the flat ellipse outline (445 px tall) is itself read as a text-run blob, and it enclosed the ink "fed mornings" label. Fix: the label moved above the sample (FLAB 1.9, 0.45) and "excluded" moved to (1.35, 1.35). A pre-check with `type_check.check_bbox_overlap` on 3840×2160 renders of B16–B19 at 10/30/50/70/90% passed, with only §8.6c advisories. B16–B19 mp4s and their 2160p partial-movie caches were cleared before the re-render.
- `art run` #3: Gate V 0 / 0, 17/17. `art final` #3: **GATE T PASS**. The §8.10 advisories on B00/B01/BVDT (the narration recites the card) are expected for TL;DR cards. The SKIN LINT note ("cold open is ClaudeTldrWhat") is also expected for tldr, and bookend_check accepts it.
- Master frame check:
  - B00 at 50%: only line 1, which is landing on its clause. At 90%: all three lines, with numeral 3 in terracotta.
  - B01 at 50%: dash 1 only. At 90%: all three dashes.
  - B02 at 90%: "Can enough data cross its own edge?" is on screen.
  - B16 at 95%: the stretched sample, with day 1,001 outside and marked "still outside".

## Manuscript notes (for Bear — not fixed in the chapter)
- **Figure 13.1** (`images/13-the-limits-of-ai-what-the-tools-cannot-do-fig-03.png`) is referenced but not present in `images/`, and neither is fig-04 (13.2). The film rebuilt 13.1 from its caption.
- **The turkey across chapters:** chapter 13 has failure on day 1,001 after 1,000 fed days. Chapter 1's sections card (`tldr-sections-01-skeptics-toolkit.md`, S1 key case) has the farmer arriving on day one thousand. That was not checked against chapter 1's own text; if it holds, the two chapters count the turkey's days differently.
- **99.7% on ten thousand cases** is offered as a hypothetical ("may still be a turkey"), not a sourced system. The film presents it as the chapter's example, not as a real deployment.
- There are three unresolved merge-conflict blocks (lines 212, 254, 496). The `d78899b` side numbers the figures 14.x and carries the AI Wayback Machine section.

## MISSING / open
- Human sign-offs pending: FACTCHECK (GATE F) and the watch-the-cut verdict.

## MASTER — 2026-09-23 15:58
`exports/landscape/tldr-the-boundary-scaling-cannot-cross.mp4`: 3840×2160, 24 fps, H.264 + AAC, 297.1 s (4:57), sha256 32d0486e025d808b…. Verdict pending. Not staged, not published. To stage (Bear's word only): `stage_publish.py` → `build_srt.py` → `art post --no-topaz`.
