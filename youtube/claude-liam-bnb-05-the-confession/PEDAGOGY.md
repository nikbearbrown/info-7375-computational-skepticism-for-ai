# PEDAGOGY — claude-liam-bnb-05-the-confession

## Act structure
7-beat episode (B00–B03, BVDT, BHTF, BOUT). Cold open (B00) repeats the one idea verbatim — required for E5 — and names the confession as the hardest page and the reason why. B01 enumerates the four required parts and distinguishes a confession from a bug report. B02 shows the part-two sentence in action through three contrasted examples: what it does not look like versus what it looks like. B03 handles the 'no mistakes found' failure mode and the residual-risk framing. BVDT restates all rules. BHTF reads the full four-part prompt with the "do not soften part 2" instruction and the diagnostic test. BOUT closes.

## Cold open law
B00 opens by repeating the one idea (builder-as-worst-auditor) verbatim, as required for E5. It immediately names what makes the confession harder than the instrument reports: the distinction between naming a mistake and naming the fluency that was being defended. This distinction is the episode's only structural argument — everything else is operational.

## Gap formula
Gap: students produce instrument reports but write the confession section as a fourth instrument report, listing findings without naming their own role in allowing the mistake through. Bridge: the four-part structure, with part two specifically framed as a sentence only the student can write. Close: the diagnostic test in BHTF — "if it sounds like a bug report, you haven't written the reason yet, go one sentence deeper" — gives a behavioral test the student can apply without external feedback.

## Utility lint
The bug-report vs. confession distinction is given behavioral form: a bug report has parts 1, 3, and 4 but not part 2. The three examples in B02 follow a strict wrong/right/wrong/right pattern, each pairing a generic form (category name) against a specific form (investment named). The 'no mistakes found' response is operationalized: "go back to the pre-registered suspect and probe harder." The residual-risk framing is given a model sentence demonstrating what calibrated uncertainty looks like in writing.

## Vocabulary / register
All key vocabulary introduced in E1–E4 is in active use here without redefinition. **Pre-registered suspect** (E1) is invoked in B03 as the instrument-less student's next step. **Residual risk** (E2) is the series-wide term for what remains after the fix. The **four-part confession** is a new structural term introduced in B01. The **"fluency you were defending"** is the series' name for the personal investment that produces builder bias — introduced in B00 and returning in the verdict.

## Honesty
The claim that "a confession that has all four parts and is honest about part two is the thing the course is training" is accurate as a statement of pedagogical intent. The examples in B02 are constructed to be plausible and recognizable across different artifact types (accuracy-based, data-quality-based, verb-based), not a single scenario. The grading note — "missing any one part drops the grade" — mirrors real rubric enforcement and is stated without softening.

## Length law
7 beats (~401s estimated). No B04 because the series-climactic episode derives its weight from depth in B01–B03, not breadth. B02 is the longest body beat (74s) because it carries three contrasted example pairs, which require space to be distinguishable. BHTF is the longest handoff in the series (80s) because it reads the full four-part prompt with the "do not soften part 2" instruction and the diagnostic test.

## Narration spot-check
B00 states the one idea verbatim ("a builder is the least reliable auditor of their own build — exactly the way a model is the least reliable judge of its own output"), as required for E5. B01 correctly states "missing any one drops the grade." B02 correctly uses three contrasted pairs — each pairing a category name (wrong) against an investment-specific sentence (right). B03 correctly states "'no mistakes found' is graded as not-looking" and gives the correct next action (go back to the pre-registered suspect). BHTF correctly includes "Do not soften part two" and the diagnostic test.

## Visual law
All Remotion. B00 uses ClaudeComposerAsk with three-item `output` array where item three names the 'I wanted to believe' sentence as the series deliverable. B01–B03 use ClaudeWindow with `view: "artifact"`, six artifact lines per beat, and a ≤4-word spark line. BVDT uses ClaudeVerdictArtifact with five lines. BHTF uses ClaudeComposerAsk. BOUT uses ClaudeTitleOutro.

VERDICT: PASS
