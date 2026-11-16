# SHOPPING.md — claude-liam-computational-epistemology (Gate D2, v2)

Written after audio lock (Kokoro am_onyx; total **8:19** — `mp3/timings.json`
is ground truth). All assets are STILLS — no motion clips this episode.
Drop files into `pantry/` with the exact names below, then run pass 2
(the intake conforms, treats, and renames; only changed slots rebuild).

How to read an entry: the locked beat window and camera plan set the
resolution FLOOR (Ken Burns crops into the image — undersized stills go
mushy at the tight end). GEN PROMPT is ready to paste into your generator
(Higgsfield/FLUX/nano-banana). SOURCES are real-archive starting points —
search links, so they can't rot. Tier 2/3 rights checks are YOURS, every
time: read the specific image's stated rights, not the institution's vibe.
The treatment pass (desaturate ~80%, contrast, cream seat, grain) is applied
by the machine — do NOT pre-stylize generations to look "vintage"; supply
clean plates.

Restoration presets (toolkit stock-styles): WARMONO for period/archival
plates, NATGEO for modern ones — applied at pantry intake, not at
generation.

---

## ☐ B02 — the seminar room (Act I) · VOX kenburns · window 11.11s

- **File:** `pantry/B02.png` · **Tier 1** (generic — no rights escalation)
- **Camera:** slow ease-out push-in toward the table, focus [0.50, 0.55].
  **Floor: ≥2000px long edge**, 16:9-friendly landscape.
- **Role in the beat:** "the classical apparatus lived in rooms like this
  one" — serif labels 'trace · check · cohere' land over it.
- **GEN PROMPT:**
  "Wide interior of a 19th-century university seminar room, long oak table
  covered with open books and loose papers, large slate chalkboard with
  faint handwriting, tall windows with warm late-afternoon light, empty
  chairs slightly pulled out as if a discussion just ended, documentary
  photograph, natural muted color, eye-level, deep focus, no people, no
  text overlays, no watermark."
- **REAL-ARCHIVE ALTERNATIVES (free/PD candidates):**
  - Library of Congress free-to-use sets: https://www.loc.gov/free-to-use/
  - LOC search "university classroom 1900": https://www.loc.gov/search/?q=university+classroom+1900
  - Wikimedia Commons search: https://commons.wikimedia.org/w/index.php?search=reading+room+interior+19th+century
  - If archival is used: `shot.source` flips to `archive` at intake and
    `pantry/B02.source.txt` (URL · license · credit) is REQUIRED.

## ☐ B07 — Edmund Gettier (Act II) · VOX kenburns · window 11.76s

- **File:** `pantry/B07.png` · **Tier 3 — NAMED PERSON — rights check is yours**
- **Camera:** 1.6× push toward the eyes, focus [0.50, 0.38].
  **Floor: ≥1600px long edge.**
