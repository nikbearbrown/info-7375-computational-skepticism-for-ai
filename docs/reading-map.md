# Reading map and cross-book connections

Readings selected 2026-09-06. The course has fifteen lessons; the narrative book has thirteen main topics plus alternate drafts. Lesson numbers are course positions, not a renumbering of the book. The exact source filenames are recorded in [course.json](../course.json) and each lesson.

## Introductory chapters: before the Skeptic’s Toolkit

Read these new introductory chapters in this order before the existing Chapter 1:

- [Agents: Understanding Before Delegating](../chapters/00a-agents-understanding-before-delegating.md).
- [Agentic Loops](../chapters/00b-agentic-loops.md).

The canonical source is the sibling `computational-skepticism-for-ai` book. The two files here are byte-identical reading copies at integration; future revisions should be made in the book and synchronized deliberately. This addition does not renumber the existing thirteen chapters, alter the historical Fall 2026 lesson positions in `course.json`, or change assignments or grading. The introductory filenames are reading-order prefixes, not extra lesson numbers.

## Main book selections

Use 01 toolkit; 02 probability; **03 data validation**; 04 robustness; **05 model explainability**; 06 bias; 07 fairness; 08 agent validation; **09 delegation**; **10 visualization**; 11 uncertainty; **12 accountability**; **13 limits**. Lessons 14 and 15 synthesize prior readings. These are explicit course selections, not deletions or claims that the competing drafts have been editorially resolved.

The alternative data-validation file numbered 05, delegation file numbered 10, and accountability file numbered 13 remain available but are not assigned by this map. Underscore-prefixed Chapter 1 materials are editorial supplements. Chapter 97 provides thematic background; it does not set grading.

## Editorial cautions for the course

- Literal merge-conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) remain in chapters 2, 4, 5, 6, 7, 8, 10, 11 and 13 (checked 2026-10-18). Chapter 1 needs a version-specific caution: the committed file at `df0a3fd` contains three conflict blocks, including one around the Knight Capital example; the locally modified working copy has no literal markers (checked 2026-11-12). A marker-free local draft does not establish that the published chapter is resolved. Do not treat conflict blocks as student instructions. The course has not silently merged competing manuscript text.
- Chapter 7 sometimes equates predictive parity with score calibration. In this course, precision parity concerns P(Y=1 | predicted positive, group); score calibration concerns outcomes conditional on a probability score. They are distinct. Impossibility and tradeoff claims depend on assumptions; identical groups and perfect predictors matter as boundary cases.
- Some manuscripts make universal claims about AI's inability to verify, report uncertainty, or reason causally. Treat these as arguments to test against their scope and counterexamples, not empirical laws established by this adaptation. External tools can contribute useful verification; a person's review also needs evidence.
- Do not infer that every classifier is deterministic or that a wrong prediction has only a bounded downstream consequence. Course fixtures are deterministic by construction; live systems and their uses require separate analysis.
- The limits chapter labels an opening clinical story as a composite. Preserve that label. No course fixture is evidence that this historical incident occurred.
- Chapter 11's verb ordering is a writing heuristic, not an automatic measure of truth. The linter is deliberately fallible.

## Prompt Engineering for Generative AI

Source: sibling info-7375-prompt-engineering-for-generative-ai, [Lesson 2: Prompt contracts and evaluation](../../info-7375-prompt-engineering-for-generative-ai/lessons/02-prompt-contracts-and-evaluation/docs/en.md). Connection: an output contract specifies structure; the audit still needs to establish support for the content. Apply this to Lesson 3's Claude-assisted join and datasheet.

For readers without the sibling checkout: write the input, expected output fields, validation rules, and a case where valid formatting hides a false claim. The original [public lesson](https://github.com/nikbearbrown/info-7375-prompt-engineering-for-generative-ai/blob/main/lessons/02-prompt-contracts-and-evaluation/docs/en.md) provides the extended exercise.

## Conducting AI

Source: [Chapter 2 — The Solve–Verify Asymmetry](../../info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md), especially its discussion of external grounding, “The live counter-case: reasoning models,” and Exercise 2.3, “Map the boundary.” Apply to Lessons 1, 9, 12, and 13.

The transferable practice: name the source, final state, or independent calculation used to check a generated answer, and the person responsible for deciding its adequacy. A second model opinion may share the first model's assumptions. The manuscript itself calls its strongest structural claim a wager; this course does not turn it into a proof or import its 30-point reading-response rubric.

## Irreducibly Human

Source: [Chapter 4 — Tier 4: Metacognitive & Supervisory](../../info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md), “How metacognition is taught — and the transfer that never happens.” Apply to Lessons 2, 7, 11, and 15.

The transferable practice: record confidence before seeing results, monitor the mismatch, and revise a concrete judgment. AI should calculate, propose tests, and help organize evidence. Humans should practice the mechanism, choose the relevant criterion, inspect evidence, and own authorized decisions. This division describes course responsibilities; it does not assert infallible human judgment or universal machine incapacity.

## Branding and AI

Source: [Chapter 18 — Portfolio as Product](../../info-7375-branding-and-ai/chapters/18-portfolio-as-product.md), the distinction among portfolio surfaces and the discussion of curation and technical evidence. Apply to Lessons 10 and 14.

The transferable practice: make a short audience-facing explanation point to an inspectable technical artifact, with consistent claims across both. Clear written evidence can do this. The course imports neither the companion's web-development stack nor a requirement to deploy a public portfolio.

Sibling links work in the books/ checkout. The explanations above are self-contained when these books are unavailable; companion reading is enrichment rather than a hidden prerequisite. This course conversion does not convert or modify the other books.

