# Simon's Ant — the four fix prompts

Run from `books/`. Each block is a complete standalone prompt. Run them in order —
step 1 produces the FAIL list step 2 consumes.

---

## STEP 1 — make the type gate able to see MUTE text

```
GATE T has a blind spot and it just passed a reel with six visible text collisions.

Open brutalist-art/runtime/scripts/type_check.py.

THE BUG: check_bbox_overlap(), check_min_size(), and the per-blob contrast check
all build their detection mask with:

    mask = ink_mask(arr, hex_to_rgb(INK_HEX))

INK only. Every label drawn in MUTE is invisible to all three checks. When a
frame's visible text is all MUTE, the mask finds 0 or 1 blob and the check
returns PASS with "no text blobs — bbox-overlap check N/A" or "fewer than 2
text-run blobs — no overlaps possible". Line 157's comment states the assumption
that broke: "All visible text uses INK." That is no longer true — Manim scene
files use MUTE for the majority of their diagram labels.

THE FIX:
1. Add a helper that returns the union of the INK mask and the MUTE mask for
   light-polarity frames (and the corresponding union for dark polarity). Keep
   the existing per-colour tolerances; do not widen them.
2. Use that union in check_bbox_overlap, check_min_size, and the per-blob
   contrast check. Leave the accent-colour checks alone.
3. Re-tune the noise/min-px floor ONLY if the union starts flagging stroke
   fragments as text. Do not raise it to make failures disappear — if a real
   label is below the size floor that is a genuine FAIL.
4. Do NOT add per-scene exemptions. The existing §8.6b false-positive
   suppressions for box borders may stay; do not add new ones.

Then update skills/make/kerning/reference/type-spec.md §8.6b and §8.1 to state
that the detection mask is INK ∪ MUTE, and fix the stale "all visible text uses
INK" comment.

VERIFY: re-run the checker on a frame you know is broken —
computational-skepticism-for-ai/youtube/claude-liam-simons-ant/_qc/B16_frame.png
— and confirm it now FAILS bbox-overlap. If it still passes, the mask fix did
not take; debug before continuing.

Report the diff and the verification result. Change nothing else.
```

---

## STEP 2 — re-gate the reel and fix the scenes properly

```
Re-run GATE T on computational-skepticism-for-ai/youtube/claude-liam-simons-ant
with the fixed checker from step 1:

    python3 brutalist-art/runtime/scripts/type_check.py \
        computational-skepticism-for-ai/youtube/claude-liam-simons-ant

The previous run reported 28 PASS / 0 FAIL. That was wrong. Expect a real list.
Print it before changing anything.

Then fix the flagged scenes in that reel's scenes.py. These six are known
broken — the full list from the checker governs:

  B07_InnerOuterInterface   ph_tag x=-2.9 and bo_tag x=-1.8, both caps(sz=28).
                            "PHOENIX" is ~1.6 units wide at that size; the gap is
                            1.1. Renders as "PHOEBOSTON".
  B09_BehaviorEquation      the terracotta arrow starts at the E(t) label group's
                            centre and draws through the word ENVIRONMENT.
  B16_AttributionTwoByTwo   col_h1/col_h2 sit at cell_h*0.85 — INSIDE the top row,
                            not above the grid. row_h1/row_h2 at -cell_w*1.15 are
                            not clear of the left column. Cells mix caps(sz=36)
                            with serif(sz=48) and the serif cells overflow.
  B19_DesignInversion       the bullet VGroup has no width constraint against a
                            fixed-width box; "ELABORATE INTERNAL LOGIC" overruns
                            the box and crosses the centre divider.
  B21_HoraInterruptionCost  rotated y_lbl at sz=36 is taller than the plot area
                            and clips at both frame edges.
  B23_CataglyphisOdometer   limit [4.0,-2.5], return_lbl [-1.5,-2.8] and
                            odometer_lbl [2.5,0.0] are three hand-placed blocks
                            competing for one quadrant.

HOW TO FIX — this matters more than the individual beats:

The file has 86 hardcoded move_to([x,y,0]) calls against 9 next_to and 7
.arrange(). That is the actual bug class: a type-size pass scaled the labels and
the coordinates stayed put. Do NOT fix this by nudging coordinates — the next
type pass re-breaks every one of them.

Convert each flagged element to relative layout:
  - labels attach to their referent with .next_to(target, DIR, buff=...)
  - label rows become VGroup(...).arrange(RIGHT, buff=...) so they cannot
    collide by construction
  - grid headers position off the grid's bounding box (get_top(), get_left()),
    never off a cell-size multiple
  - text inside a box gets an explicit width constraint derived from the box, and
    the box sizes to its content — one or the other, never neither
  - within one figure, one type size per role. B16's caps(36)/serif(48) mix is
    the collision.

Keep FILL-THE-CANVAS: fix collisions by improving layout, not by shrinking type
below the floor. If an element genuinely does not fit, the composition is
carrying two ideas — say so in BUILD-LOG.md rather than shrinking it.

Then add a guard so this cannot recur silently: a helper in scenes.py that takes
a list of mobjects and asserts no two bounding boxes intersect beyond a small
tolerance, called at the end of construct() in every scene you touch. A
collision should fail at Manim build time, not at a human's eyes.

Re-render only the changed Manim scenes, re-run GATE T until zero FAIL, then run
the Gate V visual QC pass and actually Read the sampled PNGs. Report before/after
frames for all six.
```

