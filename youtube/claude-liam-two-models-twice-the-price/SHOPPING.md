# SHOPPING.md — Two Models, Twice the Price
## Updated 2026-07-29 (post-build) — NO NEEDED-ASSET items

**All 11 Manim scenes built and passing. Zero pantry needs.**

All 41 beats filled. 20 Manim + 21 Remotion/card. No stills, no gen-AI, no
archival photos needed. Audio: existing Kokoro am_onyx mp3s only.

Classes built: B02_ComparisonTable, B03_PriceRowReveal, B09_FootnoteChart,
B13_RoutingDiagram, B14_InferenceStack, B15_FallbackNode, B22_BlankEffortField,
B27_ReceiptVsSticker, B28_ReceiptDetail, B31_ComplianceFunnel, B32_ComplianceBinary.

---
## Prior planning notes (pre-build)

**[Original text preserved below — all items completed]**

**All 9 placeholder beats are MANIM work items — not pantry fills.**

Applying the concrete-noun trap rule: every beat below was mis-classified as a
generated still. The physical object named in narration is a rhetorical stand-in
for a data structure that must be drawn. Gen-AI images produce garbled numbers
and cannot honor the illustrative-labeling rule, so generation is disqualified.

---

## Beats requiring Manim scenes

### R1 — Comparison table run (B02 + B03)

**B02** `10.8s` — *the naive read — win-row count*
- Teaches: the temptation to count win-rows in a comparison table
- Visual: drawn two-column model comparison table (generic row labels, W/L/T results);
  terracotta circles animate onto winning rows one by one
- Manim class: `B02_ComparisonTable`

**B03** `10.6s` — *the price row pull-back*
- Teaches: the price row reveals the implicit argument (more wins justify the premium)
- Visual: same table; price row at the bottom fades in or slides up to be revealed;
  terracotta bracket or highlight draws around the price cell
- Manim class: `B03_PriceRowReveal`
- Can share table-building code with B02 (same structure, price row initially hidden)

---

### B09 — Launch chart with starred footnote

**B09** `11.4s` — *the footnote is the tell*
- Teaches: the footnote on a benchmark chart reveals variant contamination
- Visual: drawn illustrative bar chart (generic labels, bars at illustrative heights);
  star marker on one bar; footnote text fades in at the bottom; terracotta ring
  draws around the starred bar; caption "(illustrative — not real measurements)"
- Manim class: `B09_FootnoteChart`

---

### R2 — Inference stack run (B14 + B15)

**B14** `13.0s` — *server racks — inference infrastructure*
- Teaches: a production inference system is a stack (routers, safety filters, fallback),
  not a single model call; all components were inside the benchmark
- Visual: vertical stack diagram; labeled boxes top-to-bottom: "prompt" → "router" →
  "safety filter" → "model" → "fallback"; arrows between each box; drawn in INK
- Manim class: `B14_InferenceStack`

**B15** `11.6s` — *the fallback node*
- Teaches: part of the score came from the fallback node, not the model under test
- Visual: same stack diagram; "fallback" box highlights in terracotta;
  label beside it: "part of the score came from here"
- Manim class: `B15_FallbackNode`
- Share stack-building code with B14

---

### B22 — Spec sheet with blank effort field

**B22** `11.0s` — *the blank effort field*
- Teaches: a blank effort field is an argument, not an omission — the author chose
  the effort level that produced this result
- Visual: drawn form/table layout; rows for metrics (Score, Context, Latency, …);
  "Effort" row present but its value cell is visibly blank; terracotta ring draws
  around the blank cell; label "Effort: ——" in terracotta
- Manim class: `B22_BlankEffortField`

---

### R3 — Receipt vs sticker run (B27 + B28)

**B27** `13.1s` — *receipt beside price sticker*
- Teaches: the per-token price sticker is a very different number from the per-task
  receipt; the gap is where the cheaper model stops being cheap
- Visual: two objects side by side — (left) price tag shape with one number labeled
  "price/token (illustrative)"; (right) itemized receipt with line items:
  "input tokens", "retries", "verbosity overhead", "re-run cost"; total at the bottom
  labeled "(illustrative total)"; builds line by line
- Manim class: `B27_ReceiptVsSticker`

**B28** `12.7s` — *pan down the receipt*
- Teaches: retries, verbosity, re-runs each add cost; fewer retries = cheaper per task
  even at a higher token rate
- Visual: same receipt; camera shifts to lower portion; each line item gets a brief
  terracotta accent as narration names it
- Manim class: `B28_ReceiptDetail`
- Share receipt code with B27

---

### B32 — Compliance binary split

**B32** `12.7s` — *the compliance gate is binary*
- Teaches: for regulated sectors the compliance gate is binary; benchmark lead is
  exactly zero if you cannot deploy
- Visual: simple binary split — "CAN DEPLOY" box (INK, left) vs "CANNOT DEPLOY"
  box (terracotta, right); dividing line between them; under "CANNOT DEPLOY":
  "benchmark lead = 0" in terracotta
  (B33 then shows the full decision diamond — B32 is the binary concept setup)
- Manim class: `B32_ComplianceBinary`

---

## Implementation notes

- All scenes: BG=#FAF9F5, INK=#3D3929, ACC=#D97757, SOFT=#A9A491
- All bars / numbers labeled "(illustrative)" or "(illustrative — not real measurements)"
- No real model names, no real benchmark numbers
- B02/B03, B14/B15, B27/B28 share scene code (same base diagram, second beat highlights)
- beat_sheet.json changes needed per beat: `shot.type:"STILL"` + `source:"ai"` →
  `shot.type:"GRAPHIC"` + `source:"own"` + `graphic.manim` section;
  lane stays VOX (tracks pedagogical rhythm, not render engine)
