# p-value reel — B20 resolved, one fabricated citation, and a correction to my own layout advice

## 1. The B20 gate worked, and my factcheck was the thing that was wrong

The beat flipped. Someone opened the abstract, the figures **are** in the first
paragraph, and B20/B21 were rewritten and re-voiced to say so:

> *"A research pass marked those numbers absent from the paper. Queries primed
> with the figures confirmed the finding. The neutral-framed query disagreed. A
> human opened the abstract. The numbers are in the first paragraph. The addendum
> got it right. This film's factcheck did not — until someone went and looked."*

That is the correct outcome and it makes the reel better than the version I
planned. The addendum was right. My research pass was wrong, in precisely the way
FACTCHECK.md flagged as possible — primed queries confirmed, the neutral query
didn't, and I held it at PLAUSIBLE rather than CONFIRMED for that reason. The
verification came back the other way and the accusation died before it shipped.

**Both narration beats flipped correctly** (B20 18.01s, B21 17.49s) — no
audio/visual contradiction. Nothing to fix here. FACTCHECK.md should be updated
to record the resolution, and BVDT's fourth verdict line should be checked for
any residual claim about the citation.

## 2. THE ACTUAL EMERGENCY — a fabricated citation, on screen

`manim/scenes.py`, line 1168:

```python
"Jovanović, Staab, Wattenhofer & Gündel — ICML 2024, PMLR 235",
```

The real authors are **Jovanović, Staab & Vechev**. "Wattenhofer & Gündel" do not
exist on that paper.

The beat sheet has it right (`attribution: 'Jovanović, Staab & Vechev — ICML
2024'`). FACTCHECK.md has it right. **The scene file re-typed the string and
invented two co-authors** — in a film about fabricated citations, one beat after
the film corrects itself for nearly making a fabricated-citation accusation.

I checked the other eight rendered citations and every key number against the
beat sheet. **Only this one drifted.** Nature 634, Patterns 2023, Krishna
NeurIPS 2023, PVMark USENIX 2026, ICML 2023 PMLR 202, 61.22%, 57.2%, 8%,
0.01/0.02%, 200/600/800 tokens — all correct.

One drift is one too many for this reel. And the systemic cause is that scene
files **restate** on-screen text instead of **reading** it.

## 3. A correction to what I told you about layout

I said the fix was relative positioning. That was incomplete, and this reel
proves it.

`manim/scenes.py` uses **70 `next_to`, 30 `.arrange()`, 20 `move_to`**. The
advice was followed thoroughly. It still collides. Look at B05:

```python
lbl_A = _t("WATERMARKED",     size=26).next_to(bar_A, DOWN, buff=0.22)
lbl_B = _t("NOT WATERMARKED", size=26).next_to(bar_B, DOWN, buff=0.22)
...
delta_grp.next_to(bars, LEFT, buff=0.30)
note_grp.next_to(bars, UP,   buff=0.60)
```

Every one of those is correct. Each label is properly anchored to its own
referent. And "WATERMARKED" still fuses into "NOT WATERMARKED", and the deltas
still print through the "≈ 20 million live Gemini responses" note.

**`next_to` guarantees an element won't collide with its referent. It guarantees
nothing about siblings.** Two elements anchored to the same bar group from
different sides will happily occupy the same pixels.

The thing that actually catches this is the pairwise bbox assertion — and
`assert_no_overlap` appears **0 times** in this file. That was step 1 of the
Simon's Ant prompt and it's the load-bearing half. I over-weighted the idiom and
under-weighted the assertion; the assertion is the fix.

## 4. Gates passed again — third reel running

GATE-V: 50 frames, 0 BLOCKERs. GATE-T: 25 beats, 0 FAILs. Five beats have
visible fused text. Same fused-run blind spot. Stop treating green as evidence.

---

## Prompt

