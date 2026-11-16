# BUILD-LOG — claude-liam-simons-ant

## Placement decision

**Standing rule established 2026-08-12:** Theorist material with a skepticism-about-capability
angle lives in `computational-skepticism-for-ai`. This is the third such reel (after
`claude-liam-chinese-room` and `claude-liam-computational-epistemology`). Bear confirmed this
pattern as the standing rule on 2026-08-12.

**Reasoning for this reel specifically:** Simon's ant parable is the origin document for the
attribution trap in AI — crediting capability to the mechanism that belongs to the terrain.
That is a core skepticism diagnostic, not an abstract philosophy exercise. The 2×2 diagnostic
(hold scaffolding/vary model vs. hold model/gut scaffolding) maps directly to the
computational-skepticism toolbox. The reel belongs here.

**External name policy:** Simon, Brooks, Wehner, and Cataglyphis are named in narration.
The rule against external names applies to software tool authors (from memory feedback
feedback_no_external_names.md). Scholarly attribution is required by the brief's fact-check
mandate — a reel about careful attribution cannot omit the name of the person being attributed.

---

## Session log — 2026-08-12

- **Beat sheet written:** 28 beats (B00–B24, BVDT, BHTF, BOUT). All body beats are MANIM.
  Bookend beats (B00, act-title cards, BVDT, BHTF, BOUT) are REMOTION.
- **Skill reclassification (2026-08-12, Bear decision):** `register` corrected from
  `"deep-explainer / documentary"` to `"ai-explainer"`. Basis: the `content_rules.no_pantry`
  "HARD RULE" was an authoring decision (not an oversight) that governs — zero pantry stills,
  zero VOX beats, every visual code-generated. The deep-explainer SKILL.md's own law says "a
  deep-explainer with 5% vox beats is an ai-explainer that skipped its pantry" — at 0% VOX
  this reel is an ai-explainer that is simply long (8:41, 7 acts). No beats change, no re-renders.
- **FACTCHECK.md written:** 8 claims evaluated. 3 VERIFIED, 3 FLAGGED (need external text
  access), 2 OMITTED from narration (scissors metaphor, satisficing chapter placement).
- **scenes.py written:** 17 Manim scene classes fully authored (not stubs).
- **Narration:** Teardown register throughout. All claims in narration are from the VERIFIED
  column of FACTCHECK.md or are described at a level of generality that does not require
  specific citation (e.g., "the two watchmakers parable" rather than citing page numbers).

## Gate state

- GATE P (PLAN): CLOSED — Bear approved 2026-08-12 ("go ... yes no_pantry hard rule an authoring decision that should govern")
- GATE T (TYPE-LOCK): PASS — 28 beats, 0 FAILs (run 2026-08-12)
- GATE V (VISUAL QC): PASS — 4 BLOCKERs found in full 2fps scan, all resolved and re-rendered
- Audio: generated (Kokoro am_onyx, all beats)
- art final: RAN — claude-liam-simons-ant.mp4 (521.2s, 2026-08-12)

## Standing order

Per STANDING ORDER — Slate Cut Gate (memory): build to slate cut (art run), STOP.
Write CHECKS-REPORT.md. Bear reviews. No art final / art post / 4K / TOPOST / publish.

---

## QC log (per beat — to be filled after renders)

