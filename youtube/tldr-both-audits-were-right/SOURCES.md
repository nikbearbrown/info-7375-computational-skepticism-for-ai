# SOURCES — tldr-both-audits-were-right

**Source document.** `chapters/06-bias-where-it-enters-and-who-is-responsible.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern University) — the HEAD side of every merge-conflict block. Read whole 2026-09-23. Load-bearing spans: §"The dataset as epistemic artifact" — the COMPAS paragraphs (ProPublica's error pattern; Northpointe's within-bucket calibration; "Both analyses were correct"), the plain-language 30% / 50% sketch, the identity v/(1−v) = p/(1−p)·t/f and the "unless p_a = p_b or t = 1, f = 0" condition, "not a data quality problem … a theorem", "a values claim", the re-arrest paragraph; the fairness-criterion table; exercise W3. Section S3 of `youtube/tldr-sections-06-bias-where-it-enters.md`.

**The chapter's own citations for the case and theorem** (named in FACTCHECK.md, not re-verified against the primaries here): Angwin, Larson, Mattu, Kirchner, "Machine Bias," ProPublica, May 23, 2016; Chouldechova 2017; Kleinberg, Mullainathan, Raghavan 2016.

**Nature of the key case.** The COMPAS dispute is real and is narrated at the chapter's level of detail (direction of the error pattern, no rates). The forty dots are CONSTRUCTED: 20 per group at the chapter's base rates with a two-box calibrated score of our own design (high → 60%, low → 20%). Captioned "constructed · 20 per group" on screen. All derived rates are recomputed with exact fractions in `make_sheet.py` and `scenes.py`.

**Framing boundary.** Chapter 7's tldr card "Hold One Fair, Watch the Other Break" (built in parallel) works the same theorem from the CHOICE side (pin one criterion, watch the other move; which to choose). This film stays on the AUDIT side: two correct audits of one tool, each read as a denominator; the choice is named only as the boundary.

**Corrections / rewrites (DOUBLE-CHECK LAW).** None to the source's numbers. The identity is presented as holding per group (true for any binary classifier), with "hold v equal" made explicit — see the manuscript note in FACTCHECK.md.

**Seeds.** `BrutalistHesitantWriter.seed` = `tldr-both-audits-were-right`; `ClaudeTitleOutro.slug` = `tldr-both-audits-were-right`.

**Narration.** Liam, in for Bear — Kokoro `am_onyx`, synthetic, free, local. Greeting: Filipino "Kumusta". Disclosed in B00 and on the outro.

**Rights.** All visuals are original Manim/Remotion renders. No third-party media.
