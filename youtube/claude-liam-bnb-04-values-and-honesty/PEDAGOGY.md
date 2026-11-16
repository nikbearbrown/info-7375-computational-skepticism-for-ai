# PEDAGOGY — claude-liam-bnb-04-values-and-honesty

## Act structure
8-beat episode (B00–B04, BVDT, BHTF, BOUT). Cold open (B00) names three instruments and makes the "these are engineering, not ethics" argument immediately. B01 covers bias and fairness: causal graph, leverage analysis, at least two fairness metrics, and the impossibility shown on the student's own numbers. B02 covers visualization honesty: two charts from the same data, deceptive only via encoding. B03 covers the verb audit and three-layer document, closing with Popper inward. B04 assembles the loop report with the verb-audit-specific residual risk framing. BVDT restates all rules. BHTF reads the full verb audit prompt with a hostile-reader closing question. BOUT closes.

## Cold open law
B00 makes an argument before giving mechanics: the "these feel like ethics but they are engineering" framing is structural justification for the three instruments that students are most likely to skip or treat superficially. The concrete examples (good accuracy, bad fairness parity; chart that hides distribution; over-reaching verb) are specific enough to be self-diagnostic before the student has done anything.

## Gap formula
Gap: students conflate "passed the accuracy check" with "evaluated the build." Bridge: three instruments targeting failures orthogonal to accuracy — group-level parity, visual encoding, and epistemic verb licensing. Close: Popper inward requires the student to state a falsifiable condition before running any further analysis, converting the audit from a post-hoc exercise into a prediction.

## Utility lint
Fairness metrics are defined by their decision-level meaning, not their equations: demographic parity = equal positive-prediction fraction; equalized odds = equal TPR and FPR; calibration parity = equal probability accuracy. The impossibility is shown "on your numbers, not as a theorem" — this is a critical distinction that prevents students from citing the impossibility theorem as an excuse not to compute. Encoding deceptions are named specifically (truncated axis, distribution-hiding aggregation, cherry-picked window, asymmetric color). The verb taxonomy is given in order (hypothesize through prove) with the evidence threshold for each level described in B03.

## Vocabulary / register
**Leverage graph** — the causal diagram plus leverage analysis marking where bias enters the pipeline; defined in B01. **Fairness impossibility** — the theorem, operationalized as showing on your actual numbers that the three metrics cannot all hold simultaneously; defined in B01. **Verb taxonomy** — the eight-level ordering from hypothesize to prove; defined and applied in B03. **Three-layer document** — plain sentence, technical sentence with method and confidence, reproducibility appendix; defined in B03. **Popper (classical move)** — the fourth classical move: state a falsifiable condition in advance; introduced in B03. Completes the set with Descartes (E2), Hume (E2), and Plato (E3).

## Honesty
The "encoding alone is enough to mislead" claim is accurate — truncated axes and distribution-hiding aggregations are the two most common visual deceptions in published research, both pure encoding choices. The warning "if you find yourself changing numbers to make version two more dramatic, you have crossed into fabrication" is clear and necessary. The verb taxonomy ordering from hypothesize to prove is not universal in all disciplines, but the ordering given (weakest to strongest epistemic claim) is defensible and pedagogically useful for the purpose of identifying over-reach.

## Length law
8 beats (~481s estimated). Three instruments in one episode makes this the most content-dense episode in the series. B03 is long (76s) because it covers both the three-layer document and the full verb taxonomy in one beat. The trade-off is justified: the verb audit and the three-layer document are both about the same thing (epistemic licensing of claims) and belong together.

## Narration spot-check
B00 correctly states: "these are the instruments most students skip because they feel like ethics instead of engineering. They are engineering." B01 correctly frames the impossibility as "on your specific numbers, not as a theorem." B02 correctly states the honesty floor: "the deception in version two comes only from encoding." B03 correctly defines the Popper condition as stated "before running any instrument." BHTF correctly closes: "the hostile-reader answer is your Popper condition."

## Visual law
All Remotion. B00 uses ClaudeComposerAsk with three-item `output` array. B01–B04 use ClaudeWindow with `view: "artifact"`, six artifact lines per beat, and a ≤4-word spark line. BVDT uses ClaudeVerdictArtifact with five lines. BHTF uses ClaudeComposerAsk. BOUT uses ClaudeTitleOutro.

VERDICT: PASS
