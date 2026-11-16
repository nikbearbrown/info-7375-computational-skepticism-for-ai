# BUILD-LOG — tldr-five-boxes-one-deployment

## Executive summary
A `tldr` film of chapter 12 of INFO 7375 Computational Skepticism for AI, section S5 "Five Boxes, One Deployment". The chapter's four-sentence content-moderation description (exercise A2, captioned "constructed exercise case") is filed into the chapter's five accountability boxes by its words: three ticks, two blanks, and an 18-month clock that fits no box. Then each box gets the chapter's own verification test, and every tick comes out: zero of five. SyRI shows the same shape in a real system: recourse and review "on paper, not in function", with the court supplying review and sanction late. Only then does the film name the rule: a requirement is present when its test passes, not when its word appears. Two TL;DR cards, the hesitant writer ("does it sound accountable?" → "does it pass the five checks?"), four terms, ten pure-Manim LEARN beats, and the your-turn close. Liam narrates, in for Bear (Kokoro `am_onyx`, greeting Zulu "Sawubona", as assigned). Master 4:52, all gates PASS. Not staged, not published; verdict pending.

## Decision log
- **GATE S:** S5 was signed by Bear on 2026-09-23 (the 13 first picks).
- **Representation:** a five-row checklist. The left side holds grey-outlined boxes, the names, and an evidence slot. The right side holds the test (dim) and, under it, the failure mode (ink). The 18-month bar sits at the bottom. The `_Board` state factory carries every state across B11–B19. The A2 fragments are the same text objects as they move from the paragraph into the rows.
- **Requirement names follow the chapter BODY.** The LLM Exercise's renamed list ("readability of decisions, traceability, redress, named-owner") is not used.
- **The tier taxonomy stays out.** That includes the table's Tier column and A2's "which tier" sub-question. It rests on the chapter's one `[verify]`. The boundary line "not taught: who holds each box" points to it without naming it.
- **"18 months, no incident" was corrected to "running for 18 months".** The sections card overstated A2, and `make_sheet.py` asserts the corrected wording.
- **The A2 verdicts are the film's own reading** through the chapter's tests, since the chapter poses A2 without an answer. FACTCHECK rows 12–17 carry the derivation. The key reading is the recourse row: the appeal belongs to moderators, via support, and the flagged poster gets nothing.
- **No equation, so no TANGENT.** The tenth slot is a post-shift INSTANCE (B17, SyRI, which the chapter's own regulatory paragraph supplies).
- **Tier:** the card said "standard". The measured film came to 4:52, one abstraction, single-insight length.
- **Greeting Sawubona** was assigned by the brief. Note that four PE-book tldr films (tldr-artifact-stopped-being-proof, -proportions-not-points, -seven-traces, -the-record-not-your-mind) already use it, and tldr-hold-one-fair's log lists it as used. It was kept because the assignment was explicit.
- **Pacing:** `_until(phrase)` puts reveals on the spoken word. The paced `play` never lets an animation straddle the clip's 50% frame: it shortens the animation to finish before the midpoint, or starts it just after. `_finish` has a 0.1 s minimum, so there is no overrun.
- **Helpers:** `lock_audio.py` comes from tldr-the-report-is-not-the-world with new anchors, and `build_srt.py` comes from the exemplar.

## Gate history
- `make_sheet.py` produced 17 beats. `bookend_check.py` PASS. `factcheck_check.py` clean (28 rows).
- Paperwork was written before any render: FACTCHECK, SHOTLIST, PROMPTS, CHECKS-REPORT (Gate-1 table), SOURCES, README, BUILD-PROMPT, build_srt.py.
- Audio: 17 mp3s, 291.8 s. BOUT was apadded 1.0 s, so `actual_duration_s` = 4.669 from ffprobe. `lock_audio.py` set B00 cues to 1.5 / 10.94 / 14.76 / 18.46 and B01 cues to 0.8 / 5.6 / 9.71 / 13.4, and set the B00/B01/B03 durations from the measured audio.
- **Gate A:** B10 failed "shapes never change", so a DIM rule under the paragraph was added. After that, 10/10 clean. Gate W 10/10 clean.
- **Layout audit (`--curve-strict`):** two findings, both fixed:
  - B19's caption ran past the safe edge, so it was shortened to "not taught: who holds each box".
  - B17's SyRI header ran past the safe edge, so it was shortened to "SyRI · Dutch welfare scoring".
  - The B17 caption was also shortened to "tested late, from outside" (it was over 34 characters).
- **Low-res contact sheets, round 1:**
  - The evidence lines crowded the names, so the row pitch was raised from 0.9 to about 1.0 and the evidence offset from 0.42 to 0.47.
  - The B13 X touched the bar label, so it moved right.
  - The B15 bracket and the B17–B19 divider touched the evidence text, so the columns were shifted (divider x −0.85, right column x −0.2).
  - Three scenes overran their audio by 0.4–0.6 s, from the 1.0 s minimum in `_finish`. The minimum was lowered.
  - Some 50% frames showed text mid-fade, so the midpoint guard now shortens the straddling animation instead of delaying it.
- **Round 2:** the bottom band was tightened (bar y −2.6, captions y −3.1).
- **4K `art run` #1:** 17/17 slots. Gate V 0 BLOCKER / 1 MAJOR: B12 at 85% was underfilled (53%) because the right column emptied once the fragments had moved. Fix: a dim note, "no sentence to file here", beside the two blank rows. It fades at the start of B13. B12 and B13 were re-rendered.
- **4K `art run` #2:** Gate W clean and **Gate V 0 BLOCKER / 0 MAJOR**.
- **`art final` #1:** **GATE T PASS** (0 FAIL, 17 beats).
- **Master frame check:**
  - B00 at ~50% (11.4 s): the question and line 1 only.
  - B00 at ~90%: all three lines, with numeral 3 in terracotta.
  - B01 at ~50%: dash 1 only. At ~90%: all three dashes.
  - B02 at ~90%: "Does it pass the five checks?", so the correction is on screen.
  - B16 at 93%: every tick is out and all five failure modes are lit. The "ticked: 0 of 5" tally lands on the final words ("Zero of five") in the last ~0.6 s of the beat, so it is brief.
  - B19 at 93%: the boundary caption is fading in on the beat's last clause.

## Manuscript notes for Bear (not fixed in the chapter)
1. **The LLM Exercise names the five requirements differently** from the body and the checklist table: "readability of decisions, traceability, redress, named-owner, etc." It should be aligned to Specifications / Audit trail / Recourse / Independent review / Sanctions.
2. **A2 asks for "which cognitive tier"** for each absent requirement, so the exercise depends on the unverifiable taxonomy (the chapter's one `[verify]`).
3. **A2 gives no answer key**, and the recourse sentence is ambiguous. It grants the appeal to *moderators*, not to the people whose posts are flagged. The film reads that as a failed recourse test. If that was not the intent, the exercise text should say who can appeal.
4. **"Most deployed AI systems are missing two or more"** (§"The five accountability requirements") is uncited. It was left out of the film.
5. The sections card's "18 months with no incident" was not in A2 (see the Decision log).
6. Figure numbering skips 12.6. There are no merge-conflict blocks in this chapter file.

## MISSING / open
- Human sign-offs pending: FACTCHECK (GATE F) and the watch-the-cut verdict.

## MASTER — 2026-09-23 15:07
`exports/landscape/tldr-five-boxes-one-deployment.mp4` — 3840×2160 · 24 fps · H.264 + AAC · 292.08 s (4:52) · sha256 52f3c2180dec907b… Verdict pending. Not staged, not published. To stage (Bear's word only): `stage_publish.py` → `build_srt.py` (full-text captions) → `art post --no-topaz`.
