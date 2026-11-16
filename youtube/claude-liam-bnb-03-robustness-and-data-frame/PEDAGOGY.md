# PEDAGOGY — claude-liam-bnb-03-robustness-and-data-frame

## Act structure
8-beat episode (B00–B04, BVDT, BHTF, BOUT). Cold open (B00) frames two instruments targeting two distinct hiding places: the model (robustness probe) and the data (data-frame audit). B01 builds the probe suite — three required probes, with agent-system additions. B02 gives the features-not-bugs three-question framing for each break. B03 constructs the data-frame audit: Gebru's five questions plus six-step epistemic-frame reconstruction, with MNAR as the key concept. B04 applies the Plato classical move and requires the one sentence. BVDT restates all rules. BHTF reads the full prompt with the proxy-feature probe design and MNAR fill-in brackets. BOUT closes.

## Cold open law
B00 names the two instruments and their distinct targets before giving any mechanics. It establishes that the loop is identical for both, preserving the series spine. It explicitly extends the robustness probe to agent and prompt-based systems — the most common student artifact in a computational skepticism course — so no student thinks this episode doesn't apply to them.

## Gap formula
Gap: students know that models can learn shortcuts but have never systematically designed a probe to surface one in their own build. Bridge: the probe suite is three specific probes with behavioral definitions — perturbation, proxy-feature, distribution-shift — and the result is a table, not a score. Close: the features-not-bugs three-question sentence ties the probe result to a specific data explanation, making the finding actionable rather than merely observed.

## Utility lint
Probe definitions are behavioral (what you do, not what it measures in theory). The robustness profile table columns are named (tested, found, monitoring flag). Features-not-bugs is given a sentence template: proxy used · real feature · gap. MNAR is defined via its consequence (imputing or ignoring both produce the same bias) rather than as a statistical abstraction. The Plato sentence has a fill-in-bracket template and an example to prevent evasion via abstract writing.

## Vocabulary / register
**Probe suite** — the set of ≥3 robustness probes; defined in B01. **Features-not-bugs** — the framing that a learned proxy was a real correlation, not a bug — making the failure mode structural, not accidental; defined in B02. **Epistemic frame** — the set of decisions (sampling, labeling, joining, windowing) that produced the data; term used in B03 and series-wide. **MNAR (missing not at random)** — values whose absence is correlated with the outcome; defined in B03 with consequence. **Plato (classical move)** — the move that names the artifact versus the world it claims to describe; introduced in B04. Plato joins Descartes and Hume from E2 as the third of the four classical moves in the series.

## Honesty
The claim that "the proxy worked, and that is exactly the failure mode" is accurate and counterintuitive in a productive way — it distinguishes structural distributional failure from modeling error. The claim that MNAR produces the same bias whether you impute or ignore is a simplification that holds for naive imputation (mean, mode, forward fill) and is accurate enough to be actionable at this level. The Gebru adaptation note is honest: these are the five questions adapted, not the original Datasheets for Datasets in full.

## Length law
8 beats (~481s estimated). B03 is the longest body beat (78s) because it enumerates all six steps plus the datasheet five questions. This is appropriate — the data-frame audit is the most procedurally dense instrument in the series. BHTF reads two distinct probe components (proxy-feature design and MNAR failure) and closes with a concrete action: run the probe as designed.

## Narration spot-check
B01 correctly states that the probe result is "a robustness profile table, not a number." B02 correctly states the features-not-bugs consequence: "good in-distribution, breaks out of distribution." B03 correctly gives MNAR's consequence: "imputing the missing values or ignoring them both produce the same bias." B04 correctly requires the Plato sentence to be written even when uncomfortable. BHTF correctly states: "The result — not the hypothesis — goes in the instrument report."

## Visual law
All Remotion. B00 uses ClaudeComposerAsk with three-item `output` array. B01–B04 use ClaudeWindow with `view: "artifact"`, six artifact lines per beat, and a ≤4-word spark line. BVDT uses ClaudeVerdictArtifact with five lines. BHTF uses ClaudeComposerAsk. BOUT uses ClaudeTitleOutro.

VERDICT: PASS
