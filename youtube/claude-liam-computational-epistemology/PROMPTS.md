# PROMPTS.md — claude-liam-computational-epistemology
# Pass 1 · 2026-07-21
#
# Generation prompts and archive trails for the 8 open pantry slots.
# Prompts are ready to paste into Higgsfield / FLUX / nano-banana-2.
# Tier 3 slots (B07, B27, B29) have no gen prompts — archive search ONLY.
# For all slots: supply CLEAN plates (no pre-stylizing; no vintage filters).
# The treatment pass (WARMONO or NATGEO) is applied at pantry intake.
# Required resolution floor is per-slot below; undersized plates go mushy.
#
# Drop files into pantry/ with the exact names given. Then run pass 2.

---

## B02 — The seminar room (Act I)
**File:** `pantry/B02.png` · Tier 1 · kenburns · 11.11s window

**Role in the reel:** "the classical apparatus lived in rooms like this one" —
serif labels 'trace · check · cohere' land over the image at 0.55.
Camera does a slow ease-out push-in toward the table, focus [0.50, 0.55].

**Floor:** ≥2000px long edge, 16:9-friendly landscape.

**GEN PROMPT:**
```
Wide interior of a 19th-century university seminar room, long oak table
covered with open books and loose papers, large slate chalkboard with
faint handwriting, tall windows with warm late-afternoon light, empty
chairs slightly pulled out as if a discussion just ended, documentary
photograph, natural muted color, eye-level, deep focus, no people, no
text overlays, no watermark.
```

**Archive alternatives (if preferred):**
- Library of Congress free-to-use: https://www.loc.gov/free-to-use/
- LOC search "university classroom 1900": https://www.loc.gov/search/?q=university+classroom+1900
- Wikimedia Commons: https://commons.wikimedia.org/w/index.php?search=reading+room+interior+19th+century

*If archival: flip `shot.source` to `archive` at intake and supply
`pantry/B02.source.txt` (URL · license · credit).*

---

## B07 — Edmund Gettier (Act II)
**File:** `pantry/B07.png` + `pantry/B07.source.txt` · **Tier 3 — NAMED PERSON**
kenburns · 11.76s window

**Role in the reel:** portrait hold as Liam describes the three-page paper
that wrecked the classical definition. Label 'Edmund Gettier · 1963' at 0.4;
terracotta ring at 0.8 on 'by accident'.
Camera: 1.6× push toward the eyes, focus [0.50, 0.38]. Floor: ≥1600px long edge.

