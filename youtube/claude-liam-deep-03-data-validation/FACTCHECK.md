# FACTCHECK — claude-liam-deep-03-data-validation

**Gate F not yet run.** This file pre-stages the claims that need verification before GATE P, per DOUBLE-CHECK LAW and the deep-explainer "unverified-source caution" rule. The source chapter is a *rough draft* that carries its own `[verify]` flags and a chapterization comment; it opens with an explicitly-labeled **composite** case. Treat every number as unconfirmed until checked against the primary source, not against the chapter. (The chapter's HTML comment / merge-style header is authored metadata, not narration — read the HEAD prose.)

| Claim in narration | Beat | Verdict | Note |
|---|---|---|---|
| Opening deployment case (three-system join, subpopulation dropped) | B00, A1V, A1M, A1R | VERIFY (framing) | Chapter **explicitly labels this a composite**, "not a single sourced incident" (`[verify]` at chapter line 12). Narration keeps it as an illustration of a mechanism and must not present it as a real, sourced incident. |
| Specific figures "79,400 rows / 85,000 / four percent" | A1M | **SOFTENED** | These are the chapter's composite illustration, not empirical claims. Narration says "eighty thousand" once (cold open, clearly illustrative) and "a few percent" — the precise 4%/79,400/85,000 figures are omitted from narration to avoid presenting a composite as fact. Keep omitted. |
| Rubin's MCAR / MAR / MNAR taxonomy | A2M | HOLDS | Rubin, "Inference and Missing Data," *Biometrika* 63(3):581–592, 1976. MNAR = missing depends on the value itself; standard imputation biases in the unmeasurable direction — field-standard. |
| Cleveland & McGill: position/length outrank area/color | A3M | VERIFY → HOLDS | Cleveland & McGill, *JASA* 79(387):531–554, 1984. The perceptual-accuracy ranking is the load-bearing citation; confirm ordering wording. Stevens 1957 is a *bridge*, not load-bearing — kept out of narration. |
| Pearson captures only linear; y=x² correlates ≈ 0 | A3M2 | HOLDS (math) | Standard identity; safe. On-screen r ≈ 0 for a symmetric parabola. |
| IQR rule Q1−1.5·IQR / Q3+1.5·IQR | A2R (on-screen list) | HOLDS | Standard box-plot/Tukey criterion. Mentioned only as a diagnostic name. |
| Email-agent boundary leak (surfaces references / non-consenting parties, no access control violated) | A5V1–3 | VERIFY | Chapter attributes the mechanics to the "Ash" agent case in *Agents of Chaos* (Shapira et al., cited as arXiv:2602.20021 — a forward-dated preprint; **confirm the citation exists and the pattern before publication**). Narration presents it as a documented red-teaming *pattern*, not a cited paper, and does not name the paper/model — matches the chapter's own hedge. |
| "Reference-rich data isn't bounded by its schema" | A5V3, BVDT | HOLDS (bounded) | Chapter bounds the claim to a spectrum — sharp at the email end, near-absent at the sensor-log end. Narration keeps it to "reference-rich data," not a universal law. |
| Datasheets for Datasets — "57 questions" | — | OMITTED | Gebru et al., *CACM* 64(12):86–92, 2021 (arXiv:1803.09010). Chapter cites "57 questions"; the specific count is omitted from narration to avoid an unconfirmed figure. Argument (a checklist instrument exists) retained implicitly, not named on screen. |
| Plato's cave / Hume's induction framings | A5M, A4R2 | HOLDS | Classical/philosophical framing used analogically, as the chapter does. |
| Six structural assumption categories | A4R, A4M, A4R2 | HOLDS | Drawn directly from the chapter's own table (sampling, time-window, label, MNAR, feature-engineering, access/boundary). |

**Datable material stripped (DOUBLE-CHECK LAW):** no tool/vendor version numbers, no named data-quality libraries (Great Expectations / Deequ / missingno kept only as generic mechanism where unavoidable — narration says "the missing-value check," not a product), no "as of <month>" claims. The chapter's own "tooling ages" section is honored by narrating questions, not tools.

**Chapter `[verify]` flags carried into VERIFY here:** composite-case label (line 12), Great Expectations/Deequ scope note (line 241 — not narrated), Agents of Chaos citation (line 154).
