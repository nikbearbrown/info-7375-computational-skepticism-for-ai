# SHOTLIST — Bias: Where It Enters and Who Is Responsible

**What.** One row per beat: what the sentence is about, the lane picked, the runner-up auditioned, and why the pick wins (BEST-BEAT LAW).
**Why.** The pick must be the picture a viewer understands with the sound off; a runner-up proves the beat was auditioned.
**Found.** Library asked first (`./art scenes`: causal graph, table with a ringed row, ladder, bar comparison, equation term by term, pipeline); the library has no causal-graph, no estimator or ladder-of-causation scene, so those are drawn in Manim (a registered Remotion scene was not built: every drawing is film-specific and lives in scenes.py). Real records are shown as themselves; run output is real stdout.

| beat | about | lane picked | runner-up | why this one wins |
|---|---|---|---|---|
| BOPEN | Film identity and payoff | Card · `lecture-title-slide-16x9` | Minimal title card | The lecture skill's approved first beat: portrait, playlist, film title, short payoff. |
| BIDEA | The reflex the film corrects | Remotion · `BrutalistHesitantWriter` | Overview card | The writer types the reflex and corrects one phrase into the film's question. |
| BDEFS | Prerequisite vocabulary | Remotion · `ClaudeDefinitions` | Library icon row | Six words the acts lean on, one plain line each. |
| A1 | Act title: Three Teams, One Problem | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B01 | A biased system and three teams, same gap | Manim · `B01_Parable` | Isometric team figures (banned: person tokens) | Two outcome bars start unequal and three team flags land beside them. |
| B02 | Team one: penalty on the model, gap shrinks a little | Manim · `B02_TeamOne` | Isometric box | A penalty tag clips onto the model block and the gap bars shorten slightly. |
| B03 | Team two: data rebalanced, gap changes shape | Manim · `B03_TeamTwo` | Stat card | New data blocks fill the thin column and the gap bars reshuffle instead of vanishing. |
| B04 | Team three: the review step, gap collapses | Manim · `B04_TeamThree` | Isometric desk | The reviewer block lights up on its name and the gap bars drop to almost nothing. |
| B05 | Three interventions, three paths of different width | Manim · `B05_ThreePaths` | Bar chart | Three paths draw from cause to outcome; two stay thin and one runs thick. |
| B06 | Nearest fix versus highest-leverage fix | Manim · `B06_NearVsLever` | Question card | A near marker sits on the model while the question's ring travels down the chain to the real node. |
| A2 | Act title: What Bias Means | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B07 | Everyday meaning versus the estimator | Manim · `B07_TwoMeanings` | Split text card | The loose word splits into two machines: one with a verdict, one with data in and a number out. |
| B08 | Bias = E[θ̂] − θ with the offset on a number line | Manim · `B08_BiasEquation` | Equation alone | The equation assembles term by term while the cloud of estimates drifts off the true value and the offset arrow draws. |
| B09 | Estimates narrow around the wrong value as n grows | Manim · `B09_MoreData` | Static two-curve chart | Histograms of real simulated estimates narrow at n = 10, 100, 1,000, 10,000 while staying centred off the true line. |
| B10 | The simulation's real output | Remotion · `CCPlainShell` | Manim table of the same numbers | SHOW-THE-THING / EXECUTABLE-EVIDENCE: the script's recorded stdout, line by line. |
| B11 | A huge sample pointing the wrong way | Manim · `B11_Poll1936` | VOX archival still (not needed: the numbers are the evidence) | A block of 2.4 million sample dots grows beside the result bar that points the other way. |
| B12 | Mailing list skew then non-response, two filters | Manim · `B12_SquireFrame` | Funnel | The population narrows through two successive filters and the surviving tint no longer matches the whole. |
| B13 | Ten sources of one offset | Manim · `B13_TenWays` | Chip grid | Ten dots land one by one on the offset arrow, each adding to the gap. |
| A3 | Act title: Selection Bias | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B14 | The ten entry points along one pipeline | Manim · `B14_TenMap` | FormB icon row | A pipeline draws left to right and the ten names pin to their stage as they are spoken. |
| B15 | Ten primitives, compounds are pairs of them | Manim · `B15_Alphabet` | Text card | Two of the ten join by a bridge labelled compound; no new dot appears. |
| B16 | A reasonable query silently drops people | Manim · `B16_QueryFilter` | Isometric conveyor | Patient dots pour through the query gate; those without a timely panel fall away grey. |
| B17 | E[Y | in sample] versus E[Y] | Manim · `B17_SelectionEquation` | Equation alone | Two expectations stand side by side; the condition appears and then breaks, turning the equals sign into not-equals. |
| B18 | Kept stable patients, dropped critical ones | Manim · `B18_SepsisFilter` | Bar chart | The critical column is cut off by the filter; the model's risk bar for it stays low, below the true level. |
| B19 | Weights restore the dropped people | Manim · `B19_IPW` | Table | Kept dots swell by 1/P and the estimate marker slides from 0.18 to 0.30. |
| B20 | Unrecorded driver, nothing to weight | Manim · `B20_NothingToWeight` | Text card | A ghosted variable shows a question mark and the weight arrow finds nothing; a new collection arrow draws instead. |
| A4 | Act title: Judgment in the Loop | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B21 | A prior leaking down a chain of judgments | Manim · `B21_PriorLeak` | Isometric pipes | A terracotta dye drops into the first stage and seeps into each later stage on its name. |
| B22 | The remaining three of the five | Manim · `B22_PriorLeak2` | Icon row | The dye reaches three more stages and a drawer of grey papers slides shut at the end. |
| B23 | Kappa formula with blinded vs unblinded counts | Manim · `B23_Kappa` | Table | Two agreement tables fill and the kappa bar drops from 0.6 to 0.2 on 'unblinded'. |
| B24 | Funnel plot with a missing corner | Manim · `B24_Funnel` | Matrix of disagreement | Simulated study dots fill a funnel, then the unpublished ones fade out of the lower-left corner. |
| B25 | Model greyed, three practices on the human step | Manim · `B25_NotTheModel` | Isometric stamps | The model block greys out while three practice tags land on the upstream human step. |
| B26 | A buried menu choice pushes entries one way | Manim · `B26_DataEntry` | Form mock | A cursor skips the deep accurate option and the tally bars lean in one direction. |
| B27 | Population share versus sample share and the weight | Manim · `B27_Reweight` | Bar chart | Sample bars sit off the population bars; each is rescaled by the weight on its name. |
| A5 | Act title: Historical and Implicit Bias | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B28 | Three ticks, and the harm remains | Manim · `B28_FaithfulData` | Checklist card | Three checks tick off one by one and the harm marker stays lit beside them. |
| B29 | P(historical | x) is not P(fair | x) | Manim · `B29_HiringHistory` | Equation alone | Green metric lights come on, then the two conditional probabilities slide apart with an unequal sign. |
| B30 | Trade-off curve with a human-chosen point | Manim · `B30_FitVsInheritance` | Three-option card | A fit-versus-inheritance curve draws and a dial the human sets slides along it. |
| B31 | Water table with four springs | Manim · `B31_WaterTable` | Icon row | A blue-grey water line draws below ground and four springs break the surface on their names. |
| B32 | An audit flag and three structural supports | Manim · `B32_Structural` | Three-option card | A flag rises over a gap, then three supports are set beneath the whole pipeline. |
| A6 | Act title: Three Flavors, and How They Compound | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B33 | Sample versus deployment population | Manim · `B33_FlavorDataset` | Pie charts | Two population blocks are compared and a thin slice is missing from the training one. |
| B34 | Crime, policing, re-arrest: the label sits on the last | Manim · `B34_FlavorLabel` | Text card | A policing filter draws between crime and re-arrest and the label tag lands on re-arrest. |
| B35 | Correct model on an uneven floor | Manim · `B35_FlavorStructural` | Isometric stairs | Three green ticks appear over a staircase whose steps are uneven for two groups. |
| B36 | Three flavors and where each is fixed | Remotion · `LectureEvidenceTable` | Manim drawn table | Rows carry the actual compared items; the ring moves on the spoken names. |
| B37 | A dataset fix aimed at a structural problem | Manim · `B37_WrongFix` | Stat card | A resampling arrow hits the data stage while the gap bars beyond it do not move. |
| B38 | Rebalancing adds historical bias | Manim · `B38_SelectionHistorical` | Two-layer card | New blocks fill the thin group and each carries the historical tint, so the tint total grows. |
| B39 | Disagreement grid: item columns versus annotator rows | Manim · `B39_ObserverCoding` | Kappa bars | A grid of agreements lights a column for coding, then a row for observers. |
| B40 | Two inflations stacked | Manim · `B40_ConfirmPublish` | Funnel | A stacked bar carries design inflation, then publication inflation; the correction removes only one slice. |
| B41 | Eight amplifying pairs | Manim · `B41_PairList` | Table | Eight pairs of chips link in turn, each pair joined by a bridge. |
| A7 | Act title: A Dataset Is Not the World | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B42 | A dataset as an archive with four fingerprints | Manim · `B42_Archive` | Text card | A box of records opens and four fingerprint tags land on it, one per spoken question. |
| B43 | ProPublica's own table, the false-positive row ringed | Remotion · `BrowserCapture` | Manim chart of the same four numbers | SHOW-THE-THING rung 1: the real record is the evidence; the camera pushes to the passage the sentence names. |
| B44 | ProPublica's four published error rates as bars | Manim · `B44_ErrorBars` | Table capture | Four bars grow from the published rates; the two false-positive bars, then the two false-negative bars, pair up. |
| B45 | Within each score, equal re-offense rates (schematic) | Manim · `B45_Calibration` | Capture of the response | Two calibration lines for the two groups lie on top of one another across the score axis. |
| B46 | Crime and policing both feed the label | Manim · `B46_ReArrest` | Two-arrow card | Two arrows, crime and policing, merge into the re-arrest label and the policing arrow is lit. |
| B47 | Recidivism nested inside policing inside the label | Manim · `B47_Nested` | Layers | Nested frames close around the thing the modeler thinks they predict and the label drops in front. |
| A8 | Act title: Two Fairness Claims, Both Correct | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B48 | The theorem's own abstract | Remotion · `BrowserCapture` | Manim equation card | SHOW-THE-THING rung 1: the real record is the evidence; the camera pushes to the passage the sentence names. |
| B49 | Two groups, one calibrated score, thresholds | Manim · `B49_Thresholds` | Two histograms | Two score distributions at different base rates; one shared threshold, then a second threshold appears and equal treatment breaks. |
| B50 | v/(1-v) = p/(1-p) · t/f built term by term | Manim · `B50_ImpossibilityAlgebra` | Text card | The identity assembles term by term with each symbol named beside it, then the base-rate factor splits in two. |
| B51 | The impossibility computed | Remotion · `CCPlainShell` | Manim bars | EXECUTABLE-EVIDENCE: the script's recorded stdout, not a typed result. |
| B52 | Three criteria that cannot all hold | Manim · `B52_Triangle` | Table | A triangle of three criteria: two corners light and the third goes dark each time one is chosen. |
| B53 | A loss function with its hidden value revealed | Manim · `B53_HiddenValues` | Text card | A loss formula sits under a neutral label and a hidden tag reading 'a value choice' is revealed in it. |
| B54 | The regulator's own sentences, quoted | Manim · `B54_AppleCard` | Capture (blocked by the site's bot protection; not bypassed) | A document card quotes the regulator's lines and the one about transparency is ringed last. |
| B55 | The three criteria and their joint limit | Remotion · `LectureEvidenceTable` | Manim drawn table | Rows carry the actual compared items; the ring moves on the spoken names. |
| A9 | Act title: Pearl's Ladder | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B56 | A three-rung ladder | Manim · `B56_Ladder` | Text card | A ladder builds rung by rung; the top rung is drawn ghosted. |
| B57 | P(Y | X) as a lookup in observed data | Manim · `B57_RungOne` | Equation alone | A scatter of observed pairs and a condition bar select the slice; the conditional probability reads off it. |
| B58 | do(X) cuts the arrows into X | Manim · `B58_RungTwo` | Equation alone | A graph with a hidden cause behind X; on 'do' the incoming arrow is cut and X is held by hand. |
| B59 | Crow and sunrise, observed versus intervened | Manim · `B59_Rooster` | Two probabilities | A crow and a sun rise together; the crow is blocked and the sun still rises. |
| B60 | The ghost rung stays at the top | Manim · `B60_RungThree` | Text card | The top rung lights with a question mark and a dashed arrow reaches toward it without arriving. |
| B61 | Observed versus do-version of the same sentence | Manim · `B61_DenialTwoWays` | Equation alone | Two probability expressions sit side by side; only the second has an arrow cut into race. |
| B62 | Four combinations of seen and caused | Manim · `B62_ComeApart` | 2x2 grid | A two-by-two fills: seen versus caused; the off-diagonal cells are ringed on their names. |
| B63 | Mitigation stuck at the first rung | Manim · `B63_RungOneStops` | Ladder alone | A figure climbs to rung one and stops; a gap sits between it and the do-rung. |
| B64 | Rung one versus rung two audit questions | Remotion · `LectureEvidenceTable` | Manim drawn table | Rows carry the actual compared items; the ring moves on the spoken names. |
| A10 | Act title: Finding the Leverage | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B65 | Three intervention points on one chain | Manim · `B65_ThreeTeamsGraph` | Isometric pipeline | A chain from world to decision lights three markers on its three stages. |
| B66 | The causal graph, node by node | Manim · `B66_BuildGraph` | Flowchart | Nodes land top to bottom, each with its arrows, on its spoken name. |
| B67 | Ten paths; what each intervention leaves open | Manim · `B67_PathCount` | Table | Ten paths highlight one at a time, then each intervention greys the paths it blocks. |
| B68 | Open paths after each team's fix | Manim · `B68_WhatIsLeftOpen` | Bar chart | The same graph appears three times; blocked paths grey out and the open-path counter reads 4, 8, then 0. |
| B69 | Steps one and two on the graph | Manim · `B69_Procedure12` | Numbered list (banned: bullet list) | Step markers land on the graph: arrows first, then each path traced. |
| B70 | Steps three and four as a choice | Manim · `B70_Procedure34` | Numbered list | Candidate cuts slice the graph one by one; the chosen cut glows and the needed path stays open. |
| B71 | Each location faces the question, one survives | Manim · `B71_DoubtFilter` | Text card | Candidate nodes each meet the question mark and drop away until one stays. |
| B72 | Engineer's house versus other houses | Manim · `B72_Houses` | Isometric rooms | House outlines draw around model and data; the graph's other nodes sit in other houses and the path crosses the walls. |
| A11 | Act title: Who Owns the Bias | Remotion · `FormACard` | Manim title with the act's first picture | A short act marker keeps the viewer oriented. |
| B73 | Structural analysis sits inside the technical chain | Manim · `B73_PoliticalTechnical` | Venn | A technical chain with a structural-analysis step that cannot be removed without breaking the link to the fix. |
| B74 | The question asked and the decisions it feeds | Manim · `B74_Formulation` | Text card | A question box feeds a row of downstream decisions; a gap opens where the formulation is delegated away. |
| B75 | The paper's own case summary, ringed | Remotion · `BrowserCapture` | Manim reconstruction | SHOW-THE-THING rung 1: the real record is the evidence; the camera pushes to the passage the sentence names. |
| B76 | A reply cut off upstream with a generic error | Manim · `B76_Truncated` | Chat card | An agent's answer starts, then stops at a gate upstream and the words 'unknown error' stamp over it. |
| B77 | The path starts outside the team's boundary | Manim · `B77_UpstreamGraph` | Houses | The team boundary draws; the biased node sits outside it with the path crossing in. |
| B78 | Switch, accept, or filter downstream | Manim · `B78_ThreeOptions` | Three-option card | Three doors: one locked, one open onto the bias, one with a filter gate. |
| B79 | Four possible owners of the node | Manim · `B79_FourOwners` | Icon row | The traced path ends at a node; owner tags drop onto four candidate nodes in turn. |
| B80 | Diffuse blame condensing onto one node | Manim · `B80_Undiffuse` | Text card | A cloud of small blame dots drains along the graph and gathers on one node. |
| B81 | A falsifier he would accept | Manim · `B81_ChangeMind` | Text card | A claim stands on a test; a dashed counter-example slot is drawn empty. |
| B82 | Two look-alike blobs and a door to the labeling process | Manim · `B82_StillPuzzling` | Text card | Two overlapping blobs read the same from the data; a door to the labeling step opens only from outside. |
| BVDT | Six-line recap | Remotion · `ClaudeVerdictArtifact` | Summary diagram | One bare sentence per idea; nothing new. |
| BHTF | Transfer task | Remotion · `ClaudeComposerAsk` | Worksheet | The viewer gets a usable prompt and two checks of their own. |
| BOUT | Locked title and channel sign-off | Remotion · `ClaudeTitleOutro` | None | The exact title spoken over the locked outro. |

## Tool beats and their SHOW-THE-THING rung

| beat | thing | rung | what is on screen |
|---|---|---|---|
| B10, B51 | the evidence script | 1 · run | `evidence/evidence.py` run on this Mac; stdout verbatim (constructed example, labelled) |
| B43 | ProPublica, Machine Bias | 1 · captured | the real table 'Prediction Fails Differently for Black Defendants', ringed |
| B48 | arXiv, Kleinberg et al. | 1 · captured | the real abstract, the theorem sentence ringed |
| B54 | New York DFS press release | 3 · quoted card | dfs.ny.gov returns a Cloudflare 403 to automated browsers; NOT bypassed. The regulator's sentences (fetched as text) are quoted on a drawn card |
| B75 | Agents of Chaos, page 20 | 1 · the paper's own page, rendered from its PDF | Case Study #6 summary, ringed |

Isometric lane (show-tell) auditioned for B01, B02, B04, B16, B35, B65, B72 and others: kept as a recurring simple cast only where the idea is a physical arrangement (B16 conveyor/gate drawn as a flat funnel; B35 steps). Causal graphs, equations and bar charts are flat Manim because the claim is a relationship, not an object.
