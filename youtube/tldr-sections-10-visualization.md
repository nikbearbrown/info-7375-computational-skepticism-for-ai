# tldr sections — Chapter 10: Visualization Under Validation: Honest, Misleading, and the Choices Between

Source: `chapters/10-visualization-under-validation-honest-misleading-and-the-choices-between.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 6 sections · 0 deferred · course film: carries the course credit (bookloop exception)

Numbers below are copied from the chapter as written. The chapter is a flagged rough draft (header comment: "Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved"): three `[verify]` flags and four unresolved git conflict blocks (`<<<<<<< HEAD` … `>>>>>>> d78899b`, chapter-10 vs chapter-11 numbering on Figures 10.1–10.3 and the closing sections). Flags are carried into the cards; whichever film builds re-verifies at `factcheck`.

Already on this chapter, different genre: `claude-liam-deep-10-visualization` (deep-explainer, "The Chart Isn't Neutral. It's Arguing.", ~9m20s plan) and the chart-lie scout reels `claude-liam-cs-18-chart-lie` / `claude-liam-vox-chart-lie` / `vox-chart-lie` (vox/scout register). A tldr film is additive: one aha, taught 3b1b-style, not a walk of the chapter.

Ranked by how visible the representation already is in the source (worked exercises with numbers first; the schematic case last).

## S4 · Where the Axis Starts                                          tier: single-insight
- question:        Same two accuracies, same chart type — why does one bar look three times the other?
- key case:        Exercise 1: y-axis 91%–96%; Model A 92.1%, Model B 94.3%; B's bar reads "roughly three times the height" of A's (computed from the exercise's values: on a 91 floor the bars are 1.1 and 3.3 units, 3.0×; on a zero floor, 92.1 and 94.3, 1.02×)
- naive:           "every number on the chart is true, so the chart is honest" — the numbers ARE true; the ratio the eye reads is not
- representation:  two bars held at fixed values while the axis floor slides from 91 down to 0; the bar heights change, the printed numbers never do; a second slide of the floor UP shows the same effect in stock-price data where it is legitimate
- abstraction:     visual ratio = (B − floor) / (A − floor): the floor is a design choice; truncation has an honest use (a genuinely narrow range, a quantity with no meaningful zero) and a dishonest one, and the pixels look the same either way — the choice is the difference
- boundary:        inconsistent axes ACROSS panels (Exercise 3: 70–100 / 85–100 / 60–100, "the three groups look about the same") → YOUR TURN; the rest of the nine-item catalog is named, not taught
- terms (prereq):  bar chart, baseline / axis floor, accuracy as a percentage
- equations:       visual ratio = (B − floor)/(A − floor)                          ← one TANGENT
- predict beat:    "Where does the floor have to sit for B to look exactly twice A?" before the floor moves (answer from the chapter's values: 89.9)
- source span:     §"The deceptive visualization catalog" (truncated axes; inconsistent axes across panels); §"The trade-off, stated plainly"; Exercises 1, 3, 7; Figure 10.1 (table stub)
- status:          built → tldr-where-the-axis-starts (master 2026-09-23 15:05, verdict pending)

## S6 · Zero at the Top                                                tier: single-insight
- question:        A murder chart that shows a drop after the law passed — and the murders went UP. How is the chart still "accurate"?
- key case:        Reuters, Florida Stand Your Ground, 2014 (Christine Chan): firearm murders 521 (2005) → 740 (2006) → 825 (2007), drawn on a y-axis with zero at the TOP, so the post-2005 spike renders as a decline (Bergstrom & West, *Calling Bullshit*, 2020, ch. 7)
- naive:           "the axis is labeled, the numbers are right, the reader should have read the axis" — technically correct; the reader takes away the opposite of the data
- representation:  the same polyline drawn zero-at-bottom (a rise), then the axis flips 180° about its midline and the identical points now read as a fall; the three labelled values ride along unchanged; beside it, an "error rate" vs "accuracy" panel where the flip is one column-name away
- abstraction:     truncation amplifies a real effect; inversion reverses one — two different deceptions; the orientation of the axis is a structural claim about which direction is "good", so state the direction-of-better in the title
- boundary:        why convention (zero at the bottom, more-is-up) is itself a learned reading, not a law; the Challenger case (contested diagnosis) → BOUNDARY line only; YOUR TURN: flip a metric dashboard's error-rate axis and write the title that would still make it honest
- terms (prereq):  line chart, y-axis orientation, "direction of better"
- equations:       none
- predict beat:    "Before the flip — with zero at the top, does 825 sit above or below 521?"
- source span:     §"Four cases that teach the catalog" (Reuters Florida 2014); the four-case table; §"Chapter summary"
- status:          pick

## S5 · The Median Hides the Tail                                      tier: single-insight
- question:        "Median latency is fine" — so why are three percent of users waiting eight seconds?
- key case:        Exercise 2: a validation report headlines median latency; the distribution is right-skewed with a tail to 8 seconds for roughly 3% of requests (the chapter gives no median value — the median tick is drawn as a labelled marker, its number left unstated, not invented)
- naive:           one number summarizes the column; "median performance is good" ends the review
- representation:  a histogram whose median marker stays PINNED while the right tail is pulled out to 8 s and the 3% mass slides into it — the summary statistic invariant while the shape underneath changes; a second instance where the same median hides a bimodal split (the chapter's box-plot warning)
- abstraction:     aggregation that hides distribution — a mean or median is a choice of what to show; when the tail holds the catastrophic cases, hiding it is not summarization, it is concealment; a box plot can hide bimodality, so add the strip plot underneath when shape matters
- boundary:        which spread technique to reach for (box / violin / strip — the technique menu is S1's territory and the deep-explainer's); YOUR TURN: write the two sentences Exercise 2 asks for, then name the single chart that would have shown the tail
- terms (prereq):  median, distribution / histogram, right-skew, tail
- equations:       none
- predict beat:    "If I double the tail to 6% of requests, does the median move?" before the mass slides
- source span:     §"The deceptive visualization catalog" (aggregation that hides distribution); §"Showing the range" (box plot / violin / strip plot watch-fors); Exercise 2
- status:          pick

## S2 · The Tie That Looked Like a Lead                                tier: single-insight
- question:        45.3% versus 44.5% — the chart shows a winner. Is there one?
- key case:        El País Catalonia poll, 2014: 45.3% "no" vs 44.5% "yes", margin ±2.95% — a 0.8-point difference inside a 2.95-point margin, drawn as two bars of visibly different height. **[verify]** carried from the chapter: primary source (the actual graphic and its date) not found; the chapter has seen the case told two incompatible ways (a 0.8-point tie as two bars vs a truncated axis amplifying a "5-point lead") and keeps it only as an *illustrative construction* of uncertainty-exceeding-effect. The card inherits that status: the film must say "illustrative" on screen or swap in the chapter's own Figure-10.2 pair (94.3% bold + thin bar vs "91–97% accuracy (95% CI)")
- naive:           draw the two numbers as two bars; the taller bar wins; the margin goes in a footnote
- representation:  two bars, then the ±2.95 interval grows out of each until the whiskers overlap and the 0.8 gap sits entirely inside either interval; then the visual-weight move — the bold central number shrinks and the interval thickens until the two are the same ink weight (Figure 10.2's left→right)
- abstraction:     when the margin exceeds the effect, the chart is a story about noise: make the interval visually larger than the effect or replace the chart with the sentence "it's a tie"; make uncertainty visually equal in weight to the estimate; round the estimate to the precision the interval supports (0.847291 ± 0.05 is 0.85)
- boundary:        WHERE the uncertainty belongs (prominent / caption / appendix — the disclosure hierarchy, Figure 10.B) — one line, the hostile-reader test; aleatoric vs epistemic is S3; YOUR TURN: Exercise 7 (93% ± 2% vs 81% ± 9%) — build the version that hides the intervals, then the one that shows them
- terms (prereq):  margin of error / confidence interval, point estimate, "effect size" as the gap between two numbers
- equations:       none (the tie is arithmetic: |45.3 − 44.5| = 0.8 < 2.95, no tangent)
- predict beat:    "Grow the intervals — do they overlap?" before the whiskers extend
- source span:     §"Uncertainty has two faces" (the poll sentence); §"Showing the range" (equal visual weight; avoid false precision; Figure 10.2 stub); §"Showing the trust" (when uncertainty is too large, do not visualize; hierarchy of disclosure); §"Four cases" (El País, flagged)
- status:          pick

## S1 · Twenty Dots, Four Filled                                        tier: standard
- question:        Why does "4 of these 20 dots" land with a hospital committee when "20% chance" does not?
- key case:        Exercise 5: a 20% probability of model failure for a hospital committee with no statistical training — shown as a percentage with a CI bar, then as a quantile dotplot: twenty dots, four filled. Second instance: Gigerenzer's natural frequencies — "9 out of 10 women with breast cancer test positive; 99 out of 1,000 women without breast cancer also test positive" produces correct reasoning where "90% sensitivity, 9.9% false-positive rate" does not; the chapter gives the base rate as roughly 8 in 1,000 and the posterior as "near 8%", and says the exact phrasing varies across Gigerenzer's papers (the arithmetic on the quoted numbers does not close cleanly to 8% — factcheck before it is spoken)
- naive:           print the number bigger; add decimals; add an error bar — the reader still has to do percentage arithmetic in their head
- representation:  the same 20% encoded four ways on one stage — a pie wedge (angle), a bubble (area), a bar (length), and 20 dots with 4 filled (position + count) — then the Cleveland–McGill ladder assembles beside them, position at the top, colour at the bottom, and each encoding slides to its rung; the dot plot is the only one a reader can *count*
- abstraction:     (1) the perception hierarchy: position on a common scale > length > angle/slope > area > volume > colour — when the answer is quantitative and precision matters, encode as position or length; (2) natural frequencies beat percentages for comprehension, and the quantile dotplot is that finding drawn: position-based, count-based, no percentage arithmetic. **[verify]** carried: the chapter could not confirm the specific per-channel error percentages against Cleveland & McGill (1984) — the ORDERING is the durable result; the film shows the ladder, never the percentages
- boundary:        the rest of the technique menu (bands, fan charts, HOPs, gradient lines) and the hurricane-cone misreading — named as the deep-explainer's territory; YOUR TURN: Exercise 5's two displays, plus "redraw one pie chart from your own work as a dot plot"
- terms (prereq):  probability as a proportion, visual channel / encoding, dot plot
- equations:       none (the hierarchy is an ordering, not an equation; no tangent)
- predict beat:    "Rank these four encodings by how accurately you can read 20% off them" before the ladder assembles
- source span:     §"Step two: the perception hierarchy" (Figure 10.A stub); §"Showing the range" (strip plot; quantile dotplot; the "useful default"); Exercise 5
- status:          pick

## S3 · A Map of News Stories                                          tier: single-insight
- question:        The map says "kidnapping rates". Why is it actually a map of headlines — and how would you ever tell?
- key case:        Cairo's GDELT Nigeria case: a FiveThirtyEight map of Nigeria "kidnapping rates" built from GDELT, which counts media mentions, not events; the spike tracked Boko Haram coverage; no disclosure of the proxy appeared on the chart (Cairo, "Ethical Infographics," IRE Journal, 2014). No numbers in the chapter — the case is schematic
- naive:           "the data came from a database, so the chart is data" — validate before you visualize was skipped; the chart carries the full visual authority of ground truth because it looks like every other chart
- representation:  a decomposition drawn as a pipeline — event → news story → GDELT row → map cell — with the identical schematic map at the end; the title swaps from "Kidnappings" to "News-story counts about kidnappings, 1985–2014" and nothing else on the map changes; then the source line moves from below the frame to INSIDE it (title = question, subtitle = answer, source line = warrant)
- abstraction:     epistemic uncertainty — the gap between the proxy and the thing — has practices, not error bars: validate the proxy first, name it in the title, put the source line inside the chart, disclose the methodology choices; "it's not true just because it's on a map" (Erin Simpson via Cairo)
- boundary:        aleatoric uncertainty and its technique menu (S1/S2); the full seven-step working sequence (Figure 10.2); YOUR TURN: take one chart from your own work and rewrite its title so it names the proxy, then judge whether the chart survives
- terms (prereq):  proxy, source line, aleatoric vs epistemic (the two-face split is the SHIFT here, not a prereq — TERMS holds "proxy" only)
- equations:       none
- source span:     §"Uncertainty has two faces"; §"Showing the trust — techniques for epistemic uncertainty" (validate before you visualize; disclose the source inside the chart; disclose what the data does not measure); working-sequence step 3
- status:          pick  (note: schematic Nigeria outline on cream; no chapter numbers to animate — ranked last for that reason)

## Not sectioned (by design)
- "Two dashboards built from one CSV" (the opener) and Glimmer 10.1 — the build-both-versions exercise is practice, and it is the deep-explainer's Act I; here it feeds the YOUR TURN of S4 and S2 (Exercise 7's 93% ± 2% / 81% ± 9% pair).
- "The medium is the message" (McLuhan) — an assertion with no case of its own; it is every card's SHIFT sentence ("the pixels are the same, the argument changed"), not a section.
- "Step one: the question the chart is answering" / the FT nine question-families and Abela's four — a lookup table (Figure 10.0), not a puzzle; nothing moves. A reading.
- The Living Deck — a process practice (dated versions, changelog slide); no chart to animate; and the chapter's own Figure 10.1 for it sits inside a git conflict block.
- Challenger 1986 — **not-yet-sectionable**: the chapter flags two incompatible diagnoses (poor *encoding* of data that was present vs *omission* of the untested cold region), commits to Tufte's encoding reading in the prose, then its own four-case table describes the omission reading ("omitted the cold-temperature region … Y-axis truncation"). Until the prose and table agree, any Manim would be choosing a diagnosis the chapter has not. A BOUNDARY line in S6 only.
- Snow's cholera map 1854 (the counter-case: show ALL the pumps) — no data in the chapter and the chapter itself footnotes the map as post-hoc argument, not instrument; a BOUNDARY line for S3 ("missing baselines"), not a section.
- Hurricane cone of uncertainty, HOPs, gradient lines, fan charts, the backfire effect — technique catalog; named in S1's BOUNDARY.
- "Why this chapter is load-bearing", "What would change my mind", Synthesis, Connections forward, Exercises, Chapter summary, the LLM Exercise (Agentic Red-Team Casebook), AI Wayback Machine (Du Bois), Prompts — back matter and course scaffolding.

## Multi-act candidates (need explicit approval)
- S4+S2 on Exercise 7's single pair (93% ± 2% vs 81% ± 9%): the two bars from S4 stay on screen, S4's BOUNDARY ("now add the intervals") is S2's HOOK, and one ~7–9 min film "Same Bars, Two Arguments" walks truncation → interval weight on one persistent object. Legal under the sectioning exception only because the key case is shared; it would displace the Catalonia case (and its `[verify]` flag) entirely, which is arguably a gain. Default remains two films.
- S4+S6 ("truncation amplifies, inversion reverses") share the abstraction but NOT the key case — not eligible for multi-act; two films.

## Chapter flags carried (for whoever builds)
- `[verify]` ×3: Cleveland–McGill per-channel error percentages (S1 — show the ordering only); El País Catalonia primary source (S2 — say "illustrative" on screen or swap to the Figure-10.2 pair); "verify current scope of domain-specific visualization standards" (back matter, not in any card).
- Four unresolved git conflict blocks (`<<<<<<< HEAD` / `>>>>>>> d78899b`), chapter 10 vs chapter 11 numbering on Figures 10.1, 10.2, 10.3 and the "Preview of next chapter" paragraph; the AI Wayback Machine and Prompts sections exist only on the d78899b side.
- Challenger: prose (encoding failure, Tufte) and table (omission / truncation) disagree — see Not sectioned.
- Gigerenzer numbers as quoted (9 of 10; 99 of 1,000; ~8 in 1,000; ~8% posterior) do not close arithmetically as written; the chapter says "roughly" — S1 carries them as a second INSTANCE only.
- Typo: "Sankov and alluvial diagrams" (Sankey) in the Flow family.
