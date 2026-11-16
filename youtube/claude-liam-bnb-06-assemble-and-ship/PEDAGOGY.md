# PEDAGOGY — claude-liam-bnb-06-assemble-and-ship

## Act structure
7-beat series closer (B00–B03, BVDT, BHTF, BOUT). Cold open (B00) frames the deliverable as a portfolio, not a pile, and names the distinguishing quality: "what you still don't know." B01 enumerates all six deliverables with the specific completeness test for each — including the new requirement to label the classical move in each instrument report. B02 runs the honesty-floor sweep (five binary checks) and introduces the stretch and the repro-note test. B03 delivers the five final pre-submit checks and names the submit gate. BVDT recaps all rules as a series close. BHTF reads the four-check pre-submit audit prompt with all fill-in brackets. BOUT closes.

## Cold open law
B00 is the shortest cold open in the series (40s) by design — at episode 6, the student knows the work; the opener's job is to name the quality criterion ("a portfolio, not a pile") and close the loop. No arc preview, no instrument framing — just the deliverable and the one distinguishing sentence.

## Gap formula
Gap: students have all components but no systematic way to verify that they constitute a portfolio rather than a collection of separately-completed deliverables. Bridge: the six-component checklist with per-component completeness tests, the honesty-floor sweep, and the four-check pre-submit audit prompt. Close: the repro-note test is the one check that requires another person — naming it as such prevents students from self-certifying on a check that cannot be self-certified.

## Utility lint
Every component in B01 is given a specific completeness criterion — not "write a repro note" but "specify the environment, the data source and access method, the parameters, and the expected output on a known input." The classical-move labeling requirement is new in E6 and appears in both B01 and the BHTF prompt. The honesty-floor flags are behavioral (retroactive prediction-lock dates are "a flag the grader is likely to ask about"). The five final checks in B03 each have a failure-mode example so a student can self-diagnose.

## Vocabulary / register
All vocabulary in active use from E1–E5. New in E6: **labeled classical move** — the requirement to label which of the four classical moves (Descartes/Hume/Plato/Popper) drove each instrument report's design; introduced in B01 and enforced in the BHTF audit. **Closing note** — the forward-facing "what would change my mind / what still puzzles me" document; distinguished from a conclusion in B01. **Honesty quartile** — referenced in B02 as the employer-relevant quality signal that a third instrument strengthens; consistent with the series framing of skepticism as professional competency.

## Honesty
The claim that the stretch "earns no extra rubric points" is direct and honest — it prevents the stretch from being perceived as hidden compliance. The claim that the repro-note test "is the only check you cannot perform yourself" is accurate: every other honesty-floor check is a self-applicable binary. The closing note is explicitly distinguished from a conclusion because the series has consistently framed calibrated uncertainty as a skill, not a deficiency.

## Length law
7 beats (~381s estimated). Series-closer pattern, no B04. The shorter total runtime compared to E2–E4 is appropriate — E6 is a checklist and an assembly guide, not a new instrument. B01 and B02 carry the most new content (72s each). B03 is the submit gate — it enumerates but does not develop. BHTF is dense (76s) because it carries four numbered checks with example fill-in brackets for each.

## Narration spot-check
B00 correctly names the distinguishing quality of a portfolio: "what you still don't know." B01 correctly introduces the labeled-classical-move requirement as new. B02 correctly names the repro-note test as "the one check you cannot perform yourself" and distinguishes "ask them to look at it" from "have them actually try to run it." B03 correctly gates submission: "when all five checks pass, submit. Not before." BHTF reads all four audit checks with named brackets and closes with the classmate test instruction.

## Visual law
All Remotion. B00 uses ClaudeComposerAsk with three-item `output` array. B01–B03 use ClaudeWindow with `view: "artifact"`, six artifact lines per beat, and a ≤4-word spark line. BVDT uses ClaudeVerdictArtifact with five lines. BHTF uses ClaudeComposerAsk. BOUT uses ClaudeTitleOutro.

VERDICT: PASS
