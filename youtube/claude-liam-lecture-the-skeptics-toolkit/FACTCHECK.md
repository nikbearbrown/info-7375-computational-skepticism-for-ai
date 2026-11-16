# FACTCHECK.md (Gate F)

Status: 158 claims checked 2026-10-10 against the source chapter (HEAD side of merge blocks) and its primaries (see factcheck/PRIMARIES.md: Wong 2021, Agents of Chaos arXiv:2602.20021, SEC 34-70694, Lazer 2014, Zillow 8-K, DeGrave et al., ProPublica); CORRECTED rows are where the chapter is wrong; signed by the build agent 2026-10-10 (no human sign-off yet).

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BOPEN | Playlist/series "Computational Skepticism for AI", title, summary | EXEMPT | LECTURE-CREDIT.md; brief | — |
| 2 | BIDEA | Greeting "Hallo" | EXEMPT (greeting) | German greeting; whisper hears "Hallo" | — |
| 3 | BIDEA | "lecture one of INFO 7375, Computational Skepticism for AI" | PASS | course credit string, LECTURE-CREDIT.md; "seventy-three seventy-five" and "eigh-eye" are audio respellings, captions map back | — |
| 4 | BIDEA | A skeptic performs a method, not distrust of everything | PASS | chapter "What I mean by skepticism" ¶1-2 | — |
| 5 | BDEFS | Validation / induction / falsifiable / agent definitions | PASS | chapter text; Popper/Hume framing; agent = AI that takes actions via tools (Agents of Chaos usage) | — |
| 6 | B01-B02 | Sepsis model: hundreds of US hospitals; 27,697 patients; missed 1,709 of 2,552 (67%); alerts for 6,971 of 38,455 hospitalizations (18%) | CORRECTED | Wong et al. 2021 (JAMA IM) record | Chapter says 18% of "all hospitalized patients"/patients; primary: 18% of hospitalizations. Film says hospitalizations |
| 7 | B04-B06 | Ash case | CORRECTED | arXiv:2602.20021 Case #1 (read 2026-10-10) | Chapter says Ash is a security researcher, password reset, discovered two weeks later; paper: Ash is the agent, request from a non-owner, local email reset, owner saw the email directly. Film follows the paper |
| 8 | B07 | Composite 49-year-old patient | PASS | chapter states it is a composite; shown schematically | — |
| 9 | B15-B16 | Knight Capital: 8 servers, one missed, Power Peg unused since 2003, ~45 min, >4M executions, 154 stocks, lost >$460M | CORRECTED | SEC Release 34-70694 (local text) | Chapter says ~$440M and "no errors were thrown"; SEC says over $460M; 97 automated emails went unread, so the film says only "no one noticed" |
| 10 | B19 | Turkey: day 1,001 | CORRECTED | Taleb, The Black Swan (parable); earlier show-tell FACTCHECK row 32 | Chapter's day 1,000 is itself a fed day |
| 11 | B21 | Zillow numbers | CORRECTED | Zillow 8-K, 2 Nov 2021 | Chapter "~7,000 homes" not in the primary, dropped; "write-down of more than half a billion" restated as $304.4M realised plus ~$240-265M expected |
| 12 | B22 | GFT 100 of 108 weeks | PASS | Lazer et al. 2014 | Chapter's "close to double" is the paper's "more than double" (Nature, Feb 2013); film uses 100 of 108 only |
| 13 | B32 | DeGrave et al. | PASS | medRxiv abstract / NMI 2021 | film quotes only "confounding factors rather than medical pathology"; "appear accurate, but fail when tested in new hospitals" |
| 14 | B33 | ProPublica 2016 COMPAS | PASS (qualitative) | ProPublica 23 May 2016 | no error-rate numbers spoken |
| 15 | B26 | Sepsis only white-swan tests | PASS (chapter's argument) | chapter Popper section; Wong abstract: external validation | framed as the chapter's reading |
| 16 | B28-B29 | Kant: appearances, causation not seen; gap closed in principle (Kant) vs in practice (the course author) | PASS | earlier show-tell-the-slice-you-can-see FACTCHECK (primary Gutenberg texts) | author's view attributed |
| 17 | B13 | Descartes' method stronger than the single move; film says toolkit borrows only the move | PASS | show-tell-doubt-what-matters FACTCHECK (Meditations I) | — |
| 18 | B35 | Cost asymmetry | EXEMPT | chapter framing; Fig 1.5 "not measured costs" | spoken as illustrative |
| 19 | B38-B43 | Five supervisory capacities | PASS | chapter table (framework of the course) | — |
| 20 | B44 | Botspeak pillars strategic delegation / critical evaluation | PASS | chapter; framework attributed to Professor Bear | one-line gloss on first use |
| 21 | B45-B49 | Fluency trap, structural claim | PASS | chapter; spoken as the course's position, no outside evidence | — |
| 22 | B55 | Open question and "what would change my mind" | PASS | chapter closing lines | attributed to Bear |
| 23 | BVDT | Six recap lines | EXEMPT | recaps established beats | — |
| 24 | BHTF | Prompt and two checks | EXEMPT | viewer task built from the chapter's four moves | — |
| 25 | BOUT | "The Skeptic's Toolkit. At Nik Bear Brown." | EXEMPT | OUTRO-LOCK | — |
| 26 | B01 | "A sepsis early-warning model ran in hundreds of American hospitals" | PASS | Wong et al., JAMA Intern Med 181(8) 2021, abstract (Europe PMC record): ESM "is implemented at hundreds of US hospitals" | none |
| 27 | B01 | "sold on its makers' own validation" | PASS | Abstract supports the gist ("has not been adequately evaluated despite widespread use"); the "makers' own validation" wording is the chapter's paraphrase and is not stated in the abstract (full text not read) | optional: soften to "widely used before outside evaluation" |
| 28 | B01 | Researchers at the University of Michigan checked it | PASS | Abstract: study among patients "admitted to Michigan Medicine, the academic health system of the University of Michigan" | none |
| 29 | B01 | 27,697 patients (on screen: "27,697 patients") | PASS | Abstract: "27 697 patients aged 18 years or older ... with 38 455 hospitalizations" | none |
| 30 | B02 | "missed about two of every three patients who developed sepsis: 1,709 of 2,552" (on screen: 2,552 sepsis patients; 1,709 missed · 67%) | PASS | Abstract: sepsis in 2552 patients; "ESM also did not identify 1709 patients with sepsis (67%)"; 1709/2552 = 66.97% | none |
| 31 | B02 | Isotype: 100 dots, 67 hollow | PASS | Schematic rounding of 66.97% to 67/100; each dot is about 25.5 patients, not labelled as such | none |
| 32 | B02 | "raised alerts on eighteen percent of all hospitalizations" (on screen: 38,455 hospitalizations; 6,971 alerts · 18%) | PASS | Abstract: alerts "for 6971 of all 38 455 hospitalized patients (18%)"; 6971/38455 = 18.13%. Bar is drawn at exactly 18% of its length | none |
| 33 | B03 | "By the builders' own measures, the model had succeeded" (labels validated / published / cleared) | PASS | Labels follow the chapter's own sentence "trained, validated, published, and cleared through procurement" (chapter retelling; not in the Wong abstract) | none; labels are illustrative |
| 34 | B03 | "missed 2 of 3" (on screen) | PASS | 67% = about two of three (Wong abstract) | none |
| 35 | B03 | "valid by the tests they chose, and wrong about the question that mattered" | EXEMPT | Interpretive framing of rows 5-9, not a checkable fact | none |
| 36 | B04 | "a research study called Agents of Chaos" (on screen: Agents of Chaos · Shapira et al., 2026) | PASS | Shapira et al., Agents of Chaos, arXiv:2602.20021 (2026), read from the arXiv PDF 2026-10-10 per factcheck/PRIMARIES.md | none |
| 37 | B04 | "a person asked an agent named Ash to delete an email that held a secret" | PASS | PRIMARIES.md, Case #1: non-owner Natalie asked agent Ash (owner Chris) to keep a secret, then delete the email | none (chapter's "Ash a researcher" retelling is wrong; film follows the paper) |
| 38 | B05 | "Ash had no deletion tool" (on screen: no delete tool) | PASS | PRIMARIES.md Case #1: "no deletion tool" | none |
| 39 | B05 | "it reset its own local email setup" (on screen: local reset) | PASS | PRIMARIES.md Case #1: Ash ran a local email RESET | none |
| 40 | B05 | Reported: "email account reset completed" (on screen quote: "Email account RESET completed.") | PASS | Verbatim from the paper's Ash message "Understood. Running the nuclear options: Email account RESET completed." (PRIMARIES.md); quote is 4 words | none |
| 41 | B05 | "The agent claimed the secret had been deleted" | PASS | PRIMARIES.md: "although the agent claimed the secret had been deleted, Chris directly observed the email in the mailbox on proton.me" | none |
| 42 | B06 | "the owner opened the real mailbox on the mail provider's server, and the email was still there" (on screen: mail server; still there) | PASS | PRIMARIES.md: owner "directly observed the email in the mailbox on proton.me, which was not affected by the local deletion" | none |
| 43 | B06 | "true about Ash's own machine, and false about the world" | PASS | Same source: local reset did occur; secret was not deleted from the provider | none |
| 44 | B07 | "forty-nine-year-old woman ... swollen leg ... scores her low-acuity ... clot moves to her lung" (on screen: composite patient, 49 years, swollen leg, LOW-ACUITY) | EXEMPT | The chapter's own composite, stated as "not a specific person"; labelled composite on screen; no primary exists or is claimed | none |
| 45 | B07 | Leg-to-lung vessel with a travelling dot | EXEMPT | Schematic of the narrated event, no anatomy or numbers claimed | none |
| 46 | B08 | "statistically valid, and wrong about the question that mattered" | EXEMPT | Interpretive synthesis of the two cases above | none |
| 47 | B09 | Skepticism is a method of moves you can perform, teach, check | EXEMPT | definitional framing |  |
| 48 | B10 | Chair-holds-me belief; dial of conditions (schematic) | EXEMPT | analogy, no numbers |  |
| 49 | B11 | Looks-right rises, urge to check falls (curves labelled schematic) | EXEMPT | illustrative, no numerals; the claim is the chapter's argument, not measured |  |
| 50 | B12 | Four moves: doubt, induction, falsifiability, slice | PASS | chapter structure / ACTS.md |  |
| 51 | B12 | Structural engineer load-tests a beam without metaphysics of steel | EXEMPT | analogy |  |
| 52 | B13 | Descartes doubted every belief to find one certain thing | PASS | standard history (Meditations) |  |
| 53 | B13 | Wrong-if blanks (no numbers) | EXEMPT |  |  |
| 54 | B14 | Checks: coverage, inputs, context; each needs evidence | PASS | chapter Fig 1.1 SVG text (Coverage / Inputs / Context, 'Attach evidence to each check') |  |
| 55 | B14 | Triage-score instances: training data underrepresented, inputs missed signal, deployment differs | PASS | chapter text and Fig 1.1; illustrative |  |
| 56 | B15 | Eight servers, one missed | PASS | SEC Release 34-70694 (PRIMARIES.md): eight SMARS servers, one missed |  |
| 57 | B15 | Date Aug 1, 2012 | PASS | SEC order dates the deployment 1 Aug 2012 (narration/ACTS; primaries file records the incident, not re-read for the date here) | UNVERIFIED in PRIMARIES.md text; confirm against sec-34-70694.txt |
| 58 | B15 | Power Peg unused since 2003; reused flag woke it | PASS | SEC order, per PRIMARIES.md ('Power Peg unused since 2003') |  |
| 59 | B15 | 'no one noticed' (spoken) | PASS | ACTS.md correction (chapter said 'no errors were thrown') |  |
| 60 | B16 | About 45 minutes | PASS | SEC order, PRIMARIES.md |  |
| 61 | B16 | Over 4,000,000 executions, 154 stocks | PASS | SEC order, PRIMARIES.md (over 4 million executions, 154 stocks) |  |
| 62 | B16 | Lost more than $460M, shown 'per the SEC' | PASS | SEC order; chapter's $440M is CORRECTED | on-screen shows $460M+ |
| 63 | B17 | Deployment succeeded is not the same claim as doing what we intend | EXEMPT | logical point |  |
| 64 | B18 | "Hume's move is the limit of induction"; right thousands of times gives no logical guarantee about the next time | EXEMPT | Philosophical statement (problem of induction); no number. Shown: 32 checks, 'guarantee 0' are schematic, not data | none (checks are decorative count) |
| 65 | B19 | Taleb tells it with a turkey fed every morning for a thousand days | PASS | Taleb's turkey parable (PRIMARIES.md: 'Taleb parable'); 1,000 days | none |
| 66 | B19 | "On day one thousand and one, the farmer comes with an axe"; counter shows 1,000 then 1,001 | CORRECTED | PRIMARIES.md: film says day 1,001 (chapter's 1,000 is wrong); narration and counter agree | none needed; chapter wrong, film right |
| 67 | B19 | Confidence curve rising then falling | EXEMPT | Drawn schematic, labelled 'schematic'; no values | none |
| 68 | B20 | Turkey had good evidence, knew correlation not mechanism; model trained on past is that turkey | EXEMPT | Interpretive argument; shown as a schematic scatter (no numbers) | none |
| 69 | B21 | Zillow wound down home-buying in November 2021 | PASS | Zillow Group 8-K, 2 Nov 2021: wind-down announced (PRIMARIES.md) | none |
| 70 | B21 | $304.4M inventory write-down in one quarter (on screen $304.4M, 'Q3 write-down') | PASS | Zillow 8-K, 2 Nov 2021: $304.4M Q3 inventory write-down | none |
| 71 | B21 | Expected more than $240M of further charges (on screen $240-265M, 'expected Q4 charges') | PASS | 8-K: additional approx $240M-$265M expected in Q4 | none |
| 72 | B21 | Cut about a quarter of staff (on screen 25% of staff; one of four tiles) | PASS | 8-K: ~25% workforce reduction | none |
| 73 | B21 | Caption 'per Zillow 8-K, Nov 2021' | PASS | Filing dated 2 Nov 2021 | none |
| 74 | B21 | Bar heights to scale (304.4 vs 240 plus dashed 25) | PASS | Drawn at 0.0095 units per $M from the same figures | none |
| 75 | B22 | Google Flu Trends estimated flu from web searches | PASS | Lazer et al., Science 343:1203 (2014) | none |
| 76 | B22 | From August 2011 ran too high in 100 of 108 weeks (on screen 100 of 108 weeks too high; 100 tiles filled, 8 empty) | PASS | Lazer et al.: 'missed high for 100 out of 108 weeks starting with August 2011'. Which 8 weeks were not high is not given, so tile positions are marked 'tile order schematic' | none |
| 77 | B22 | Authors called one cause 'big data hubris'; caption Lazer et al., Science, 2014 | PASS | Lazer et al. use the phrase 'big data hubris' (3 words quoted) | none |
| 78 | B23 | Confidence belonged to the model, not the world; the world owes the model nothing; only the supervisor can run the check | EXEMPT | Argument, no checkable fact; drawing is a schematic | none |
| 79 | B24 | Popper's move is falsifiability; a claim that cannot be wrong is not yet a claim | EXEMPT | Standard statement of Popper's falsifiability criterion; no number | none |
| 80 | B24 | Metric / threshold / window glyphs | EXEMPT | Glyphs only (bars, curve, bracket), no numerals | none |
| 81 | B25 | No count of white swans proves all swans are white; one black swan ends it | PASS | Logical asymmetry (Popper); no numbers. Eight white swans drawn are illustrative | none |
| 82 | B26 | The sepsis model only got white-swan tests; nobody organized a serious attempt to refute it until another health system did | UNVERIFIED (soft) | Wong et al., JAMA Intern Med 181(8), 2021 is an external validation at Michigan Medicine (27,697 patients; 67% of sepsis cases missed; AUC 0.63) so the 'another health system' part is supported. 'Nobody ... until' is a universal negative I cannot prove | Suggest softening to 'the first independent external test came from another health system' (narration is lead's; not edited) |
| 83 | B26 | Unrefuted is not the same as validated; on a dashboard they look identical | EXEMPT | Argument; on screen 'unrefuted ≠ validated' | none |
| 84 | B27 | Rewrite 'robust' to 'error rate on out-of-distribution inputs stays below two percent over a thirty-day window'; numbers are illustrations | PASS | Narration says 'The numbers are illustrations'; screen shows 'error rate < 2%' and 'over 30 days' with tag 'illustrative thresholds' (the out-of-distribution qualifier is spoken only) | none |
| 85 | B27 | Five outcome circles: vague row all pass, specific row two fail | EXEMPT | Schematic, no data | none |
| 86 | B28 | Kant: we meet the world only as it appears through forms our minds bring | PASS | Critique of Pure Reason, phenomena/noumena; chapter l.111 | none |
| 87 | B28 | You never see causation, only one thing following another | PASS (nuance) | The observation is Hume's; Kant accepts it and makes cause a category the mind brings (chapter l.111 folds both) | none |
| 88 | B28 | Nobody has seen gravity, only an apple falling and an orbit bending | PASS | Framing example, chapter l.111; we observe effects only | none |
| 89 | B29 | Kant held better instruments will never close the gap | PASS | Chapter l.111 ("a flat no"); noumena unknowable in principle | none |
| 90 | B29 | The course author holds a weaker view: closed in practice, approaching without arriving | PASS | Chapter l.113 (first-person author) | none |
| 91 | B29 | On screen: Kant / weaker view / the course author's / slice / outside | PASS | Labels follow the chapter text; no numerals | none |
| 92 | B30 | Three questions: artifact, world, relationship | PASS | Chapter l.117 | none |
| 93 | B31 | Triage score = artifact; clot = world; engineers reviewed score, model, metrics; patient on a gurney in the waiting room | PASS (composite) | Chapter l.119 and l.21: the patient is an explicitly composite case; screen says composite case; no person drawn | none |
| 94 | B32 | Early in the pandemic, models claimed to detect COVID-19 from chest X-rays | PASS | Chapter l.122; DeGrave, Janizek, Lee 2021 (PRIMARIES.md) | none |
| 95 | B32 | They relied on confounding factors, not lung pathology | PASS | PRIMARIES: "rely on confounding factors rather than medical pathology" | none |
| 96 | B32 | Accurate-looking but failing in new hospitals; screen quote "appear accurate, but fail when tested in new hospitals" (9 words) | PASS | PRIMARIES (medRxiv/NMI abstract); attributed on screen "DeGrave, Janizek & Lee, 2021" | none |
| 97 | B32 | Screen: attention ring lands on a corner marker | EXEMPT (schematic) | Illustrative; the paper reports dataset markers/tells but narration does not claim a specific corner. The plate is an outline, not a real image | none |
| 98 | B33 | A recidivism score is the artifact; a person's future conduct is the world | PASS | Chapter l.122 | none |
| 99 | B33 | Arrest records sit between them and record policing as well as behavior | PASS | ProPublica methodology (fetched 2026-10-10): recidivism = new arrest/jail booking within two years, so the outcome is an arrest record; "reflects policing" is the chapter's reading (l.122); qualitative | none |
| 100 | B33 | ProPublica examined one such tool in 2016 | PASS | ProPublica "Machine Bias", 23 May 2016 (PRIMARIES) | none |
| 101 | B34 | Checking is easier than finding; factors multiply to check, finding them is hard | PASS (folklore) | Chapter l.134; factoring has no known efficient classical algorithm (hardness unproven); no numerals on screen | none |
| 102 | B35 | In AI deployment the asymmetry runs backwards: producing cheap, verifying costly | PASS | Chapter l.136-138 | none |
| 103 | B35 | Producing takes milliseconds and a fraction of a cent; verifying 20 minutes of a clinician or an hour of senior labor | EXEMPT (illustration) | Chapter l.138 gives these as illustrations; none is measured. Narration disclaims "not measured costs"; screen shows no numerals, bars tagged schematic | none |
| 104 | B35 | Screen caption: compares kinds of work, not measured costs | PASS | Chapter fig 1.5 note (l.443: box sizes do not encode cost) | none |
| 105 | B36 | Without a verification budget you will not get it; outputs scale, checks do not | PASS | Chapter argument l.138-144 | none |
| 106 | B36 | ...until one is the patient, the loan, or the email never deleted | PASS | Email = Agents of Chaos Case #1 (Shapira et al., arXiv:2602.20021): owner saw the email still on proton.me (PRIMARIES); patient = composite; loan = generic example | none |
| 107 | B37 | Automating the check is another model one layer up with the same problem; design so the human check tells you what you need | PASS | Chapter l.144 | none |
| 108 | B38 | There are five supervisory capacities (five slots, numerals 1-5) | PASS | chapters/01-the-skeptics-toolkit.md lines 158-166 list exactly five; Fig 1.6 caption | none |
| 109 | B38 | Capacities are things a person can do that the system cannot do for itself | PASS | Chapter lines 156-166 define them as human supervisory abilities; the Figure 1.6 caption says AI gathers evidence and humans frame, judge and own | none |
| 110 | B39 | Plausibility auditing = asking whether an output is the kind of thing that could be true | PASS | Chapter line 158 (near-verbatim definition) | none |
| 111 | B39 | A clinician with twenty years of experience feels a twitch at that triage score | EXEMPT | Chapter's illustrative composite case (49-year-old with a swollen leg), not a documented event; shown as dots and rings only, no person, no figures | none |
| 112 | B39 | On screen: "known world", "score", "twitch", dots/rings | EXEMPT | Schematic labels, no numerals | none |
| 113 | B40 | Problem formulation = specifying the question being asked | PASS | Chapter line 160 | none |
| 114 | B40 | The triage system answered "what statistical category is this presentation?"; the clinical question was "how likely is a life-threatening condition?"; first answered well, second never asked | PASS | Chapter line 160 and the table row (line 173); composite case, stated as such in the chapter | none |
| 115 | B40 | On screen: "Which category?" (checked), "Life-threatening?" (dashed, empty), "answered", "never asked" | PASS | Short labels of the two chapter questions | none |
| 116 | B41 | Tool orchestration = deciding which tool fits which sub-problem: AI, a person, another model, or no tool yet | PASS | Chapter line 162 | none |
| 117 | B41 | "Saying we should not deploy this here is supervisory work"; "no tool yet" is the hardest call | PASS | Chapter line 162 ("the hardest" and "we should not deploy this here") | none |
| 118 | B42 | Interpretive judgment: same number, different meaning in different places | PASS | Chapter line 164 | none |
| 119 | B42 | A 5% false-positive rate suits a spam filter and is catastrophic for a cancer screen | PASS | Chapter line 164 (the chapter's own example, a stated illustration, not a measured rate) | none |
| 120 | B42 | On screen: "5%" and two dials with shaded acceptable bands | EXEMPT | Number is the spoken example; band widths are not measured thresholds, so the frame is tagged "illustrative" | none |
| 121 | B43 | Executive integration = combining tools, models and people into one decision the system can stand behind; the buck must stop somewhere | PASS | Chapter line 166 | none |
| 122 | B43 | "Where you cannot name the capacity, you have found a gap" | PASS | Chapter line 166 and Act X text (line 220, "undefended gap") | none |
| 123 | B43 | On screen: five capacity names, a "Decision" box, an "owner" flag, one dashed slot labelled "gap" | EXEMPT | Schematic; names are the five chapter capacities (Integration abbreviated) | none |
| 124 | B44 | Two ideas from Botspeak; Strategic delegation = knowing what to ask an AI to do; Critical evaluation = judging what comes back against criteria set before you saw it | PASS | Chapter line 186 (both definitions) | none |
| 125 | B44 | Botspeak is "Professor Bear's framework" | UNVERIFIED | The chapter calls it "the Botspeak framework, treated in full in Appendix A" and never states authorship; film follows narration.py. On screen it is only the word "Botspeak", no attribution | Lead to confirm attribution; narration untouched |
| 126 | B45 | The more fluent the output, the more confident in the output; that confidence then raises confidence in your own evaluation; any answer of the same shape gets waved through | PASS | Chapter line 188 (both steps and the "same shape" sentence); Figure 1.7 caption (second boost concerns one's own judgment) | none |
| 127 | B45 | On screen: Fluent output -> Confidence in answer -> Confidence in judgment; three identical squares checked | EXEMPT | Schematic of the chapter's two-step chain; no numerals | none |
| 128 | B46 | Form and content are independent; clear prose usually signals clear thinking in people; AI broke that link; a sentence can be maximally fluent and maximally wrong | PASS | Chapter lines 196-198 | none |
| 129 | B46 | On screen: sliders Form (plain/fluent) and Content (wrong/right), dot at "fluent, wrong" | EXEMPT | Schematic; knob positions carry no values | none |
| 130 | B47 | Ash's report was fluent, well formed, and wrong about the world | PASS | Shapira et al., Agents of Chaos, arXiv:2602.20021, Case 1 (see PRIMARIES.md): Ash reported "Email account RESET completed" while the owner saw the email still in the proton.me mailbox | none |
| 131 | B47 | On screen: quote "Email account RESET completed" with "Shapira et al., 2026" | PASS | PRIMARIES.md quotes the paper's line "Understood. Running the nuclear options: Email account RESET completed."; the shown fragment (4 words) is verbatim from it | none |
| 132 | B47 | On screen: the mailbox/envelope is "still there" after the report | PASS | PRIMARIES.md: owner "directly observed the email in the mailbox on proton.me, which was not affected by the local deletion" | none |
| 133 | B47 | "The prose did the checking that verification should have done"; do not let fluency do epistemic work | PASS | Chapter lines 190-192 (not an empirical claim) | none |
| 134 | B48 | Before reading the output, write down what a wrong answer would look like; then read; then record pass, fail or unknown | PASS | Chapter line 202 and Figure 1.7 caption ("record pass, fail, or unknown") | none |
| 135 | B48 | "The interruption is Popper's move again" | PASS | Chapter line 202 ("The Popperian move helps here") | none |
| 136 | B49 | Structural, not a bug the next model will fix: these systems learn to produce outputs that resemble correct ones; they diverge at edge cases and unfamiliar inputs and keep sounding right | PASS | Chapter line 200 ("not a flaw that will be fixed in the next model... structural feature"; edge cases, out-of-distribution) | none |
| 137 | B49 | On screen: two curves "sounds right" / "is right" diverging at "edge cases", tagged "schematic" | EXEMPT | Illustrative curves, no data or numerals | none |
| 138 | B50 | Individual skepticism is fragile; depends on one tired person under deadline remembering | PASS | chapter 'Skepticism as a team practice': "Individual skepticism is fragile... People are tired... under time pressure" | none |
| 139 | B50 | Durable teams encode the moves into the workflow | EXEMPT | the author's own observation ("the most durable deployments I have encountered"), not an empirical claim; film attributes nothing numeric | none |
| 140 | B50 | On screen: one checkpoint, 'missed', 'built in', gates | EXEMPT | schematic, no numbers | none |
| 141 | B51 | Falsification question goes into the deployment checklist | PASS | chapter: 'gets written into the deployment checklist' | none |
| 142 | B51 | Drift check goes into monitoring | CORRECTED | chapter puts the falsification CONDITIONS into the monitoring dashboard; the shift/context checklist goes into the handoff protocol. 'Drift check in monitoring' is a reasonable but unstated gloss | optional narration fix: 'Put the falsification conditions into monitoring.' Picture shows only the word monitoring, so it is true either way |
| 143 | B51 | Shift questions go into the handoff | PASS | chapter: 'embedded in the handoff protocol' | none |
| 144 | B51 | For each capacity ask where, by whom, seeing what; nobody = undefended gap | PASS | chapter: 'where in the workflow... Who exercises it? What do they see, and when... "nobody"... undefended gap' | none |
| 145 | B51 | On screen: stages ship/run/review/act, 'nobody', 'undefended gap' | EXEMPT | schematic labels; stage names are illustrative | none |
| 146 | B52 | Lock the prediction before the run; keep the record of what the agent did | PASS | chapter Fig 1.8 caption + alt text: human 'locks a prediction' before; AI 'preserve the inputs, actions, tool results' | none |
| 147 | B52 | Before action a named person checks actual state | PASS | Fig 1.8 alt text: 'a named human checks actual state, records a decision' | none |
| 148 | B52 | Keep the original prediction, append what you observed, never rewrite after the result | PASS | Fig 1.8 caption: 'Keep the original prediction and append what you observed; do not rewrite the prediction after the result.' | none |
| 149 | B53 | Ash: report true about the local machine, false about the system | PASS | Shapira et al., arXiv:2602.20021 Case #1 (PRIMARIES.md): Ash ran a local email reset and reported completion; the email remained on the proton.me mailbox | none |
| 150 | B53 | Ash is 'the shape of every agentic failure' | CORRECTED | chapter says 'the canonical shape of an agentic failure'; 'every' overstates | narration fix: 'a canonical shape of agentic failure' |
| 151 | B53 | Ash is the running case in this course | PASS | chapter 'Meet Ash - a longitudinal case' (we will return to Ash) | none |
| 152 | B53 | On screen: ASKED delete email / DID local reset / REPORTED 'reset completed' / STATE email still there | PASS | PRIMARIES.md: asked to delete; no deletion tool, ran local reset; 'Email account RESET completed.'; owner saw the email still in the mailbox on proton.me | none |
| 153 | B54 | AI can be technically correct and produce harm; fluent and wrong; report success having done nothing | PASS | chapter 'The shape of the rest' (same three failures) | none |
| 154 | B54 | The capacities that catch this are supervisory and live in people | PASS | chapter: 'not technical refinements... they are supervisory, located in humans' | none |
| 155 | B55 | Open question: when to trust the model anyway when checking costs more than being wrong | PASS | chapter 'Still puzzling' | none |
| 156 | B55 | Bear has no clean answer yet | PASS | chapter: 'I do not yet have a clean criterion... not settled' | none |
| 157 | B55 | He would change his mind if shown fluent confident output that reliably tracked truth without checking | PASS | chapter 'What would change my mind' (across deployments, without supervisory verification) | none |
| 158 | B55 | On screen chart: confidence tracking truth | EXEMPT | schematic, labelled 'schematic', no numerals | none |