---

## STEP 3 — add the missing opening (Simon, and why this is about AI)

```
The reel computational-skepticism-for-ai/youtube/claude-liam-simons-ant violates
EXECUTIVE-SUMMARY LAW (ai-explainer SKILL.md). Its spine is:

    B00 cold open (ant hook) → B01 "Act one. The beach." → B02 detail beat

There is no Beat 2 BLUF. B01 is a segment card. Two things are never established:
Herbert Simon is not named until B06 (~1:40 in) and the first AI beat is B16
(~5:00 in). For five minutes the viewer is watching an insect with no idea why.

Fix: revise B00 and insert two beats before B01. Do not touch B01 onward.

B00 — REPLACE narration_text with:
"An ant walking across a beach traces a path so jagged, so full of detours and
backtracks, that anyone watching from above would conclude: that animal is
solving a hard problem. That inference is wrong — and it is the same inference
you make every time you watch an AI agent produce an impressive trajectory. Liam
here, in for Professor Bear."
Update the ClaudeComposerAsk output lines so the ask lands answered on the new
stakes (COLD OPEN LAW). Keep the greeting and folderLabel as they are.

B00A — NEW BEAT, after B00, act "OPEN", lane REMOTION:
narration_text:
"The ant belongs to Herbert Simon. Nobel prize in economics, Turing Award, and
one of the handful of people who founded artificial intelligence as a field. He
put the ant in The Sciences of the Artificial, nineteen sixty-nine — not as a
charming image, but as a claim he meant literally, about how to tell a system
apart from the world it is walking through."
show block: three credential chips land on their spoken names (economics prize /
Turing Award / founded the field), then the book title and the year 1969 set
beneath in terracotta. Use FormBCard or ChipGrid — match the component's zod
schema exactly. No portrait unless a rights-cleared one is already in pantry/.

B00B — NEW BEAT, after B00A, act "OPEN", lane MANIM:
narration_text:
"Here is why that matters now. When an agent chains tool calls, recovers from a
failure, and hands you a clean answer, you are standing on the dune looking down
at the path. The question is which part of that performance is the model and
which part is the scaffolding around it. Simon's parable gives you a test, and by
the end of this you will be able to run it."
show block: redraw the beach path ONCE as an agent trajectory — same jagged
shape, relabelled tool call / retry / tool call / answer. Then the two-axis
diagnostic from B16 appears for about half a second and dissolves. It is the
promise, not the payoff — do not explain it here.
production_viz.note: "This beat makes the ant a diagram of the agent from the
start. The half-second diagnostic flash is deliberate — B16 pays it off."

Then:
  - generate audio for B00, B00A, B00B only (Kokoro am_onyx, free — this reel is
    claude-liam). Write measured durations back to actual_duration_s.
  - build the B00B Manim scene and render the B00A Remotion scene.
  - recompile and report the new total runtime (expect ~9:20).
  - do NOT re-render beats B01 onward; only changed slots recompile.

Do not publish. Do not touch books/youtube/TOPOST/.
```

---

## STEP 4 — sweep the other reels for the same blind spot

```
The MUTE blind spot in type_check.py (fixed in step 1) means EVERY reel whose
Manim scenes label in MUTE has been passing GATE T without being checked.

Find the blast radius. For each reel folder under books/*/youtube/*/ that has
both a scenes.py and a TYPECHECK.md reporting PASS:

  1. count MUTE-coloured text calls in scenes.py — caps(...clr=MUTE),
     serif(...clr=MUTE), mono(...clr=MUTE)
  2. count hardcoded move_to([ ... ]) calls vs next_to( and .arrange(
  3. flag the reel if MUTE text count > 10 AND move_to calls outnumber
     next_to + .arrange by more than 3:1

That ratio is the signature of the Simon's Ant failure: many labels the checker
cannot see, positioned absolutely so any type change collides them.

Write the ranked result to brutalist-art/MUTE-BLINDSPOT-SWEEP.md — reel path,
MUTE count, move_to : relative ratio, TYPECHECK status, and a RE-GATE / OK
verdict. Rank most-suspect first.

Do NOT re-render or edit any reel in this pass. Re-run type_check.py with the
fixed checker on the top 5 flagged reels only, and paste each one's real FAIL
count into the report so the scale of the problem is visible before anyone
decides what to rebuild.
```
