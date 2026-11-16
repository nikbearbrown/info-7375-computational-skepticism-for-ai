# BUILD-LOG — claude-liam-dashboard-that-lied

## 2026-07-21 — authored + audio locked (Cowork session; deep-explainer episode 3)

- HUMAN NOTE (logged first): Bear — "next deep explainer" + his own
  published Chapter 1 ("The Dashboard That Lied", skepticism.ai,
  2026-03-16). Standing episode-1 process applies: agent builds and locks
  Liam audio while Bear shops; one Claude Code paste per pass; standing
  free-pipeline audio authorization = GATE P signature.
- OWNERSHIP DECISION: the chapter's home book is Living Models
  (Living-Models / living-models-book), but the deep-explainer series
  lives in computational-skepticism-for-ai/youtube/ per Bear's standing
  instruction ("build these deep-explainer videos here"). Built there;
  the reel is self-contained and can move wholesale if Bear reassigns it.
- Plan: 33 beats — B00 cold open + 28 body beats across six acts + closing
  block (B30 verdict / B31 your-turn / B32 title outro). Lane mix (body):
  vox 7 (25.0%) · manim 8 · remotion 7 · card 6 · ask 1 (exempt). Quota
  dead-center.
- Vox runs: R1 = B07→B08 (SALE tags tight → the whole promotional world,
  one plate), R2 = B23→B24 (trading screens tight → the unmanned floor,
  one plate). Handoffs authored at plan time.
- Audio: all 33 beats, Kokoro am_onyx via the toolkit's generator + model
  files. Locked total **7:32** (452.4s). timings.json is ground truth.
- Gate D2: SHOPPING.md — 5 files / 7 windows, ALL tier-1 generated (no
  rights escalations this episode; lightest shop of the three).
- Captions: claude-liam-dashboard-that-lied.srt (118 cues, source text on
  measured windows). description.txt drafted with chapters + a link back
  to the chapter post.
- FIRST-PARTY SOURCE RULES: the WAU story is narrated AS the chapter's
  teaching case (on-screen label), never as a named real company. External
  claims (JCP $4.3B / 17-month timeline, Knight $440M / 45 min, Pearl
  attribution) verify against independent sources at Gate F. No portrait
  of Judea Pearl (living person — mechanism over face).
- No code/ files this episode — the ask→result pair lands on a Manim DAG
  (B15), not a code block.

## Gate status

- [x] GATE F — FACTCHECK.md signed 2026-07-21. All 18 rows ✓ PASS. External: JCP ~$4.3B/17mo rounds to "eighteen months" ✓; Pearl do(·) from Causality 2000 ✓; Knight Capital $440M/45min via SEC File No. 3-15570 ✓. WAU rows verified against SOURCE.md only. No narration fixes → no audio regen.
- [x] GATE P — standing authorization (free pipeline).
- [x] Audio lock — 7:32; timings.json is the clock.
- [x] Gate D2 SHOPPING.md — written from locked durations; Bear shopping.
- [x] Gate D1 previz — PASS 1 COMPLETE 2026-07-21. Details below.
- [ ] Pantry fill / pass 2 / review cut / final — pending.

## HUMAN FEEDBACK — 2026-07-21

Bear: "Read brutalist-art/skills/make/deep-explainer/SKILL.md completely, then its reference/ files, then the parents it names. Standing rules #1–#4 in brutalist-art/EXAMPLES-CAMPAIGN.md govern. Free pipeline only, never publish. Reel: computational-skepticism-for-ai/youtube/claude-liam-dashboard-that-lied — Execute PASS 1 exactly as written in the reel's BUILD-PROMPT.md (Gate F close-out → scenes.py for the 8 named Manim scenes → SHOTLIST.md + PROMPTS.md → pattern-id reconcile vs Root.tsx → art run → VISUAL QC → report in BUILD-LOG.md and stop)."

---

## PASS 1 — Gate D1 previz — 2026-07-21

### What was built

**Gate F close-out:** All 18 factcheck rows signed ✓ PASS. FACTCHECK.md header
updated; BUILD-LOG Gate F line checked.

**scenes.py — 8 Manim scenes authored and rendered clean:**
All 8 scenes cleared GATE A (static coords) and GATE B (layout audit).

