# SOURCES — tldr-average-hides-the-patient

**Source document.** `chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern University). Read whole 2026-09-23. The film uses:
- §"Subgroup calibration: where aggregate metrics lie": the subgroup table, the ECE_g formula, and the Epic Sepsis Model paragraph citing Wong et al. (2021);
- §"Expected Calibration Error: binning the predictions": the ECE formula;
- §"What calibration metrics cannot see": the construct-validity row;
- "Still puzzling": the deployment-halt threshold as a values question;
- exercise A5, for YOUR TURN.

The film follows section S2 of `youtube/tldr-sections-11-communicating-uncertainty.md`. All of the material used sits outside the chapter's seven merge-conflict blocks (the HEAD / d78899b figure-numbering conflicts), so no conflict side was needed.

**Primary behind the chapter's sepsis numbers.** Wong, A., et al. (2021). "External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients." *JAMA Internal Medicine* 181(8): 1065–1070. Only the chapter's reported figures are used (missed 1,709 of 2,552 septic patients). On screen the tool is "a widely used sepsis alert", with no product named.

**Illustrative table.** The subgroup table cites no dataset, so the film treats it as the chapter's illustrative table and captions it once on screen ("the chapter's illustrative table", B10). It is never tied to the sepsis model.

**Pedagogical template.** `brutalist.art/skills/make/tldr/reference/pedagogy.md`.

**Corrections applied (DOUBLE-CHECK LAW).**
- Pediatric flag. The chapter's table marks pediatric (0.029) as flagged, but its own rule (> 2 × 0.018 = 0.036) says it is not. The film applies the rule: three of five.
- Base rate. The printed global base rate 0.041 does not match the N-weighted rows (0.044), so no base rate is shown.
- Derived numbers. The film's own derivations (row share × gap, the ≤ 0.0073 bound, the 0.028 patient-weighted average) are marked "derived" in FACTCHECK.md.

**Seeds.** `BrutalistHesitantWriter.seed` = `tldr-average-hides-the-patient`; `ClaudeTitleOutro.slug` = `tldr-average-hides-the-patient`.

**Narration.** Liam, in for Bear: Kokoro `am_onyx`, synthetic, free, local. Greeting "Salaam" (Arabic/Farsi). Disclosed in B00 and on the outro.

**Rights.** All visuals are original Manim/Remotion renders. No third-party media.
