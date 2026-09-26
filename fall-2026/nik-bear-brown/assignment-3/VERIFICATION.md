# Verification of the shipped candidate — Assignment 3

**Nothing has been verified yet.** This file holds the acceptance criteria, fixed **before** anything runs, as the assignment requires. Every other field is filled in from an actual run, never from an expectation.

**Candidate version or content identifier:** _pending — the commit hash of the shipped probe suite goes here and in Canvas._

**Input sources and fixture/simulation/live labels:** The baseline and the discrete input space are **fixtures**, written for this assignment. Any Claude explanation obtained live is labelled live, with its date and model identifier, and kept separate from an offline surrogate.

**Environment and exact commands:** _pending — the actual `python3 probes.py …` and `python3 scoring_rule.py …` invocations and the test command, with the Python version._

**Acceptance criteria fixed before checking:**
1. **A probe can fail.** Against the deliberately fragile baseline, at least one of the three frozen probes fails before the repair. If none fails, the suite is reported as weak, not the baseline as robust.
2. The runner is **deterministic** — two runs on the same inputs produce a byte-identical `robustness-profile.csv`.
3. Every probe row names its expected relation *before* the observed output, so a pass cannot be decided after seeing the result.
4. The counterfactual enumeration is **exhaustive** over the declared discrete space, and the code asserts the count it expected to enumerate.
5. Unchanged input produces no decision change; an unreachable target decision is reported as unreachable, not as a failure; an infeasible feature change is marked infeasible and excluded from the decision-flip count.
6. **Two cases computed by hand** — one probe outcome and one counterfactual — and compared against the tools' output.

**Expected result from independent source or calculation:** The two hand calculations in (6). The tools checking themselves is not a check.

**Observed result and evidence path:** _pending._

**Checks that failed and subsequent revision:** _pending. Failures get recorded with the repair that followed, not edited out._

**Shared assumptions or possible common errors:** The probes, the baseline, and the tests would be written in the same session by the same agent, so all three can share one wrong assumption about what the baseline does with its input. The hand calculations and the deliberately fragile baseline exist to break that.

**Remaining limits:** A passing finite suite is evidence about those probes only. A counterfactual of a program is not an intervention on the world. No claim is made that every perturbation used preserves meaning — the semantic probes are *intended* to change it.

**Actual reviewer or automated checker:** _pending — name who or what actually ran the checks._

**Final handoff decision and owner:** _pending — Professor Bear._

Put the final Git commit hash in Canvas after committing this file. Do not invent a human signature or claim checks that were not run.