- **THE PROBLEM:** cleared photographs of Gettier are genuinely scarce
  (he avoided publicity; most circulating photos are late-20th-century and
  under the photographer's rights — the PHOTOGRAPH's term governs, not the
  subject's).
- **SEARCH TRAIL:**
  - Wikipedia article (check the image's file page + license):
    https://en.wikipedia.org/wiki/Edmund_Gettier
  - Wikimedia Commons: https://commons.wikimedia.org/w/index.php?search=Edmund+Gettier
  - UMass Amherst (his department; obituary press photos, ask/verify):
    https://www.google.com/search?q=site%3Aumass.edu+Edmund+Gettier
- **AUTHORED FALLBACK (narration unchanged — recommended if nothing clears):**
  supply a clean plate of the 1963 paper's first page instead —
  "Is Justified True Belief Knowledge?", *Analysis* 23(6): 121–123.
  DOI landing page: https://doi.org/10.1093/analys/23.6.121
  That flips the entry to Tier 2 (journal scan) — check the scan's rights
  field; a re-typeset title card is the zero-rights fallback of the
  fallback (Claude Code can build it as a DOCUMENT plate if you say so).
- **Sidecar REQUIRED either way:** `pantry/B07.source.txt`.

## ☐ B14 — the ledger (Act III) · VOX kenburns · ONE plate serves B14 + B15 (run R1) · windows 8.76s + 10.49s

- **File:** `pantry/B14.png` (one file — the run's camera does both beats)
- **Tier 1** · **Camera:** starts 2.1× tight on the ink entries (focus
  [0.42, 0.50]), eases OUT to full frame revealing stacked volumes.
  **Floor: ≥2400px long edge** — the tight end is a hard crop; this is the
  strictest floor on the list.
- **Composition requirement:** the zoom-out must REVEAL something — the
  open ledger surrounded by many stacked, worn ledgers (years of records =
  the externalist track record made visible).
- **GEN PROMPT:**
  "Antique accounting ledger lying open on a wooden desk, dense neat
  handwritten ink entries in columns, surrounded by tall stacks of worn
  leather-bound ledger volumes receding into shadow, warm overhead lamp
  light, documentary photograph, overhead three-quarter angle, deep focus,
  high detail, no people, no readable modern text, no watermark."
- **REAL-ARCHIVE ALTERNATIVES:**
  - Commons: https://commons.wikimedia.org/w/index.php?search=ledger+handwritten+accounting
  - The Met open access: https://www.metmuseum.org/art/collection/search?q=ledger
  - LOC: https://www.loc.gov/search/?q=ledger+account+book

## ☐ B22 — the string wall (Act IV) · VOX parallax · window 12.50s · TWO layers

- **Files:** `pantry/B22-bg.png` + `pantry/B22-mid.png` · **Tier 1**
- **Camera:** layers drift at different rates (parallax ratios ~1 : 1.4);
  terracotta ring lands on the densest knot. **Floor: ≥2200px wide EACH.**
- **Layer contract:** bg = corkboard with pinned photos/cards/clippings,
  NO string. mid = the red string web ALONE on transparent alpha, matching
  the bg's perspective. (Generate bg first, then ask for the string layer
  "isolated on transparent background" — or generate one flat image and
  cut the string layer yourself.)
- **GEN PROMPT (bg):**
  "Large corkboard densely pinned with photographs, index cards, and
  newspaper clippings, moody side lighting, slight vignette, documentary
  photograph, straight-on view, no string, no readable text, no people's
  identifiable faces, no watermark."
- **GEN PROMPT (mid):**
  "Web of red yarn string stretched between push pins, many crossing
  lines forming a dense network with one dense central knot, isolated on
  transparent background, straight-on view matching a flat corkboard,
  photorealistic."
- **Graceful degrade:** if layering is a pain, supply ONE flat
  `pantry/B22.png` — the beat downgrades to kenburns at intake (logged).
- **Stock candidates:** https://www.pexels.com/search/conspiracy%20board/ ·
  https://unsplash.com/s/photos/corkboard-investigation (check each
  photo's license page; Pexels/Unsplash licenses are permissive but read
  the specific page; sidecar it either way).

## ☐ B27 — René Descartes (Act V, run R2 opener) · VOX kenburns · window 10.03s · ALSO B28's background layer

- **File:** `pantry/B27.png` · **Tier 3 — NAMED PERSON — rights check is yours**
- **Camera:** opens 1.35× tight on the eyes (focus [0.50, 0.35]), eases
  out; then the SAME plate slides left at half opacity behind B28's grid.
  **Floor: ≥1800px long edge**, and it must read well both tight and small.
- **THE CANONICAL IMAGE:** the portrait after Frans Hals (Louvre). The
  painting is 17th-century — public domain everywhere; what you're
  checking is the DIGITIZATION's stated terms.
- **SEARCH TRAIL:**
  - Wikipedia lead image → its Commons file page carries the license:
    https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes
  - Commons search: https://commons.wikimedia.org/w/index.php?search=Ren%C3%A9+Descartes+portrait+Frans+Hals
  - Prefer the highest-resolution Commons scan (several exist; take
    ≥2000px if offered).
- **Sidecar REQUIRED:** `pantry/B27.source.txt` (URL · license · credit —
  the credits block builds from it).

## ☐ B28 — the synthetic grid (Act V, run R2) · VOX cutout · window 12.43s

- **File:** `pantry/B28.png` · **Tier 1** (no real people — that's the point)
- **Camera:** tiles spring up one by one (machine staggers entrances), so
  a clean regular grid matters. **Floor: ≥2000px.** Alpha not required.
- **GEN PROMPT:**
  "Grid of nine portrait photographs of people who do not exist, arranged
  three by three with even gutters, neutral studio backgrounds, consistent
  head-and-shoulders framing, subtle uncanny artifacts — slightly wrong
  ears, asymmetric earrings, melted background details — muted natural
  color, photorealistic, no text, no watermark."
- **Alternative build:** generate 9 separate synthetic faces and tell
  Claude Code to tile them (it can — then each tile's entrance is a real
  layer). Drop them as `pantry/B28-tile1.png` … `-tile9.png` if you go
  that way and note it; otherwise one flat grid is fine.

## ☐ B29 — David Hume (Act V, run R2 closer) · VOX cutout · window 15.74s

- **File:** `pantry/B29.png` · **Tier 3 — NAMED PERSON — rights check is yours**
- **Camera:** Hume SPRINGS UP beside the dimmed grid per the R2 handoff —
  a CUTOUT (figure on alpha) is preferred. Supply the full painting and
  let the intake cut it, or pre-cut it yourself. **Floor: ≥1600px on the
  figure itself.**
- **THE CANONICAL IMAGE:** Allan Ramsay's 1766 portrait (National
  Galleries of Scotland). Painting is public domain; check the
  digitization's terms.
- **SEARCH TRAIL:**
  - Wikipedia lead image → Commons file page for license:
    https://en.wikipedia.org/wiki/David_Hume
  - Commons search: https://commons.wikimedia.org/w/index.php?search=David+Hume+Allan+Ramsay+1766
  - NGS collection (their own scan + stated terms):
    https://www.google.com/search?q=site%3Anationalgalleries.org+David+Hume+Allan+Ramsay
- **Sidecar REQUIRED:** `pantry/B29.source.txt`.

---

## Not yours (machine lanes — pass 1 builds these while you shop)

All Manim beats (B06 B08 B11 B12 B17 B20 B23 B25 B31 B33 B35), all
Remotion beats (bookends, act cards, patterns, code blocks), the three
`code/` files, and the slate previz. The 8 slots above render as labeled
slates until your files land — the previz is watchable regardless.

## Status

- [ ] B02 · [ ] B07 (+source.txt) · [ ] B14 · [ ] B22-bg · [ ] B22-mid ·
  [ ] B27 (+source.txt) · [ ] B28 · [ ] B29 (+source.txt)
- Review cut waits on all-checked OR an explicit "ship with slates"
  override logged in BUILD-LOG.md.
