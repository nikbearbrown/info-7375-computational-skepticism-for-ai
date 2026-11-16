# Simon's Ant — round 2. Why it's still green, and the prompt.

## The MUTE fix landed. That wasn't the whole bug.

`check_bbox_overlap` now calls `visible_text_mask(arr, polarity)` →
`ink_mask(INK) | ink_mask(MUTE)`. MUTE text is detected. That part is fixed.

**It still passes because a total collision is invisible to an overlap check by
construction.**

The check compares bounding boxes of *distinct text runs*. When two labels
collide completely — `PHOENIX` + `BOSTON` printing over each other — the blob
labeller sees one contiguous ink region and `text_run_bboxes()` merges it into
**one run**. One run cannot overlap itself. And when a frame's text merges down
to a single run, the function hits:

```python
if len(bboxes) < 2:
    return "PASS", "fewer than 2 text-run blobs — no overlaps possible"
```

The more complete the collision, the more certainly it passes. The detector is
blind to exactly the defect it was written to catch.

`scenes.py` was edited at 13:54 (B16 gained its caption, B23's text moved),
GATE T ran at 14:05, green. B07's coordinates were never touched:

```python
l_label = caps("SUNDIAL", sz=28, clr=INK).move_to([-3.2, -1.55, 0])
ph_tag  = caps("Phoenix", sz=28, clr=INK).move_to([-2.9, -0.95, 0])
bo_tag  = caps("Boston",  sz=28, clr=MUTE).move_to([-1.8, -0.95, 0])
```

1.1 units apart; `PHOENIX` at sz=28 is ~1.6 units wide.

**Stop trying to catch this in the raster.** Assert it on the mobjects, before
render — exact geometry, no thresholds, no blob heuristics, and it fails at
build time instead of at your eyes. `scenes.py` currently has **86 hardcoded
`move_to([x,y,0])`, 9 `next_to`, and zero assertions.**

---

## The prompt

```
Fix the text collisions in
computational-skepticism-for-ai/youtube/claude-liam-simons-ant/scenes.py.

CONTEXT — do not re-do work that is already done:
The MUTE blind spot in brutalist-art/runtime/scripts/type_check.py IS fixed.
check_bbox_overlap correctly calls visible_text_mask() = ink_mask(INK) |
ink_mask(MUTE). Leave that alone.

WHY IT STILL PASSES: the overlap check compares bounding boxes of DISTINCT text
runs. When two labels collide completely, the blob labeller sees one contiguous
region and text_run_bboxes() merges it into ONE run. One run cannot overlap
itself, and if a frame's text merges to a single run the function returns
"fewer than 2 text-run blobs — no overlaps possible" → PASS. A total collision
is structurally invisible to it. Do not try to fix this by tuning the raster
heuristics — assert on the mobjects instead.

STEP 1 — add the geometry assertion and wire it into every scene.

At the top of scenes.py add:

    def assert_no_overlap(*mobs, tol=0.02, scene=""):
        """Fail at build time if any two mobject bounding boxes intersect
        beyond tol (fraction of the smaller box's area). Exact geometry —
        immune to the raster checker's fused-run blind spot."""
        items = [m for m in mobs if m is not None]
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                a, b = items[i], items[j]
                ax0, ay0 = a.get_left()[0], a.get_bottom()[1]
                ax1, ay1 = a.get_right()[0], a.get_top()[1]
                bx0, by0 = b.get_left()[0], b.get_bottom()[1]
                bx1, by1 = b.get_right()[0], b.get_top()[1]
                ix = max(0.0, min(ax1, bx1) - max(ax0, bx0))
                iy = max(0.0, min(ay1, by1) - max(ay0, by0))
                inter = ix * iy
                if inter <= 0:
                    continue
                smaller = min(max(1e-6, (ax1-ax0)*(ay1-ay0)),
                              max(1e-6, (bx1-bx0)*(by1-by0)))
                if inter / smaller > tol:
                    raise AssertionError(
                        f"{scene}: text overlap {inter/smaller:.0%} between "
                        f"'{getattr(a,'text','?')}' and '{getattr(b,'text','?')}'")

Call it at the end of construct() in EVERY scene you touch, listing every text
mobject in that scene. A collision must fail the Manim build, not the eye.

STEP 2 — fix the four broken scenes with RELATIVE layout, not nudged numbers.

  B07_InnerOuterInterface   ph_tag x=-2.9 and bo_tag x=-1.8, both caps(sz=28).
                            Renders as "PHOEBOSTON". SUNDIAL sits under them.
  B16_AttributionTwoByTwo   col_h1/col_h2 at cell_h*0.85 are INSIDE the top row,
                            not above the grid; row_h1/row_h2 at -cell_w*1.15 are
                            not clear of the left column (hence "CHANG-ES" and
                            "SURVIV-ES" ghosting); cells mix caps(sz=36) with
                            serif(sz=48) and the serif cells overflow into the
                            caps cells.
  B19_DesignInversion       the bullet VGroup has no width constraint against a
                            fixed-width box; "ELABORATE INTERNAL LOGIC" overruns
                            the box and crosses the centre divider.
  B23_CataglyphisOdometer   the "Simon's claim: which LEVEL OF DESCRIPTION
                            explains the path." block still collides with
                            "(HOME VECTOR COMPUTED)".

HOW — this matters more than the four beats:
  - labels attach to their referent: .next_to(target, DIR, buff=...)
  - label rows become VGroup(...).arrange(RIGHT, buff=...) so they cannot
    collide by construction
  - grid headers position off the grid's bounding box (get_top(), get_left()),
    never off a cell-size multiple
  - text inside a box gets an explicit width derived from the box, and the box
    sizes to its content — one or the other, never neither
  - ONE type size per role within a figure. B16's caps(36)/serif(48) mix is the
    collision.
  - do NOT fix by shrinking type below the §8.1 floor. If it genuinely does not
    fit, the composition carries two ideas — say so in BUILD-LOG.md.

STEP 3 — sweep the rest of the file.
scenes.py has 86 hardcoded move_to([x,y,0]) against 9 next_to and 9 .arrange().
That ratio is the bug class: a type-size pass scaled the labels and the
coordinates stayed put. After fixing the four, add assert_no_overlap to every
remaining scene and re-render ALL of them. Report every scene that now fails —
those are collisions the gate has been passing this whole time.

STEP 4 — re-render, re-gate, and LOOK.
  python3 brutalist-art/runtime/scripts/remotion_scenes.py <reel>   (if any
      Remotion beats changed; Manim scenes render through the normal path)
  ./brutalist-art/art run computational-skepticism-for-ai/youtube/claude-liam-simons-ant
  GATE T → TYPECHECK.md zero FAIL
  Gate V → sample frames, actually Read the PNGs for B07, B16, B19, B23 and
      paste them back. A green gate is not evidence any more — this reel proved
      that. Frames or it didn't happen.

STEP 5 — close the hole in the checker so the next reel is caught.
In check_bbox_overlap, the "fewer than 2 text-run blobs" early return is a false
PASS when a frame HAS multiple text elements that fused. Add a fused-run
heuristic: FAIL (or WARN loudly) when a single text run's height exceeds ~1.8x
the median run height on that frame, or when a frame the beat sheet says has
N>=3 labelled elements resolves to 1 text run. Log it as §8.6c. This is a
backstop — STEP 1's mobject assertion is the real fix.

Do not publish. Do not touch books/youtube/TOPOST/.
```
