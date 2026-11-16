# PEDAGOGY — claude-liam-bnb-02-loop-and-calibration

## Act structure
8-beat episode (B00–B04, BVDT, BHTF, BOUT). Cold open (B00) states the four-step loop in one pass and frames calibration as the instrument. B01 builds the reliability diagram from scratch — bins, axis, diagonal, over/underconfidence. B02 adds the three numbers (Brier, ECE, temperature scaling) and introduces the critical trap: in-sample ≠ good calibration. B03 applies Descartes and Hume as the two classical moves that generate the shifted re-plot prescription. B04 assembles the loop report, four fields, with the residual risk framing. BVDT restates all key rules. BHTF reads the full prompt with named brackets for artifact type, ten sample predictions, bins, and data source. BOUT closes.

## Cold open law
B00 delivers the loop in one sentence in the exact four-step order used throughout the series (predict → run → report → fix + residual risk). It frames calibration as a single yes/no question before giving any mechanics. No preamble about what calibration is in theory — opens with what the assignment requires.

## Gap formula
Gap: students know calibration as a concept but have never computed it on their own build's predictions, and have never re-plotted on a shifted slice. Bridge: reliability diagram computed from their own binned predictions, ECE and Brier as specific numbers, temperature scaling as a one-scalar fix. Close: the shifted-distribution re-plot distinguishes in-sample performance from deployment-environment performance — the gap most builds never close.

## Utility lint
Every formula is given in terms of operations students can execute: bin by stated confidence, compute fraction positive per bin, plot, compare to diagonal. ECE is defined as a weighted average. Temperature scaling is defined as dividing logits by T > 1 fitted on a held-out set. The "critical trap" (in-sample ≠ good calibration) is named explicitly and given a behavioral prescription: re-plot on a shifted slice. The four loop report fields are each distinguished by what goes in them — no field is vague.

## Vocabulary / register
**Reliability diagram** — the calibration plot; bins, axes, and diagonal defined in B01. **ECE (Expected Calibration Error)** — weighted average calibration error across bins; defined in B02. **Brier score** — mean squared error of probability estimates; defined in B02. **Temperature scaling** — dividing logits by scalar T > 1 to soften confidence; defined in B02. **Shifted-distribution re-plot** — re-computing the reliability diagram on a population slice different from training; defined in B02 and operationalized via Descartes/Hume in B03. **Four classical moves** — Descartes, Hume, Plato, Popper appear across E2–E4; Descartes and Hume are introduced here as the two questions that drive the shifted re-plot. **Residual risk** — what remains after the fix; defined in B04 and used in every subsequent episode.

## Honesty
The claim "overconfident tail is the usual finding" is accurate — it reflects the structural consequence of training on label-matching loss. The claim that Descartes and Hume produce the shifted re-plot prescription is operationally true in the sense that each question names one dimension of the re-plot design (the suspect bin and the population gap). The claim that temperature scaling cannot fix subgroup-varying calibration is accurate.

## Length law
8 beats (~463s estimated). B04 is the full loop-report assembly beat, which is new in E2 and longer than a typical body beat because it enumerates all four fields with examples. BHTF reads the full prompt with all named brackets and closes with two concrete next actions (compute ECE yourself; run the re-plot). Both are behavioral, not aspirational.

## Narration spot-check
B00 states the four-step loop in order. B01 correctly defines the diagonal as the perfect-calibration reference. B02 correctly states that temperature scaling is fit on a held-out set. B03 correctly derives the shifted re-plot from Descartes (suspect bin) and Hume (population gap). B04 correctly states that the prediction-lock goes in verbatim, not rewritten. BHTF explicitly instructs: "compute ECE yourself — do not report Claude's number as your result without verifying it on your actual data." The re-plot result, not the in-sample result, is named as the finding.

## Visual law
All Remotion. B00 uses ClaudeComposerAsk with three-item `output` array. B01–B04 use ClaudeWindow with `view: "artifact"`, six artifact lines per beat, and a ≤4-word spark line. BVDT uses ClaudeVerdictArtifact with five lines. BHTF uses ClaudeComposerAsk. BOUT uses ClaudeTitleOutro. Spark lines avoid lonely asterisks.

VERDICT: PASS
