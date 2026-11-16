# SOURCES — tldr-the-99-percent-test

**Source document.** `chapters/02-probability-uncertainty-and-the-confidence-illusion.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern University) — §"The test that is 99% accurate, and the patient it kills", §"Bayes' theorem — the bookkeeping made explicit" (the disease line and the term table), §"The false-positive structure is everywhere", Figures 2.5 and 2.6, Glimmer 2.3. Read whole 2026-09-23. Section S1 of `youtube/tldr-sections-02-probability-confidence.md`.

**Merge conflicts in the chapter.** The chapter carries six unresolved merge blocks. This film uses the HEAD side throughout; the only block it touches is at line 258 (HEAD carries the sensitivity/specificity precision note and the long Figure 2.5 caption; d78899b truncates the caption to "Population grid of 10,000 dots arranged as a"). Nothing in the film exists only on the d78899b side.

**Cited primaries (via the chapter).**
- Casscells, W., Schoenberger, A., & Graboys, T. B. (1978). Interpretation by physicians of clinical laboratory results. *New England Journal of Medicine*, 299(18), 999–1001.
- Wong, A., et al. (2021). External validation of a widely implemented proprietary sepsis prediction model in hospitalized patients. *JAMA Internal Medicine*, 181(8), 1065–1070. (The Epic Sepsis Model; named here, not in the film.)

**Executable evidence.** `make_sheet.py` recomputes every number with exact fractions and asserts it at import: 0.01 × 9,999 = 99.99; 1/101 = 0.0099; 0.000099 / 0.010098 = 0.0098039; the 98× lift; the exact 99× odds lift; the YOUR TURN coin-flip point (1 in 100 → exactly 0.5). `scenes.py` re-asserts the on-screen values.

**Pedagogical template.** `brutalist.art/skills/make/tldr/reference/pedagogy.md`.

**Corrections applied (DOUBLE-CHECK LAW).** The chapter prints the posterior two ways (≈ 0.0098 in prose, ≈ 0.0099 in the term table) without reconciling them; the film shows both and says why (the count lets the test catch the sick person for certain). "Sixty Harvard house officers, students, and attendings" is condensed to "sixty Harvard physicians and students". The Epic product name is kept out of the film.

**Seeds.** `BrutalistHesitantWriter.seed` = `tldr-the-99-percent-test`; `ClaudeTitleOutro.slug` = `tldr-the-99-percent-test`; the 100 lit false-positive squares in B16 are chosen by `random.Random("tldr-the-99-percent-test")` in `scenes.py`.

**Narration.** Liam, in for Bear — Kokoro `am_onyx`, synthetic, free, local. Disclosed in B00 and on the outro.

**Rights.** All visuals are original Manim/Remotion renders. No third-party media.
