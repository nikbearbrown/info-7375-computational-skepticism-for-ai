# SOURCES — tldr-hold-one-fair

**Source document.** `chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern University): §"Three definitions" (demographic parity, equalized odds, calibration parity and the values table), §"The arithmetic — the actual proof, not a gesture" (Bayes for PPV, the odds identity, the cross-group ratio, the two numeric tables), Figure 7.1 (HEAD caption, not rebuilt), Exercise 6 (BHTF). Read whole 2026-09-23. Section S1 of `youtube/tldr-sections-07-fairness-metrics.md`. Merge conflicts: the HEAD side of every block; nothing the film uses exists only on `d78899b`.

**Primary literature the chapter cites (not re-read for this film; the film makes no claim beyond the chapter's arithmetic).** Chouldechova, "Fair prediction with disparate impact," Big Data 2017; Kleinberg, Mullainathan, Raghavan, "Inherent trade-offs in the fair determination of risk scores," ITCS 2017; Hardt, Price, Srebro, "Equality of Opportunity in Supervised Learning," NeurIPS 2016.

**Executable evidence.** `make_sheet.py` and `scenes.py` recompute PPV, positive-prediction rate, base-rate odds and TPR/FPR for all five configurations (both chapter tables, group A's rates on group B) and assert the odds identity for each, the 2/7 cross-group coefficient, and the Exercise 6 base-rate odds.

**Pedagogical template.** `brutalist.art/skills/make/tldr/reference/pedagogy.md`.

**Corrections applied (DOUBLE-CHECK LAW).** None to the source. Presentation choices: the chapter's two tables are shown as two constructed settings, without the chapter's threshold labels (they do not reconcile; see BUILD-LOG manuscript notes). The chapter's "perfect prediction (t = 1, f = 0)" exit is shown as `f = 0` and spoken "no false alarms at all".

**Seeds.** `BrutalistHesitantWriter.seed` = `tldr-hold-one-fair`; `ClaudeTitleOutro.slug` = `tldr-hold-one-fair`.

**Narration.** Liam, in for Bear: Kokoro `am_onyx`, synthetic, free, local. Disclosed in B00 and on the outro.

**Rights.** All visuals are original Manim/Remotion renders. No third-party media.
