# Chapter 1 — figure notes and review

Illustration pass: 2026-09-10. Source: [The Skeptic's Toolkit](../chapters/01-the-skeptics-toolkit.md).

Eight original diagrams replace seven missing diagram assets and add a supervisory-capacities overview. PNGs are embedded in the chapter; matching SVGs retain editable text and embedded fonts. The portrait is a sourced archival photograph, not a generated likeness. Figure approval sidecars remain `verified: false`: technical checks are not human sign-off.

## Figure map and substance review

| Figure | Topic | Representation and guard against misreading |
|---|---|---|
| [1.1](../images/01-the-skeptics-toolkit-fig-01.png) | Cartesian inspection | A claim branches into coverage, inputs, and context checks. Passing one check is not universal assurance. |
| [1.2](../images/01-the-skeptics-toolkit-fig-02.png) | Hume's turkey | Schematic expectation curve, not measured probabilities. Expectation stays high across the surprise; no automatic detection is implied. |
| [1.3](../images/01-the-skeptics-toolkit-fig-03.png) | Three portable moves | Distinct questions and review artifacts. Kant's slice, the fourth move, follows in the next section (rebuilt 2026-10-15; the caption previously named Plato's Cave). |
| [1.4](../images/01-the-skeptics-toolkit-fig-04.png) | Artifact versus world | Redrawn 2026-10-15 around the chapter's two cases: the Netflix Prize (error predicting star ratings versus a member finding something to watch and staying) and the Amazon recruiting engine (resemblance to past résumés versus ability to do the job). A schematic of the cases, not captured results. It replaces the earlier email-deletion illustration. |
| [1.5](../images/01-the-skeptics-toolkit-fig-05.png) | Producing versus checking | Qualitative work comparison, not invented cost bars, a benchmark, or a claim that every AI task has the same cost ordering. |
| [1.6](../images/01-the-skeptics-toolkit-fig-06.png) | Five supervisory capacities | All five names match the chapter. Parallel responsibilities, not a mandatory sequence. Human decision ownership is explicit. |
| [1.7](../images/01-the-skeptics-toolkit-fig-07.png) | Fluency trap | Separates confidence in an answer from confidence in one's own review. Criteria and independent evidence interrupt the mechanism. No empirical effect size is asserted. |
| [1.8](../images/01-the-skeptics-toolkit-fig-08.png) | Team workflow | Prediction and limits come before execution. AI preserves evidence; a named human verifies and decides. Failed or unknown checks require revision or stopping. |

All eight depict conceptual relationships from the supplied manuscript. No new clinical statistics, incident timelines, benchmark results, observed agent runs, or quantitative cost estimates were generated. The generic bar-chart prompts at the chapter's end were replaced with prompts matching the actual diagrams. Suggested interactive HTML paths are clearly labeled as not yet built.

## Portrait provenance

- Asset: [karl-popper.jpg](../images/karl-popper.jpg), unmodified JPEG downloaded from Wikimedia Commons.
- Photographer: Franz Barta. Collection: LSE Library, accession IMAGELIBRARY/5. Date: circa 1980.
- [Source and rights statement](https://commons.wikimedia.org/wiki/File:Karl_Popper.jpg): no known copyright restrictions (Flickr Commons). This wording is preserved; it is not presented as a newly determined public-domain license.
- [Original image](https://upload.wikimedia.org/wikipedia/commons/4/43/Karl_Popper.jpg).
- Downloaded 2026-09-10. Dimensions: 600 × 769 pixels.
- SHA-256: `4df72b581196a6099f280ac44774026739fca9d1f47a4a2069235c1a51880b67`.
- The previous missing-image caption described an AI-generated portrait from the 1950s. It now describes the actual photograph and links its attribution.

## Rebuilding

The chapter-specific SVG source is [build_chapter01_figures.mjs](../scripts/build_chapter01_figures.mjs). It takes an output directory and a Brutalist `runtime/fonts` directory, embeds Inter and EB Garamond, and refuses to overwrite a human-verified SVG. The accompanying [renderer](../scripts/render_chapter01_figures.cjs) uses Playwright and installed Google Chrome to rasterize only this chapter's SVGs, waiting for embedded fonts and checking actual text bounds before writing PNGs. Supply the image directory as its argument. It refuses to overwrite human-verified PNGs. These are chapter assets, not modifications to the shared AI+1 tooling.

Embedded font license notices are included beside the figures: [Inter OFL](../images/01-figures-Inter-OFL.txt) and [EB Garamond OFL](../images/01-figures-EB-Garamond-OFL.txt).

## Technical checks

- All eight SVGs passed the shared AI+1 geometry audit: zero layout errors and zero warnings.
- Browser rendering waited for embedded EB Garamond and Inter; both fonts loaded in all eight figures. Actual rendered text bounds passed canvas and containing-box checks.
- All eight final PNGs and the portrait were visually inspected for clipping, legibility, hierarchy, and correspondence to their captions. Diagram PNGs are 3,750 pixels wide.
- Color is redundant with text, position, line style, and boundaries; no distinction depends on red versus green. The expectation curve is directly described and distinguishes a dashed prediction from preceding observations.
- Diagram content was reviewed separately from geometry using the conceptual constraints in the figure map above. Human approval remains outstanding.
- All nine chapter image embeds resolve locally and have descriptive alt text. Captions run consecutively from Figure 1.1 to 1.8. The three original conflict-marker regions are unchanged.
- JavaScript syntax checks and `git diff --check` passed. The course validator passed all 49 course-layer files (15 lessons and 10 assignments); this is not a factual certification of the manuscript.
- The root ignore policy initially excluded the entire image directory. A narrow Chapter 1 allowlist now includes only these SVGs, PNGs, portrait, approval sidecars, and font licenses; other images, media, large-file exclusions, and student-material exclusions remain intact.

## Scope and remaining manuscript issues

The source attachment matched the repository chapter byte-for-byte before this pass (SHA-256 `4367fa488e8de5525a54cc19ed4637fe477ba0161cbecd918281a1f4c87001fe`). The worktree was clean at inspection.

Three pre-existing merge-conflict regions remain: the Knight Capital passage, the DeGrave/COMPAS passage, and the closing AI Wayback Machine/Prompts block. The chapter's `AGENTS.md` says not to silently resolve manuscript conflicts. No branch content or conflict markers were removed. Only the image caption and figure-prompt material within the final disputed block was updated to match the actual assets.

This is an illustration and image-provenance review, not a complete fact-check of the existing prose. In particular, the cited Ash narrative and broad claims about model priors, automated verification, and clinical performance still require a separate source-based editorial review. The figures avoid turning those unreviewed assertions into apparent measured evidence. No course policies, exercises, student materials, or other chapters were changed. No publication or Git push was performed.

## Update 2026-10-15

The chapter was rewritten around the Netflix Prize and the Amazon recruiting engine. The three merge-conflict regions listed above are now resolved, keeping both sides, and the Ash and sepsis material is out of the chapter. Figures 1.3 and 1.4 were rebuilt (Kant's slice in place of Plato's Cave; Figure 1.4 redrawn around the two cases) and all eight PNGs were re-rendered from the same script. The layout audit found zero errors and zero warnings on both rebuilt SVGs, and the live-font check passed for all eight. Prompts for Figures 3, 6, 7 and 8 were added and the Figure 4 prompt rewritten. Figure approval sidecars remain `verified: false`. What was checked and what was not is in `chapters/_ch1-rewrite-factcheck.md`.