```
Fix computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict.

Do NOT touch B20 or B21. Those beats were correctly resolved: a human checked the
paper, the figures ARE in the abstract's first paragraph, and both beats were
rewritten and re-voiced to say the factcheck was wrong and the addendum was
right. That is the intended final state.

STEP 1 — FABRICATED CITATION ON SCREEN. Fix this first.

manim/scenes.py line 1168 renders:
    "Jovanović, Staab, Wattenhofer & Gündel — ICML 2024, PMLR 235"
The real authors are Jovanović, Staab & Vechev. "Wattenhofer & Gündel" are
invented. The beat sheet and FACTCHECK.md both have it right; the scene file
re-typed it and hallucinated two names.

Correct it to:
    "Jovanović, Staab & Vechev — ICML 2024, PMLR 235"

Then audit EVERY other literal string in manim/scenes.py that names a person,
paper, venue, year, or figure, and diff it against beat_sheet.json and
FACTCHECK.md. I checked the other eight citations and the key numbers and they
match — confirm that independently and report any I missed.

STEP 2 — STOP SCENE FILES FROM RESTATING ON-SCREEN TEXT.
This is the systemic cause of step 1. Scene files currently re-type citations,
labels, and figures that already exist in beat_sheet.json.

Change the pattern: on-screen text is READ FROM the beat sheet, never restated in
the scene. Each Manim scene should take its strings from its beat's
shot.show[] events / graphic.production_viz / a new explicit
graphic.text{} block, so there is exactly one place a citation can be wrong.
Where a scene genuinely needs a string the beat sheet doesn't carry, ADD it to
the beat sheet and read it back — do not inline it.

Apply this to this reel's scenes now. Report what it would take to apply it
toolkit-wide; do not do that sweep in this pass.

STEP 3 — THE COLLISIONS. Read this before you start.

My earlier guidance was incomplete. This file ALREADY uses relative layout —
70 next_to, 30 .arrange(), 20 move_to — and it still collides, because next_to
only guarantees an element won't hit its REFERENT. It says nothing about
siblings. B05 is the proof:

    lbl_A = _t("WATERMARKED",     size=26).next_to(bar_A, DOWN, buff=0.22)
    lbl_B = _t("NOT WATERMARKED", size=26).next_to(bar_B, DOWN, buff=0.22)
    delta_grp.next_to(bars, LEFT, buff=0.30)
    note_grp.next_to(bars, UP,   buff=0.60)

Every line correct; "WATERMARKED" still fuses with "NOT WATERMARKED", and the
deltas still print through the 20-million-responses note.

So the fix is the ASSERTION, which this file does not have (assert_no_overlap
appears 0 times). Add the helper from
computational-skepticism-for-ai/youtube/claude-liam-simons-ant/FIX-PROMPT-2.md
(pairwise mobject bbox intersection, tolerance 0.02, raises AssertionError with
the scene name), and call it at the end of construct() in EVERY scene in
manim/scenes.py — not just the broken ones. Then fix whatever it catches.

Known broken (the assertion will find more):
  B05  "WATERMARKED" fuses with "NOT WATERMARKED"; the Δ pair prints through
       "≈ 20 million live Gemini responses"
  B13  three stacked title lines crowd the top and "61.22%"; at the bottom
       "NON-NATIVE ENGLISH WRITERS" collides with "ESSAYS" and with the Liang
       citation
  B15  "IMPOSSIBLE", "PUBLIC-KEY VERIFICATION" and "ZERO-KNOWLEDGE PROOF" are
       all on screen at once, overlapping. The spec was a SEQUENCE: wall reads
       IMPOSSIBLE → two doors open → wall RELABELS to UNBUILT. Check whether the
       relabel is happening at all; if the three labels are meant to coexist,
       they need separate regions.
  B16  "DEPLOYED SCHEMES" collides with "> 80%"; "SYNTHID" collides with
       "mostly fails"; the citation collides with "SCRUB" and the bottom rule
  B20  the query-path labels (PRIMED QUERY / NEUTRAL QUERY / OPEN ABSTRACT /
       ABSTRACT / ABSTRACT, FIRST PARAGRAPH / PRESENT) and the two quoted
       figure strings are mutually overlapping — this beat is the worst in the
       reel and it is the beat about checking things carefully

HOW to fix what the assertion catches: siblings that can collide must be laid out
as a GROUP — VGroup(...).arrange(DIR, buff=...) — so the arrangement itself
guarantees separation, rather than each being next_to'd independently to a shared
referent. Where two labels sit under adjacent bars, arrange the label row and
distribute it to the bars, or widen the bar gap. One type size per role. Never
shrink below the §8.1 floor to make something fit; if it genuinely doesn't fit,
the beat carries two ideas — log it in BUILD-LOG.md.

STEP 4 — re-render, then LOOK.
Manim scenes render through the normal path; then recompile. Do NOT trust the
gates: GATE-V passed 50 frames with 0 BLOCKERs and GATE-T passed 25 beats with 0
FAILs on the cut that has all five of these collisions in it. That is the
documented fused-run blind spot — completely collided text merges into one run
and cannot be detected. Extract and READ frames for B05, B13, B15, B16, B20 and
paste them back. Frames or it didn't happen.

STEP 5 — update FACTCHECK.md.
Record the B20 resolution: the numbers ARE in the abstract's first paragraph of
Kirchenbauer et al. (ICLR 2024); the addendum was correct; this reel's own
research pass was wrong, and the priming-contamination caveat in the original
entry is what caught it. Also check BVDT's verdict lines for any residual claim
about the citation being absent, and log the Jovanović citation fix.

Do not publish. Do not touch books/youtube/TOPOST/.
```
