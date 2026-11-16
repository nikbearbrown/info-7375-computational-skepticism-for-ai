# SHOTLIST — tldr-average-hides-the-patient
This is the typed work order per slot. Every slot is pipeline-owned: **no human media, no pantry, no gen-AI** (tldr rule 6). Every number is the chapter's own or is first-party arithmetic on the chapter's inputs, asserted in code.

| Beat | Role | Type × source | Owner | What it is |
|---|---|---|---|---|
| B00 | TL;DR · WHAT | REMOTION own (bookend) | pipeline | ClaudeTldrWhat: "Salaam, Liam"; the question writes on; three numbered lines land on their clauses |
| B01 | TL;DR · WHY | REMOTION own (bookend) | pipeline | ClaudeTldrWhy: the stake writes on; three dashed consequences land |
| B02 | THE QUESTION | REMOTION own (bookend) | pipeline | BrutalistHesitantWriter: "for every patient" → "group by group" |
| B03 | TERMS | REMOTION own (card) | pipeline | ClaudeDefinitions: calibration · calibration error · subgroup · confidence bin |
| B10 | HOOK | GRAPHIC own | Manim `B10_OneNumber` | one wide bar at 0.018 over 12,955 patients; the rare row (95, 0.103); "both true — how?" |
| B11 | INSTANCE | GRAPHIC own | Manim `B11_SplitRows` | the bar splits into five equal columns at 0.018; adults settle to 0.019, children climb to 0.029 |
| B12 | INSTANCE | GRAPHIC own | Manim `B12_ThreeClimb` | 65+ 0.044, pregnancy 0.071, rare 0.103 climb; the twice-global line draws; three above it |
| B13 | NAIVE | GRAPHIC own | Manim `B13_AverageRows` | the row-average line at 0.053 against the report's 0.018; X beside "average of the rows" |
| B14 | SHIFT | GRAPHIC own | Manim `B14_WeighPatients` | column widths morph to patient counts; the rare row becomes a sliver; area readouts 0.012 and 0.0008 |
| B15 | INSTANCE · predict | GRAPHIC own | Manim `B15_Predict` | the line one hundredth above the global; dot beside the sliver; hold |
| B16 | TRANSFORM | GRAPHIC own | Manim `B16_PourAndLift` | the sliver pours into a hairline (0.0008; ≤ 0.0073 at error 1), gathers back, and widens to the whole axis at 0.103 |
| B17 | ABSTRACTION | GRAPHIC own | Manim `B17_NameIt` | the ECE_g formula; a brace under N_g; "subgroup calibration error"; the reporting rule |
| B18 | TANGENT | GRAPHIC own | Manim `B18_Tangent` | formula on top; sentences, glossary, the weights 95/12,955 and 95/95, the 0.018 ≤ 0.028 line |
| B19 | PAYOFF | GRAPHIC own | Manim `B19_BothTrue` | the HOOK's bar splits into patient columns that rise; "both true"; boundary caption |
| BVDT | VERDICT | REMOTION own (bookend) | pipeline | ClaudeVerdictArtifact: four lines |
| BHTF | YOUR TURN | REMOTION own (bookend) | pipeline | ClaudeComposerAsk "Your turn.": exercise A5 as a predict-then-compute transfer, read in full |
| BOUT | OUTRO | REMOTION own (bookend) | pipeline | ClaudeTitleOutro: spoken title + "At Nik Bear Brown", 1.0 s tail, no jingle |