**⚠ NO GEN PROMPT — archive search and rights check are yours.**
Cleared photographs of Gettier are scarce (he avoided publicity; most
circulating photos are late-20th-century with the photographer's rights).

**Search trail:**
- Wikipedia image → check its Commons file page for stated license:
  https://en.wikipedia.org/wiki/Edmund_Gettier
- Wikimedia Commons: https://commons.wikimedia.org/w/index.php?search=Edmund+Gettier
- UMass Amherst (his department): https://www.google.com/search?q=site%3Aumass.edu+Edmund+Gettier

**Authored fallback (narration unchanged — recommended):**
If nothing clears rights: supply the 1963 paper's first page as a clean plate.
"Is Justified True Belief Knowledge?", Analysis 23(6): 121–123.
DOI: https://doi.org/10.1093/analys/23.6.121
→ Tier 2 (journal scan; check the scan's own rights field).
→ Zero-rights fallback: re-typeset title card (Claude Code can build a
DOCUMENT plate if you say so — no rights issues at all).

**`pantry/B07.source.txt` REQUIRED** (URL · license · credit) regardless of
which path you take.

---

## B14 — The ledger (Act III · VOX run R1)
**File:** `pantry/B14.png` · Tier 1 · ONE plate serves B14 + B15 · 8.76s + 10.49s

**Role in the reel:** B14 holds tight on ink entries ('internalism — reasons
you can produce'); B15 eases OUT to reveal the full surrounding volumes
('externalism — a process with a record'). The zoom-out is the reveal.
Camera: starts 2.1× tight on entries, eases out to full frame.
Focus B14: [0.42, 0.50]. **Floor: ≥2400px long edge** (strictest floor; hard crop at the tight end).

**Composition requirement:** the open ledger must be surrounded by many
stacked worn ledgers (years of records made visible = the externalist point).

**GEN PROMPT:**
```
Antique accounting ledger lying open on a wooden desk, dense neat
handwritten ink entries in columns, surrounded by tall stacks of worn
leather-bound ledger volumes receding into shadow, warm overhead lamp
light, documentary photograph, overhead three-quarter angle, deep focus,
high detail, no people, no readable modern text, no watermark.
```

**Archive alternatives:**
- Commons: https://commons.wikimedia.org/w/index.php?search=ledger+handwritten+accounting
- The Met open access: https://www.metmuseum.org/art/collection/search?q=ledger
- LOC: https://www.loc.gov/search/?q=ledger+account+book

---

## B15 — Ledger wide (Act III · VOX run R1)
**No separate file** — uses the same `pantry/B14.png`.
The run's camera does both beats from the same plate.

---

## B22 — The string wall (Act IV)
**Files:** `pantry/B22-bg.png` + `pantry/B22-mid.png` · Tier 1 · parallax · 12.50s
*(Graceful degrade: single `pantry/B22.png` → kenburns at intake.)*

**Role in the reel:** "a conspiracy wall is perfectly coherent — every thread
supports every other thread." Wall drifts; string layer parallaxes over it
(ratio ~1:1.4); terracotta ring circles densest knot at 0.6.
Floor: ≥2200px wide EACH layer.

**Layer contract:**
- **B22-bg:** corkboard with pinned photos/cards/clippings — NO string.
- **B22-mid:** red string web ONLY, on transparent alpha, matching bg perspective.
  (Generate bg first; then prompt for the string layer "isolated on transparent
  background." Or generate flat + cut the string layer yourself.)

**GEN PROMPT (B22-bg — corkboard):**
```
Large corkboard densely pinned with photographs, index cards, and newspaper
clippings, moody side lighting, slight vignette, documentary photograph,
straight-on view, no string, no readable text, no people's identifiable
faces, no watermark.
```

**GEN PROMPT (B22-mid — string layer):**
```
Web of red yarn string stretched between push pins, many crossing lines
forming a dense network with one dense central knot, isolated on transparent
background, straight-on view matching a flat corkboard, photorealistic.
```

**Stock alternatives:**
- Pexels: https://www.pexels.com/search/conspiracy%20board/
- Unsplash: https://unsplash.com/s/photos/corkboard-investigation
  *(check each photo's own license page; Pexels/Unsplash permissive but read the specific entry; sidecar it either way)*

---

## B27 — René Descartes (Act V · VOX run R2 opener)
**File:** `pantry/B27.png` + `pantry/B27.source.txt` · **Tier 3 — NAMED PERSON**
kenburns → stays as bg layer in B28 · 10.03s window

**Role in the reel:** R2 opener; opens tight on the eyes, eases out, then the
SAME plate slides left at half opacity behind B28's synthetic grid.
Camera: 1.35× tight on eyes [0.50, 0.35], eases out.
Floor: ≥1800px long edge (must read well both tight and at 55% scale).

**⚠ NO GEN PROMPT — archive search and rights check are yours.**
The canonical image: the portrait after Frans Hals, in the Louvre. The
painting is 17th-century (public domain); what you're checking is the
DIGITIZATION's stated terms.

**Search trail:**
- Wikipedia lead image → its Commons file page for the license:
  https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes
- Wikimedia Commons: https://commons.wikimedia.org/w/index.php?search=Ren%C3%A9+Descartes+portrait+Frans+Hals
  *(Multiple scans available; prefer ≥2000px if offered.)*

**`pantry/B27.source.txt` REQUIRED** (URL · license · credit).

---

## B28 — The synthetic grid (Act V · VOX run R2)
**File:** `pantry/B28.png` · Tier 1 · cutout · 12.43s window

**Role in the reel:** "the demon shipped" — tiles spring up one by one
(staggered machine entrances) over the dimmed Descartes portrait from B27.
These are AI-generated faces of non-existent people — that IS the point.
Floor: ≥2000px. Clean regular grid required for the entrance stagger.

**GEN PROMPT:**
```
Grid of nine portrait photographs of people who do not exist, arranged
three by three with even gutters, neutral studio backgrounds, consistent
head-and-shoulders framing, subtle uncanny artifacts — slightly wrong ears,
asymmetric earrings, melted background details — muted natural color,
photorealistic, no text, no watermark.
```

**Alternative tiled build:**
Generate 9 separate synthetic faces → ask Claude Code to tile them.
Name them `pantry/B28-tile1.png` through `pantry/B28-tile9.png` and note it
in BUILD-LOG.md; the intake will composite them. One flat grid file is fine too.

---

## B29 — David Hume (Act V · VOX run R2 closer)
**File:** `pantry/B29.png` + `pantry/B29.source.txt` · **Tier 3 — NAMED PERSON**
cutout · 15.74s window

**Role in the reel:** Hume's portrait springs up beside the dimmed grid from
the B28 handoff frame; label 'David Hume · the problem of induction' at 0.5;
rightmost grid tiles fray on 'shifts' at 0.8. Preferred as a CUTOUT (figure
on transparent alpha) for the spring-up entrance; supply full painting and
intake will cut it — or pre-cut yourself.
Floor: ≥1600px on the figure itself.

**⚠ NO GEN PROMPT — archive search and rights check are yours.**
The canonical image: Allan Ramsay, 1766 (National Galleries of Scotland).
Painting is public domain; check the digitization's stated terms.

**Search trail:**
- Wikipedia lead image → Commons file page for license:
  https://en.wikipedia.org/wiki/David_Hume
- Wikimedia Commons: https://commons.wikimedia.org/w/index.php?search=David+Hume+Allan+Ramsay+1766
- National Galleries of Scotland (their own scan):
  https://www.google.com/search?q=site%3Anationalgalleries.org+David+Hume+Allan+Ramsay

**`pantry/B29.source.txt` REQUIRED** (URL · license · credit).

---

## Summary table

| Beat | File(s)                       | Tier | Method         | Notes                             |
|------|-------------------------------|------|----------------|-----------------------------------|
| B02  | pantry/B02.png                | 1    | Gen prompt ↑  | Seminar room; 16:9 landscape      |
| B07  | pantry/B07.png + source.txt   | 3    | Archive only  | Gettier; authored fallback avail  |
| B14  | pantry/B14.png (serves B15)   | 1    | Gen prompt ↑  | Ledger; ≥2400px; R1 plate         |
| B15  | (same as B14)                 | —    | —             | No separate file needed           |
| B22  | pantry/B22-bg.png + B22-mid   | 1    | Gen prompt ↑  | Two layers; degrade to one plate  |
| B27  | pantry/B27.png + source.txt   | 3    | Archive only  | Descartes; Frans Hals after; R2   |
| B28  | pantry/B28.png                | 1    | Gen prompt ↑  | Synthetic grid; uncanny faces     |
| B29  | pantry/B29.png + source.txt   | 3    | Archive only  | Hume; Ramsay 1766; cutout pref    |