| Scene | What it shows | Terracotta accent | Issues resolved |
|---|---|---|---|
| B03_GreenLine | WAU +18% line chart | +18% chip | cite label "the chapter's case" → "J&J loyalty-program WAU case" (W7) |
| B04_VanishingDenominator | EU dots fade; ratio climbs | "felt like good news." period | — |
| B10_RemoveThePromos | Spikes deleted; expected↑ actual↓ | — | stroke_dasharray unsupported in Manim 0.20.1 → DashedVMobject; label-on-line → shifted labels UP/DOWN 0.25 |
| B12_DoOperator | P(Y\|X) vs P(Y\|do(X)); do() glows | do() terracotta MathTex | — |
| B13_CategoryBoundary | Tile shelf; do-arrow off shelf | — | n_tiles 6→5 + extra_tiles 3→2 (frame-coord fix); do_world_lbl buff 0.15→0.4; extra_tile labels removed (label-on-line) |
| B15_ConfounderDAG | Z→X severed; terracotta ring on Z | z_ring terracotta | z_sub UP buff 0.15→0.6 (label-on-ring); xy_arrow stroke_dasharray unsupported → removed |
| B17_TheLadder | 3-rung ladder; rung 3 highlight | rung 3 terracotta rect | — |
| B22_ConceptDrift | Regime shift; model extrapolates | — | model_lbl moved UP buff 0.45 from line (label-on-curve) |

**SHOTLIST.md** — 33-beat table with lane/medium/pattern/duration; lane quota
vox 25.0% ✓; vox-run continuity R1(B07–B08) R2(B23–B24) ✓; pattern ID
reconcile table included.

**PROMPTS.md** — 5 pantry image prompts (B02, B05, B07, B19, B23); B07/B23
at ≥2800px for vox-run Ken Burns; all Tier 1 generated.

**Pattern-ID reconcile vs Root.tsx:**
13 beat_sheet.json `shot.remotion.pattern` IDs corrected:
- SegmentCard → FluencySegmentCard (B01, B06, B11, B16, B20, B26)
- deckPatterns/divergence → FluencyDivergence (B09, B21)
- deckPatterns/scale → DtlScale (B18) — NEW reel-local component
- illustrations/ChipGrid → DtlChipGrid (B25) — NEW reel-local component
- illustrations/LayerStack → DtlLayerStack (B27, B29) — NEW reel-local component
- illustrations/SourceFlow → FluencySourceFlow (B28)

New file: `brutalist-art/runtime/remotion/src/DashboardThatLied.tsx` — three
reel-local components (DtlScale, DtlChipGrid, DtlLayerStack) with zod schemas.
Registered in `Root.tsx` under `<Folder name="DashboardThatLied">`.

**art run output:**
- All 8 Manim scenes rendered and slotted (B03 B04 B10 B12 B13 B15 B17 B22)
- Review cut: `claude-liam-dashboard-that-lied-slate.mp4` (452.4s = 7:32) ✓
- QC contact sheet: `qc-sheet.png` ✓

**Visual QC — all 8 Manim scenes PASS:**
- B03: axes, INK line, terracotta +18% chip in frame ✓
- B04: dot grid, "felt like good news." at bottom ✓
- B10: spike triangles + dashed expected line + actual below ✓
- B12: two equation cards, do() terracotta, chip under wrong side ✓
- B13: equation group top, tile shelf, do-arrow + "do-world" label ✓
- B15: DAG arrows, severed Z→X, terracotta ring on Z ✓
- B17: 3-rung ladder, rung 3 terracotta, "worlds that never existed" ✓
- B22: data points, model line, regime-shift dashed marker, "reality has left." ✓

### Warnings (non-blocking, logged for Bear)
- **B15 safe-area WARN x2**: `observe:` and `do(X):` labels left edge at
  x=-6.31 (safe area is ±6.3 — 0.01 outside). Pipeline slotted B15. Can tighten
  by changing `to_edge(LEFT, buff=0.8)` → `buff=0.85` if Bear wants clean green.
- **Motion histogram**: remotion=54% (18/33 beats) — over the ~40% guideline.
  Expected for PASS 1 previz; all 18 beats are slates awaiting Remotion fill in
  PASS 2. Resolves once Remotion and vox beats render.
- **SKIN LINT B00/B32**: ClaudeComposerAsk and ClaudeTitleOutro pattern
  annotations absent — expected (B00/B32 are still slates in PASS 1).

### State: stopped here per BUILD-PROMPT.md PASS 1 instruction.
Next: Bear fills pantry/ (5 images per SHOPPING.md + PROMPTS.md), then PASS 2.

