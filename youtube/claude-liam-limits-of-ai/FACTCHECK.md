# FACTCHECK — claude-liam-limits-of-ai

Status: **DRAFTED WITH THE PLAN — Gate F NOT YET SIGNED.** The source doc
already performed one precision correction (the Challenger attribution);
verify the rest with the same standard.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B00/B02 | Three limits (meaning, intentionality, data-world gap) claimed as constitutive, not scale-dependent | ☐ | The essay's thesis via SOURCE.md — spoken AS the claim under examination | Framing; the acts argue it |
| 2 | B04/B05 | Harnad 1990, symbol grounding problem; the dictionary argument (symbols defined by symbols can't bootstrap grounding) | ☐ | Harnad, "The Symbol Grounding Problem," Physica D 42 (1990) | — |
| 3 | B06 | Bender & Koller: text-only training on form cannot in principle yield meaning | ☐ | Bender & Koller, ACL 2020 ("Climbing towards NLU") | — |
| 4 | B07 | Document grounding vs world grounding distinction; citation ≠ current world | ☐ | SOURCE.md Part 1 (the source's own sharpening) | — |
| 5 | B09 | The two-check flag (entity resolution = document; freshness = world; human sign-off regardless) | ☐ | code/flag_ungrounded_output.py — source's own code, verbatim | — |
| 6 | B11 | Searle's original vs derived intentionality; systems' outputs carry derived aboutness on loan from builders/readers | ☐ | Searle, Intentionality (1983); SEP "Intentionality"; SOURCE.md [cites 72-1, 74-1] | — |
| 7 | B12 | The removal test (what aboutness survives without reader/operator) as a documentation-review heuristic | ☐ | SOURCE.md Part 2 (the source's own operationalization) | — |
| 8 | B13 | Dennett rejects intrinsic intentionality outright; Boden cautions against overloading intentionality arguments | ☐ | SEP summary per SOURCE.md; Dennett's stated position | Boden caveat lives in props note, not narration |
| 9 | B15 | Shift taxonomy: covariate / label / concept drift | ☐ | Moreno-Torres et al. 2012, Pattern Recognition | — |
| 10 | B16 | WILDS: real deployment shifts (hospitals, camera traps, time, geography) degrade OOD performance materially; gap survives robustness methods | ☐ | Koh et al., WILDS benchmark | No invented magnitudes on screen |
| 11 | B17 | Guo et al.: modern networks poorly calibrated; softmax confidence can be arbitrarily high far outside training distribution | ☐ | Guo et al. 2017, "On Calibration of Modern Neural Networks" | — |
| 12 | B18 | "Fail loudly" framing: shift detection as instrumentation, not repair | ☐ | Rabanser, Günnemann & Lipton, "Failing Loudly" | — |
| 13 | B20 | Moral crumple zone: term, definition (system protected, nearest operator absorbs blame), coined by Elish; cases: Three Mile Island, AF447 | ☐ | Elish 2019, Engaging STS; SOURCE.md [cites 79-1, 83-1, 88-1] | Cases live in SOURCES, not narration |
| 14 | B21 | Experimental HITL work: oversight doesn't reliably correct errors, can worsen them; overseer preferences shape which errors pass | ☐ | SOURCE.md [cite 82-1] — "recent large-scale experimental study"; verify the actual study before render | Keep unquantified; cite generically if the specific paper can't be located |
| 15 | B22 | Jan 27–28 1986; ice on the pad; Thiokol engineers incl. Boisjoly argued delay with O-ring cold data | ☐ | Rogers Commission record | — |
| 16 | B23 | THE QUOTE: Mason to Lund, "take off your engineering hat and put on your management hat" (Rogers Commission testimony); call reconnected; Thiokol reported go | ☐ | Rogers Commission testimony (the source's own precision correction) | HARD RULE: never the NASA-to-Boisjoly variant |
| 17 | B24 | The three override conditions; their alignment with NIST AI RMF / OECD guidance; Boisjoly had condition 1; conditions 2–3 failed | ☐ | Elish analysis + SOURCE.md Part 5; NIST/OECD alignment is the source's reading | Alignment claim stays in SOURCES/props |
| 18 | B26 | ECE applies to human experts; Good Judgment Project method: lock prediction, score outcome (Brier), repeat; calibration trainable only via scored practice | ☐ | Guo et al. (definition); GJP forecasting methodology | — |
| 19 | B27 | Model cards / datasheets precedent for limits-as-primary-artifact | ☐ | Mitchell et al., Model Cards; Gebru et al., Datasheets | — |
| 20 | B28 | The five-condition no-deploy list | ☐ | SOURCE.md Part 7 (the source's own list, faithfully compressed) | — |

Editorial flourishes (labeled, no verification needed): "the seal holds"
(B05), "on loan" (B11), "the trap inside the trap" (B17), "detection
survived the night. Authority didn't." (B23), "the limit is the verdict"
(B28/B29).
