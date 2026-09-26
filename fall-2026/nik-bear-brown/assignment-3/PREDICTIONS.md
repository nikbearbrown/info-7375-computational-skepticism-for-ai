# Predictions — Assignment 3, robustness and explanation

Written **before** any probe is designed or run, which is what the assignment is testing. Nothing below has been executed.

## Before the run

**Date:** 2026-09-26

**Question, part 1 (robustness):** Which input changes should preserve the result, and which should change it?

- **Should preserve:** leading and trailing whitespace, collapsed internal whitespace, and the order of items in a list the rule treats as a set. If any of these moves the output, the mechanism is keying on formatting.
- **Should change:** negation, and swapping the one word the decision actually turns on. If these *don't* move the output, the mechanism is not reading meaning at all.
- **Expected to degrade, not break:** a slice from a different distribution than the baseline was built on.

**Question, part 2 (explanation):** Will the feature named in a fluent explanation be necessary for the output?

**Expected result:** No — and specifically, I expect Claude to name the **correlated proxy** as the reason for the decision, because it moves with the outcome in every example it will be shown. The removal test should show the decision unchanged when the proxy is removed and the real feature held, and changed when the real feature is removed and the proxy held.

**Concrete removal test:** For each of the 2–3 features, hold the others fixed, remove or zero that one feature, re-enumerate the decision, and record whether it flipped. A feature the explanation calls central whose removal flips nothing is a false explanation, in writing.

**Confidence and reason:** High on the proxy prediction — that is the standard result and the reason the lesson exists. Low on the whitespace probes: I do not know whether my own baseline strips input before scoring, and that is the sort of thing I would guess wrong about my own code.

**Assumptions:**
- The baseline starts **deliberately fragile**, so at least one probe can fail. A suite that passes against a robust baseline proves nothing about the suite.
- The input space is small and discrete enough to enumerate exhaustively, so "every counterfactual" is literal, not sampled.
- Live Claude observations are recorded separately from any offline surrogate, and labelled.

**Measurable failure condition:** If all three frozen probes pass on the first run, the prediction is wrong *and* the suite is suspect — I will report it as a weak suite rather than a robust baseline, and design a probe that fails before claiming anything.

**Observation that would change my mind:** Claude naming the actually-necessary feature, with the proxy correctly dismissed, from examples alone. That would mean a fluent explanation can be trusted more than I am assuming here — and would be the more interesting result.

## After the run — append, do not rewrite above

**Actual output and evidence path:** _not run yet_

**Difference from prediction:** _not run yet_

**Revised understanding and remaining uncertainty:** _not run yet_
