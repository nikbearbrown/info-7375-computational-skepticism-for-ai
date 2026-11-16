# tldr sections — Chapter 3: Data Validation: Reconstructing the Epistemic Frame Behind a Dataset

Source: `chapters/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 5 sections · 4 deferred · course film: carries the course credit (bookloop exception)

Already on this chapter, different genre: `claude-liam-deep-03-data-validation/` ("The Data Is Clean. That's the Problem.", deep-explainer register, 8m31s per DEEP-EXPLAINERS-INDEX) plus the shorts `claude-liam-cs-04-clean-but-broken` (the clean missing-values check), `claude-liam-cs-24-mnar-bias` / `claude-liam-vox-missing-mnar` (MNAR) and `claude-liam-cs-25-proxy-column`. A tldr film is additive: one aha, taught 3b1b-style, not a walk of the chapter.

Duplicate-version note: `chapters/05-data-validation-…` (10,714 words) is the pre-chapterization copy of this chapter (8,992 words); the deep-explainer index treated it as the older duplicate and it was NOT sectioned here. It does hold material 03 lacks: a TL;DR + learning objectives block; the procedural pass as sub-headed Steps 0–6 with 4 code blocks (03 has 2); a fuller marks-and-channels section — marks and channels defined, the Cleveland–McGill channel hierarchy as Figure 5.7, the **expressiveness** and **effectiveness principles** with Figure 5.8 (size-for-categorical), pie-chart guidance; an AI Wayback Machine (Suzanne Briet); and figure prompts. 03 has no figures 3.7/3.8 and never explains the two named principles — yet 03's exercises 4 and 13 and its chapter summary still test them. The opener's numbers (three source systems, four-percent drop) match across both files. If S3 builds and wants the principle names, they come from 05.

Chapter flags carried into the cards: the header comment marks the file "Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved". In-body: **[verify]** at the opener (the join case is a composite, not a sourced incident) and "[Verify: current scope of Great Expectations, Deequ, and successor tools before publication.]" under "What would change my mind". No `[verify-xref]` survives in the body.

Ranked by how visible the representation already is in the source (a figure with a contrast first, then the chapter's own numbers, then diagrams of procedures).

## S2 · Missing Is Not One Thing                                        tier: single-insight
- question:        Two columns each have 18% blanks. Why is one safe to fill in and the other a trap?
- key case:        `income` with 18% missing, the blanks co-occurring with the `age < 25` subgroup (exercise 8) — versus the same 18% where the high earners are the ones who left it blank (the chapter's MNAR example)
- naive:           fill the blanks with the column mean (or the age-group mean) — fine for the first, and for the second "standard imputation produces bias in exactly the direction I cannot measure"
- representation:  the missingno matrix (Figure 3.2, rebuilt): rows as lines, columns as stripes, dark where absent. Three versions of the same 18% side by side — scattered dots (MCAR), dark cells aligned with the age stripe (MAR), dark cells aligned with a hidden true-income bar the matrix cannot draw (MNAR). The first and third look identical from inside the data; only when the hidden bars are revealed does the imputed mean slide away from the truth.
- abstraction:     Rubin's taxonomy — MCAR / MAR / MNAR — is whether the chance of a blank depends on nothing, on something you can see, or on the missing value itself; procedural EDA cannot detect MNAR at all, you detect it by reasoning about who would not report
- boundary:        choosing an imputation method; a row dropped in a join is not "missing" in any sense the matrix can register → S1
- terms (prereq):  missing value, impute, subgroup
- equations:       none (the taxonomy is stated in words; nothing to tangent)
- predict beat:    "Same 18% blank. Which of these two fills in safely?" before the hidden bars appear
- source span:     §"The procedural EDA pass" ¶Missingness (+ footnote Rubin 1976); Figure 3.2; failure table row "Missing not at random (MNAR)"; exercise 8
- status:          published (unlisted) → tldr-missing-is-not-one-thing · https://youtu.be/-FZsJZmFYPo · 2026-09-24

## S1 · Why Are There Exactly N Rows?                                   tier: single-insight
- question:        The missing-values check came back at zero. How can the dataset still be missing people?
- key case:        the chapter's opener — three source systems joined on a shared identifier, a four-percent drop rate, one subpopulation whose identifier was formatted inconsistently in one system, so the drop lands on them; EDA clean, deployment fails on exactly that subpopulation. **[verify]** carried: the chapter flags this as a composite of "silent-join pathologies", not a sourced incident — the film must say so on screen. Companion numbers from exercise 1 (a DIFFERENT two-system scenario, do not fuse): CRM documents 85,000 active customers, merged table has 79,400 rows (gap 5,600)
- naive:           run the missing-value count → 0% → "clean"; then blame the model — retrain, tune, regularize — and the failure persists
- representation:  two row-strips, "supposed to be" over "is", with the join as a sieve between them: rows that fall through never reach the frame, so the missingness matrix underneath stays entirely light. Then the same 4% dropped twice — spread evenly (both strips shrink uniformly, nothing downstream changes) vs concentrated in one coloured subpopulation (that colour vanishes from the training strip and reappears in the deployment strip)
- abstraction:     N is the residue of a process, not a fact about the world; "you cannot compute the missingness of rows that never existed" — the question the pass never asks is N_expected vs N_observed
- boundary:        tracing a row back to its source system (Step 5); MNAR proper (S2); which of the two causes a temporal drop has (Figure 3.4 / exercise 6 as a post-shift INSTANCE, not a film)
- terms (prereq):  join (on a shared key), row / record, subpopulation
- equations:       N_expected − N_observed (arithmetic: 85,000 − 79,400 = 5,600 in the exercise scenario; no tangent)
- predict beat:    "Four percent of rows fell through. Does it matter WHICH four percent?" before the second drop plays
- source span:     opener ¶1–9, Figure 3.1; §"The procedural EDA pass" closing ¶ ("none can see what was never written"); exercises 1, 12
- status:          pick  (note: overlaps `cs-04-clean-but-broken` and the deep-03 cold open in subject; differs in genre)

## S3 · Position Beats Colour                                           tier: single-insight
- question:        Two cells on a correlation heatmap — is 0.43 really different from 0.51? Why can't your eye tell?
- key case:        the chapter's own heatmap caveat: 0.43 vs 0.51 encoded as colour intensity is "unreliable"; the same pair as two positions on a common scale is read almost faithfully (Cleveland & McGill 1984 — the load-bearing citation; Stevens 1957 is "the mood, not the finding")
- naive:           "the plot looks clean, so the data is" — treating a chart as a neutral window instead of an encoding
- representation:  the same two numbers, 0.43 and 0.51, encoded four ways on one stage — position on a common axis, bar length, circle area, colour intensity — and the viewer asked to rank them each time; the gap between the two is plainly visible in the first two and gone by the fourth. Then the heatmap cell and its number side by side. (All four encodings rebuilt in Manim — REBUILD LAW; 03's Figure 3.6 is a marks+channels illustration, the hierarchy figure exists only as 05's Figure 5.7)
- abstraction:     channels are not interchangeable — position, then length, with area and colour intensity "well down the list", empirically; a chart is an argument made through which variable gets the strong channel; a heatmap is an overview tool, confirm the number before you act on it
- boundary:        the expressiveness and effectiveness principles (tested by 03's exercises 4/13 but only explained in the 05 duplicate); Pearson-is-linear-only (y = x² correlating near zero) as one line; "what is the chart NOT showing?" → the interrogation (S1, S4)
- terms (prereq):  correlation coefficient (a number between −1 and 1), heatmap, histogram
- equations:       none
- predict beat:    "Which of these two cells is bigger?" on the colour pair, before the positions are revealed
- source span:     §"A chart is an argument — and the argument is in the encoding" (+ footnotes cm, stevens); Figure 3.6; §"Bivariate relationships" ¶; exercises 4, 5, 13
- status:          pick

## S4 · The Boundary Is Not the Schema                                  tier: single-insight
- question:        No access control was violated. So how did the agent surface phone numbers nobody authorised?
- key case:        the chapter's email-corpus agent (echoing the "Ash" agent case in *Agents of Chaos*, Shapira et al. 2026, arXiv:2602.20021): the team draws the boundary at the corpus and sets access controls; the agent's answer surfaces, from message bodies, phone numbers, addresses, credit-card fragments, references to internal documents outside the corpus, and third parties who never consented
- naive:           validate the corpus — the records that are present — and treat the schema as the edge of the data world
- representation:  Figure 3.9 rebuilt as a concentric boundary: the schema box with the access-control wall drawn on its edge; edges grow out of the message bodies to nodes outside the box (a phone number, an internal doc, a third party); the agent walks the edges and never crosses the wall. Second case, one thing changed: a self-contained table of temperature readings — no edges grow, wall and boundary coincide
- abstraction:     the boundary of a dataset is the schema ∪ everything its contents reference, link to, or imply — a spectrum, sharpest at the email end, near-absent at the sensor-log end; the validation question is "what is the boundary of this data, and how do I know?"
- boundary:        the chapter admits it has no scalable diagnostic for this ("What would change my mind"); Chapter 8 takes it up from the agent-validation side; exercise 7 (Slack workspace, public channels only, no DMs, no files) is the transfer
- terms (prereq):  schema, access control, corpus
- equations:       none
- predict beat:    "The wall holds. Does the agent stay inside it?" before the edges grow
- source span:     §"The access assumption — and where the boundary really lives" (+ footnote chaos); Figure 3.9; failure table row "Access/boundary assumption"; exercise 7
- status:          pick  (note: Ash is the agent in Agents of Chaos, not a researcher; the deep-03 film already carries this case in the deep register)

## S5 · Lock the Prediction First                                       tier: single-insight
- question:        You wrote up what the data turned out to be. Why does it feel like you learned nothing?
- key case:        Step 3's worked gap: you predicted the dataset holds a year of records; the row count is consistent with maybe nine months — "that gap is a finding. Pursue it."
- naive:           read the metadata, run the EDA, write the frame you finally arrived at — which "feels obvious in retrospect", so no gap ever existed and you "don't notice you've learned anything"
- representation:  two runs of the six-step procedure side by side, one state at a time (Figure 3.10 rebuilt as a strip of six boxes). Left: a prediction card written and LOCKED at Step 1 ("12 months"), the record-count bar filling to 9 of 12 at Step 3, and at Step 6 both cards held up together — a visible three-month gap. Right: no card at Step 1; the same bar fills to 9; at Step 6 one card, "9 months", and nothing to compare it to. Same data, same finding; one run learns and one does not
- abstraction:     the epistemic frame is what you write at Step 6 minus what you wrote at Step 1; without the prediction-lock the gap has no left-hand side
- boundary:        Steps 4–5 in full (dropped joins, fields documented but absent, tracing one row to its source — or "document the opacity" when the source is unreachable); Glimmer 3.1 is the practice → YOUR TURN: any public dataset, lock a prediction, run the six steps (exercise 9: "the honesty of the prediction-lock is" what's graded)
- terms (prereq):  metadata, schema documentation, record count
- equations:       none
- predict beat:    "Before the bar fills — how many months do you think are in here?" (the film performs the lock on the viewer)
- source span:     §"Reconstructing the epistemic frame — a working procedure"; Figure 3.10; Glimmer 3.1; exercise 9
- status:          pick  (weakest representation of the five: Figure 3.10 is a workflow diagram, not a case, and the nine-of-twelve months is the only number)

## Deferred / not-yet-sectionable
- **Label assumption** ("re-arrest is not crime; a click is not interest; survival is not health") — stated as a list, no worked case and no number; a film would have to invent proxy-vs-construct data and fact-check it as its own. `not-yet-sectionable`. Partly covered by `cs-25-proxy-column`.
- **Feature-engineering assumption** (`customer_lifetime_value` is "somebody's model, baked into your input layer") — asserted, no case. `not-yet-sectionable`.
- **Sampling / time-window assumptions** — asserted in prose, and the sampling paragraph appears twice. The one concrete case (exercise 6: imaging records Jan 2018–Dec 2022, a sharp drop March through June 2020; Figure 3.4) is folded into S1 as a post-shift INSTANCE ("a sharp drop is always a finding; the chart hands you the finding, not the cause"). `deferred` — not its own film.
- **IQR outlier triage** ($1,200,000 salary: decimal-point error / legitimate CEO / sentinel for "unknown"; Q₁ − 1.5×IQR, Q₃ + 1.5×IQR; Figure 3.5) — sectionable (one flagged dot, three worlds it could mean) but a tools beat, not the chapter's aha. `deferred`, low priority.

## Not sectioned (by design)
- Strategic delegation table (delegate freely / verify before trusting / do not delegate) — a policy, not a lesson; its "do not delegate" row is S5's abstraction restated. Solve–verify asymmetry already has its own reel (`solve-verify-asymmetry`).
- Types-first, shape, univariate, bivariate, temporal paragraphs — a tools tour the chapter itself calls "not a pandas tutorial"; their shared blind spot ("none can see what was never written") is S1's SHIFT.
- Plato's Cave and Hume framing, Datasheets for Datasets (57 questions), the tooling-aging note, What would change my mind, Synthesis, Connections forward, Exercises, Chapter summary, the LLM Exercise (Red-Team Casebook "Data Frame Audit") — front/back matter and practice.

## Multi-act candidates (need explicit approval)
- S1+S5 share the N-rows question end to end: S1 lands "N is a residue", S5's key case (nine of twelve months) is the same question asked with a lock, and S5's HOOK is S1's BOUNDARY. One ~8–10 min "Why Are There Exactly N Rows?" is legal under the sectioning exception. Default remains two films.
- S1+S2 do NOT qualify: adjacent ideas (a dropped row is not a "missing" value) but different key cases (join vs `income`).

## Unresolved in the chapter itself (for the hand-rewrite, not for the films)
- The "six structural failures" are unstable: the table names six (sampling, time-window, label, MNAR, feature-engineering, access); the prose adds schema-and-provenance as a seventh and states sampling twice; the LLM Exercise names a different six (scope, sampling, definition, joining, time, access).
- Figures jump 3.6 → 3.9 → 3.10; 3.7/3.8 exist only in the 05 duplicate. Exercises 4/13 and the summary test principles the 03 body no longer explains.
- Two in-body verify flags (composite opener; Great Expectations/Deequ scope), plus the header "rough draft" marker.
