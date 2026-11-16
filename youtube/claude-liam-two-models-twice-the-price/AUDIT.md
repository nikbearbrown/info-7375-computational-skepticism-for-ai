# AUDIT.md — Two Models, Twice the Price
## Pilot fix session — 2026-07-29

Reel: `claude-liam-two-models-twice-the-price`

This audit documents the 11 violations found and the before → after change for each.

---

## Violation log (11 beats rewritten)

| Beat | Before | After | Violation class |
|------|--------|-------|-----------------|
| B02 | STILL · source:ai · kenburns "comparison table with rows and ticks" | GRAPHIC · Manim · `B02_ComparisonTable` — 9-row comparison table with header, win/loss marks per row, ACC circles on win cells, animated row-by-row reveal | gen-AI still → drawn data graphic |
| B03 | STILL · source:ai · kenburns "comparison table, price row highlighted" | GRAPHIC · Manim · `B03_PriceRowReveal` — same table rebuilt quickly, then price row pulled down with ACC bracket; "price ≠ winner" label | gen-AI still → drawn data graphic |
| B09 | STILL · source:ai · kenburns "bar chart, one bar starred footnote" | GRAPHIC · Manim · `B09_FootnoteChart` — 3 bars (Task A/B†/C), ACC ring on the footnoted bar, footnote text below | gen-AI still → drawn diagram |
| B13 | FormACard "The routing diagram" (narration names it) | GRAPHIC · Manim · `B13_RoutingDiagram` — vertical 5-node flow (prompt→router→safety filter→model) with CurvedArrow (ACC) showing fallback reroute when flagged | withheld show (FormACard naming a diagram) → Manim diagram |
| B14 | STILL · source:ai · kenburns "server racks in a datacenter" | GRAPHIC · Manim · `B14_InferenceStack` — vertical stack (prompt / router / safety filter / model / fallback), FadeIn + GrowArrow sequence, caption "every component has a policy" | concrete-noun trap (server racks = inference stack) → drawn stack diagram |
| B15 | STILL · source:ai · kenburns "cable routing junction" | GRAPHIC · Manim · `B15_FallbackNode` — same stack, INK ring around fallback group, annotation "part of the score came from here" with ACC arrow | concrete-noun trap (cable junction = fallback node) → drawn stack + highlight |
| B22 | STILL · source:ai · kenburns "blank paper form" | GRAPHIC · Manim · `B22_BlankEffortField` — 5-field spec form (Score/Context/Latency/Effort level/Pricing tier), Effort row shows DashedLine instead of value; INK ring draws around it; "Effort: ——" label | concrete-noun trap (blank form = missing data field) → drawn spec form |
| B27 | STILL · source:ai · kenburns "price sticker and receipt side by side" | GRAPHIC · Manim · `B27_ReceiptVsSticker` — divider line; LEFT: price-tag shape with "$X.XX (illustrative)"; RIGHT: 4 receipt lines building (input tokens / retries / verbosity / re-run cost); ACC bracket + total label | concrete-noun trap (receipt = per-task cost breakdown) → drawn data graphic |
| B28 | STILL · source:ai · kenburns "detailed receipt close-up" | GRAPHIC · Manim · `B28_ReceiptDetail` — same 4 receipt items start SOFT; ACC highlight bar moves down row by row as each item is called out; total separator + "TOTAL ≠ price/token × tokens" | concrete-noun trap (receipt = itemized cost) → animated drawn diagram |
| B31 | FormACard "The compliance funnel" (narration names it) | GRAPHIC · Manim · `B31_ComplianceFunnel` — funnel shape (three trapezoid bands, narrowing) with "all models → compliant subset → deployable" labels; arrow + "capability analysis starts here" annotation | withheld show (FormACard naming a funnel) → Manim diagram |
| B32 | STILL · source:ai · kenburns "locked records room" | GRAPHIC · Manim · `B32_ComplianceBinary` — vertical divider; LEFT: "CAN DEPLOY" + sub-label; RIGHT: "CANNOT DEPLOY" in INK, "benchmark lead = 0" | concrete-noun trap (locked room = binary compliance gate) → drawn gate diagram |

---

## Kept as-is (not touched)

- B00 (ClaudeComposerAsk bookend), BVDT (title card), BHTF (opening), BOUT (ClaudeTitleOutro)
- B01, B07, B12, B18, B23, B30, B34, B37 (act-divider / aphorism text cards — legit sparing cards)
- B04, B06, B08, B11, B17, B21, B24, B29, B35 (existing Remotion beats — no violations)
- B05, B10, B16, B19, B20, B25, B26, B33, B36 (pre-existing Manim scenes — already clean)

---

## GATE T fix log (ACC-text-on-cream violations found in rendering)

After initial render, GATE T found 6 ACC-as-text violations in new scenes. Root causes:

1. **ACC used as Text color on cream** — `color=ACC` in Manim `Text()` objects: fixed in B09 (footnote), B13 (flag_label + node labels via `node()` helper), B15 (note text), B22 (blank_label), B28 (highlight text), B32 (right_lbl, right_sub) → all changed to INK
2. **ACC SurroundingRectangle boxes detected as text blobs** — at 4K, a rectangular outline with w/h between 1.5–15 passes all text-run filters. Fixed in B15 and B22 by changing ring `color=ACC→INK`; fixed in B13 and B15 by changing fallback node box `stroke_color=ACC→INK`
3. **font_size=20 below floor** — `flag_label` in B13 rendered at 28px physical < 34px floor at 4K. Fixed: font_size=20→26

All 6 contrast violations resolved across builds 9–12. GATE T PASS (41/41).
