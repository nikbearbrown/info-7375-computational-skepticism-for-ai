# Case study checklist

## Executive summary

**What this is.** A short list of things to look for when you read a case study in INFO 7375, Computational Skepticism for AI. Each case on the exam describes a situation, an instruction given to an AI system, and that system's confident output, with at least one real flaw in it. This checklist is the set of questions to run through before you write anything.

**Why read it.** The exam rewards finding the real flaw, naming it with the exact term, asking for the evidence that would settle it, and writing a fix. Each item below gives you the question to ask, the exact terms, what the problem looks like on the page, the evidence to ask for, and a fix, with a job-search example.

**Status.** Started 2026-11-12. Nine checklist items so far: (1) what we measure versus what we care about; (2) whether there are checks, whether they are the right ones, and whether the right agent does them; (3) what could make this wrong, which is Cartesian doubt; (4) what is missing from the data, which is the Kantian slice; (5) whether deterministic work such as math and random draws is done by code or by a language model; (6) whether the system said "I don't know" when it did not know; (7) whether anyone outside the source validated it; (8) whether anyone tried to break it (adversarial checks); (9) where bias could have entered, with the formal definition, the ten ways in, the three flavors and the trade-offs of fixing it. Then notes on skepticism (it is about evidence), falsifiability, plausibility auditing and the fluency trap for the multiple-answer questions, plus a short reminder of what each term named after a person means (Cartesian doubt, Hume's induction problem, the Kantian slice and the rest), because the name is easier to remember than the idea. Items are added one at a time, in the order Professor Bear names them.

---

## How to use it on a case

Read the case once for the story. Then go down the list and ask each question of the case. When one of them catches, you have the answer to the four probes:

1. **What is wrong, and the exact term:** the item's question, and its terms.
2. **The check that turns the claim into evidence:** the item's "Evidence to ask for".
3. **The corrected instruction:** the item's "Fix".
4. **Two plain sentences for the stakeholder:** the item's "In plain words".

A case can have more than one flaw. Keep going after the first hit.

---

## Terms named after people: what each one means

Many of the course's terms carry a person's name, and the name is easy to remember while the idea is not. Each line gives the person in a few words, the idea in plain words, and the question it gives you on a case. Definitions follow the course's glossary decks.

**The Skeptic's Toolkit (Chapter 1)**
- **Cartesian doubt** (Descartes, a philosopher who doubted everything he could). Doubt a claim until you can list the conditions under which it would be wrong. *On a case:* what would have to be true for this output to be wrong? That list is your suspects.
- **Hume's induction problem**, also called the **limit of induction** (Hume, a philosopher). However many times something worked before, that is no guarantee it works next time; the world has to cooperate. *On a case:* is the system trusted only because it has worked so far? What has changed? (Example: for years, knowing some Python got people entry-level programming jobs, until AI coding agents arrived.)
- **Popperian falsifiability** (Popper, a philosopher of science). A real claim says in advance what would prove it false: the metric, the threshold and the time window. *On a case:* could any result have shown this claim wrong? If not, it is a rhetorical claim.
- **Kantian slice** (Kant, a philosopher). You only ever see a slice of the world, so keep in view what lies outside it. *On a case:* what could this system, this test or this dataset not see?
- **Goodhart's law** (Goodhart, an economist). When a measure becomes a target, it stops being a good measure. *On a case:* is someone pushing on the number, so it rises while the real goal does not? (See item 1.)

**The Confidence Illusion (Chapter 2)**
- **Bayes' theorem** (Bayes, an eighteenth-century minister and mathematician). Update a belief with evidence: what you believed before, times how likely the evidence is if it is true, divided by how likely the evidence is overall. *On a case:* how common was the thing before the test (the base rate)?
- **Turkey problem**. A turkey grows more confident every day it is fed, until the day it is not. Hume's problem as a picture. *On a case:* is the confidence built only on days that went well?

**Data Validation (Chapter 3)**
- **Plato's Cave** (Plato, a philosopher). A dataset is shadows on a wall, not the world that cast them; checking the data measures the shadows, not the fire. *On a case:* who recorded this data, how, and what did that recording leave out?
- **Datasheets for Datasets** (Gebru and colleagues). A set of questions that documents where a dataset came from, how it was collected and who maintains it. *On a case:* is there a record of how this data came to be?

**Model Explainability (Chapter 5)**
- **Shapley value** (Shapley, a mathematician who studied fair sharing). The credit a feature gets for one prediction, averaged over every order in which the features could be added. *On a case:* it explains what the model used, not why the outcome happened in the world.
- **Rudin's argument** (Rudin, a computer scientist). For high-stakes decisions, use a model people can read, rather than explaining a black box afterwards. *On a case:* should this decision be made by a model nobody can read at all?

**Bias and Fairness (Chapters 6 and 7)**
- **Pearl's ladder** (Pearl, a computer scientist who works on causation). Three levels of causal question. **Only the first two rungs are on the exam.**
  - **Rung 1, association (seeing):** two things go together. An association goes both ways: it does not tell you which one drives the other, or whether something else drives both. *Example:* applicants who send cover letters get more interviews; that alone does not show the letters cause the interviews.
  - **Rung 2, intervention (doing):** a small experiment that changes one thing on purpose to test the direction of an association. *Example:* send a cover letter with a randomly chosen half of your applications, and compare the interview rates.
  - **Rung 3, counterfactual (imagining what would have happened to this one case)** is not on the exam. For more on counterfactuals, take the 7390 course.
  - *On a case:* does the claim say one thing causes another? If the evidence only shows the two go together (rung 1), ask for an intervention (rung 2).
- **Cohen's kappa** (Cohen, a statistician). How much two people labelling the same items agree, beyond what chance alone would give. *On a case:* if the labels come from people, do they agree?
- **Lipschitz condition** (Lipschitz, a mathematician). Two people who are nearly alike should be treated nearly alike; the gap in treatment may not exceed the gap between them. *On a case:* do two near-identical applicants get very different outcomes?

**Accountability (Chapter 12)**
- **Kantian framework** (Kant again). Responsibility follows who could have acted otherwise and what duty the situation put on them. *On a case:* who could have stopped this, and was it their job to?
- **Utilitarian framework**. Hold accountable whoever it does the most good to hold accountable, to change incentives and reduce harm. *On a case:* whose behaviour would change if they were held responsible?
- **Gödel analogy** (Gödel, a logician). Gödel showed that a consistent formal system rich enough for arithmetic cannot prove its own consistency; the course uses this only as an analogy for why a system should not certify itself. It is not a proof about AI. *On a case:* is the system checking its own work?

**The Limits of AI (Chapter 13)**
- **Turing's argument** (Turing, a founder of computer science). If behaviour is enough evidence that a person has a mind, demanding more of a machine is unprincipled. *On a case:* does the claim rest on behaviour alone?
- **Chinese Room** (Searle, a philosopher). Following rules on symbols can look like understanding without being understanding. *On a case:* does the system understand, or produce the right-looking output?
- **Mediocristan and Extremistan** (terms from Taleb, a writer on risk). In Mediocristan no single case moves the average (heights); in Extremistan one rare case can outweigh all the rest (wealth). *On a case:* can one rare event outweigh everything the system was tested on?
- **Black swan** (Taleb's term). A rare event that no past data could have anticipated. *On a case:* what would a black swan look like here, and what happens if it arrives?

---

## Other terms to know

- **Black box model:** a model whose inner workings a person cannot inspect or follow. You can see what goes in and what comes out, but not how it got from one to the other. Large neural networks and most commercial AI systems used through an app or an API are black boxes to the people using them.
  - *Not the same as:* an **interpretable** model, which a person can follow well enough to predict new cases (a short scoring rule, a small decision tree). **Transparency** (the code, weights and data can be inspected) does not by itself make a model interpretable: a published network with millions of weights is open and still a black box to a reader.
  - *Explaining a black box afterwards:* tools such as SHAP and LIME give a **post-hoc explanation**, a reason worked out after the output. It describes what the model used, not why the outcome happened in the world. Rudin's argument: for high-stakes decisions, use an interpretable model rather than explaining a black box after the fact.
  - *In robustness:* a **black-box attack** only sees the model's outputs and probes them; a **white-box attack** has the model's insides (weights and gradients).
  - *On a case:* if the system is a black box, ask what evidence exists that it works (item 7, validation) and whether a decision this important should rest on a model nobody can follow.
  - *Job-search example:* an applicant-tracking system rejects a résumé and nobody, including the employer, can say how it reached that score. A short published checklist of required qualifications would be interpretable.

---

## 1. What are we measuring, and what do we care about?

**The question.** What number is the system being judged on, and what does anyone actually want? Ask of the number: *what is this a number of?*

**Why it matters.** The thing we care about is usually hard to observe, so systems are scored on something nearby that is easy to compute. Usually the easy thing tracks the hard thing, which is why it was picked. So every metric says success, and the failure stays invisible until someone checks the hard thing.

**Exact terms.**
- **Measure versus want:** the number a system is scored on is only a stand-in for what is really needed.
- **Gap from the start:** the stand-in never matched the target. You can catch it before deployment by asking what the number measures.
- **Gap that opens later:** the stand-in matched, then the world moved (or pressure was put on the number), and it stopped matching. You catch it only by checking again.
- **Goodhart's law:** when a measure becomes a target, it ceases to be a good measure.

**What it looks like in a case.**
- Success is reported as a number (accuracy, error, a score, a count, a rate) and nobody says what that number stands for.
- The number is easy to compute; the real goal (a good hire, a satisfied user, a patient who recovers) is never checked.
- People or systems are rewarded on the number, and the number keeps improving.
- The measure was chosen some time ago, and something about the world has changed since.

**Questions to ask.**
- What is the system scored on? What does the person in the case actually need?
- Did the stand-in ever track the need (gap from the start), or did it track it once and drift (gap that opens later)?
- When did anyone last check the real goal, not just the number?
- Is someone pushing on the number, so it rises while the goal does not (Goodhart's law)?

**Evidence to ask for.**
- A direct check of the want on a sample: follow a batch of cases to the real outcome, and compare it with the number.
- How well the number and the want agree on recent cases, against how well they agreed when the measure was chosen.
- The date the link between the measure and the want was last checked, and who checked it.

**Fix (an instruction you could give).** "Before reporting success, name the outcome we actually care about. Check a sample of recent cases against that outcome, report how often the score and the outcome agree, and say when this was last checked. Do not report the score alone."

**In plain words (for the stakeholder).** "The system is getting better at the number it is graded on, but nobody has checked whether that number still means what we want. Until someone checks real outcomes, treat the improvement as unproven."

**Job-search examples.**
- *Measure versus want:* an AI job agent reports "120 applications sent this week". The count is the measure; what the job seeker wants is interviews, and in the end a good job.
- *Gap from the start:* a job seeker ranks listings by how impressive the title sounds. A grand title was never the same as a good job.
- *Gap that opens later:* a polished cover letter used to signal effort. Once AI tools could produce one in seconds, polish stopped meaning effort.
- *Goodhart's law:* applicant-tracking systems score résumés on keywords from the listing, so job seekers copy the keywords in. The scores climb and say less about who can do the job.

**Course cases.** The Netflix Prize (scored on star-rating error; members wanted something to watch tonight; a gap that opened later when streaming arrived) and the Amazon recruiting engine (scored on resemblance to past résumés; the want was ability to do the job; a gap from the start).

**Source.** Chapter 1, The Skeptic's Toolkit, "What you measure and what you care about" (`chapters/01-the-skeptics-toolkit.md`). Film: *Key Terms: The Skeptic's Toolkit* (Computational Skepticism, Exam Prep).

---

## 2. Are there checks? Are they the right checks? Is the right agent doing them?

**The question.** Three questions, asked early on every case:
1. **Are there checks at all?** If there are none, the system had better be very simple. Even a moderately complex system needs checks.
2. **Are the checks appropriate?** Does each check actually test what could go wrong at that step, or is it a box ticked?
3. **Is the appropriate agent doing each check, human or AI?** Some checks an AI does well. Others it should not do at all.

**Why it matters.** An AI produces output in seconds, and checking it can take far longer, so checks get skipped or quietly waved through. A system with no checks, or with checks done by the wrong party, can fail without anyone noticing, and the confident output looks the same either way.

**What an AI can usually check.** Things with an exact, mechanical answer that anyone could confirm by inspection:
- Does the code run, and do the tests pass?
- Is this hex color exactly the value in the design file?
- Is every required field present, in the right format?
- Does the arithmetic add up? Do the dates parse?

**What an AI should not be the one to check.** Things that need knowledge of the world, judgment, or someone who answers for the result:
- Whether the output is true about the world, not just well formed (plausibility auditing).
- Whether it answered the right question (problem formulation).
- What a number means in this setting (interpretive judgment).
- Its own work: a model's self-check comes from the same system being checked.
- Another AI built the same way: the two share blind spots.
- High-stakes or irreversible decisions, and the final sign-off. Someone has to answer for those, and an AI cannot.

**Exact terms.**
- **Verification cost:** how costly a human check is. A check that is nearly a redo quietly pushes people to accept the output.
- **Solve-verify asymmetry:** in computer science checking is easier than finding; in AI deployment, producing is cheap and verifying is costly.
- **Stakes:** the cost of being wrong on a step. When one error is catastrophic, the average is the wrong statistic.
- **Reversibility:** whether an action can be undone. Irreversible ones need a human approval gate (a **gating condition**).
- **Delegation buckets:** the three outcomes of the sort: AI executes, human only, or hybrid with human checks.
- **Phase gates:** who does what, task by task, AI or human.
- **Delegate freely / delegate and verify / do not delegate:** mechanical work you can check by inspection; plausible output you must check against the world; work that stays with a person.
- **Irreducibly human:** a step the AI cannot take because it needs domain knowledge, domain judgment or responsibility.
- **Testable** and **graded testability:** a check a stranger could apply and tell whether it was met; some checks anyone can do, some only a qualified reviewer, some nobody.
- **Validator independence:** a check counts only when it comes from outside the system being checked.
- **Metacognition:** checking one's own reasoning; a model's self-check comes from the same system it is checking.
- **Common cause failure:** two checks built alike fail together; a monitor shares the blind spots of what it watches.
- **False-success catch:** after an action, observe the world yourself and compare it with the report.
- **Plausibility auditing:** asking whether an output could even be true of the world it describes.

**What it looks like in a case.**
- An agent reports "done" or "verified", and the only verification is the agent's own say-so.
- A second AI, or the same model, is used to check the first one's work on a question of fact or judgment.
- A person is said to "review" the output, but nothing says what they check, and the review is as long as doing the work again.
- An action that cannot be undone (sending, paying, deleting, publishing) runs with no human approval.
- A fairly complex pipeline with several steps and no check named at any of them.

**Questions to ask.**
- List the steps. Where is each check, and who does it?
- For each check: what exactly does it look at, and would it catch the flaw that matters at that step?
- Is each check something an AI can confirm mechanically, or does it need judgment, world knowledge or accountability? Does the right party do it?
- Is any check the system certifying itself?
- Which steps are irreversible or high-stakes, and is there a human gate before them?

**Evidence to ask for.**
- The list of checks per step, each with who performs it and what counts as a pass.
- The record that each check actually ran (the artifact it leaves: a log, a filled checklist, a test result), not a statement that it did.
- For an AI's check: a sample of its passes re-checked independently, to see what it lets through.

**Fix (an instruction you could give).** "Before any step runs, list the checks: what each one tests, who does it (AI or a named person), and what counts as a pass. Let the AI run the mechanical checks (tests, exact values, formats). A person checks anything that needs judgment about the world, and approves every irreversible action. Record each check as it happens."

**In plain words (for the stakeholder).** "Right now nobody independent checks whether the system's work is right before it goes out. The machine can check the routine parts; a person needs to check the parts that need judgment, and sign off before anything that cannot be undone."

**Job-search examples.**
- *No checks:* an agent finds listings, tailors the résumé and submits applications all week, and nothing checks any step. Fine for sorting listings into folders; not fine for sending applications in someone's name.
- *Right agent, AI:* the agent checks that every application has a résumé attached, the file is a PDF, and the job ID matches the listing. Mechanical, exact, checkable by anyone.
- *Wrong agent:* the same AI that tailored the résumé is asked whether the résumé is truthful. Only the job seeker can confirm that a skill listed is really hers.
- *Check that is not appropriate:* "a human reviews each cover letter", with no checklist, so the review is skimming. An appropriate check: confirm the company name, the role, and every claim about the applicant against her real history.
- *Irreversible step:* submitting an application cannot be taken back, so the job seeker approves each one before it goes.

**Course cases.** The Ash case (an agent reported a secret email deleted; it was still on the server, and no check caught it; the fix is a false-success catch, observing the world after the action). The Knight Capital deployment (seven of eight servers updated, ninety-seven warning emails unread).

**Source.** Chapter 9, Delegation, Trust, and the Supervisory Role; Chapter 8, Validating Agentic AI; Chapter 12, Accountability; Chapter 13, The Limits of AI (delegate freely, delegate and verify, do not delegate); Chapter 1 (solve-verify asymmetry, the five supervisory capacities).

---

## 3. What could make this wrong? (Cartesian doubt)

**The question.** Take the case's main claim, the one the AI output or the stakeholder is most confident about, and ask: *what would have to be true for this to be wrong?* Keep asking until you have a list. The list is the product.

**Why it matters.** This is the heuristic that turns a vague unease into things you can check. It works best exactly when nothing looks wrong: when the system reports success and means it. It does not tell you which suspect is guilty; it gives you the suspects, and the evidence step (item 2's checks, Popperian falsifiability) settles them.

**Exact terms.**
- **Cartesian doubt** (Descartes): doubt a claim until you can list the conditions under which it would be wrong.
- **Artifact versus world:** the output (a score, a "done", a report) is not the thing it describes. "The command returned success" and "the system is doing what we intend" are different claims.
- **Popperian falsifiability:** the follow-up move: name the result that would show the claim false.

**The usual suspects** (the chapter's three, checkable on almost any case):
- **Coverage:** did the training or test data under-represent cases like this one?
- **Inputs:** do the inputs actually contain the signal that matters?
- **Context:** is the system used the way it was tested, on the people or conditions it was tested on?

Then add the case's own: a step that silently failed, a source that was not what it claimed, a number that was not computed the way it says.

**What it looks like in a case.**
- A confident success claim ("deployment succeeded", "the model is accurate", "all applications sent") with nothing that would show it false.
- Someone trusts the output because it agreed with them the last many times.
- A "done" or "success" that comes from the system's own report rather than from looking at the world.

**Evidence to ask for.** For each suspect on your list, the one check that would rule it in or out: the share of cases like this one in the test data; whether the input field holds the signal; whether the deployment matches the test conditions; an independent look at the world after the action.

**Fix (an instruction you could give).** "Before reporting this as a success, list the conditions under which it would be wrong, at least: under-covered cases, missing input signal, and a difference between how it was tested and how it is used. For each, run the check that rules it in or out, and report the results with the claim."

**In plain words (for the stakeholder).** "Nobody has yet asked what would make this result wrong. There are at least three ways it could be, and each one can be checked before we rely on it."

**Job-search example.** An AI screener gives a résumé two stars. Cartesian doubt asks what would make that rating wrong about this applicant: résumés like hers were rare in the training data, the features miss what she can actually do, or the screener is being used on a kind of job it was never tested on. Each is a check, not an argument.

**Course cases.** A two-star rating on a résumé (the chapter's own example). Knight Capital: ask what would make "deployment succeeded" wrong about the running system, and it points straight at the eighth server that missed the update and the ninety-seven warning emails nobody read.

**Source.** Chapter 1, "What I mean by skepticism" (Descartes's move and Figure 1.1).

---

## 4. What am I not seeing? What is missing from the data? (Kantian slice)

**The question.** What am I not saying? What is important to this decision that should be in the data, and is not? Every dataset, test and model sees only a slice of the world. Name what lies outside the slice.

**Why it matters.** A review can examine the output closely (how it was computed, how well it matches the training data) and still never touch the question that mattered, because that question lives outside the slice being examined. Missing things do not show up as errors; they simply are not there.

**Exact terms.**
- **Kantian slice** (Kant): you only ever see a slice of the world; keep in view what lies outside it, and the fact that there is an outside at all.
- **Artifact versus world:** the output is not the thing it describes. Ask: what is the artifact, what is the world, and what is the relationship between them?
- **Recording instrument:** the sensor, form or system that did the recording, and what it could not see.
- **Epistemic frame:** every unwritten decision about what was recorded, kept, joined and cut off.
- **Plato's Cave:** a dataset is shadows on a wall; checking the data measures the shadows, not the fire.
- **Selection bias** and **sampling assumption:** who is in the data depends on what happened to them, or on who was easy to reach; deployment meets everyone.
- **MNAR** (missing not at random): the gaps follow the missing value itself. *Good to know for a real dataset; MCAR, MAR and MNAR are not on the exam.*

**What it looks like in a case.**
- A conclusion drawn from records of only some of the people or events it is about (only those hired, only those who applied online, only the cases that were flagged).
- A field that matters to the decision is not collected at all, and nothing says so.
- Blanks that are likelier for some kinds of cases than others.
- A test set drawn from the same narrow place as the training data, so the test shares the slice.
- An output that cites only what its sources contained, with no word on what the sources could not see.

**Questions to ask.**
- What decision does this support, and what would a person need to know to make it well?
- Which of those things are in the data, and which are not? Who recorded the data, and what could that recording not see?
- Who is missing: people never recorded, people screened out earlier, people who did not answer?
- Are the gaps random, or do they follow something that matters?

**Evidence to ask for.**
- A list of what the data contains and what it leaves out, set against what the decision needs.
- Where the data came from and how it was recorded (a datasheet), including who was not reachable.
- A check on a sample from outside the slice: the cases not recorded, the people turned away, a different site or period.

**Fix (an instruction you could give).** "Before reporting this, list what the decision needs to know and mark which of those things the data contains. Name who and what is not in the data and why. Check the conclusion on cases from outside the data's reach, or state plainly that it covers only the slice it saw."

**In plain words (for the stakeholder).** "This result is based on part of the picture. Some things that matter for the decision are not in the data at all, so the result says nothing about them until someone looks."

**Job-search examples.**
- A hiring model learns from how the people it hired turned out. The people it turned away are outside its slice; nobody knows how they would have done.
- An AI job agent searches the big job boards. Jobs posted only on company sites, or filled by word of mouth, are not in its data, so "no good matches" may mean "no matches on the boards I can see".
- A salary tool learns from salaries people chose to post. Offers nobody posted, often the low ones, are missing, so its estimates run high.

**Course cases.** The Amazon recruiting engine (the rating was the artifact; whether the applicant could do the job lived outside the slice the review examined). The COVID chest X-ray models (they read a marker in the image's corner and never examined the lungs; they failed at new hospitals). Netflix (the leaderboard could not see whether a member found something to watch).

**Source.** Chapter 1, "The slice" (Kant's move); Chapter 3, Data Validation (recording instrument, epistemic frame, Plato's Cave, MNAR; MNAR is not on the exam); Chapter 6 (selection bias).

---

## 5. Is the deterministic work done deterministically?

**The question.** Find every step in the case that has one right answer: arithmetic, counting, totals and percentages, sorting, dates, unit conversions, a random draw from a stated distribution, a database lookup. For each, ask: is it done by code that computes it (a script, a function, a calculator, a query), or is a language model being asked to produce the answer as text?

**Why it matters.** A chat model predicts text; it does not compute. It can give a confident, well-formatted sum that is wrong, a "random" list that is not random (it favours some answers, repeats patterns, and gives different results on different runs), or a statistic it never calculated. A script that computes the same thing gives the same answer every time, and anyone can run it again to check. The course's rule: keep deterministic checks deterministic. A fixed calculation does not become more trustworthy because a model decides whether to perform it.

**Exact terms.**
- **Deterministic versus probabilistic output:** in a deterministic system the output is a fact ("the function returned 42" is true or false, and can be checked); a model's output is a degree of belief, conditional on its training and assumptions.
- **Tool orchestration** (capacity 3): choosing which tool fits which sub-problem. Arithmetic and random draws go to code, not to the language model's text.
- **Delegate freely:** mechanical, well-defined procedures whose output you can check by inspection. Running a script is one; trusting a model's mental arithmetic is not.
- **Seeded simulation:** a random draw made by code with a fixed seed, so it comes out the same every time and can be re-run and checked.
- **Plausibility auditing:** the quick check that a computed number could even be right (a total larger than its parts, a share above 100%).

**What it looks like in a case.**
- Numbers in the AI's output with no sign of how they were computed: no code, no query, no tool call, no formula.
- "I randomly selected 50 records" or "a random sample shows" from a model that has no way to draw at random.
- A simulation, Monte Carlo estimate or p-value reported by a chat model, with no script and no seed.
- Totals and percentages that do not add up when you recompute them.
- The same question asked twice gives different numbers.

**Questions to ask.**
- Which steps here have one right answer? For each, what actually produced the number?
- Is there code, a query or a tool call that someone can re-run? Does it give the same result?
- If something is "random", what made it random, and from what distribution? Is there a seed?
- Do the numbers add up when you recompute them yourself?

**Evidence to ask for.**
- The script, query or tool call that produced each number, and its output.
- A re-run: the same code on the same input gives the same answer (for random draws, the same seed gives the same draw).
- A spot recomputation of two or three figures by hand or in a spreadsheet.

**Fix (an instruction you could give).** "Do not compute numbers in your reply. Write and run code for every calculation, count and random draw; use a fixed seed for any random draw; show the code and its output next to each number you report."

**In plain words (for the stakeholder).** "Some of these numbers were written by a language model rather than calculated. Until they are recomputed by a program that anyone can re-run, we do not know they are right."

**Job-search examples.**
- An AI assistant says "you applied to 47 jobs this month and heard back from 12%", but nothing counted the applications; the numbers are text it generated. A script reading the application log counts them.
- A job agent is asked to choose a random sample of postings for a market report. If the model chooses them in its reply, the sample is not random (it favours the first, the famous, the familiar). A script that draws the sample with a seed is.
- A salary report gives a median and a range for a role with no code behind it. Recompute from the listings with a script before trusting either.

**Source.** Chapter 0a, "When not to use an agent" ("Keep deterministic checks deterministic when you can"); Chapter 2 (deterministic versus probabilistic outputs); Chapter 1 (tool orchestration, plausibility auditing).

---

## 6. When it did not know, did it say "I don't know"?

**The rule.** Saying "I don't know" when you don't know is the right call. Making up a number when you don't know is not. This holds for the AI system and for you on the exam.

**The question.** Where in the case did the system lack the information it needed (no data, no source, no tool, a question outside what it was built for)? At those points, did it say so, or did it produce a confident answer anyway?

**Why it matters.** A made-up number looks exactly like a real one. Once it is in a report, people act on it, copy it and build on it, and nobody can tell it was invented. An honest "I don't know", or a flag that says what is missing, is useful information: it tells the reader where to look.

**Exact terms.**
- **Failure visibility:** when something cannot be done, say so with a flag instead of inventing a plausible substitute.
- **Epistemic uncertainty:** not knowing because of missing knowledge or data; more data or a check could reduce it. Name it and say what would reduce it.
- **Throat-clearing hedge:** a qualifier that names no specific gap ("results may vary", "further work is needed"). It sounds careful and carries no information; it is not the same as saying what you do not know.
- **Plausibility auditing:** the reader's defence when a number appears that the system could not have known.

**What it looks like in a case.**
- A precise figure for something the system had no data on: a salary for a role that did not exist until this year, a rate for a group it never saw.
- A name, date, source or contact filled in where the input had none.
- A "random" number or a statistic produced with no computation behind it (see item 5).
- An answer that should have been "not found" or "cannot tell from this data", given confidently instead.

**Questions to ask.**
- What did the system actually have to work with? Could it have known this?
- Where it could not know, did it say so? Did it say what was missing?
- Is any number, name or source in the output one it could only have invented?

**Evidence to ask for.** For each figure or fact: where it came from (the source, the query, the computation). Anything with no traceable source is treated as unknown until shown otherwise.

**Fix (an instruction you could give).** "If you do not have the data, a source or a tool for something, say 'I don't know' or 'not found', and say what is missing. Never fill a gap with an estimate unless I ask for one, and then label it as an estimate with its basis."

**In plain words (for the stakeholder).** "Some of these figures could not have been known from what the system had; they were made up. We should treat them as unknown and find the real numbers."

**Job-search examples.**
- An agent writing a cover letter cannot find the hiring manager's name. The right output is a flag ("name not found"), not an invented name.
- Asked for the salary range of a brand-new kind of role, an assistant gives a precise median. With no comparable postings, the honest answer is that it does not know, and which people or postings would tell you.
- Asked for a random number, a chatbot writes 17. It cannot draw at random; the honest answer is to run code, or to say it cannot.

**On the exam, the same rule applies to you.** If a case does not give you a number, do not make one up. Say what is missing and what check would supply it; that is often exactly the evidence request the case is looking for.

**Source.** Chapter 9 (failure visibility); Chapter 11, "Saying what you do not know" (epistemic uncertainty, throat-clearing hedge); Chapter 1 (plausibility auditing).

---

## 7. Who validated it? The source itself, or someone outside?

**On the exam.** Validation will be on the exam: what validation is, and why it has to be independent. Validation means checking the answer against something outside the thing that gave the answer, never by asking the same source again.

**The question.** Validation is a basic check. For every claim that something works or is true, ask: who says so? Is the only evidence the source's own word (the developer, the vendor, the agent, the model checking itself), or has someone outside the source checked it, on data or cases the source did not choose?

**Why it matters.** A source that validates itself chooses its own test, its own data and its own reading of the result, and it shares its own blind spots. Results often look good on the developer's data and much worse outside it. The failure only becomes visible when someone independent looks.

**Exact terms.**
- **External validation:** testing at an outside site, on its own cases, where the model was never developed or tuned.
- **Validation set:** held-out data from the training distribution. It is a real check, but it comes from the same place as the training data, so it is not external validation.
- **Validator independence:** a check counts only when it comes from outside the system being checked.
- **Circular verification:** checking a claim by asking the unverified source to confirm itself.
- **Independent review:** a reviewer outside the deployment team with authority to halt or revise.
- **Provenance tracking** and **authority laundering:** a record of where each piece of information first came from; without it, data handed on looks like a legitimate output and the receiver cannot check where it started.
- **Evidence ladder:** stronger verbs need stronger evidence. Only external validation (with subgroup analysis and documented distribution match) licenses "show"; internal evaluation alone licenses at most "find".

**What it looks like in a case.**
- Performance figures that come only from the vendor or the team that built the system.
- "Validated" with no word on who did it, where, or on what data.
- An agent confirming its own work, or a second model built the same way doing the confirming.
- A claim checked by asking the source again ("are you sure?", "are you really the recruiter?").
- Information passed between agents or reports with no record of where it first came from.

**Questions to ask.**
- Who produced the evidence that this works? Did they also build or sell it?
- Was it ever tested somewhere else, on cases the source did not pick?
- Did the outside test find the same result? If no outside test exists, what verb does the claim deserve?
- Where did each fact first come from, and can anyone trace it?

**Evidence to ask for.** An external validation: a test by someone independent, at another site or on another population, with the result reported in full, including subgroups. Failing that, the source's own test results with the data and method, so an outside party could repeat them.

**Fix (an instruction you could give).** "Report who validated each claim, where, and on what data. Mark any claim supported only by the developer's own testing as unvalidated. Before relying on it, arrange a test by someone independent on our own cases."

**In plain words (for the stakeholder).** "So far the only evidence this works comes from the people who built it. Until someone independent tests it on our own cases, we do not know how it will do here."

**Job-search examples.**
- A résumé-screening vendor reports high accuracy from its own test. External validation is your company running it on last year's applicants, whose outcomes you know.
- An agent screening candidates "confirms" a candidate's past job title by asking the candidate. That is circular. An outside check: the former employer, or a reference who worked there.
- A salary figure in a report came from another agent, which took it from an editable forum post. Without provenance tracking, nobody downstream can tell.

**Course cases.** The Epic Sepsis Model: deployed in hundreds of hospitals with developer-reported performance; an external validation at another hospital system found it missed most sepsis cases and that most of its alerts were false alarms. The COVID chest X-ray models: high accuracy on their own data; they failed at new hospitals.

**Source.** Chapter 11 (external validation, the Epic Sepsis Model, the evidence ladder); Chapter 12 (validator independence, independent review); Chapter 8 (circular verification, provenance tracking, authority laundering); Chapter 13 (validation set).

---

## 8. Has anyone tried to break it? (adversarial checks)

**The question.** A system that has only been tested on ordinary inputs has only been shown to work on ordinary inputs. To make sure something is robust, someone has to try to make it fail on purpose: reword the input, slip in something misleading, push it to the edge of what it was built for. Has anyone done that here? What did they find?

**Why it matters.** Testing should be organized around trying to find evidence that a system fails, not only evidence that it works. Ordinary tests say how a system does when nothing is pushing against it. Real users, real attackers and a changing world will push.

**Exact terms.**
- **Adversarial testing:** testing with inputs built to fool the model, to see what it relies on.
- **Adversarial example:** an input nudged on purpose so the answer flips while a person sees no real change.
- **Prompt injection:** instructions hidden in data the system reads, which it treats as commands.
- **Semantic invariance** and **prompt sensitivity:** the answer should stay the same when the input is reworded without changing its meaning; if prompts that mean the same thing get noticeably different answers, that is prompt sensitivity.
- **Distribution shift** and **natural adversarial input:** no attacker, but inputs unlike the training data, or rare cases it never learned.
- **Adaptive attack:** an attack built knowing the defense, so it is designed to get past it. A defense tested only against attacks that did not know about it is not tested.
- **Robustness profile:** what the system resists and what it does not, by attack, size of change and shift, not one number.
- **Residual risk disclosure:** a written list of known weaknesses that were not fixed.

**What it looks like in a case.**
- Only one accuracy number, measured on clean, ordinary test data, and a claim that the system is "robust".
- No test of reworded inputs, edge cases, hidden instructions, or inputs from a new setting.
- A defense said to work, tested only against attacks that did not know it was there.
- No list of what the system does not resist.

**Possible things to do to check robustness** (pick the ones that fit the case):
- Reword the same request several ways and compare the answers (semantic invariance).
- Feed it inputs with instructions hidden inside them and see whether it obeys (prompt injection).
- Make small, meaningless changes that should not matter and see whether the answer flips (adversarial examples).
- Try rare, unusual and boundary cases, and inputs from a new place or time (natural adversarial inputs, distribution shift).
- Attack the defense knowing how it works (adaptive attack).
- Write down the result as a robustness profile, and list what was not fixed (residual risk disclosure).

**Evidence to ask for.** The adversarial tests that were run, what each one tried, and what broke; a robustness profile, not a single accuracy figure; and the list of known weaknesses.

**Fix (an instruction you could give).** "Before calling this robust, test it against reworded inputs, hidden instructions in the data it reads, small meaningless changes, and rare or new cases. Report what each test found as a robustness profile, and list the weaknesses that remain."

**In plain words (for the stakeholder).** "It has only been tested on normal cases. Nobody has yet tried to make it fail, so we do not know what happens when someone, or something, pushes on it."

**Job-search examples.**
- A résumé screener scores the same résumé differently when "led a team of five" is rewritten as "managed five people". Rewording tests catch it.
- A job listing hides a line in white text telling an AI assistant to rank this posting first. A prompt-injection test catches it.
- A screener tuned on standard office résumés meets a career changer whose experience is all on farms. Testing unusual résumés catches it before a real applicant is turned away.

**Source.** Chapter 4, Robustness (adversarial testing, adversarial examples, prompt injection, semantic invariance, prompt sensitivity, adaptive attacks, robustness profile, residual risk disclosure); Chapter 1 (test to find failure, not only success).

---

## 9. Where could bias have entered? (the ten ways in)

**The question.** If the case reports a number about people (a rate, a score, an estimate, a prediction), ask where along the pipeline it could have been pushed off in one direction. Walk the ten ways in. Then ask which fix would actually reach the place where the bias entered.

**The formal definition.** Bias is a property of an *estimator*: any procedure that computes a quantity from data (a mean, a rate, a risk score, a prediction). If θ is the true value and θ̂ is your estimate:

**Bias(θ̂) = E[θ̂] − θ**

that is, how far the estimate sits from the truth *on average, over every dataset you might collect*. If it is zero, the estimator is **unbiased**: it can miss on any one dataset, but not systematically. If it is not zero, it is **biased**: systematically off in one direction.

**The consequence that matters most.** More data does not fix a biased estimator. More data narrows the scatter; it does not move the offset. You get the wrong answer with more confidence. (The 1936 *Literary Digest* poll: 2.4 million responses from a skewed frame predicted the wrong winner; a far smaller, better-drawn sample got it right.)

**The ten ways in** (the chapter's ten entry points; each is a different way of making E[θ̂] − θ nonzero):

| Type | Formal definition (how it enters) | Job-search example |
|---|---|---|
| **Selection bias** | Who ends up in the sample depends on what happened to them, so the sample average is off. The estimator computes the average among those kept, E[Y given in sample], when you wanted E[Y]; the two match only if being kept does not depend on the outcome. | A survey of a résumé tool's users reaches only those still subscribed; people who got no interviews quit early. |
| **Sampling bias** | Some groups are underrepresented because they were hard to reach, not because of their outcomes. | A job-market survey goes out only through one career website. |
| **Confirmation bias** | The researcher's prior steers what data is collected, kept and reported. | A developer sure her matching agent works counts its good matches and sets the bad ones aside as "odd listings". |
| **Observer bias** | A labeler's prior leaks into the label, so labels track what the labeler already believed. | A recruiter rating interview notes can see each candidate's school and rates famous-school notes higher. |
| **Data-coding bias** | Systematic miscoding when judgment is needed to fit material into categories; the category, not the coder, is unclear. | Taggers disagree mostly on whether a listing is "remote friendly". |
| **Publication bias** | Significant results get published and null results stay in drawers, so the literature looks stronger than it is. | Studies of AI résumé tools get published when callbacks rose; the ones that found nothing do not. |
| **Self-report bias** | People misreport themselves in a consistent direction. | Applicants rate their own spreadsheet skills; most round up. |
| **Data-entry bias** | Patterned transcription error: not random slips, but errors that lean one way. | An agent filling in forms keeps picking the job title nearest the top of a long dropdown. |
| **Historical bias** | A faithful, representative record of a world you did not want to reproduce; its accuracy is the harm. | A model learns from a firm's accurate callback records, which rarely called people with gaps in their résumés. |
| **Implicit bias** | The unconscious associations of the people in the pipeline; the medium the other biases swim in. | A hiring manager warms to candidates who share her background without noticing. |

**Three flavors** (which part of the pipeline the bias lives in, and so which fix reaches it):
- **Dataset bias:** the training sample does not represent the people it will be used on. Comes from selection, sampling and some data-entry bias. *Fix the sample.*
- **Label bias:** the labels record a biased process, so the model predicts a distorted stand-in (a **biased measurement**, such as re-arrest recorded for crime). Comes from observer, data-coding, historical and some self-report bias. *Fix what is measured.*
- **Structural bias:** good data, accurate labels, a correct model, and still unfair outcomes, because of the world it is deployed into. Fed by implicit, confirmation and publication bias. *No model or data fix reaches it; the fix is in how the system is used.*

**The bias trade-offs.** Every fix costs something:
- **Correcting selection** with **inverse probability weighting** (weight each kept case by 1 over its chance of being kept) buys back an unbiased estimate, but only if the thing that drove selection was recorded. If it was not, no weight recovers it; the fix is collecting different data.
- **The five that enter through people** (confirmation, observer, data-coding, publication, self-report) are not fixed by touching the model. The fixes are process: decide the hypothesis before seeing outcomes, blind the labelers, pay someone to find the case that disconfirms. You spend time and process to buy back an unbiased record.
- **Fairness:** when groups have different base rates, a model cannot be calibrated, equal in false positives and equal in false negatives all at once (the impossibility theorem). Choosing a fairness metric is choosing which error you accept (a **values claim**).

**Diagnostics to ask for.** Cohen's kappa when two people label the same items (low when unblinded points to observer bias; low on particular items points to data-coding bias); a funnel plot for publication bias; an outside record (payroll, transcripts) to check self-reports; consistency checks against source documents for data entry; who was dropped and why, for selection.

**Fix (an instruction you could give).** "For this estimate, list where bias could have entered, using the ten types, and say which flavor each is (dataset, label or structural). For each, propose the fix that reaches the place it entered, and say what that fix costs."

**In plain words (for the stakeholder).** "This number could be off in one direction, and collecting more of the same data will not correct it. We need to find where the skew came in and fix it there."

**Source.** Chapter 6, Bias: Where It Enters and Who Is Responsible ("What 'bias' actually means"; "Ten mechanisms, distinguished"; "Three flavors of bias"); Chapter 7 for the fairness impossibility.

---

## Also expect on the multiple-answer questions: skepticism, which is about evidence

Skepticism itself is likely to come up in the multiple-answer questions. The one idea to hold on to: **we look at things based on evidence.** Skepticism is not distrust and not doubt for its own sake. It is checking how a belief was formed and whether the evidence behind it still holds.

**The idea.** In this course, skepticism is a method, not a mood: a set of moves you perform on a claim, each of which leaves something another person can inspect. It is not the rejection of evidence, and not a refusal to believe anything. It is the discipline of knowing how you formed a belief, so you notice when the conditions that made it reliable have changed. The main enemy of skepticism is not laziness but confidence: the moves matter most when the output looks right.

**The moves** (each named after a philosopher; see "Terms named after people" above):
- **Cartesian doubt:** list what would have to be true for the claim to be wrong.
- **Hume's induction problem:** past success is no guarantee; ask what has changed since the evidence was collected.
- **Popperian falsifiability:** a claim must say what result would show it false.
- **Kantian slice:** any check sees only part of the world; name what it could not see.

**Statements of the kind to judge.** Practice statements written for this checklist, not exam items.
- "Skepticism is the discipline of knowing how you formed a belief." **True.**
- "A skeptic doubts every claim equally, including claims backed by strong evidence." **False.** Strong evidence earns belief; the chapter's example is the chair that will hold your weight.
- "The main enemy of skepticism is confidence." **True.**
- "A claim that no result could contradict is strong evidence that the system works." **False.** That is a rhetorical claim; it can never fail, so it tells you nothing.

**Job-search example.** A recruiter says an AI screener "has always picked good people". A skeptic does not just disagree. She asks what evidence that rests on, whether it was ever tested against the people the screener turned away, and what has changed in the applicant pool since it was checked.

**Source.** Chapter 1, "What I mean by skepticism".

---

## Also expect on the multiple-answer questions: falsifiability

**The idea, in one line.** If it is not possible for a test to be wrong, it is not a test.

**What it means.** A real claim says in advance what result would show it false: the measure, the threshold and the time window. "The system is robust" fits every possible outcome, so it can never fail, and a claim that can never fail tells you nothing. "Error below two percent on out-of-distribution inputs, over a thirty-day window" can fail, so passing it means something.

**Exact terms.**
- **Popperian falsifiability** (Popper): a claim must name the metric, threshold and window that would show it false.
- **Rhetorical claim:** a claim that describes things in words ("robust", "performs well", "stands out") with no specific test, number or condition that could make it right or wrong. No observation could contradict it.
- **The swans:** a thousand white swans do not prove all swans are white; one black swan proves they are not. Agreeing cases never prove a claim; one clear failure can refute it.

**Statements of the kind to judge.** Practice statements written for this checklist, not exam items.
- "'The system is robust' is a falsifiable claim." **False.** No result could contradict it.
- "Falsifiability is about whether a claim could be shown wrong, not whether it is wrong." **True.**
- "A test that every possible result would pass still tells you something useful." **False.** If it cannot fail, it is not a test.
- "'Precision of at least 0.91 on the held-out set, checked monthly' could be shown false." **True.**

**Job-search example.** A résumé service promises to make your résumé "stand out". No number of callbacks could show that false, so it is a rhetorical claim. A falsifiable version: "at least twice as many callbacks as your old résumé, over the next fifty applications."

**On a case.** Ask of the main claim: what result would have shown it false? If the answer is "none", say so with the exact term, and rewrite it with a measure, a threshold and a window.

**Source.** Chapter 1, "What I mean by skepticism" (Popper's move; the swans).

---

## Also expect on the multiple-answer questions: plausibility auditing

**The idea.** Before you check any source, ask: could this even be true, given what I know of the world? Some AI outputs are wrong in a way you can see at a glance: a percentage above 100, a person with more years of experience than years alive, a task done faster than any human could. Plausibility auditing is noticing that, and saying so, before the confident wording talks you out of it.

**Exact term.** **Plausibility auditing** (the first of the five supervisory capacities): asking whether an output is even the kind of thing that could be true, given what you know. It gives you the twitch that something is wrong; finding exactly what is wrong still takes evidence.

**Statements of the kind to judge.** Practice statements written for this checklist, not exam items. An AI résumé summary says a 22-year-old applicant "has 30 years of experience leading global teams".
- "Without checking anything, you can tell this summary contains an error." **True.** Thirty years of experience is impossible at twenty-two.
- "The summary is detailed and confident, so the experience figure is probably right." **False.** Detail and confidence are form, not evidence.
- "Once you see the impossible figure, you know exactly what the correct figure is." **False.** You know something is wrong; you still have to find out what.

**On a case.** Read every number in the AI's output and ask whether it could happen at all: shares above 100%, totals that do not add up, amounts far outside any normal range, impossible speeds. A case's planted flaw is sometimes exactly that, in plain sight.

**Source.** Chapter 1, "The Five Supervisory Capacities".

---

## Also expect on the multiple-answer questions: probability, likelihood and log probability

Expect a simple chance setup (coins, dice or cards) with statements about three ideas. The exam is on paper, so nothing needs a calculator: fractions and one rule about logs.

- **Probability of independent events:** when one outcome does not affect the other, multiply. Two fair coin flips both heads: 1/2 × 1/2 = 1/4.
- **Likelihood:** the chance of the evidence *if* a hypothesis is true. For "the coin is fair", the likelihood of three heads is 1/8. It is not the chance that the coin is fair; that is the **posterior**, which also needs the prior (Bayes' theorem). Likelihood and posterior are a look-alike pair.
- **Log probability** (the "logprob" a language model reports for each word): the logarithm of a probability. Because probabilities are at most 1, log probabilities are at most 0; a certain event has log probability 0, and the closer to 0, the more likely. For independent events the log probabilities **add**, because the log of a product is the sum of the logs. That is why models add log probabilities instead of multiplying many tiny numbers.

**Statements of the kind to judge.** Practice statements written for this checklist, not exam items. A coin is flipped three times and lands heads every time.
- "If the coin is fair, the chance of three heads is 1/8." **True.**
- "A likelihood of 1/8 for 'the coin is fair' means the coin is fair with probability 1/8." **False.** That would be the posterior.
- "The log probability of the three flips is three times the log probability of one head." **True.** Three equal logs added.
- "A log probability can be a large positive number for a very likely event." **False.** It is at most 0.

**Source.** Chapter 2 (the multiplication rule, independence, Bayes' theorem: prior, likelihood, posterior); the course term glossary (token probability or logprob, log loss).

---

## Also expect on the multiple-answer questions: the fluency trap

The fluency trap is likely to come up in the multiple-answer questions, so know it well enough to judge true-or-false statements about it. It also shows up in cases: an AI output that reads beautifully is the most common disguise for a flaw.

**The idea, in two moves.** First, the more fluently an AI presents its output, the more confident you become in the output. Second, and this is the trap, the more confident you become in the output, the more confident you become in *your own evaluation* of it. Fluency boosts wrong evaluations as readily as right ones.

**Exact terms.**
- **Fluency trap:** fluent output raises confidence in the answer, then in your own evaluation of it. Smooth, well-formed output gets taken as evidence it does not carry.
- **Form versus content:** how well an output reads and whether it is true are independent in AI output.
- **Fluent versus correct:** fluent means it reads smoothly; correct means it matches the world.
- **Prediction-lock:** write your prediction before seeing the result and never revise it; append what you observed. It interrupts the trap because your criteria were fixed before the fluent output could move them.
- **Fluency-trap detector:** treat a strong verb in AI output ("demonstrates", "proves", "clearly shows") as a flag, then ask what evidence stands behind it.
- **Verb downgrade:** swap in the weaker verb the evidence supports; the facts stay, the posture drops.

**Statements of the kind to judge.** These are practice statements written for this checklist, not exam items.
- "Fluency boosts wrong evaluations as readily as right ones." **True.**
- "A smooth answer shows that the model understood the question." **False.** Smooth wording is form; understanding is not shown by it.
- "An explanation that is accurate about the model can still mislead about the world." **True.** That is the fluency trap in explanations (Chapter 5).
- "A verb downgrade changes the facts in a sentence so that they match the evidence." **False.** The facts stay; only the verb's strength drops.
- "With a prediction-lock you may revise your prediction after seeing the result, as long as you note why." **False.** The prediction is never revised; what you observed is added below it.

**Job-search example.** An AI writes a smooth, confident cover letter. Because it reads well, the job seeker feels it has been checked and sends it, without noticing it claims a skill she does not have.

**Source.** Chapter 1, "The fluency trap"; Chapter 5 (fluency trap in explanations); Chapter 11 (fluency-trap detector, verb downgrade).

---

## To add next

Professor Bear has already named one way to read a case, while reviewing the Delegation and Trust film (2026-11-12). It is listed here so it is not lost; it has not been written up as items yet:

- Is there a contract? Should there be one? If so, what is it, and is it appropriate?
- Are the steps appropriate?
- Who is evaluating, and is that appropriate?

(The checks question from the same list is now item 2.)
