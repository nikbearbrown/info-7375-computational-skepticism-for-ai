# FACTCHECK — tldr-five-boxes-one-deployment

Status: **GATE F verified 2026-09-23 by Claude (Opus 5.5) — every claim checked against `chapters/12-accountability-who-is-responsible-when-the-system-fails.md` (read whole this session; no merge-conflict blocks in this file); the counts (5 requirements, 4 sentences, 3 word-filed boxes, 2 blank, 0 passed) are asserted in `make_sheet.py`. Human sign-off pending.**

Source: chapter 12 §"The five accountability requirements and the tiers they depend on" and its checklist table (the BODY list — Specifications · Audit trail · Recourse · Independent review · Sanctions — not the LLM Exercise's renamed list), Application A2, and the SyRI paragraph of §"The regulatory landscape". Section S5 of `youtube/tldr-sections-12-accountability.md`.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B01 | Course credit: chapter twelve of INFO 7375, Computational Skepticism for AI, Northeastern | ✓ PASS | course-film convention (spoken + cards' course line) | — |
| 2 | B10, B11, B19 | The four A2 sentences, quoted verbatim | ✓ PASS | Application A2, word for word ("The system flags posts for review. Moderators can appeal a flag by contacting the support team. The company's trust and safety team reviews reported issues periodically. The system has been running for 18 months.") | — |
| 3 | B10 | A2 is an exercise scenario, captioned "constructed exercise case" | ✓ PASS | A2 is posed as "evaluate the following description" — a hypothetical audit case, not a named company | — |
| 4 | B10, B13, B19, B02 | "running for 18 months" — never "18 months without incident" | ✓ CORRECTED | A2 states only the running time. The sections card's question ("run for 18 months with no incident") overstated the text; the film says "running" only (asserted in make_sheet.py) | card wording not reused |
| 5 | B11, B14, B18, BVDT | The five requirements are specifications, audit trails, recourse, independent review, sanctions | ✓ PASS | §"The five accountability requirements…", first paragraph and checklist table | — |
| 6 | B14, BHTF | Specifications test: can a reviewer predict what counts as success | ✓ PASS | table: "A reviewer can read the spec and predict what counts as success" | — |
| 7 | B14, BHTF | Audit-trail test: rebuild an incident in under an hour | ✓ PASS | table: "Pull a random recent incident; can the chain be reconstructed in under an hour?" | — |
| 8 | B14, BHTF | Recourse test: can an outsider find the channel and use it | ✓ PASS (paraphrase) | table: "An external party can read the channel description and use it" | — |
| 9 | B14, BHTF | Review test: someone named, outside the team, able to halt it | ✓ PASS (paraphrase) | table row: "A reviewer outside the deployment team with authority to halt or revise"; test "Named reviewer; documented review cadence; visible halt authority" | — |
| 10 | B14, BHTF | Sanctions test: can a named role lose something | ✓ PASS (paraphrase) | table: "Pull the policy; can a specific named role lose something specific for a specific failure?" | — |
| 11 | B14, B16, B19 | Failure modes shown: "“the model said so” is the audit" · "review reconstructs nothing" · "routes to support, no resolution" · "the company grades its own work" · "no one bears the cost" | ✓ PASS (condensed) | table "Failure mode if absent" column; "grades its own work" is the body text's "the deploying organization is grading its own work" | — |
| 12 | B11, B12, B13 | A word-matching reader files three sentences into three boxes and leaves two blank | ✓ PASS (our derivation) | Sentence 1 → Specifications, 2 → Recourse, 3 → Independent review; A2 never mentions logs or consequences (asserted) | — |
| 13 | B14 | Specifications fails: "flags posts for review" names a task, no success criteria | ✓ PASS (our derivation) | Chapter's spec = "named acceptance criteria, signed by an accountable human"; A2 gives neither | — |
| 14 | B16 | Recourse fails: the appeal is given to moderators, via support; the flagged poster is given no channel | ✓ PASS (our derivation) | A2's only appeal sentence names moderators and "the support team"; the chapter's failure mode names exactly "complaints route to 'support' with no resolution path" | — |
| 15 | B16 | Review fails: the company's own team, "periodically", no named reviewer, no halt authority | ✓ PASS (our derivation) | A2 sentence 3 vs the test "Named reviewer; documented review cadence; visible halt authority" and "outside the deployment team" | — |
| 16 | B16, B19, BVDT | Zero of five pass | ✓ PASS (our derivation) | rows 13–15 plus silence on audit trail and sanctions; asserted `sum(PASSES) == 0`. The chapter poses A2 without an answer key; this is the film's reading, stated through the chapter's own tests | — |
| 17 | B13, BVDT | "a clock, not a check": running time is not one of the five requirements | ✓ PASS (our derivation) | none of the five rows or tests mentions running time | — |
| 18 | B19 | Eighteen months without an audit trail is eighteen months nobody could reconstruct | ✓ PASS (hedged) | table failure mode for a missing audit trail: "Post-incident review reconstructs nothing" | — |
| 19 | B18, BVDT | "a slogan, not a practice" for a regime that cannot tick all five | ✓ PASS | table caption: "A regime that cannot tick all five boxes is a regime in which AI accountability is a slogan, not a practice" | — |
| 20 | B18 | "audit instrument" | ✓ PASS | "The checklist below turns the five into a reusable audit instrument"; table caption "Designed as a reusable audit instrument" | — |
| 21 | B17 | SyRI: a Dutch welfare-fraud (risk-)scoring system | ✓ PASS | §"The regulatory landscape": "The Dutch welfare-fraud risk-scoring system" | — |
| 22 | B17, BVDT | SyRI's recourse and independent review existed on paper and not in function | ✓ PASS | same paragraph, verbatim sense | — |
| 23 | B17 | Struck down by a court in The Hague in 2020 | ✓ PASS | "struck down by The Hague District Court in 2020"; NJCM c.s. v. The Netherlands, ECLI:NL:RBDHA:2020:865, 5 February 2020 | — |
| 24 | B17 | The court supplied the review and the sanction the system had not built in — late, from outside, after the harm | ✓ PASS | "The court supplied the independent review and the sanction the regime had failed to build in — late, externally, after the harm had landed" | — |
| 25 | B19 | Not taught: who must hold each box and why it must be a person | ✓ PASS | boundary; the chapter's answer rests on the Irreducibly Human tiers (its one `[verify]`), kept out of the film | — |
| 26 | B03 | Term definitions (specification, audit trail, recourse, sanction) | ✓ PASS (paraphrase) | table "What it consists of" column | — |
| 27 | BHTF | The transfer exercise is the viewer's own audit | EXEMPT | a prompt for the viewer; no model output shown | — |
| 28 | all | Nothing datable: no model names, product names, versions or "as of" claims; the only date is the 2020 ruling (a historical event) | ✓ PASS | sweep of the sheet | — |

**Kept out (by rule):** the *Irreducibly Human* tier taxonomy and every tier label (the chapter's one `[verify]`, "the load-bearing dependency"); A2's "which cognitive tier" sub-question; "most deployed AI systems are missing two or more" (uncited in the chapter); the EU AI Act penalties and NIST items (the chapter says this section "ages fastest"); SyRI's legal ground (right to private life) — true per the chapter but not needed.
