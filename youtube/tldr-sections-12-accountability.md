# tldr sections — Chapter 12: Accountability: Who Is Responsible When the System Fails?

Source: `chapters/12-accountability-who-is-responsible-when-the-system-fails.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 6 sections · 0 deferred · 2 not-yet-sectionable · course film: carries the course credit (bookloop exception)

Already on this chapter, different genre (deep-explainer register, not lessons): `claude-liam-deep-12-accountability/` ("The Signature the Machine Can't Sign", 39 beats, 9m26s, per `DEEP-EXPLAINERS-INDEX.md`). A tldr film is additive: one aha, taught 3b1b-style, not a walk of the chapter.

Duplicate-version note: `chapters/13-accountability-…` (13,093 words) is the older copy the deep-explainer index treated as superseded; only the 12 file was sectioned. 13 does carry material 12 lacks — a standalone "Generative AI and the accountability topology" section (misuse surface, provenance via watermarking/content credentials, its own `[verify]` on copyright guidance), a John Dewey "AI Wayback Machine" (*The Public and Its Problems*, 1927), a "Figure 13.6 — Generative vs" figure and the D3 figure prompts. 12 folds the generative point into one paragraph and drops Dewey. 12 in turn has what 13 lacks: the attestation gate, the regime trade-off section, Matthias/Santoni de Sio citations, the SyRI ruling and the Epic Sepsis audit (C3). Nothing in 13 changes a card below; Dewey would be a TANGENT candidate for S1 if the human wants it.

Chapter flags carried: the file header marks it `Rough draft for hand-rewrite`; one `[verify]` (the *Irreducibly Human* tier taxonomy is the author's forthcoming, uncheckable source — the chapter itself calls it "the load-bearing dependency"). Every card that names a tier inherits that flag. Figure numbering skips 12.6 (12.1–12.5, then 12.7).

Ranked by how visible the representation already is in the source (tables and worked text first).

## S5 · Five Boxes, One Deployment                                       tier: standard
- question:        The system has run for 18 months with no incident — so it's accountable, right?
- key case:        the A2 audit text: "The system flags posts for review. Moderators can appeal a flag by contacting the support team. The company's trust and safety team reviews reported issues periodically. The system has been running for 18 months."
- naive:           "there's an appeal, there's a review team, it's been fine for 18 months" — presence of words for each requirement mistaken for the requirement
- representation:  the five-row checklist (Specifications · Audit trail · Recourse · Independent review · Sanctions) filling one row at a time against that sentence; each row gets its "how to verify" probe run live ("can an external party read the channel and use it?"), the box stays empty, and the "failure mode if absent" column lights: "complaints route to support with no resolution path", "the deployment team marks its own homework", "no one bears the cost"
- abstraction:     a requirement is present only when its verification probe passes; a regime that cannot tick all five is "a slogan, not a practice" — and each empty box names a specific human job (Tier 4 / Tiers 3+6 / Tier 7 `[verify]`)
- boundary:        WHY those jobs cannot be an AI's (S4); which tier each needs is scaffolding from an unpublished taxonomy → YOUR TURN: run the five probes on a deployment you use
- terms (prereq):  specification, audit trail, recourse, sanction (as plain words; the tiers arrive at the end, flagged)
- equations:       none
- source span:     §"The five accountability requirements and the tiers they depend on" + checklist table; Application A2; SyRI paragraph in §"The regulatory landscape" as a second INSTANCE (recourse and review "existed on paper and not in function")
- status:          built → tldr-five-boxes-one-deployment (master 2026-09-23 15:07, verdict pending)

## S2 · Two Frameworks, One Topology                                    tier: single-insight
- question:        If Kant and Mill disagree about everything, why do they give the same answer here?
- key case:        the mail-server deletion (Agents of Chaos §16.5) run through both tables: Kantian magnitude low / zero / high / high / medium-high; utilitarian leverage small / none / high / highest / medium — for non-owner / agent / owner / framework developers / model provider
- naive:           pick a framework, get a verdict, name the culprit — one framework, one answer
- representation:  one five-row table with two columns filling side by side: Kantian = capacity × duty, utilitarian = leverage on future failures; the agent row goes to zero in BOTH columns for different reasons; the mass sits on multiple rows in both; the utilitarian column tilts upstream (framework, provider)
- abstraction:     "Two frameworks. Different bases. Same topology. Responsibility distributes, and the distribution is the finding." — with the utilitarian sharpening: highest leverage is often upstream of the proximate party
- boundary:        whether a different architecture SHOULD consolidate responsibility (strict liability, vertical integration) is a values choice → C2 as YOUR TURN
- terms (prereq):  Kantian (capacity to act otherwise + duty), utilitarian (best aggregate outcome / deterrence), proximate cause
- equations:       Kantian responsibility ∝ capacity × duty (the chapter's words; a TANGENT if written as symbols)
- source span:     §"Two frameworks, one topology" + the Party × Kantian/Utilitarian table
- status:          pick

## S1 · Necessary, Not Sufficient                                       tier: single-insight
- question:        Five parties, one deleted mail server — who is at fault?
- key case:        Agents of Chaos §16.5: a non-owner's natural-language request; the agent accepts tone/plausibility as authority; the owner granted privileged access; the framework treated identity as a signal not a credential; the provider's training set the defaults — the agent complies, reports success
- naive:           the suspect list — walk the five candidates looking for the one real culprit; every candidate has a reason, none is the answer
- representation:  Figure 12.1 rebuilt: five nodes on a path to the failure; toggle any ONE node off and the path breaks (each necessary); light any one node ALONE and nothing reaches the failure (none sufficient); the culprit search is replaced by a distribution — shading spread over the nodes
- abstraction:     "Each one's choices were necessary; none was sufficient" → Matthias's responsibility gap (2004) and Santoni de Sio & Mecacci's four gaps (2021): closed by design (humans placed where answerability is required), not by finding one guilty party
- boundary:        how to weight the shading (S2); why a human must sit at the nodes at all (S3/S4); emergent multi-agent failures where no node even cumulatively determined the outcome (the chapter's "still puzzling") → YOUR TURN: W1 on the medication-dosage case (A1)
- terms (prereq):  autonomous agent, privileged access, authority signal
- equations:       none
- source span:     chapter opener through §"…responsibility gap" paragraph; Figure 12.1; Warm-Up W1, W5
- status:          pick  (overlaps the deep-explainer's opening case in subject; differs in genre)

## S3 · The Shape of a Sign-off                                          tier: single-insight
- question:        The AI wrote a perfectly good sign-off with my name on it — what's missing?
- key case:        the chapter's three-second experiment: *"Write me the sign-off statement for the model we just validated."* → "This model has been validated against the acceptance criteria and is approved for deployment. Reviewed and signed, [Your Name]."
- naive:           it names a person, asserts a review, says approved — the form is complete, so the accountability is complete
- representation:  the generated sentence decomposed on stage into its four claims (a review happened · criteria were met · a named person · approved), each with an empty evidence slot beneath; then the four-part attestation built beside it — what was tested / what was NOT tested / who cleared which gate / calibrated verbs — and part 2 is the box the machine leaves blank because "it does not know what it did not do"
- abstraction:     answerability: accountability is a relationship between a judgment and the person who made it — the obligation to revise, face, reckon; "an AI can produce the words of accountability. It cannot produce the thing." The signer's authority to WITHHOLD the signature is what separates a gate from a rubber stamp
- boundary:        the trade-off the regime buys (speed, deniability) and why deployments route around it — one line; WHY the machine can't fill part 2 is S4 → YOUR TURN: A6, write the "what was NOT tested" section for a bank's customer-service LLM (four conditions)
- terms (prereq):  acceptance criteria, sign-off, gate
- equations:       none
- predict beat:    "Which of the four parts will the model never write?" before the attestation fills
- source span:     opener paragraph ("Before I ask who is at fault…"); §"The Gödel argument" answerability paragraph; §"The gate: the attestation you sign"; §"What the attestation regime optimizes for"; Synthesis S4
- status:          pick

## S6 · The Regime Produces a Different System                          tier: single-insight
- question:        Would the deletion still have happened if we'd just trained a better model?
- key case:        the mail-server case replayed under one changed variable: a regime requiring cryptographic authority verification instead of a social-signaling authority model — same agent, untouched weights; the authority signal it was tricked by is never presented
- naive:           "the model behaves better" — fix the algorithm, retrain, add a monitor; the counterfactual lives in the parameters
- representation:  Figure 12.5 rebuilt as Pearl's ladder with the regime as a rung ABOVE the model: Rung 1 sees the data, Rung 2 the model, Rung 3 the regime that produced both; two side-by-side runs of the identical agent differing only in the regime box upstream — in one the request carries an authority signal, in the other that signal does not exist, and the path to deletion never forms
- abstraction:     the governance counterfactual: "what regime, if implemented before the failure, would have prevented it?" — the regime is the intervention; "the counterfactual is not 'the model behaves better'. It is the regime produces a different system." Most catastrophic AI failures are regime failures
- boundary:        the causal identification (regime change CAUSED vs correlates) is Tier 5 work the chapter says the model can't do `[verify]` — asserted, not shown; multi-agent emergent failures out of scope → YOUR TURN: Glimmer 12.1 with prediction locked, on COMPAS / Apple Card / SyRI / an own case
- terms (prereq):  Pearl's ladder (Rungs 1–3, from Ch 4), intervention, counterfactual
- equations:       none (Pearl's do-notation optional in Glimmer 12.1; a TANGENT only if the plan writes it)
- source span:     §"Closing Pearl's Rung 3"; Figure 12.5; Glimmer 12.1; Application A4
- status:          pick

## S4 · The First Opinion Run Twice                                      tier: single-insight
- question:        Why not have a second AI check the first one?
- key case:        the Ash case (Ch 1, recalled here): the agent's completion report was in the audit trail and the trail was wrong; the email still existed on Proton Mail; only an independent state check — a human looking at the world, not the log — caught it
- naive:           redundancy: two checkers are better than one; the monitor catches what the monitored misses
- representation:  Figure 12.4 rebuilt: two systems drawn on the same foundation (similar data, similar architecture); their blind-spot regions overlap almost exactly, so the wrong-but-plausible output passes both; then a checker drawn OFF the shared base — the world / a human with stakes — whose blind spot does not coincide; the correlated check vs the independent one differ in one respect: what they stand on
- abstraction:     common cause failure — a monitor built like the system it monitors "is not a second opinion, it is the first opinion run twice"; independence requires a validator outside the system, and "outside" ultimately means answerable (something to lose)
- boundary:        Gödel is an analogy, not a proof — the chapter's own guardrail; the load-bearing arguments are common cause + answerability; whether a Tier 4/5 AI could ever be built is the author's stated change-my-mind → YOUR TURN: W6
- terms (prereq):  audit trail, redundancy, independent validation
- equations:       none
- source span:     §"Common cause failure"; Figure 12.4; §"The Gödel argument" (the guardrail paragraph); the audit-trail paragraph of §"The five accountability requirements…"; §"What would change my mind"; Warm-Up W4, W6
- status:          pick  (note: the key case is carried from Chapter 1 by reference; the chapter cites it without restating the specifics — the plan must pull them from `chapters/01-…` at factcheck)

## Not-yet-sectionable (reason logged)
- §"AI as extended mind" + the 16-row capacity table + the seven-tier taxonomy — the source states the abstraction (episodic memory / moral salience / metacognition are absent) without a case; the tiers rest on the chapter's one `[verify]` (forthcoming, uncheckable). Any key case would be ours and would have to be fact-checked as ours. The tiers enter S5/S6 only as the flagged label at the ABSTRACTION.
- §"Stages and stakes" table (low / moderate / high stakes × oversight intensity) — categories with example lists, no worked case; its one sharp line ("a human can be present at every stage and still supply nothing") is S3's rubber-stamp boundary, not a film.

## Not sectioned (by design)
- §"The regulatory landscape" (EU AI Act 2024/1689, €35 M / 7% penalties, NIST AI RMF, NIST agent initiative Feb 2026) — the chapter says it "ages fastest"; SyRI (ECLI:NL:RBDHA:2020:865) survives as an INSTANCE in S5.
- §"Why responsibility resists clean attribution" — restates S1 as a testable structural claim plus the generative-AI flattening; a BOUNDARY line in S1/S2, not a section.
- §"What would change my mind", §"The shape of the rest", Exercises, the LLM Exercise (Red-Team Casebook), tags — back matter; the exercises feed the YOUR TURN beats above.
- Epic Sepsis Model (C3, Wong et al. JAMA IM 2021) — a strong audit case, but the chapter gives it only in the exercise with no numbers; an alternative INSTANCE for S3 or S5 if the human prefers a medical case to content moderation.

## Multi-act candidates (need explicit approval)
- S1+S2 share the mail-server case end to end; S2's HOOK ("who gets how much?") is S1's BOUNDARY. One ~7–9 min film "Who Is Responsible" is legal under the sectioning exception. Default remains two films.
- S1+S6 share the same case; S6 replays it under a changed regime. S6's HOOK is S1's "what would have prevented it" boundary. Also legal; three-act S1+S2+S6 would be the chapter's full arc on one object (~11–13 min) and needs the human's explicit yes.
- S3+S4 share the "shape vs substance" spine (the empty sign-off; the AI-checks-AI checker) but not a key case — NOT a multi-act candidate under the rule.
