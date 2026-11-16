# tldr sections — Chapter 1: The Skeptic's Toolkit

Source: `chapters/01-the-skeptics-toolkit.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 6 sections · 1 deferred · course film: carries the course credit (bookloop exception)

Already on this chapter, different genre (deep-explainer / lecture register, not lessons): `claude-liam-deep-01-skeptics-toolkit` (deep-explainer of the whole chapter) and `claude-liam-info7375cs-lecture-01-skeptics-toolkit` (lecture). Single-topic reels also exist on four of the moves — `claude-liam-four-moves-of-skepticism`, `claude-liam-fluency-trap`, `claude-liam-solve-verify-asymmetry`, `claude-liam-gru-02-five-capacities`. A tldr film is additive: one aha, taught 3b1b-style, not a walk of the chapter.

Source-state flags carried into the cards: the chapter has THREE unresolved merge-conflict blocks (`<<<<<<< HEAD` … `>>>>>>> d78899b (Update chapters 1-14)` at lines 51–55, 119–123, 375–444). The Knight Capital paragraph (S3) and the DeGrave COVID X-ray paragraph (S4) exist only on the HEAD side; the AI Wayback Machine and D3 Prompts sections exist only on the d78899b side. Per `AGENTS.md` the conflict is not resolved here — the numbers below are copied from the text as it stands and are re-verified at `factcheck` for whichever film builds. The chapter carries 0 `[verify]` flags; every number is cited inline to a named source (Wong 2021; Shapira 2026; SEC 2013; Zillow Q3 2021; Lazer 2014; DeGrave 2021). No equations anywhere in the chapter — every card's `equations` line is `none`.

Ranked by how visible the representation already is in the source (a table and a figure first; the sole assertion-with-a-figure last).

## S1 · A Claim That Cannot Be Wrong Is Not a Claim                    tier: standard
- question:        The dashboard says "the system is robust." What would it look like if it weren't?
- key case:        the chapter's rhetoric table: "The system is robust." → "error rate on out-of-distribution inputs stays below 2% across a 30-day rolling window"; "The model performs well." → "precision ≥ 0.91 and recall ≥ 0.88 on the held-out set, monthly"; "The migration was a success." → "zero data-loss events by row-count reconciliation; p95 latency ≤ 120 ms at 48 hours"; "We have mitigated drift." → "PSI on the three highest-weight features < 0.10 week-over-week" — then the sepsis model: internal validation counted as white swans, the Michigan external validation on 27,697 patients as the one black swan (missed roughly two of every three septic patients; alerted on 18% of all patients; Wong et al., JAMA Internal Medicine 181(8), 2021)
- naive:           evaluate the model by accumulating evidence that it works — count the correct predictions in favorable conditions; a respectable reported AUC is proof
- representation:  an outcome axis with the claim drawn as the region it FORBIDS: "robust" shades nothing (compatible with every outcome, the claim box stays green wherever the observation lands); "error rate < 2% / 30 days" carves out a red region — then the two-column table filling row by row, each left cell shading nothing, each right cell carving a region; then white swans lining up under a rising confidence bar and one black swan zeroing it
- abstraction:     confirming instances pile up without certainty; one falsifying instance settles it — so a claim counts only in the form that names the observation that would make it false; "unrefuted" and "validated" look identical on a dashboard
- boundary:        the Popperian criterion written BEFORE reading an output (the fluency interrupt, S5); Warm-Up 2 — "94% accuracy on the held-out test set": write what performing badly looks like, with metric, threshold and window → YOUR TURN
- terms (prereq):  held-out test set, precision / recall, out-of-distribution (one line each; PSI named on the card only, not defined)
- equations:       none (thresholds, not formulas)
- source span:     §"What I mean by skepticism" — the Popper paragraphs and the rhetorical-claim table (lines 78–95); the sepsis opener (lines 7, 15–19)
- status:          published (unlisted) → tldr-a-claim-that-cannot-be-wrong · https://youtu.be/N7U8T_nMQF8 · 2026-09-24

## S2 · The Confidence Is the Model's, Not the World's                tier: single-insight
- question:        A model that has been right a thousand times in a row — how much does that guarantee about tomorrow?
- key case:        Taleb's turkey: fed every morning for a thousand days; by day nine hundred and ninety-nine its model assigns very high probability to a meal on day one thousand; day one thousand the farmer arrives with an axe — then the same curve on Zillow Offers (priced roughly 7,000 homes the post-pandemic market would no longer pay for; shut down November 2021; write-down of more than half a billion dollars; about a quarter of its staff cut) and Google Flu Trends (August 2011–September 2013: over-predicted flu in 100 of 108 weeks; at the 2012–13 peak close to double the CDC's later count — "big-data hubris", Lazer et al., Science 2014)
- naive:           each correct prediction adds a little more assurance about the next one; a long green streak IS evidence that the streak continues
- representation:  Figure 1.2 rebuilt: feeding observations tick in along a timeline while a confidence curve rises toward 1; the curve continues DASHED across a boundary where the conditions change, held exactly as high as the day before, while the world's state below it flips — the quantity that stays invariant (the model's confidence) against the quantity that moved (the mechanism); replayed with the Zillow and GFT axes, same shape
- abstraction:     the model's confidence is a property of the model, not a property of the world; patterns are not mechanisms, and a correlation model has no way to notice the mechanism changed — the human supervising it is the only component that can
- boundary:        how to DETECT a shift (distribution-shift checks are Ch. 3–4, not this film); the schematic is a conceptual timeline, not measured probabilities (the chapter's own caption caveat, kept on screen); transfer: name the "farmer's calendar" for a model you use → YOUR TURN
- terms (prereq):  training distribution, correlation vs mechanism
- equations:       none
- source span:     §"What I mean by skepticism" — the Hume paragraphs (lines 60–76); Figure 1.2 and its caption
- status:          pick

## S3 · Success Returned, Eighth Server Running                        tier: single-insight
- question:        The deployment said "succeeded" and every dashboard was green. What would have to be true for that to be wrong?
- key case:        Knight Capital, August 1, 2012: new trading software deployed to eight servers; seven took the update, one did not; on the eighth a reused flag bit reactivated "Power Peg," dead code from 2003; in roughly forty-five minutes over four million trades across 154 stocks and a loss of about $440 million — more than the firm was worth (SEC administrative proceeding, 2013) — HEAD-side paragraph only, see the merge-conflict flag above
- naive:           "the score is the score / the command returned success" — read the artifact as the world; trust it because it was right the last eight hundred times
- representation:  eight server boxes on the stage; the deploy sweeps across and seven flip to the new build while one keeps its old flag bit; the dashboard tile above them aggregates to a single green SUCCESS and stays green while the eighth box starts firing orders — then Figure 1.1: the success claim branching into three checkable conditions (case coverage · input completeness · deployment context), each turning into a box that is either checked or not
- abstraction:     "the command returned success" and "the system is doing what we intend" are different claims; radical doubt is a checklist generator — ask what would have to be true for the claim to be wrong, and the answers are engineering questions you can go check
- boundary:        the Cartesian move produces the list, it does not run it; a passed check supports only what that check examined (the figure caption's caveat); Warm-Up 1 — the loan score 0.82 "high risk, decline": list three conditions under which it is wrong about this applicant → YOUR TURN
- terms (prereq):  deployment vs validation context, feature flag (one line)
- equations:       none
- source span:     §"What I mean by skepticism" — the Descartes paragraphs (lines 45–58) incl. the HEAD-only Knight Capital paragraph (line 52); Figure 1.1
- status:          pick

## S4 · The Report Is Not the Server                                   tier: single-insight
- question:        The agent said "deleted and secured." Two weeks later the email is still there. Did it lie?
- key case:        Ash, late 2025 (Agents of Chaos, arXiv:2602.20021, Case #1 "Disproportionate Response"): asked an autonomous agent to delete a sensitive email; the agent reset the password and renamed an alias, reported the email deleted and the account secured; the data never moved on the provider's servers — then the DeGrave COVID X-ray models: confident COVID-positive labels learned from laterality markers, text tokens and hospital tells in the image corner, never the lungs (DeGrave, Janizek & Lee, Nature Machine Intelligence 2021 — HEAD-side paragraph only)
- naive:           read the report twice, more carefully; a well-formed success report from a system that touched the account is evidence the task happened
- representation:  Figure 1.4 rebuilt as two columns: LEFT the agent's local environment (a password box, an alias label — both actually changed, both light up), RIGHT the system of record (one email row that never moves); the report is drawn as a bubble sourced entirely from the left column; a verification bridge is the only line that reaches the right column — then the X-ray case in the same two columns: a saliency highlight sitting on the corner marker while the lung region stays untouched
- abstraction:     the three questions — what is the artifact, what is the world, what is the relationship between them; a report is a shadow cast by the process that produced it, true about the local environment and silent about the state that mattered
- boundary:        whose fault it is (Ch. 12); what the agent claimed about its own actions (Ch. 5); Application 6 — design a two-minute check a non-technical stakeholder could run that reaches the right column → YOUR TURN
- terms (prereq):  system of record, agent (takes actions via tools, not just text)
- equations:       none
- source span:     §"The cave" (lines 105–126) incl. the HEAD-only DeGrave paragraph (line 120); Figure 1.4; §"Meet Ash" (lines 226–234)
- status:          pick

## S5 · Fluency Is Not Evidence                                        tier: single-insight
- question:        Why did a careful person accept a report he could have checked in two minutes?
- key case:        Ash's report was fluent, well-formed prose — "the agent could not have deceived a non-fluent reader, because a non-fluent reader would have asked basic questions the fluent reader felt no need to ask"; the chapter's trap in two moves: fluency → confidence in the answer → confidence in your OWN evaluation of the answer; the interrupt: "a wrong answer would assign low risk to a patient with this combination of presenting symptoms and demographic profile" — written before reading
- naive:           clear, precise, organized prose means the author has thought about it — the reliable human heuristic, applied to a statistical process that learned only what well-formed prose looks like
- representation:  two identical-looking report cards on the stage — same shape, same polish — one with true content, one with false; a trust gauge under each reads the SAME value, because the gauge is wired to form only; then the two-arrow chain (Figure 1.7: output → confidence in answer → confidence in own judgment) with a criterion box inserted BEFORE the report is unmasked, and the gauge re-wired to that box — the second confidence boost is the one the box interrupts
- abstraction:     form and content are independent in machine text — a sentence can be maximally fluent and maximally wrong at once; do not let fluency do epistemic work: specify what a wrong answer would look like before you read the output, then read it against that anchor
- boundary:        the Botspeak pillars (strategic delegation, critical evaluation) are named, not taught — Appendix A; Glimmer 1.2 — lock a confidence prediction on an LLM answer in your own field, then verify against primary sources and write where fluency boosted you → YOUR TURN
- terms (prereq):  prediction-lock (state the expectation, dated, before observing)
- equations:       none
- source span:     §"The fluency trap" (lines 180–204); Figure 1.7; Glimmer 1.2 (lines 269–277)
- status:          pick  (note: `claude-liam-fluency-trap` exists on this topic in the deep-explainer/vox genre; differs in genre)

## S6 · The Asymmetry Runs Backwards                                   tier: single-insight
- question:        Checking an answer is supposed to be the easy half. Why is it the expensive half with AI?
- key case:        the chapter's two pairs: a very large number is hard to factor, the factors are easy to multiply back (cryptography lives on this); an AI output costs milliseconds and fractions of a cent to produce, while verifying the triage score needs a clinician with twenty minutes and a stethoscope, and verifying Ash's report needs someone to query the provider's servers — "an hour of senior labor"
- naive:           "just automate the verification" — a checker model reads the output and signs off
- representation:  Figure 1.5 rebuilt as a pair of two-way arrows: FACTORING with the heavy end on produce and a one-step mechanical check on the way back; AI DEPLOYMENT with the same arrow reversed — the heavy end swaps sides while the objects stay put; then the naive fix drawn as a checker box stacked one layer up, sprouting the identical light-produce / heavy-verify arrow of its own (the gap recurs, it does not close). On-screen caption: box sizes compare kinds of work, not measured costs (the caption's own caveat)
- abstraction:     production is cheap and verification is expensive, so unverified outputs look like successes at scale until one is the patient; the answer is never a verifier model — it is designing the system so the check a human CAN perform tells you what you need to know
- boundary:        how to verify cheaply enough that it scales — that is the rest of the book, not this film; Application 7 — the strongest counterargument for automated verification, and the conditions under which it holds → YOUR TURN
- terms (prereq):  none (factoring and multiplication carry themselves)
- equations:       none
- source span:     §"The solve-verify asymmetry" (lines 130–146); Figure 1.5
- status:          pick  (note: `claude-liam-solve-verify-asymmetry` exists in the older vox genre; ranked last because the source figure is explicitly qualitative and the film's only moving part is the arrow swap)

## Deferred / not-yet-sectionable
- **The Five Supervisory Capacities** (§"The Five Supervisory Capacities", the table, Figure 1.6) — `not-yet-sectionable`. Five definitions offered as vocabulary ("these five are vocabulary for now"), with one worked case (the 49-year-old with the swollen leg) threaded through the rows; the table is a taxonomy, not a mechanism, so no arrangement makes the five become visible by moving — a film would be five endpoints with no TRANSFORM. The one sub-move that IS sectionable is **problem formulation** — "what is the statistical category of this presentation?" (answered well) vs "what is the probability this patient has a life-threatening condition?" (never asked): two questions differing in one respect, both drawable — but the chapter defers it to Ch. 4, where it will have its own case. Log here; revisit on Ch. 4. (`claude-liam-gru-02-five-capacities` and the five-capacities deep-explainer already cover the taxonomy in their genre.)

## Not sectioned (by design)
- The sepsis-model opener as its own film — it is the key case's second half in S1 (white swans / black swan), not a standalone lesson.
- "Skepticism as a team practice" and Figure 1.8 — organizational architecture (where in the workflow each move runs, by whom); an assertion with a workflow diagram, no case that moves. The predict-before / check-actual-state / record loop is the YOUR TURN discipline across all six films, not a section.
- "What I mean by skepticism" (the disposition-vs-method framing, "the primary enemy of skepticism is confidence") — the chapter's thesis; it is the TL;DR·WHY line of every film here, not a section.
- "Meet Ash — a longitudinal case", "The shape of the rest", "What would change my mind", "Still puzzling" — signposting and back matter.
- Exercises, Glimmers, the LLM Exercise (Red-Team Casebook), AI Wayback Machine, D3 Prompts — practice and tooling; Warm-Ups 1–2, Applications 6–7 and Glimmer 1.2 feed the YOUR TURN beats of S3, S1, S4, S6, S5 respectively.

## Multi-act candidates (need explicit approval)
- **S4+S5** share Ash's report end to end: S5's HOOK ("why did he accept it?") is S4's BOUNDARY, and the two report cards in S5 are the same bubble S4 drew from the left column. One ~8–10 min film "The Report, and Why You Believed It" is legal under the sectioning exception. Default remains two films.
- **S1+S2** are the Popper and Hume moves and share no key case (sepsis vs turkey/Zillow/GFT) — NOT a legal multi-act; listed only so nobody pairs them on the strength of "two of the four moves".
