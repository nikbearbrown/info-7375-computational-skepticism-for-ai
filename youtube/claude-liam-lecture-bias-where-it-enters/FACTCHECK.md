# FACTCHECK — Bias: Where It Enters and Who Is Responsible (Lecture 6)

**What.** Gate F: every number and named claim in the narration or on screen, checked against its primary, with what was changed.
**Why.** This lecture is about real organisations and real people; nothing is stated about a named organisation without a primary, and Bear's own arguments are attributed as arguments.
**Found.** Primaries fetched 2026-10-10: the ProPublica article, the arXiv abstract of Kleinberg et al., the Agents of Chaos PDF (page 20, text extracted and read), the New York DFS press release text, the Squire / Literary Digest record. Two corrections to the chapter (Gallup's 50,000, and the chapter's "Case #6 detail" flag resolved); one capture refused by the site and not bypassed. All worked numbers are recomputed by `evidence/evidence.py`.

Status: signed by the build agent (Claude, Sonnet 5.5) 2026-10-10; no verdict outstanding.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B01–B06 | The three engineering teams are a constructed parable, not a reported case | EXEMPT | Chapter says so itself ("a composite built to isolate a real pattern, not a case I am reporting from a filing") | Said aloud in B01; "an order of magnitude" is the parable's own claim, said inside the parable |
| 2 | B08 | Bias(θ̂) = E[θ̂] − θ; zero means unbiased | PASS | Standard definition of estimator bias | None |
| 3 | B09, B10 | With a filter keeping 40% of positives and 80% of negatives, a 30% true rate is estimated at 0.1765 at every n; spread falls with n (n=10 sd 0.1158 … n=10,000 sd 0.0037) | PASS | `evidence/evidence.py`, derivation 0.3·0.4 / (0.3·0.4 + 0.7·0.8) = 0.1765, simulation agrees | Spoken "seventeen point six percent" is a rounding of 0.1765 → 17.6% (CORRECT: 17.65 rounds to 17.6 or 17.7; narration says "near") |
| 3b | B10 | "near seventeen point six percent" | CORRECTED | 0.1765 ≈ 17.65% | Narration changed to "near seventeen and a half percent" |
| 4 | B11 | The Literary Digest polled about 2.4 million people (2,376,523 ballots returned of 10 million mailed) and predicted a Landon win | PASS | Squire, Public Opinion Quarterly 52(1):125–133 (1988), as summarised in secondary accounts (ProQuest blog; Iowa State PDF) | "about two point four million" kept; exact count not spoken |
| 5 | B11 | Roosevelt won with about 61% of the vote | PASS | 1936 US presidential election popular vote (60.8%) | None |
| 6 | B12 | Squire found the skew in who was mailed and who answered together produced the error | PASS | Squire 1988 (analysis of a 1937 Gallup survey of whether people answered the Digest poll). A later critic (Lusinchi 2012) disputes that the frame alone explains it; narration claims both together, as Squire does | None; the counterfactual "if everyone had responded" is not claimed |
| 7 | B12 | Chapter: "Gallup … roughly 50,000 respondents" | CORRECTED | Not confirmed in Squire or the other sources found | The Gallup comparison and the 50,000 figure are not spoken |
| 8 | B14–B15 | Ten mechanisms; the pairs in the compound list are derived interactions, not new primitives | EXEMPT | The chapter's own taxonomy (Bear's framework, stated as such) | None |
| 9 | B16–B18 | Sepsis six-hour-lab filter | EXEMPT | The chapter's illustrative example ("as an illustration" said aloud); no sepsis statistics spoken | None |
| 10 | B17 | E[Y \| i∈S] = E[Y] iff P(i∈S) is independent of Y | PASS | Definitional; checked by the simulation in row 3 | None |
| 11 | B19 | Inverse probability weighting: weight 1/P(kept); naive ≈ 18%, weighted ≈ 30% | PASS | `evidence.py` B: naive 0.1797, weighted 0.3047, true 0.30 | None |
| 12 | B23 | Cohen's kappa = agreement beyond chance; constructed counts give 0.6 blinded, 0.2 unblinded | PASS | Cohen 1960; `evidence.py` C: po 0.8 / pe 0.5 → 0.6; po 0.6 / pe 0.5 → 0.2 | Labelled constructed |
| 13 | B24 | Funnel plot: a missing lower-left corner shows unpublished small null studies | PASS | Standard meta-analysis diagnostic; simulated in `evidence.py` D (90 studies, 74 published, mean 0.228 vs true 0.20) | Labelled constructed |
| 14 | B26 | Data-entry bias, buried menu code | EXEMPT | The chapter's illustration, said as an illustration | None |
| 15 | B27 | Weight = (population share) ÷ (sample share) | PASS | `evidence.py` E: 0.30/0.60 → 0.5, 0.50/0.30 → 1.67, 0.20/0.10 → 2.0 | Labelled constructed |
| 16 | B29 | Hiring model on promotion records | EXEMPT | "Imagine" (the chapter's hypothetical) | None |
| 17 | B33 | Face system trained mostly on light-skinned faces is "the textbook example" of dataset bias | EXEMPT | The chapter's example; no study or number stated | Not attributed to a named study |
| 18 | B37 | "Most common failure in this field" | CORRECTED | The chapter's own claim; no rate source | Attributed to Bear as his judgment, "not a measured rate" |
| 19 | B41 | Eight amplifying pairs | EXEMPT | Bear's working list (the chapter's table); said as his list | None |
| 20 | B43 | ProPublica, 2016: Broward County, scores for people arrested 2013–2014; among defendants who did not re-offend, 44.9% of Black defendants vs 23.5% of white defendants were labeled higher risk | PASS | ProPublica "Machine Bias" (Angwin, Larson, Mattu, Kirchner, 23 May 2016), table "Prediction Fails Differently for Black Defendants"; "How We Analyzed the COMPAS Recidivism Algorithm" (Broward County, 2013–2014 scores) | None |
| 21 | B44 | Among defendants who did re-offend, 47.7% of white vs 28.0% of Black defendants were labeled lower risk | PASS | Same table | None |
| 22 | B45 | Northpointe's response (July 2016): within each score, about the same re-offense rates across groups; "predictive parity" | PASS | Dieterich, Mendoza, Brennan, "COMPAS Risk Scales: Demonstrating Accuracy Equity and Predictive Parity," 8 July 2016 (equivant.com, via search summary) | Schematic calibration lines labelled schematic |
| 23 | B46 | The label is re-arrest (a new arrest within two years), not crime | PASS | ProPublica "How We Analyzed…": recidivism defined as a new arrest within two years | None |
| 24 | B48 | Kleinberg, Mullainathan, Raghavan (2016): no method satisfies the three conditions simultaneously except in highly constrained special cases; Chouldechova showed the incompatibility for recidivism tools | PASS | arXiv:1609.05807 abstract (captured); Chouldechova, Big Data 5(2), 2017 (arXiv:1610.07524, 1703.00056) | None |
| 25 | B50 | v/(1−v) = p/(1−p) · t/f for a calibrated score (v = PPV, p = base rate, t = TPR, f = FPR) | PASS | PPV = pt / (pt + (1−p)f) rearranged; checked in `evidence.py` F | None |
| 26 | B51 | PPV 60%, TPR 70% ⇒ FPR 20% at base rate 30%, 46.7% at 50% | PASS | `evidence.py` F: 0.2000 and 0.4667, PPV recomputed 0.6000 for both | Labelled constructed |
| 27 | B52 | The three criteria cannot all hold when base rates differ unless prediction is perfect | PASS | Kleinberg et al. 2016; Chouldechova 2017 | None |
| 28 | B53 | "Which error are we less willing to make is a values claim"; engineers' loss functions encode a values choice | EXEMPT | Bear's argument; said as "Professor Bear's argument … not a finding" | None |
| 29 | B54 | Apple Card limits drew bias allegations in 2019; New York's DFS reported on 23 March 2021 "did not produce evidence of unlawful discrimination", applications with similar credit characteristics "generally had similar outcomes", and faulted customer service and transparency | PASS | DFS press release "DFS Issues Findings on the Apple Card and Its Underwriter Goldman Sachs Bank", 23 March 2021 (text fetched 2026-10-10); 2019 allegations per news coverage of the investigation | The page refused automated capture (Cloudflare 403): not bypassed, quoted on a drawn card instead |
| 30 | B56–B63 | Pearl's ladder: association, intervention (do), counterfactual; rooster and sunrise | PASS | Pearl & Mackenzie, *The Book of Why* (2018); Pearl, *Causality* | None |
| 31 | B64 | Rung-one versus rung-two phrasing of the audit questions | EXEMPT | The chapter's own table (Bear's pairing) | None |
| 32 | B65–B70 | Procedure of four steps; ten paths in the constructed graph; what each fix leaves open (4, 8, 0 of 10) | PASS | `evidence.py` G (paths APFMORK … ACK; blocked counts 6, 2, 10 → open 4, 8, 0) | Labelled constructed; "counting paths isn't measuring bias" said aloud |
| 33 | B71 | Leverage analysis is Descartes' method of doubt turned on a pipeline | EXEMPT | The chapter's framing (merge block 7, HEAD) | None |
| 34 | B73–B74 | "The political dimension is the technical dimension"; five supervisory capacities include problem formulation | EXEMPT | Bear's argument and framework, attributed; framework glossed on first use | None |
| 35 | B75 | Agents of Chaos (2026) red-teamed autonomous agents in a live lab; sixth case study "Agents Reflect Provider Values" used benign but politically sensitive prompts on an agent backed by a Chinese provider's model | PASS | arXiv:2602.20021 abstract and PDF p. 20 ("Case Study #6", Quinn, Kimi K2.5 trained and hosted by a Chinese provider) | The chapter's `[verify]` flag is resolved by the primary; the model and provider are not named in narration |
| 36 | B76 | The provider's API repeatedly truncated responses with "unknown error" on politically sensitive topics, silently preventing valid tasks; provider influence is "often invisible to users" | PASS | Same, page 20 ("Outcome", "Discussion") | Spoken as "the authors report" |
| 37 | B80 | Arendt asked about systemic harm as the output of diffused, role-bound responsibility | PASS | Arendt, *Eichmann in Jerusalem* (1963); connection to pipelines is Bear's reading, said as his | None |
| 38 | B81–B82 | Bear's uncertainty statements | EXEMPT | Bear's first-person statements; not facts about the world | The two papers the chapter cites there are flagged `[verify]` and are not spoken |
| 39 | BVDT | Six recap lines | EXEMPT | Recaps only what the acts established | None |

**Datable material stripped (DOUBLE-CHECK LAW).** No model version numbers; the Kimi model and Moonshot are not named; no arXiv id in narration; Gallup's 50,000 removed; the sepsis model product name never appears; no "as of" claims.
