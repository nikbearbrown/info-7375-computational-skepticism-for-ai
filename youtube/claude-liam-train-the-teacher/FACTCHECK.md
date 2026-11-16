# FACTCHECK — claude-liam-train-the-teacher

**Gate F.** Every factual claim spoken or shown in the reel, checked against the
two supplied documents.

## The verification boundary — read this first

This film is *about* a citation audit, so its own citation discipline has to be
stated exactly, not implied.

Two source documents were supplied:

1. **The essay** — Nik Bear Brown, "Not the App. Not the Ban. Train the
   Teacher.", skepticism.ai, 2026-05-16.
2. **The audit** — an adversarial evidence audit of that essay, dated
   2026-09-07, which verified, corrected or failed to verify each of the
   essay's citations.

**What was checked:** every claim in the narration against the audit document,
and every place the film characterises the essay against the essay text.

**What was NOT checked:** the audit's own primary sources. I did not open NBER
WP 34388, the WestEd cost report, Texas HB 1481 guidance, NY Education Law
§2803, the TALIS country note, the IES evaluation, or the Federal Register
notice. This session's knowledge cutoff precedes most of them, and several are
recorded in the audit itself as retrieved indirectly (the Figlio & Özek numbers
come from the authors' own Education Next account, not the working paper; the
audit says the original NBER retrieval failed).

**Precedence rule, applied throughout:** where the essay and the audit
disagree, the audit governs and the film says so on screen. This is a
second-order check — the film inherits the audit's confidence, and the audit's
own stated limits (below) travel with it.

**The audit's stated limits, carried forward:**
- Not a 50-state legal audit. The "31 states" count is unverified — so the film
  never says a number of states.
- The 3.5 million observation count is unverified — the film says so on screen
  (B10) rather than repeating or silently dropping it.
- Several originals were inaccessible; substitutes are identified in the
  audit's own source notes.

---

## Claim ledger

| # | Beat | Claim as spoken / shown | Verdict | Basis | Fix applied |
|---|---|---|---|---|---|
| 1 | B00 | Bear published the essay in May, then had it adversarially audited | HOLDS | Both documents; the audit's framing is explicitly adversarial | "He paid to have it attacked" → "He had it attacked". Payment is not established. |
| 2 | B00 | "Four of its sentences do not [survive]" | HOLDS | The film shows exactly four struck sentences (B09, B11, B13, B15) plus one reclassification (B25) and one false premise (B26). "Four" is a floor, not a total, and the film does not claim it is exhaustive. | — |
| 3 | B03 | The debate offered two answers: ban the device, buy the platform | HOLDS | Essay, verbatim structure | — |
| 4 | B04 | Best causal evidence on bans is one large Florida district; cost year one, benefit year two | HOLDS | Audit: "covers one large Florida district, comparing schools with different pre-ban phone use" | Film never says "statewide". |
| 5 | B09 | ~30% first-year increase = **in-school** suspensions, **Black students** | CORRECTS THE ESSAY | Audit, from the authors' May 2026 account | Essay said "Black boys"; film strikes it on screen. |
| 6 | B09 | No significant effect on out-of-school suspensions | HOLDS | Audit | — |
| 7 | B10 | ~1.1 percentile points overall; not significant for female or elementary students | HOLDS | Audit | Film explicitly retires the essay's "all groups benefited". |
| 8 | B10 | The 3.5M observation count is unverified | HOLDS | Audit says so in terms | Shown on screen as UNVERIFIED rather than dropped. |
| 9 | B11 | $46.23/student, 2021 dollars, includes platform maintenance and implementation support | CORRECTS THE ESSAY | Audit, Feng/Weiser/Collins 2024 | Essay said "entirely in teacher professional development". |
| 10 | B11 | 63 schools; 0.10 SD later 8th-grade maths | HOLDS | Audit | — |
| 11 | B12 | NCES 2021: 4% smartphone-only, 3% no home access, ages 3–18; 4/(4+3)≈57% | HOLDS | Audit | Film's whole beat is that the denominator is the seven, not the classroom. |
| 12 | B13 | Texas: specific exceptions, no general educational-use carve-out. New York: authorisation for a specific educational purpose | CORRECTS THE ESSAY | Audit, TEA HB 1481 guidance + NY §2803 | Essay's "Not one defines it" struck on screen as OVERSTATED. |
| 13 | B14 | NY §2803(7) bars suspension solely for device access; requires demographic enforcement reporting + mitigation plans | CORRECTS THE ESSAY | Audit | Essay said no new law addressed it. |
| 14 | B15 | 30/70 is WestEd, *Investing in Technology: The Learning Return*, August 2002, citing Wahl (2000) | CORRECTS THE ESSAY | Audit | Essay cited it undated and as current. 2002→2026 = 24 years; the film says "twenty-four years". |
| 15 | B17 | Kraft, Blazar & Hogan (2018): 60 studies, causal designs; 0.49 SD practice, 0.18 SD achievement | HOLDS | Audit | Film says "about half" and "about a fifth" in narration; exact figures on screen. |
| 16 | B18 | Larger effectiveness studies produce smaller effects | HOLDS (direction only) | Audit states the attenuation; it does **not** publish a pooled effect per scale tier | **FIXED.** First draft printed invented figures (0.31 → 0.11). The component now takes `showValue: false` and prints "larger" / "smaller". The bar still shrinks; no number is asserted. The on-screen note says why. |
| 17 | B19 | IES: ~200 4th-grade teachers, six districts, 93 hours; knowledge and some practices improved; no positive achievement effect | HOLDS | Audit | **FIXED.** First draft printed "+58" for the knowledge meter — a magnitude the source does not state. Now `showValues: false`; the meter fills, the number is gone. |
| 18 | B20 | The ASSISTments intervention was software + PD + warm-up year + ongoing support | HOLDS | Audit | — |
| 19 | B21 | Tutor CoPilot: 900 tutors, 1,800 K-12 students; +4pp topic mastery, +9pp for students of lower-rated tutors; end-of-year maths not significant | HOLDS | Audit | Working paper — labelled as such on screen. |
| 20 | B24 | Almost no trials of AI-specific teacher PD measured on student outcomes | **AUDIT-INFERRED — flagged** | The audit does not print this sentence. It (a) reclassifies the thesis as "a policy recommendation drawn from the evidence, not a proven universal spending formula", (b) proposes the missing trial design under "Test the additional value of sustained support", and (c) rules every supporting study to be about something adjacent. The film states the implication those three moves carry. | The on-screen note constrains it: "Not a claim that training fails. A claim that nobody has run the study." Each dissolving row names its own disqualifier, so the viewer sees the reasoning rather than taking the conclusion on trust. |
| 21 | B25 | "What the evidence shows" is properly a defensible bet | HOLDS | Audit's own framing, near-verbatim | — |
| 22 | B26 | Illinois requires 120 hours for licence renewal | CORRECTS THE ESSAY | Audit | Essay claimed the infrastructure does not exist. |
| 23 | B26 | Massachusetts: 50 CME credits per two-year cycle, not 50/year | HOLDS | Audit | On screen in the note. |
| 24 | B27 | TALIS 2024 US: 70% of non-AI-using teachers cite lacking knowledge/skills | HOLDS | Audit | — |
| 25 | B27 | 67% other responsibilities, 59% scheduling | HOLDS — **but a different survey item** | Audit: these are barriers to *professional learning*, not to AI use | **FIXED.** First draft treated all three as one list ("two of the three barriers are not about knowing"). Narration and chart labels now separate the two questions explicitly. |
| 26 | B29–B31 | The study design and its six measures | HOLDS | Audit's evaluation section, condensed | Presented as the audit's proposal, not as an existing trial. |
| 27 | B31 | Equal results in coached vs uncoached schools would falsify the thesis | HOLDS (logical consequence of the proposed design) | — | **FIXED.** `showValues: false` — a hypothetical result must not wear a numeral. |

