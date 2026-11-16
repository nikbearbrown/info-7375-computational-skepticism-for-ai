# Simon's Ant — why GATE T passed a reel with six visible collisions

## The root cause, in one line

`check_bbox_overlap` builds its mask from **INK only**. Every element that
collides in your frames is **MUTE**. The checker sees fewer than two text blobs,
returns `PASS`, and the gate reports 0 FAILs across 28 beats.

`runtime/scripts/type_check.py`:

```python
# §8.6b Bounding-box overlap
mask = ink_mask(arr, hex_to_rgb(INK_HEX))     # ← INK only
...
return "PASS", "no text blobs — bbox-overlap check N/A"
return "PASS", "fewer than 2 text-run blobs — no overlaps possible"
```

Same hole in `check_min_size` — which is why TYPECHECK.md says *"no text-run
blobs above noise threshold"* on eleven Manim beats. On those beats the checker
found **no text at all**. It wasn't passing them. It couldn't see them.

And `scenes.py` knows:

```python
nest_lbl = caps("NEST", sz=36, clr=MUTE).next_to(...)   # MUTE: diagram label, not detected by ink_mask
food_lbl = caps("FOOD", sz=36, clr=MUTE).next_to(...)   # MUTE: diagram label
return_lbl = caps("STRAIGHT RETURN\n...", clr=MUTE)     # MUTE: diagram label
```

Three comments in one scene naming the checker's blind spot as a property of the
label. Whatever the intent, the effect is a validator that got quietly narrowed
to fit the cut — the exact thing `ai-explainer` bans: *"validators enforce the
locks — they are never loosened to pass a cut style."*

Line 157 of the checker states the assumption out loud: **"All visible text uses
INK."** `scenes.py` uses MUTE for 60+ visible labels. The assumption stopped
being true and nothing noticed.

---

## The second root cause: absolute coordinates

`scenes.py` positions text with **86 hardcoded `move_to([x, y, 0])` calls**
against **9 `next_to`** and **7 `.arrange()`**. Type sizes cluster hard at
`sz=28` (35 uses) and `sz=36` (19 uses) — the signature of a floor-raising pass
that scaled every label up and left every coordinate where it was.

That is the whole bug class. Text got bigger; the layout didn't move. In a
coordinate-positioned scene there is nothing to absorb it.

---

## The six collisions, with the line that causes each

| Beat | What you see | Cause |
|---|---|---|
| **B07** | `PHOEBOSTON` | `ph_tag` at x = **−2.9**, `bo_tag` at x = **−1.8** — 1.1 units apart, both `caps(sz=28)`. "PHOENIX" alone is ~1.6 units wide at that size. |
| **B09** | terracotta arrow drawn through the word ENVIRONMENT | the `E(t)` label group sits at y = −0.9; the arrow starts at the group's *centre*, not below its bottom edge. |
| **B16** | headers ghosting through cells, `MODEL DOES WORK` running into `ANT BEHAVIOR` | `col_h1/col_h2` placed at `cell_h * 0.85` above grid origin — that is **inside the top row**, not above the grid. `row_h1/row_h2` at `−cell_w * 1.15` isn't clear of the left column. And the cells mix `caps(sz=36)` with `serif(sz=48)` — the serif cells overflow. |
| **B19** | `ELABORATE INTERNAL LOGIC` overruns its box and crosses the divider | bullet list is `.arrange(...).move_to([−3.2, 0.1, 0])` with no width constraint against a box of fixed width. Nothing clips it. |
| **B21** | Y-axis label clipped top and bottom | `y_lbl` at `sz=36` rotated — taller than the plot area it labels; positioned at x = −5.5 by hand. |
| **B23** | `…on's claim: …ch LEVEL OF DESCRIPTION explains the path` half-buried | `limit` serif at [4.0, −2.5] vs `return_lbl` at [−1.5, −2.8] and `odometer_lbl` at [2.5, 0.0] — three hand-placed blocks in one quadrant. |

The QuickTime scrubber in your B23 frame is your player, not a render defect —
ignore it.

---

## The fix order that actually holds

Fixing the six scenes first is the trap: the checker still can't see MUTE, so
nothing stops the seventh collision on the next reel.

1. **Fix the checker.** `ink_mask(INK) → ink_mask(INK) | ink_mask(MUTE)` in
   `check_bbox_overlap`, `check_min_size`, and the contrast check. Then re-run
   GATE T on this reel and read the *real* FAIL list — it will be longer than six.
2. **Fix the scenes against that list**, converting `move_to` to `next_to` /
   `.arrange()` / `VGroup` with buffers. Nudged coordinates re-break on the next
   type pass; relative layout doesn't.
3. **Add an overlap assertion inside the scene helpers**, so a collision fails at
   Manim build time rather than at your eyes.

---

# The bigger problem: the viewer doesn't know why they're watching

You're right, and it's a law violation, not a taste call.

`ai-explainer` **EXECUTIVE-SUMMARY LAW**: *"The beat immediately after the cold
open is ALWAYS a one-breath executive summary… The failure this law exists to
prevent is the near-universal one — diving from the intro straight into details,
so the viewer collects specifics with no scaffold to hang them on."*

Current spine:

```
B00  cold open — the ant hook
B01  "Act one. The beach."        ← segment card, not a BLUF
B02  the jagged path              ← detail beat
```

There is no Beat 2. The reel goes hook → act card → detail. And two things
never get established:

- **Who Simon is.** His name first appears at **B06**, ~1:40 in, as *"Simon
  performs the substitution himself"* — assuming the viewer already knows who
  that is and why his word counts.
- **Why this is about AI.** The first AI beat is **B16**, ~5:00 in. For five
  minutes the viewer is watching an insect.

Fix: one revised cold open + two new beats before B01. ~40 seconds, taking the
reel to about 9:20 — still inside the deep-explainer band.

### B00 — revised (name the stakes in the hook)

> An ant walking across a beach traces a path so jagged, so full of detours and
> backtracks, that anyone watching from above would conclude: that animal is
> solving a hard problem. That inference is wrong — and it is the same inference
> you make every time you watch an AI agent produce an impressive trajectory.
> Liam here, in for Professor Bear.

### B00A — WHO SIMON IS *(new)*

> The ant belongs to Herbert Simon. Nobel prize in economics, Turing Award, and
> one of the handful of people who founded artificial intelligence as a field.
> He put the ant in *The Sciences of the Artificial*, nineteen sixty-nine — not
> as a charming image, but as a claim he meant literally, about how to tell a
> system apart from the world it is walking through.

*Visual:* portrait plate or a redrawn title page; the three credentials set as
chips landing on their spoken names; the book year in terracotta.

### B00B — THE BLUF *(new)*

> Here is why that matters now. When an agent chains tool calls, recovers from a
> failure, and hands you a clean answer, you are standing on the dune looking
> down at the path. The question is which part of that performance is the model
> and which part is the scaffolding around it. Simon's parable gives you a test,
> and by the end of this you will be able to run it.

*Visual:* the beach path redrawn once as an agent trajectory — tool call, retry,
tool call, answer — same jagged shape, different labels. Then the two-axis
diagnostic appears for half a second and dissolves: the promise, not the payoff.

That second beat is the one doing the real work. It makes the ant a *diagram of
the agent* from the start, so every beat between here and B16 lands against a
whole the viewer already holds.
