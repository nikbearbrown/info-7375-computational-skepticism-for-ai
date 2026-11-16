# SOURCE — the solve-verify asymmetry (Chapter 1)

**What this is.** The verbatim source for this film: the section "The solve-verify asymmetry" of `info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md` (Chapter 1, "The Skeptic's Toolkit", lines 132–148 as of 2026-09-27), copied read-only. The chapter file carries Bear's uncommitted edits and was not modified or staged. Bear's order (2026-09-27, in `../SHOW-TELL-SOLVE-VERIFY.md`): "Look at the most recent updates to the show tell skill to make sure you have the most recent instructions for that. Show tell film on the solve-verify asymmetry." **Why.** Every narration line and FACTCHECK row traces to this section; the film adds no figure, case or claim the section does not contain. **Found.** The section's arc is the film's spine: the folklore (factoring is hard, multiplying back is easy; cryptography rests on it) → in AI deployment the asymmetry inverts (producing the output is cheap: milliseconds, fractions of a cent; verifying it is expensive: a clinician with twenty minutes, or a query against the provider's servers; an hour of senior labor) → not a complaint, an observation about where the costs sit → if you don't budget for verification you don't get it, and every unverified output looks like a success until one is the patient, the loan, the warrant or the undeleted email → the wrong fix is to automate verification (another model, one layer up) → the right fix is to design the system so the verification a human can perform tells you what you need to know. Its Figure 1.5 caption says the boxes "compare kinds of work, not measured costs", which is why the film's bars are labelled illustrative and carry no values. "Ash's agent's report" is the chapter's running case (an agent that reported an email deleted); the film says "an agent's report that an email was deleted" and never introduces Ash.

---

## Chapter 1, "The solve-verify asymmetry" (verbatim, lines 132–148)

## The solve-verify asymmetry

There is a piece of folklore in computer science that says verifying a solution is easier than producing one. If I give you a very large number, it is hard to factor it. If I hand you the factors, it is easy to multiply them and check. Most of cryptography is built on this asymmetry. It is real and it is beautiful and you should know about it.

Here is the joke. The asymmetry inverts in AI deployment. It runs the other way.

When an AI system produces an output, *producing* the output is cheap. The model runs, the result appears, the latency is in milliseconds, the cost is fractions of a cent. *Verifying* the output is expensive. To verify the triage score, you need a clinician with twenty minutes and a stethoscope and a body of training the model does not have. To verify Ash's agent's report, you need to query the provider's servers, examine the actual data state, and compare it to what the agent claimed. The output cost a fraction of a cent. The verification costs an hour of senior labor.

This is not a complaint. It is an observation about where the costs sit, and where the costs are going to sit for the foreseeable future.

If you do not budget for verification, you will not get verification. The system will produce outputs at scale. Verification will not happen at scale. The unverified outputs will look like successes — every one of them — until one of them is the patient, or the loan, or the warrant, or the email that did not actually get deleted.

Most of this book is about how to verify cheaply enough that verification scales. The answer is *never* "automate the verification" — because that is just another model, with the same problem, sitting one layer up. The answer is always: design the system so that the verification a human can perform tells you what you need to know.

![Two comparisons contrast searching for integer factors and multiplying them to check, with generating an AI completion report and inspecting actual state to verify it.](../images/01-the-skeptics-toolkit-fig-05.png)

*Figure 1.5 — Where does the verification work live? A mathematical witness can have a direct mechanical check. A deployment claim may require independent access, domain context, and examination of consequences. The boxes compare kinds of work, not measured costs, runtimes, or a universal ordering of difficulty.*