---

## MISSING / open questions for Bear

- Standing pattern-id reconcile against Root.tsx at pass 1.
- Confirm the ownership decision (computational-skepticism-for-ai vs the
  Living Models book) before publish — playlist metadata currently says
  "Computational Skepticism for AI".

## PASS 2 TYPE-LOCK — 2026-07-24

§8.1–§8.4 form pass. No audio re-generated. No paid spend.

### Typecheck result
GATE T: **PASS** (0 FAILs, 33 beats checked)
Checked: 2026-07-24T09:27

### Final output
`claude-liam-dashboard-that-lied.mp4` — 450.5s (~7m30s), 13MB. Master locked. Never published.

---

## REVISION PASS — 2026-08-11 (new brief)

Reel revised to match the "hypothetical.ai / Living Models Ch. 1" brief.

**Placement conflict flagged to Bear**: reel lives in computational-skepticism-for-ai/
but the chapter's home book is living-models-book/. Proceeding in place; move
is a one-line directory rename whenever Bear decides.

**Chapter editorial note for Bear**: the chapter contains a near-duplicate paragraph.
The "even a fully realized prescriptive system falls short…" passage appears in both
the four-stages section and the Living Models section (§ on Living Model definition).
Not a factual error, but worth one editorial pass before a major print.

**Changes this pass:**

1. B02 narration: changed "The scene:" → "The chapter's illustrative case." per
   brief requirement to label the WAU story explicitly in narration.
2. B25 pattern: DtlChipGrid → DtlParallelLadder (new component). 2D maturity×causal-rung
   grid with WAU (Descriptive, Rung 1) and J.C. Penney (Prescriptive, Rung 1) plotted.
   This is the brief's "two-axis payoff diagram" showing "prescriptive ≠ causal —
   parallel climbs."
3. B28B (new beat): "Barriers to rung two" — three stacked walls (incentive structure,
   data architecture, comfort of precision). DtlLayerStack. Inserted between B28 and B29.
4. B31 (YOUR TURN): Replaced loyalty-program exercise with the observability two-question
   prompt: "which rung do your questions live on?" + "what would this dashboard do if it
   silently stopped measuring what you think it measures?" Points at Problem 1.5.
5. description.txt: Updated attribution to include Nik Bear Brown, Living Models Ch. 1,
   hypothetical.ai.
6. shot.remotion added to 17 beats that previously only had top-level remotion.pattern
   (needed for remotion_scenes.py to render them).
7. New Remotion component DtlParallelLadder added to DashboardThatLied.tsx + Root.tsx.
   Registered as DtlParallelLadder (16:9) + DtlParallelLadder916 (9:16). TEMPLATE-MISSES.md
   created at runtime/remotion/src/ with the registration record.

**Audio regenerated**: B02 (15.32s), B28B (24.09s new), B31 (20.12s). Total reel
duration increases from 452.4s to ~500s (~8m20s) with B28B added.

**GATE F**: existing 18 rows remain PASS. B28B introduces no verifiable factual claims
(editorial framing only). B31 new prompt references "Chapter Problem 1.5" — verified
as real in SOURCE.md.

**GATE T**: Previous PASS 2026-07-24 covers beats unchanged. B25 (DtlParallelLadder),
B28B (DtlLayerStack, barriers mode), B31 (ClaudeComposerAsk, updated command) need
visual QC after render.

---

## Library-first pantry fill pass — 2026-07-22

Library search (1,500 image stills, 566 SVG icons): 0 matches for any outstanding
SHOPPING.md slot. Library is an illustration/character collection, not editorial
stock — no genuine match for any of the 5 SHOPPING.md plates.

`art todo` run: todo.json / STATUS.md / ToDo.md refreshed.

**Key finding:** `pantry/` already contains all 5 SHOPPING.md plates as AI-generated
mp4 clips (B02, B05, B07, B08, B19, B23, B24 — sourced via Midjourney flux-kontext
on 2026-07-21). Pantry is pre-staged. No new files dropped this pass.

Next step (human): run `python3 brutalist-art/runtime/scripts/pantry.py
computational-skepticism-for-ai/youtube/claude-liam-dashboard-that-lied` to
intake those mp4s into media/, then PASS 2 (`art run`). Update SHOPPING.md
checkboxes ☐ → ✓ after intake. Full status in books/PANTRY-FILL-REPORT.md.
