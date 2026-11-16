# tldr sections — Chapter 11: Communicating Uncertainty: Calibrating Claims to Evidence

Source: `chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 6 sections · 3 deferred (not-yet-sectionable) · course film: carries the course credit (bookloop exception)

Already on this chapter, different genre (deep-explainer register, not lessons): `claude-liam-deep-11-communicating-uncertainty` ("The Number Didn't Change. The Verb Did.", six acts, ~8m43s planned, walks the whole chapter). A tldr film is additive: one aha, taught 3b1b-style, not a walk of the chapter. Related single-insight reels elsewhere in `youtube/`: `claude-liam-cs-10-calibration-curve`, `claude-liam-cs-22-calibration-useless`, `claude-liam-cs-23-subgroup-hidden`, `claude-liam-cs-28-conformal-wrap` (vox/cs register) — checked before GATE S so a pick does not remake one of them.

Chapter state the cards inherit (see "What the chapter itself flags" at the bottom): the file is a CHAPTERIZED rough draft with SEVEN unresolved git conflict blocks (`<<<<<<< HEAD` / `>>>>>>> d78899b`, chapter 11 vs chapter 12 numbering of every figure and of the "next chapter" pointer), two in-body `[verify]` flags, and one internal arithmetic inconsistency in the subgroup table. Numbers below are copied exactly as the chapter prints them; anything the chapter flags is flagged here too.

Ranked by how visible the representation already is in the source (a filled table and a worked number first; an asserted mechanism last).

## S2 · Where the Average Hides the Patient                          tier: single-insight
- question:        The model's calibration error is 0.018 overall — so why is it wrong by 0.103 on the patients who need it most?
- key case:        the chapter's subgroup table: global ECE 0.018 on N = 12,955; rare-disease cases N = 95, base rate 0.420, ECE 0.103, MCE 0.176; pregnancy-related N = 380, ECE 0.071; elderly N = 2,850, ECE 0.044 — four of five subgroups flagged (> 2× global) while the aggregate looks fine. Backed by the real case: the Epic Sepsis Model, Wong et al. (2021), 27,697 patients / 38,455 hospitalizations — AUC 0.63 vs developer-reported 0.76–0.83, PPV 12% (88% of alerts false), 67% of sepsis cases missed (1,709 of 2,552)
- naive:           "low global ECE means the model is calibrated" — one number certifies every patient
- representation:  five bars whose WIDTH is the subgroup's N and whose HEIGHT is its ECE, on one cream axis; the global value is drawn as the pooled result — the 95-wide rare-disease bar at 0.103 carries 0.7% of the weight and the pooled bar barely moves; then the same predictions re-binned per subgroup, so the hidden bar stands up on its own axis
- abstraction:     ECE_g = Σ_m (|B_m^g| / N_g) · |acc(B_m^g) − conf(B_m^g)| computed per named subgroup; report the global ECE AND the full distribution {ECE_g}; flag any subgroup ECE > 2× global
- boundary:        what ratio should HALT a deployment — the chapter says this is a values question it cannot yet teach ("Still puzzling"); construct-validity failure (the sepsis model encoding clinician suspicion, not sepsis onset) is upstream of any calibration metric → YOUR TURN: A5's three subgroups (0.030 / 0.092 / 0.141 at 80% / 15% / 5% of the population)
- terms (prereq):  calibration (stated confidence vs observed frequency), ECE (as "the weighted average gap"), subgroup, base rate
- equations:       ECE_g per subgroup                                                ← one TANGENT
- predict beat:    "Global ECE is 0.018. Rare-disease patients are 95 of 12,955. Before I show the row — what could their ECE be without moving the global number?" before the re-bin
- source span:     §"Subgroup calibration: where aggregate metrics lie" (the table + Wong et al.); §"What calibration metrics cannot see" (the failure-mode table, first row); "Still puzzling"
- status:          built → tldr-average-hides-the-patient (master 2026-09-23 15:07, verdict pending)

## S1 · Same Number, Three Verbs                                       tier: single-insight
- question:        If the evidence never changed, how can one sentence be true and the other be an over-claim?
- key case:        the chapter's opener: one finding — 87% accuracy on a single held-out test set, no significance test, no confidence interval; prior model 84% on the same set — written as sentence A ("We conclude that the new model is more accurate"), B ("We find … 87% … compared to 84%"), C ("We observe … 87% on this single held-out evaluation; whether the difference … is statistically significant is not yet established")
- naive:           "the verb is grammar, not a claim" — engineers default to sentence A without noticing; the numbers are right, so the sentence is right
- representation:  the frozen ladder as eight rungs on one cream stage (hypothesize → suggest → observe → find → show → demonstrate → conclude → prove), each rung carrying its minimum-evidence column from the chapter's table; the ONE evidence stack (a single test set, no CI) is held fixed on the left and fills up to between *observe* and *find*; the verb pointer slides from A to B to C and lands on the rung the stack reaches — *conclude* sits three rungs above the evidence
- abstraction:     warranted assertibility — you may assert in proportion to your evidence; the verb is the dial; most engineering evidence sits between *observe* and *find*, most engineering prose uses *conclude*, and the gap is the problem
- boundary:        the ladder flattens TWO axes (inferential caution — *suggest*, *indicate* — vs evidential strength — *observe*, *find*, *show*) into one line on purpose; *indicate* is deliberately off the ladder; the IPCC calibrated-language precedent (Mastrandrea et al., 2010) is named, not taught → YOUR TURN: W1's five report sentences (a)–(e), or A1's AI paragraph ("conclusively demonstrates … clearly show … we therefore conclude") — pull each verb down to the rung its evidence reaches
- terms (prereq):  held-out test set, significance test / confidence interval (as "the two things the finding does not have")
- equations:       none
- predict beat:    "Same 87%. Which of the three sentences does the evidence actually pay for?" before the pointer lands
- source span:     opening (sentences A/B/C); §"The verb taxonomy" — "The classical move", "The working hierarchy", the five-column verb table; §"The verb taxonomy applied to AI output" (as the PAYOFF's second instance); W1, A1
- status:          pick   (note: this is the deep-11 film's Act I–II subject; the tldr differs by holding ONE fixed evidence stack against a moving pointer — the deep walks the ladder rung by rung)

## S3 · One Score, Three Pieces                                        tier: single-insight
- question:        Two models have the same Brier score — why is one useful for triage and the other useless?
- key case:        W4's decomposition on a base rate of ȳ = 0.20: Uncertainty = 0.160, Resolution = 0.045, Calibration = 0.028 → BS = 0.160 − 0.045 + 0.028 = 0.143; versus the model that says 0.20 for every instance (Resolution 0, Calibration 0 → BS = 0.160); versus the coin-flip model p = 0.5 → BS = 0.25 at any base rate
- naive:           "lower Brier is better, report the one number" — and the chapter's warning that a low Brier score can belong to a model that is honest about uncertainty and useless for ranking
- representation:  the score as one bar that splits into three: the base-rate piece ȳ(1 − ȳ) that no model can move, the resolution piece that SUBTRACTS as predictions spread away from the base rate, the calibration piece that ADDS as predicted probability drifts from observed frequency; two models built side by side — spread-but-dishonest and honest-but-flat — landing on the same total for opposite reasons
- abstraction:     BS = (1/N) Σ (p_i − y_i)² is a proper scoring rule (minimized in expectation only by the true probability) and it decomposes: BS = ȳ(1 − ȳ) − REL + CAL — the decomposition, not the raw score, is what diagnoses the model
- boundary:        why "proper" holds (the expected-value argument) is stated, not derived; ECE and the reliability diagram are the calibration piece seen bin by bin → S4; AUROC / decision-curve analysis as what catches "calibrated but useless" (the failure-mode table, row 2) → YOUR TURN: W4's interpretation questions, then S2 of the Synthesis exercises (high resolution AND high calibration error at once — what does the reliability diagram look like?)
- terms (prereq):  predicted probability p_i, binary outcome y_i, base rate ȳ
- equations:       the Brier score; the three-term decomposition                      ← two TANGENTs
- predict beat:    "A model that says 0.20 for everyone — is its Brier score higher or lower than 0.143?" before the flat model's bar lands
- source span:     §"The Brier score: a proper scoring rule" (both equations, the low-Brier/poor-resolution paragraph); Figure 11.2/12.2 (conflict block); §"What calibration metrics cannot see", paragraph 2; W4
- status:          pick   (note: the chapter's symbols name the resolution term REL and the calibration term CAL — Murphy (1973) uses REL for *reliability* = the calibration term; keep the chapter's letters on screen but the film must say which is which, and factcheck should flag the swap to the author; the W4 total 0.143 is our arithmetic on the chapter's three numbers)

## S4 · The Diagonal Is the Promise                                    tier: single-insight
- question:        When the model says "90% sure," is it right nine times in ten — and how would you even check?
- key case:        the chapter's overconfidence instance: a model predicting "90% positive" that is actually right 70% of the time — a point 0.20 below the diagonal; then Figure 11.3's four shapes — below the diagonal (overconfident), above (underconfident), sigmoidal (over at the extremes, under in the middle — gradient-boosted trees), fine-in-aggregate-but-locally-off
- naive:           "check accuracy" — accuracy rewards being right; it never asks whether the 90% was earned; a single confidence number cannot be checked against a single outcome at all
- representation:  the reliability diagram built one prediction at a time: dots sorted into confidence bins along x, each bin's observed frequency rising on y; the diagonal drawn as the promise; the gap in each bin as a terracotta bar whose weighted sum IS the ECE; then the same dots rebinned (fewer bins, more bins) so the viewer watches the bars — and the number — move while the dots do not
- abstraction:     ECE = Σ_m (|B_m| / N) · |acc(B_m) − conf(B_m)|; a perfectly calibrated model has ECE = 0 and lies on the diagonal; the SHAPE of the deviation is the diagnosis, the aggregate number is not
- boundary:        the rebinning INSTANCE uses our own dots — the chapter asserts bin-dependence without a numeric example, so the film's rebinned values are ours and go through factcheck as ours; the rule-of-thumb thresholds (0.02–0.05 "well-calibrated", > 0.10 "systematic") carry the chapter's own `[verify]` — show them as folklore, not facts; MCE (the worst bin) named as the safety-critical companion; "overconfidence is THE dominant failure mode of deep nets / LLMs" carries the chapter's second `[verify]` (Guo et al. 2017 vs Minderer et al. 2021) — cite Guo for the phenomenon, hold the superlative → YOUR TURN: W5 (an ECE of 0.04 — name three things the number alone does not tell you)
- terms (prereq):  confidence bin, observed frequency / accuracy in a bin
- equations:       ECE (and MCE as a one-line variant)                                ← one TANGENT
- predict beat:    "Same dots. I cut ten bins into five. Does the ECE go up, down, or stay?" before the rebin
- source span:     §"Expected Calibration Error: binning the predictions"; §"The reliability diagram" (the four bullets); Figure 11.3/12.3 (conflict block); W5, A5
- status:          pick   (note: overlaps `claude-liam-cs-10-calibration-curve` / `claude-liam-vox-calibration-curve` in subject — vox register; the tldr adds the rebin-and-watch-the-number move)

## S5 · The Ladder Has Two Columns                                     tier: single-insight
- question:        You measured ECE = 0.03. Which word are you now allowed to write — observe, find, show, or conclude?
- key case:        the chapter's own walk: ECE = 0.03 on the validation set → *find* calibration is adequate on that set; all subgroup ECEs within 2× global → still *find*, not *conclude* (deployment shift may invalidate the calibration set); external validation + subgroups + documented distribution match → *show*; conformal guarantee → *prove* only with exchangeability stated; A6: pre-scaling ECE 0.11 → 0.03 after temperature scaling, validated at one hospital 2019–2021, deploying across three health systems in 2026 — one verb for the calibration hospital, a weaker one for the network
- naive:           "the metric is good, so the model is calibrated" — one number, one verb, and the verb chosen is *conclude*
- representation:  the L0–L5 evidence ladder as a two-column table filling one row at a time — left column the evidence you actually hold (internal ECE → held-out ECE → subgroup ECE → replicated → replicated under stress → validated in deployment), right column the verb it licenses (hypothesize → observe → find → show → demonstrate → conclude); the verb pointer never jumps a row; each row also shows "what remains uncertain" and "what evidence would move to the next row"
- abstraction:     the verb follows from the evidence: every calibration claim in a report is traceable to a row, and the row names the upgrade path; *conclude* is reached only by a monitored live deployment, and only for that regime
- boundary:        what "external validation" or "prospective study" cost to run is not taught; the two-axis wobble (S1) is inherited, not re-argued; temperature scaling and conformal are rows here, not mechanisms (S6; deferred D2) → YOUR TURN: A5 — the warranted verb for the global claim vs the tertiary-subgroup claim, and what that does to the Layer 1 summary
- terms (prereq):  the verb ladder (S1, or a ten-second recap), ECE (S4, or "a calibration error number"), external validation, distribution shift
- equations:       none
- predict beat:    "Held-out ECE 0.03, one site, no subgroups. Which row am I on?" before the pointer lands on L1
- source span:     §"From calibration metrics to trust claims" (both tables: evidence → warranted verb, and the L0–L5 ladder); A5, A6
- status:          pick   (multi-act candidate with S1 — same ladder object; see below)

## S6 · One Knob Cannot Close Two Gaps                                 tier: single-insight
- question:        Temperature scaling took the calibration error from 0.11 to 0.03 — so why doesn't that number travel to the next hospital?
- key case:        A6: a classifier's pre-scaling ECE 0.11 (systematic overconfidence); after temperature scaling with T = 1.8 the calibration-set ECE drops to 0.03; the calibration set is one hospital, 2019–2021; the deployment is three health systems in 2026. Chapter mechanism: divide every logit by one learned scalar T > 1 — the distribution flattens, the argmax never changes
- naive:           "the model is now calibrated" — the fix is trivial to compute, preserves accuracy, so ship it everywhere
- representation:  three probability bars over three classes flattening as T rises from 1 toward 1.8 while their ORDER stays fixed (the invariant); then the reliability curve pulled down toward the diagonal by the one knob — and a second population whose curve bends the OTHER way in a different confidence range, which the same knob cannot fix because it applies one correction to every prediction
- abstraction:     p^scaled = softmax(z / T); T learned by minimizing negative log-likelihood on a held-out calibration set with weights frozen; a single global correction cannot fix miscalibration that varies by confidence level, input type, or subgroup, and it does not transfer across distribution shift — a miscalibrated model that has been temperature-scaled is a miscalibrated model whose outputs were adjusted
- boundary:        Platt scaling and isotonic regression (more parameters, overfit risk on small calibration sets) named, not built; the "second population bending the other way" is an illustrative instance we draw, not a chapter number — factcheck as ours; the verb the 0.03 licenses is S5's question → YOUR TURN: A6's two verbs and what would close the gap
- terms (prereq):  logit, softmax (as "scores into chances"), calibration set
- equations:       p^scaled = softmax(z_i / T)                                          ← one TANGENT
- predict beat:    "T goes from 1 to 1.8. Does the top class ever change?" before the bars flatten
- source span:     §"Temperature scaling: the fix and its limits" (equation + the three structural limits); Figure 11.4/12.4 (conflict block); A6
- status:          pick   (note: the softmax-temperature mechanism is already a built tldr film in the PE book — `tldr-temperature-not-truth`, S4 of `tldr-sections-01-randomness-and-first-prompts.md`; this card's insight is the NON-TRANSFER, not the flattening — if that film is reused for the mechanism, this section shrinks to the second-population instance and may be better folded into S5 as an INSTANCE)

## Not yet sectionable (deferred — the source states the abstraction without a case)

### D1 · Three Layers, One Document                                    status: not-yet-sectionable
- question:        Why write one layered document instead of a paper plus an executive summary?
- reason:          the chapter asserts the three-layer pattern and the claim that plain English "exposes the un-calibrated verb" ("state-of-the-art calibration" hiding a *conclude*), but gives no worked document. A2 (89% sensitivity / 81% over-75, written in three layers) and A4 (Layer 1 says ready, Layer 2 shows 12 points lower) are exercises whose worked answers would be ours to invent and then fact-check as our own. No representation that moves: a document splitting into three bands is a diagram of a claim, not a mechanism. Figure 11.1 is a static structure figure. Revisit if the author writes the A2 answer into the chapter body.
- source span:     §"Two readers, one document"; Figure 11.1/12.1; A2, A4; "Still puzzling" (the author says he has no efficient way to teach this)

### D2 · The Guarantee That Comes With a Population                    status: not-yet-sectionable
- question:        How can a predictor PROVE 90% coverage, and what does the proof stop covering?
- reason:          the mechanism is drawable (nonconformity scores on a calibration set → the (1 − α)-quantile q̂ → every label with score ≤ q̂ goes into the set; marginal, not conditional; exchangeability breaks under shift) but the chapter carries no instance — no α, no scores, no set sizes, and "for a binary classifier this often reduces to a probability threshold" is an assertion. The key case would be invented. Also already covered by `claude-liam-cs-28-conformal-wrap`. Revisit with a worked α = 0.1 example from Angelopoulos & Bates (2021) if the author adds one.
- equations:       P(y ∈ C(x)) ≥ 1 − α
- source span:     §"The conformal prediction guarantee — and what it costs"; Figure 11.5/12.5 (conflict block)

### D3 · Two Kinds of Not Knowing                                       status: not-yet-sectionable
- question:        Will more data shrink this uncertainty, or is it built into the world?
- reason:          epistemic vs aleatoric is the one drawable idea in "Saying you do not know in writing" (two uncertainty bands against n — one narrows, one does not), but the chapter's instances are one-line assertions (a rare subgroup never seen → epistemic; individual outcomes in a noisy system → aleatoric) and the CI example ([0.81, 0.89] vs "approximately 0.85") is a single sentence. The other four moves (name the reason, quantify, strike the throat-clearing hedge, state what would change your mind) are prose rules — readings, not sections. W2 and A3 are the practice surface.
- source span:     §"Saying you do not know in writing"; W2, A3

## Not sectioned (by design)
- "Why solitary review does not work — and the peer critique protocol", Glimmer 11.1 — a procedure and an assignment; practice, not a lesson. The blind-spot argument ("your blind spots are blind to you") is a BOUNDARY line for S1, not a film.
- "The verb taxonomy applied to AI output" as its own film — it is S1's second instance and its YOUR TURN (A1's paragraph); a separate film would re-teach the ladder.
- "What survives review" — a document checklist; the Layer-1/limitations/what-would-change-my-mind structure feeds no representation.
- "Where this leaves us", "What would change my mind", "Still puzzling", the Exercises, the LLM Exercise (Red-Team Casebook passes 1–4), the AI Wayback Machine (Nightingale), the D3 Prompts — back matter and practice.
- The IPCC calibrated-language scheme — one sentence of precedent inside S1's boundary; it carries no case of its own here.

## Multi-act candidates (need explicit approval at GATE S)
- **S1+S5** share one object — the verb ladder. S1 holds the evidence fixed and moves the verb; S5 holds the verb rule fixed and fills the evidence column row by row. S5's HOOK ("you measured ECE = 0.03 — which word may you write?") is exactly S1's BOUNDARY. One ~8–10 min film "Same Number, Three Verbs / The Ladder Has Two Columns" is legal under the sectioning exception. Default remains two films.
- **S4+S2** share the reliability diagram and its bins. S2's HOOK ("global ECE 0.018 — so why 0.103 on the rare-disease row?") is S4's BOUNDARY ("the aggregate number is not the diagnosis"). The same dots stay on screen and get re-sorted by subgroup. One ~8 min film. Default remains two films.
- S3 stands alone (its object is the decomposed bar, not the diagram); S6 stands alone or folds into S5 as an INSTANCE (see its status note).

## What the chapter itself flags (carried into every card that touches it)
- **Seven unresolved git conflict blocks** (`<<<<<<< HEAD:chapters/11-…` / `>>>>>>> d78899b (Update chapters 1-14):chapters/12-…`): every figure is numbered both 11.x and 12.x; the AI-output caveat paragraph ("verbs carry action-warrant … the verb caught it") exists ONLY in the HEAD side; the "Preview of next chapter" says Chapter 12 (HEAD) vs Chapter 13 (d78899b); the AI Wayback Machine and the D3 Prompts sections exist only in the d78899b side. The book's `AGENTS.md` says not to silently resolve manuscript conflicts — cards cite figures as "11.x/12.x (conflict block)".
- **`[verify]` ×2 in the body** (a third `[verify]` mention is the CHAPTERIZED header comment): (1) the ECE rules of thumb 0.02–0.05 / > 0.10 — unsourced; (2) "overconfidence is the dominant failure mode … extended to LLMs" — Guo et al. 2017 vs Minderer et al. 2021, no canonical LLM study.
- **Subgroup table arithmetic**: the global row prints base rate 0.041, but the five subgroup rows N-weighted give ≈0.044 (571.4 / 12,955). The global ECE 0.018 is consistent (a pooled ECE may sit below the N-weighted mean of subgroup ECEs, ≈0.028, by cancellation within bins) — that cancellation is itself the S2 mechanism and worth a dim caption.
- **Brier notation**: the decomposition labels the resolution term REL and the calibration term CAL; in Murphy (1973) REL is *reliability* (the calibration term) and RES is resolution. Not wrong on the page, but a reader who checks the citation will trip. S3 must name which is which.
- The chapter header marks the whole file "Rough draft for hand-rewrite".