| Beat | Frame extracted | Text bboxes | Intersections | Status |
|------|----------------|-------------|---------------|--------|
| B00 | _qc/beats/B00_mid.png | topic/title/greeting/output lines | none | PASS |
| B01 | _qc/beats/B01_mid.png | "The Beach" act title | none | PASS |
| B02 | _qc/beats/B02_mid.png | "VIEW FROM ABOVE — THE BEACH" title | none | PASS |
| B03 | _qc/beats/B03_mid.png | "THE FLAT TABLE — NO OBSTACLES" / "SAME RULE · SAME ANT" | none | PASS |
| B04 | _qc/beats/B04_mid.png | "THE BEACH" / "THE TABLE" column headers | none | PASS |
| B05 | _qc/beats/B05_mid.png | "The Thesis" act title | none | PASS |
| B06 | _qc/beats/B06_mid.png | quote + "THE 1969 TEXT" attribution | none | PASS |
| B07 | _qc/beats/B07_mid.png + B07_85.png | "Phoenix"/"Boston" tags + "SUNDIAL" label | **BLOCKER — ph_tag/bo_tag overlap sundial base rect (same y level)** | FIXED (see below) |
| B08 | _qc/beats/B08_mid.png | "The Formalism" act title | none | PASS |
| B09 | _qc/beats/B09_mid.png | equation labels M/E(t)/G + question | none | PASS |
| B10 | _qc/beats/B10_mid.png | H(B)/H(B|E) labels + body text | none visible (bottom text tight to rule — cosmetic) | PASS |
| B11 | _qc/beats/B11_mid.png | "The Simulation" (dark bg FormACard) | none | PASS |
| B12 | _qc/beats/B12_mid.png + B12_early.png | "ONE RULE…" banner + "DENSITY 0.0/0.4" tags | **BLOCKER — DENSITY tags at y=2.6 inside rule_text (bottom ≈2.54)** | FIXED (see below) |
| B13 | _qc/beats/B13_mid.png | "OBSTACLE DENSITY SWEEP" + "DENSITY: 0.00" + "NOTHING IN THE AGENT CHANGED" | none | PASS |
| B14 | _qc/beats/B14_mid.png | "The Fallacy" act title | none | PASS |
| B15 | _qc/beats/B15_mid.png | "The Ant Fallacy" + definition + terracotta question | none | PASS |
| B16 | _qc/beats/B16_mid.png + B16_late.png | 2×2 table with "VARY MODEL"/"VARY SCAFFOLD" headers | none confirmed (right-side header extends to edge by design) | PASS |
| B17 | _qc/beats/B17_mid.png | dark-bg warning card | none | PASS |
| B18 | _qc/beats/B18_mid.png | "Build Like Hora" act title | none | PASS |
| B19 | _qc/beats/B19_mid.png + B19_late.png | comparison columns + "AGENT: MINIMAL" box | **BLOCKER — agent_box (y=-0.85 top=-0.50) overlaps items_good "contract validators" (center y≈-0.78)** | FIXED (see below) |
| B20 | _qc/beats/B20_mid.png | watchmaker comparison + INTERRUPT labels | none | PASS |
| B21 | _qc/beats/B21_mid.png | cost chart + "TEMPUS"/"HORA" lines | none | PASS |
| B22 | _qc/beats/B22_mid.png | "The Limits" act title | none | PASS |
| B23 | _qc/beats/B23_mid.png + B23_early.png + B23_late.png | Cataglyphis path + "ODOMETER"/"SKY COMPASS"/"STRAIGHT RETURN" labels + "Simon's claim:" text block | **BLOCKER — 5-line limit text (sz=48, y=-1.8) overlaps compass_lbl and return_lbl** | FIXED (see below) |
| B24 | _qc/beats/B24_mid.png | "DESCRIPTION"/"EXCUSE"/"Who designed the obstacles?" | none | PASS |
| BVDT | _qc/beats/BVDT_mid.png | verdict artifact card 5 items | none | PASS |
| BHTF | _qc/beats/BHTF_mid.png | handoff composer + prompt | none | PASS |
| BOUT | _qc/beats/BOUT_mid.png | "The Parable of the Ant." + "@NikBearBrown" + mascot | none | PASS |

### GATE-V fixes applied — 2026-08-12

- **B07**: ph_tag moved from [-2.7,-0.65] → [-2.9,-0.95]; bo_tag from [-2.0,-0.65] → [-1.8,-0.95]; l_label from [-3.2,-1.1] → [-3.2,-1.55]
- **B12**: left_tag and right_tag moved from y=2.6 → y=2.1 (below rule_text bottom at y≈2.54)
- **B19** (two-pass fix): First pass moved agent_box y=-0.85→-1.16 (cleared items_good) but agent_box bottom at -1.51 clipped result_good top at -1.17. Second pass: expanded box_bad/box_good height 3.6→5.0 center -0.2→-0.5; moved result_bad/result_good from y=-1.5→-2.2; moved x_mark/check_mark from y=-2.1→-2.8; agent_box/agent_lbl moved to y=-1.34. All clearances ≥0.15 units.
- **B23** (full restructure): All diagram labels sz=36→sz=28 and repositioned — compass_lbl to [-2.0,0.4]; odometer_lbl to [2.5,0.0]; return_lbl to [-1.5,-2.8]; limit shortened to 3 lines at [4.0,-2.5]. No remaining collisions.

### art final — 2026-08-12

`art final` ran per Bear's STEP 5 authorization. Output: `claude-liam-simons-ant.mp4` (521.2s, 28/28 beats, all gates PASS). GATE-AUDIO mean −24.1 dB. STOP — no art post, no TOPOST, no publish.
