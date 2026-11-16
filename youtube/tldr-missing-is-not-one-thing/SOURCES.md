# SOURCES — tldr-missing-is-not-one-thing

**Source document.** `chapters/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern University) — §"The procedural EDA pass — what it sees, and what it structurally cannot", ¶**Missingness** and its footnote (Rubin 1976; Little & Rubin 1987); Figure 3.2 "Missingno-style matrix visualization" (caption; the image file is not in the book's `images/` folder — the figure is rebuilt from its caption, REBUILD LAW); the failure table row "Missing not at random (MNAR)"; ¶"missing-data assumption"; exercise 8. Read whole 2026-09-23. Section S2 of `youtube/tldr-sections-03-data-validation.md`.

**Cited primary (via the chapter).** Donald B. Rubin, "Inference and Missing Data," *Biometrika* 63(3):581–592, 1976, DOI:10.1093/biomet/63.3.581. Roderick J. A. Little & Donald B. Rubin, *Statistical Analysis with Missing Data*, Wiley, 1987.

**Constructed evidence.** `world.py` — a seeded, deterministic 50-row table (age, city, income) with three blank patterns of exactly 9 cells (18%): random (two draws), under-25 (9 of the 12 young rows, drawn at random within the band), top-9 earners; plus the study-dropout relabel. Every relation the film shows is asserted at import, and the direction claims are re-checked over 2,000 fresh random draws (`ROBUST`). No income value is shown or spoken.

**Pedagogical template.** `brutalist.art/skills/make/tldr/reference/pedagogy.md`.

**Corrections applied (DOUBLE-CHECK LAW).** None to the source. Framing choices: the chapter's "Rubin's 1976 taxonomy" is spoken as "Donald Rubin's work on missing data" and shown "after Rubin (1976)", because the chapter's own footnote says the three labels were consolidated in 1987. "missingno" is not named (tooling rotates; the chapter's own aging note).

**Seeds.** `BrutalistHesitantWriter.seed` = `tldr-missing-is-not-one-thing`; `ClaudeTitleOutro.slug` = `tldr-missing-is-not-one-thing`; `world.py` seeds 20260923 (ages) / 118 (incomes) / 28, 30 (random wipes) / 9 (under-25 draw) / 11 (city) / 99 (robustness).

**Narration.** Liam, in for Bear — Kokoro `am_onyx`, synthetic, free, local. Disclosed in B00 and on the outro.

**Rights.** All visuals are original Manim/Remotion renders. No third-party media.