---

## Stripped — claims present in the essay that the film deliberately does not use

| Claim | Why it was cut |
|---|---|
| "$165 billion EdTech market" | Audit: omit unless year, geography and market definition are sourced. No source supplied. |
| "Thirty-one states enacted one" | Audit: unverified, and needs a definition distinguishing full-day from instructional-time restrictions. The film says "phone-ban statutes" and never counts. |
| "A five-dollar-per-student AI tool is genuinely better than no tool" | Audit: unsupported guarantee. Cut. |
| "A great teacher trained in AI will outperform any expensive platform" | Audit: remove the universal superiority claim. Cut — the film's B22 replaces it with "supported implementation". |
| "It costs less to build than the hardware budgets it would replace" | Audit: requires a costed proposal. Cut. |
| "Fewer than 40 percent of districts use Title II-A for technology-enabled learning" | The audit shows the denominator is districts that funded teacher PD through Title II-A, from 2022–23 data predating widespread generative-AI adoption. Too many caveats to carry in a spoken beat without misleading; cut rather than half-stated. |
| Muralidharan et al. (Mindspark) effect sizes | Real, but Indian after-school setting; the audit warns against transferring them to US classrooms. Cut rather than caveated into meaninglessness. |
| Bastani et al. guardrails result | The audit deliberately omits headline numbers (correction text inaccessible). Film follows suit and omits the study. |
| FCC E-Rate hotspot rescission | Kept out of the film. The audit narrows it substantially — a *planned* support pathway was cancelled, not an operating connection withdrawn — and the essay's "both removals, same students, simultaneously" does not survive that. Too long to correct properly inside this film's arc; noted here so the omission is deliberate, not an oversight. |

---

## Datable material (DOUBLE-CHECK LAW)

- No model names, tool versions or vendor product names in the narration.
- No "as of [month]" constructions.
- Dates appear only where the date **is** the point: the 2002 WestEd brief
  (B15) and the 2021 NCES estimates (B12).
- "May" and "twenty-four years" in B00/B15 are anchored to the essay and the
  brief, both of which are fixed points.

## Gate F verdict

**PASS**, with one flagged inference (row 20, B24) and four defects found and
fixed before audio spend (rows 16, 17, 25, 27 — three invented numerals and one
conflated survey item). The flagged inference is disclosed on screen in the
beat's own note.
