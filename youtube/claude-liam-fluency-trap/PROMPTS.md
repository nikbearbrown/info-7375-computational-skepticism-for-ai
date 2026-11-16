# PROMPTS — claude-liam-fluency-trap
# Beat-prefixed generation prompts for the five open pantry slots.
# From SHOPPING.md (Gate D2, written after audio lock).
# Drop each generated file into pantry/ with the exact filename shown.

---

## B02 — The School of Athens (R1 plate, serves B02 + B03)

**Target file:** `pantry/B02.png`
**Required sidecar:** `pantry/B02.source.txt` (scan URL · license · credit)
**Tier 2** (specific real object — famous artwork, public domain painting,
check the SCAN's stated rights)
**Floor:** ≥3000px wide (tight 2.0× Ken Burns push will reveal brush detail
at anything less)

**Sourcing path (preferred — real archive):**
Search Wikimedia Commons for the largest available scan of Raphael's
"The School of Athens" (1509–1511, Vatican):
  https://commons.wikimedia.org/w/index.php?search=School+of+Athens+Raphael

Take the file with the HIGHEST resolution offered (often 10k+ px, labeled
"Scuola di Atene" or similar). Record the Commons file URL, the license
field, and the attribution line from the file page in pantry/B02.source.txt.

**What to write in B02.source.txt:**
```
url: <commons file page URL>
license: <license field from the file page, verbatim>
credit: <attribution as listed, e.g. "Raphael / Vatican Museums / WIKIMEDIA">
retrieved: 2026-07-21
```

The PAINTING is PD; the SCAN may carry its own rights — read the file page's
"licensing" section verbatim. Most high-res Commons scans of public-domain
works are themselves PD or CC0 (the Bridgeman doctrine or explicit release),
but verify per the specific file.

**Camera plan:** Run R1. B02 opens tight at 2.0× on the central disputing
figures (Plato and Aristotle, center of the composition). B03 eases OUT to
the full fresco. Supply a scan wide enough that the 2.0× crop still resolves.

---

## B08 — The graded stack

**Target file:** `pantry/B08.png`
**Tier 1** (generic / illustrative — no specific real referent)
**Floor:** ≥2000px on the long edge

**Generation prompt (AI image tool — GPT Image 2, Higgsfield, or equivalent):**
```
Tall stack of student essays on a wooden desk, the top essay pulled
forward showing handwritten red-pen margin marks and a circled letter
grade, warm desk-lamp light from the upper left, documentary photograph
style, three-quarter overhead angle, deep focus, no readable full
sentences, no real names visible, no watermark, clean background.
```

**Stock alternative if AI gen is unavailable:**
  https://www.pexels.com/search/graded%20papers/
  https://unsplash.com/s/photos/essay-grading
(Read the specific photo's license page; if used, add pantry/B08.source.txt
with the photo URL and its license.)

**Camera plan:** Slow kenburns push toward the marked page, focus [0.45, 0.50];
a terracotta ring draws on the grade at t=0.85. Ensure the grade and margin
marks are in the upper portion of the image to survive the push-in crop.

---

## B13 — The typewriter evening

**Target file:** `pantry/B13.png`
**Tier 1** (generic)
**Floor:** ≥2000px on the long edge

**Generation prompt:**
```
Manual typewriter on a desk at night with a half-finished letter in the
platen, several crumpled draft pages scattered around it, single warm
desk lamp, wristwatch beside the machine, documentary photograph style,
shallow depth of field with the room falling to shadow, no readable text
beyond a few blurred lines on the page, no watermark.
```

**Real-archive alternative:**
Library of Congress free-to-use collection:
  https://www.loc.gov/search/?q=typewriter+letter+writing
(If used, add pantry/B13.source.txt with the LOC item URL and its
stated rights; LOC free-to-use items are PD or have no known copyright.)

**Camera plan:** Slow push toward the page in the platen, focus [0.50, 0.48].
"the price was the proof" serif label lands at t=0.6. Ensure the page in
the platen is near center-frame for the push-in.

---

## B26 — The flawless letter (R2 opener)

**Target file:** `pantry/B26.png`
**Tier 1** (generic)
**Floor:** ≥2000px on the long edge
**Visual family note:** B26 and B27 must read as the SAME visual family
(same paper texture, similar light quality) — generate or source them in
the same session if possible.

**Generation prompt:**
```
A crisp formal business letter lying on a modest kitchen table, reading
glasses resting beside it on the table, perfect typography with the
salutation line clearly visible, soft domestic morning light through
a window, documentary photograph style, slightly elevated angle, the
letter's text present but softly out of focus except the sharp salutation
line at the top, no bank or company logos, no watermark.
```

**Camera plan:** R2 run. B26 opens tight at 1.7× on the letter's salutation
(focus [0.50, 0.45]). Ensure the salutation is in the upper third of the
image. B27 must be from the same visual family — generate both in the same
prompt session or source them as a matched pair.

---

## B27 — The flood of paper (R2 closer)

**Target file:** `pantry/B27.png`
**Tier 1** (generic)
**Floor:** ≥2400px wide (the wide-end reveal carries this beat)
**Visual family:** MUST match B26's paper / light / documentary feel.
Generate in the same session as B26 for consistency.

**Generation prompt:**
```
An institutional office desk buried under overflowing stacks of identical
crisp formal letters, canvas mail sacks leaning against the desk spilling
envelopes, one letter centered on the blotter matching a domestic formal
letter, cool institutional overhead light with a warm desk lamp, documentary
photograph style, wide angle from desk height, no readable text on any
letter, no logos, no watermark.
```

**Real-archive alternative (period mailroom):**
Library of Congress:
  https://www.loc.gov/search/?q=congressional+mail+room
(If used, pantry/B27.source.txt required with LOC item URL + rights.)

**Camera plan:** B27 continues R2 from B26's handoff — camera eases OUT
from one letter to a room full of them. Supply a wide image with the desk
and letters filling the frame so the ease-out has room to travel.
"cheap to send · expensive to answer" label + terracotta underline at t=0.7.

---

## Status

- [ ] B02 (+source.txt) — rights check required (Tier 2)
- [ ] B08
- [ ] B13
- [ ] B26
- [ ] B27

All five files must land in `pantry/` before pass 2.
Pass 2 runs after all five are supplied (or "ship with slates" override
logged in BUILD-LOG.md per SHOPPING.md lifecycle).
