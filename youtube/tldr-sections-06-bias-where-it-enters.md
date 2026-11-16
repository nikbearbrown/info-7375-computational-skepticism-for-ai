# tldr sections — Chapter 6: Bias: Where It Enters and Who Is Responsible

Source: `chapters/06-bias-where-it-enters-and-who-is-responsible.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 5 sections · 2 deferred · course film: carries the course credit (bookloop exception)

Numbers below are copied from the chapter as written. The chapter is a marked rough draft (`CHAPTERIZED 2026-07-02`, "rough draft for hand-rewrite") carrying 8 unresolved git merge-conflict blocks (HEAD `06-…` vs `d78899b` `03-…`, which renumbers every figure as 3.x) and 2 `[verify]` flags; cards read the HEAD side only, and every number is re-verified at `factcheck` for whichever film builds. The three-team parable is labelled *constructed* by the chapter itself; any card that uses it must say so on screen.

Already on this chapter, different genre (deep-explainer register, not lessons): `claude-liam-deep-06-bias` ("Fix the Room, Not the Model.", ~8m38s, plan-gated) — the leverage/three-teams walk of the whole chapter. Also bias-adjacent, other genres: `claude-liam-cs-12-bias-pipe`, `claude-liam-cs-24-mnar-bias`, `claude-liam-vox-bias-pipe`, `claude-liam-ra-03-bias-and-explanation`. A tldr film is additive: one aha, taught 3b1b-style, not a walk of the chapter. S5 below is the card that overlaps the deep-explainer most; flagged on the card.

Ranked by how visible the representation already is in the source (worked numbers, equations and tables first; the constructed parable and the assertion-only passages last).

## S3 · Both Audits Were Right                                          tier: standard
- question:        ProPublica said COMPAS was biased; Northpointe said it was calibrated. How can both be doing correct arithmetic?
- key case:        Group 1 true recidivism rate 30%, Group 2 50%; a perfectly calibrated score (a "50" means 50% in both groups) forced to have equal false-positive rates — the threshold has to sit in a different place for each group
- naive:           "one of them must have fudged the numbers" — or "collect cleaner data and the disagreement goes away" (it is not a data-quality problem; it is a theorem)
- representation:  two populations of dots at base rates 30% and 50%, one score axis; hold calibration (the per-bucket reoffend share) equal in both and slide the threshold — the FPR and FNR boxes come apart; then hold FPR equal and watch calibration break. Three dials, only two can be locked
- abstraction:     v/(1−v) = p/(1−p) · t/f — with PPV v held equal and p_a ≠ p_b, t/f must differ; equal error rates demand it not differ; both hold only when p_a = p_b or t=1, f=0
- boundary:        the full proof, and *which two to lock* (demographic parity / equalized odds / calibration worked in arithmetic) → Chapter 7; the re-arrest-is-not-crime layer is S5's territory, one line here
- terms (prereq):  base rate, calibration, false positive rate / false negative rate, threshold
- equations:       v/(1−v) = p/(1−p) · t/f                                      ← one TANGENT (five symbols, no derivation)
- predict beat:    "Calibrated in both groups. Can the false-positive rates ALSO be equal? Commit." before the threshold slides
- source span:     §"The dataset as epistemic artifact" (COMPAS paragraphs, the 30%/50% sketch, the algebra), fairness-criterion table, Figure 6.5 (HEAD caption; `d78899b` side calls it 3.4/3.2)
- status:          built → tldr-both-audits-were-right (master 2026-09-23 13:50, verdict pending)

## S1 · More Data Makes It More Confidently Wrong                       tier: single-insight
- question:        If I just collect more data, doesn't the bias average out?
- key case:        1936 Literary Digest: 2.4 million responses → Landon landslide; Roosevelt won by a landslide; Gallup called it with roughly 50,000. Second instance: the sepsis model whose "labs within six hours" query drops exactly the patients too critical to be tested
- naive:           "more samples → closer to the truth" — true of the scatter, silent about the offset; the reflex Team Two ran (recollect, rebalance, retrain)
- representation:  a cloud of estimate-dots around a target θ; grow n — the cloud shrinks, tighter and tighter, around a centre that is NOT the target; the gap E[θ̂] − θ is the one quantity that never moves while everything else collapses (Figure 6.1 rebuilt). Then the sepsis frame: a population strip, the six-hour filter removes the darkest end, the sample mean slides away from the population mean
- abstraction:     Bias(θ̂) = E[θ̂] − θ; and E[Y | i ∈ S] = E[Y] only when P(i ∈ S) is independent of Y
- boundary:        what a weight can and cannot buy back (inverse-probability weighting 1/P(i ∈ S), stratum reweighting w_i = (N_i/N)/(n_i/n) — only when the selecting variable was recorded) → named, not taught
- terms (prereq):  estimator, expectation E[·], sample vs population, sampling frame
- equations:       Bias(θ̂) = E[θ̂] − θ; E[Y | i ∈ S] vs E[Y]                         ← two TANGENTs
- predict beat:    "2.4 million ballots or 50,000 — which poll would you trust?" before the clouds move
- source span:     §"What 'bias' actually means" (Literary Digest, Squire 1988), §"Ten mechanisms, distinguished" → "Selection bias" (sepsis, IPW); Figure 6.1
- status:          pick

## S4 · Seeing Is Not Doing                                              tier: single-insight
- question:        The model approves Group A at a rate 12 points above Group B — is that discrimination, or a correlation wearing its costume?
- key case:        the rooster and the sun: P(sunrise | rooster crowed) is high AND P(sunrise | do(rooster doesn't crow)) is high — the sun rises anyway; then exercise W2's loan audit: (a) a 12-point approval gap in the data, (b) set zip code (a race proxy) to a neutral value and rerun — the gap fell to 2 points
- naive:           "equal outputs across groups = fair; unequal = discrimination" — reading Rung 1 as if it answered Rung 2
- representation:  a three-node graph (cause → X → Y, with a hidden common cause into both). OBSERVE: shade the rows where X happened and read Y — the confounder path is still lit. DO: cut every arrow INTO X, set it by hand, read Y again — the same two probabilities now differ or don't. Two cases, one edge deleted
- abstraction:     P(Y | X = x) ≠ P(Y | do(X = x)); equal Rung 1 metrics do not certify causal fairness, and a Rung 1 disparity does not prove causal discrimination
- boundary:        Rung 3 (the counterfactual for THIS individual) — opened in Chapter 4, closed in Chapter 12; the four-row Rung 1/Rung 2 table becomes the YOUR TURN ("rewrite this audit finding one rung up")
- terms (prereq):  conditional probability P(Y | X), proxy feature, protected attribute
- equations:       P(Y | do(X = x))                                                ← one TANGENT (what "do" deletes)
- predict beat:    "Zip code set to neutral, everything else fixed. Does the 12-point gap vanish, stay, or shrink?" before the rerun
- source span:     §"Pearl's Ladder — Rungs 1 and 2" (rooster, loan-denial paragraphs, the Rung 1/Rung 2 table), Figure 6.6; exercise W2 for the 12 → 2 numbers
- status:          pick

## S5 · Fix the Room, Not the Model                                       tier: single-insight
- question:        Three teams fix the same biased system honestly — why did the one that never touched the model win by an order of magnitude?
- key case:        the chapter's constructed three-team parable (must be captioned *composite*): Team A adds a fairness penalty to the loss → disparity drops a little; Team B recollects the underrepresented subgroup and retrains → disparity changes shape; Team C changes the human reviewer's process → disparity drops by an order of magnitude
- naive:           "fix the thing closest to your hands" — the loss function, then the dataset; each blocks one real path and reports a partial success
- representation:  the causal graph of Figure 6.7 — protected attribute → proxies → model features → model output → deployment context (reviewer, threshold, appeals) → outcome — drawn with bias-flow as lit paths. Drop a block on the model node: one path dims, the proxy and reviewer paths stay lit. Block the data node: a different single path dims. Block the reviewer node: most of the flow goes dark. Same graph, three blocks, three residual glows
- abstraction:     the four-step leverage procedure — draw the graph, list the paths, ask which paths each intervention blocks and leaves open, choose the block that darkens the largest fraction of bias-carrying paths without cutting the paths the deployment needs
- boundary:        the case where the brightest path is upstream of your graph entirely — *Agents of Chaos* Case #6, provider-values bias (carries the chapter's own `[verify]` flag on the Kimi-K2.5 / "unknown error" detail; narrate only at the chapter's confidence or omit) — named, not taught; owner = whoever sits at the node
- terms (prereq):  causal graph (nodes, arrows, path), proxy, deployment context
- equations:       none (a procedure, no tangent)
- predict beat:    "Three blocks. Which one darkens the most paths?" after the three teams are named, before the blocks drop
- source span:     cold open (the three teams), §"Leverage analysis — finding the high-leverage intervention point" (four steps), Figures 6.7–6.8; §"A limit case" for the boundary
- status:          pick  (overlap warning: this is the spine of `claude-liam-deep-06-bias`; as a tldr it is the graph-with-three-blocks aha alone, ~4 min, not the chapter walk — Bear to decide whether it is additive)

## S2 · Accurate Is the Harm                                              tier: single-insight
- question:        Every check comes back green — representative sample, accurate labels, no annotator error — so why is the hiring model still poison?
- key case:        a hiring model trained on ten years of promotion records at a company that promoted men into engineering roles at higher rates; it learns P(Y_historical | x) well, and P(Y_historical | x) is not P(Y_fair | x)
- naive:           "the labels are clean, so the pipeline is clean" — the data-quality reflex; every earlier mechanism had a defect to find, this one has none
- representation:  a ten-year strip of promotion records filling in faithfully; a quality checklist beside it flipping green one item at a time (sample ✓, labels ✓, coding ✓, entry ✓); the model's fit tightens onto the records — and the target label on the axis is revealed to read Y_historical while the thing wanted, Y_fair, sits at a fixed distance that the fit never closes. Two targets, one fit
- abstraction:     historical bias: the data is a faithful recording of a world you did not want to reproduce; corrections lower the leverage of the historical signal (a less-biased proxy, a fairness constraint, time-weighting) and each spends predictive fit to buy less inheritance — you choose the price, not the loss function
- boundary:        the dataset / label / structural three-flavor map and where each fix cannot reach (the Figure 6.4 table) → YOUR TURN: exercise W1, the three colleagues' three diagnoses of this same hiring model
- terms (prereq):  training distribution, accuracy on the training distribution, label
- equations:       P(Y_hist | x) ≠ P(Y_fair | x)                                     ← one short TANGENT (two targets, same x)
- predict beat:    "Sample representative, labels accurate, no coding error. Is the model biased?" before the target label is revealed
- source span:     §"Historical bias", Figure 6.2 (HEAD side); §"Three flavors of bias" (structural example, Figure 6.4 table); exercise W1
- status:          pick  (weakest representation of the five: a scenario with no numbers; the motion re-uses S1's invariant-offset shape with a different reveal)

## Deferred — not-yet-sectionable
- **How bias types compound (Selection × Historical).** The claim is concrete ("rebalancing the sample addresses the first — and makes the second worse") and the compound table is a real table, but the chapter gives no worked case: no counts, no period split, no before/after. A Manim representation exists (records shaded by period; rebalancing adds more shaded rows) but the key case would have to be invented and then fact-checked as our own. Re-run if a numbered example lands in the hand-rewrite. Candidate INSTANCE for S5 (Team B's "changed shape") instead.
- **The kappa diagnostic (items vs annotators).** "Disagreement clusters on specific items → coding problem; on specific annotators → observer problem" is a clean two-cases-differing-in-one-respect representation (a rater × item disagreement matrix clustered by column vs by row), and κ = (P_o − P_e)/(1 − P_e) is a tangent-ready equation — but the chapter states the rule with no matrix, no κ values, no unblinding case. Not sectionable without inventing the data.

## Not sectioned (by design)
- The ten-mechanism taxonomy as a film — a list, not an aha; the chapter itself takes only three apart (selection → S1, historical → S2, implicit → not sectioned: "the water table" is a metaphor with no case).
- The five human-in-the-loop mechanisms and the two at the keyboard — grouped assertions with diagnostics named, no worked cases; their leverage line ("you do not fix any of these by touching the model") is S5's abstraction seen from the other side.
- The Apple Card note — the chapter explicitly refuses to over-claim it; a BOUNDARY line at most.
- Agents of Chaos Case #6 — one `[verify]`-flagged case, no graph of its own; S5's boundary.
- "The political dimension is the technical dimension", "What would change my mind" (its Hardt/Madras references carry the chapter's second `[verify]`), Synthesis and bridge, Glimmer 6.1, Exercises, LLM Exercise, AI Wayback Machine (Arendt), the D3 figure prompts (which on the `d78899b` side are boilerplate "5-bar chart" prompts even for the flowchart) — practice, back matter, or front matter.

## Multi-act candidates (need explicit approval)
- S1+S2: S2's HOOK ("every check is green and it is still poison") is the natural continuation of S1's aha ("more data sharpens the wrong answer") and the invariant-offset motion is the same shape — but they do NOT share a key case (Literary Digest vs the hiring model), so the exception does not strictly apply. Default remains two films.
- S3+S4: both are COMPAS-adjacent (S3 the impossibility, S4 the observational/interventional split on a loan audit) and the chapter's own bridge is "read the dataset like a historian" — different key cases, no exception claimed. Two films.
- S5 alone is the only card whose key case would carry a second act (leverage → the upstream owner), and that second act is exactly what `claude-liam-deep-06-bias` already does. Single film or skip.
