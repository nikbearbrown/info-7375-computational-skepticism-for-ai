# ACTS — Bias: Where It Enters and Who Is Responsible (Lecture 6, INFO 7375)

**What.** The coverage map: every section of Chapter 6 assigned to an act or listed under LEFT OUT with a reason; the eight merge-conflict blocks and which side was used; deck versus chapter; the recurring cast per act.
**Why.** The lecture skill's WHOLE-SOURCE LAW: nothing is dropped silently, and no merge block is resolved silently.
**Found.** Eleven acts, 82 body beats. The chapter's merge blocks were all resolved to the HEAD side (current course layer); two of the eight carry a teaching point (blocks 1 and 7, both HEAD-only). Only block 8 is not teaching prose. The Lecture 6 deck folder is empty, so the chapter is the whole source. Source read in full: `/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/chapters/06-bias-where-it-enters-and-who-is-responsible.md` (sha256 in `beat_sheet.json`; never edited).

## Coverage map

| Chapter section | Act | Treatment |
|---|---|---|
| Opening: the three engineering teams (constructed parable) | I Three Teams, One Problem (B01–B06) | Labelled constructed aloud; one gap-bar cast carried through the act; "an order of magnitude" is the parable's own claim |
| Learning objectives, Prerequisites, "Why this chapter uses the capacity twice" | — | LEFT OUT (course apparatus and cross-references; the Your Turn carries the build/audit idea) |
| What "bias" actually means (estimator, formula, more data, 1936 Literary Digest) | II What Bias Means (B07–B13) | Equation animated; the n = 10…10,000 simulation run and shown; 1936 poll numbers corrected (see FACTCHECK) |
| Ten mechanisms, distinguished: bookkeeping note, selection bias (+ IPW, propensity, unobserved case) | III Selection Bias (B14–B20) | Entry-point map; query funnel; IPW run and shown; propensity-score matching is not given its own beat (see LEFT OUT); the unobserved-driver case is spoken |
| The five that enter through the humans in the loop (+ kappa, funnel plot, trim-and-fill, self-report gold standard) | IV Judgment in the Loop (B21–B25) | Kappa worked on constructed counts; funnel simulated; the self-report "gold standard" discipline is not given its own beat (see LEFT OUT) |
| The two that enter at the keyboard (data-entry, sampling) | IV (B26–B27) | Reweighting numbers from `evidence.json` |
| Historical bias | V Historical and Implicit Bias (B28–B30) | Faithful-data checklist; the hiring illustration labelled as imagined |
| Implicit bias | V (B31–B32) | Water-table drawing; audit as flag not verdict |
| Three flavors mapped to the ten types (table, Fig 6.4) | VI Three Flavors, and How They Compound (B33–B37) | Table beat from the chapter's own table |
| How bias types compound (three worked pairs + table of eight) | VI (B38–B41) | Each worked pair and the eight-pair list |
| The dataset as epistemic artifact: archive, COMPAS, impossibility, Apple Card, criteria table | VII A Dataset Is Not the World (B42–B47) and VIII Two Fairness Claims, Both Correct (B48–B55) | Real ProPublica table and arXiv abstract shown; algebra and numbers computed; Apple Card held to "adjudicated, not proven" |
| Pearl's Ladder, Rungs 1 and 2 (+ Rung 3 sketched, rooster, fairness table) | IX Pearl's Ladder (B56–B64) | Rung 3 only as the ghost rung, as the chapter does |
| Leverage analysis (three teams resolved, procedure, Descartes' doubt, whose house) | X Finding the Leverage (B65–B72) | Constructed 10-path graph computed in `evidence.py`; counting paths labelled as not measuring bias |
| The political dimension is the technical dimension | XI Who Owns the Bias (B73–B74) | Attributed to Bear as an argument, not a finding |
| A limit case: leverage upstream; who owns it (Agents of Chaos Case #6; accountability; Arendt) | XI (B75–B80) | Verified against the paper's page 20; the chapter's `[verify]` flag is resolved by the primary |
| What would change my mind; still puzzling | XI (B81–B82) | Spoken as Bear's own uncertainty; the two named papers are LEFT OUT (chapter flags them unverified) |
| Synthesis and bridge | BVDT recap | One bare sentence per idea; the bridge to the next chapter is course sequencing, LEFT OUT |

## LEFT OUT (with reasons)

| Item | Reason |
|---|---|
| Learning objectives, Prerequisites paragraph, "Why this chapter uses the capacity twice" | Cross-references to other chapters and course apparatus; the lecture stands alone (SELF-CONTAINED LAW) |
| "Preview of next chapter" lines, Synthesis "next chapter" bridge | Cross-reference to a chapter the viewer has not seen |
| Glimmer 6.1 The Bias Trace | An exercise; its idea (trace a documented case, lock a prediction) is the Your Turn |
| Exercises W1–W3, A1–A4, S1–S4, C1, C2, the LLM Exercise (Agentic Red-Team Casebook) | Exercises are apparatus, not main teaching prose; optional per the brief. The Your Turn takes the leverage-and-owner idea |
| AI Wayback Machine (Hannah Arendt) and the "Prompts" D3 figure-generation prompts (end matter inside merge block 8) | Optional end matter; the Arendt idea already sits in the main text and is spoken in B80 |
| Hardt–Price–Srebro and Madras et al. citations in "What would change my mind" | The chapter flags them `[verify these references]`; not verified in this build, so not spoken |
| Propensity-score matching (named inside the selection-bias paragraph) | No beat of its own: IPW carries the same lesson (weight what you observed); matching adds a second method with no new idea |
| Self-report "gold standard" discipline, and trim-and-fill's mechanics | Named in one clause each (B22, B40); not given their own beats |
| Apple Card, Amazon résumé screener, Obermeyer health-cost-proxy mentions in the exercises | Exercise mentions; the Amazon and Obermeyer cases were not verified against primaries in this build, so not stated |

## SOURCE CONFLICTS (the chapter's eight unresolved merge blocks)

HEAD = `chapters/06-…` side (current course layer); other = `d78899b "Update chapters 1-14"` side (chapters numbered 03).

| # | Lines | HEAD says | Other side says | Used | Why / kind |
|---|---|---|---|---|---|
| 1 | 48–56 | A "design-critic" paragraph: the newspaper meaning of bias was optimized for moral clarity at the expense of causal precision; the formal definition gives up moral punch and buys something you can act on ("tells you where to intervene"); Figure 6.1 | Figure 3.1 with a truncated caption ("Biased vs") | HEAD | Real teaching sentence, only on the HEAD side. Spoken in B07. Image filename differs (06 vs 03) |
| 2 | 99–106 | Historical-bias fixes cannot be data-quality fixes; all are attempts to lower the leverage of the historical signal; each trades fit for less inheritance; "you decide how much fit to spend"; "no clean technical fix" | A shorter list of the same three mitigations (less-biased proxy, fairness constraints, time weighting), "none fully solve the problem" | HEAD | Same three fixes on both sides; HEAD adds the trade-off and who decides. Nothing in the other side contradicts it. Spoken in B30 |
| 3 | 114–122 | Figure 6.3 (pipeline entry-point map) only | Figure 3.3 plus an older duplicate of the implicit-bias audit paragraph (demographic-parity auditing, diverse teams, structured processes, continuous auditing) | HEAD | Image-only on HEAD; the other side's paragraph duplicates text already in the common portion directly above the block. Not teaching prose that is missing |
| 4 | 211–219 | Figure 6.5 (fairness impossibility visual proof sketch) | Figure 3.4 and a stray duplicate caption "Figure 3.2" | HEAD | Image filename and caption only |
| 5 | 242–250 | Figure 6.6 (Pearl's ladder) | Figure 3.5 and duplicate caption "Figure 3.3" | HEAD | Image filename and caption only |
| 6 | 285–293 | Figure 6.7 (causal graph of a biased deployment) | Figure 3.6 and duplicate caption "Figure 3.4" | HEAD | Image filename and caption only |
| 7 | 310–318 | Figure 6.8 and the Descartes paragraph: leverage analysis is Descartes' doubt turned on a pipeline | Figure 3.7 only | HEAD | Real teaching sentence, only on the HEAD side. Spoken in B71 |
| 8 | 531–613 | "Preview of next chapter" (Chapter 7 fairness) | A different preview (Chapter 4's journal), the AI Wayback Machine (Arendt) and the D3 figure-prompt apparatus | HEAD | End matter and apparatus, not teaching prose. Arendt's idea is already in the main text and spoken in B80 |

Net: blocks 1, 2 and 7 each carry a real teaching point (all on the HEAD side, nothing contradicts anything, so nothing from the other side was needed). Blocks 3–6 differ only in image names and duplicate captions; block 3's other side repeats a paragraph that is already in the common text. Block 8 is end matter. No real conflict between two contradictory teachings exists in Chapter 6, but the file still needs Bear's resolution (the manuscript is untouched).

## DECK vs CHAPTER

The Lecture 6 deck folder `/Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/lectures/03-bias-where-it-enters-and-who-is-responsible/` (named 03 before the book was renumbered on 2026-07-02) holds only `assets/assets.json` with no assets. There is no deck, no narration seed, no figure. The chapter is the whole source; the order of acts is the chapter's order.

| Deck had | Chapter has |
|---|---|
| nothing | everything above |

## Cast per act

| Act | Recurring objects |
|---|---|
| I | one pair of outcome bars (the gap) and one pipeline strip: data → model → reviewer → outcome; team one/two/three flags |
| II | the number line with true value θ and the estimate cloud; the 1,000-dot sample |
| III | patient dots, the query gate, grey dropped dots |
| IV | five-stage judgment chain with the terracotta prior dye; kappa tables; the funnel |
| V | green-tick checklist; the water table |
| VI | sample/label/world three-tier strip; the pairs of chips |
| VII–VIII | archive box; the two group colours (ink and dim); the three-criteria triangle |
| IX | the ladder, three rungs, rung three ghosted |
| X | the ten-node causal graph (A, P, D, L, F, M, O, R, C, K) |
| XI | the same graph inside a team boundary; the owner tags |

## Interpretive choices, flagged
- Greeting: Namaste (Bear's brief); the pronunciation dictionary has an entry.
- The film says "Lecture 6" only in BIDEA and the on-card credit lines; elsewhere it never says "chapter" or "the book".
- Bear's frameworks, said once with a plain gloss at first use: the five supervisory capacities (B74).
