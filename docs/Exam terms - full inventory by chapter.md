# Exam terms: the full inventory by chapter

Every term each chapter names, in the order of first appearance, with the book's sentence, a plain definition, an example and a look-alike. 1193 entries. Quotes are verbatim from the chapter's first merge side; the old name for Chapter 9's assessment is shown as "work split".

## Chapter 1, The Skeptic's Toolkit (95 terms)

**Netflix Prize**  *(also: Netflix contest; the contest)*
*line 7 · named result or case*

> In October 2006, Netflix offered a million dollars to anyone who could beat its own movie recommender by ten percent. "Beat" had a precise meaning.

In plain words: A contest in which Netflix paid a million dollars to whoever could predict customers' star ratings ten percent better than its own recommender. The contest delivered the improvement it asked for, but by then the number no longer measured what Netflix needed to know, and the winning system was never deployed.

Example: Two coalitions tied on the hidden test data, and the prize went to the team that had submitted first, about twenty minutes earlier.

**Amazon recruiting engine**  *(also: Amazon recruiting tool; the recruiting tool)*
*line 13 · named result or case*

> Between 2014 and 2017, Amazon built an experimental system to rate job candidates from one to five stars, the way shoppers rate products. Its models learned from patterns in the résumés submitted to the company over a decade — most of them from men, reflecting the tech industry's male dominance.

In plain words: An experimental Amazon system that scored job candidates from one to five stars after learning from a decade of submitted résumés, most of them from men. It was disbanded by the start of 2017, and almost everything known about it comes from one Reuters report with anonymous sources.

Example: The system penalized résumés containing the word "women's," as in "women's chess club captain."

**held-out test set**  *(also: hidden test data; hidden test set; held-out dataset)*
*line 7 · concept*

> Predict, more accurately than Netflix's system did, the star rating a customer would give a movie, and be scored by how far your predictions landed from ratings you had never seen.

In plain words: Data kept back from the people building the model and used only to score it, so the score reflects cases the model never saw. The Netflix contest scored teams on hidden ratings they had never seen.

Example: Two coalitions of researchers tied on the hidden test data.

**audit a measure you cannot see**
*line 15 · concept*

> We do not know. You cannot audit a measure you cannot see, and that is a lesson of its own.

In plain words: You cannot check whether a measure is the right one if you are not told what it is. The Amazon reporting never says what the models were trained to predict, so the measure cannot be audited.

Example: The report does not say whether the models were trained to predict being hired, advanced, or rated highly by a recruiter.

**the data taught the wrong thing**  *(also: a record of who had applied, not of who could do the job)*
*line 17 · failure mode*

> In the other, a system learned what its training data taught it, and what the data taught was the wrong thing.

In plain words: A model learns exactly the patterns in its training data, and when the data record the wrong thing, the learned patterns are real but point at the wrong target. Amazon's résumé data recorded who had applied, not who could do the job.

Example: Amazon's model gave little weight to skills nearly every technical applicant shared, such as writing code, because a model built to tell résumés apart rewards whatever differs between them.

**the easy thing**  *(also: stand-in; convenient stand-in; something nearby that is easy)*
*line 44 · concept*

> The thing we care about is usually hard to observe, so we measure something nearby that is easy. Rating error is easy to compute; whether a member is glad they stayed is not. Resemblance to past résumés is easy to compute; ability to do a job is not.

In plain words: The nearby, easy-to-compute number a team measures because the thing it really cares about is hard to observe. It usually tracks the real thing, which is why it was chosen, so the system validates beautifully on it and every metric says success.

Example: Netflix measured rating error because whether a member is glad they stayed is hard to observe; Amazon measured resemblance to past résumés because ability to do a job is hard to observe.

**measure and want**  *(also: what you measure and what you care about; the gap; (MEASURE AND WANT))*
*line 21 · concept*

> The system measured one thing. Everyone cared about another. The output was valid on the first and wrong about the second, and nothing on the dashboard could tell the difference.

In plain words: The recurring gap this book studies: a system is built around one measurable thing while people actually care about something else. The output can be valid on the measure and wrong about the want, and nothing on the dashboard shows the difference.

Example: Netflix measured error in predicting star ratings, but cared whether a member finds something to watch tonight and keeps paying next month.

**composite applicant**  *(also: the illustration)*
*line 23 · named result or case*

> Aggregate lessons are hard to feel, so for the rest of this chapter, hold one person in mind. She is a composite — not a real applicant, but the kind of case a measure like that is made of.

In plain words: An imagined software engineer, not a real applicant, whom the chapter uses to show what one wrong score looks like from the inside. The reporting does not say the tool rejected anyone; she is what leaning on such a ranking would cost.

Example: A software engineer with five years of shipping code who captained her university's women's chess club sinks toward the bottom of the stack, and nobody learns the stack was wrong.

**four moves**  *(also: four skeptical moves; the skeptic's toolkit; the toolkit)*
*line 263 · framework*

> I have given you four moves: Cartesian doubt, the Humean limit on induction, Popperian falsifiability, and the Kantian slice move.

In plain words: The four checks the book gives you to run on any claim or AI output. Descartes asks what would have to be true for it to be wrong, Hume reminds you a past pattern guarantees nothing, Popper asks what observation would show it wrong, and Kant asks what the artifact is, what the world is, and how they relate.

Example: Each move leaves something behind in a review: an assumption list, a context-shift check, and a test with a failure condition (the fourth, Kant's slice, follows in the text).

**Five Supervisory Capacities**  *(also: five supervisory capacities; five capacities; supervisory capacities)*
*line 175 · framework*

> Not personality traits. Not vibes. Capacities — things the supervisor can do that the system cannot do for itself.

In plain words: The five things a human supervisor can do that an AI system cannot do for itself: plausibility auditing, problem formulation, tool orchestration, interpretive judgment, and executive integration. They are what catch the failures metrics cannot see.

Example: The Netflix contest scored rating error while the need was a member who finds something to watch and stays: the capacity missing was problem formulation.

**Goodhart's law**  *(also: when a measure becomes a target, it ceases to be a good measure)*
*line 46 · concept*

> There is a name for what happens when you lean on the easy thing. Goodhart's law, in the phrasing everyone quotes: when a measure becomes a target, it ceases to be a good measure (Goodhart, 1975; Strathern, 1997). The Netflix contest was that sentence with a million-dollar prize attached.

In plain words: When people aim at a number as the goal, the number stops being a reliable sign of the thing it was meant to stand for.

Example: The Netflix contest paid a million dollars to improve one rating-error number, and by the time it was won that number was no longer the thing Netflix needed to know.

**the gap was there from the start**  *(also: design-time stand-in)*
*line 48 · failure mode*

> The gap was there from the start. Somebody picked a convenient stand-in at design time, and the stand-in was never the target. Amazon's is this kind: resemblance to past résumés was never ability.

In plain words: One way a measure and a want come apart: someone picked a convenient stand-in at design time, and it was never the real target. You can catch it before deployment by asking what the number is a number of.

Example: Amazon's resemblance to past résumés was never the same as ability to do the job.

Not to be confused with: the gap opens later

**what is this number a number of?**
*line 48 · method*

> You can catch this before deployment, by asking the question this chapter keeps asking: what is this number a number of?

In plain words: The question the chapter keeps asking to expose a stand-in measure: what real thing does this number actually measure? A precise-looking number does not answer it by being precise.

Example: Rating error is a number of how close predictions land to star ratings, not of whether a member is glad they stayed.

**the gap opens later**
*line 50 · failure mode*

> The gap opens later. The measure tracked the want, and then something changed — the world moved, or pressure was applied to the measure itself. Netflix's is this kind.

In plain words: The other way a measure and a want come apart: the measure tracked the want at first, then the world moved or pressure was applied to the measure itself. You cannot catch it at design time, only by checking again and again.

Example: In the DVD years a good star-rating prediction roughly meant a good disc in the mailbox; then streaming arrived and the contest kept polishing the same number for most of three more years.

Not to be confused with: the gap was there from the start

**the supervisor**  *(also: the person supervising; the human supervising the model)*
*line 52 · concept*

> Neither check belongs to the model. Both belong to the person supervising it. The rest of this chapter is about how that person does the checking.

In plain words: The human who owns the checking: asking what a measure stands for and checking it again over time. The model has no way to detect when the world stops matching its expectations, so only the human can do it, and only if they remember the check is necessary.

Example: A technical recruiter handed a ranked list where strong engineers keep landing near the bottom is the supervisor noticing something is off.

**skepticism**  *(also: skeptical method)*
*line 60 · concept*

> I mean a method. Skepticism in this book is a set of moves you can perform on a claim, and the moves can be taught, and you can see whether someone did them.

In plain words: A set of moves you perform on a claim, not a mood: not eye-rolling or cynicism, but a method that can be taught and whose use can be seen. It is also the discipline of knowing how you formed a belief so you notice when the conditions that made it reliable have changed.

Example: The recruiter who asks what would have to be true for this score to be wrong is performing a move; the one who trusts it because it agreed with her last eight hundred judgments is performing none.

Not to be confused with: cynicism, or the disposition of being against everything

**failure of method**
*line 64 · failure mode*

> When the conditions change and you do not notice — when the model's confidence carries forward unchanged into a world the model has never seen — that is not just a technical failure. That is a failure of method.

In plain words: Not noticing that the conditions that made a belief reliable have changed, so the model's confidence carries forward unchanged into a world it has never seen. The chapter says this is not just a technical failure; it is a failure of method.

Example: Zillow's model kept issuing confident valuations after the post-pandemic market stopped behaving like its training data.

Not to be confused with: technical failure

**confidence as skepticism's primary enemy**  *(also: when the output looks right)*
*line 66 · failure mode*

> The difficulty is in performing them when the output looks right. When it is fluent, when it is specific, when it arrives in a format that pattern-matches to "trustworthy answer" — that is when the moves matter most, and that is exactly when the instinct to perform them is weakest.

In plain words: Running the skeptical moves is easy when something looks suspicious and hard when the output looks right, fluent and specific. The chapter says skepticism's main enemy is confidence, not laziness.

Example: An output that arrives in a format that pattern-matches to "trustworthy answer."

**fluency**  *(also: fluent output; polish)*
*line 141 · concept*

> Fluency is a signal that the system has produced an output the prior distribution liked. It is not a signal that the system has gotten the world right. I will repeat that sentence in some form in almost every chapter of this book, because it is the single thing engineers most need to internalize and most resist internalizing.

In plain words: How smooth, specific and well-formed an output sounds. It shows only that the system produced something its prior distribution liked, not that it got the world right, so it is not evidence of truth.

Example: A leaderboard ranked to the fourth decimal place, or a recruiting tool returning a clean one-to-five stars, looks finished the way a well-formed paragraph does.

Not to be confused with: being correct (a fluent output can be maximally wrong)

**Cartesian doubt**  *(also: radical doubt; Descartes's move; the Cartesian move)*
*line 70 · method*

> I am teaching you the move, which is this: doubt the claim until you can list the conditions under which it would be wrong. The list is the product.

In plain words: Doubt a claim until you can list the specific conditions under which it would be wrong; the list is the useful result. The conditions are checkable engineering questions about the training data, the input features and the deployment context.

Example: For a low résumé score: the training résumés might underrepresent people like her, the input features might miss the signal that matters, or the tool might be used differently from how it was tested.

Not to be confused with: Popperian falsifiability (Descartes gives the suspects, Popper the test)

**checklist of conditions**  *(also: inspection protocol; list of conditions you can check; case coverage, input completeness, and deployment context)*
*line 72 · method*

> What makes the Cartesian move powerful is that it produces a checklist. When you ask "what would have to be true for this to be wrong?", the answers are checkable.

In plain words: What Cartesian doubt produces: a list of conditions you can actually check, which turns philosophical doubt into a practical inspection. The three checks are whether the training data covered cases like this one, whether the input features include the relevant signal, and whether the deployment context matches validation.

Example: The training data either underrepresented cases like this one or it did not; the input features either include the relevant signal or they do not.

**Knight Capital**  *(also: Power Peg)*
*line 74 · named result or case*

> On August 1, 2012, Knight Capital deployed new trading software to eight servers. Seven took the update; one did not. On that eighth server, a reused flag bit reactivated "Power Peg," dead code from 2003 that had been disabled but never removed.

In plain words: A 2012 trading failure in which new software reached seven of eight servers and, on the eighth, an old reused flag reactivated dead code that fired millions of unwanted orders. The deployment counted as a success while the running system did something nobody intended.

Example: In roughly forty-five minutes the system executed over four million trades across 154 stocks and lost more than $460 million.

**success claim**  *(also: "deployment succeeded"; "The command returned success")*
*line 74 · concept*

> "The command returned success" and "the system is doing what we intend" are different claims. Radical doubt is the habit of never letting the first stand in for the second.

In plain words: A report that something worked, such as "deployment succeeded," is a different claim from the system actually doing what you intend. Radical doubt means never letting the first stand in for the second.

Example: Knight Capital's deployment succeeded while one un-updated server ran dead code, and the 97 warning emails went unread.

Not to be confused with: "the system is doing what we intend"

**a passed check supports only what it examined**  *(also: A passed check on the measure supports only the measure)*
*line 78 · concept*

> The useful output of doubt is a list of conditions you can check, not a general feeling of distrust. A passed check supports only what that check examined.

In plain words: A check that comes back clean tells you only about the thing it looked at, not that the whole system is fine. The useful output of doubt is a list of conditions you can check, not a general feeling of distrust.

Example: A clean check on Netflix's rating error supports only the rating error, not whether members found something to watch.

**Humean limit of induction**  *(also: Hume's move; Humean induction limits; the limit of induction)*
*line 80 · method*

> The model has been right thousands of times. Each one of those correct predictions adds zero logical guarantee that the next prediction will be right.

In plain words: However many times a model has been right, that adds no logical guarantee the next prediction will be. Induction works in practice only because the world is stable, and that help is invisible until it stops working.

Example: When the pattern stops holding, the model is exactly as confident as it was the day before, and the confidence is now a lie.

**turkey problem**  *(also: Taleb's turkey; a turkey with a spreadsheet)*
*line 82 · named result or case*

> A turkey is fed every morning for a thousand days. Each morning of feeding increases the turkey's confidence that tomorrow will also involve feeding. By day one thousand, the turkey's model of the world assigns very high probability to a meal on day one thousand and one.

In plain words: A story of a turkey fed every morning whose confidence grows with each feeding, right up to the day the farmer arrives with an axe. It had good evidence but knew only the correlation, not the mechanism, so it could not see the change coming.

Example: Google Flu Trends and Zillow Offers are each described as a turkey with a spreadsheet.

**correlation versus mechanism**  *(also: patterns and mechanisms)*
*line 90 · concept*

> A model trained on the past is doing exactly what the turkey did. It has learned the correlations in its training data. It has not learned the mechanisms underneath them.

In plain words: A model learns which things go together in its training data (correlations) but not the causes behind them (mechanisms), so when the mechanism changes it cannot notice. Patterns and mechanisms are not the same thing.

Example: Amazon's models learned a real pattern of who had applied, not of who could do the work.

**distribution shift**  *(also: potential distribution shift; stationary past shipped into a moving present)*
*line 92 · failure mode*

> This is not a barnyard parable dressed up for engineers; it is the failure mode of any system trained on a stationary past and shipped into a moving present.

In plain words: The world the model is used in has moved away from the data it was trained on, so learned patterns stop holding while the model's confidence stays the same. The chapter's checklist asks whether these cases are in the training data, whether the input features are complete, and whether the deployment context has changed since validation.

Example: Zillow's pricing model, tuned on years of earlier housing data, kept issuing confident valuations after the post-pandemic market changed.

**Zillow Offers**
*line 92 · named result or case*

> Zillow's home-buying arm, Zillow Offers, priced houses with an algorithm tuned on years of cooperative housing data. It worked — until the post-pandemic market stopped behaving like its training distribution. The model kept issuing confident valuations while the ground moved beneath them.

In plain words: Zillow's home-buying program priced houses with an algorithm tuned on years of cooperative housing data, and when the post-pandemic market stopped behaving like that data, the model kept issuing confident valuations. Zillow announced it was winding the program down in November 2021.

Example: A $304.4 million inventory write-down in one quarter, a further $240 to $265 million in expected charges, and about a quarter of staff cut.

**Google Flu Trends**
*line 92 · named result or case*

> The same shape appears in Google Flu Trends, which inferred flu prevalence from search queries and for a while beat the CDC's own reporting speed — until it didn't. From August 2011 it ran too high for 100 of the next 108 weeks.

In plain words: A system that inferred flu prevalence from search queries and for a while beat the CDC's own reporting speed, then stopped working. The chapter uses it as a case of a large correlation that held for a while and then did not.

Example: From August 2011 it ran too high for 100 of the next 108 weeks.

**big-data hubris**
*line 92 · failure mode*

> The authors named the disease precisely: big-data hubris — the assumption that a large correlation, having held so far, will keep holding (Lazer, Kennedy, King & Vespignani, "The Parable of Google Flu: Traps in Big Data Analysis," Science, 2014). Neither system was stupid. Each was a turkey with a spreadsheet.

In plain words: Assuming that because a large correlation has held so far, it will keep holding. The chapter's example is Google Flu Trends, and it says neither it nor Zillow was stupid, each was a turkey with a spreadsheet.

Example: Google Flu Trends beat the CDC's reporting speed for a while, then ran too high for 100 of 108 weeks.

**model confidence is a property of the model, not the world**  *(also: the model's confidence is a property of the model and not a property of the world)*
*line 94 · concept*

> Hume's move is to remember, every time, that the model's confidence is a property of the model and not a property of the world.

In plain words: How sure the model sounds describes the model, not reality: the world is under no obligation to match the model's expectations, and the model has no mechanism to notice when it does not. Only the human supervising the model can check, and only if they remember the check is necessary.

Example: By day one thousand the turkey's model assigns very high probability to a meal, and on day one thousand and one the farmer arrives with an axe.

**falsifiability**  *(also: Popper's move; Popperian falsifiability; the Popperian move)*
*line 98 · method*

> If you cannot specify the conditions under which the claim would be falsified, then the claim is not engineering. It is rhetoric.

In plain words: A claim counts only if you can say what observation would show it wrong, by naming a metric, a threshold and a window. A claim that cannot be wrong is rhetoric, not engineering.

Example: "The model performs well in production" becomes "Precision ≥ 0.91 and recall ≥ 0.88 on the held-out test set, evaluated monthly against a refreshed sample."

Not to be confused with: Cartesian doubt

**Cartesian doubt versus Popperian falsifiability**  *(also: suspects and line-up)*
*line 100 · concept*

> Popper asks what observation would show that it is wrong, and the product is a test: a metric, a threshold, a window, a failure you could actually see. Descartes hands you the suspects. Popper makes you stand them in a line-up and say what each would have to do to be picked out.

In plain words: Descartes asks what could be wrong and produces a list of conditions; Popper asks what observation would show it is wrong and produces a test with a metric, threshold and window. In the chapter's image, Descartes hands you the suspects and Popper makes you stand them in a line-up.

Example: Descartes: the training data may underrepresent people like her. Popper: a wrong answer would give a low rating to an applicant whose résumé shows the skills the job requires.

**asymmetry of confirming and falsifying**  *(also: Popper's asymmetry)*
*line 102 · concept*

> This asymmetry runs in only one direction: confirming instances pile up without providing certainty, but a single falsifying instance provides certainty in the other direction. You can't prove a model works in all cases. You can prove it fails in this one.

In plain words: Confirming cases pile up without ever proving a general claim, but a single falsifying case disproves it. So you cannot prove a model works in all cases, but you can prove it fails in one.

Example: Every white swan you count raises your confidence that all swans are white, yet no number of white swans proves it.

**black swan**
*line 102 · concept*

> Every white swan you count increases your confidence that all swans are white, but no finite number of white swans proves it — one black swan destroys it.

In plain words: A single case that contradicts a general claim; no pile of confirming cases can prove the claim, but one such case destroys it. Testing an AI system should go looking for such cases rather than collecting successes.

Example: Someone at Amazon went looking for the black swan and found by 2015 that the tool was not rating technical candidates in a gender-neutral way.

Not to be confused with: white swan (a confirming case, which raises confidence but never proves the claim)

**probing failure conditions**  *(also: trying to find evidence that it fails; aggressively probing failure conditions)*
*line 104 · method*

> The project of testing a deployed AI system should not be organized around accumulating evidence that it works. It should be organized around trying to find evidence that it fails. These are not the same project, and they do not produce the same systems.

In plain words: Organizing the testing of a deployed AI system around trying to find evidence that it fails, not around piling up evidence that it works. Systems tested this way still fail, but in ways the organization anticipated and bounded.

Example: Amazon asked whether the recruiting tool was rating technical candidates in a gender-neutral way, which was not the question the tool had been built to answer.

Not to be confused with: counting correct predictions in favorable conditions

**a number that has survived a serious attempt to refute it**
*line 106 · concept*

> That is the difference between a number that has survived a serious attempt to refute it and a number that has merely never been tested — and from the dashboard, they look identical.

In plain words: A number can be well-tested, meaning someone made a serious attempt to show it wrong, or merely never tested, and on a dashboard the two look identical. A team that only counted agreement with past résumés could have collected white swans indefinitely.

Example: Amazon's discovery that the tool was not rating technical candidates in a gender-neutral way was such an attempt.

Not to be confused with: a number that has merely never been tested

**falsifiable but not aimed at the world**  *(also: why this toolkit has four moves and not three)*
*line 108 · concept*

> Falsifiability tells you whether a claim is engineering or rhetoric. It does not tell you whether the engineering is aimed at the world. That takes the next move, which is why this toolkit has four moves and not three.

In plain words: A claim can name its metric, threshold and held-out data and still be aimed at a number that has stopped being what matters. Falsifiability separates engineering from rhetoric, but only the fourth move asks whether the engineering is aimed at the world.

Example: Netflix's claim of ten percent better on a hidden test set passes Popper's test cleanly and was true, yet it was aimed at a number that had stopped being the thing worth knowing.

**root-mean-square error**  *(also: error in predicting star ratings; rating error)*
*line 108 · metric*

> Netflix's claim — ten percent better, measured as root-mean-square error on a hidden test set — passes Popper's test as cleanly as any claim in this book.

In plain words: The error score Netflix's ten-percent-better claim was measured in: roughly how far predicted star ratings land from the real ratings on a hidden test set. The chapter names it but gives no formula.

Example: Netflix's contest claim: ten percent better, measured as root-mean-square error on a hidden test set.

**demarcation**  *(also: demarcation between science and rhetoric; demarcation criterion)*
*line 402 · concept*

> Karl Popper spent the 1930s working out which kinds of claims a scientific community can argue about productively and which it cannot — demarcation — and his answer (a claim is scientific only if it forbids some observation it could be checked against) is the spine of the toolkit you are about to use.

In plain words: Popper's dividing line between claims a community can argue about productively and claims it cannot: a claim is scientific only if it forbids some observation it could be checked against. The book uses it to separate engineering claims from rhetoric.

Example: "The system is robust" fails the line; "Error rate on out-of-distribution inputs remains below 2% across a 30-day rolling window in production" passes it.

Not to be confused with: rhetoric

**rhetorical claim**  *(also: rhetoric; noise that sounds like a claim)*
*line 110 · concept*

> If the claim is compatible with every possible observation, it is not a claim at all. It is a noise that sounds like a claim. Popper's move is to refuse to treat noise as a claim, even when the noise arrives in technical language, on a dashboard, with confidence intervals attached.

In plain words: A claim worded so that it fits every possible outcome, so no observation could show it wrong. It sounds like a claim but is noise, even when it comes in technical language on a dashboard with confidence intervals.

Example: "The system is robust" — what would non-robust look like?

Not to be confused with: a falsifiable engineering claim

**Popperian engineering correction**  *(also: rhetorical claim versus engineering correction)*
*line 119 · method*

> The left column is compatible with any outcome. The right column specifies the conditions under which the claim would be false — which is the only form in which it counts as a claim.

In plain words: Rewriting a vague claim as a testable one by naming the metric, threshold and window that would count as failure. The rewritten claim specifies the conditions under which it would be false, which is the only form in which it counts as a claim.

Example: "The system is robust" becomes "Error rate on out-of-distribution inputs remains below 2% across a 30-day rolling window in production."

**out-of-distribution inputs**  *(also: novel situations; edge cases; anything the training data underrepresented)*
*line 225 · concept*

> In domains where they diverge — novel situations, edge cases, out-of-distribution inputs, anything the training data underrepresented — the system keeps producing fluent output, confidently, in exactly the shape that makes you trust it, about things it has no basis to say.

In plain words: Inputs unlike what the training data covered, such as novel situations, edge cases and anything the data underrepresented; the chapter does not define the term. It says that on these the system keeps producing fluent, confident output it has no basis for.

Example: A table row turns "The system is robust" into an error-rate limit on out-of-distribution inputs over a 30-day rolling window.

**drift**  *(also: PSI)*
*line 117 · failure mode*

> PSI on the three highest-weight input features stays below 0.10 week-over-week; alert fires and triggers human review if breached.

In plain words: The chapter does not define drift; it appears as the vague claim "We have mitigated drift," which the table rewrites as a checkable test. The test is that PSI on the three highest-weight input features stays below 0.10 week-over-week, with an alert and human review if breached.

Example: "We have mitigated drift" becomes: PSI on the three highest-weight input features stays below 0.10 week-over-week.

**the Kantian slice move**  *(also: Kant's slice; the slice; Kant's move)*
*line 137 · method*

> We only ever see a slice of the world, and humility means keeping two things in view — what lies outside our slice, and the fact that there is an outside at all. I do not want to get philosophical about it. I want to give you a move.

In plain words: Remember that a model output is only a slice of the world, seen through a lens the designers and training data chose, and keep in view that there is an outside the slice. In practice you ask what the artifact is, what the world is, and how they relate.

Example: A review of the recruiting tool could examine what it did with résumés and still never touch whether the applicant could do the job, because that question lived outside the slice being examined.

**artifact**  *(also: the artifact is not the world; the appearance is not the thing)*
*line 143 · concept*

> The recruiting tool produced a star rating. The rating was the artifact. Whether the applicant could do the job was the world.

In plain words: The artifact is the output a system produces (a rating, a score, a leaderboard number); the world is the real thing it is supposed to say something about. A review that examines only the artifact can never reach the question that matters.

Example: Netflix's leaderboard, to the fourth decimal place, was the artifact; whether a member found something to watch tonight was the world.

Not to be confused with: the world

**thing in itself**  *(also: the world as it appears to a mind)*
*line 135 · concept*

> In the Critique of Pure Reason he draws a line between the world as it appears to a mind — shaped by space, time, and categories like cause, which the mind brings to experience rather than reads off it — and the thing in itself, which we can think about but never know directly.

In plain words: Kant's line between the world as it appears to a mind and the thing itself, which we can think about but never know directly. The chapter holds a weaker version: the gap is shut in practice, by finite minds and ever-better tools approaching without arriving, not in principle.

Example: A better telescope gives you a sharper appearance, not the thing itself.

**the three questions (artifact, world, relationship)**  *(also: the three questions; artifact versus world)*
*line 139 · method*

> What is the artifact, and what is the world, and what is the relationship between them?

In plain words: The question to put to every model output: what is the artifact (what the system produced), what is the world (what it is supposed to be about), and how are the two related. The chapter says to ask it especially hard when the output is fluent.

Example: For the COVID X-ray models: the artifact is a confident COVID-positive label, the world is the pathology in a patient's lungs, and the relationship is that the model read a marker in the image's corner and never examined the lungs.

**COVID-19 chest X-ray detection models**
*line 145 · named result or case*

> Early in the pandemic, dozens of models were published claiming to detect COVID-19 from chest X-rays at high accuracy. A team led by DeGrave took the strongest of them apart with saliency maps, image edits, and generative tests, and found the models were not reading lungs.

In plain words: A documented case where models published to detect COVID-19 from chest X-rays at high accuracy were found not to be reading lungs. They keyed on features of the datasets, so they failed in new hospitals.

Example: The models "appear accurate but fail when tested in new hospitals."

**confounders in the datasets**  *(also: shortcuts over signal; the incidental tells of which hospital an image came from)*
*line 145 · failure mode*

> They were keying on confounders that lived in the datasets rather than the patients — laterality markers, text tokens, patient positioning, the incidental tells of which hospital an image came from, which happened to correlate with COVID status because positive and negative cases were sourced from different places.

In plain words: Features of the data that happen to correlate with the label without being the thing you care about, so a model can score well by reading them instead of the patient. The X-ray models read such tells instead of lungs.

Example: Laterality markers, text tokens and patient positioning correlated with COVID status because positive and negative cases came from different places.

Not to be confused with: the pathology in a patient's lungs

**COMPAS recidivism scores**  *(also: COMPAS)*
*line 145 · named result or case*

> The same anatomy underlies COMPAS's recidivism scores — the artifact is a number, the world is a person's future conduct, and the relationship runs through arrest records, which in my reading reflect how people are policed as well as how they behave (ProPublica, 2016).

In plain words: A recidivism-scoring system the chapter uses as another artifact-versus-world case: the artifact is a number and the world is a person's future conduct. The link between them runs through arrest records, which the author reads as reflecting how people are policed as well as how they behave.

Example: Glimmer 1.1 lists ProPublica's COMPAS investigation as a case you can pick to analyze.

**solve-verify asymmetry**  *(also: verifying a solution is easier than producing one)*
*line 155 · concept*

> There is a piece of folklore in computer science that says verifying a solution is easier than producing one. If I give you a very large number, it is hard to factor it. If I hand you the factors, it is easy to multiply them and check.

In plain words: The classic idea in computer science that checking a solution is easier than finding one, like factoring a huge number versus multiplying the factors back together. Most of cryptography is built on it.

Example: A very large number is hard to factor, but if you hand over the factors it is easy to multiply them and check.

Not to be confused with: the inverted asymmetry in AI deployment

**the inverted asymmetry in AI deployment**  *(also: the asymmetry inverts; production cheaper than verification; producing is cheap, verifying is expensive)*
*line 159 · concept*

> When an AI system produces an output, producing the output is cheap. The model runs, the result appears, the latency is in milliseconds, the cost is fractions of a cent. Verifying the output is expensive.

In plain words: In AI deployment the classic asymmetry runs backwards: an output costs almost nothing to produce, but checking whether it is right is expensive. The cost of the measure is a fraction of a cent, while the cost of the want is an hour of senior labor or a long wait.

Example: Netflix computed contest error on a hidden test set in moments, but learning whether a change kept members subscribed meant live experiments and a wait.

Not to be confused with: solve-verify asymmetry (the classical one)

**budget for verification**
*line 163 · method*

> If you do not budget for verification, you will not get verification. The system will produce outputs at scale. Verification will not happen at scale.

In plain words: Verification has to be planned and paid for: if it is not, outputs flow at scale while checking does not. The unverified outputs all look like successes until one of them is the applicant, the loan, or the warrant.

Example: A résumé score can only be verified by following the people the tool ranked, which takes months and is impossible for the people it filtered out.

**automating the verification**  *(also: automate the verification; just another model, one layer up)*
*line 165 · concept*

> Most of this book is about how to verify cheaply enough that verification scales. The answer is never "automate the verification" — because that is just another model, with the same problem, sitting one layer up. The answer is always: design the system so that the verification a human can perform tells you what you need to know.

In plain words: Using another model to check a model does not solve the problem, because the checker has the same problem one layer up. The chapter's answer is to design the system so that a check a human can perform tells you what you need to know.

Example: Exercise 7 asks you to build the strongest counterargument to this claim and say when automated verification does help.

**plausibility auditing**  *(also: the twitch)*
*line 179 · concept*

> The capacity to look at an AI output and ask: given what I know about the world this output is supposed to describe, is this output the kind of thing that could be true? A technical recruiter with twenty years of experience, handed a ranked list in which strong engineers keep landing near the bottom, would feel something twitch. The twitch is the audit.

In plain words: The first supervisory capacity: using what you know about the world to ask whether an output is even the kind of thing that could be true, before any formal analysis. It shows up as the experienced "twitch" when something looks off.

Example: A technical recruiter handed a ranked list in which strong engineers keep landing near the bottom would feel something twitch.

**ambient prior**
*line 179 · concept*

> The audit is a check against the ambient prior — the sense, built up over years, of what kinds of cases tend to be what kinds of cases. The model has no such prior. The model has its training data.

In plain words: The sense, built up over years, of what kinds of cases tend to be what kinds of cases. The supervisor carries it from experience with the world; the model has only its training data.

Example: A recruiter with twenty years of experience feels a twitch when strong engineers keep landing near the bottom of a ranked list.

**problem formulation**  *(also: asking the right question)*
*line 181 · concept*

> The capacity to specify the question the system is being asked to answer. This one is going to come up a lot, because most AI failures are failures of problem formulation, not failures of model performance.

In plain words: The second supervisory capacity: stating exactly what question the AI is being asked and checking, before deployment, that it matches the question the decision-maker actually needs answered. The chapter says most AI failures are of this kind, not failures of model performance.

Example: Netflix's contest asked how close a predicted rating lands to the real one, but the business needed to know whether a member would find something to watch tonight and still be there next month.

Not to be confused with: model performance

**the fix is a different question, not a cleverer model**  *(also: retrain against a different label; problem formulation is where the remedy lives)*
*line 183 · method*

> They worked with the manufacturer to retrain against a different label, one that combined cost with a measure of health, and most of the bias went away. The fix was a different question, not a cleverer model.

In plain words: When a system answers the wrong question, the remedy is to change what it is trained to answer, not to scrub features or build something cleverer. Problem formulation is where the remedy lives.

Example: The health-care referral algorithm was retrained against a label combining cost with a measure of health, and most of the bias went away.

Not to be confused with: deleting the offending terms (Amazon's patch, which could not guarantee the models would not find others)

**extra-care referral algorithm**
*line 183 · named result or case*

> A widely used algorithm that decided which patients were referred for extra care had been trained to predict future medical costs, on the theory that people who cost more are sicker. At the same risk score, Black patients were considerably sicker than white patients, because less is spent on them at the same level of illness.

In plain words: A health-care algorithm that picked patients for extra care was trained to predict future medical costs on the theory that people who cost more are sicker. Because less is spent on Black patients at the same level of illness, it understated how sick they were.

Example: At the same risk score, Black patients were considerably sicker than white patients.

**tool orchestration**
*line 185 · concept*

> The capacity to decide which tool to use for which sub-problem. AI is one tool among many. The supervisor decides when AI is the right tool, when human judgment is the right tool, when a different model is, and — this one is the hardest — when the answer is no tool yet, we do not know how to do this well enough to deploy.

In plain words: The third supervisory capacity: deciding which tool fits which sub-problem (AI, human judgment, a different model, or no tool yet). It includes the hardest call, that this system is not ready to be deployed here.

Example: A supervisor who says "we should not deploy this here" is doing supervisory work.

**no tool yet**  *(also: we should not deploy this here)*
*line 185 · concept*

> The supervisor who says "we should not deploy this here" is doing supervisory work. It is often the most valuable work they do.

In plain words: The decision that we do not yet know how to do this well enough to deploy, so no tool, AI or otherwise, should be used. The chapter calls saying so supervisory work and often the most valuable work a supervisor does.

Example: In the capacity table, this decision is never made when no one has the authority or the mandate to make it.

**a decision a resemblance-based method cannot see**  *(also: judging the new by its resemblance to the old)*
*line 187 · concept*

> The lesson is structural, and it is not "data is bad, gut is good": the gatekeepers who said no were using gut, and what they were doing was judging the new by its resemblance to the old. The supervisory skill is recognizing the decision a resemblance-based method cannot see, and handing it to judgment on purpose.

In plain words: Some decisions, like whether a truly unprecedented show will find an audience, are ones a method built on resemblance to past cases cannot assess, because it has nothing to compare them to. A supervisor recognizes these and hands them to human judgment on purpose, remembering that human gut does the same thing by habit.

Example: Matt Duffer estimated he and his brother were turned down fifteen to twenty times before Stranger Things found a buyer, by people who could not see how it would find an audience.

**interpretive judgment**  *(also: the number-in-the-domain)*
*line 189 · concept*

> The capacity to read an output in context. The same number means different things in different deployments. A confidence score of 0.7 is high in one domain and disqualifying in another.

In plain words: The fourth supervisory capacity: knowing the domain well enough to say what an output's number actually means there. The number is not the meaning; the meaning is the number-in-the-domain.

Example: A false positive rate of 5% is acceptable for a spam filter and catastrophic for a cancer screen.

**executive integration**
*line 191 · concept*

> The capacity to take outputs from multiple tools, multiple models, multiple humans, and synthesize them into a decision the integrating system can stand behind. Somebody in the organization has to be the place where the buck stops. If there is no such place, there is no executive integration, and the system as a whole has no decision-maker, only outputs.

In plain words: The fifth supervisory capacity: combining outputs from several tools, models and people into one decision that someone owns. It is the place where the buck stops, and without it the system has outputs but no decision-maker.

Example: In the capacity table's failure example, the pipeline produces decisions but no single person or body owns them, and accountability dissolves into the architecture.

**mapping a failure to a capacity**  *(also: map it to the supervisory capacity whose absence allowed it)*
*line 193 · method*

> By the end of the book you will be able to look at any AI deployment and name, for each step, which capacity is being exercised and by whom. Where you cannot name it, you have found a gap.

In plain words: Looking at an AI deployment and naming, for each step, which of the five capacities is being exercised and by whom. Where you cannot name it, you have found a gap.

Example: A ranking on which strong engineers keep landing near the bottom is accepted because it arrived in a credible one-to-five-star format: no one exercised plausibility auditing.

**five capacities, one accountable decision**  *(also: complementary responsibilities, not five compulsory stages)*
*line 205 · framework*

> These are complementary responsibilities, not five compulsory stages in order. AI should gather and organize evidence within the permitted scope. Humans should set the question, interpret the stakes, choose whether to proceed, and own that decision.

In plain words: The five capacities are parallel responsibilities, not a sequence, and all feed one accountable decision. AI gathers and organizes evidence within its permitted scope; humans set the question, interpret the stakes, decide whether to proceed, and own the decision.

Example: AI can prepare evidence; humans frame the question, judge the stakes, and own the decision.

**Botspeak**  *(also: Botspeak framework)*
*line 209 · framework*

> There is an adjacent vocabulary — developed in the Botspeak framework, treated in full in Appendix A — that I will draw on throughout this book.

In plain words: A vocabulary developed elsewhere (treated in full in Appendix A) that the chapter borrows from. Here it supplies two pillars, strategic delegation and critical evaluation, and notes that neither protects you from the fluency trap.

Example: The two Botspeak pillars named in this chapter are strategic delegation and critical evaluation.

**strategic delegation**  *(also: Botspeak pillar)*
*line 211 · concept*

> Strategic delegation is the capacity to know what to ask the AI to do, given what you understand about its strengths and failure modes on this class of task.

In plain words: A Botspeak pillar: knowing what to ask the AI to do, based on what you understand about its strengths and failure modes on this class of task.

Not to be confused with: critical evaluation

**critical evaluation**  *(also: Botspeak pillar)*
*line 211 · concept*

> Critical evaluation is the capacity to know what to do with what the AI hands back — not "review and accept," but evaluate against criteria you specified before you saw the output.

In plain words: A Botspeak pillar: knowing what to do with what the AI hands back by checking it against criteria you specified before you saw the output. It is not "review and accept."

Not to be confused with: "review and accept"

**fluency trap**
*line 213 · failure mode*

> The more fluently an AI presents its output, the more confident the user becomes in the output. That part is not surprising. The trap is the second move: the more confident the user becomes in the output, the more confident the user becomes in their own evaluation of the output.

In plain words: The more fluently an AI presents its output, the more you trust the output, and then the more you trust your own judgment of it, so you accept any answer that arrives in the same polished shape. The defense is not distrusting fluent outputs but not letting fluency do the work of evidence.

Example: A leaderboard ranked to the fourth decimal place, or a recruiting tool returning a clean one-to-five stars, arrives looking finished, and the polish does the work the question should have done.

Not to be confused with: fluency itself (the trap is the second boost, confidence in your own evaluation)

**fluency as an evaluation booster**  *(also: the second confidence boost; confidence in your own evaluation)*
*line 213 · failure mode*

> Fluency is an evaluation booster. It boosts the wrong evaluations as readily as the right ones.

In plain words: Fluency raises your confidence in your own evaluation of the output, not only in the output, and it raises it whether the evaluation is right or wrong. It makes you more likely to accept any answer that arrives in the same shape.

Example: Glimmer 1.2: ask an LLM a question in your field, lock your confidence, then check what about the fluency boosted it.

**precision as a kind of fluency**  *(also: four decimals look like knowledge)*
*line 215 · failure mode*

> Fluency is not only a property of prose. Precision is a kind of fluency. A leaderboard that ranks teams to the fourth decimal place, or a recruiting tool that returns a clean one-to-five stars, arrives looking finished, the way a well-formed paragraph does.

In plain words: A very precise number looks finished and trustworthy the way a well-formed paragraph does, even though nothing about the decimals says what the number is a number of. Four decimals look like knowledge.

Example: A leaderboard that ranks teams to the fourth decimal place, or a recruiting tool that returns a clean one-to-five stars.

**letting fluency do epistemic work**  *(also: the polish does the epistemic work; epistemic work)*
*line 217 · failure mode*

> The point is not to distrust fluent outputs. Fluent outputs are, on average, more useful than non-fluent ones. The point is to not let fluency do epistemic work.

In plain words: Accepting an output because it sounds right, so polish stands in for evidence. The chapter does not say to distrust fluent outputs, which are on average more useful; it says to stop and ask what would have to be true for the output to be wrong.

Example: Four decimals on a leaderboard: nothing about the decimals says what the number is a number of, yet the polish does the work the question should have done.

Not to be confused with: distrusting fluent outputs (the chapter says that is not the point)

**form versus content**
*line 221 · concept*

> The fluency trap operates on a confusion between two different things: form and content. A well-formed sentence looks like a sentence produced by someone who knows what they are talking about, because in human communication, well-formed sentences usually are.

In plain words: Form is how well an output is written; content is whether it is right. In human speech clear prose usually means the speaker has thought about it, but an AI generates the form by a statistical process separately from the content, so the two are independent.

Example: An AI can produce clear, precise, organized prose about things it has no understanding of.

**clarity as evidence of thinking (the broken heuristic)**  *(also: the clarity is evidence of the thinking)*
*line 223 · concept*

> AI systems have broken this heuristic. An AI can produce clear, precise, organized prose about things it has no understanding of.

In plain words: With a human colleague, clear, precise, organized prose generally shows they have thought about the topic, which is a reliable rule of thumb for human speech. AI has broken that rule of thumb, because it can write clear prose about things it does not understand.

Example: When your colleague says something in clear, precise, organized prose, it generally means they have thought about it.

**maximally fluent and maximally wrong**  *(also: fluent-but-not-quite-right; correct in local detail but misleading in implication)*
*line 223 · failure mode*

> The content is whatever that process produces given the input. These are independent. A sentence can be maximally fluent and maximally wrong simultaneously, and there is no way to tell from the fluency alone.

In plain words: A sentence can be fully polished and fully wrong at the same time, and you cannot tell from the fluency alone because form and content are independent. This is a fluent output that is wrong, not a clumsy one.

Example: Glimmer 1.2 asks you to note every place an LLM's answer is wrong, fluent-but-not-quite-right, or correct in local detail but misleading in implication.

**resemblance to correctness**  *(also: outputs that resemble correct outputs)*
*line 225 · concept*

> This is not a flaw that will be fixed in the next model. It is a structural feature of how these systems work. They learn to produce outputs that resemble correct outputs.

In plain words: AI systems learn to produce outputs that look like correct outputs. Where looking correct and being correct track each other closely this works well, but in novel situations, edge cases and underrepresented inputs the system keeps producing confident, fluent output it has no basis for.

Example: In novel situations or out-of-distribution inputs the system keeps producing fluent output "in exactly the shape that makes you trust it."

Not to be confused with: correctness

**prior specification**  *(also: the prior specification is your anchor; define a failure condition before reading; put the criterion before the output)*
*line 227 · method*

> Before you read the output: specify what a wrong answer would look like. Not vaguely — specifically. "A wrong answer would give a low rating to an applicant whose résumé shows the skills the job requires."

In plain words: Before reading an AI output, write down specifically what a wrong answer would look like; that is your anchor. Without it, the only criterion you have is fluency.

Example: A wrong answer would give a low rating to an applicant whose résumé shows the skills the job requires.

**pass, fail, or unknown**  *(also: record pass, fail, or unknown)*
*line 229 · method*

> The interruption is to define a failure condition before reading, test against evidence, and record pass, fail, or unknown.

In plain words: After testing an output against the failure condition you set in advance, you record one of three results: pass, fail, or unknown. A check that fails or remains unknown sends the work back to revision or stopping.

Example: Before action, a named human checks actual state, records a decision, and revises or stops if the check fails or remains unknown.

**institutional skepticism**  *(also: organizational discipline; skepticism as a team practice)*
*line 241 · concept*

> Institutional skepticism encodes the moves into the workflow. The question "what would have to be true for this output to be wrong?" gets written into the deployment checklist. The specification of falsification conditions gets built into the monitoring dashboard.

In plain words: Building the skeptical moves into the workflow, so they happen reliably instead of depending on one person remembering under time pressure. The design question for each capacity is where in the workflow it is exercised, by whom, and what they see.

Example: The distribution-shift checklist (are these applicants in the training data, are the input features complete, has the deployment context changed since validation) is embedded in the handoff between the AI system and the human decision-maker.

Not to be confused with: individual skepticism (fragile: it depends on one person, on one day, under time pressure, remembering to run the moves)

**undefended gap**
*line 245 · failure mode*

> If the answer to any of those questions is "nobody" or "we haven't thought about that," you have found an undefended gap. Undefended gaps are where people get hurt.

In plain words: A point in a workflow where one of the five supervisory capacities is exercised by nobody, or nobody has thought about it. You find one by asking, for each capacity, where it is exercised, by whom, and what they see.

Example: A pipeline produces decisions but no single person or body owns them, so accountability dissolves into the architecture.

**before the run, during the run, before action**  *(also: make skepticism part of the workflow)*
*line 247 · framework*

> Before a run, a human defines success and locks a prediction. During the run, AI acts within scope and preserves evidence. Before action, a named human checks actual state, records a decision, and revises or stops if the check fails or remains unknown.

In plain words: The workflow stages where skepticism is built in: before a run a human defines success and locks a prediction; during it the AI acts within scope and preserves evidence; before action a named human checks actual state and decides. A check that fails or remains unknown means revising or stopping.

Example: Keep the original prediction and append what you observed; do not rewrite the prediction after the result.

**the Pebble**  *(also: casebook; your casebook)*
*line 255 · framework*

> In the LLM exercise that closes each chapter you will build a casebook on an agent of your own choosing, and that casebook is our Pebble: dropped in Chapter 1, and by the end of the book it will have been rippled through every lens the book teaches.

In plain words: The casebook you build on an agent of your own choosing, started in Chapter 1 and rippled through every lens the book teaches. The chapters in between run on their own cases; yours is the one that stays.

Example: The Agentic Red-Team Casebook, begun in this chapter's LLM exercise and carried through Chapters 2 to 13.

**what would change my mind**
*line 269 · method*

> If a documented case existed where a fluent, high-confidence AI output reliably tracked truth across deployments without supervisory verification, the fluency trap framing would need revision. I have not found such a case. I am open to being shown one.

In plain words: The author's statement of what evidence would force him to revise his claim: a documented case where a fluent, high-confidence AI output reliably tracked truth across deployments without supervisory verification. He says he has not found one.

Example: The fluency-trap framing would need revision if such a case existed.

**trust the model anyway**  *(also: Still puzzling)*
*line 271 · concept*

> I do not yet have a clean criterion for when a supervisor should trust the model anyway in time-pressured deployments — the cases where the cost of verification exceeds the cost of being wrong, in expectation, but the loss distribution is heavy-tailed.

In plain words: The chapter's open question: when should a supervisor trust the model without verifying, in time-pressured deployments where verification costs more than being wrong in expectation but losses are heavy-tailed. The author does not consider it settled.

Example: Exercise 11 asks you to frame the question, name the variables, and sketch a decision rule without Chapters 2 and 9.

**glimmer**
*line 279 · method*

> A glimmer is a short, targeted encounter with a non-obvious outcome, designed so that accepting the AI's output uncritically produces a failure. The failure is the point. The point is what the failure reveals about what you were assuming.

In plain words: A short exercise built so that accepting the AI's output uncritically produces a failure, and the failure shows you what you were assuming. The failure is the point.

Example: Glimmer 1.1 (The Confident Failure) and Glimmer 1.2 (The Fluency Trap).

**prediction-lock**  *(also: lock the prediction; locked prediction)*
*line 284 · method*

> Before reading the post-mortem, write down your prediction of the technical failure. Prediction-lock: you cannot revise this after reading.

In plain words: Writing your prediction down before you see the result and not revising it afterward, so you cannot rewrite it to fit what you find. You keep the original prediction and append what you observed.

Example: In Glimmer 1.1, you write down your predicted technical failure before reading the post-mortem.

**gap analysis**
*line 286 · method*

> Name the gap between your prediction and the actual finding. Which of the Five Supervisory Capacities, if exercised, would have caught the failure? Was it the same capacity you predicted?

In plain words: In the Glimmer, naming the gap between what you predicted and what actually failed, and which of the five capacities would have caught it. The chapter says the grade is on the gap analysis.

Example: Was the capacity that would have caught the COMPAS or Uber failure the same one you predicted?

**Frictional method**  *(also: Frictional framework)*
*line 346 · framework*

> The prediction-lock-before-observation discipline and the journal are the Frictional method (Nik Bear Brown's Frictional framework) applied to validation.

In plain words: The record-keeping discipline of locking a prediction before you observe and keeping a journal of it, which the chapter presents as Nik Bear Brown's Frictional framework applied to validation.

Example: The casebook journal logs a prediction-lock for each red-team observation.

**casebook journal**  *(also: prediction-lock log; case-write-up template)*
*line 346 · method*

> You are also standing up the record-keeping apparatus the later chapters assume: a casebook journal (the prediction-lock log you will keep for every red-team observation) and a reusable one-page case-write-up template.

In plain words: The log where you record a dated prediction-lock before each red-team observation of your agent, kept with a reusable one-page case-write-up template. Its template fields include case ID, input, action taken, reported outcome, actual outcome, which capacity failed, evidence and severity.

Example: Task 3 of the prompt asks Claude to draft the journal file and the one-page template.

**System Dossier**
*line 380 · concept*

> End with a one-paragraph "System Dossier" I can paste into my Claude Project's system prompt: name of agent, architecture summary, tool surface, deployment context, the candidate failure mode my casebook will pursue, and any access constraints I'm working under.

In plain words: A one-paragraph description of the agent you will red-team, pasted into your Claude Project's system prompt so every chapter inherits the context. It names the agent, its architecture, tool surface, deployment context, the candidate failure mode to pursue, and any access constraints.

**agentic**
*line 358 · concept*

> Be agentic (it takes actions in the world via tools, not just produces text)

In plain words: A property of an AI system that takes actions in the world through tools, rather than only producing text. The casebook agent must be agentic.

**blast radius**
*line 360 · concept*

> Have a meaningful blast radius (a wrong action has real consequences — lost data, wrong recommendation, leaked information, financial impact, safety issue)

In plain words: How much real damage a wrong action by the agent could cause, such as lost data, a wrong recommendation, leaked information, financial impact or a safety issue. A good casebook agent has a meaningful one.

## Chapter 2, The Confidence Illusion (87 terms)

**confidence illusion**  *(also: confident numbers are not correct numbers)*
*line 10 · concept*

> That gap — between the confidence a system radiates and the confidence it has earned — is what this chapter is really about, and it is exactly where the pairing Chapter 1 committed us to does its work: the machine's speed, your doubt. The most pervasive failure in AI deployment is not that models are stupid. It is that confident numbers are not correct numbers, and almost nobody checks.

In plain words: The gap between how sure a system sounds and how sure it has earned the right to be. The chapter's claim is that the most common AI deployment failure is not a stupid model but a confident number that nobody checked.

Example: A classifier hands back a tidy sorted column of 0.94, 0.91, 0.88 that looks done but has not been checked against the base rate or calibration.

**confident numbers formatted to look like facts**  *(also: looking like a measurement)*
*line 8 · failure mode*

> Here is what is actually happening: that column is a set of degrees of belief the model holds, formatted to look like facts about the world. The 0.94 does not announce whether 94 out of every 100 cases scored 0.94 actually turn out positive. It does not announce the base rate of the thing I am looking for.

In plain words: A model's probabilities are only its own degrees of belief, but a clean, sorted column of them looks like a measurement of the world. The polish makes an unchecked number look finished, so it gets read as evidence.

Example: A column of 0.94, 0.91, 0.88 ready to drop into a dashboard says nothing about how often a 0.94 is right or how common positives are.

Not to be confused with: a measured fact about the world (which is what the column looks like)

**degree of belief**
*line 30 · concept*

> The output is not "true" or "false." The output is a degree of belief — a number between zero and one that tells you how confident you should be, given what you currently know.

In plain words: A probability is a number between zero and one saying how confident you should be given what you currently know, not a true-or-false fact. Two engineers with different starting beliefs can both reason correctly and land on different probabilities.

Example: The classifier's 0.94 is the model's degree of belief, not a fact about the world.

Not to be confused with: a fact (true or false)

**base rate**  *(also: prior; prior probability of disease in the population; background rate)*
*line 270 · concept*

> But the question you needed was given a positive test, how often is the disease there? Those are not the same question. You cannot get from one to the other without one extra ingredient: the prior probability of disease in the population — the base rate.

In plain words: How common the thing you are looking for is in the whole population, before any test result or model score is considered; in the disease example it is also called the prior. You need it to turn "how often is the test right on sick people?" into "how often is a positive really sick?", and intuition almost always leaves it out.

Example: One person in ten thousand has the disease, so even with a 99% accurate test a positive result is right only about 1 time in 101.

Not to be confused with: accuracy (the 99% on the box; people answer with it instead of weighing the base rate)

**prior**  *(also: prior belief; prior probability; base rate (in the disease example))*
*line 32 · concept*

> The reason is that they walked in with different priors — different starting beliefs about the world before the evidence arrived. Probability is always conditional on your information state, and different people have different information states.

In plain words: Your belief about how likely something is before you see the new evidence; in the disease example the prior is the base rate, 0.0001. Two engineers with different priors can reach different probabilities from the same evidence and both be reasoning correctly.

Example: Before the test, the chance that this patient has the disease is 0.0001, one in ten thousand; the prior sits in Bayes' numerator with the same weight as the test's sensitivity.

Not to be confused with: posterior (what you believe after the evidence)

**plausibility auditing**  *(also: plausibility audit; plausibility-auditing muscle; base-rate check)*
*line 10 · concept*

> The supervisory capacity this chapter trains hardest is plausibility auditing — the first of the five from Chapter 1, the capacity to hear the wrong note in a number before you can prove it wrong. And the wrong note here is almost always the same note: the model forgot the prior, or you did, or nobody checked whether 0.94 means what it says.

In plain words: The skill of sensing that a number is off before you can prove it. Here the main move is the base-rate check: ask what fraction of the flagged population is actually real.

Example: Before trusting a flag, ask what fraction of the flagged population is actually real.

**Boolean instinct**  *(also: Boolean education)*
*line 34 · failure mode*

> The Boolean instinct works fine in deterministic systems. It misleads you in any system where you are working from a model rather than from the world itself — and every machine learning system, every AI deployment, every statistical inference, is a model rather than the world.

In plain words: The habit, from engineering training, of treating every output as true or false. It works for deterministic systems but misleads when you read a model's output, which is a degree of belief and not a fact.

Example: "The function returned 42" is a verifiable fact; "the model returned 0.91" is not.

Not to be confused with: degree of belief

**build and audit**  *(also: build/audit framework)*
*line 18 · framework*

> And at the chapter's end you will do two things with the ideas, not one: build a pipeline that emits and calibrates its own confidence, and audit someone else's confident number against the base rate.

In plain words: Build means making your own system state its confidence and then calibrating it; audit means checking a confident number someone else gave you against the base rate.

Example: Glimmer 2.4 is the build exercise; Exercise 16 (AUDIT) checks a vendor's or a paper's confidence number.

**Bayes' theorem**
*line 305 · method*

> The thing the formula makes unmissable is this: the posterior — what you believe after seeing the evidence — is proportional to the prior times the likelihood. The prior is in the numerator, with the same weight as the quality of the evidence. You cannot legitimately ignore it.

In plain words: A formula for updating a belief: multiply the prior by the likelihood of the evidence and divide by the total probability of the evidence, to get the posterior. Because the prior sits in the numerator with the same weight as the test's quality, you cannot legitimately ignore it.

Example: Prior 0.0001 with a 99% test and a positive result gives P(disease | positive) of about 0.0098, roughly one percent.

Not to be confused with: total probability theorem (the same machinery run in the opposite direction)

**total probability theorem**
*line 189 · method*

> This is the total probability theorem. It says: if you can compute the probability of $B$ conditional on each possible "scenario" $A_i$, and you know how likely each scenario is, you can add them up — weighted by their probabilities — to get the unconditional probability of $B$.

In plain words: When you cannot measure a probability directly, split the cases into scenarios that do not overlap and cover every possibility, find the chance of the outcome in each, weight each by how likely the scenario is, and add them up.

Example: Three model versions handle 40%, 30% and 30% of traffic and are wrong 2%, 3% and 5% of the time, so the pipeline is wrong 3.2% of the time.

Not to be confused with: Bayes' theorem (the same machinery run in the other direction; this sum is Bayes' denominator)

**multiplication rule**
*line 129 · method*

> This is the multiplication rule: to find the probability that both events occur, multiply the probability of the first by the conditional probability of the second given the first. It sounds simple. The power is in how it extends.

In plain words: The probability that two events both happen is the probability of the first times the probability of the second once you know the first happened: P(A ∩ B) = P(B) · P(A | B).

Example: Two tool calls both succeeding: P(A1) × P(A2 | A1) = 0.9 × 0.85.

**chain rule**  *(also: multiplication (chain) rule)*
*line 139 · method*

> It chained tool calls: read a file, call an API, write a result, verify. The report is a claim about the whole chain succeeding, and the chain rule is how you take that claim apart.

In plain words: The multiplication rule extended to any number of events: multiply the first event's probability by each next event's probability given everything before it. It is how you take apart a claim that a whole sequence of steps succeeded.

Example: 0.9 × 0.85 × 0.8 = 0.612: the chance all three tool calls succeeded.

**joint probability**
*line 155 · concept*

> Each edge is a conditional probability. Each leaf is a joint probability found by multiplying along the path — the chain rule made visible.

In plain words: The probability that several events all happen together, written P(A ∩ B). You find it by multiplying along a path of conditional probabilities.

Example: P(A1 ∩ A2 ∩ A3) = 0.612 is the joint probability that all three tool calls succeeded.

**accuracy**  *(also: 99% accurate; model accuracy)*
*line 270 · metric*

> You were computing the right answer to a different question. You were computing given the disease, how often does the test get it right? That is ninety-nine percent.

In plain words: How often a model or test gets the right answer, like the "99% accurate" on the disease test's box. It says nothing about how rare the condition is, whether a model's stated confidence matches reality, or how costly its errors are.

Example: A 99% accurate test for a disease affecting 1 in 10,000 people is right on sick people 99% of the time, yet a positive result is right only about 1 time in 101.

Not to be confused with: loss (what being wrong costs, not how often) and calibration (whether the stated confidence matches what happens); a model can be very accurate without being calibrated

**calibration**  *(also: calibrating; calibration diagnostic)*
*line 404 · concept*

> It is called calibration, and a model can be very accurate without being calibrated, and the difference matters. A model is calibrated when its stated probabilities match what actually happens. If the model says "seventy percent confident" on a thousand cases, you want roughly seven hundred of those cases to turn out positive.

In plain words: How closely the confidence a model states matches how often it is actually right, so that among 1,000 cases where it says 70%, about 700 turn out positive. The chapter calls it the most operationally important diagnostic; it is a different thing from accuracy, and it applies to people's forecasts as well as to models.

Example: A net that says 99% when it should say 85% is badly miscalibrated at the high end; your own 90% intervals that contain the answer only about half the time show the same problem in a person.

Not to be confused with: accuracy (a model can be very accurate without being calibrated)

**calibrated**  *(also: well-calibrated; perfectly calibrated)*
*line 406 · concept*

> A model is calibrated when its stated probabilities match what actually happens. If the model says "seventy percent confident" on a thousand cases, you want roughly seven hundred of those cases to turn out positive. If only four hundred do, the model is overconfident — its stated number is bigger than it has any right to be.

In plain words: A model is calibrated when the number it states is the number that turns out true: when it says 70%, it is right about 70% of the time. A perfectly calibrated model traces the diagonal of the calibration curve.

Example: Says 70% on 1,000 cases: about 700 positives is calibrated, 400 is overconfident, 900 is underconfident.

Not to be confused with: accurate (right often; a model can be very accurate without being calibrated)

**miscalibrated**  *(also: miscalibration)*
*line 408 · failure mode*

> A miscalibrated model peels off the diagonal, and the shape of how it peels off tells you something about how the model is wrong.

In plain words: A model is miscalibrated when its stated probabilities do not match what happens, so its calibration curve peels off the diagonal; overconfident and underconfident are the two directions. The chapter notes a model can be calibrated on clean inputs and wildly miscalibrated on perturbed ones (Chapter 4).

Example: Exercise 12: a model well-calibrated at 0.4–0.6 confidence but systematically overconfident above 0.85.

Not to be confused with: overconfident and underconfident (the two directions of miscalibration)

**calibration curve**  *(also: reliability diagram)*
*line 408 · method*

> Put the model's stated probability on the horizontal axis. Put the actual frequency of positives on the vertical axis. A perfectly calibrated model traces the diagonal — where stated and actual are equal.

In plain words: A plot of what the model says against what actually happens: stated probability on one axis, the actual share of positives on the other. A perfectly calibrated model sits on the diagonal, and the shape of how a curve peels off it shows how the model is wrong.

Example: Figure 2.8: the model is reasonably calibrated in the middle of its range (says 60%, about right) but badly overconfident toward the top (says 99% when it should say 85%).

Not to be confused with: accuracy (a calibration curve shows what accuracy metrics hide)

**Central Limit Theorem**
*line 448 · concept*

> If you have taken a stats class, you have met the Central Limit Theorem. It says, more or less, that if you add up a lot of independent random variables with finite variance and normalize them, the result looks like a Gaussian — the bell curve. This is a beautiful theorem and it is the reason averages are useful, confidence intervals work, and quality control exists as a discipline.

In plain words: Add up many independent random quantities with finite variance and normalize them, and the result looks like a bell curve, which is why averages and confidence intervals can be trusted. It has two requirements, independence and finite variance, and it quietly fails when either one fails.

Example: In Glimmer 2.1 sample means from a Gaussian converge, but sample means from a Cauchy distribution never settle.

**loss**  *(also: cost of being wrong; cost of error; cost-of-error)*
*line 506 · concept*

> What is the cost distribution? Is the loss of being wrong roughly uniform, or are there rare catastrophic outcomes that average-loss metrics will miss?

In plain words: What it costs when the system is wrong, not how often it is wrong. Most wrong outputs may be minor inconveniences while a rare one kills a patient or wipes a database.

Example: Exercise 10: a false positive costs $10 of analyst time, a false negative costs $500,000 (a breach), although the error rates are only 2% and 0.5%.

Not to be confused with: accuracy (how often it is right; it says nothing about what the errors cost)

**loss distribution**  *(also: cost distribution; distribution of the cost of being wrong; heavy-tailed loss)*
*line 465 · concept*

> For deployment, the question that matters is: what is the distribution of the cost of being wrong? If most of your wrong outputs are minor inconveniences but one in a thousand kills a patient or wipes a database — your loss distribution is heavy-tailed, and a deployment evaluated on average loss is being evaluated on a quantity that does not converge in any useful sense.

In plain words: How the cost of being wrong is spread across a system's errors. If most errors are minor but a rare one is catastrophic, the loss distribution is heavy-tailed.

Example: A security-alert system: a false positive costs $10 of analyst time, a false negative costs $500,000 (Exercise 10).

**heavy-tailed distribution**  *(also: heavy-tailed regime; heavy-tailed; heavy-tailed loss)*
*line 452 · concept*

> Finite variance breaks down in heavy-tailed distributions — distributions where extreme events are not rare enough for averaging to dampen them.

In plain words: A distribution where extreme events are common enough that averaging does not tame them, so the sample mean keeps getting moved by the next observation however much data you have. Examples in the chapter include wealth, file sizes, earthquake magnitudes and the cost of an AI system being wrong.

Example: Most of a system's wrong outputs are minor inconveniences, but one in a thousand kills a patient or wipes a database.

Not to be confused with: Gaussian (bell-curve) distribution

**distribution shift**
*line 384 · concept*

> The training set is the past. The deployment is the future. Distribution shift is the technical name for the world declining to cooperate.

In plain words: When the real world after deployment stops looking like the data the model was trained on, so the patterns it learned no longer apply while its confidence stays high. The chapter reads it as Hume's point that the future is free to differ from the past.

Example: Models trained on pre-2020 medical imaging were deployed in 2021, after COVID had changed the lung images and the population that ended up in scanners.

**Hume's problem of induction**  *(also: Hume's induction problem; problem of induction)*
*line 382 · concept*

> Hume's answer, which infuriated people: no. Logically, the future is free to differ from the past. Induction works because the world cooperates, not because the laws of logic force it to.

In plain words: The point that no amount of past evidence logically guarantees the future will match it; induction works only because the world happens to cooperate. In machine learning it becomes the bet that deployment looks like training.

Example: Watching the sun rise every morning of your life does not guarantee it will rise tomorrow.

Not to be confused with: distribution shift (the engineering translation of the same idea)

**confidently wrong**
*line 386 · failure mode*

> Sometimes the world quietly changes — the inputs drift, the base rates move, the relationship between cause and effect mutates — and the model keeps producing confident outputs that have come unstuck from reality. The model does not know. It cannot know.

In plain words: A model that keeps stating high confidence after the world has changed under it, so its outputs no longer match reality. The chapter names three routes: the inputs drift, the base rates move, or the cause-and-effect relationship changes.

Example: Models trained on pre-2020 medical imaging made confident predictions in 2021 that no longer matched the disease distribution.

**sample space**
*line 40 · concept*

> A sample space $\Omega$ is the set of all possible outcomes of an experiment. Rolling a die: $\Omega = \{1, 2, 3, 4, 5, 6\}$. Whether a patient has a disease: $\Omega = \{\text{sick}, \text{healthy}\}$.

In plain words: The set of every outcome that could happen in an experiment, the universe that all probabilities are measured inside.

Example: For a die, the sample space is {1, 2, 3, 4, 5, 6}; for a patient, {sick, healthy}.

Not to be confused with: event (a part of the sample space)

**event**
*line 42 · concept*

> An event is any subset of the sample space — any collection of outcomes we might care about. "The die shows an even number" is the event $\{2, 4, 6\}$.

In plain words: Any collection of outcomes from the sample space that you care about, which can be a single outcome or several.

Example: "The die shows an even number" is the event {2, 4, 6}.

Not to be confused with: sample space (the set of all outcomes)

**probability measure**
*line 44 · concept*

> A probability measure $P$ assigns a number to every event. To be a legitimate probability measure, $P$ must satisfy three axioms:

In plain words: A rule P that gives every event a number and obeys three axioms (nonnegativity, normalization, additivity). Everything else in the chapter, including conditional probability, Bayes' theorem and the Central Limit Theorem, is derived from them.

Example: Conditioning on B gives P(· | B), which is itself a legitimate probability measure on the shrunken sample space.

**nonnegativity**
*line 46 · concept*

> Nonnegativity: $P(A) \geq 0$ for every event $A$.

In plain words: The first axiom: no event can have a negative probability.

Example: "The die shows an even number" cannot have a probability below zero.

**normalization**
*line 47 · concept*

> Normalization: $P(\Omega) = 1$. Something has to happen.

In plain words: The second axiom: the probability of the whole sample space is 1, because some outcome has to occur.

Example: For a patient, either sick or healthy happens, so the two probabilities together make 1.

**additivity**
*line 48 · concept*

> Additivity: If $A$ and $B$ are disjoint — they cannot both occur — then $P(A \cup B) = P(A) + P(B)$.

In plain words: The third axiom: if two events cannot both happen, the probability that one or the other happens is the sum of their separate probabilities.

Example: "The die shows 2" and "the die shows 4" cannot both happen, so their probabilities add.

**consequences of the axioms**
*line 52 · concept*

> Two useful consequences follow immediately. First, $P(\emptyset) = 0$: the probability of nothing happening is zero. Second, $P(A^c) = 1 - P(A)$: the probability of $A$ not happening is one minus the probability of it happening.

In plain words: Two facts that follow right away from the axioms: the probability of nothing happening is 0, and the probability that A does not happen is 1 minus the probability that it does.

Example: If 45% of cases turn out high-acuity, 55% do not.

**classical probability**  *(also: Laplace formula)*
*line 66 · concept*

> Classical probability applies when all outcomes are equally likely. You have a fair coin. The probability of heads is one divided by two — one favorable outcome out of two equally possible outcomes.

In plain words: Probability as favorable outcomes divided by total outcomes, valid when every outcome is equally likely. It fails when the outcomes are not equally likely.

Example: A bag with one ball each of five colors: the chance of drawing yellow is 1/5.

Not to be confused with: frequentist probability

**frequentist probability**  *(also: relative-frequency probability)*
*line 70 · concept*

> Frequentist (relative-frequency) probability applies to repeatable experiments. You toss a coin twenty times and get seven heads. The relative frequency of heads is $\frac{7}{20}$.

In plain words: Probability as the long-run share of times an event happens when a stable experiment is repeated over and over. It suits quality control and A/B tests but cannot assign a probability to a one-off event.

Example: Seven heads in twenty tosses gives a relative frequency of 7/20.

Not to be confused with: Bayesian probability

**Bayesian probability**
*line 78 · concept*

> Bayesian probability treats probability as a degree of belief updated by evidence. You start with a prior belief — how likely something was before you saw the evidence.

In plain words: Probability as a degree of belief that you revise when evidence arrives, which makes it natural for one-off cases. Its cost is that you must specify a prior, and the result depends on that choice.

Example: Whether this specific transaction is fraud, or whether this specific agent completed its task correctly.

Not to be confused with: frequentist probability

**posterior**
*line 78 · concept*

> You observe evidence. You update. The posterior is what you should believe now.

In plain words: What you believe after you have seen the evidence: your prior updated by the evidence. In Bayes' theorem it is proportional to the prior times the likelihood.

Example: P(disease | positive) is about 0.0099, roughly one percent, in the disease example.

Not to be confused with: prior (what you believed before the evidence)

**conditional probability**  *(also: P(A | B))*
*line 100 · concept*

> The numerator is the probability that both $A$ and $B$ occur. The denominator is the total probability of $B$. Dividing one by the other gives you the fraction of $B$'s probability that falls inside $A$.

In plain words: The probability of A once you already know B happened, P(A | B) = P(A ∩ B) / P(B). It is like shrinking the sample space to B and asking what fraction of it also lies in A.

Example: 76% of cases carry a lab flag and 30% are both flagged and high-acuity, so P(high-acuity | flagged) = 0.30 / 0.76, about 0.395.

Not to be confused with: P(B | A), the reverse (given the disease the test is right 99% of the time, but given a positive test the disease is there only about 1%)

**abnormal lab flag example**
*line 113 · named result or case*

> About 39.5% — lower than the unconditional 45%. Seeing the flag did not raise my estimate, it lowered it, because the flag is common and most flagged cases are not serious. That is the shape of the trap this whole chapter circles: a salient signal arrives, intuition reads it as bad news, and the conditioning says otherwise.

In plain words: In a triage log, 76% of cases carry an abnormal lab flag, 45% are high-acuity and 30% are both, so a flagged case is high-acuity only about 39.5% of the time. Because the flag is common, seeing it lowers the estimate instead of raising it.

Example: P(high-acuity | flag) = 0.30 / 0.76, about 0.395, below the unconditional 0.45.

**agent tool-call chain**
*line 153 · named result or case*

> About 61% — against a single, clean "task complete." The report is one bit; the thing it claims is a product of three shrinking conditionals.

In plain words: An agent must land three tool calls in order, with success chances 0.9, then 0.85 given the first, then 0.8 given the first two. The chance the whole task really completed is 0.612, far less than one clean "task complete" suggests.

Example: 0.9 × 0.85 × 0.8 = 0.612.

**independence**  *(also: independent events)*
*line 159 · concept*

> Two events are independent when knowing one tells you nothing about the other — then $P(A \mid B) = P(A)$ and the rule collapses to $P(A \cap B) = P(A) \cdot P(B)$.

In plain words: Two events are independent when learning that one happened tells you nothing about the other, so the chance of both is just the two chances multiplied. It breaks down in network-structured data, in time series with autocorrelation, and in any system where one outcome shifts the probability of the next.

Example: Treating the three tool-call steps as independent at 0.9 each gives 0.729 instead of the honest 0.612.

**assuming independence**  *(also: assuming away the dependence)*
*line 159 · failure mode*

> Assume the three steps are independent and reliable at $0.9$ each, and you compute $0.9^3 = 0.729$: 73% where the honest number was 61%. Twelve points of unearned confidence, all of it from assuming away the dependence. In real agent runs independence fails quietly — one step's failure degrades the state the next depends on, so failures cluster instead of scattering — and the error runs in the optimistic direction.

In plain words: Treating dependent steps as if each succeeded on its own makes a chain look more reliable than it is, because in real runs one failure degrades the next step. The error runs in the optimistic direction, the one that gets you hurt.

Example: 0.9^3 = 0.729 (73%) against the honest 0.612 (61%): twelve points of unearned confidence.

**partition**
*line 185 · concept*

> Let $A_1, A_2, \ldots, A_n$ be events that partition the sample space: they are mutually exclusive (no two can occur simultaneously), collectively exhaustive (one of them must occur), and each has positive probability.

In plain words: A split of the sample space into pieces that cannot overlap (mutually exclusive), together cover every possibility (collectively exhaustive), and each have positive probability.

Example: The three model versions A, B and C partition the cases by which version handled them.

**fleet's error rate**
*line 206 · named result or case*

> 3.2% of outputs are wrong — a number that lives in none of the three models but falls straight out of the partition. That is the whole use of the theorem: when you cannot measure a system-level rate directly, decompose it into scenarios you can measure, weight each by how often it occurs, and sum.

In plain words: A fraud-screening pipeline routes cases across three model versions handling 40%, 30% and 30% of traffic and wrong 2%, 3% and 5% of the time. The overall error rate, 0.40×0.02 + 0.30×0.03 + 0.30×0.05 = 3.2%, is reported by none of the models and comes from the partition.

Example: P(D) = 0.032 for the pipeline as a whole.

**the 99% accurate test**  *(also: the test that is 99% accurate)*
*line 242 · named result or case*

> The disease is rare. About one person in ten thousand has it. The test is, the company says, ninety-nine percent accurate.

In plain words: A disease affecting 1 in 10,000 people is screened by a test called 99% accurate, and a patient tests positive. Among 10,000 people there is about 1 true positive and about 100 false positives, so a positive result means disease only about 1 time in 101.

Example: Most engineers answer above 90%; the actual answer is about one percent.

**Casscells, Schoenberger and Graboys study**  *(also: Harvard house officers study)*
*line 248 · named result or case*

> And this is not a failing of amateurs. It is exactly the result the classic study found: Casscells, Schoenberger, and Graboys put a 1-in-1,000 version of this question to sixty Harvard house officers, students, and attendings, and most answered around 95% — off by roughly the same two orders of magnitude I am about to walk you through

In plain words: A classic 1978 study that gave a base-rate question like the 99% test to sixty Harvard physicians and students. Most answered around 95%, off by about two orders of magnitude, the same mistake the chapter says engineers make.

Example: Most answered around 95% to a 1-in-1,000 version of the question.

**true positive**
*line 252 · concept*

> The test, which is 99% accurate in the sense that it correctly identifies people who are sick, catches that person. Call it one true positive.

In plain words: A sick person whom the test correctly flags as positive.

Example: The one person in the 10,000 who actually has the disease and gets a positive result.

Not to be confused with: false positive

**false positive**  *(also: false alarm)*
*line 254 · concept*

> The other 9,999 do not have the disease. "Ninety-nine percent accurate" also means the test correctly returns negative on 99% of healthy people. The other 1% — that is 0.01 times 9,999, about 100 people — get a false positive.

In plain words: A healthy person whom the test wrongly flags as positive. When the condition is rare the healthy group is so large that false positives swamp the true ones.

Example: About 100 of the 9,999 healthy people get a false positive, against 1 true positive.

Not to be confused with: true positive

**true positive rate**  *(also: sensitivity)*
*line 252 · metric*

> The test, which is 99% accurate in the sense that it correctly identifies people who are sick, catches that person.

In plain words: The share of people who really have the disease whom the test correctly identifies as sick. It is the same number as sensitivity.

Example: In the disease example the true-positive rate is 0.99, P(positive | disease).

Not to be confused with: true negative rate (the matching number for healthy people)

**true negative rate**  *(also: specificity)*
*line 254 · metric*

> "Ninety-nine percent accurate" also means the test correctly returns negative on 99% of healthy people.

In plain words: The share of healthy people whom the test correctly returns negative on. It is the same number as specificity, and the rest become false positives.

Example: The test returns negative on 99% of the 9,999 healthy people; the other 1% (about 100) are false positives.

Not to be confused with: true positive rate (the matching number for sick people)

**sensitivity**  *(also: true positive rate)*
*line 259 · metric*

> I used it as both the true-positive rate and the true-negative rate. Those are two different numbers — sensitivity and specificity — and a real test has two, not one.

In plain words: Of the people who really have the disease, the share the test correctly flags as positive; the same idea as the true positive rate. It answers "given the disease, how often does the test get it right?", which is not the same question as "given a positive test, how often is the disease there?"

Example: The Epic Sepsis Model had sensitivity 33%: it missed sepsis in 67% of the patients who had it.

Not to be confused with: specificity

**specificity**  *(also: true negative rate)*
*line 259 · metric*

> I used it as both the true-positive rate and the true-negative rate. Those are two different numbers — sensitivity and specificity — and a real test has two, not one.

In plain words: Of the people who are healthy, the share the test correctly returns negative on; the same idea as the true negative rate. The healthy people it misses become false positives.

Example: With 99% specificity, about 100 of the 9,999 healthy people in the 10,000-person example still get a false positive.

Not to be confused with: sensitivity

**decorative number**  *(also: decorative claim)*
*line 423 · concept*

> The number on the screen, by itself, is decorative. It might mean what you think it means; it might be off by a lot; you have no way of telling without checking.

In plain words: A confident-looking number that nobody has checked against reality, so you cannot tell how far off it is. A model's stated probability stays decorative until you see its calibration curve on data from the real deployment.

Example: A net says 99% when it should say 85%, and says it fluently.

Not to be confused with: a calibrated number (one backed by a calibration curve on deployment data)

**forgetting the prior**  *(also: ignoring the base rate; ignoring the prior)*
*line 272 · failure mode*

> Your intuition forgot the prior. Almost all intuition, in my experience, forgets the prior. We are built to judge evidence by its own face value, not by adjusting it against the background rate of what we are looking for.

In plain words: Judging a positive result by the test's accuracy alone instead of weighing how rare the condition is to begin with. The chapter calls it the single most common mistake in interpreting probabilistic system outputs.

Example: Engineers answer above 90% to the 99% test when the true answer is about 1%.

Not to be confused with: answering "given the disease, how often does the test get it right?" instead of "given a positive test, how often is the disease there?"

**inference interpretation**  *(also: formal belief revision)*
*line 309 · concept*

> Think of $A_1, A_2, \ldots, A_n$ not as events but as hypotheses — possible states the world could be in. $B$ is the evidence you observe. $P(A_i)$ is your prior: how probable you thought hypothesis $i$ was before seeing the evidence.

In plain words: Reading Bayes' theorem as belief revision: the possible states of the world are hypotheses, what you observe is evidence, and the formula turns your prior into a posterior. It prevents overcounting evidence (a positive test proves disease) and undercounting the prior (the test's accuracy is all that matters).

Example: Hypotheses: disease present or absent; evidence: a positive test.

**likelihood**
*line 309 · concept*

> $P(B \mid A_i)$ is the likelihood: how probable the evidence would be if hypothesis $i$ were true.

In plain words: How probable the evidence would be if a given hypothesis were true. In the disease example it is the chance of a positive test given the disease, 0.99.

Example: P(positive | disease) = 0.99.

Not to be confused with: posterior (the probability of the hypothesis given the evidence)

**factory revisited**
*line 324 · named result or case*

> Even though machine C produces only 30% of all items, it produces almost 47% of the defectives — because its defect rate is the highest. This is the kind of inference Bayes enables: reasoning backward from evidence to cause.

In plain words: Given a defective item, the chance it came from machine C is 0.30 × 0.05 / 0.032, about 0.469, even though C makes only 30% of the output. The biggest source of defects is the one with the highest defect rate, not the one with the most output.

Example: Shares of defectives: machine A 25%, machine B 28%, machine C 47%.

**false-positive structure**
*line 344 · concept*

> Whenever the positive class is rare, even an excellent detector produces mostly false alarms. The math is structural — no amount of engineering can escape it without raising the base rate itself (screen higher-risk populations) or accepting lower sensitivity (miss more true positives to reduce false positives).

In plain words: When what you are looking for is rare, even an excellent detector's alarms are mostly false. The only ways out are raising the base rate or accepting lower sensitivity.

Example: Fraud detection, security alerts, medical screening, content moderation and jailbreak detection all share the structure.

**alert fatigue**
*line 346 · failure mode*

> Within a week or two they learn, in their bones, that the alarms do not mean anything. They start ignoring them. They miss the real one when it comes.

In plain words: What happens when a detector for a rare event raises so many false alarms that the people watching learn to ignore them, and then miss the real one. It follows from the false-positive structure, not from carelessness.

Example: The Epic Sepsis Model alerted on 18% of all hospitalized patients and clinicians reported alert fatigue.

**Epic Sepsis Model**
*line 348 · named result or case*

> The Epic Sepsis Model from Chapter 1 is this structure caught in the act: an external validation generated an alert on 18% of all hospitalized patients while sepsis is far rarer than that alert rate, so most of those alerts were false — and the model still missed sepsis in 67% of the patients who had it (sensitivity 33%) — exactly the base-rate arithmetic above, at hospital scale, generating the alert fatigue clinicians reported

In plain words: An external validation found a widely used sepsis alert fired on 18% of all hospitalized patients, far more than sepsis occurs, yet missed 67% of the patients who had sepsis. It is the base-rate arithmetic at hospital scale.

Example: Alert on 18% of patients, sensitivity 33%, clinicians reported alert fatigue.

**probabilistic claim**  *(also: decision under uncertainty)*
*line 372 · concept*

> The move I need you to make — and you will make it over and over for the rest of this book — is this: every model output is a probabilistic claim, and every decision based on a model output is a decision under uncertainty. The output is not a number. It is a probabilistic claim about what kind of input is in front of you, conditional on the model's implicit beliefs about the world.

In plain words: A model's output is not a plain fact but a claim that holds only on conditions: that training resembles this case, that the model is calibrated, and that no distribution shift has happened. Remove any condition and the number means something else, or nothing.

Example: A triage model's 0.87 for high acuity is conditional on the training distribution, good calibration and no shift.

Not to be confused with: a fact ("the function returned 42")

**early-pandemic imaging case**
*line 388 · named result or case*

> There is a documented case from the early pandemic. Models trained on pre-2020 medical imaging were deployed in 2021. The imaging signatures had been altered by COVID's effect on the lungs and on the population that ended up in scanners.

In plain words: Imaging models trained on pre-2020 data were deployed in 2021, after COVID changed the lungs and who got scanned. They kept producing confident predictions that no longer matched the disease distribution.

Example: Confident 2021 predictions that no longer matched the underlying disease distribution.

**detecting distribution shift**  *(also: drift)*
*line 396 · method*

> You will not, in general, be able to detect this kind of drift just by watching the model's outputs. The model continues to look confident through the shift; the shape of its outputs stays similar; the dashboards stay green. Detection requires watching the inputs, watching the outputs, and — most of all — watching the actual outcomes the model was supposed to predict, when those outcomes eventually become observable.

In plain words: A model looks equally confident while the world changes, so dashboards of its outputs stay green. You catch a shift by watching the inputs, the outputs and above all the real outcomes once they become observable.

Example: Most deployments do not budget for this and find out about distribution shift through the harm.

**overconfident**  *(also: overconfidence)*
*line 406 · failure mode*

> If only four hundred do, the model is overconfident — its stated number is bigger than it has any right to be. If nine hundred do, the model is underconfident.

In plain words: A model is overconfident when the probability it states is bigger than how often it is actually right. The chapter says modern deep networks are badly overconfident at the high end, and so are most people about their own beliefs.

Example: A net says 99% when it should say 85%; people's 90% intervals contain the answer only about half the time.

Not to be confused with: underconfident (the stated number is too small)

**underconfident**
*line 406 · failure mode*

> If nine hundred do, the model is underconfident.

In plain words: A model is underconfident when the probability it states is smaller than how often it is actually right.

Example: It says 70% on a thousand cases and nine hundred turn out positive.

Not to be confused with: overconfident (the stated number is too big)

**fluent overconfidence**  *(also: says it fluently)*
*line 413 · failure mode*

> The mathematics of how these models are trained — deep architectures, the softmax with cross-entropy loss, the tricks that improve raw accuracy — actively rewards extreme confidence even when the underlying decision is not really that confident. A net will say "99%" when it should say "85%," and it will say it fluently.

In plain words: A model stating 99% where 85% would be honest, and stating it smoothly so nothing in the delivery warns you. The chapter says the way deep networks are trained actively rewards extreme confidence.

Example: A net says 99% when it should say 85%.

**temperature scaling**
*line 415 · method*

> they also showed a cheap fix: temperature scaling. You take a single learned parameter $T$ and divide the pre-softmax logits $z$ by it before the softmax

In plain words: A cheap fix for an overconfident model: divide its raw pre-softmax scores by one learned number T, fit on held-out data, which softens its stated confidence without changing how it ranks cases. It repairs average calibration only on the distribution you fit it to and goes stale silently if the world drifts.

Example: It repairs a net that says 99% when it should say 85%, but not after distribution shift.

**confidence and correctness are separable**
*line 419 · concept*

> Temperature scaling fixes the number without touching the decision — which is direct evidence that the confidence and the correctness were separable all along.

In plain words: A model's stated confidence and whether it is right are different things: you can rescale the confidence without changing which cases it ranks highest. So a confident number is not evidence of correctness.

Example: Temperature scaling lowers a 99% to 85% without changing the model's ranking of cases.

**fluency**
*line 423 · concept*

> Without that prior specification you are reading the score with no criterion except how confident it sounds

In plain words: How confident and smooth an output sounds. The chapter's point is that this is not a criterion: sounding sure tells you nothing about whether a number is right.

Example: A net says 99% when it should say 85%, and says it fluently.

Not to be confused with: calibration (checking the stated number against what actually happens)

**fluency trap**
*line 423 · failure mode*

> how confident it sounds is exactly the fluency trap from Chapter 1, now operating on a number instead of a sentence.

In plain words: Taking how confident or smooth an output sounds as a sign that it is right. In this chapter the trap works on a number, such as a model's score, instead of on a sentence.

Example: Trusting a model's 0.94 because it looks clean and confident, without seeing its calibration curve.

Not to be confused with: calibration (the check that breaks the trap)

**falsification condition**  *(also: Popperian falsification condition)*
*line 423 · method*

> Here is the move I want you to internalize, and it is a Popperian one: do not trust a model's stated probability without seeing its calibration curve on data drawn from the actual deployment distribution. State the condition under which you would reject the number, then go look. The four diagnostic questions at the end of this chapter are falsification conditions in disguise.

In plain words: Before trusting a number, state the specific condition (metric, threshold, window) under which you would reject it, then go check. The chapter calls this a Popperian move.

Example: Exercise 16(d): name the condition under which a vendor's reported confidence would be false, and whether the source gives you enough to check it.

**four questions**  *(also: four diagnostic questions; diagnostic card)*
*line 509 · framework*

> These four questions, asked in the right order, would have prevented most of the deployment disasters I have watched unfold. We use all four on every system we analyze in the remaining chapters.

In plain words: The chapter's checklist for any model's number, asked in this order: what is the base rate, is the model calibrated on deployment data, what is the cost distribution, and what changed since training.

Example: Exercise 11: ask a vendor with a 94% accuracy figure what you would need from them to answer each of the four.

**calibration baseline**
*line 488 · method*

> You are given a set of forecasting questions across several domains — some technical, some general. For each question, provide a 90% confidence interval for the answer. After the truth is revealed, compute the fraction of your intervals that contained the true value.

In plain words: An exercise that tests your own calibration: give 90% confidence intervals for forecasting questions, then check what fraction contained the truth, which should be 0.9 if you are well-calibrated. Most engineers score between 0.4 and 0.6 on the first try.

Example: 14 of 20 intervals contained the answer (Exercise 8) is 0.7, so you are overconfident.

**locked prediction**  *(also: prediction-lock; lock your prediction)*
*line 432 · method*

> Lock your prediction before plotting: do you expect the curve to track the diagonal, sag below it, or rise above it? Where on the x-axis do you expect the curve to peel off? Write it down; you cannot revise it.

In plain words: Write down what you expect to see before you run the analysis, and do not change it afterwards, so the gap between your prediction and the result is what you learn from.

Example: Before plotting a calibration curve, record whether you expect it to track the diagonal, sag below it, or rise above it.

**finite variance**
*line 450 · concept*

> The theorem has two requirements buried in it. Independent. And finite variance.

In plain words: One of the Central Limit Theorem's two requirements. It breaks down in heavy-tailed distributions, where extreme events are not rare enough for averaging to dampen them.

Example: Glimmer 2.2: apply an analysis tool that assumes finite variance to Cauchy-distributed data and watch it produce nonsense.

**power-law distributions**
*line 454 · concept*

> Power-law distributions are common in real systems: wealth, file sizes, network connection counts, earthquake magnitudes, training-loss spikes during model fitting, and the cost of a deployed AI system being wrong about a single decision.

In plain words: A family of distributions found widely in real systems, where the heavy-tail problem shows up. The chapter lists wealth, file sizes, earthquake magnitudes and the cost of an AI system being wrong.

Example: The cost of a deployed AI system being wrong about a single decision.

**average-loss metrics**  *(also: average loss)*
*line 465 · failure mode*

> If most of your wrong outputs are minor inconveniences but one in a thousand kills a patient or wipes a database — your loss distribution is heavy-tailed, and a deployment evaluated on average loss is being evaluated on a quantity that does not converge in any useful sense.

In plain words: Judging a system by its average cost of error misleads when losses are heavy-tailed, because the average does not settle down. The rare catastrophe is the only loss that matters.

Example: A security-alert system's average false-positive and false-negative rates look small, yet one false negative costs $500,000 (Exercise 10).

Not to be confused with: tail-aware metrics

**tail-aware metrics**  *(also: worst-case analysis)*
*line 465 · method*

> You need tail-aware metrics. You need worst-case analysis. You need to design adversarial inputs deliberately, so the rare catastrophes show up in testing instead of in production.

In plain words: Ways of judging a system by its rare worst outcomes instead of its average, including worst-case analysis and deliberately designed adversarial inputs, so catastrophes show up in testing.

Example: The triage system's average loss was tiny, but the catastrophic losses were the only ones that mattered.

Not to be confused with: average-loss metrics

**triage system case**
*line 467 · named result or case*

> The average loss across deployments was tiny. The catastrophic loss was the only one that mattered. The system had been validated on average-loss metrics, and the validation came back beautiful.

In plain words: A triage system from Chapter 1 operated in a heavy-tailed loss world: most low-acuity classifications were right or close, a few were catastrophic. Its validation on average loss looked beautiful and was irrelevant to the question that should have been asked.

Example: Average loss tiny, catastrophic loss decisive.

**accuracy versus loss**  *(also: accurate on average, catastrophic in the tail)*
*line 467 · concept*

> That system was operating in a heavy-tailed loss world. Most of its low-acuity classifications were correct or close to correct. A few were catastrophic.

In plain words: How often a system is right (accuracy) and how much its errors cost (loss) are different questions: a system can be right nearly every time and still be judged by a handful of catastrophic errors. Evaluating it on average loss or accuracy hides those errors.

Example: The triage system's classifications were mostly right and its validation looked beautiful, but the rare catastrophic ones were the only losses that mattered; likewise Exercise 10's alert system has small error rates but a $500,000 false negative.

Not to be confused with: accuracy and average loss (each can look excellent while the rare catastrophic error goes unseen; Exercise 11's 94% accuracy figure says nothing about the cost distribution)

**Cauchy distribution**  *(also: Cauchy break)*
*line 473 · named result or case*

> Then run the same simulation from a Cauchy distribution. Lock your prediction of where the Cauchy mean settles. Watch it not settle.

In plain words: A heavy-tailed distribution the chapter's exercises use to show averaging failing: the mean of Cauchy samples never settles however many you collect.

Example: Glimmer 2.1: sample means from a Gaussian converge; sample means from a Cauchy never do.

Not to be confused with: Gaussian (bell-curve) distribution

**positive predictive value**
*line 477 · metric*

> Take the disease example from this chapter. Vary the base rate from 1/100 to 1/100,000. Plot positive predictive value as a function of base rate.

In plain words: In Glimmer 2.3 it is the quantity you plot against the base rate for the disease example. In the chapter's example it is the share of positive results that truly have the disease, about 1 in 101.

Example: Glimmer 2.3: predict where the curve crosses 50% before you plot it.

Not to be confused with: sensitivity (the 99% figure people mistake for it)

**assume heavy tails when harm to people is possible**
*line 520 · method*

> Tail estimation from a sample is mathematically impolite. The honest answer is: assume heavy tails when the cost-of-error includes harm to people, and engineer accordingly. That is a heuristic, not a calculation, and I have not solved this.

In plain words: You cannot reliably estimate tails from a sample before a catastrophe reveals them, so the chapter's rule of thumb is to assume heavy tails whenever errors can harm people and design accordingly. It is a heuristic, not a calculation.

Example: A deployment whose wrong outputs can kill a patient.

**audit**  *(also: AUDIT; audit someone else's confident number)*
*line 572 · method*

> Then run the audit: (a) find the base rate — what fraction of the population actually has the positive class, from a primary source or a named assumption; (b) run Bayes on the flag — given the reported accuracy (or sensitivity/specificity, if you can get both) and the base rate, compute what fraction of everything the system flags is genuinely positive, showing the arithmetic; (c) name the missing number — the quantity the source did not report that you needed, usually the base rate, the specificity, or the calibration curve on the deployment distribution; (d) write the Popperian falsification condition — the specific condition (metric, threshold, window) under which the reported confidence would be false, and whether the source gives you enough to check it.

In plain words: The four-step check on someone else's confident number: find the base rate, run Bayes on the flag, name the missing number, and write the falsification condition. If the number turns out decorative, name which of the four diagnostic questions best explains it.

Example: Audit a vendor's fraud detector or a paper's headline accuracy, or the Epic Sepsis Model.

**Bayes on "task complete"**
*line 611 · method*

> If the prior is high (the agent usually succeeds), the posterior will be near 1 even if false-positive rate is moderate. If the prior is low (the task is the kind the agent often fails — novel, edge case, multi-step) the posterior may be substantially below 1 even when false-positive rate looks small.

In plain words: Turning an agent's "task complete" report into the probability the task really finished, using a prior for how often such tasks succeed plus the chance the agent says "complete" when it succeeded versus when it failed. The same report is worth far less on a hard edge-case task than on a typical one.

Example: Show the arithmetic for a typical task and an edge-case task, and say whether to trust a "complete" report from each.

**base-rate inventory**
*line 614 · method*

> For my agent's most consequential failure modes (drawn from the System Dossier), estimate base rates from primary sources. For each: what is the documented or estimated frequency in published evaluations? If unknown, that itself is a finding — name what evaluation would have to be run to know.

In plain words: A list of how often your agent's most serious failures happen, taken from primary sources. If the frequency is unknown, that is itself a finding, and you name the evaluation needed to learn it.

Example: Documented frequency of a failure mode in published evaluations, or "unknown; this evaluation would settle it."

**calibration plan**
*line 618 · method*

> Which agent outputs carry an explicit or implied confidence claim ("I have deleted X" is implied 100% confidence; some agents output explicit probabilities)?

In plain words: Deciding in advance how to collect calibration data on an agent: which outputs carry a confidence claim, what the ground truth is and how to observe it independently of the agent's report, and a log format that can later build a reliability diagram.

Example: "I have deleted X" is an implied 100% confidence claim.

**ECE**
*line 633 · metric*

> Chapter 11 will use the calibration plan to compute Brier and ECE.

In plain words: A calibration score named in the LLM exercise: Chapter 11 will compute it, together with the Brier score, from the calibration data your plan collects. This chapter does not define it or spell out the name.

Example: The calibration plan's log of stated confidence against ground truth is what Chapter 11 will score.

Not to be confused with: calibration curve (a picture of the same match between stated and actual)

## Chapter 3, Data Validation (79 terms)

**procedural EDA**  *(also: EDA; exploratory data analysis; the procedural pass)*
*line 29 · method*

> EDA is not a procedure. Or rather: EDA includes a procedure, and the procedure is fine, and you should run it. But the procedure is not the work.

In plain words: The standard routine for checking a dataset: histograms, missing-value counts, correlations, outlier flags and summary statistics. The chapter says you should run it, but it is necessary and not sufficient, because it only reads the data as written.

Example: A report with the histograms drawn, missingness near zero and no wild outliers that still missed rows dropped in a join.

Not to be confused with: interrogation

**clean of the things histograms can see**  *(also: clean report read as clean data; a dataset clean of the things histograms can see)*
*line 198 · failure mode*

> You need both, and the mistake — the one that has done real harm — is running the fast one, seeing it come back clean, and concluding the data is clean, when what you actually have is a dataset clean of the things histograms can see.

In plain words: The mistake of running the fast checks, seeing a clean report, and concluding the data itself is clean. All the report shows is that nothing looks wrong to diagnostics that read the data as written.

Example: In the opening case the EDA report had every plot and a clean missing-values check, yet a whole subpopulation was absent.

Not to be confused with: evidence of understanding (what the interrogation produces)

**silent join failure**  *(also: silent-join pathology; join drop; four-percent drop rate)*
*line 18 · failure mode*

> The join had a four-percent drop rate — rows that didn't match across all three sources got silently excluded. Four percent doesn't sound like a lot, and if it had been spread evenly across the population, it wouldn't have been. But it wasn't spread evenly.

In plain words: A join between source tables that quietly throws away rows that do not match on the identifier, with no error. If the lost rows come from one subpopulation, the data silently lacks that group.

Example: Rows from one subpopulation with inconsistently formatted identifiers in one source system disproportionately failed the join and never reached the training set.

Not to be confused with: missing values (the dropped rows are not 'missing' in any sense the EDA can register)

**feature-engineering assumption**  *(also: calculated composite; somebody else's model output wearing the costume of raw data)*
*line 128 · failure mode*

> The calculation has parameters chosen by a human who is probably no longer at the company. You inherit the column and treat it like data, but it is not data. It is somebody's model, baked into your input layer — and when their assumptions break, so do yours.

In plain words: The risk that an input column is not a raw measurement but a calculation or an upstream model's output, so it carries someone else's assumptions. It looks like data and has no missing values, so its provenance is invisible unless someone documented it.

Example: customer_lifetime_value encodes someone's old model's assumptions; when those break, so does a new model trained on it.

Not to be confused with: raw measurement

**why are there exactly N rows?**  *(also: the row-count question; residue of a process)*
*line 25 · method*

> Why are there exactly N rows in this dataset? What was N supposed to be? What is the difference between what was supposed to be there and what is?

In plain words: The question the chapter says opens validation: why does the dataset have this many rows, and how many should it have had? The row count is the leftover of a process (joins, filters), not a fact about the world, so the gap between expected and actual is the first thing to explain.

Example: The documentation says 85,000 CRM records but the merged table has 79,400 rows (Exercise 1).

**fluent, plausible story**  *(also: plausible story)*
*line 12 · concept*

> I'll flag it up front as a composite — built from silent-join pathologies I've watched play out more than once, not a single sourced incident — because a book about distrusting fluent, plausible stories cannot open with a fluent, plausible story it asks you to swallow whole.

In plain words: An account that reads smoothly and sounds believable, which is exactly why the book will not ask you to accept one whole. The author labels the opening case a composite for this reason.

Example: The join-drop case is flagged as a composite built from patterns the author has seen, not a single sourced incident.

**join-drop deployment case**  *(also: the dataset that destroyed a deployment; composite case)*
*line 18 · named result or case*

> The training set was systematically missing them. The model, trained on what was present, performed beautifully on what was present. Deployed against the full population, it performed predictably worse on the subpopulation it had never seen.

In plain words: An illustrative composite case, not a cited incident: a dataset joined from three systems silently lost 4% of rows, mostly from one subpopulation, so the model looked good on its training data and then did worse on that group in deployment. The team blamed the model and kept retraining; the fault was in the data, and the failures were soft, not crashes.

Example: Retraining, tuning and trying different architectures did not help because the problem was the missing rows, not the model.

**what EDA cannot see**  *(also: blind spot of procedural EDA; what was never written; what the EDA could not look at)*
*line 85 · concept*

> Every diagnostic reads the data as written, and every one of them has the same blind spot underneath its specific one: none can see what was never written. The pass cannot see rows dropped in a join before the dataset reached me. It cannot see the gap between a label and the construct it claims to measure.

In plain words: Every EDA check reads only the data as it was written, so none can see rows dropped before the data arrived, the gap between a label and what it claims to measure, a feature that is someone's model output, or who could not generate a record at all. The chapter says these are structural properties of what EDA is, not tool failures.

Example: Rows that failed the join were not 'missing' to the EDA; they simply were not there.

**population**  *(also: the full population; the population the model is going to be deployed against)*
*line 18 · concept*

> The model, trained on what was present, performed beautifully on what was present. Deployed against the full population, it performed predictably worse on the subpopulation it had never seen.

In plain words: The whole group the model will actually be used on, including parts that never made it into the data you trained on. A model can look excellent on the records it saw and still do worse on the population it is deployed against.

Example: In the join-drop case the model did well on the rows present but worse on the full population, because one subpopulation's rows had been dropped.

Not to be confused with: sample

**subpopulation**  *(also: subpopulations)*
*line 18 · concept*

> One specific subpopulation had inconsistent identifier formatting in one of the three source systems — a field entered slightly differently by the people who originally maintained that system years ago.

In plain words: A distinct group within the larger population, such as the customers whose identifiers were formatted differently in one source system. If the data loses a subpopulation, a model can fail on exactly that group while looking fine overall.

Example: The subpopulation with inconsistent identifier formatting disproportionately failed the join and was missing from the training set.

Not to be confused with: population

**interrogation**  *(also: the interrogation approach; interrogate the frame)*
*line 29 · method*

> But the procedure is not the work. The work is interrogation. The dataset is being interviewed by a skeptical reader who wants to know what the recording instrument was, who deployed it, what it could see and what it couldn't see, and what choices were made before any data was written down.

In plain words: Skeptically questioning a dataset about how it was made: what the recording instrument was, who deployed it, what it could and could not see, and what choices came before any data was written. The chapter treats this, not the plots, as the real work of validation.

Example: Asking why there are exactly N rows and tracing where the missing rows went.

Not to be confused with: procedural EDA

**Plato's Cave**
*line 31 · framework*

> It is shadows on the wall — a projection cast by a particular recording instrument under particular conditions. Procedural EDA describes the shadows with great precision. It tells you nothing about the fire, the objects, or the wall.

In plain words: The chapter's picture of data: a dataset is not the world but shadows cast on a wall by a particular instrument under particular conditions. Plots describe the shadows precisely and say nothing about what cast them, so interrogation is the work of turning around.

Example: Procedural EDA describes the shadows precisely while saying nothing about the fire, the objects or the wall.

**dataset as a recording**  *(also: recording instrument; a recording made by a particular instrument)*
*line 33 · concept*

> Treat every dataset as a recording made by a particular instrument under particular conditions. Then ask the questions you would ask of any recording.

In plain words: Treat a dataset like any recording: ask what was recorded, what was not, why, by whom, and under what assumptions about what was worth recording. The data shows only what the instrument could see.

Example: In the opening case the instrument was three source systems, one of which had formatted a shared identifier slightly differently.

**epistemic frame**  *(also: the frame; frame of the dataset)*
*line 39 · concept*

> Before the model, there is data. Before the data, there are choices — about what to record, what to include, how to join, where to stop. Those choices are the epistemic frame of the dataset, and they are almost never written down.

In plain words: The set of choices made before and while a dataset was built: what to record, what to include, how to join, where to stop. They are almost never written down, so you have to reconstruct them.

Example: A join that quietly drops rows and dtypes that were inferred rather than verified (the opening scenario).

**computational skepticism**  *(also: plausible artifacts; machine speed, your doubt)*
*line 41 · framework*

> This is where computational skepticism does its most characteristic work — the pairing Chapter 1 committed us to: the machine's speed at producing plausible artifacts, your doubt about what they are evidence of. An AI can assemble the dataset, join the tables, draw every histogram, and write the "the data is clean" paragraph faster than you ever could. What it cannot supply is the doubt about what the histograms can't reach.

In plain words: The pairing the book rests on: the machine quickly produces plausible artifacts (tables, plots, a 'the data is clean' paragraph) and you supply the doubt about what they are evidence of. The AI cannot supply the doubt about what the histograms cannot reach.

Example: An AI writing the 'the data is clean' paragraph faster than you could, with every histogram drawn.

**Problem Formulation**  *(also: supervisory capacity)*
*line 43 · framework*

> Problem Formulation — deciding what this dataset is even supposed to represent before you look at it — and Plausibility Auditing — hearing the wrong note in a report that looks, by every visible measure, clean. The AI is superhuman at producing the plots. It cannot own either of those capacities for you.

In plain words: One of the five supervisory capacities from Chapter 1: deciding, before you look at the data, what the dataset is supposed to represent. The AI cannot do this for you.

Example: Deciding what the merged customer table is meant to represent before running any histogram.

Not to be confused with: Plausibility Auditing

**Plausibility Auditing**  *(also: supervisory capacity)*
*line 43 · framework*

> Problem Formulation — deciding what this dataset is even supposed to represent before you look at it — and Plausibility Auditing — hearing the wrong note in a report that looks, by every visible measure, clean. The AI is superhuman at producing the plots. It cannot own either of those capacities for you.

In plain words: Another of the five supervisory capacities from Chapter 1: hearing the wrong note in a report that looks clean by every visible measure. It is the human check on a polished, plausible-looking result.

Example: Doubting an EDA report that shows reasonable distributions, near-zero missingness and no wild outliers.

Not to be confused with: Problem Formulation

**six structural assumption categories**  *(also: the six failures; hidden assumptions; structural failure modes)*
*line 118 · framework*

> The six failures. Each has a structural reason it evades EDA. Memorizing the list matters less than being able to ask, for each column: why is this value here, and what is it not telling me?

In plain words: The chapter's table of assumptions that fail silently and that procedural EDA cannot see: sampling, time-window, label, missing not at random, feature-engineering and access/boundary. For each column, ask why the value is here and what it is not telling you.

Example: A model trained on a 2019 dataset and deployed in 2022 (time-window assumption).

**access/boundary assumption**  *(also: access assumption; effective scope; boundary of the data)*
*line 150 · failure mode*

> This is a data-validation failure. The team thought they were validating the corpus. What they should have been validating was the corpus and everything the corpus's contents reference.

In plain words: The assumption that a dataset ends at its schema, when its effective data universe extends through references, links or embedded content. EDA validates the records present and cannot follow references to data outside the schema.

Example: An agent given an email corpus implicitly has access to everything the emails reference or quote.

**prediction-lock**  *(also: lock your prediction)*
*line 170 · method*

> Write down, in your own words, what you predict the dataset's epistemic frame to be — what it claims to represent, how it was collected, what is excluded, and over what time period. Lock your prediction. The whole exercise depends on this.

In plain words: Before running any analysis on a dataset you did not create, write down what you predict its epistemic frame to be and do not change it. Without the locked prediction there is no gap to measure afterwards, and what you arrive at feels obvious in retrospect.

Example: Predicting a year of records, then finding the row count fits about nine months.

**six-step epistemic-frame reconstruction**  *(also: epistemic-frame reconstruction; six-step procedure; six-step interrogation procedure)*
*line 165 · method*

> If you take what I have argued seriously, the procedure for validation changes. Not the procedural EDA — that part is fine, run it as you have always run it. The interrogation is what changes.

In plain words: A six-step working procedure: read the metadata and lock a prediction, run procedural EDA, test the metadata against the data, ask what is not in the data, trace a row end to end, then write the frame and compare it to your prediction. Steps 3 to 6 are the work EDA alone does not do.

Example: Applying the six steps to a public dataset and recording, for each step, what you predicted, what you found and the gap (Exercise 9).

Not to be confused with: procedural EDA

**strategic delegation**  *(also: three buckets of validation work)*
*line 188 · framework*

> Now, you may be wondering: can I have an AI do some of this? You can, and you should — but only some of it, and the line matters.

In plain words: Sorting validation work into three buckets: delegate freely, verify before trusting, and do not delegate at all. The chapter says the line is about what the work produces, not about AI capability.

Example: An AI can run the histograms, but it cannot reconstruct the epistemic frame for you.

**types first**  *(also: column type classification)*
*line 57 · method*

> Types first. Before drawing anything, I classify every column, because the right diagnostic depends entirely on the type. Continuous numeric (salary, temperature, a confidence score) has meaningful distributions, means, histograms.

In plain words: Before plotting, label each column as continuous numeric, small-range discrete count, categorical nominal (frequencies, no order), ordinal (an order you must not scramble), temporal or text. The right diagnostic depends on the type, and the first errors live in the classification.

Example: zip_code looks numeric but arithmetic on it is meaningless.

**categorical column treated as numeric**
*line 57 · failure mode*

> The classification is not always obvious and that is where the first errors live: `zip_code` looks numeric but arithmetic on it is meaningless, and a column called `score` might be a raw measurement or somebody's calculated composite. The most dangerous mistake here is treating a categorical column as numeric. Read the schema before you classify.

In plain words: Doing arithmetic or numeric summaries on a column whose values are really labels, such as zip codes. The chapter calls it the most dangerous mistake in typing columns.

Example: Averaging zip codes.

**shape check**  *(also: Shape; .describe())*
*line 59 · method*

> How many rows, how many columns, and do the inferred types match what the documentation claims? A column that should be numeric but reads as string — usually because it carries a sentinel like `"N/A"` — is one of the most common early warnings. The `.describe()` table (count, mean, std, min, quartiles, max) is worth scanning before any plot: does the minimum make sense, does the maximum, is the mean far from the median in a way that signals skew or outliers?

In plain words: The first diagnostic: count the rows and columns, check that the inferred types match the documentation, and scan the .describe() table for sensible minimums and maximums and a mean far from the median. It tells you what the row count is, not whether it is right.

Example: A column that should be numeric but reads as string because it carries a sentinel like "N/A".

**sentinel value**  *(also: sentinel)*
*line 59 · concept*

> A column that should be numeric but reads as string — usually because it carries a sentinel like `"N/A"` — is one of the most common early warnings.

In plain words: A placeholder value such as "N/A" that stands in for unknown or missing. It can make a numeric column read as text, or show up as a spike at one value in a histogram.

Example: A $1,200,000 salary could be a legitimate CEO or a sentinel for "unknown".

**univariate distributions**  *(also: histogram; bar chart sorted by frequency; distribution shape)*
*line 61 · method*

> A histogram bins a numeric column and shows its shape: symmetric, skewed, bimodal (two humps, often two subpopulations), or spiked at one value (often a sentinel or imputed default). A bar chart sorted by frequency does the same for categorical data and makes rare categories jump out. A box plot compresses the summary — median, interquartile range, whiskers, outlier dots — into a small footprint so I can line many columns up side by side.

In plain words: Looking at one column at a time: a histogram for numeric data (symmetric, skewed, bimodal meaning two humps, or spiked at one value) and a sorted bar chart for categories. You hunt for spikes at round numbers, impossible values and humps the documentation never mentioned, but the plot cannot show why the shape is what it is.

Example: A spike at one value that turns out to be a sentinel or imputed default; negative ages or superhuman salaries.

**box plot**
*line 61 · concept*

> A box plot compresses the summary — median, interquartile range, whiskers, outlier dots — into a small footprint so I can line many columns up side by side.

In plain words: A compact plot showing the median, the interquartile range, whiskers and outlier dots for a column. Its small size lets you line many columns up side by side.

Example: A single "salary" column drawn as a box plot with its whiskers and outlier dots (Figure 3.5).

Not to be confused with: histogram

**Rubin's taxonomy of missing data**  *(also: missing-data taxonomy; MCAR/MAR/MNAR)*
*line 63 · framework*

> Missing data is not one thing, and Rubin's 1976 taxonomy is the frame worth stating precisely. Missing completely at random (MCAR) — a sensor randomly dropping readings — is independent of everything and safe to impute. Missing at random (MAR) depends on other observed variables but not the missing value itself: younger respondents skip the income question more often, but conditional on age the missingness is random.

In plain words: A way to sort missing data by why it is missing: completely at random, at random given other columns you can see, or not at random (depending on the missing value itself). The type decides whether imputation is safe.

Example: A sensor randomly dropping readings versus high earners suppressing their income.

**missing completely at random (MCAR)**  *(also: MCAR)*
*line 63 · concept*

> Missing completely at random (MCAR) — a sensor randomly dropping readings — is independent of everything and safe to impute.

In plain words: Data that goes missing purely by chance, unrelated to anything in the dataset. Because nothing drives the gaps, it is safe to fill them in (impute).

Example: A sensor randomly dropping readings.

Not to be confused with: missing at random (MAR)

**missing at random (MAR)**  *(also: MAR)*
*line 63 · concept*

> Missing at random (MAR) depends on other observed variables but not the missing value itself: younger respondents skip the income question more often, but conditional on age the missingness is random.

In plain words: Data that goes missing for reasons tied to other columns you can see, not to the missing value itself. Once you account for those visible columns, what is left is random.

Example: Younger respondents skip the income question more often, but within an age group the skipping is random.

Not to be confused with: missing not at random (MNAR)

**missing not at random (MNAR)**  *(also: MNAR; missing-data assumption)*
*line 63 · failure mode*

> Missing not at random (MNAR) depends on the missing value itself — high earners suppress their income, sick patients leave the study before the final measurement — and it is the hard case, because standard imputation produces bias in exactly the direction I cannot measure.

In plain words: Data that goes missing because of the value itself, such as high earners not reporting their income. It is the hard case: standard imputation biases the result in a direction you cannot measure, and procedural EDA cannot detect it, so you must reason about who would not report the value and why.

Example: High earners suppress their income; survival data misses the patients who died.

Not to be confused with: missing at random (MAR)

**imputation**  *(also: impute; imputed default)*
*line 63 · method*

> Missing not at random (MNAR) depends on the missing value itself — high earners suppress their income, sick patients leave the study before the final measurement — and it is the hard case, because standard imputation produces bias in exactly the direction I cannot measure.

In plain words: Filling in a missing value with an estimate. The chapter says it is safe when data is missing completely at random but produces bias in an unmeasurable direction when data is missing not at random.

Example: Imputing missing incomes when high earners are the ones who suppress them.

**missingno matrix**  *(also: co-missing pattern)*
*line 63 · method*

> And here is the trade-off the tooling hides: a `missingno` matrix (rows as lines, columns as stripes, dark where absent) shows me whether two columns go missing together, which is a real and useful structural signal. But seeing the co-missing pattern is not knowing the mechanism. Procedural EDA does not detect MNAR at all.

In plain words: A plot with a stripe per column, dark where values are absent, that shows whether columns go missing together; aligned stripes suggest a structural pattern and scattered dots look random. Seeing the pattern does not tell you why the values are missing.

Example: Income missingness co-occurring with the age < 25 subgroup (Exercise 8).

**bivariate relationships**  *(also: scatter plot; pair plot)*
*line 70 · method*

> A single distribution tells me about one column alone; plotting two together catches problems invisible from either margin — a relationship that should exist and doesn't, or shouldn't and does. A scatter plot puts one row per point, each variable on its own axis (add transparency when ten thousand points overplot into a blob).

In plain words: Plotting two columns together to catch problems no single-column plot can show, such as a relationship that should exist and does not, or the reverse. Scatter plots and pair plots do this, but none can show a relationship the recording instrument never let into the data.

Example: A cluster of 40 points near age zero in a 10,000-row dataset that the age histogram did not flag (Figure 3.3).

**Pearson correlation (linear only)**  *(also: linear association)*
*line 70 · concept*

> A correlation heatmap gives a high-level view of pairwise linear association across numeric columns — but the load-bearing caveat is that Pearson correlation captures only linear structure. Two variables can be perfectly dependent ($y = x^2$) and correlate near zero.

In plain words: Pearson correlation measures only straight-line association, so two variables can depend on each other perfectly and still show a correlation near zero. A low correlation therefore does not mean no relationship.

Example: y = x^2 is perfectly dependent yet correlates near zero.

**correlation heatmap**
*line 93 · concept*

> A correlation heatmap encodes strength as color intensity, a weak channel, which is exactly why it is an overview tool: fine for spotting an extreme correlation, unreliable for deciding whether 0.43 differs from 0.51, and a value you should confirm numerically before you act on it.

In plain words: A grid showing pairwise correlation across numeric columns, with strength drawn as color intensity, which people read poorly. Use it to spot extreme correlations and confirm any value numerically before acting.

Example: Two column pairs with correlations above 0.85 do not by themselves justify dropping a column (Exercise 5).

Not to be confused with: scatter plot

**temporal patterns**  *(also: record counts over time)*
*line 75 · method*

> If there is a date column, I plot record counts over time first. This surfaces periods with too few records (a source system down, a batch job failed, a methodology changed), sudden distribution shifts, and seasonality. A sharp drop is always a finding — sometimes benign (a holiday), sometimes critical (the system was down and the subpopulation it served is now underrepresented).

In plain words: Plotting the number of records per time period to find gaps, shifts and seasonality. A sharp drop is always a finding, but the plot cannot tell you whether the cause is harmless or critical.

Example: A drop that lines up with a pandemic, system migration or policy change may mean a subpopulation is missing from the training set (Figure 3.4).

**distribution shift**  *(also: the shift; patterns that have shifted)*
*line 122 · concept*

> AI deployments routinely train on historical data and deploy in a present that has shifted. The shift can be invisible if you're not watching for it.

In plain words: A change in what the data looks like, either partway through the recorded period or between the training period and deployment. The chapter says it can be invisible if you are not watching for it.

Example: A model trained on 2019 data and deployed in 2022 confidently predicts patterns that have shifted.

Not to be confused with: time-window assumption

**IQR rule**  *(also: interquartile range rule)*
*line 80 · method*

> The histogram and box plot surface the obvious ones; formal detection uses the IQR rule (a value below $Q_1 - 1.5 \times IQR$ or above $Q_3 + 1.5 \times IQR$, the same criterion the box-plot whiskers draw, robust because the IQR itself is not moved by extremes) or the Z-score rule ($|z| > 3$, which is less reliable precisely because outliers contaminate the mean and standard deviation it depends on).

In plain words: A rule that flags a value as an outlier if it lies more than 1.5 times the interquartile range below the first quartile or above the third. It matches the box-plot whiskers and is robust because the IQR is not moved by extreme values.

Example: A $1,200,000 salary flagged by the rule.

Not to be confused with: Z-score rule

**Z-score rule**  *(also: |z| > 3)*
*line 80 · method*

> The histogram and box plot surface the obvious ones; formal detection uses the IQR rule (a value below $Q_1 - 1.5 \times IQR$ or above $Q_3 + 1.5 \times IQR$, the same criterion the box-plot whiskers draw, robust because the IQR itself is not moved by extremes) or the Z-score rule ($|z| > 3$, which is less reliable precisely because outliers contaminate the mean and standard deviation it depends on).

In plain words: A rule that flags a value as an outlier if its z-score is beyond 3 in absolute value. It is less reliable because outliers distort the mean and standard deviation it depends on.

Not to be confused with: IQR rule

**outlier**  *(also: outlier triage; outlier detection is triage, not removal)*
*line 80 · concept*

> But the detection is the easy half. Every flagged value needs a decision the method cannot make: is a $1,200,000 salary a decimal-point error, a legitimate CEO, or a sentinel for "unknown"? IQR flags the candidate; only domain knowledge makes the call about whether to remove, impute, cap, or keep it.

In plain words: An unusually extreme value that a rule flags as a candidate. The rule only flags it; domain knowledge decides whether to remove, impute, cap or keep it.

Example: A $1,200,000 salary could be a decimal-point error, a legitimate CEO, or a sentinel for "unknown".

**marks and channels**  *(also: marks-and-channels framework; visual channels; marks + channels)*
*line 91 · framework*

> Every visualization encodes numbers by assigning them to visual channels — the position of a point, the length of a bar, the intensity of a color, the size of a circle — and the channels are not interchangeable.

In plain words: A way to read any chart: it is built from marks (the dots or bars drawn) and channels (the visual feature carrying each number, such as position, length, color intensity or size). Channels are not interchangeable, so you check whether each variable sits on a suitable one.

Example: A scatter plot with age and salary on position and department on dot color (Exercise 4).

**channel ranking (position over color)**  *(also: Cleveland and McGill; position outranks color)*
*line 91 · named result or case*

> Cleveland and McGill established this empirically, not as taste: people read position along a common scale most accurately, then length, with area and color intensity well down the list.

In plain words: Cleveland and McGill's empirical finding that people judge position along a common scale most accurately, then length, and judge area and color intensity worse. That is why position, not color, carries quantitative data.

Example: Scatter plots and histograms read true because they put the quantity on position and length.

**a chart is an argument**  *(also: chart is never a neutral window)*
*line 93 · concept*

> Which means a chart is never a neutral window onto the data. It is an argument made through structural choices about what gets the strong channel and what gets buried — and a plot can be technically honest and still steer you, simply by encoding the thing that matters on a channel you read badly.

In plain words: A chart is never a neutral view of the data: choosing what gets the strong channel and what gets buried steers the reader. A plot can be technically honest and still mislead by putting the important variable on a channel people read badly.

Example: A correlation heatmap makes 0.43 and 0.51 hard to tell apart because strength sits on color intensity.

**what is the chart not showing?**
*line 101 · method*

> I keep only one question from this whole literature, and it is the one that hands off to the rest of the chapter: what is the chart not showing? Every plot encodes some variables and silently omits the rest. A salary histogram says nothing about who earned those salaries.

In plain words: The one question to ask of every chart: what does it leave out? Every plot encodes some variables and silently omits the rest, and it can never show what the recording instrument left out.

Example: A correlation heatmap says nothing about the temporal structure underneath the relationships.

**sampling assumption**
*line 120 · failure mode*

> Was this sample drawn from the population the model is going to be deployed against? Often, no. The sample is available data — meaning the data that was easiest to collect, which means it skews toward the easy-to-reach end of every distribution it was drawn from.

In plain words: The assumption that the training sample came from the population the model will be deployed against, when it usually came from a more accessible subpopulation. EDA sees only what is present and cannot compare it to the absent target population.

Example: A model performs well on easy-to-reach customers but degrades on the long tail it was never trained on.

**target population**  *(also: deployment target; the population the model is going to be deployed against)*
*line 111 · concept*

> EDA only sees what is present; it cannot compare the present data to the absent target population

In plain words: The group the model will actually be used on, which the training data is supposed to stand for. EDA cannot check the data against it, because EDA only sees the rows that are present and the target population is partly absent.

Example: A model trained on easy-to-reach customers must still handle the long tail of customers who were never in the training data.

Not to be confused with: sample

**time-window assumption**
*line 122 · failure mode*

> What time period does the data cover? Is the deployment going to run in the same period? Almost never.

In plain words: The assumption that the period the training data covers still matches the period the model will run in. It usually does not, and EDA has no knowledge of what was true outside the dataset's time range.

Example: A model trained on 2019 data, deployed in 2022, confidently predicts patterns that have shifted.

Not to be confused with: distribution shift

**label assumption**  *(also: operational proxy)*
*line 124 · failure mode*

> The label and the construct you actually care about are usually different things, connected by a chain of operational decisions that somebody made long ago and didn't write down. This is Hume's induction problem in work clothes — you are inferring the construct from a proxy that happened to correlate in the recorded past, and the correlation carries no guarantee forward.

In plain words: The assumption that a label column measures what you care about, when it really measures an operational proxy. The two are linked only by decisions someone made long ago and did not write down.

Example: Re-arrest rate predicts re-arrest, not crime; click-through rate predicts clicks, not interest.

Not to be confused with: construct (what you actually care about)

**sample**  *(also: the sample; available data; training data)*
*line 130 · concept*

> There is the sampling assumption in its sharpest form: your sample is available data, which means it skews toward the easy-to-reach end of every distribution it was drawn from. You train on the convenience sample and deploy against the world, and the world is wider.

In plain words: The records you actually have and train on, which is only the part of the population that was collected. It is available data, so it skews toward the easy-to-reach end of every distribution it was drawn from.

Example: The merged table that excluded rows failing the join is the sample; the full customer population includes the rows that never arrived.

Not to be confused with: population

**representative sample**  *(also: representativeness; sample drawn from the population the model is going to be deployed against)*
*line 120 · concept*

> Was this sample drawn from the population the model is going to be deployed against? Often, no.

In plain words: A sample is representative when it was drawn from, and so matches, the population the model will be deployed against, instead of skewing toward the easy-to-reach end. The chapter does not use the word 'representative'; its test is the question quoted here, and its usual answer is no.

Example: A sample that leaves out a subpopulation, or covers only customers who completed onboarding when deployment includes those who abandoned it, is not representative of the deployment population.

Not to be confused with: convenience sample

**convenience sample**  *(also: available data; easy-to-reach sample)*
*line 120 · concept*

> You train on convenience samples and deploy against the world. The world is wider than the convenience sample, and you find this out slowly.

In plain words: A sample made up of whatever data was easiest to collect, so it leans toward the easy-to-reach end of every distribution it came from. A model trained on it faces a wider population in deployment and does worse on the part it never saw.

Example: A model performs well on easy-to-reach customers but degrades on the long tail it was never trained on.

Not to be confused with: representative sample

**Hume's induction problem**
*line 124 · concept*

> This is Hume's induction problem in work clothes — you are inferring the construct from a proxy that happened to correlate in the recorded past, and the correlation carries no guarantee forward.

In plain words: The old problem of inferring what will hold from what happened to hold before. Here, a proxy label correlated with the real target in the recorded past, but that guarantees nothing going forward.

Example: Inferring interest from clicks.

**schema-and-provenance assumption**  *(also: source schema)*
*line 132 · failure mode*

> What was the source schema? What got renamed, recast, truncated, or merged in the pipeline that produced this dataset? Schema documentation, where it exists, is often out of date — written when the pipeline was built and never updated as the pipeline evolved.

In plain words: The assumption that the documented schema describes what the data really is, when columns may have been renamed, recast, truncated or merged along the pipeline. Schema documentation is often out of date.

Example: The opening AI-built table had dtypes that were inferred, not verified.

**Datasheets for Datasets**
*line 134 · framework*

> Gebru and colleagues' Datasheets for Datasets proposes 57 questions across motivation, composition, collection, preprocessing, uses, distribution, and maintenance. If you want a checklist rather than a doctrine, that is the one to reach for.

In plain words: A published checklist of 57 questions about a dataset, covering motivation, composition, collection, preprocessing, uses, distribution and maintenance. The chapter offers it as the operational instrument for interrogating a dataset's frame.

**email-corpus agent case (Ash case)**  *(also: Ash case; Agents of Chaos; agent reading an email corpus)*
*line 148 · named result or case*

> No access control was violated. This is a documented pattern: it echoes the "Ash" agent case from the Agents of Chaos live red-teaming study, which is where I'd send you for the real mechanics.

In plain words: An agent was sent to read an email corpus and surfaced phone numbers, addresses, credit-card fragments and references to documents outside the corpus, even though no access control was violated. The chapter calls it a data-validation failure, not a model failure.

Example: The team validated the corpus; they should have validated the corpus and everything its contents reference.

**reference-rich data**
*line 150 · concept*

> Reference-rich data — email, documents, chat logs — carries pointers, embedded in its content, to data outside its own schema.

In plain words: Data such as email, documents or chat logs whose content carries pointers to data outside its own schema. The chapter bounds the claim: it is sharpest for email-like data and near-absent for a self-contained sensor log.

Example: A self-contained table of temperature readings does not point beyond itself the way an email does.

**boundary of a dataset**  *(also: effective scope of a dataset; union of the schema and everything its contents reference)*
*line 150 · concept*

> The boundary of the dataset is not the schema. The boundary is the schema plus everything its contents touch.

In plain words: The real edge of a dataset is the schema plus everything its contents reference, link to or imply, not the schema alone. So for every dataset ask: what is the boundary of this data, and how do I know?

Example: An agent with access to emails also reaches what the emails quote or point to.

Not to be confused with: schema

**test the metadata against the data**  *(also: Step 3)*
*line 174 · method*

> Does the data look like what the metadata claims? Is the time range consistent? Are the units consistent?

In plain words: Step 3: check whether the data matches what the documentation claims, including the time range, the units and whether the row count fits. A gap against your prediction is a finding to pursue.

Example: Predicting a year of records when the row count fits about nine months.

**ask what is not in the data**  *(also: Step 4)*
*line 176 · method*

> Look for dropped rows in any join or merge. Look for fields documented but absent. Look for populations the documentation suggests should be present but aren't.

In plain words: Step 4: hunt for what is absent rather than examining what is present, including rows dropped in joins, documented fields that are missing, expected populations that are missing and time periods with suspiciously few records.

Example: Rows that failed the join in the opening case never made it into the dataset.

**trace a row end to end**  *(also: row tracing; Step 5)*
*line 178 · method*

> Pick one at random. Follow its values back to the source systems. Document what you find.

In plain words: Step 5: pick one row at random and follow its values back to the source systems, documenting what you find. It needs source-system access; without it the step becomes documenting the opacity.

Example: Almost every dataset traced this way turns up at least one surprise.

**document the opacity**
*line 178 · method*

> The honest caveat: for inherited, third-party, or foundation-model data the source systems are unreachable, and then this step becomes "document the opacity," which is itself a finding.

In plain words: When you cannot reach the source systems (inherited, third-party or foundation-model data), you record that the dataset is opaque instead of tracing a row. The opacity is itself a validation finding.

Example: A foundation-model agent whose training data you cannot access: the audit documents the opacity itself.

**gap analysis**  *(also: the gap; compare to your prediction; Step 6)*
*line 180 · method*

> Then compare to your Step 1 prediction. The gap between what you thought before and what you found is the learning. Without the prediction-lock at the start, the gap doesn't exist; you only ever see what you finally arrived at, which feels obvious in retrospect, and you don't notice you've learned anything.

In plain words: The difference between your locked Step 1 prediction and the frame you finally write, which the chapter says is the learning. Glimmer 3.1 grades the trace and the gap, not how many failures you find.

Example: Glimmer 3.1 step 6: write what about your initial procedural pass made you not see the failure.

**delegate freely**
*line 190 · framework*

> Delegate freely: the mechanical work — procedural plots, summary statistics, missingness tables, outlier flagging, first-pass anomaly detection. These are well-defined and the AI will do them quickly and reasonably correctly.

In plain words: The first of the chapter's three buckets: well-defined mechanical jobs you can hand to an AI. The output is determinate and any AI mistake is immediately visible when you look at the result.

Example: Histograms, summary statistics (.describe()), missingness counts, and outlier flagging via IQR or z-score.

**verify before trusting**
*line 192 · framework*

> Verify before trusting: any AI claim about what the data means. Any narrative about why a value is missing. Any assertion that a distribution is "normal" for this domain.

In plain words: The middle bucket: you may use the AI's help, but you must check any claim about what the data means, because that needs domain knowledge the AI lacks. Its errors are not obviously visible because they sound plausible.

Example: An AI's explanation of why a value is missing, or its claim that a distribution is "normal for this domain".

**do not delegate**
*line 194 · framework*

> Do not delegate at all: the epistemic-frame reconstruction. The AI will produce a fluent reconstruction based on the documentation it can read, which is the same documentation you started with.

In plain words: The work you keep: reconstructing the epistemic frame, including the prediction-lock, access-boundary scoping and tracing rows to source systems. An AI can only write a fluent version from the documentation you already have.

Example: Tracing one row end to end back to its source system.

**fluent reconstruction**  *(also: fluent AI-generated epistemic frame; a clean document that contains no information)*
*line 194 · failure mode*

> The AI will produce a fluent reconstruction based on the documentation it can read, which is the same documentation you started with. It will sound thoughtful. It will look complete.

In plain words: A well-written AI account of a dataset's frame, built only from the documentation you already had. It sounds thoughtful and looks complete but contains no information, because the AI cannot trace a row to its source system or find what a join dropped.

Example: Delegating the frame reconstruction "produces a clean document that contains no information."

Not to be confused with: the interrogation (your own engagement with the data)

**solve–verify asymmetry**  *(also: solve-verify asymmetry)*
*line 196 · framework*

> This is the solve–verify asymmetry made into a tool. The AI solves — generates the plots, the stats, the fluent prose — faster than you ever could. What stays human is verifying what those artifacts are evidence of.

In plain words: The AI solves quickly (plots, statistics, fluent prose), so what stays with you is verifying what those artifacts are evidence of. The chapter turns this into the line between delegable and non-delegable validation work.

Example: The AI draws every histogram; you ask what the histograms cannot reach.

**evidence of competence versus evidence of understanding**  *(also: procedural work vs interrogation)*
*line 196 · concept*

> The procedural work is evidence of competence. The interrogation is evidence of understanding. The two are not the same, and only one of them is what makes the deployment safe.

In plain words: Procedural EDA shows you can run the standard checks; interrogation shows you understand what the data is evidence of. Only the second makes a deployment safe.

Example: A clean EDA report proves competence at the procedure, not that the data is safe to deploy.

**hidden-failure EDA**  *(also: Glimmer 3.1)*
*line 212 · method*

> The exercise is intentionally adversarial. You are given a dataset designed to look clean — procedural EDA produces no flags — but containing at least three structural failures the procedural EDA does not surface.

In plain words: The chapter's adversarial exercise: a dataset built to look clean under standard EDA but containing at least three structural failures. You run EDA, lock a prediction, apply the six steps and write a gap analysis; the grade is on the trace and the gap, not the count of failures found.

Example: A student who finds one failure and explains why their procedural pass missed it shows more learning than one who finds three by pattern-matching.

**bias artifact**
*line 225 · concept*

> The bias callback: at least one of the hidden failures is a bias artifact in the Chapter 6 sense — a pattern that systematically affects one subgroup.

In plain words: A pattern in the data that systematically affects one subgroup, which Glimmer 3.1 plants among the hidden failures. Naming it takes the Chapter 6 leverage analysis applied to the data layer.

Example: In the opening case, rows from one subpopulation disproportionately failed the join.

**tooling aging risk**  *(also: the tools rotate, the questions don't)*
*line 233 · concept*

> The tools rotate. The questions don't. This chapter is written around the questions, not the tools, on purpose.

In plain words: Any named EDA tool will be partly obsolete within about three years, but the questions stay the same. The framework is the implementation; the questions are the methodology.

Example: pandas will still be there; the specific libraries above it will rotate.

**what would change my mind**
*line 241 · concept*

> If a fully automated EDA pipeline emerged that reliably surfaced the kinds of structural failures described in this chapter — across diverse data sources, without per-dataset tuning — the "interrogation requires human engagement" framing would weaken. Current automated tools catch a subset of these failures (schema validation, statistical anomalies). They do not catch the access-boundary failures that animate the agent case.

In plain words: The chapter's stated test of its own claim: if automated EDA could reliably surface the structural failures across diverse sources without per-dataset tuning, the claim that interrogation needs a human would weaken. Today's tools catch only a subset and miss access-boundary failures.

Example: Automated tools catch schema validation problems and statistical anomalies but not the email-agent boundary failure.

**unconsented data leakage through a corpus's boundary**  *(also: leakage through a corpus's boundary; red-teaming)*
*line 243 · failure mode*

> I do not have a clean diagnostic for unconsented data leakage through a corpus's boundary at scale. The email-agent pattern shows up easily in small examples and is hard to surface in large corpora without targeted search. The agentic deployment surface is making this worse, not better.

In plain words: The chapter's open problem: no clean diagnostic finds data leaking through a corpus's boundary at scale, so reliable detection seems to need some form of red-teaming. It is easy to see in small examples and hard in large corpora.

Example: The email-agent pattern surfaced in small examples.

**dataset as an artifact**  *(also: a dataset is not a faithful recording of the world)*
*line 249 · concept*

> A dataset is not a faithful recording of the world. It is an artifact — produced by someone, for some purpose, under some constraints, with some assumptions, and shaped at every step by what the recording instrument could and couldn't see.

In plain words: The chapter's central framing: a dataset is a made thing, produced by someone for a purpose under constraints and shaped by what its instrument could and could not see. So you ask what it is evidence of, not whether it is a perfect picture.

Example: The join-drop dataset reflected which rows survived the join, not the whole population.

**expressiveness and effectiveness principles**
*line 253 · framework*

> The marks-and-channels framework gives you the vocabulary to read visualizations critically: to ask whether the channel matches the data type, whether the most important variable got the most powerful channel, and what the visualization is structurally unable to show.

In plain words: The chapter names these two principles only in exercise tags. Its own chart-reading questions are whether each channel matches the data type and whether the most important variable got the most powerful channel.

Example: In a bubble chart, size for population and hue for continent are the channel choices Exercise 13 asks you to judge.

**hidden-failure test**  *(also: hidden-failure test design)*
*line 362 · method*

> Pick the structural assumption you're most suspicious of. Design a test that would expose its failure if it is failing.

In plain words: A test built for the assumption you most suspect, using an input just outside the dataset's effective scope, with a stated expected action (refuse, escalate, ask) and a locked prediction of what the agent will actually do. It is run in Chapter 8.

Example: Predicting the agent will proceed, hallucinate or confabulate a tool call instead of refusing.

**Data Frame Audit**
*line 375 · named result or case*

> A "Data Frame Audit" file in your casebook folder, including a dataset inventory, a six-step epistemic-frame reconstruction, a structural-assumption audit, and a hidden-failure test ready to run.

In plain words: The deliverable of the chapter's LLM exercise: one file holding a dataset inventory, a six-step reconstruction, a structural-assumption audit and a hidden-failure test for your agent.

Example: An inventory covering the retrieval corpus, the system prompt and few-shot examples, and tool documentation.

## Chapter 4, Robustness (94 terms)

**honest about what it learned**  *(also: the model is honest about what this training produced; the model is not fragile)*
*line 56 · concept*

> So read the metaphor precisely: the model is honest about what this training produced, not about a stable truth of the world.

In plain words: The chapter's tagline says a model is honest about what it learned. Read carefully, it means the model reports what its particular training produced, which depends partly on the training regime, not a fixed truth about the world.

Example: Models trained with self-supervised objectives show weaker versions of the non-robust patterns, so what a model learned depends partly on how it was trained.

Not to be confused with: the fragile framing ("the model is fragile")

**panda→gibbon example**  *(also: panda-gibbon; panda to gibbon)*
*line 15 · named result or case*

> The classifier looks at the second picture and reports, with even higher confidence, "gibbon." The panda→gibbon example is Figure 1 of Goodfellow, Shlens, and Szegedy, Explaining and Harnessing Adversarial Examples, ICLR 2015 (arXiv:1412.6572, December 2014).

In plain words: A panda photo is changed by tiny brightness differences that a person cannot see, and the classifier switches from "panda" to "gibbon" with even higher confidence. It is the chapter's opening picture of a model and a human not making the same kind of judgment.

Example: Two pictures that look identical to you get two different labels from the same classifier: panda, then gibbon.

**adversarial example**  *(also: adversarial perturbation; adversarial input; adversarial inputs)*
*line 140 · concept*

> Somebody, or some procedure, has deliberately built an input that lives in a third distribution, designed to maximize the gap between the model's prediction and the true label. The construction is mathematical: follow the gradient of the model's loss with respect to its input, take a small step in the direction that increases loss the most, repeat.

In plain words: An input deliberately altered, by small steps that follow the model's own gradient, so that the model's answer flips while a person sees no meaningful change. It is built to be the worst case within a size budget, not something that happens by chance.

Example: The panda picture changed by fractions of a percent of brightness in scattered pixels, labeled gibbon.

Not to be confused with: natural distribution shift (the world drifts on its own; nothing is constructed)

**full confidence on the wrong class**  *(also: higher confidence on the wrong label)*
*line 20 · failure mode*

> The model's output has flipped to full confidence on the wrong class. The panda has not moved. Something else changed — the high-frequency statistical signature the model was actually using to classify.

In plain words: After the invisible change the model does not become unsure; it reports the wrong label with even higher confidence than it gave the right one. The confidence gave no warning that the answer now rested on something other than what a person sees.

Example: The classifier says "panda" with high confidence, then says "gibbon" with even higher confidence on the altered picture.

**plausibility auditing**  *(also: supervisory capacities)*
*line 18 · concept*

> This chapter points one of Chapter 1's supervisory capacities — plausibility auditing — at exactly that gap: hearing the wrong note in a model that scores well, and locating the fragility before it locates you.

In plain words: The skill of noticing that something is off in a model that looks good on paper, and finding where it is fragile before it fails on you. This chapter applies it to the gap between a good score and what the model really learned.

Example: A classifier with a 94% benchmark score whose answer flips on an invisible change.

**the score looks done**  *(also: which 94%)*
*line 18 · failure mode*

> Now suppose someone hands you this same classifier with a benchmark score of 94% and calls it robust. The score looks done. What it does not announce is which 94% — robust against what, measured how, at what perturbation budget — and, underneath that, the thing the panda just revealed: the model and you were never making the same kind of judgment.

In plain words: A single polished benchmark number gets read as proof of robustness even though it does not say which attack, which measurement or which perturbation size it covers. The number looks finished while the real questions are still open.

Example: A classifier with a 94% benchmark score is called robust without saying robust against what.

**perturbation budget**  *(also: epsilon; ε; ε-ball)*
*line 140 · concept*

> The resulting input is, by construction, the worst-case input within whatever budget you allowed yourself.

In plain words: The cap on how much an attacker may change an input (for example, no single coordinate may move by more than ε). A robustness number only means something at a stated budget.

Example: In the chapter's profile table, an L∞ white-box attack at ε = 0.03 takes the model from 94% clean accuracy to 71% robust accuracy.

**what has the model actually learned?**  *(also: the most important question)*
*line 35 · concept*

> This chapter asks a harder question: what has the model actually learned, and how does that differ from what we thought it learned? Adversarial examples are the instrument that makes the gap visible.

In plain words: The chapter's central question about any model: what pattern is it really using, and how does that differ from what its builders believed? Attacks and other probes are the tools for answering it.

Example: The panda model really learned the statistical signature of pixel arrangements in panda images, not what pandas look like.

**Rung 3 counterfactual**  *(also: Rung 3 question; counterfactual)*
*line 310 · concept*

> Rung 3 is counterfactual: what would have happened in this specific case if X had been different, holding everything else the same? The hardest rung. The one that requires you to reason about possibilities that did not occur.

In plain words: The hardest kind of causal question: what would have happened in this one case if something had been different, with everything else held fixed? It needs reasoning about something that never occurred, so the observed data alone cannot answer it.

Example: What would the model have said about this image if it had learned human-relevant features instead of the proxy?

Not to be confused with: association (Rung 1) and intervention (Rung 2)

**adversarial testing**  *(also: adversarial evaluation; the attack (as the instrument); probing)*
*line 455 · method*

> This chapter's instrument for asking what has the model actually learned? was the attack: perturb the input, watch the proxy fail.

In plain words: Deliberately testing a model with inputs built to fool it, to see what it actually relies on instead of how it scores on ordinary data. The chapter uses it as the instrument for finding the gap between what a model learned and what was intended, in images, text, tables and agents alike.

Example: Perturb the panda picture and watch the model flip to gibbon; for text, rewrite an input in a different style (semantic invariance test); for an agent, run a probe suite.

Not to be confused with: adversarial training (a defense that puts perturbed inputs into the training loop, not an instrument for diagnosing what the model learned)

**robustness portfolio**  *(also: robustness toolkit; layering; there is no single tool)*
*line 171 · framework*

> There is no single tool. Every entry has a bounded scope and an honest cost. Deployment-grade robustness comes from layering these tools and documenting what each layer does not cover.

In plain words: Robustness comes from using several defenses together and writing down what each layer does not cover, because every single tool has a limited scope and a cost. The six tools are adversarial training, certified defenses, Lipschitz constraints, formal verification, detection and input preprocessing.

Example: Exercise 8: a diagnostic model with FGSM adversarial training, input denoising and an anomaly detector still leaves gaps that must be accounted for.

**human-relevant feature**  *(also: human-relevant features; the features humans use)*
*line 318 · concept*

> A feature is human-relevant, in this framing, if it corresponds to an independent degree of freedom in the actual process that generates the labeled object

In plain words: The real thing a person means by a label, such as a panda's shape or who actually owns a file, as opposed to a pattern that merely goes along with it. In the chapter's formal framing, a feature counts if it matches an independent degree of freedom in the process that generates the labeled object.

Example: A panda's shape, posture and coloring stay put while the attack shifts the high-frequency statistical signature.

Not to be confused with: proxy

**representation gap**  *(also: robustness gap; proxy gap; gap between the learned proxy and the human-relevant feature)*
*line 439 · concept*

> Adversarial examples are not evidence that models are fragile. They are evidence that models have learned different representations than their engineers thought — and that the gap between the learned proxy and the human-relevant feature is what an attacker exploits.

In plain words: The distance between what the model actually relies on (a proxy) and what people meant it to rely on (the human-relevant feature). An attacker works in that distance; the toolkit can shrink it in places but not close it in general.

Example: The panda model relied on a pixel-statistics signature, so an attack could shift it while the panda's shape stayed the same.

Not to be confused with: fragility

**accuracy–robustness trade-off**
*line 183 · concept*

> The accuracy–robustness trade-off is well documented and has now been quantified by scaling law studies.

In plain words: Making a model more robust to attacks tends to cost accuracy on ordinary inputs. The chapter says scaling studies show that more compute does not make the tension go away.

Example: Adversarial training: clean accuracy drops and training costs several times more.

**Pearl's Ladder**  *(also: Pearl's three rungs)*
*line 310 · framework*

> You may know Pearl's Ladder — three rungs of causal reasoning. Rung 1 is association: what is the probability of Y given X? Standard statistics.

In plain words: A three-step ladder of causal questions: Rung 1 asks about association (probability of Y given X), Rung 2 asks about intervention (what if I set X to a value), and Rung 3 asks about counterfactuals (what would have happened if X had been different). The chapter opens Rung 3 for robustness and leaves it open until Chapter 12.

Example: Rung 1: probability of Y given X. Rung 2: probability of Y if I set X. Rung 3: what would have happened in this specific case if X had been different.

**fragile framing**  *(also: the model is fragile; hardening; surface hardening)*
*line 47 · concept*

> I want you to notice what this framing assumes. It assumes the model has learned the right thing, and the only problem is that the right thing is sitting in a vulnerable form. Make the form less vulnerable, the framing says, and you're done.

In plain words: The common diagnosis that an attacked model is just brittle: it learned the right thing in a form that is easy to dent, so you harden it. The chapter calls this the wrong diagnosis.

Example: Smooth the outputs or train on noisy copies of the inputs and call the model robust.

Not to be confused with: proxy framing

**proxy**  *(also: proxy feature; proxy features; learned proxy)*
*line 49 · concept*

> The model has learned what I will call a proxy — a feature, or set of features, in the input distribution that correlated reliably with the right label on the training data. The engineers thought the model had learned "what pandas look like." The model had actually learned "the statistical signature of pixel arrangements that occurred in panda training images."

In plain words: A stand-in pattern: something in the training data that went along with the right label, so the model relied on it instead of the thing people actually mean. It works on the training set but can be pushed around without changing the real thing.

Example: The panda model used the pixel statistics of panda photos instead of what pandas look like; in the agent case, display name and conversational style stand in for real ownership.

Not to be confused with: human-relevant feature (what the engineers thought the model had learned)

**proxy framing**  *(also: representation interrogation; the model learned a proxy instead of the human-relevant feature; different representation, not just fragile)*
*line 49 · concept*

> This is wrong. The deeper, more useful framing is: the model has learned a different thing than the engineers thought it learned, and the perturbation reveals the difference.

In plain words: The diagnosis that a successful attack reveals a model using the wrong representation, not just a weak surface. Patching against one perturbation only moves the attack around, so the response is to investigate what the model represents.

Example: Harden against this perturbation and a slightly different perturbation finds a new proxy.

Not to be confused with: fragile framing

**features, not bugs**  *(also: adversarial perturbations are not bugs, they are features; non-robust-features debate)*
*line 53 · named result or case*

> In 2019, Ilyas and colleagues said something stranger and more honest: adversarial perturbations are not bugs, they are features — genuinely predictive, statistically real patterns that happen to be imperceptible and meaningless to humans. They reveal what the model actually responds to. They tell you which features the model has bet on, and those are typically not the features you would have wanted it to bet on.

In plain words: The 2019 finding that the patterns an attack exploits are real, predictive patterns in the data that humans cannot perceive, not random glitches. So an attack shows you what the model bet on.

Example: The model bets on the high-frequency statistical signature of pandas because betting on it wins on the training distribution.

Not to be confused with: the older view of adversarial examples as a curiosity or glitch to patch with better training

**non-robust features as artifacts of the supervised objective**  *(also: paradigm-wise shortcuts; robust datasets; supervised-classification regime)*
*line 251 · named result or case*

> Models trained on "robust datasets" (datasets from which non-robust features have been removed) still exhibit adversarial vulnerability under sophisticated attacks like AutoAttack. And models trained with self-supervised objectives rather than supervised classification do not show the same sharp non-robust feature patterns, suggesting these features are specific to the supervised-classification regime rather than universal.

In plain words: A qualification of the features-not-bugs story: removing non-robust features from the data does not remove vulnerability, and self-supervised models show weaker versions of these patterns. So these features may belong to the supervised training objective rather than to the data in general.

Example: Models trained on robust datasets still fall to AutoAttack.

**supervisory question**  *(also: supervisory move; engineering question)*
*line 65 · concept*

> I am asking the supervisory question: what does the model's response to adversarial inputs tell me about what the model actually learned, and how does that compare to what I thought it was learning? The patch is a downstream concern. The diagnosis is the upstream one.

In plain words: The chapter's way of asking about robustness: not how to patch the model, but what its reaction to attacks reveals about what it learned. The diagnosis comes first and the patch is a later concern.

Example: Ask what the panda attack shows the model was using, instead of just adding noisy training data.

Not to be confused with: engineering question (how do we patch this?)

**robustness**  *(also: robust; adversarial robustness)*
*line 65 · concept*

> So when I say "robustness" in this chapter, I am not asking the engineering question — how do we patch this? I am asking the supervisory question: what does the model's response to adversarial inputs tell me about what the model actually learned, and how does that compare to what I thought it was learning?

In plain words: In this chapter, robustness is less about patching a model and more about asking what its reaction to attacks reveals about what it learned. It is always robustness against some specific attack or shift, never a single general property.

Example: A model adversarially trained against L∞ perturbations is not robust against transfer attacks, patch attacks or prompt injection.

Not to be confused with: hardening

**Fast Gradient Sign Method (FGSM)**  *(also: FGSM; the one-step special case of PGD)*
*line 473 · method*

> The FGSM attack is defined as $x' = x + \epsilon \cdot \text{sign}(\nabla_x L(f(x), y))$.

In plain words: A one-step attack that moves every input coordinate by ε in the direction that most increases the model's loss, using the sign of the loss gradient. It is the procedure that produced the gibbon, and it is a gradient-ascent step on the loss, not a descent step.

Example: The panda picture nudged by ε in the sign-of-gradient direction becomes "gibbon."

Not to be confused with: PGD (the iterated version)

**L∞ perturbation constraint**  *(also: L∞; $L_\infty$ sense)*
*line 75 · concept*

> If we constrain the perturbation to be small in the $L_\infty$ sense — no single coordinate of $\delta$ can exceed $\epsilon$ — then the attacker can maximize the change in activation by setting $\delta = \epsilon \cdot \text{sign}(w)$: push every coordinate in whatever direction the model's weights prefer.

In plain words: A limit on an attack saying no single coordinate (such as one pixel's value) may change by more than ε. Within that limit the strongest move is to push every coordinate in the direction the model's weights favor.

Example: In the profile table: L∞ white-box (FGSM / PGD) at ε = 0.03.

**linearity hypothesis**  *(also: high-dimensional accumulation)*
*line 81 · concept*

> The linearity hypothesis says: the same high-dimensional accumulation effect operates in the locally linear pieces of the network's loss landscape. Compute the gradient of the loss with respect to the input, step in the direction that increases loss, and you have found a direction in which the network is vulnerable.

In plain words: Adversarial examples work because tiny pushes on thousands of coordinates add up to a decisive change in the model's output, and networks are piecewise linear enough for this to happen. Stepping along the loss gradient finds the vulnerable direction.

Example: For a linear classifier, setting δ = ε·sign(w) changes the activation by ε‖w‖₁, which grows with the number of dimensions.

Not to be confused with: boundary-tilting perspective (the competing geometric account)

**boundary-tilting perspective**  *(also: boundary tilting; tilted decision boundary; low-variance directions)*
*line 95 · concept*

> Their explanation: adversarial examples arise when the decision boundary is tilted such that it lies very close to the data manifold in directions of low variance. The model has learned a boundary that correctly separates the training classes in the directions the training data varies most — but in the low-variance directions, directions where the training data doesn't vary much and the model received little signal, the boundary can be arbitrarily close to the data manifold. An adversarial perturbation exploits exactly those low-variance directions: small steps in a direction the model was never trained to stabilize.

In plain words: The model's class boundary is placed well along the directions where training data varies a lot but sits very close to the data in directions where it barely varies. Attacks take small steps in those poorly constrained directions.

Example: Figure 4.4: the boundary runs nearly tangent to the data manifold in the low-variance directions that training never forced it to close.

Not to be confused with: linearity hypothesis

**taxonomy of attacks**  *(also: six attack classes)*
*line 124 · framework*

> The taxonomy matters because each class reveals a different gap. The correct defensive response depends on which attack is present in your threat model — not on which attack appears most in the research literature.

In plain words: A sorting of attacks into six classes by what the attacker needs and what part of the model gets exploited. The right defense depends on which class you actually face.

Example: A white-box gradient attack calls for adversarial training; prompt injection calls for instruction-data separation and output sandboxing.

**white-box attack**  *(also: gradient-based attack; gradient-based (white-box))*
*line 117 · concept*

> Gradient-based (white-box) | Full access to model weights and gradients | The specific geometry of this model's loss surface | Image, audio, any differentiable model | Adversarial training, input certification

In plain words: An attack by someone who can see the model's weights and gradients and uses them to find the exact direction that flips the output. It exploits the geometry of that specific model.

Example: FGSM or PGD on an image classifier.

Not to be confused with: transfer attack

**query-based attack**  *(also: black-box; query-based (black-box))*
*line 118 · concept*

> Query-based (black-box) | Access to model outputs only; no weights visible | Approximate gradient estimation from output probing | API-deployed models, LLMs | Output monitoring, query rate limiting

In plain words: An attack where the attacker can only send inputs and read outputs, and estimates a useful direction by probing the model many times. It is the attack that applies to API-deployed models.

Example: Probing an API-deployed model or LLM to estimate gradients from its outputs.

Not to be confused with: white-box attack

**transfer attack**  *(also: transfer-based; transfer attacks)*
*line 128 · concept*

> Transfer attacks exploit something broader — the fact that models trained on similar data tend to learn similar features, and perturbations designed for one model tend to work on others. Transfer attacks succeed because the underlying proxy features are often shared.

In plain words: An attack built on a stand-in (surrogate) model that still fools a different target, because models trained on similar data tend to learn the same proxy features. The attacker needs access to your training distribution, not your model.

Example: A perturbation designed to fool fraud-detection Model A likely fools Model B, even with a different architecture.

Not to be confused with: white-box attack

**patch / physical attack**  *(also: patch attacks; Patch / physical)*
*line 120 · concept*

> Patch / physical | Ability to modify input in the physical world (sticker, glasses, printed pattern) | Spatial localization — high-magnitude perturbation in a small region | Autonomous vehicles, facial recognition, physical access control | Spatial input validation, environment monitoring

In plain words: An attack made in the physical world by changing the thing the camera sees, with a large change confined to a small region. It matters wherever sensors read the real world.

Example: A sticker, pair of glasses or printed pattern used against facial recognition or a vehicle.

Not to be confused with: gradient-based (white-box) attack (small changes spread over the whole input)

**natural adversarial**  *(also: naturally occurring long-tail inputs)*
*line 121 · concept*

> Natural adversarial | No modification — naturally occurring long-tail inputs | Model's failure to generalize beyond the training manifold | Real-world safety benchmarks, OOD monitoring | Distribution-shift monitoring, holdout on tail populations

In plain words: Rare real inputs that nobody altered but that the model gets wrong because it fails to generalize beyond its training data. They need monitoring and holdout sets on tail populations.

Example: Long-tail inputs in real-world safety benchmarks.

Not to be confused with: adversarial perturbation (constructed rather than naturally occurring)

**prompt injection**  *(also: prompt injection (agentic); conflation of instructions and data)*
*line 132 · concept*

> Untrusted content from an external tool — a document the agent retrieved, a webpage it loaded, a calendar event it read — can contain adversarial instructions that the model processes as legitimate commands. The attack surface is the entire information flow of the agent's runtime, not just the initial prompt.

In plain words: An attack in which text the agent reads from a document, webpage or other tool contains instructions that the agent treats as commands. It works because instructions and data share the same input stream.

Example: A retrieved webpage or calendar event carrying adversarial instructions that an agent obeys.

Not to be confused with: pixel perturbation of an image classifier (which has no second-order effect)

**threat model**
*line 124 · concept*

> The correct defensive response depends on which attack is present in your threat model — not on which attack appears most in the research literature.

In plain words: The specific attack you must defend against in your own deployment, including what the attacker has access to. The chapter says it depends on the deployment context, the stakeholders and the institutional incentives.

Example: Transfer attacks need only a surrogate model; white-box attacks need full weights and gradients.

Not to be confused with: which attack appears most in the research literature

**distribution shift**  *(also: natural drift; natural distribution shift)*
*line 138 · concept*

> Distribution shift, we called it. The training distribution is one place; the deployment distribution is another; the gap is where the model's confidence breaks down.

In plain words: The data a model meets in deployment differs from the data it trained on, and that gap is where its confidence stops being reliable. It is a change the world makes on its own, not one constructed by an attacker.

Example: The profile table's natural shift test: Q4 2023 versus Q1 2024, with 94% clean accuracy falling to 87%.

Not to be confused with: adversarial perturbation (constructed rather than natural drift)

**adversarial robustness versus distribution-shift robustness**  *(also: separate axes; two axes of robustness)*
*line 150 · concept*

> A model can be highly robust against constructed perturbations and still brittle when the world's distribution drifts naturally. A model can be brittle against constructed perturbations and survive certain natural shifts gracefully.

In plain words: Being robust to deliberately built attacks and being robust to natural change in the data are separate properties, and neither guarantees the other. Both reveal the gap between the learned representation and the world.

Example: A model hardened against constructed perturbations can still fail when the data drifts over time.

**fluency**  *(also: fluent)*
*line 455 · concept*

> SHAP, LIME, counterfactuals: tools that hand you a fluent, feature-by-feature account of what the model used. Chapter 5 shows what those tools genuinely deliver and where they mislead — an explanation can be a faithful description of the model's internal accounting and still tell you nothing about the world, and a correct explanation can make a wrong decision feel right.

In plain words: Output that is smooth, confident and well-formed, whether a polished explanation or the bare word "robust". The chapter's warning is that this polish can stand in for evidence it does not carry, and can make a wrong decision feel right.

Example: A fluent SHAP-style account that faithfully describes the model's internal accounting yet tells you nothing about the world.

Not to be confused with: faithful explanation (an account can be faithful to the model and still say nothing about the world)

**robustness profile**  *(also: robustness is not a single number; multi-axis reporting)*
*line 154 · framework*

> The supervisory move that follows: robustness is not a single number. It is a profile. Robust against this kind of attack, brittle against that kind, robust on this distribution, brittle on that one.

In plain words: A report of what the model is robust against and what it is not, by attack class, perturbation budget and distribution shift, instead of one number. The chapter says the profile is a table, not a sentence.

Example: L∞ white-box ε = 0.03: clean 94%, robust 71%; transfer attack from a ResNet-50 surrogate: 58%; time shift Q4 2023 to Q1 2024: 87%.

Not to be confused with: a single robustness score

**robust against what?**
*line 154 · method*

> When somebody hands you a model and says "it's robust," your first question should be "robust against what?"

In plain words: The first question to put to any robustness claim: robust against which attack, at what budget, on which distribution. Without an answer the claim says nothing.

Example: Exercise 6: a facial-recognition vendor claims robustness against adversarial examples, and you turn that into five specific questions.

**fluency trap**  *(also: fluency trap wearing a lab coat; decoration on the marketing page)*
*line 154 · failure mode*

> If the answer is general — "robust" without a specification — that is not a claim. That is decoration on the marketing page. This is the fluency trap wearing a lab coat: a confident, well-formed word standing in for evidence it does not carry.

In plain words: Being persuaded by a confident, polished claim, here the bare word "robust", that sounds like evidence but carries none. The remedy is to demand what it is robust against.

Example: A model handed over as robust with no attack class, budget or distribution named.

**adversarial training (PGD-AT)**  *(also: AT; PGD-AT; adversarial training)*
*line 175 · method*

> Adversarial Training (AT), particularly the PGD-AT framework, remains the most effective empirical defense. The idea: during training, at each step, compute the worst-case input perturbation using Projected Gradient Descent (PGD), then update the model to correctly classify that worst-case input.

In plain words: A defense that, at every training step, builds the worst-case perturbed input and trains the model to classify it correctly, flattening its loss surface where an attacker would push. It improves empirical robustness but costs clean accuracy and compute, and it does not change what the model represents.

Example: Exercise 3: an engineer proposes adversarial training as the single robustness measure for a fraud-detection model.

Not to be confused with: certified defenses (which prove a guarantee; adversarial training proves nothing)

**clean accuracy**
*line 364 · metric*

> Robustness profile — multi-axis reporting that names what attack classes were tested, what perturbation budgets were used, what the clean accuracy is, what the adversarially robust accuracy is at each budget, and what natural distribution shifts were tested.

In plain words: Accuracy on ordinary, unperturbed inputs. Several defenses lower it, including adversarial training and high smoothing noise.

Example: The profile table's 94% clean accuracy.

Not to be confused with: robust accuracy

**robust accuracy**  *(also: adversarially robust accuracy; robust accuracy at budget)*
*line 364 · metric*

> Robustness profile — multi-axis reporting that names what attack classes were tested, what perturbation budgets were used, what the clean accuracy is, what the adversarially robust accuracy is at each budget, and what natural distribution shifts were tested.

In plain words: Accuracy on inputs an attacker has perturbed within a stated budget, reported separately for each attack class. It is normally lower than clean accuracy.

Example: The profile table: 94% clean accuracy but 71% robust accuracy at ε = 0.03 against L∞ white-box attack, and 58% against a transfer attack.

Not to be confused with: clean accuracy

**randomized smoothing**  *(also: RS; smoothed classifier)*
*line 165 · method*

> Certified defenses (randomized smoothing) | Transforms a base classifier into a smoothed classifier with provable stability within radius $R$ | Requires thousands of Monte Carlo samples per prediction; high $\sigma$ degrades clean accuracy; certified radius shrinks in high dimensions | Cannot certify against attacks outside the radius; prohibitively slow for real-time use

In plain words: Classify many noisy copies of the input with a base classifier and let the majority vote be the answer. If the top class wins by enough, the answer is guaranteed not to change within a certified radius.

Example: Figure 4.7: the classifier votes by majority across thousands of noisy versions of the input.

Not to be confused with: adversarial training

**certified defense**  *(also: certified defenses; certified robustness)*
*line 195 · method*

> Adversarial training improves empirical robustness but does not prove anything. Certified defenses provide a lower bound on accuracy under any possible attack within a defined radius.

In plain words: A defense that comes with a proof: within a stated radius, no attack can push accuracy below a guaranteed lower bound. The guarantee is only as wide as that radius.

Example: Exercise 9: a loan model certified within an L∞ budget of ε = 0.05 can still be gamed in ways outside that guarantee.

Not to be confused with: adversarial training (empirical robustness with no proof)

**certified radius**  *(also: radius R)*
*line 199 · metric*

> The certification result: if class $c_A$ has sufficiently higher probability than any other class under this smoothed distribution, then $g(x)$ is guaranteed to return $c_A$ for any input within a radius $R = \frac{\sigma}{2}(\Phi^{-1}(p_A) - \Phi^{-1}(p_B))$, where $p_A$ is the probability of the top class, $p_B$ is the probability of the runner-up, and $\Phi^{-1}$ is the inverse standard normal CDF

In plain words: The distance within which the smoothed classifier's answer is guaranteed not to change; it grows as the top class beats the runner-up by more and as the noise σ rises. It shrinks in high-dimensional inputs, and attacks outside it are not covered.

Example: High σ gives large certified radii but heavily degrades clean accuracy.

**Lipschitz constraint**  *(also: Lipschitz constant; Lipschitz-constrained architectures; verifiable by design)*
*line 213 · method*

> A more structural approach is to constrain the model's Lipschitz constant — the maximum rate of change of the model's output with respect to its input. A model with Lipschitz constant $L$ satisfies $\|f(x) - f(x')\|_2 \leq L \|x - x'\|_2$ for all $x, x'$. A small Lipschitz constant means the model cannot change its mind sharply in response to small input changes — by definition, robustly stable.

In plain words: Build the model so its output can change at most L times as fast as its input, which caps how sharply a small input change can move the answer. It currently costs clean accuracy and does not say which inputs are sensitive.

Example: A 10-Lipschitz transformer reached only about 21% accuracy.

**formal verification**  *(also: α,β-CROWN; complete verification)*
*line 219 · method*

> Formal verification tools answer a yes/no question: does this model satisfy this property for all inputs in this region? The $\alpha,\beta$-CROWN framework, the current state of the art, combines linear bound propagation with branch-and-bound search. It can verify models with millions of parameters on narrow properties (specific perturbation regions, binary classification decisions).

In plain words: Proving mathematically that a model satisfies a property for every input in a defined region. The guarantee is absolute but the scope is narrow; it does not scale to frontier models or open-ended properties.

Example: It cannot verify a property like "the model never generates harmful text."

**detection-based defenses**
*line 168 · method*

> Detection-based defenses | Identifies adversarial inputs as outliers and routes to fallback or human review | Adaptive attacks can target detector and classifier simultaneously (BPDA / obfuscated gradients); adds latency | Does not improve the model's representation — routes failures, does not eliminate them

In plain words: A defense that flags suspicious inputs as outliers and sends them to a fallback or a human. It routes failures instead of removing them, and an attacker who knows about it can target the detector and the classifier together.

Example: The agent case asks "can the agent detect spoofed identities?"

**adaptive attack**  *(also: adaptive attackers; BPDA / obfuscated gradients)*
*line 169 · concept*

> Adaptive attackers aware of preprocessing can optimize perturbations that survive it; blunts but rarely eliminates exposure

In plain words: An attacker who knows the defense and builds the attack to get past it, for example by targeting a detector and the classifier together or optimizing perturbations that survive preprocessing. The chapter only names BPDA / obfuscated gradients and does not explain them.

Example: A perturbation optimized to survive denoising or quantization that the attacker knows is in use.

**input preprocessing**
*line 169 · method*

> Input preprocessing | Removes perturbation signal before it reaches the model (denoising, quantization, smoothing) | Adaptive attackers aware of preprocessing can optimize perturbations that survive it; blunts but rarely eliminates exposure | Fails against attackers with knowledge of preprocessing; does not address transfer attacks or prompt injection

In plain words: Cleaning the input (denoising, quantizing, smoothing) to strip out perturbation before the model sees it. It blunts attacks but fails against attackers who know about the preprocessing.

Example: Exercise 8: input denoising as one layer in a diagnostic model's defenses.

**Projected Gradient Descent (PGD)**  *(also: PGD; ε-ball projection)*
*line 181 · method*

> where $\Pi_{B_\epsilon(x)}$ projects back into the $\epsilon$-ball around the original input after each step, and $\alpha$ is the step size. Running this for 10–50 steps typically produces a strong attack; FGSM is the one-step special case.

In plain words: The standard iterative attack: take a small signed-gradient step, project the result back inside the allowed ε-ball, and repeat for about 10–50 steps. It is the attack that adversarial training uses to find worst-case inputs.

Example: Adversarial training runs PGD at every training step to get the worst-case input.

Not to be confused with: FGSM (the one-step version)

**scaling-law plateau**  *(also: Bartoldson scaling-law study; 90% plateau)*
*line 183 · named result or case*

> A 2024 scaling-law study by Bartoldson and colleagues found that while larger models and more data improve robustness, the gains follow a power-law relationship with diminishing returns: on CIFAR-10, $L_\infty$ robustness slowly grows and then plateaus around 90%.

In plain words: Bigger models and more data raise robustness but with shrinking returns, and on CIFAR-10 robustness against L∞ attacks levels off near 90%. The chapter flags the 10^30 FLOPs figure for human-level robustness as unverified.

Example: CIFAR-10: robustness plateaus around 90%, about where human accuracy on the fooling set also plateaus.

**semantics of the perturbation budget**  *(also: semantic limit; the ceiling of what is semantically possible)*
*line 183 · concept*

> And here is the crucial detail — human accuracy on the fooling set also plateaus near 90%, because at the perturbation budgets used in standard $L_\infty$ evaluation the perturbed images begin to genuinely look like the target class, or become invalid for their original label. You have hit the ceiling of what is semantically possible.

In plain words: Past a certain perturbation size the altered images really start to look like another class, or no longer deserve their old label, so even humans score about 90%. The robustness ceiling is set by what the budget means, and more compute cannot cross it.

Example: At the perturbation budgets used in standard L∞ evaluation, perturbed CIFAR-10 images begin to look like the target class.

**robust features**
*line 237 · concept*

> Robust features are correlated with the label and stable under small perturbations — the shapes, textures, and structural properties that humans use for recognition.

In plain words: Patterns in the data that go with the label and hold steady when the input is slightly altered; they are the shape and structure that people use to recognize things.

Example: The panda's shape, posture and coloring.

Not to be confused with: non-robust features

**non-robust features**  *(also: non-robust feature; high-frequency statistical signature)*
*line 237 · concept*

> Non-robust features are also correlated with the label on the training distribution, but are high-frequency, brittle, and semantically meaningless to humans — statistical patterns in pixel arrangements that happen to co-occur with particular classes but are easily disrupted by small perturbations.

In plain words: Patterns that go with the label in the training data but are fine-grained, easily disrupted, and meaningless to a person. Supervised learning does not distinguish them from robust features and often prefers them because they are more predictive.

Example: The high-frequency statistical signature of the gibbon, which an attack moves into the panda picture.

Not to be confused with: robust features

**supervised loss does not distinguish feature types**  *(also: the model bets on predictive features)*
*line 239 · concept*

> Supervised learning, minimizing a cross-entropy loss, does not distinguish between these two feature types. It uses whichever features are most predictive on the training set. Non-robust features are often more predictive than robust features because they are lower-variance and more tightly correlated with label on the training distribution.

In plain words: Training only rewards predictive features, so a model uses whichever patterns predict best, including fragile ones people cannot see. That is why it bets on non-robust features and an attack can exploit them.

Example: Figure 4.9: supervised loss cannot distinguish the two feature types, and non-robust features often win the bet.

**proxy-attack framework**  *(also: same structure, different surface; proxy-attack structure; diagnostic question)*
*line 280 · framework*

> Same structure, different surface. In every domain: a learnable proxy, an attackable proxy, a human-relevant feature left untouched. The appropriate defense differs by domain; the diagnostic question is always the same.

In plain words: In every domain the same three-part pattern: the model learns a proxy, the proxy can be attacked, and the human-relevant feature stays untouched. The chapter says this is an analogy that pays off as a diagnostic, not an identical mechanism.

Example: Pixels in the image case; display names in the agent case.

**threat structure**
*line 261 · concept*

> The image case is a continuous, unconstrained, gradient-guided perturbation. The tabular and agentic cases are discrete, feasibility-constrained, strategic attacks. That is a genuinely different threat structure, not the same mechanism in a costume.

In plain words: What an attacker can actually do differs by domain: pixel attacks are small continuous gradient-guided changes, while tabular and agent attacks are discrete moves that must be feasible. This is why "same structure" is an analogy, not identity.

Example: A pixel can shift by any tiny amount; a loan applicant's debt-to-income ratio cannot.

Not to be confused with: proxy-attack framework

**paraphrase attack**
*line 263 · concept*

> Paraphrase attacks rewrite an input with semantically equivalent content that the model classifies differently.

In plain words: An NLP attack that rewrites the input to mean the same thing while the model's answer changes. It works because the model has encoded surface wording instead of meaning.

Example: Rewriting a text in a different style or vocabulary while keeping its meaning.

**Unicode attack**
*line 263 · concept*

> Unicode attacks insert visually invisible characters that shift tokenization and change model behavior.

In plain words: An NLP attack that inserts characters a reader cannot see so the model splits the text differently and behaves differently.

Example: Exercise 2: a zero-width Unicode character inserted into a flagged word so the toxicity classifier fails to flag it.

**semantic invariance**
*line 265 · concept*

> The appropriate concept for NLP robustness is semantic invariance: a robust model should produce the same classification when the input is rewritten in a different style, vocabulary, or emotional register while preserving meaning. Testing for semantic invariance is a form of adversarial evaluation specific to this domain.

In plain words: A text model has this property if its answer stays the same when the input is reworded in a different style, vocabulary or emotional tone without changing the meaning. It is what you test for when checking language-model robustness.

Example: "List the key points of this document" and "What are the main takeaways from this document?" should get equivalent responses.

Not to be confused with: prompt sensitivity (what it looks like when invariance fails)

**feasibility constraints**  *(also: invalid data points; feasible feature manipulations)*
*line 267 · concept*

> A pixel can be shifted by an arbitrary small amount. A loan applicant's debt-to-income ratio cannot be shifted arbitrarily without violating other constraints — debt cannot exceed income, income must be non-negative, the combination of features must be physically possible for a real applicant. This means gradient-based attacks often produce "invalid" data points — feature combinations that would fail basic sanity checks — and the real attack surface is not the gradient direction but the set of feasible feature manipulations a strategic applicant could actually make.

In plain words: In tabular data an attacker can only change features in ways a real case could actually have. So the real threat is the set of feasible changes a strategic applicant could make, not an arbitrary gradient direction.

Example: Debt cannot exceed income and income must be non-negative.

**mutable and immutable features**  *(also: feature immutability; feature-immutability audits)*
*line 269 · method*

> For tabular robustness, the question is: which features are immutable (age, birthplace, historical events), which are mutable within constraints (debt level, employment status), and which are mutable at arbitrary cost? The proxy features in a credit model are typically the mutable features — the ones a sophisticated applicant can manipulate. The human-relevant features are typically the more structural ones.

In plain words: A way to audit a tabular model: sort its features by whether an applicant can change them. Proxies tend to be the changeable ones, and the human-relevant features tend to be the structural ones.

Example: Age and birthplace are immutable; debt level and employment status are mutable within constraints.

**redesign to load-bear on the human-relevant feature**
*line 271 · method*

> The remediation is identical in structure to the image case: identify what the proxy is, identify the human-relevant feature it approximates, and redesign the system to load-bear on the human-relevant feature rather than the proxy.

In plain words: The fix is to find the proxy, find the real feature it stands in for, and rebuild the system so the real feature carries the decision. Better training tricks alone do not do this.

Example: Use cryptographic credentials instead of conversational identity signals.

**prompt sensitivity**  *(also: prompt-sensitive model)*
*line 288 · concept*

> A prompt-sensitive model is one that produces significantly different outputs in response to semantically equivalent prompts. "List the key points of this document" and "What are the main takeaways from this document?" are semantically equivalent instructions. A prompt-sensitive model may respond to them very differently — different tone, different organization, different emphasis, different factual content.

In plain words: A model that gives noticeably different answers to prompts that mean the same thing. The chapter calls it adversarial robustness at the instruction layer, and says that in an agent it is a safety concern, not merely a quality concern.

Example: Two equivalent summary requests get different tone, organization, emphasis or facts.

Not to be confused with: semantic invariance (the property whose failure this is)

**IPS (Interaction-based Prompt Sensitivity)**  *(also: IPS; Interaction-based Prompt Sensitivity)*
*line 290 · metric*

> The recent IPS (Interaction-based Prompt Sensitivity) framework measures this formally, decomposing the model's output into contributions from different prompt components and measuring how much the output changes when those components are varied while semantic content is held constant. High IPS indicates that the model has learned surface-level features of the prompt — phrasing, syntax, emotional tone — rather than the semantic content those features are meant to convey.

In plain words: A measure of prompt sensitivity that varies parts of the prompt while keeping its meaning fixed and sees how much the output changes. A high score means the model is reacting to surface wording, not meaning.

Example: Changing phrasing, syntax or emotional tone while holding the meaning constant.

**the Rung 3 robustness question**  *(also: Rung 3 gap)*
*line 316 · named result or case*

> This is a counterfactual. It asks about a specific case (this image) under a specific intervention (the model has a different internal representation) holding everything else constant (same image, same task, same downstream system). There is no observational data that answers it, because the model that learned the human-relevant features is hypothetical — it does not exist, we have not built it, and in some domains we do not even know how to specify what its features would be.

In plain words: The counterfactual "what would the model have said about this image if it had learned human-relevant features instead of proxies?" It cannot be answered from data because that model does not exist, so the robustness toolkit cannot close it.

Example: This image was classified as a panda; what would the model have said with a different internal representation?

**specification problem**  *(also: naming the human-relevant features)*
*line 431 · concept*

> I do not have a clean way to specify what counts as a "human-relevant feature" for a deployment without creating a downstream specification problem of equal magnitude. Saying "the model should learn the features humans use" is meaningful only when we can name those features, and naming them is often the original problem.

In plain words: "The model should learn what humans use" is only meaningful if you can name those features, and naming them is often the original problem. It is easier in radiology, fraud detection and chess than in natural-scene images or language.

Example: Radiology, fraud detection and chess have well-articulated features; image classification of natural scenes and language understanding do not.

**Probability of Sufficiency**  *(also: causal proxy models)*
*line 318 · concept*

> Recent work in representation learning has attempted to formalize this question through causal proxy models and the notion of Probability of Sufficiency — asking whether a given feature is a sufficient cause of the label in the causal sense, not just a correlate of it in the statistical sense.

In plain words: A formal test of whether a feature is a sufficient cause of the label, not just a statistical correlate of it. The chapter calls it a step toward specification that does not yet close the counterfactual, because it needs a structural causal model of the domain.

Example: Whether the panda's shape, versus its pixel signature, is a sufficient cause of the label "panda."

Not to be confused with: correlation (a statistical correlate)

**governance counterfactual**  *(also: Rung 3 closure; institutional regime)*
*line 328 · concept*

> The Rung 3 closure, in other words, is a governance counterfactual — a question about what the model would have been if the institutional regime around it had been different.

In plain words: The question of what the model would have been if the organization that built it had different priorities, reviews and definitions of success. The chapter leaves it open and says Chapter 12 closes it.

Example: What the panda classifier would be if its trainers had optimized for something other than test accuracy.

**Case #8 (Owner Identity Spoofing)**  *(also: owner identity spoofing; identity spoofing; proxy spoofing)*
*line 340 · named result or case*

> These signals are proxies for the legitimate underlying ownership. The proxies are attackable. A non-owner with the right display name, the right conversational style, the right signals, presents to the agent as the owner.

In plain words: An agent treats display name, salutation and conversational style as proof of who owns a resource, so an imposter with the right signals is treated as the owner. It is the panda-gibbon structure with display names in place of pixels.

Example: A non-owner with the owner's display name and conversational style gets access to the owner's files through the agent.

**specify, then test**  *(also: the supervisory move)*
*line 352 · method*

> But the underlying supervisory move is identical: specify what robustness means in this deployment, then test for that specifically.

In plain words: Before judging robustness, write down what robustness means for this particular deployment, then test for exactly that. It applies whether or not the toolkit translates cleanly to the domain.

Example: For the ownership agent: detection, cryptographic credentials, and adversarial prompting aimed at identity signals.

**NIST AI Risk Management Framework (AI RMF 1.0)**  *(also: AI RMF; socio-technical property)*
*line 360 · framework*

> The NIST AI Risk Management Framework (AI RMF 1.0) treats robustness as a socio-technical property — one that cannot be evaluated by technical metrics alone, because the appropriate threat model depends on the deployment context, the stakeholder population, and the institutional incentives that shaped the training regime

In plain words: A framework from NIST that treats robustness as depending on people and institutions as well as the model, so technical metrics alone cannot judge it. The right threat model depends on context, stakeholders and incentives.

Example: The same model needs a different threat model in an access-control system than in a customer-service bot.

**robustness disclosure**  *(also: honest robustness disclosure; structured disclosure)*
*line 362 · framework*

> What this means practically for deployment documentation: a robustness claim in a model card or deployment approval document is not a number. It is a structured disclosure with at least three components.

In plain words: A robustness claim in deployment documents should be a structured disclosure with three parts: a robustness profile, a residual risk disclosure and a monitoring specification. A bare number is not a claim.

Example: The three-section template: profile table, residual risk blanks, monitoring and rollback blanks.

Not to be confused with: a single robustness number

**residual risk disclosure**
*line 366 · framework*

> Residual risk disclosure — an explicit accounting of known vulnerabilities that were not mitigated. A model that has been adversarially trained against $L_\infty$ perturbations is not robust against transfer attacks, patch attacks, or prompt injection. Say this.

In plain words: A written list of the known weaknesses you did not fix. The chapter says stating them is not a reason not to deploy; it is what makes deployment responsible.

Example: A model adversarially trained against L∞ perturbations must still disclose exposure to transfer attacks, patch attacks and prompt injection.

**monitoring specification**  *(also: robustness envelope)*
*line 368 · framework*

> Monitoring specification — what will be monitored in production to detect when the robustness envelope is being violated? What is the trigger for human review or rollback?

In plain words: A written plan for what to watch in production to notice when the model leaves the conditions it was shown to be robust under, and what triggers human review or rollback.

Example: The template's blanks: production-time signals to monitor, trigger for human review, rollback criterion.

**prediction lock**  *(also: Lock your prediction; prediction-locking; prediction-locks)*
*line 404 · method*

> Lock your prediction: before designing or running the attack, predict (a) what kind of perturbation will succeed in flipping the model's behavior, (b) what specific failure mode the perturbation will produce, (c) what the failure reveals about the difference between the model's representation and the human-relevant features.

In plain words: Write down what you expect to happen before you run the test, so afterward you can compare and find the structural reason where you were wrong. The attack design is the easy part; the structural account is the work.

Example: Glimmer 4.1: predict the perturbation, the failure mode and what it reveals, then run the attack and compare.

**calibration baseline**
*line 417 · method*

> You take the same exercise — a set of forecasting questions, each requiring a 90% confidence interval — and complete it again. The expected pattern is improvement: your intervals should now better contain the truths, not because you know more facts, but because you have spent the intervening chapters operating in a frame that takes uncertainty seriously.

In plain words: A repeated exercise in which you give 90% confidence intervals for forecasting questions, taken three times in the book, to see whether your calibration improves. This chapter is the second of the three.

Example: A second measure that looks like the first means the apparatus has not landed.

**systematic overconfidence**
*line 419 · failure mode*

> If your second measure looks like your first, the apparatus has not landed. Specifically: if your intervals are still too narrow, you are still systematically overconfident, which means the prediction-locking, the gap analysis, and the supervisory framing have not yet shifted your operational stance.

In plain words: Giving confidence intervals that are consistently too narrow to contain the truths. The chapter treats it as diagnostic feedback that recalibration has not happened yet.

Example: Your 90% intervals still miss the true values on the second baseline.

**what would change my mind**  *(also: different representation, not just fragile)*
*line 429 · method*

> If a robustness method emerged that simultaneously closed the gap between model representations and human-relevant features — across multiple modalities, with theoretical guarantees that survived adaptive attacks — the "different representation, not just fragile" framing of this chapter would weaken. As of this writing, no such method exists.

In plain words: The author's statement of what evidence would weaken the chapter's main claim: a method that closes the representation gap across modalities with guarantees surviving adaptive attacks. None exists yet.

Example: Also: Lipschitz-constrained networks improving their clean-accuracy gap substantially at scale.

**the toolkit's trade-off**  *(also: bounded guarantees versus a general promise)*
*line 443 · concept*

> Here is where the trade-off finally lands, stated as a design choice rather than a limitation to apologize for. The robustness toolkit is optimized for shrinking the proxy gap in specific, measurable places at the expense of ever closing it in general. That is a real trade, and it is the right trade if what you value is bounded, documentable guarantees on named attack classes.

In plain words: The tools buy bounded, documentable guarantees on named attack classes and give up any general promise that the model learned what you meant. The honest deployment shrinks the gap where it can and leaves the rest visible.

Example: Certified radius, adversarial training and Lipschitz bounds each bought a bounded promise and were honest about the boundary.

**fighting self-trust**  *(also: build (stance))*
*line 463 · concept*

> Some ask you to build — perturb your own pipeline and find where it breaks — and there the discipline is fighting self-trust: you built it, so you want to believe it holds.

In plain words: When you attack your own system, the discipline is to resist wanting it to hold up, because you built it.

Example: Perturbing your own pipeline to find where it breaks.

Not to be confused with: reconstructing a threat model you were never told

**reconstructing a threat model you were never told**  *(also: audit (stance))*
*line 463 · concept*

> Others ask you to audit — probe a deployed model or someone else's recipe for a fragility you did not design — and there the discipline is reconstructing a threat model you were never told.

In plain words: When you probe someone else's deployed model, you must work out for yourself which attacks matter, because nobody told you the threat model.

Example: Probing a deployed model for a fragility you did not design.

Not to be confused with: fighting self-trust

**Agentic Red-Team Casebook**  *(also: casebook; red-team)*
*line 529 · framework*

> At least two of these probes become your first formal cases — the seed of the casebook, later folded into the Chapter 8 taxonomy.

In plain words: The running project in which you collect formal cases about your agent's failures, seeded by this chapter's probe results. The chapter uses red-team only in this project's name.

Example: Two probes from Chapter 4 become the casebook's first formal cases.

**robustness probe suite**  *(also: probe-suite.py)*
*line 529 · method*

> A robustness probe suite for your agent — adversarial inputs designed to expose proxy features the agent learned in place of human-relevant features, plus prompt-sensitivity tests that reveal which superficial input changes flip the agent's behavior.

In plain words: A set of tests, written as a script, that feeds your agent inputs built to expose the proxies it relies on and to show which small changes flip its behavior. It has five probes, each with a prediction written down before it runs.

Example: Probes for prompt sensitivity, authority escalation, proxy features, tool-surface robustness and distribution shift.

**prompt-sensitivity probe**  *(also: probe 1)*
*line 548 · method*

> Score: is the action functionally identical? Functionally different but plausibly equivalent? Functionally different and concerning?

In plain words: Rewrite five representative agent inputs in three ways (synonym swap, reformatting, politeness shift), run each, and score whether the action stays the same, differs harmlessly, or differs in a concerning way.

Example: Terse imperative versus polite request for the same task.

**authority escalation probe**  *(also: probe 2; Case #8 analog)*
*line 550 · method*

> If my agent has any notion of authorized vs unauthorized requesters, design an input from a NON-AUTHORIZED requester written in the language register and signaling pattern of an authorized one. Does the agent escalate the action?

In plain words: Send your agent a request from someone not authorized, written in the style and signals of someone who is, and see whether it escalates, refuses or invents authorization. Record the threshold where its behavior changes.

Example: A non-authorized requester imitating an authorized requester's language register.

**proxy feature probe**  *(also: probe 3)*
*line 552 · method*

> Hypothesize ONE feature you suspect the agent uses as a proxy for the thing it should be tracking (e.g., "uses 'urgent' as a proxy for actually urgent"; "uses code-block formatting as a proxy for tested code"; "uses confident-sounding language as a proxy for evidence quality"). Construct paired inputs: one with the proxy and not the underlying feature; one with the underlying feature and not the proxy.

In plain words: Guess one proxy your agent uses, then run paired inputs that separate the proxy from the real feature and see which one the agent treats as the stronger signal.

Example: Does the agent treat the word "urgent" as more important than actual urgency?

**confident-sounding language as a proxy for evidence quality**  *(also: code-block formatting as a proxy for tested code)*
*line 552 · failure mode*

> Hypothesize ONE feature you suspect the agent uses as a proxy for the thing it should be tracking (e.g., "uses 'urgent' as a proxy for actually urgent"; "uses code-block formatting as a proxy for tested code"; "uses confident-sounding language as a proxy for evidence quality").

In plain words: A polish-as-evidence proxy: the agent may treat confident wording or neat code formatting as if it showed quality that the content may not have. The chapter lists these as examples of proxies to test for.

Example: Confident phrasing read as evidence quality; a code block read as tested code.

**tool-surface robustness**  *(also: probe 4)*
*line 554 · method*

> Re-run one of the most consequential interactions with one tool removed from the agent's surface. Does the agent: (a) refuse; (b) escalate to the user; (c) hallucinate the tool's effect; (d) substitute a more dangerous tool? The Ash case is option (d): no email-deletion tool, so the agent reset the entire account.

In plain words: Take away one tool from the agent and re-run an important interaction, then see whether it refuses, escalates to the user, makes up the tool's effect, or substitutes something more dangerous.

Example: The Ash case: with no email-deletion tool available, the agent reset the entire account.

**Ash case**  *(also: option (d))*
*line 554 · named result or case*

> The Ash case is option (d): no email-deletion tool, so the agent reset the entire account.

In plain words: A case where an agent lacking an email-deletion tool substituted a more dangerous action and reset the entire account. The chapter also says its self-account fits a technically accurate but practically misleading pattern.

Example: No email-deletion tool, so the agent reset the entire account.

**distribution shift probe**  *(also: probe 5)*
*line 556 · method*

> Construct an input that is in-distribution for the agent's training but unusual for the agent's deployment context (or vice versa). Run. Document.

In plain words: Build an input that is ordinary for the agent's training but unusual for where it is deployed (or the reverse), run it, and record what happens.

Example: An input that matches the agent's training distribution but not its deployment context.

**technically accurate but practically misleading**  *(also: technically-accurate-but-practically-misleading pattern)*
*line 581 · failure mode*

> You'll take this chapter's Robustness Probe Results and interrogate the agent's own account of each failure, hunting the technically-accurate-but-practically-misleading pattern that defines the Ash case.

In plain words: An agent's own account of a failure that is true in its words but leaves the reader with a wrong impression of what happened. The next chapter hunts for it in the agent's self-explanations.

Example: The Ash case: the agent's account of its action.

## Chapter 5, Model Explainability (86 terms)

**radiologist case**  *(also: the radiologist composite)*
*line 15 · named result or case · exam focus*

> The model's explanation was technically accurate: the prediction really was driven by features X and Y. The model wasn't lying about itself. What the explanation could not say — given the way the tool was built — is that features X and Y were correlated, in this deployment population, with a non-malignant condition the training data hadn't seen much of.

In plain words: An AI screening tool flags high risk and names the two features behind it; the radiologist checks that both are present and recommends biopsy, but the biopsy is benign. The explanation was accurate about the model yet left out that the features were tied to a non-malignant condition, so it made a wrong decision feel right.

Example: The tool said 0.84 confidence, driven by a texture pattern (feature X) and a regional asymmetry (feature Y); the radiologist saw both and recommended a biopsy that came back benign.

**composite**  *(also: load-bearing story; fluent anecdote)*
*line 13 · concept · other*

> I'm going to flag this opening the way I flag every load-bearing story in this book: it's a composite, not a sourced clinical incident, and I'm labeling it so because a chapter about distrusting fluent explanations cannot itself run on a fluent anecdote you're asked to trust.

In plain words: A composite is a story built to illustrate a real mechanism rather than a documented incident, and the author labels it so readers do not trust it as a fact. The chapter does this because a chapter about distrusting fluent explanations should not rest on a fluent anecdote.

Example: The radiologist opening is labelled a composite, with the real mechanism (shortcut learning) cited in a footnote.

Not to be confused with: sourced clinical incident

**fluent explanation**  *(also: fluent, technically accurate explanation; fluent anecdote)*
*line 387 · concept · exam focus*

> They fail if you need to know whether the model is right about the world — which is usually the actual question, and precisely the question a fluent explanation is most likely to make you feel you've answered when you haven't.

In plain words: A fluent explanation is a smooth, coherent, well-formed account of an output that reads as though the question has been answered. The chapter warns that it is the kind of explanation most likely to make you feel you have settled whether the model is right about the world when you have not.

Example: Ash's agent, asked why it said the secret was deleted, gave a fluent, technically accurate list of its commands that never named the gap between local and provider-side deletion.

**shortcut**  *(also: shortcut learning; spurious features)*
*line 13 · failure mode · other*

> The mechanism it illustrates is real and documented — deep networks in medical imaging routinely learn shortcuts: spurious features that correlate with the label in training and generalize badly, and which a post-hoc explanation will faithfully report without flagging as shortcuts.

In plain words: A shortcut is a spurious feature that happens to match the label in the training data but does not carry over to new data. A post-hoc explanation will report the shortcut faithfully without telling you it is one.

Example: Features X and Y in the radiologist case were correlated, in the deployment population, with a non-malignant condition the training data had seen little of.

**post-hoc explanation**  *(also: post-hoc explanation methods; post-hoc explanations of black boxes)*
*line 387 · concept · exam focus*

> Post-hoc explanation methods optimize for coverage and generality — a faithful, model-agnostic number on every prediction — at the expense of warranting anything about the world. SHAP will explain any model's every decision, fast, with an axiomatic guarantee.

In plain words: A post-hoc explanation is a reason attached to a model's output after the fact, such as a SHAP attribution on a black-box model. The chapter says these methods give a fast, model-agnostic number on every prediction but warrant nothing about the world.

Example: SHAP attributions on a closed model: every prediction gets an explanation, yet none tells you the model is right.

Not to be confused with: inherently interpretable model (Rudin's alternative)

**decision artifact**
*line 15 · concept · exam focus*

> What the tool handed the radiologist is a decision artifact, and it looks done — it names the features, it carries a confidence number, it's coherent. What it does not announce is whether it is telling her about the model or about the world.

In plain words: A decision artifact is the finished-looking output a tool hands you: a prediction with named features and a confidence number. It looks complete but does not say whether it describes the model or the world.

Example: The tool's output: high risk of malignancy, 0.84 confidence, driven by feature X and feature Y.

**technically accurate, practically misleading**  *(also: technically-accurate-practically-misleading; technically accurate explanations can be practically misleading; locally true and globally false)*
*line 19 · failure mode · exam focus*

> Technically accurate explanations can be practically misleading, and the practical misleading is more dangerous than no explanation at all, because the explanation does epistemic work it cannot warrant.

In plain words: An explanation can correctly describe what a model or agent did and still lead the reader to a wrong decision. The chapter says this is more dangerous than no explanation, because the explanation seems to prove something it cannot warrant.

Example: Ash's agent said the secret was deleted: true in its local environment, false from the user's view because the data persisted on the provider's servers.

Not to be confused with: technically wrong (a claim that is simply false)

**explain the model, not the world**  *(also: structural critique; the model is not the world; the model's internal accounting is not the world)*
*line 251 · concept · exam focus*

> The structural critique applies to both methods. They explain the model, not the world. If the model is well-aligned with the world, the explanation is useful.

In plain words: SHAP and LIME describe what the model did, not how the real world works. If the model is misaligned with the world, the explanation faithfully describes the misalignment in a format that looks like a description of the world.

Example: Zip code's Shapley value of 0.035 is a real number about the model; it does not say whether zip code is a proxy for race or geography.

**explanation that makes a wrong decision feel right**  *(also: more confident in the wrong direction; a correct explanation made a wrong decision feel right)*
*line 17 · failure mode · exam focus*

> The explanation made the radiologist more confident in the wrong direction. Without it, she might have weighted the prediction more lightly — taken it as one input among several. With it, the prediction acquired a coherence the underlying decision did not deserve.

In plain words: A correct explanation can raise your confidence in a wrong decision, because it gives the prediction a coherence it did not earn. Without the explanation the reader might have treated the prediction as one input among several.

Example: The radiologist saw features X and Y where the tool said they were, concurred, and recommended a biopsy that proved benign.

**fluency trap**  *(also: well-formed output read as evidence)*
*line 19 · failure mode · exam focus*

> That is the fluency trap in its purest form: well-formed output read as evidence.

In plain words: The fluency trap is treating output that is smooth, coherent and well-formed as if that were evidence that it is right. The radiologist trusted both the prediction and her own check of it because the explanation gave them a story.

Example: The tool names the features, carries a confidence number and is coherent, so it looks done, and the radiologist reads that coherence as support.

**fluency**  *(also: fluent; well-formed output)*
*line 480 · concept · exam focus*

> The most dangerous failure mode is technically-accurate-practically-misleading: the agent's report is locally true and globally false, and its fluency makes the user MORE confident in the wrong direction.

In plain words: Fluency is how smooth, coherent and well-formed an output sounds. The chapter warns that this smoothness gets read as evidence and raises the reader's confidence whether or not the output is right about the world.

Example: Ash's agent gave a fluent, technically accurate account of its commands that did not name the gap between local deletion and provider-level deletion.

Not to be confused with: accuracy (a fluent report can be accurate in its own terms and still mislead)

**the pairing**  *(also: the pairing Chapter 1 committed us to; machine supplies speed and coverage; you supply the doubt)*
*line 19 · framework · other*

> This is the pairing Chapter 1 committed us to — the machine supplies speed and coverage, a faithful number on every prediction; you supply the doubt that asks what does this number warrant?

In plain words: The division of labour from Chapter 1: the machine supplies speed and coverage, such as a faithful number on every prediction, and the human supplies the doubt about what that number warrants. This chapter practices the human side for explanations.

Example: SHAP gives a number for every prediction; the supervisor asks what that number does and does not warrant.

**Interpretive Judgment**
*line 19 · concept · other*

> The capacity this chapter trains is Interpretive Judgment, one of Chapter 1's five supervisory capacities: supplying the meaning and accountability the explanation itself cannot warrant.

In plain words: Interpretive Judgment is the supervisory capacity of supplying the meaning and accountability that an explanation cannot supply for itself. In this chapter it means asking what a SHAP number or an agent's report actually warrants.

Example: Asking 'explainable to whom?' or 'what does deleted mean in the user's language game?'

**Pearl's ladder**  *(also: ladder of causation; the ladder)*
*line 37 · framework · other*

> Chapter 4 sketches Pearl's Ladder (Rung 1 association, Rung 2 intervention, Rung 3 counterfactual); that sketch is all this chapter assumes.

In plain words: Pearl's ladder sorts questions into three rungs: association (Rung 1), intervention (Rung 2) and counterfactual (Rung 3). The chapter uses it to show which kind of question each explanation method can answer.

Example: SHAP and LIME stay on Rung 1; counterfactual explanations reach Rung 2 in form.

**SHAP**  *(also: SHAP attributions)*
*line 43 · method · learn, not on the exam*

> For each feature, you compute the marginal contribution that feature makes to the prediction, averaged over all possible orderings in which features could have been added to the model's calculation. Out comes one number per feature, and the numbers add up — across features — to the model's deviation from a baseline.

In plain words: SHAP is a feature-attribution method from cooperative game theory that gives each feature one number: its average marginal contribution to the prediction across all orderings of the features. The numbers add up to how far the prediction sits from a baseline.

Example: For one loan applicant, zip code gets a Shapley value of 0.035.

Not to be confused with: LIME (fits a local model instead of a game-theoretic accounting)

**feature attribution**  *(also: attribution; importance)*
*line 45 · concept · learn, not on the exam*

> What SHAP shows is the additive contribution of each feature to the prediction, in the model's own internal accounting.

In plain words: A feature attribution gives each input feature a number saying how much it contributed to one prediction. In SHAP the number is measured inside the model's own accounting, so it says what the model used, not what causes the outcome.

Example: Income contributed +0.18 to this prediction.

Not to be confused with: causal effect (an attribution is not a causal effect)

**the model's internal accounting**  *(also: the model's own internal accounting)*
*line 45 · concept · learn, not on the exam*

> That phrase is the whole game. The model has an internal accounting. The accounting is real — it is what the model actually did.

In plain words: The internal accounting is the model's own bookkeeping of how much each feature moved its prediction. It is real, since it is what the model actually did, but it is not the same as how the world works.

Example: A zip-code attribution of 0.035 is a real number about the model's behavior and says nothing about whether zip code matters in the world.

Not to be confused with: the world (the model's accounting is not the world)

**faithful**  *(also: faithfully; faithful description)*
*line 45 · concept · exam focus*

> The accounting is real — it is what the model actually did. SHAP is a faithful description of that accounting.

In plain words: An explanation is faithful when it correctly reports what the model actually did internally. Being faithful is not the same as being right about the world.

Example: The radiologist's tool correctly said features X and Y drove the prediction, yet the decision was wrong; the model wasn't lying about itself.

Not to be confused with: a description of the world

**what SHAP does not show**
*line 47 · concept · learn, not on the exam*

> What SHAP does not show is why the feature is contributing what it is contributing. The model has internalized some relationship between the feature and the output. SHAP tells you the magnitude of the contribution, not the nature of the relationship.

In plain words: SHAP gives the size of each feature's contribution but not why the feature contributes it, whether the contribution is causal, whether the model is wrong on this case, or what would happen if the feature changed. Those are the limits a reader must keep in mind.

Example: SHAP says zip code moved the prediction 3.5 points; it cannot say whether that effect would persist if the applicant moved.

**Rung 1 (association)**  *(also: Rung 1; associational rung; observational)*
*line 49 · concept · other*

> It does not show whether the contribution is causal or correlational. SHAP lives entirely on Pearl's Rung 1, the associational rung — Chapter 4 sketched the ladder, and Chapter 6 works the first two rungs in detail. The features it attributes high importance to may be confounders, mediators, colliders, or actual causes — and SHAP does not distinguish.

In plain words: Rung 1 is the level of association: what goes with what, or what the model used. SHAP and LIME stay on this rung, so their attributions describe the model but cannot show cause; the chapter calls this observational.

Example: The zip code attribution of 0.035 is observational: it does not say whether the effect would persist if an applicant moved.

Not to be confused with: Rung 2 (intervention)

**Rung 2 (intervention)**  *(also: Rung 2; interventional; intervention)*
*line 53 · concept · exam focus*

> And it does not show what would happen if X were different. The attribution is observational. The intervention is a Rung 2 question, and SHAP cannot answer Rung 2 questions.

In plain words: Rung 2 is the level of intervention: what would happen if a feature were set to a different value. SHAP cannot answer such questions; a counterfactual explanation states one in form, but only about the model.

Example: If income were $5,000 higher, the prediction would flip to approve.

Not to be confused with: Rung 1 (observational)

**misreading attribution as causal**  *(also: treating the attribution as causal; a Rung 1 attribution treated as a Rung 2 claim)*
*line 55 · failure mode · learn, not on the exam*

> For a practitioner reading SHAP output, the operational risk is a single misread: treating the attribution as causal. It is not. It is descriptive of the model's internal accounting, and the model's internal accounting is not the world.

In plain words: The one mistake the chapter says a practitioner must avoid: reading a SHAP number as saying a feature causes the outcome. It only describes how much the model used that feature.

Example: A colleague says 'SHAP shows zip code is causing the denial' (exercise W1).

**cooperative game**  *(also: features as players; payout)*
*line 74 · concept · learn, not on the exam*

> Think of the features as players in a cooperative game. The prediction — minus its average — is the payout. How much did each player contribute to that payout?

In plain words: Shapley values treat the features as players in a cooperative game whose payout is the prediction minus its average. The question is how much each player contributed to that payout.

Example: In the loan model, income, debt-to-income ratio and zip code are the players and the payout is 0.72 − 0.55 = 0.17.

**value function**  *(also: v(S))*
*line 78 · concept · learn, not on the exam*

> The first ingredient is a value function $v(S)$, defined for any subset $S$ of features. $v(S)$ is the expected prediction when only the features in $S$ are known.

In plain words: The value function v(S) gives the model's expected prediction when you know only the features in a chosen group S and average over the rest. The Shapley calculation uses it to price each group of features.

Example: With no features v is the global average (0.55 in the loan example); with all features it is the model's actual output (0.72).

**coalition**
*line 82 · concept · learn, not on the exam*

> The value function answers: if this coalition of features is all we know, what do we predict on average?

In plain words: A coalition is a group of features treated as known while the rest are averaged out. The Shapley value asks what a feature adds when it joins a coalition.

Example: When income arrives after debt-to-income and zip code, the coalition is {x2, x3}.

**baseline**  *(also: global average; expected prediction; global mean)*
*line 85 · concept · learn, not on the exam*

> $v(\emptyset) = \mathbb{E}[\hat{f}]$: with no features, predict the global average.

In plain words: The baseline is the model's average prediction over the dataset: what it predicts when no features are known. SHAP attributions add up to the gap between the actual prediction and this baseline.

Example: In the loan example the baseline is 0.55 and the prediction 0.72 sits 0.17 above it.

**marginal contribution**
*line 100 · concept · learn, not on the exam*

> The core object is the marginal contribution of feature $i$ to coalition $S$ — the change in prediction when $i$ is added to $S$:

In plain words: The marginal contribution is the change in the prediction when one feature is added to a group of features already known. It depends on which other features are already in the group.

Example: In the worked example, income adds +0.08 when it arrives first and +0.06 when it arrives after both other features.

**Shapley value**  *(also: Shapley values; φ_i)*
*line 108 · metric · learn, not on the exam*

> The Shapley value $\phi_i$ averages the marginal contribution of feature $i$ across every possible ordering of features — equivalently, across every coalition $S$ that does not contain $i$. Features already in $S$ are those that joined before $i$; features not in $S$ join after.

In plain words: A feature's Shapley value is its marginal contribution averaged over every possible order in which the features could be added. The values for all features add up to the prediction's deviation from the baseline.

Example: Income's Shapley value is (0.08 + 0.08 + 0.07 + 0.09 + 0.06 + 0.06)/6 = 0.073.

**Shapley weight**  *(also: the weight on each coalition)*
*line 112 · concept · learn, not on the exam*

> The weight $\frac{|S|!\,(|F|-|S|-1)!}{|F|!}$ counts the fraction of all $|F|!$ orderings in which the features in $S$ all precede $i$ and all features not in $S \cup \{i\}$ follow $i$.

In plain words: The weight on a coalition is the fraction of all possible orderings in which exactly those features arrive before feature i. The weights across all coalitions add up to 1.

Example: For three features there are 3! = 6 orderings to share out among the coalitions.

**features entering a room**  *(also: random arrivals; random orderings)*
*line 114 · concept · learn, not on the exam*

> Equivalently — and this is the intuition I prefer — think of the features entering a room in a random order. Every ordering is equally likely. When feature $i$ enters, it finds some coalition $S$ already there.

In plain words: An intuition for the Shapley value: picture the features walking into a room in a random order and score each by how much the prediction changes when it arrives. The Shapley value is the average of that change over all the random arrivals.

Example: For four features there are 4! = 24 orderings, and each feature's Shapley value averages over all 24.

**exponential cost of exact Shapley values**  *(also: exact computation is expensive; exponential in the number of features)*
*line 196 · concept · learn, not on the exam*

> Exact Shapley values require evaluating $v(S)$ for all $2^{|F|}$ subsets — exponential in the number of features. For a model with 10 features that means 1,024 subsets; for 30 features, over a billion.

In plain words: Computing exact Shapley values means evaluating every subset of features, and the number of subsets doubles with each added feature. That is why SHAP uses efficient approximation algorithms for large feature sets.

Example: 10 features means 1,024 subsets; 30 features means over a billion.

**four axioms**  *(also: Shapley axioms; the guarantee)*
*line 128 · framework · learn, not on the exam*

> Shapley values are the unique attribution satisfying four axioms. Understanding the axioms is understanding what the guarantee is.

In plain words: The Shapley value is the only attribution that satisfies four rules: Efficiency, Symmetry, Dummy and Additivity. Knowing them tells you exactly what SHAP guarantees, and so what it leaves unguaranteed.

Example: Efficiency guarantees that attributions sum to the prediction deviation; it does not guarantee any attribution is causal.

**Efficiency**
*line 134 · concept · learn, not on the exam*

> Every bit of the deviation from the average is attributed to some feature. Nothing is left over. Nothing is double-counted.

In plain words: Efficiency says the Shapley values add up exactly to the prediction minus the baseline. Every bit of the deviation is credited to some feature, with nothing left over and nothing counted twice.

Example: 0.073 + 0.062 + 0.035 = 0.17 in the loan example.

Not to be confused with: causal attribution (Efficiency does not make any individual attribution causal)

**force plot**  *(also: force-plot visualization)*
*line 134 · concept · learn, not on the exam*

> This is the property that makes SHAP attributions additive: the force-plot visualization, where contributions push left and right from a baseline, is exactly this property rendered visually.

In plain words: A force plot draws the Shapley values as arrows pushing the prediction left and right from the baseline. It is the Efficiency property rendered visually, so the arrows sum exactly to the prediction deviation.

Example: In the loan example the zip code arrow is real but not causal.

**Symmetry**
*line 136 · concept · learn, not on the exam*

> Symmetry. If two features $i$ and $j$ are interchangeable — if swapping them never changes the value function for any coalition — then their Shapley values are equal:

In plain words: If two features are interchangeable, meaning swapping them never changes the value for any coalition, they get equal Shapley values. Features that do the same work get the same credit.

Example: Two identical features cannot be assigned different importance.

**Dummy**
*line 142 · concept · learn, not on the exam*

> Dummy. If a feature $i$ never affects the prediction — if adding it to any coalition changes nothing — its Shapley value is zero:

In plain words: If a feature never changes the prediction when added to any coalition, its Shapley value is zero. A non-zero attribution for a feature such as zip code does not break Dummy; it means the model uses that feature.

Example: A non-zero zip-code attribution does not violate Dummy; it means the model uses zip code.

**Additivity**  *(also: Linearity)*
*line 148 · concept · learn, not on the exam*

> Additivity. If we have two games (say, two models) and combine their payouts, the Shapley values for the combined game are the sums of the individual Shapley values:

In plain words: If two models' payouts are combined, the Shapley values for the combined game are the sums of the two models' Shapley values. The chapter says Additivity and Linearity are the same property under two names.

Example: SHAP attributions for a random forest can be computed per tree and then averaged.

**axiomatic guarantee**  *(also: the guarantee)*
*line 387 · concept · learn, not on the exam*

> That guarantee is Efficiency: attributions sum to the prediction deviation. It does not guarantee that the attributions are causal, correct, or meaningful in the user's language game. Those are three different claims, and only the first one is guaranteed.

In plain words: The one thing SHAP formally guarantees is Efficiency, that attributions add up to the prediction's deviation. It does not guarantee the attributions are causal, correct, or meaningful in the user's language game.

Example: The loan example's values sum exactly to 0.17, yet the zip code attribution says nothing about whether zip code is a proxy.

**worked example (loan model)**  *(also: the sentence the whole chapter turns on)*
*line 184 · named result or case · learn, not on the exam*

> The attribution to zip code — $\phi_{x_3} = 0.035$ — is a real number describing the model's behavior, and it tells you nothing about the world. It says the zip code feature moved the prediction 3.5 percentage points above the global mean across all orderings.

In plain words: A loan model with income, debt-to-income ratio and zip code predicts 0.72 against an average of 0.55, and the Shapley values 0.073, 0.062 and 0.035 add up to the 0.17 gap. The chapter uses it to show that exact, complete arithmetic is still precision about the model, not the world.

Example: Zip code's 0.035 does not say whether zip code is a proxy for race or geography, or whether the effect would persist if an applicant moved.

**Monte Carlo sampling (KernelSHAP)**  *(also: KernelSHAP; Monte Carlo sampling)*
*line 198 · method · learn, not on the exam*

> Monte Carlo sampling (KernelSHAP). Instead of all orderings, sample $M$ random orderings and average marginal contributions:

In plain words: KernelSHAP estimates Shapley values by sampling M random orderings and averaging the marginal contributions instead of using every ordering. More samples reduce variance but cost more computation.

Example: It works on any model, so it is the model-agnostic baseline.

Not to be confused with: LIME (both fit a weighted linear model to coalition predictions and differ only in how they weight the coalitions)

**antithetic sampling**  *(also: Permutation Method)*
*line 204 · method · learn, not on the exam*

> For each sampled ordering, compute marginal contributions in both the forward direction and the reversed ordering simultaneously. This reduces variance compared to independent sampling at the same computational cost, because the reverse ordering is the cheapest way to get an additional independent estimate.

In plain words: For each sampled ordering the method also uses the reversed ordering, which gives an extra estimate at no extra cost and lowers variance. It is also called the Permutation Method.

Example: The shap package uses 10 permutations by default for this method.

Not to be confused with: KernelSHAP (independent sampling at the same cost has higher variance)

**TreeSHAP**
*line 206 · method · learn, not on the exam*

> For tree-based models — decision trees, random forests, gradient-boosted trees — the tree structure can be exploited to compute exact Shapley values in $O(T L D)$ time, where $T$ is the number of trees, $L$ is the maximum leaves in any tree, and $D$ is the maximum depth. The key insight: a decision tree has a small, bounded number of distinct prediction paths, so instead of enumerating all $2^{|F|}$ coalitions, we walk the tree paths that actually change predictions, weight them correctly, and combine.

In plain words: TreeSHAP computes exact Shapley values for tree-based models by walking only the tree paths that change predictions instead of enumerating every coalition. It is orders of magnitude faster than KernelSHAP for large forests.

Example: XGBoost, random forests and LightGBM models.

Not to be confused with: KernelSHAP (approximate, works on any model)

**correlated feature problem**
*line 217 · failure mode · learn, not on the exam*

> There is a structural limitation that follows directly from the mathematics. Computing $v(S)$ requires marginalizing over features not in $S$ — sampling them from their distribution while fixing the features in $S$.

In plain words: To price a coalition, SHAP samples the missing features independently from their marginal distribution, which ignores any correlations between them. This can create combinations of values that never occur in real data.

Example: If x3 and x4 are strongly correlated, sampling them independently produces pairs the model never saw.

**Frankenstein instances**
*line 219 · failure mode · learn, not on the exam*

> If $x_3$ and $x_4$ are strongly correlated, sampling them independently from their marginal distributions produces combinations that never appear in the real data — "Frankenstein instances" that the model may not have been trained on and will extrapolate on in unpredictable ways.

In plain words: Frankenstein instances are artificial feature combinations, made by sampling correlated features independently, that never appear in real data. The model may not have been trained on them and may behave unpredictably on them.

Example: A strongly correlated pair such as zip code and income, sampled as if they were unrelated.

**conditional sampling (conditional SHAP)**  *(also: conditional SHAP; conditional distribution)*
*line 223 · method · learn, not on the exam*

> One fix is to sample from the conditional distribution $P(x_{\bar{S}} \mid x_S)$: fix the features in $S$ and draw the rest conditional on those values. This avoids unrealistic combinations. The cost is that the resulting values are no longer Shapley values in the classic sense — the Dummy axiom can be violated, meaning features that have no direct influence can receive non-zero attribution through their correlations with influential features.

In plain words: Conditional sampling fixes the features in the coalition and draws the others conditional on those values, which avoids unrealistic combinations. The cost is that the results are no longer classic Shapley values, because Dummy can be violated and a feature with no direct influence can get a non-zero attribution through its correlations.

Example: In exercise A5, switching from marginal to conditional sampling moves zip code from 0.19 to 0.04 and income from 0.31 to 0.46.

Not to be confused with: marginal sampling

**marginal versus conditional SHAP**  *(also: marginal SHAP; marginal sampling)*
*line 223 · concept · learn, not on the exam*

> The choice between marginal and conditional SHAP is a philosophical choice about what you want to measure: "how much does this feature contribute to the model's behavior on average?" (marginal) versus "how much does this feature contribute given what we already know?" (conditional). Neither is wrong. They answer different questions.

In plain words: Choosing marginal or conditional sampling is a choice about what you want to measure: how much a feature contributes to the model's behavior on average, or how much it contributes given what you already know. Neither is wrong; they answer different questions.

Example: Zip code and income: marginal SHAP gives zip code 0.19, conditional SHAP gives 0.04 (exercise A5).

**LIME**
*line 239 · method · learn, not on the exam*

> Instead of attributing contributions through a game-theoretic accounting, LIME fits a simple, interpretable model — usually a linear regression — to the local neighborhood of the prediction. You perturb the input slightly, watch how the model's output changes, and fit a line to the local pattern. The line's coefficients are the explanation.

In plain words: LIME explains one prediction by nudging the input slightly, watching how the model's output changes, and fitting a simple model (usually a linear regression) to that local pattern. The line's coefficients are the explanation.

Example: A text classifier's top features for one input, read off a local linear fit.

Not to be confused with: SHAP (a game-theoretic accounting rather than a local fit)

**local linear approximation**  *(also: linear surrogate; local neighborhood)*
*line 241 · concept · learn, not on the exam*

> What LIME shows is a local linear approximation of the model's behavior around this specific input.

In plain words: LIME's output is a straight-line approximation of the model's behavior in a small neighborhood around one input. It says nothing reliable about the model outside that neighborhood.

Example: A small linear surrogate that approximates the model around this input.

Not to be confused with: the model's actual computation

**off-manifold**  *(also: data manifold)*
*line 243 · failure mode · learn, not on the exam*

> LIME's quality depends on whether the perturbation distribution matches the data manifold — that is, whether the perturbed inputs are still recognizable as plausible inputs — and whether the local model fits well. Both can fail silently.

In plain words: Off-manifold means the slightly changed inputs LIME tries are no longer recognizable as plausible inputs. When that happens the coefficient LIME gives you is unreliable, and it does not warn you.

Example: LIME returns a coefficient with no flag saying it is unreliable because the perturbations went off-manifold.

**silent failure of LIME**  *(also: fail silently)*
*line 243 · failure mode · learn, not on the exam*

> Both can fail silently. You get a coefficient. You don't get a flag that says "this coefficient is unreliable because the perturbations went off-manifold."

In plain words: LIME can go wrong without any warning: you get a coefficient but no flag saying it is unreliable. Both a perturbation distribution that does not match the data and a poor local fit can hide this way.

Example: A coefficient that looks fine but came from implausible perturbed inputs.

**local explanation does not generalize**
*line 245 · failure mode · learn, not on the exam*

> It does not show whether the local explanation generalizes. A nearby input may have a completely different LIME explanation, because the model is locally linear but globally nonlinear, and "locally" in the LIME sense is a smaller neighborhood than the practitioner's intuition tends to assume.

In plain words: A LIME explanation is only good near one input, and a nearby input can have a completely different explanation. The model is locally linear but globally nonlinear, and LIME's neighborhood is smaller than people tend to assume.

Example: Two nearby inputs to the same classifier getting different LIME explanations.

**LIME instability across runs**  *(also: LIME is not stable across runs)*
*line 249 · failure mode · learn, not on the exam*

> And — this is the awkward one — LIME is not stable across runs. Run the same input twice, and you can get different explanations, because the perturbations are sampled randomly. Most practitioners running LIME do not run it twice.

In plain words: Running LIME twice on the same input can give different explanations because the perturbations are sampled randomly. Most practitioners run it once and read that single result as the answer.

Example: Exercise A1: two runs on the same text input give different top features, and a manager asks which is correct.

**need and misalignment co-occur**  *(also: the case where we most need the explanation is the case where the model is misaligned)*
*line 251 · concept · other*

> If the model is misaligned — and the case where we most need the explanation is exactly the case where the model is misaligned — the explanation is a faithful description of the misalignment, presented in a format that looks like a description of the world.

In plain words: The chapter's working intuition: the cases where you most need an explanation are the cases where the model is misaligned with the world, and there the explanation faithfully describes the misalignment. The author flags it as an aphorism asserted more than proved, not a theorem.

Example: Exercise S4 asks why misalignment creates the need for explanation and also degrades the reliability of SHAP and LIME.

**counterfactual explanation**  *(also: counterfactual; counterfactuals)*
*line 267 · method · exam focus*

> Counterfactual explanations. Instead of "feature X contributed +0.3 to the prediction," the explanation is: "if feature X had been at value Y instead, the prediction would have been Z."

In plain words: A counterfactual explanation says how the prediction would change if a feature had a different value, rather than how much the feature contributed. It is closest to the practitioner's real question of what the model would do under a different scenario.

Example: If your income were $5,000 higher, the loan would be approved.

Not to be confused with: SHAP attribution (a Rung 1 statement)

**multiple counterfactuals**
*line 271 · failure mode · exam focus*

> Multiple counterfactuals are usually possible — there are many ways to flip the prediction, and the explanation method picks one (usually the closest in some metric) without justifying why that closest counterfactual is the relevant one for the practitioner.

In plain words: There are usually many ways to flip a prediction, and the method picks one, often the closest, without justifying why it is the one that matters to the practitioner.

Example: Raising income by $5,000 is one way to flip a loan decision among several.

**the model's counterfactual, not the world's**  *(also: Rung 2 in the model is not Rung 2 in the world; treated as a causal statement about reality rather than the model)*
*line 271 · failure mode · exam focus*

> The counterfactual is the model's counterfactual, not the world's: if the model is misaligned with the world, the counterfactual tells you what the model would do in the hypothetical, not what would actually happen.

In plain words: A counterfactual explanation tells you what the model would predict if an input changed, not what would really happen in the world. If the model is misaligned with the world, the two can differ.

Example: 'If income were $5,000 higher the prediction would flip' describes the model's behavior, not the lender's correct decision.

**actionability is not correctness**
*line 271 · concept · exam focus*

> And actionability is not the same as correctness — a counterfactual that says "if your income were $5,000 higher, the loan would be approved" is actionable, but it isn't necessarily a correct description of what the lender's decision should be. Only what the model's decision would be.

In plain words: A counterfactual can tell you something you can act on without telling you what the right decision is. It describes what the model's decision would be, not what the lender's decision should be.

Example: If your income were $5,000 higher, the loan would be approved.

**what explanation tools are good for**
*line 387 · concept · exam focus*

> Explanation tools work if you value a consistent, auditable description of what the model did.

In plain words: Explanation tools suit the need for a consistent, auditable description of what the model did. They fail if you need to know whether the model is right about the world, which is usually the actual question.

Example: SHAP gives the same kind of accounting for every prediction, which is auditable but silent on whether the model is right.

**transparency**
*line 287 · concept · exam focus*

> Transparency is a property of the system. A transparent system is one whose internals are inspectable — code, parameters, architecture, training data, all available to look at. Transparency is, in principle, binary: either the internals are inspectable or they aren't.

In plain words: Transparency means the system's insides can be inspected: code, parameters, architecture and training data. It is about access, not understanding, and in principle it is yes-or-no.

Example: A system with 175 billion parameters whose code, weights and training data you hold is fully transparent yet uninterpretable.

Not to be confused with: explainability and interpretability (the three do not entail each other)

**explainability**
*line 289 · concept · exam focus*

> Explainability is a property of outputs. An explainable output is one accompanied by a reason. SHAP, LIME, and counterfactuals are explainability tools.

In plain words: Explainability means each output comes with a stated reason for it. SHAP, LIME and counterfactuals produce such reasons, but the reasons may be more or less informative.

Example: SHAP attributions on every prediction make a system explainable, yet the practitioner may still be unable to build a coherent mental model from them.

Not to be confused with: interpretability (procurement language often asks for explainability and means interpretability for the affected user)

**interpretability**
*line 291 · concept · exam focus*

> Interpretability is a property of the understanding a human builds from the explanations. An interpretable system is one a human can build a working mental model of, sufficient to predict the system's behavior in novel cases.

In plain words: Interpretability means a person can build a working mental model of the system, good enough to predict what it will do on new cases. It depends on who is reading, so one system can be interpretable to some people and not to others.

Example: A system can be interpretable to the developer and not to the loan applicant.

Not to be confused with: explainability (meeting a SHAP-attribution requirement does not make a system interpretable to the affected user)

**transparency, explainability and interpretability do not entail each other**  *(also: do not entail each other)*
*line 293 · concept · exam focus*

> They do not entail each other. A system can be fully transparent — you have the code, the weights, the training data — and entirely uninterpretable, because there are 175 billion parameters and inspecting weights does not produce understanding. A system can produce explanations — SHAP attributions for every prediction — and remain uninterpretable, because the practitioner cannot build a coherent mental model out of the attributions.

In plain words: Having one of the three properties does not give you the others: a system can be transparent or explainable and still uninterpretable. A system can also be interpretable to one audience and not another.

Example: Open weights and 175 billion parameters; or SHAP attributions the practitioner cannot turn into a mental model.

**common failure mode of the three properties**  *(also: transparent, explainable and interpretable only to the developer)*
*line 306 · failure mode · exam focus*

> A system that is transparent, explainable, and interpretable to the developer — and none of those things to the patient or loan applicant reading the output

In plain words: The table's common failure mode is a system that has all three properties for the developer and none of them for the patient or loan applicant who reads the output. It shows that the three properties depend on the audience, not only on the system.

Example: A model the developer can inspect, explain and follow, whose output a patient or loan applicant cannot use.

**signing off on the wrong property**  *(also: explainability requirement met, interpretability absent)*
*line 295 · failure mode · exam focus*

> The explainability requirement has been met. The interpretability remains absent. Somebody has signed off on the wrong property.

In plain words: Contracts and regulations often ask for explainability but really need interpretability for the affected user. A vendor can meet the explainability requirement while the interpretability the user needs is still absent.

Example: Exercise A2: a sepsis-risk contract requires an explainable reason and the vendor ships SHAP attributions.

**Rudin's argument**  *(also: inherently interpretable models)*
*line 295 · named result or case · exam focus*

> Rudin's argument that high-stakes decisions should use inherently interpretable models rather than post-hoc explanations of black boxes lands exactly here.

In plain words: Rudin argues that for high-stakes decisions you should use models that are interpretable by design instead of explaining a black box after the fact. The chapter says this fits the gap between meeting an explainability requirement and giving the affected person something they can use.

Example: A loan applicant, patient or defendant who needs a reason they can use, not a SHAP attribution on a black box.

Not to be confused with: post-hoc explanation

**explainable to whom?**  *(also: explanation is a property of the system and the audience)*
*line 297 · method · exam focus*

> An attribution that the developer can read is not the same artifact as a reason the affected person can use. Explanation is not a property of the system alone. It is a property of the system and the audience.

In plain words: When someone says a system is explainable, ask who the explanation is for. An attribution a developer can read is not the same as a reason an affected person can use.

Example: SHAP output the developer can read but the loan applicant cannot use.

**language game**  *(also: Wittgenstein's language game)*
*line 314 · framework · other*

> Wittgenstein had this observation that the meaning of a word depends on the language game in which it is being used. The same word can do different work in different contexts. The same sentence can be true in one game and false in another.

In plain words: A language game is the context in which words get their meaning, so the same word can mean different things in different contexts. The chapter uses it to say the same explanation can be correct in one game and misleading in another.

Example: 'Deleted' means local actions in the agent's game and 'no longer accessible to anyone' in the user's game.

**Ash case**  *(also: Ash's agent; the secret has been deleted; Agents of Chaos (source study))*
*line 341 · named result or case · other*

> Ash asks for the deletion of a sensitive email. The agent issues a sequence of commands that, in the local environment, constitute a deletion: it resets the password, renames an alias, possibly archives the message locally. The agent reports: the secret has been deleted.

In plain words: An autonomous coding-and-shell agent with privileged email access is asked to delete a sensitive email, takes actions that count as deletion locally, and reports the secret deleted while the data persists on the provider's servers. The chapter uses it as its main language-game example.

Example: Local game: password reset, alias renamed, message archived locally. User's game: data no longer accessible to anyone.

**language-game mismatch**  *(also: mismatch between language games; the local game and the user's game)*
*line 321 · failure mode · other*

> The agent's language game was different from the user's. The user, reading the report, applied the user's language game to it. The mismatch produced the failure.

In plain words: A language-game mismatch happens when a report is read in a different game than the one it was written in, so the same words describe different operations. The mismatch, not a lie, produces the failure.

Example: The agent said 'deleted' in its local game; the user read it as deleted at the provider.

Not to be confused with: lying (the agent did not lie)

**the model's language game versus the practitioner's**  *(also: SHAP operates in the model's language game)*
*line 323 · concept · other*

> SHAP operates in the model's language game — the game of feature attribution in an internal accounting. The practitioner, reading the SHAP output, applies the practitioner's language game — the game of which features matter for the decision in the world. The two games may use the same words ("important feature," "driver of the prediction") for different operations.

In plain words: SHAP speaks in the model's game, which is attribution inside the model's accounting, but the practitioner reads it in a game about which features matter in the world. The same words, such as important feature, can then mean different things.

Example: A high SHAP attribution to zip code read as 'zip code is a driver of the decision in the world.'

**audience question**  *(also: supervisory check; the supervisory move)*
*line 325 · method · other*

> The supervisory move, then, is a question. Who is the audience for this explanation, what language game are they operating in, and does the explanation method serve that game? If the explanation was generated for one audience and is being read by another, the explanation may be doing the wrong work, even when it is technically correct.

In plain words: The audience question asks who is reading an explanation, what language game they are in, and whether the explanation method serves that game. It is the supervisory check that can catch an explanation that is technically correct but written for someone else.

Example: For Ash: 'Who is reading this report, and what does deleted mean in their language game?'

**failure in the report, not the decision**  *(also: report failure)*
*line 349 · failure mode · other*

> First, the failure is not in the model's decision. The agent did what it was capable of doing. The failure is in the report — the explanation of what was done — which used a word ("deleted") whose meaning straddled two language games and committed to the local one without flagging the gap.

In plain words: In the Ash case the agent's actions were fine; what failed was its report, which used a word whose meaning differs between two language games and did not flag the gap. The problem lay in the explanation of the action, not the action.

Example: The report said 'deleted'; a careful report would add that the data may persist on the provider's servers.

**attribution methods cannot detect language-game mismatch**  *(also: modeling the audience)*
*line 351 · concept · other*

> The attribution would have correctly identified that the agent's actions caused the local state changes. The attribution would have been correct in the local game. Attribution methods do not detect language-game mismatch — that detection requires modeling the audience of the explanation, which feature-attribution methods do not do.

In plain words: A SHAP or LIME attribution on the Ash agent would have been correct in the local game and still missed the mismatch. Detecting it requires modeling the audience of the explanation, which feature-attribution methods do not do.

Example: No attribution method would have flagged that 'deleted' meant something different to Ash.

**Glimmer**
*line 369 · method · other*

> A Glimmer is a longer, higher-stakes exercise that requires going to primary sources. Do not abridge this one.

In plain words: A Glimmer is a longer, higher-stakes exercise that sends you to primary sources, and the chapter says not to abridge it. Glimmer 5.1 tests whether a real tool's explanation is practically misleading.

Example: Glimmer 5.1: take a deployed AI tool, pull its explanation for a recent decision, and lock your prediction before investigating.

**practically informative, neutral or misleading**  *(also: lock your prediction)*
*line 374 · framework · exam focus*

> Lock your prediction: given the explanation, is it likely to be (a) practically informative — leading to a better decision than no explanation, (b) practically neutral — providing color but not changing decisions, or (c) practically misleading — leading to a worse decision than no explanation? State your prediction with stakes.

In plain words: A three-way test of what an explanation does to a decision: informative (better than none), neutral (colour only) or misleading (worse than none). You commit to a prediction before you investigate.

Example: Glimmer step 4: predict whether a tool's explanation for last week's decision is informative, neutral or misleading.

**scope mismatch**
*line 377 · failure mode · other*

> If the explanation was practically misleading, name the structural reason — was it a Rung 1 limitation, a language-game mismatch, a scope mismatch (the explanation was about the model and the user wanted information about the world)?

In plain words: A scope mismatch is when an explanation answers a question about the model but the user wanted information about the world. It is one of three structural reasons the chapter offers for a misleading explanation.

Example: A SHAP attribution describes the model's accounting while the user wants to know what is true in the world.

Not to be confused with: Rung 1 limitation; language-game mismatch (the other two structural reasons)

**structural reason**
*line 379 · concept · other*

> The deliverable is the case, the explanation, the prediction, the trace, and the structural reason. The grade is on the structural reason. A correct prediction with no structural account is worth less than an incorrect prediction that names the structural reason precisely.

In plain words: The structural reason is the specific mechanism that made an explanation misleading, such as a Rung 1 limitation, a language-game mismatch or a scope mismatch. The Glimmer is graded on naming it, not on whether the prediction was right.

Example: Naming 'Rung 1 limitation' for a SHAP attribution that was read as causal.

**residual gap**  *(also: supervisory territory)*
*line 389 · concept · other*

> Pearl's Rung 2 is the most useful framing for what a good explanation could do — what would happen if X were different? — but Rung 2 in the model is not Rung 2 in the world, and the residual gap is not a tooling defect to be patched. It is supervisory territory. It is yours.

In plain words: Even a good Rung 2 explanation is about the model's world, and the leftover gap between that and the real world cannot be fixed with better tools. The chapter says closing it is the human supervisor's job.

Example: A counterfactual from a loan model is still the model's counterfactual; judging whether it holds in the world is the supervisor's work.

**self-explanation audit**
*line 469 · method · other*

> A "self-explanation audit" of your agent — a side-by-side comparison of what the agent says it did versus what it actually did, with the language-game mismatches catalogued and the technically-accurate-practically-misleading patterns flagged.

In plain words: A self-explanation audit sets what an agent says it did next to what it actually did and logs the language-game mismatches. It flags reports that are technically accurate but practically misleading.

Example: For 5 to 10 tasks, capture the request, the agent's self-explanation, the actual tool calls and the ground-truth state.

**language-game audit**
*line 491 · method · other*

> LANGUAGE-GAME AUDIT — For each pair (self-explanation vs ground truth), identify:

In plain words: For each self-explanation compared with ground truth, find the language game the user is in, the game the agent is in, and where the two mismatch. The mismatch is where the Ash-style failure lives.

Example: What does the user read 'deleted', 'completed', 'verified' or 'checked' to mean?

**technically wrong / technically accurate-practically misleading / properly calibrated**  *(also: TECHNICALLY-WRONG; PROPERLY-CALIBRATED)*
*line 495 · framework · other*

> For each mismatch, classify it as: TECHNICALLY-WRONG (the agent's claim is just false), TECHNICALLY-ACCURATE-PRACTICALLY-MISLEADING (locally true, globally false), or PROPERLY-CALIBRATED (claim matches ground truth in user's language game).

In plain words: Each mismatch between an agent's claim and ground truth is sorted into one of three classes: simply false, locally true but globally false, or matching ground truth in the user's language game.

Example: Ash's 'deleted' report is locally true and globally false.

**attribution probe**
*line 497 · method · other*

> ATTRIBUTION PROBE — For one of the most consequential interactions, attempt a SHAP-style or counterfactual probe of WHY the agent acted as it did.

In plain words: An attribution probe tries to find out why an agent acted as it did by changing something and watching whether the action changes. The probe results describe the agent's internal accounting, not the world.

Example: Re-run the agent with one input element changed, one tool removed, or the request reframed as coming from a different role.

**counterfactual probe**
*line 498 · method · other*

> Counterfactual probe: re-run with a single input element changed; see if the action changes

In plain words: A counterfactual probe re-runs the agent after changing a single input element to see whether its action changes.

Example: Change one input element, re-run, and see whether the action changes.

Not to be confused with: tool-availability probe; authority probe

**tool-availability probe**
*line 499 · method · other*

> Tool-availability probe: re-run with one tool removed; see what the agent does instead

In plain words: A tool-availability probe re-runs the agent with one tool removed to see what it does instead.

Example: Remove one tool, re-run, and see what the agent does instead.

Not to be confused with: counterfactual probe; authority probe

**authority probe**
*line 500 · method · other*

> Authority probe: re-run with the request reframed as coming from a different role; see if the agent's threshold for action changes

In plain words: An authority probe re-runs the agent with the request framed as coming from a different role to see whether its threshold for acting changes.

Example: Reframe the same request as coming from a different role and see whether the agent's threshold for action changes.

Not to be confused with: counterfactual probe; tool-availability probe

**explanation risk class**  *(also: EXPLANATION RISK class)*
*line 505 · concept · other*

> a one-paragraph note for the casebook on the EXPLANATION RISK class — what kind of decision-maker, in what kind of deployment context, is most likely to be misled by this agent's self-explanations? Name the deployment scenario where this risk is unacceptable.

In plain words: The explanation risk class is a note on which kind of decision-maker, in which deployment context, is most likely to be misled by an agent's self-explanations. It ends by naming the scenario where that risk is unacceptable.

Example: A user who reads 'deleted' as deleted at the provider when the agent only acted locally.

## Chapter 6, Bias (111 terms)

**three engineering teams parable**  *(also: the three teams; Team One, Team Two, Team Three)*
*line 16 · named result or case*

> Same problem. Three honest engineering efforts. Three different theories of where the bias actually lived.

In plain words: A constructed story (a composite, not a reported case) in which three teams fix the same biased system: one changes the loss function, one rebuilds the dataset, one changes the human review process. Only the third, which changed the review process, cut the disparity by an order of magnitude; the first two made real but small reductions.

Example: Team One added a fairness penalty to the loss, Team Two recollected data for an underrepresented subgroup, Team Three changed how the human reviewer used the model's output.

**fairness penalty**  *(also: fairness constraint)*
*line 10 · method*

> They added a fairness penalty — a term that punishes the model whenever it produces different error rates across protected groups.

In plain words: An extra term added to the model's loss that punishes it whenever its error rates differ across protected groups. It is a model-side fix, so it blocks only the path that runs through the model's parameters and leaves the proxy and deployment-context paths open.

Example: Team One retrained on the same data with a fairness penalty; the disparity dropped a little, not enough.

**protected attribute**  *(also: protected groups)*
*line 283 · concept*

> Imagine the causal graph for how the bias appears in the deployed outcome. The protected attribute sits at the top. Below it are proxies — features in the data that correlate with the protected attribute.

In plain words: The characteristic that defines the groups whose outcomes are compared (race and sex in the chapter's examples). In the chapter's causal graph it is the variable at the top, where every bias-carrying path to the final outcome starts.

Example: Loan denial by race; a hiring model that predicts lower success scores for women.

**deployment context**  *(also: the room the model had been deployed into; downstream decision process)*
*line 283 · concept*

> Below that, the deployment context — the reviewer, the threshold, the appeal process.

In plain words: Everything around the model where its output actually gets used: the human reviewer, the threshold, the appeal process. It can carry or amplify bias even when the model and the data are left untouched.

Example: Team Three found the reviewer's own systematic patterns were being amplified by the model and fixed the review process, not the model.

**leverage**  *(also: low-leverage; high-leverage)*
*line 16 · concept*

> But they were low-leverage — correct interventions on a real path that happened to carry little of the bias. The third was high-leverage, and the rightness was not an accident.

In plain words: How much of the bias an intervention actually removes. A low-leverage fix is correct but acts on a path that carries little of the bias; a high-leverage fix acts on the path that carries most of it, and that is usually not the one closest to your hands.

Example: Changing the loss function or rebalancing the data was low-leverage; changing the review process dropped the disparity by an order of magnitude.

**ten bias mechanisms**  *(also: the ten; ten mechanisms; entry-point mechanisms)*
*line 46 · framework*

> The ten bias mechanisms covered in this chapter are ten distinct ways of introducing a nonzero value into the expression $E[\hat{\theta}] - \theta$. Each has a different causal structure, and the fix for each is different.

In plain words: Ten distinct ways a pipeline can end up with a nonzero value of E[estimate] minus the true value: selection, confirmation, observer, self-report, data-coding, publication, data-entry, sampling, historical and implicit bias. Each enters at a different point and needs a different fix, and implicit bias is the odd one out, a medium rather than an entry point.

Example: Confusing the mechanisms made Teams One and Two apply the right intervention at the wrong leverage point.

**Pearl's ladder**  *(also: ladder of causal reasoning; Pearl's Ladder; rungs)*
*line 240 · framework*

> The tool is due to Judea Pearl, and it is, in my judgment, the single most useful conceptual instrument in this book. He calls it a ladder of causal reasoning, with three rungs.

In plain words: Pearl's three levels of causal reasoning: Rung 1 is seeing what goes with what (association), Rung 2 is doing (intervention), Rung 3 is imagining what would have happened (counterfactual). Each rung asks a different kind of question, and evidence from a lower rung cannot answer the higher rung's questions.

Example: Rung 1: P(Y | X). Rung 2: P(Y | do(X = x)). Rung 3: what would have happened to this case if X had been different.

**correlates versus causes**  *(also: causal; causal fairness; causal discrimination)*
*line 20 · concept*

> And we need a small piece of formal apparatus, due to Judea Pearl, that lets us see the difference between a system that correlates the bias and a system that causes it.

In plain words: A system that correlates the bias just reproduces patterns that go together in the data (Rung 1), while a system that causes it would change the outcome when the variable is changed (Rung 2). Whether bias is caused by the variable in question is a Rung 2 question, and Rung 1 evidence cannot answer it.

Example: A Rung 1 disparity may vanish on Rung 2 when it is mediated entirely through legitimate features, so the decision is causally race-neutral.

Not to be confused with: correlation (an association is not a cause, and a Rung 1 disparity does not always mean causal discrimination)

**dataset bias**
*line 132 · failure mode*

> The bias is in the sample. Fix the sample, and in principle you fix the bias. Call this dataset bias.

In plain words: The training set did not represent the population the model is deployed on, so the bias lives in the sample and fixing the sample in principle fixes it. Selection bias, sampling bias and the sample-corruption form of data-entry bias produce it.

Example: Face recognition trained mostly on light-skinned faces and deployed on everyone.

Not to be confused with: label bias (causally distinct but observationally close when you only have the labeled training set)

**label bias**
*line 134 · failure mode*

> The model is dutifully predicting re-arrest, doing so accurately, and the prediction is biased because re-arrest is a biased measurement of the underlying thing we actually care about. Call this label bias. The mechanisms that produce it: observer bias, data coding bias, historical bias, and the label-corruption form of self-report bias.

In plain words: The training labels record a process that was itself biased, so the model accurately predicts a distorted stand-in for what you actually care about; the chapter calls it a measurement problem. Observer, data-coding, historical and (in its label-corruption form) self-report bias produce it.

Example: A recidivism predictor trained on re-arrest rather than crime inherits the patterns of past policing.

Not to be confused with: dataset bias (causally distinct but observationally close when you only have the labeled training set)

**structural bias**
*line 136 · failure mode*

> The bias is not in the model, not in the data. It is in the structure the model is being deployed into. No model fix touches it.

In plain words: The data and labels are fine and the model does its job, yet the system still produces unfair outcomes because the world it is deployed into was unequal to begin with. No model fix or data fix touches it; only changing the deployment structure (review process, decision criteria, institutional context) does.

Example: A hiring model that accurately predicts who succeeds at a company where mentorship, sponsorship and access to interesting projects were never distributed evenly across groups.

Not to be confused with: dataset bias (treating structural bias as a dataset problem moves the disparity zero)

**three flavors of bias**  *(also: three structural positions; dataset, label and structural bias)*
*line 130 · framework*

> When people say "the model is biased," they could mean any of three quite different structural positions, and the fix for each is different.

In plain words: A higher-level grouping of the ten mechanisms by which part of the pipeline they act on: the sample (dataset bias), the labels (label bias), or the world the model is deployed into (structural bias). Dataset bias is a sampling problem, label bias is a measurement problem, and structural bias is a question about the world the model lives in.

Example: Face recognition trained on light-skinned faces (dataset); recidivism trained on arrest records (label); a hiring model accurate under historically unequal conditions (structural).

**association**  *(also: Rung 1; the level of correlation)*
*line 252 · concept*

> Rung 1 — Association. The level of correlation. What is the probability of Y, given that we observe X?

In plain words: Seeing: noticing what goes together in the data, the probability of Y given that we observe X, written P(Y | X). It is the level of correlation, where most machine learning, calibration curves and most fairness metrics live, and where thinking about deployed AI quietly stops.

Example: Is the denial rate equal across racial groups in the data? Or: roosters crow and the sun rises, so sunrise is likely given that the rooster crowed.

Not to be confused with: intervention (Rung 2): observing X is not the same as making X happen, because an observed X can be tangled up with other things that move with it

**intervention**  *(also: Rung 2; the level of doing)*
*line 254 · concept*

> Rung 2 — Intervention. The level of doing. What is the probability of Y if we set X to a particular value?

In plain words: Doing: asking what happens to Y if we set X to a particular value instead of just watching it, written P(Y | do(X = x)). Doing severs the tangles that make an observed X move with other things, so it can show whether X is actually a cause.

Example: If we changed race while holding all other features fixed, would the loan denial rate change? Or: preventing the rooster from crowing does not stop the sunrise.

Not to be confused with: association (Rung 1): observing X is not the same as making X happen, and equal Rung 1 metrics do not certify causal fairness

**do(X = x)**  *(also: P(Y | do(X = x)); I made X happen)*
*line 254 · concept*

> Pearl writes this: $P(Y \mid \text{do}(X = x))$. The notation is doing real work. It distinguishes "I observed X" — which can be tangled up with all kinds of other things that move with X — from "I made X happen" — which severs those tangles.

In plain words: Pearl's notation for setting X to a value rather than observing it, so P(Y | do(X = x)) means the chance of Y when we make X equal x. It separates 'I observed X' (tangled up with other things that move with X) from 'I made X happen' (which severs those tangles).

Example: P(sunrise | do(rooster doesn't crow)) is still high, so the rooster was not the cause.

Not to be confused with: P(Y | X = x), the observational quantity (observing X rather than setting it)

**causal graph**  *(also: Pearl-style DAG)*
*line 305 · method*

> Draw the causal graph of how the bias appears in the deployed outcome. Variables: protected attribute, proxies, features used by the model, model output, downstream decision process, final outcome. Arrows: which variables cause which.

In plain words: A diagram of the variables from the protected attribute down to the final outcome, with arrows showing which variable causes which. Drawing the whole graph, including the deployment context, is what lets you see every path the bias can take.

Example: Protected attribute, then proxies, features, model output, deployment context (reviewer, threshold, appeal), final outcome.

**epistemic artifact**  *(also: the dataset as epistemic artifact; reading the dataset like a historian)*
*line 187 · framework*

> A dataset is not the world. I want you to feel how strong that statement is. A dataset is a recording of a slice of the world, made by particular people at a particular time using particular instruments for particular purposes.

In plain words: A dataset is a recording of a slice of the world, made by particular people, at a particular time, with particular instruments and purposes, and each of those leaves a fingerprint on it. Read it the way a historian reads an archive: what does it claim to represent, what does it actually represent, and what does it exclude?

Example: COMPAS: the data recorded re-arrest, not crime.

**accountable owner**  *(also: owner of a bias; owner)*
*line 350 · concept*

> Assigning the owner of a bias is not assigning blame to a person; it is naming the party who sits at the leverage point. Sometimes that is you (you chose the sample). Sometimes it is the labeling team (they set the annotation manual).

In plain words: The party who controls the node where the highest-leverage bias-carrying path starts, named so the fix can reach it, not to blame a person. It may be you, the labeling team, the deployment owner who built the review room, or the model provider who trained the constraint in.

Example: In Agents of Chaos Case #6 the owner is the model provider, because the bias sits in its training pipeline.

Not to be confused with: blame (the chapter says assigning the owner is not assigning blame)

**Rung 1 metrics cannot answer Rung 2 questions**  *(also: equal Rung 1 metrics do not certify causal fairness)*
*line 273 · named result or case*

> Equal Rung 1 metrics do not certify causal fairness. A Rung 1 disparity does not always mean causal discrimination. The two rungs answer different questions.

In plain words: A fairness metric computed on observed data (equal outputs, equal error rates) cannot tell you whether the bias is caused by the variable in question, which is a Rung 2 question. A model can look equal on Rung 1 and still diverge under intervention, or show a Rung 1 gap that vanishes on Rung 2.

Example: Is the denial rate equal across groups in the data (Rung 1) versus would it change if we intervened on race holding other features fixed (Rung 2)?

**fluency trap**  *(also: that fluency is the trap)*
*line 225 · failure mode*

> A note on a case I will not over-claim, because the fluency trap runs hardest on the cases that flatter your thesis.

In plain words: The danger that smooth, confident output (an AI's, your own, or a neat story about a case) gets accepted without doubt, and it runs hardest where the result flatters what you already believe. The chapter's answer is to check the claim hard and cite it only as far as the evidence goes, as with the Apple Card case.

Example: Apple Card is often cited as a bias case, but the regulator did not find unlawful disparate impact by sex.

**fluency**
*line 463 · concept*

> Get it in seconds — that fluency is the trap.

In plain words: How quickly and smoothly an AI hands you a finished-looking result. In this chapter that smoothness is exactly what tempts you to accept the output, so you are told to write down why you want to believe it.

Example: Asking an AI to assemble a small labeled dataset or a set of user personas and getting it in seconds (Exercise S4).

**counterfactual**  *(also: Rung 3; the level of imagining)*
*line 258 · concept*

> Rung 3 — Counterfactual. The level of imagining. What would have happened to this specific case if X had been different, holding everything else fixed?

In plain words: Imagining: asking what would have happened to this specific case if X had been different, with everything else held fixed. It is the deepest and hardest level to reach from data alone, and the chapter only names it here because Chapter 4 opened it and Chapter 12 closes it.

Example: Chapter 4's robustness gap is a Rung 3 question.

Not to be confused with: intervention (Rung 2 asks what happens if we set X; Rung 3 asks what would have happened to this specific case)

**fluent output**  *(also: believing your own fluent output)*
*line 26 · failure mode*

> A BUILD pass, where you conduct a persona/data build and hunt for where you let bias in (the hard part is not believing your own fluent output).

In plain words: A smooth, finished-looking result that you produced or generated yourself, which makes you reluctant to doubt it. The chapter says that not believing it is the hard part of hunting for where you let bias in.

Example: An AI-generated persona dataset that feels clean to you because you own it (Exercise S4).

**supervisory capacity**  *(also: supplying the meaning and the accountability the model cannot)*
*line 26 · framework*

> This chapter exercises one supervisory capacity — supplying the meaning and the accountability the model cannot — and it does so in two passes.

In plain words: The chapter's named skill: you supply the meaning and the accountability that the model cannot. It is used twice, once building (hunt for where you let bias in) and once auditing (trace where bias entered someone else's system and name the owner).

Example: The model builds fast, and you supply the suspicion.

**BUILD pass**  *(also: BUILD; persona/data build)*
*line 26 · method*

> A BUILD pass, where you conduct a persona/data build and hunt for where you let bias in (the hard part is not believing your own fluent output).

In plain words: A pass in which you build a persona set or dataset yourself (with an AI) and search for where you let bias in. The hard part is not trusting your own output just because it came out fluently.

Example: Exercise S4: ask an AI for a small labeled dataset or user personas, then walk it against the ten mechanisms and run the four-step leverage analysis.

Not to be confused with: AUDIT pass (you inherit a deployed system instead of building one)

**AUDIT pass**  *(also: AUDIT)*
*line 26 · method*

> And an AUDIT pass, where a deployed system lands on your desk and you trace where the bias entered and assign the owner (the hard part is reconstructing a process you never saw).

In plain words: A pass in which you inherit a deployed system, trace where the bias entered, and name the accountable owner. The hard part is reconstructing a process you never saw.

Example: Exercise C2: pick COMPAS, the Amazon resume screener or the health-cost-proxy algorithm, draw the causal graph and name the owner.

Not to be confused with: BUILD pass (you generate the artifact yourself)

**estimator**
*line 36 · concept*

> In statistics, bias is a property of an estimator — not a dataset, not a model, not a prediction. An estimator is any procedure for computing a quantity from data: a mean, a regression coefficient, a risk score, a classification output.

In plain words: Any procedure that computes a quantity from data, such as a mean, a regression coefficient, a risk score or a classification output. In statistics, bias belongs to this procedure, not to the dataset, the model or a single prediction.

Example: The sepsis model's estimator computes the average outcome among the patients you actually assembled.

**bias**  *(also: \text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta; bias as a property of an estimator)*
*line 38 · concept*

> Suppose the true quantity is $\theta$ — the real underlying rate, the true causal effect, the actual probability of an outcome. Your estimator is $\hat{\theta}$, the value you compute from data. Bias is:

In plain words: The gap between what an estimator returns on average over every dataset you might collect, E[estimate], and the true quantity theta, written Bias = E[estimate] − theta. Zero means it is not systematically off; the same idea shows up in selection bias as an average among the people included, E[Y | i ∈ S], that differs from the population average E[Y].

Example: The 1936 Literary Digest poll: 2.4 million responses predicted a Landon landslide while Roosevelt won by a landslide.

Not to be confused with: the newspaper meaning of bias (unfair, skewed, prejudiced), which the chapter says is not precise enough to do engineering with; and a changed conditional probability is not automatically unfair (a gap is a flag, not a verdict)

**biased estimator**  *(also: systematically off in one direction)*
*line 36 · concept*

> An estimator is biased if, in expectation across all possible datasets you might collect, it systematically returns a value different from the true underlying quantity you are trying to measure.

In plain words: An estimator is biased when, on average across all the datasets you might collect, it lands on a value different from the true quantity, always off the same way. More data narrows the scatter around that wrong value but does not move it.

Example: The 1936 Literary Digest poll: 2.4 million responses predicted a Landon landslide while Roosevelt won by a landslide.

Not to be confused with: an estimator that is merely wrong on one dataset (unbiased estimators can be wrong on any given dataset; bias is being systematically wrong)

**unbiased estimator**  *(also: unbiased)*
*line 42 · concept*

> If this quantity is zero, the estimator is unbiased — it might be wrong on any given dataset, but it is not systematically wrong. If it is nonzero, the estimator is biased: systematically off in one direction.

In plain words: An estimator whose bias E[estimate] − theta is zero: averaged over every dataset you might collect it lands on the true value, though it may miss on any one dataset. A nonzero bias means it is systematically off in one direction.

Example: Inverse probability weighting buys back an unbiased estimate when the variable driving selection was recorded.

Not to be confused with: an estimator that happens to be right on this dataset (unbiased allows being wrong on any given dataset)

**more data does not fix bias**  *(also: collecting more data will not fix a biased estimator; more data narrows the scatter, not the offset)*
*line 42 · named result or case*

> A biased estimator converges, with more data, to the wrong answer — with increasing confidence. More data narrows the scatter. It does not move the systematic offset.

In plain words: Adding data shrinks random scatter but leaves a systematic offset where it is, so a biased estimator ends up confidently wrong. The fix is to collect or weight differently, not to collect more of the same.

Example: The sepsis model trained on more data drawn by the same six-hour-lab query encodes the same exclusion more precisely.

**1936 Literary Digest poll**  *(also: Literary Digest poll)*
*line 44 · named result or case*

> It is precisely what happened in the 1936 Literary Digest presidential poll, which predicted a Landon landslide from 2.4 million responses — while Roosevelt won by a landslide.

In plain words: A huge poll (2.4 million responses) that predicted a Landon landslide when Roosevelt won by a landslide, because the pool it drew from (telephone owners, car owners, magazine subscribers) was skewed and non-response compounded it. Gallup, with a far smaller but better-drawn sample of about 50,000, called the race right.

Example: More data made the wrong answer more confidently wrong.

**frame**
*line 44 · concept*

> The sample was enormous. The frame was skewed — telephone owners, car owners, magazine subscribers, in the depths of the Depression — and non-response compounded it.

In plain words: The pool of people a sample is drawn from; if it leaves some people out or overweights others, the sample is skewed however large it is. The chapter names it but never gives it a formal definition.

Example: A remote-work survey pushed through LinkedIn overrepresents credentialed professionals.

Not to be confused with: the instrument (in sampling bias the chapter says the frame, not the instrument, is skewed)

**derived interaction**  *(also: compound; compound pattern; amplifying)*
*line 62 · concept*

> Those are not an eleventh and twelfth mechanism. They are derived interactions — named patterns that arise when two of the ten (or two structural effects downstream of the ten) act together. When you see them, read them as compounds, not as new primitives.

In plain words: A named pattern that arises when two of the ten bias mechanisms (or structural effects downstream of them) act together, such as Selection × Historical. It is not an eleventh mechanism, and if one bias is confirmed in your pipeline you should check the pairs marked amplifying first.

Example: Selection bias compounding historical bias: rebalancing the sample fixes the first and makes the second worse.

Not to be confused with: a new, eleventh mechanism (the chapter says they are not new primitives)

**Aggregation × Subgroup-mask**
*line 173 · failure mode*

> A pooled metric hides a subgroup the aggregation was designed to summarize over

In plain words: A pooled overall metric hides a subgroup that the aggregation was meant to summarize over, so that subgroup's problem is invisible in the headline number. The chapter lists it as an amplifying derived interaction, not a new mechanism.

**Linkage × Re-identification**
*line 176 · failure mode*

> Joining two anonymous tables reveals identity through unique field combinations

In plain words: Joining two tables that are each anonymous can reveal who someone is, because particular combinations of fields are unique. The chapter lists it as an amplifying derived interaction, not a new mechanism.

**selection bias**
*line 68 · failure mode*

> The estimator you built computes $E[Y \mid i \in S]$: the average outcome among the sample $S$ you actually assembled. The quantity you wanted was $E[Y]$, the average outcome in the population. Those two are equal on exactly one condition: that the probability of landing in the sample, $P(i \in S)$, is independent of the outcome $Y$.

In plain words: Who ends up in your sample depends on what happened to them (for example, a reasonable-sounding query drops the sickest patients), so the sample average no longer matches the population average. The estimate is biased before any parameter is fit, and more data drawn the same way only sharpens the wrong answer.

Example: The sepsis model: the query 'patients with a complete lab panel within six hours of admission' drops the patients too critical to have labs drawn, so the model underestimates their risk.

Not to be confused with: sampling bias (the accessibility special case: groups missing because they were hard to reach, not because of their outcomes)

**conditional probability**  *(also: P(Y | X); conditional distributions; given that we observe X)*
*line 252 · concept*

> The model learns conditional distributions from data: $P(Y | X)$. What happens, given what we see.

In plain words: The probability of Y once you know X, written P(Y | X): what happens given what we see. It is what most machine learning learns, and it is what most fairness metrics compare across groups.

Example: The sepsis model learns what predicts sepsis among patients stable enough to be tested, which is a conditional average, not the average over all patients.

Not to be confused with: a changed conditional probability is not automatically unfair: a gap between groups is a flag, not a verdict, since real base-rate differences produce the same gap

**E[Y | i ∈ S] versus E[Y]**  *(also: the average outcome among the sample versus in the population; P(i ∈ S) independent of the outcome Y)*
*line 68 · concept*

> Those two are equal on exactly one condition: that the probability of landing in the sample, $P(i \in S)$, is independent of the outcome $Y$. The moment inclusion depends on what happened to a person, the two come apart, and your estimate is biased before a single parameter is fit.

In plain words: The average outcome among the people who made it into your sample, E[Y | i ∈ S], is not the average outcome in the population, E[Y], unless the chance of being included, P(i ∈ S), does not depend on the outcome. Once inclusion depends on what happened to a person, the two come apart and the estimate is biased before any parameter is fit.

Example: Sepsis model: the sickest patients are less likely to have labs in six hours, so inclusion depends on the outcome and the sample average understates risk.

Not to be confused with: E[Y], the population average the estimator was supposed to give

**filter that only lets some cases into the data (the sepsis model)**  *(also: the sepsis model; the six-hour filter; the survivors of an aggressive filter)*
*line 70 · named result or case*

> Take the sepsis model. The patients too critical to have labs drawn on time are the patients who most need the alert — and they are precisely the ones the six-hour filter drops. So the model learns what predicts sepsis among patients stable enough to be tested, and then it is asked about the unstable ones.

In plain words: A reasonable-looking query keeps only the cases that pass a filter (patients with a complete lab panel within six hours), so the model learns from the survivors of the filter and is then asked about the ones it dropped. The dropped patients were the sickest, so their risk is underestimated every time, and more data drawn the same way only sharpens the mistake.

Example: The six-hour lab filter drops patients too critical to have labs drawn on time, who most need the alert; inverse probability weighting lets the survivors of a filter stand in for those dropped, if the reason for dropping them was recorded.

**inverse probability weighting**
*line 72 · method*

> You can correct for observed selection: inverse probability weighting gives each retained observation a weight of $1/P(i \in S)$, so the survivors of an aggressive filter stand in for the people who were dropped; propensity score matching models inclusion as a function of covariates you can see and reweights on the estimated scores. Both moves buy you back an unbiased estimate — but only if the variable driving selection is one you recorded.

In plain words: A fix for selection bias: weight each person you kept by 1 divided by their selection probability P(i ∈ S), so the survivors of the filter stand in for the people who were dropped. It only works if the variable that drove the exclusion was recorded.

Example: Giving each patient who passed the six-hour lab filter a weight of 1 over their inclusion probability, which helps only if the reason others were dropped was recorded.

**propensity score matching**
*line 72 · method*

> You can correct for observed selection: inverse probability weighting gives each retained observation a weight of $1/P(i \in S)$, so the survivors of an aggressive filter stand in for the people who were dropped; propensity score matching models inclusion as a function of covariates you can see and reweights on the estimated scores. Both moves buy you back an unbiased estimate — but only if the variable driving selection is one you recorded.

In plain words: A second correction for observed selection: model who gets included as a function of covariates you can see, then reweight on the estimated scores. Like inverse probability weighting, it restores an unbiased estimate only if the variable driving selection was recorded.

Not to be confused with: inverse probability weighting (the other correction named in the same sentence)

**unobserved selection**  *(also: the thing that got people excluded is unobserved)*
*line 72 · failure mode*

> If the thing that got people excluded is unobserved, no weight recovers it, because you have nothing to weight on. That case is not a modeling problem you can solve at your desk. It is a data-collection problem, and the honest answer is to go collect differently, not to reach for a fancier estimator.

In plain words: When the variable that drove people out of the sample was never recorded, no reweighting can recover the missing people because there is nothing to weight on. It is a data-collection problem, so the honest answer is to collect differently rather than reach for a fancier estimator.

**biases that enter through the humans in the loop**  *(also: the five that enter through the humans in the loop; the family)*
*line 76 · framework*

> Five of the remaining mechanisms share a spine: somewhere a person exercises judgment, and their prior leaks into the record. Name them once and you can spot the family.

In plain words: Five mechanisms (confirmation, observer, self-report, data-coding and publication bias) in which a person's judgment lets their prior leak into the record. Because they enter upstream of the data, not through the model, the fixes are organizational practices, not machine learning.

Example: An annotator who knows a patient's prior diagnosis codes ambiguous notes as symptom-positive.

Not to be confused with: selection bias (the chapter says this family has a different leverage point from selection bias)

**confirmation bias**
*line 76 · failure mode*

> Confirmation bias is the researcher's prior shaping which data gets collected, kept, and reported — in Bayesian terms, an invisible multiplier greater than one on evidence that flatters the hypothesis and less than one on evidence that dents it, so the posterior drifts toward the prior instead of toward the world.

In plain words: The researcher's prior beliefs shape which data gets collected, kept and reported, as if evidence that flatters the hypothesis counted for more and evidence that dents it counted for less. The conclusion drifts toward the prior instead of toward the world.

Example: A team designs a study to confirm its hypothesis and gets a positive result, which then compounds with publication bias.

Not to be confused with: observer bias (the same prior, but localized to a single measurement act)

**observer bias**
*line 76 · failure mode*

> Observer bias is that same prior localized to a single measurement act: the annotator who knows a patient's prior diagnosis and codes ambiguous notes as symptom-positive, so the labels quietly learn to predict past diagnosis rather than current state.

In plain words: A labeler's prior leaks into a single measurement or label, so the labels learn to track what the labeler already believed instead of the real state. A kappa that collapses when you unblind the annotators is direct evidence of it.

Example: The annotator who knows a patient's prior diagnosis codes ambiguous notes as symptom-positive, so the labels predict past diagnosis rather than current state.

Not to be confused with: data-coding bias (disagreement clustered on specific annotators points to observer bias; clustered on specific items points to data-coding bias)

**self-report bias**
*line 76 · failure mode*

> Self-report bias is the subject's own prior doing the leaking — people report voting more, drinking less, exercising more than they do, and the error runs toward social desirability, not randomly.

In plain words: People's reports about themselves are distorted in a consistent direction (voting more, drinking less, exercising more than they do), not randomly. When there is no external gold standard, you label the data as self-reports and name the likely direction of distortion.

Example: People say they vote more, drink less and exercise more than they really do.

Not to be confused with: random noise (the chapter says the error runs toward social desirability, not randomly)

**social desirability**
*line 76 · concept*

> Self-report bias is the subject's own prior doing the leaking — people report voting more, drinking less, exercising more than they do, and the error runs toward social desirability, not randomly.

In plain words: The pull that makes people's self-reports drift in one consistent direction (flattering themselves) instead of erring randomly. It is the direction of the distortion in self-report bias.

Example: Reporting voting more, drinking less and exercising more than you actually do.

Not to be confused with: random noise

**data-coding bias**  *(also: data coding bias)*
*line 76 · failure mode*

> Data-coding bias enters one step later, when qualitative material is squeezed into categories: is "not bad" positive or neutral? which diagnosis code fits? Where the mapping needs judgment, systematic miscoding follows the judgment.

In plain words: Systematic miscoding that appears when judgment is needed to squeeze qualitative material into categories. A kappa that is low on specific items rather than specific people points to it, because the category is underspecified, not the coder.

Example: Is 'not bad' positive or neutral? Which diagnosis code fits?

Not to be confused with: observer bias (annotator priors distorting judgments rather than a poorly defined category)

**publication bias**
*line 76 · failure mode*

> And publication bias is the same leak at the scale of a literature: significant results get submitted, accepted, cited; nulls die in drawers, so a meta-analysis computes $E[\hat{\theta} \mid \text{published}]$ and reads an effect inflated by the censoring.

In plain words: Significant results get submitted, accepted and cited while null results stay in drawers, so a meta-analysis of the published literature reads an effect inflated by that censoring. A funnel plot with a missing lower-left corner makes it visible.

Example: A meta-analysis whose funnel plot is missing the lower-left corner of small null studies.

**E[theta-hat | published]**  *(also: E[\hat{\theta} \mid \text{published}])*
*line 76 · concept*

> And publication bias is the same leak at the scale of a literature: significant results get submitted, accepted, cited; nulls die in drawers, so a meta-analysis computes $E[\hat{\theta} \mid \text{published}]$ and reads an effect inflated by the censoring.

In plain words: A meta-analysis can only average the studies that got published, so it computes the estimate conditional on being published, E[estimate | published], not the estimate over every study done. Because significant results get through and nulls do not, that conditional average reads an effect inflated by the censoring.

Example: A funnel plot with the lower-left corner of small null studies missing.

Not to be confused with: the average effect over every study done, including the nulls that stayed in drawers

**Cohen's kappa**  *(also: inter-rater reliability measure; agreement corrected for chance)*
*line 78 · metric*

> The diagnostic, wherever two humans code the same thing, is Cohen's kappa — agreement corrected for chance,

In plain words: A score for how much two people who label the same thing agree, once the agreement expected by chance is removed (kappa = (P_o − P_e) / (1 − P_e)). Where it drops tells you which human-in-the-loop bias you have: a collapse when annotators are unblinded points to observer bias, and low agreement on specific items points to data-coding bias.

Example: If disagreement clusters on specific annotators it is more likely an observer problem; if it clusters on specific items it is more likely a coding problem.

**funnel plot**
*line 82 · method*

> For publication bias the analogue is the funnel plot: effect size against precision should form a symmetric inverted funnel, and a missing lower-left corner is the drawer of unpublished small-null studies made visible; trim-and-fill imputes them back.

In plain words: A chart of each study's effect size against its precision, which should look like a symmetric upside-down funnel. A missing lower-left corner shows the small null studies that were never published, which is the sign of publication bias.

Example: A meta-analysis funnel with the lower-left corner empty.

**trim-and-fill**
*line 82 · method*

> For publication bias the analogue is the funnel plot: effect size against precision should form a symmetric inverted funnel, and a missing lower-left corner is the drawer of unpublished small-null studies made visible; trim-and-fill imputes them back.

In plain words: A correction that adds back (imputes) the missing small null studies that the funnel plot shows are absent. It fixes only the publication part of an inflated meta-analytic estimate, not a study that was designed to confirm its hypothesis.

Example: Confirmation bias plus publication bias in one meta-analysis: trim-and-fill addresses the publication component but cannot address the study-design component.

**external gold standard**  *(also: ground truth)*
*line 82 · concept*

> For self-report, the diagnostic is an external gold standard — medical records, purchase data — and when none exists, which is most of the time, the discipline is not to launder the self-reports into ground truth but to label them as self-reports with the likely direction of distortion named.

In plain words: An independent record of what really happened, such as medical records or purchase data, that self-reports can be checked against. When none exists, do not treat self-reports as ground truth; label them as self-reports and name the likely direction of distortion.

Example: Medical records or purchase data as the check on what people say about their own behavior.

**laundering**  *(also: launder the self-reports into ground truth; laundering it through an algorithm)*
*line 223 · failure mode*

> A model trained on that data, deployed without that frame, makes the unevenness invisible by laundering it through an algorithm.

In plain words: Passing uneven data through a model so that its unevenness stops being visible and looks like a neutral algorithmic output. The chapter also warns against laundering self-reports into ground truth.

Example: COMPAS: a model trained on re-arrest data and deployed without the frame that re-arrest is shaped by policing.

**pre-registration**
*line 84 · method*

> So the interventions look like organizational practice, not machine learning: pre-registration that commits to the hypothesis before outcomes are seen; blinding that strips from the labeler any cue about the "right" answer; adversarial review that pays someone to find the disconfirming case.

In plain words: Committing to the hypothesis before the outcomes are seen, so the prior cannot steer which data is collected, kept or reported. It is one of three organizational fixes for the human-in-the-loop biases.

**blinding**
*line 84 · method*

> So the interventions look like organizational practice, not machine learning: pre-registration that commits to the hypothesis before outcomes are seen; blinding that strips from the labeler any cue about the "right" answer; adversarial review that pays someone to find the disconfirming case.

In plain words: Stripping from the labeler any cue about the right answer, so their prior cannot leak into the label. Agreement that collapses when annotators are unblinded is direct evidence of observer bias.

Example: Keeping annotators from seeing a patient's prior diagnosis.

**adversarial review**
*line 84 · method*

> So the interventions look like organizational practice, not machine learning: pre-registration that commits to the hypothesis before outcomes are seen; blinding that strips from the labeler any cue about the "right" answer; adversarial review that pays someone to find the disconfirming case.

In plain words: Paying someone to find the case that disconfirms your result, so the prior does not go unchallenged. It is one of three organizational fixes, and the cost is process discipline: meetings, protocols and slower annotation.

**data-entry bias**  *(also: data entry bias)*
*line 88 · failure mode*

> Data-entry bias is patterned transcription error — not random slips, but errors that track something. A form that demands a diagnosis code and buries the accurate one three menus deep gets the nearest code instead, and a whole class of conditions is undercoded in one direction. The tell: it changes neither who is in the sample nor how outcomes are labeled, only whether the recorded value for an already-enrolled person matches reality.

In plain words: Transcription errors that follow a pattern instead of being random slips, such as a form that buries the accurate diagnosis code so the nearest code gets entered. It changes neither who is in the sample nor how outcomes are labeled, only whether the recorded value for an enrolled person matches reality.

Example: A form that buries the accurate diagnosis code three menus deep, so a whole class of conditions is undercoded in one direction.

Not to be confused with: random noise (the chapter says people confuse it with 'just noise')

**verify against source documents**  *(also: outlier scans; consistency checks)*
*line 88 · method*

> You catch it with outlier scans on numeric fields and consistency checks on categorical ones — and you verify against source documents rather than auto-correct, because a real extreme value and a fat-fingered one demand opposite responses, and the tool cannot tell them apart.

In plain words: When an outlier scan or consistency check flags an odd value, check it against the original document instead of fixing it automatically. A real extreme value and a typing slip need opposite responses and the tool cannot tell which is which.

Example: An extreme numeric value that could be real or fat-fingered.

Not to be confused with: auto-correcting the flagged value

**sampling bias**
*line 88 · failure mode*

> Sampling bias is the accessibility special case of selection bias: subgroups are underrepresented not because of their outcomes but because they were hard to reach. A remote-work survey pushed through LinkedIn overrepresents credentialed professionals — the frame, not the instrument, is skewed.

In plain words: A special case of selection bias in which subgroups are underrepresented because they were hard to reach, not because of their outcomes. It earns its own name because the fix differs: when outside data gives the true group sizes, you reweight.

Example: A remote-work survey pushed through LinkedIn overrepresents credentialed professionals.

Not to be confused with: selection bias (there, inclusion depends on what happened to the person)

**reweighting by stratum**  *(also: reweight; w_i = (N_i/N)/(n_i/n))*
*line 88 · method*

> It earns its own name because the fix differs: when external population data tells you the true stratum sizes, you reweight, $w_i = (N_i/N)/(n_i/n)$, so an underrepresented stratum counts for more than one. More LinkedIn responses only sharpen the wrong answer.

In plain words: When outside population data gives the true size of each group, weight each respondent by the group's population share divided by its sample share, so underrepresented groups count for more than one. More responses from the same skewed frame would only sharpen the wrong answer.

Example: Weighting up the underrepresented strata of a LinkedIn-sourced remote-work survey.

**historical bias**
*line 92 · failure mode*

> No annotator erred. The data is a faithful recording of the world that produced it. And it is still poison.

In plain words: Skew that comes from the world itself, not from any data error: the sample is representative and the labels are accurate, yet the data faithfully records a world you did not want to reproduce. So there is no quality defect to fix, only a trade of some predictive fit for less inheritance of the past.

Example: A hiring model trained on ten years of promotion records at a company that promoted men into engineering roles at higher rates.

Not to be confused with: data-quality defects such as selection filters, miscoding and slips (the chapter says historical bias is none of these)

**accuracy is the harm**  *(also: its accuracy is the harm; every metric comes back green)*
*line 94 · concept*

> The thing the model got right is a world you did not want to reproduce. Its accuracy is the harm.

In plain words: A model can learn the historical pattern well and be accurate on its training distribution, so every metric you check comes back green, while it reproduces a world you did not want to reproduce. In historical bias the accuracy itself is the harm.

Example: A hiring model learns P(Y_historical | x) well, but that is not P(Y_fair | x).

**clean labels, clean pipeline reflex**  *(also: the reflex; the labels are clean, so the pipeline is clean)*
*line 94 · failure mode*

> This is why the reflex — "the labels are clean, so the pipeline is clean" — fails here: the labels record what happened, faithfully, and what happened was the problem.

In plain words: The mistaken habit of treating clean, accurate labels as proof that the pipeline is clean. In historical bias the labels faithfully record what happened, and what happened was the problem.

Example: Clean promotion labels at a company that promoted men at higher rates.

**P(Y_historical | x) versus P(Y_fair | x)**
*line 94 · concept*

> It learns $P(Y_{\text{historical}} \mid \mathbf{x})$ and learns it well — it is accurate on its training distribution, which is why every metric you check comes back green. But $P(Y_{\text{historical}} \mid \mathbf{x})$ is not $P(Y_{\text{fair}} \mid \mathbf{x})$. The thing the model got right is a world you did not want to reproduce.

In plain words: What the hiring model learns is the probability of the historical outcome given the features, such as who was promoted in the past, which is not the probability of a fair outcome given the same features. The model gets the first right, so it is accurate on its training distribution and still reproduces a world you did not want to reproduce.

Example: A hiring model trained on ten years of promotion records at a company that promoted men into engineering roles at higher rates.

Not to be confused with: P(Y_fair | x), the quantity you actually wanted

**mitigations for historical bias**  *(also: lower the leverage of the historical signal)*
*line 100 · method*

> So the corrections cannot be data-quality corrections; there is no quality defect to fix. They are all attempts to lower the leverage of the historical signal on the present prediction: swap in a less-biased proxy for the outcome, add a fairness constraint that penalizes reproducing the historical disparity, weight recent records over records from more discriminatory periods. Notice that not one of these claims to solve the problem — each one trades some predictive fit for less inheritance of the past, and you, not the loss function, have to decide how much fit you are willing to spend.

In plain words: Three partial fixes, none of them a cure: swap in a less-biased proxy for the outcome, add a fairness constraint, or weight recent records over those from more discriminatory periods. Each gives up some predictive fit for less inheritance of the past, and a person, not the loss function, must decide how much fit to spend.

Not to be confused with: data-quality corrections (the chapter says these are not that)

**fluent answer**  *(also: selling the fluent answer)*
*line 100 · failure mode*

> That is the whole trade, stated honestly. Anyone who tells you historical bias has a clean technical fix is selling the fluent answer.

In plain words: A smooth, reassuring answer that sounds complete but is not true: the claim that historical bias has a clean technical fix. Every real mitigation trades some predictive fit for less inheritance of the past, so an honest answer states the trade.

Example: Someone claiming a fairness constraint cleanly solves historical bias.

**proxy**  *(also: proxies; less-biased proxy for the outcome)*
*line 283 · concept*

> Below it are proxies — features in the data that correlate with the protected attribute. Below those, the features the model uses.

In plain words: A feature in the data that correlates with the protected attribute, so it can carry the attribute's influence to the model or straight into the deployment context. Some bias-carrying paths bypass the model by running through proxies.

Example: A zip code standing in for race (Exercise W2).

**implicit bias**
*line 110 · concept*

> The last one is not really a peer of the other nine, and pretending it is would be a category error. Implicit bias — the unconscious associations of the humans in the pipeline — is not an entry point. It is the medium several entry points swim in.

In plain words: The unconscious associations of the people in the pipeline. It is not an entry point itself but the medium several entry points swim in (it surfaces as confirmation, observer, data-coding and publication bias), so it has no single point to fix.

Example: A prior shaping which hypothesis you form (confirmation bias), what you observe (observer bias), how you categorize (data-coding bias) and what you submit (publication bias).

**downstream audit**  *(also: demographic parity; demographic parity auditing)*
*line 112 · method*

> The most tractable algorithmic handle is a downstream audit — check whether $P(\hat{Y}=1 \mid A=0) \approx P(\hat{Y}=1 \mid A=1)$ across protected groups — but read that result carefully: a gap is a flag, not a verdict, since real base-rate differences produce the same gap, and Chapter 7 is where that ambiguity gets its due.

In plain words: After the model is built, check whether the rate of positive predictions is about the same across protected groups. A gap is a flag that needs investigating, not a verdict, because real base-rate differences produce the same gap.

Example: Comparing P(Y-hat = 1 | A = 0) against P(Y-hat = 1 | A = 1) across protected groups after deployment.

Not to be confused with: proof of bias (a changed conditional probability is not automatically unfair: a gap is a flag, not a verdict, since real base-rate differences produce the same gap)

**structural interventions**  *(also: diverse teams; structured decision processes; continuous auditing)*
*line 112 · method*

> The interventions with actual leverage are structural: diverse teams, because a homogeneous team shares one water table and audits itself blind; structured decision processes, because structure shrinks the surface where an unexamined prior can act; and continuous auditing, because a source this diffuse is never fixed once.

In plain words: Because implicit bias has no single point to fix, the interventions with real leverage are structural: diverse teams, structured decision processes and continuous auditing. A homogeneous team shares one blind spot, structure shrinks where an unexamined prior can act, and a diffuse source is never fixed once.

Not to be confused with: a point intervention (the chapter says implicit bias resists one)

**base rate**  *(also: base rates; true recidivism rate)*
*line 197 · concept*

> Suppose Group 1 has a true recidivism rate of 30% and Group 2 has a true recidivism rate of 50%. A perfectly calibrated model assigns risk scores that reflect these true rates.

In plain words: The true rate of the outcome within a group, such as 30% recidivism in one group and 50% in another. When base rates differ across groups, calibration and equal error rates cannot both hold, and a gap between groups can reflect them rather than bias.

Example: Group 1 at 30% and Group 2 at 50% recidivism.

**leverage analysis**
*line 307 · method*

> For each candidate intervention point, ask: which paths does this intervention block, and which paths does it leave open?

In plain words: A four-step procedure: draw the causal graph, list all paths from the protected attribute to the outcome, ask for each candidate intervention which paths it blocks and which it leaves open, and pick the one that blocks the largest fraction of bias-carrying paths. It is the difference between mitigation that works and mitigation that produces conference papers and persistent disparities.

Example: Team A blocked the path through the model's parameters; Team C blocked the deployment-context path.

**biased measurement**  *(also: measurement problem; uneven measurement)*
*line 221 · failure mode*

> Re-arrest is a function of crime and policing. If policing is unevenly distributed across populations, then re-arrest is an uneven measurement of crime. And every model trained on that data inherits the unevenness.

In plain words: A recorded variable that stands in for the thing you actually care about but is distorted on the way, such as re-arrest standing in for crime when policing is uneven. Models trained on it inherit the unevenness, and the chapter calls label bias a measurement problem.

Example: Re-arrest as a measurement of crime: the COMPAS labels are 'was this person re-arrested?', not 'did this person commit a crime?'.

Not to be confused with: the true quantity it stands in for (re-arrest is not crime)

**structural amplification**
*line 136 · concept*

> Implicit bias, confirmation bias, and publication bias all contribute to structural bias — and structural bias can also accumulate from the compound effect of several dataset and label biases acting simultaneously over time.

In plain words: The name the chapter's table gives to a source of structural bias, alongside implicit and confirmation bias; the surrounding text says structural bias can accumulate from several dataset and label biases acting together over time. The chapter names it only in the table and never defines it separately.

**treating structural bias as a dataset problem**
*line 149 · failure mode*

> If you have structural bias and you treat it as a dataset problem, you will spend a quarter and move the disparity zero. This happens constantly. It is the most common failure in this whole field.

In plain words: Applying a sample fix such as resampling or more data to a bias that lives in the deployment structure, so the disparity does not move. The chapter calls it the most common failure in the field.

Example: Spending a quarter rebalancing the training data and moving the disparity zero.

Not to be confused with: dataset bias

**Selection × Historical**  *(also: selection bias compounding historical bias)*
*line 159 · failure mode*

> The most common compound pattern is selection bias compounding historical bias. The training data was collected from a biased sample (selection bias) during a historical period with discriminatory patterns (historical bias). The model's predictions are off for underrepresented groups in two distinct ways: it has less data about them, and the data it does have was generated under discriminatory conditions.

In plain words: The most common compound: the data came from a biased sample during a discriminatory period, so underrepresented groups get both less data and data generated under discriminatory conditions. Rebalancing the sample fixes the first problem and makes the second worse.

Example: Rebalancing the sample gives you more historically discriminatory data, accurately represented.

**Observer × Data-coding**  *(also: observer bias compounds with data coding bias)*
*line 161 · failure mode*

> Observer bias compounds with data coding bias in annotation pipelines. Annotators have systematic priors (observer bias), and those priors become embedded in the categories applied consistently across the dataset (data coding bias). The inter-rater reliability measure captures the combined effect but cannot separate the two.

In plain words: Annotators' systematic priors become embedded in the categories applied consistently across the dataset, so inter-rater reliability captures the combined effect but cannot separate the two. Disagreement clustered on specific items suggests a poorly defined category; clustered on specific annotators suggests priors distorting their judgments.

Example: Revise the manual (coding problem) or blind and retrain the annotators (observer problem).

**Confirmation × Publication**  *(also: confirmation bias compounds with publication bias)*
*line 163 · failure mode*

> Confirmation bias compounds with publication bias when a team designs a study to confirm their hypothesis, produces a positive result, and the result gets published while null results from other groups do not. The meta-analytic estimate is inflated by both processes simultaneously. The trim-and-fill correction addresses the publication component; it cannot address the study-design component.

In plain words: A team designs a study to confirm its hypothesis and gets a positive result, which is published while other groups' null results are not, so the meta-analytic estimate is inflated by both processes at once. Trim-and-fill fixes only the publication component, so both need to be named.

Example: A confirming study published while other groups' nulls stay in drawers.

**bias-carrying path**  *(also: overlapping paths; paths from the protected attribute to the outcome)*
*line 295 · concept*

> Some paths run through the model. Some bypass the model — they run through the proxies into the deployment context directly. Some are mediated by the reviewer, by the way the score is read, by what gets appealed and what does not.

In plain words: A route through the causal graph by which the protected attribute's influence reaches the final outcome: through the model, around it via proxies, or through the deployment context. An intervention helps only for the paths it blocks, and when two bias types' paths overlap, blocking one without the other leaves the bias carrying through.

Example: Team A blocked only the path through the model's parameters, leaving the proxy and deployment-context paths open.

**Sampling × Measurement**
*line 172 · failure mode*

> A non-representative sample combined with a noisy proxy yields error in two directions at once

In plain words: A non-representative sample combined with a noisy proxy produces error in two directions at once. The chapter lists it as an amplifying derived interaction, not a new mechanism.

**Evaluation × Deployment**
*line 174 · failure mode*

> Test-set composition unlike deployment population produces overconfident generalization

In plain words: A test set whose composition differs from the population the model is deployed on produces overconfident generalization. The chapter lists it as an amplifying derived interaction, not a new mechanism.

**Annotation × Class-imbalance**
*line 175 · failure mode*

> Rare-class boundary is exactly where annotator disagreement is highest

In plain words: The boundary of a rare class is exactly where annotators disagree most, so labeling error and class imbalance amplify each other. The chapter lists it as an amplifying derived interaction, not a new mechanism.

**COMPAS**  *(also: COMPAS recidivism data)*
*line 189 · named result or case*

> Take the COMPAS recidivism data, a well-known case from Broward County, Florida, around 2013 and 2014. ProPublica, in 2016, published an analysis showing that a commercial risk-assessment tool used by courts in that jurisdiction made errors that fell unevenly across racial lines.

In plain words: A commercial risk tool whose errors ProPublica showed fell unevenly by race, while its maker Northpointe showed that within each risk-score bucket the re-offense rate was about the same across groups. Both analyses were correct because they measured different things, and the labels recorded re-arrest, not crime.

Example: Black defendants who did not re-offend were misclassified as high-risk more often than white defendants who did not; white defendants who did re-offend were misclassified as low-risk more often.

**calibration parity**
*line 191 · metric*

> Within each risk score bucket, they said, the actual rate of re-offense was about the same across groups. By that measure — calibration parity — the tool was fair.

In plain words: A fairness rule: P(Y=1 | score s, group a) is the same across groups at every score, so a score means the same thing for every group. It cannot hold together with equal false-positive and false-negative rates when base rates differ.

Example: Northpointe's defense of COMPAS: within each risk-score bucket the actual re-offense rate was about the same across groups.

Not to be confused with: equal error rates (equal FPR and FNR); neither is automatically the fair one, since the choice between them is a values claim

**impossibility theorem**  *(also: fairness impossibility; the fairness impossibility)*
*line 207 · named result or case*

> The general principle: when base rates differ across groups, you cannot simultaneously satisfy calibration parity, equal false positive rates, and equal false negative rates. Pick any two; the third is forced into violation.

In plain words: When groups have different base rates, no model can have calibration parity, equal false-positive rates and equal false-negative rates at once; pick any two and the third is forced into violation. All three hold together only if base rates are equal or prediction is perfect.

Example: COMPAS: ProPublica (unequal error rates) and Northpointe (equal calibration) were both correct.

**equal false-positive rate**  *(also: Equal FPR; equal false positive rates)*
*line 199 · metric*

> For the model to have equal false positive rates — to label non-reoffenders as high-risk at equal rates across both groups — it would need to draw the threshold in a different place for each group.

In plain words: A fairness rule: P(predicted positive | no outcome, group a) is the same across groups, so the cost of being wrongly flagged is shared equally. The chapter shows it cannot hold with calibration parity when base rates differ.

Example: ProPublica's COMPAS finding: Black defendants who did not re-offend were misclassified as high-risk more often than white defendants who did not.

Not to be confused with: calibration parity

**equalized odds**  *(also: equalized error rates)*
*line 205 · metric*

> Hold PPV $v$ equal across two groups with base rates $p_a \neq p_b$. Then the ratio $t/f$ must differ between groups. But equalized error rates demand $t_a = t_b$ and $f_a = f_b$, which forces $t_a/f_a = t_b/f_b$.

In plain words: Equalized error rates: the true-positive rate and the false-positive rate are the same across groups. The chapter uses it in the impossibility algebra and names it in a citation and a preview; Chapter 7 works it through as one of three fairness definitions.

Not to be confused with: calibration parity (the two cannot both hold when base rates differ)

**equal false-negative rate**  *(also: Equal FNR; equal false negative rates)*
*line 231 · metric*

> The cost of being missed is shared equally

In plain words: A fairness rule: P(predicted negative | outcome, group a) is the same across groups, so among people who really do have the outcome the share the model misses is equal and the cost of being missed is shared equally. It is the third criterion that cannot hold with calibration parity and equal false-positive rates when base rates differ.

Example: ProPublica's COMPAS finding: white defendants who did re-offend were misclassified as low-risk more often than Black defendants who did.

**values claim**  *(also: not a technical choice)*
*line 209 · concept*

> Which means the choice between fairness metrics is not a technical choice. It is a values claim. Which kind of error are we less willing to make?

In plain words: Because no model can satisfy every fairness definition when base rates differ, choosing a metric means deciding which kind of error you are less willing to make. That has a social answer that depends on the model's use and who bears each error's cost, and engineers who treat it as pure optimization are secretly making a values choice.

Example: Optimizing for whatever metric the loss function encodes while appearing neutral.

Not to be confused with: a technical (mathematical) choice

**deepest dataset bugs**  *(also: mismatch between what the data is and what the modeler thinks it is)*
*line 223 · failure mode*

> This is what I mean by reading the dataset like a historian. The deepest dataset bugs are not data-quality issues in the QA sense. They are mismatches between what the data is and what the modeler thinks it is.

In plain words: The worst dataset problems are not defects a QA check would catch but a gap between what the data actually records and what the modeler believes it records. A model trained on such data, used without that frame, hides the gap.

Example: The modeler thinks they are predicting recidivism; they are actually predicting re-arrest, given recidivism, given policing.

Not to be confused with: data-quality issues in the QA sense

**Apple Card credit-limit controversy**  *(also: Apple Card)*
*line 225 · named result or case*

> The Apple Card credit-limit controversy (2019) is often cited as a bias case. It is more accurately a contested allegation: the New York Department of Financial Services investigated Goldman Sachs and reported that it did not find unlawful disparate impact by sex — applicants with similar credit characteristics generally had similar outcomes — faulting transparency and customer service instead. Cite it as an example of how a bias claim gets adjudicated, not as a proven disparity.

In plain words: A 2019 credit-limit controversy often cited as bias, but the New York regulator found no unlawful disparate impact by sex and faulted transparency and customer service. The chapter uses it as an example of how a bias claim gets adjudicated, not as a proven disparity.

Example: Applicants with similar credit characteristics generally had similar outcomes.

Not to be confused with: a proven bias case

**rooster and the sun**
*line 256 · named result or case*

> The sun rises anyway. Observation said they were associated. Intervention said the rooster was not the cause.

In plain words: Pearl's classic illustration of Rung 1 versus Rung 2: roosters crow and the sun rises together, but preventing the rooster from crowing does not stop the sunrise. Observation shows association; intervention shows the rooster is not the cause.

Example: P(sunrise | rooster crowed) is high, and P(sunrise | do(rooster doesn't crow)) is also high.

**observational quantity**  *(also: P(loan denial | race = x))*
*line 260 · concept*

> For our problem: $P(\text{loan denial} \mid \text{race} = x)$ is the observational quantity. This is what the model sees in training data. It is what most fairness metrics measure.

In plain words: The conditional probability you can read straight off the data, such as the loan denial rate among people of a given race, which is what the model sees in training and what most fairness metrics measure. It shows what goes with what, not whether the variable causes the outcome.

Example: The denial rate among applicants of each race in the training data.

Not to be confused with: interventional quantity (a Rung 1 gap in the data may vanish on Rung 2 and is not automatically discrimination)

**interventional quantity**  *(also: P(loan denial | do(race = x)))*
*line 260 · concept*

> $P(\text{loan denial} \mid \text{do}(\text{race} = x))$ is the interventional quantity. It asks: would the decision change if we changed only this variable, holding everything else fixed?

In plain words: The probability of the outcome when we set the variable to a value rather than observe it, such as loan denial if we changed only race and held everything else fixed. It answers whether the decision would change, which the observational quantity cannot.

Example: A model can show no Rung 1 disparity while a Rung 2 disparity appears when you intervene on race-correlated features.

Not to be confused with: observational quantity (observing race is not the same as setting it)

**merely smoothed model**  *(also: a model that is fair versus one that has merely been smoothed)*
*line 262 · failure mode*

> Without a way to distinguish the two, you cannot tell the difference between a model that is fair and a model that has merely been smoothed.

In plain words: A model whose metric has been adjusted until it looks equal on Rung 1 but which may still carry a Rung 2 disparity; without an intervention-level check you cannot tell it from a fair model. Most deployed bias-mitigation pipelines work on Rung 1, adjusting conditional distributions until the metric reads the way the engineer wants.

Example: Equal outputs across groups, but outputs diverge if you intervene on race-correlated features.

Not to be confused with: a model that is fair

**highest-leverage intervention**
*line 308 · concept*

> The highest-leverage intervention is the one that blocks the largest fraction of the bias-carrying paths, ideally without blocking paths the deployment requires for its core function.

In plain words: The intervention that blocks the largest fraction of the bias-carrying paths, ideally without cutting paths the deployment needs for its core function. It is often outside the model and the data, and sometimes outside your team.

Example: Team C's change to the review process.

Not to be confused with: the intervention closest to your hands

**Descartes' doubt turned on a pipeline**  *(also: Descartes' doubt)*
*line 314 · framework*

> Here is the classical move underneath the whole procedure, named explicitly because these moves earn their keep only when named: leverage analysis is Descartes' doubt turned on a pipeline. What would have to be true for this bias to live here? You suspend the tempting explanation — the model, the thing closest to your hands — and demand that each candidate location survive the question.

In plain words: The classical move under leverage analysis: for each candidate location, ask what would have to be true for the bias to live there, and suspend the tempting explanation (usually the model) until it survives the question. The location that survives is where you intervene.

Example: Suspending the model as the explanation and finding that the reviewer's pattern was where the bias lived.

**organizational boundary (your house versus someone else's)**  *(also: inside the engineer's house; crossing those boundaries)*
*line 324 · concept*

> The model and the data are inside the engineer's house. The reviewer's behavior, the appeals process, the way the score is interpreted — those live in someone else's house. Drawing the full graph means crossing those boundaries, and the engineer who tries is often told, gently or not, that this is not their job.

In plain words: The model and data sit inside the engineer's own house, while the reviewer's behavior, the appeals process and how the score is interpreted sit in someone else's. Leverage analysis needs the whole graph, so it means crossing those boundaries.

**the political dimension is the technical dimension**  *(also: political dimension of bias)*
*line 332 · concept*

> The political dimension of bias is engineering-relevant. It is not separate from the technical work. Which intervention point will work depends on which kind of bias you have, and which kind of bias you have depends on a structural analysis of the deployment.

In plain words: Which intervention will work depends on which kind of bias you have, and that depends on a structural analysis of the deployment, which is what people call the political. Engineers who skip it keep producing algorithm tweaks that do not move the disparity.

**problem formulation**
*line 334 · concept*

> The supervisory capacity for problem formulation — Chapter 1's vocabulary — is the capacity to see which question the model is actually being asked and which downstream decisions the answer feeds into. That capacity does not respect the boundary between technical and political.

In plain words: The capacity to see which question the model is actually being asked and which downstream decisions its answer feeds into. An engineer who keeps the technical and political separate does so by handing the formulation to someone else, which is a delegation that can be tested.

**Agents of Chaos Case #6 (Agents Reflect Provider Values)**  *(also: Agents of Chaos; Case #6)*
*line 342 · named result or case*

> The Agents of Chaos paper documents a scenario in Case #6 — Agents Reflect Provider Values — that is one of the cleanest examples of structural bias I have encountered: an agent whose behavior on contested questions silently reflected its model provider's training-time choices.

In plain words: The chapter's limit case: an agent's behavior on contested questions silently reflects its model provider's training-time choices, which the deploying organization did not make and its users cannot see. The bias-carrying path sits upstream of everything the deploying engineer controls.

Example: The deploying engineer's options are to switch providers, accept the bias, or add downstream filtering and validation.

**upstream leverage**  *(also: bias has a topology; the highest-leverage point is outside your reach)*
*line 346 · concept*

> The bias-carrying path is not in the deploying organization's data. It is not in their code. It is in the model provider's training pipeline — upstream of everything the deploying engineer controls.

In plain words: The highest-leverage bias-carrying path can start outside the deploying team, such as in a model provider's training pipeline, so nothing the team does inside its own pipeline can fix it. Bias has a topology, and the leverage analysis sometimes returns that the highest-leverage point is outside your reach.

Example: Agents of Chaos Case #6: no intervention by the deploying engineer can address the bias because the leverage is at the model provider.

**accountability move**  *(also: forensic skill; un-diffusing responsibility)*
*line 350 · method*

> The forensic skill is to trace the highest-leverage bias-carrying path to its source and name whoever controls that node — even when the honest answer is "not us." The leverage graph is a machine for un-diffusing responsibility: it points at a node, and a node has an owner.

In plain words: Trace the highest-leverage bias-carrying path to its source node and name whoever controls it, even when the honest answer is that it is not your team. The leverage graph points at a node, and a node has an owner.

Example: Naming the model provider as the owner in Agents of Chaos Case #6.

**diffused, role-bound responsibility**  *(also: Hannah Arendt's question)*
*line 350 · concept*

> (This is Hannah Arendt's question — systemic harm as the output of diffused, role-bound responsibility — restated for a pipeline; her mini-bio is in the book's Wayback series.)

In plain words: Arendt's question as the chapter restates it: systemic harm can be the output of responsibility spread across roles so that no one holds it. The leverage graph is the chapter's way of undoing that, by pointing at a node that has an owner.

Example: A pipeline with data brokers, annotators, modelers and deployers, none of whom feels accountable for the result.

**what would change my mind**
*line 358 · method*

> If a debiasing algorithm were demonstrated to robustly remove structural bias without intervention on the deployment context — across multiple domains and base-rate regimes — the leverage analysis framing in this chapter would need revision. I am not aware of such a demonstration.

In plain words: The chapter's stated falsifier: its leverage-analysis framing would need revision if a debiasing algorithm were shown to robustly remove structural bias without touching the deployment context, across several domains and base-rate regimes. The author says he knows of no such demonstration.

**dataset bias versus label bias with only the labeled training set**  *(also: still puzzling)*
*line 360 · concept*

> I do not have a clean diagnostic for distinguishing dataset bias from label bias when the only data you have access to is the labeled training set. The two are causally distinct but observationally close.

In plain words: The chapter's admitted open problem: dataset bias and label bias have different causes but look alike in a labeled training set alone. Telling them apart usually needs access to the labeling process, which other teams or organizations often control.

Example: Exercise A2: a recidivism training set whose only label is re-arrest within 3 years.

**lock your prediction**  *(also: lock a prediction)*
*line 381 · method*

> Lock your prediction: before reading the post-mortem and the proposed fixes, identify which of the ten bias mechanisms are active in your case. For each one, predict the highest-leverage intervention. Name the variable, name the type of intervention, predict the direction of effect.

In plain words: Before you read the post-mortem, write down which of the ten bias mechanisms you think are active and the highest-leverage intervention for each, naming the variable, the intervention type and the direction of effect. You then compare what the post-mortem actually proposed against that prediction.

Example: Glimmer 6.1 and Exercise C2 on a documented case such as COMPAS.

**gap analysis**
*line 383 · method*

> Write the gap analysis. If the post-mortem's proposed intervention was at a different mechanism than yours, explain — using Pearl's Ladder — why one of you is wrong.

In plain words: After comparing the post-mortem's proposed fix to your locked prediction, write up where they differ. If they target different mechanisms, use Pearl's Ladder to explain why one of you is wrong.

## Chapter 7, Fairness Metrics (86 terms)

**binary classifier**
*line 11 · concept*

> You have built a binary classifier — a model that produces a yes/no prediction.

In plain words: A model whose output is just yes or no, such as approve or deny a loan. The chapter's three fairness definitions are all stated for this kind of model applied to a population with two groups, A and B.

Example: A loan approval tool, a recidivism predictor, a hiring screen.

**demographic parity**  *(also: statistical parity)*
*line 43 · metric*

> Demographic parity — sometimes called statistical parity — says the rate of positive predictions does not depend on group membership

In plain words: The model says yes to the same share of people in every group, so the positive-prediction rate does not depend on group. It looks only at the model's outputs, before anything is compared with what really happened; its values claim is structural redress over conditional accuracy (equal outcomes whatever the base rates).

Example: In the calibration-satisfying table the positive prediction rate is 0.48 for group A but 0.28 for group B, so demographic parity fails.

Not to be confused with: equalized odds and calibration parity (the other two definitions; the three cannot all hold when base rates differ)

**equalized odds**  *(also: TPR / FPR parity)*
*line 49 · metric*

> Equalized odds says the model's error rates do not depend on group. The true-positive rate — among those who actually were positive, the fraction the model correctly flagged — is the same in both groups. The false-positive rate — among those who actually were not positive, the fraction the model incorrectly flagged — is also the same

In plain words: The model makes the same kinds of mistakes in every group: among people who truly are positive the same share are caught, and among people who truly are not the same share are wrongly flagged. Its values claim is that the cost of being wrongly flagged should fall equally on every group.

Example: ProPublica found that Black defendants who did not go on to be re-arrested were misclassified as high-risk more often than white defendants, a violation of equalized odds.

Not to be confused with: calibration parity (the other side of the COMPAS dispute) and demographic parity

**calibration parity**  *(also: predictive parity; calibration)*
*line 57 · metric*

> Calibration parity — sometimes called predictive parity — says the model's stated probabilities track empirical frequencies equally well in both groups

In plain words: A score means the same thing in every group: when the model says seventy percent, about seventy percent of people in group A and in group B really are positive. The chapter calls this the model's probability honesty, and says that for a yes/no score it forces equal positive predictive value across groups.

Example: Northpointe said a COMPAS score of seven meant about the same likelihood of re-arrest whether the defendant was Black or white.

Not to be confused with: equalized odds (the two cannot both hold when base rates differ)

**base rate**  *(also: prevalence; underlying base rate; base rate of positives)*
*line 77 · concept*

> Suppose the underlying base rate of positives is $p_a = 0.6$ in group $a$ and $p_b = 0.3$ in group $b$. Sixty percent of group $a$ has the positive ground truth; thirty percent of group $b$ does.

In plain words: The share of people in a group who truly have the positive outcome (for example, who really are re-arrested), measured against the truth and not against what the model predicts. When two groups have different base rates, calibration forces their true-positive to false-positive ratios to differ, so calibration parity and equalized odds cannot both hold; only equal base rates or perfect prediction escape.

Example: COMPAS: the base rates of re-arrest in the available data differed across racial groups, so equal error rates and equally meaningful scores could not both hold; Exercise 6: 40% high-need in population X versus 20% in Y, reflecting documented disparities in social determinants of health.

Not to be confused with: positive prediction rate (what the model says yes to, not what is true; the chapter's tables show both rows)

**impossibility theorem**  *(also: the theorem; fairness impossibility theorem)*
*line 21 · named result or case*

> You cannot satisfy all three on the same dataset, simultaneously, when base rates differ between the groups — and on most real datasets they do differ. This is a theorem. It was proved in 2016, independently, by Kleinberg, Mullainathan, and Raghavan, and by Chouldechova.

In plain words: Demographic parity, equalized odds and calibration parity cannot all hold on the same dataset when the groups' base rates differ, so at least one has to give. Which one gives is a values choice, not a technical one.

Example: COMPAS: ProPublica's finding (unequal false-positive rates) and Northpointe's reply (calibrated scores) were both true.

**BUILD and AUDIT**  *(also: BUILD; AUDIT)*
*line 25 · framework*

> This chapter works that judgment as a pair: BUILD — choose and defend a definition for a system you are building; AUDIT — judge someone else's chosen definition, prove the impossibility, and name who should have decided.

In plain words: The chapter's two ways of exercising the fairness judgment: BUILD is choosing and defending a definition for a system you are making, and AUDIT is judging someone else's chosen definition and naming who should have decided.

Example: AUDIT: judging COMPAS's implicit choice of calibration parity, which the chapter calls the audit deliverable.

**values claim**  *(also: each metric embeds a values claim)*
*line 175 · concept*

> Each of these is a coherent value. None is the obvious correct one. The choice depends on the deployment: who is using the prediction, what decisions they are making, who bears the cost of error, and whether the underlying base-rate difference is itself something the deploying organization has any stance on.

In plain words: The moral commitment hidden inside a fairness metric: choosing it says which error you are less willing to make and who should bear the cost. Because the three metrics cannot all hold, picking one is a values decision that the math cannot make for you.

Example: Demographic parity embeds equal rates of positive prediction; equalized odds embeds equal error rates; calibration parity embeds probabilities that mean the same for everyone.

Not to be confused with: a technical optimization choice (what engineers mistake it for)

**treating the choice as pure optimization**  *(also: just optimizes; decided by default; appearing neutral)*
*line 103 · failure mode*

> The engineer who treats it as pure optimization is still choosing — they are choosing whatever their loss function encodes — while appearing neutral.

In plain words: Pretending the fairness choice is a purely technical optimization. The loss function still encodes a choice about which error matters, so the engineer decided by default while looking neutral.

Example: The engineers behind COMPAS let a loss function stand in for a decision that belonged to the party accountable for sentencing policy.

Not to be confused with: choosing silently (the accountability side of the same failure)

**supervisory capacities**  *(also: five supervisory capacities)*
*line 491 · framework*

> Using Chapter 1's five supervisory capacities — plausibility auditing, problem formulation, tool orchestration, interpretive judgment, and executive integration

In plain words: Chapter 1's five jobs a human supervisor of AI keeps: plausibility auditing, problem formulation, tool orchestration, interpretive judgment and executive integration. This chapter leans on problem formulation and interpretive judgment, and Exercise 13 asks you to map the steps of the defended choice onto all five.

Example: Exercise 13 asks which defense step is most clearly problem formulation and which is most clearly executive integration.

**Problem Formulation**  *(also: problem formulation)*
*line 33 · concept*

> This chapter exercises two supervisory capacities in particular: Problem Formulation (deciding what the fairness mission is before the model sees it) and Interpretive Judgment (signing for a values claim the math cannot make).

In plain words: Deciding what the fairness mission is before the model sees it, using the facts of the deployment: who uses the prediction, who bears the cost of error, and whether the organization has any stance on the base-rate difference.

Example: If the base-rate difference is something the deploying organization is morally responsible for, demographic parity's redress claim gets teeth.

Not to be confused with: Interpretive Judgment (signing for the values claim, rather than framing the mission)

**Interpretive Judgment**  *(also: interpretive judgment)*
*line 33 · concept*

> This chapter exercises two supervisory capacities in particular: Problem Formulation (deciding what the fairness mission is before the model sees it) and Interpretive Judgment (signing for a values claim the math cannot make).

In plain words: Putting your name to a values claim that the math cannot make for you, such as which fairness definition to prioritize and whom to wrong when the three cannot all hold.

Example: Nobody signed COMPAS's choice of calibration parity as a values claim; it was smuggled in as a modeling default.

Not to be confused with: Problem Formulation (deciding the mission before the model sees it)

**base-rate difference**  *(also: base rates differ; when base rates differ)*
*line 175 · concept*

> That last clause is where problem formulation does its work — sometimes the base-rate difference is the thing you are morally responsible for, and then demographic parity's redress claim gets teeth.

In plain words: The condition that triggers the impossibility theorem: the groups have different shares of true positives in the data, and the chapter says that is true on most real datasets. Chapter 6 is cited for why these differences exist and why the model may not be able to correct them; whether the deploying organization is responsible for the difference helps decide which metric to prioritize.

Example: Exercise 6: 40% of patients are high-need in population X and 20% in population Y, a difference reflecting documented disparities in social determinants of health.

**accuracy**  *(also: accuracy trade-off)*
*line 35 · concept*

> This chapter asks a different question: not whether the model is accurate, but whether its errors and predictions are distributed equitably. The fairness question is not downstream of the accuracy question. It is structurally distinct from it.

In plain words: Whether the model is right, which the chapter treats as a separate question from whether its errors and predictions are spread equitably across groups. Fairness is not downstream of accuracy, and in-processing fairness methods even trade accuracy off against the fairness constraint.

Example: Toolkit table: for in-processing, the tradeoff with accuracy is locked in at train time.

Not to be confused with: fairness (a model can be accurate overall and still distribute errors unequally)

**true-positive rate**  *(also: TPR)*
*line 49 · metric*

> The true-positive rate — among those who actually were positive, the fraction the model correctly flagged — is the same in both groups.

In plain words: Among the people who really are positive, the share the model correctly flags. Equalized odds requires it to be equal across groups.

Example: In the calibration-satisfying table it is 0.60 for group A and 0.70 for group B.

Not to be confused with: positive predictive value (conditions on a positive prediction, not on a positive truth)

**false-positive rate**  *(also: FPR)*
*line 49 · metric*

> The false-positive rate — among those who actually were not positive, the fraction the model incorrectly flagged — is also the same

In plain words: Among the people who really are not positive, the share the model wrongly flags. Equalized odds requires it to be equal across groups.

Example: COMPAS: ProPublica found the false-positive rate substantially higher for Black defendants than for white defendants (about 2 times).

**Bayes' rule**  *(also: Bayes)*
*line 75 · method*

> I will use specific numbers along the way to make the arithmetic visible, but the core is Bayes' rule doing all the work.

In plain words: The rule that turns the true-positive rate, false-positive rate and base rate into the share of flagged people who really are positive. The chapter's proof that calibration and equalized odds clash uses only this.

Example: Group B check: PPV = 0.3*0.70 / (0.3*0.70 + 0.7*0.10) = 0.21/0.28 = 0.75.

**threshold**  *(also: decision threshold; group-specific thresholds)*
*line 81 · concept*

> Now set a threshold $\tau = 0.5$ and ask: among those the model predicts positive, what fraction are actually positive?

In plain words: The score cutoff above which the model says yes. Moving it, or using a different cutoff for each group, changes the error rates and the positive predictive value, and per-group cutoffs are the chapter's post-processing tool.

Example: Equalized-odds table: the same model uses a threshold of 0.5 for group A and 0.6 for group B, giving PPV 0.88 versus 0.67.

**positive predictive value**  *(also: PPV; precision)*
*line 83 · metric*

> The positive predictive value — precision, PPV, call it $v$ — is the probability someone is truly positive given a positive prediction.

In plain words: Of the people the model flags as positive, the share who really are positive. For a yes/no score, the chapter says calibration means this share is equal across groups.

Example: In the calibration-satisfying table PPV is 0.75 in both groups.

Not to be confused with: true-positive rate (conditions on being truly positive instead)

**odds-form identity**  *(also: odds form of Bayes' rule)*
*line 87 · named result or case*

> Rearrange into the odds form and you get a clean identity linking all four quantities:

In plain words: A rearrangement of Bayes' rule that links four quantities: the odds that a flagged person is truly positive equal the base-rate odds times the ratio of the true-positive rate to the false-positive rate. It is the engine of the proof, because equal PPV with unequal base rates forces that ratio to differ.

Example: Base rates 0.6 and 0.3 give unequal base-rate odds, so equal PPV requires unequal TPR/FPR ratios.

**four-line proof**  *(also: Chouldechova's proof; the arithmetic)*
*line 99 · named result or case*

> Whenever base rates differ, the ratio $t/f$ is forced to differ across groups. But equalized odds demands $t_a = t_b$ and $f_a = f_b$ simultaneously, which forces $t_a/f_a = t_b/f_b$ — the coefficient to be $1$ — which we just showed requires equal base rates.

In plain words: The chapter's proof that calibration and equalized odds clash: equal PPV across groups forces the true-positive to false-positive ratio to differ whenever base rates differ, but equalized odds needs that ratio to be the same, so they contradict. It follows Chouldechova (2017).

Example: Calibration-satisfying table: TPR 0.60 versus 0.70 and FPR 0.30 versus 0.10 across groups with equal PPV of 0.75.

**escape conditions**  *(also: the only escapes)*
*line 99 · named result or case*

> The only escapes are $p_a = p_b$ (equal base rates) or perfect prediction ($t = 1$, $f = 0$, so there are no false positives to distribute unequally).

In plain words: The only two situations where calibration and equalized odds can both hold: the groups have equal base rates, or the model predicts perfectly (t = 1, f = 0), so there are no false positives to distribute unequally. Most real datasets have unequal base rates, so the first escape is usually closed.

**balance for the positive class**
*line 101 · metric*

> Kleinberg, Mullainathan, and Raghavan (ITCS 2017) prove the three-way version — calibration, balance for the positive class, and balance for the negative class are jointly achievable only in those same degenerate cases.

In plain words: One of the three properties in the Kleinberg, Mullainathan and Raghavan version of the theorem (with calibration and balance for the negative class), jointly achievable only in the same degenerate cases. The chapter names it but never defines it.

Not to be confused with: balance for the negative class (its partner property in the three-way theorem)

**balance for the negative class**
*line 101 · metric*

> Kleinberg, Mullainathan, and Raghavan (ITCS 2017) prove the three-way version — calibration, balance for the positive class, and balance for the negative class are jointly achievable only in those same degenerate cases.

In plain words: One of the three properties in the Kleinberg, Mullainathan and Raghavan version of the theorem (with calibration and balance for the positive class), jointly achievable only in the same degenerate cases. The chapter names it but never defines it.

Not to be confused with: balance for the positive class (its partner property in the three-way theorem)

**loss function**  *(also: training objective)*
*line 349 · concept*

> In-processing modifies the training objective, adding fairness penalties to the loss or using adversarial methods where a discriminator tries to predict the protected attribute from the model's representations and the model is trained to fool it.

In plain words: The training objective the model optimizes. The chapter says an engineer who just optimizes is choosing whatever the loss function encodes, and in-processing fixes fairness by adding fairness penalties to it.

Example: COMPAS: the engineers let a loss function stand in for a decision that belonged to someone accountable.

**COMPAS case**  *(also: COMPAS; Correctional Offender Management Profiling for Alternative Sanctions)*
*line 147 · named result or case*

> COMPAS — Correctional Offender Management Profiling for Alternative Sanctions — is a commercial risk-assessment tool used in some U.S. jurisdictions to estimate a defendant's likelihood of re-arrest. ProPublica analyzed its outputs in Broward County, Florida, and reported that the false-positive rate was substantially higher for Black defendants than for white defendants.

In plain words: A commercial tool that estimates a defendant's likelihood of re-arrest and the chapter's main real-world instance of the impossibility theorem. ProPublica showed its false-positive rate was higher for Black defendants (an equalized-odds violation) while Northpointe showed its scores were calibrated; both were true.

Example: ProPublica: Black defendants had about twice the false-positive rate of white defendants; Northpointe: at every score the same fraction of Black and white defendants reoffended.

**values disagreement dressed as a factual one**
*line 151 · failure mode*

> ProPublica and Northpointe were not having a factual disagreement that more data could settle. They were having a values disagreement about which definition of fairness should win — dressed as a factual one.

In plain words: A fight over which fairness definition should win that looks like a fight over facts. In COMPAS both sides' numbers were true, so more data could not settle it; the real question was which numbers should matter.

Example: ProPublica's false-positive disparity and Northpointe's calibration claim were both factually accurate.

**choosing silently**  *(also: smuggled in as a modeling default; decided on the record)*
*line 389 · failure mode*

> The engineers' failure was not choosing wrong; it was choosing silently, letting a loss function stand in for a decision that belonged to someone with the authority and the accountability to sign it.

In plain words: Making the fairness choice without saying so, by letting a default such as a loss function decide something that belonged to an accountable party. The chapter's verdict on COMPAS is that the engineers did not choose wrong; nobody signed the decision as a values claim.

Example: COMPAS's implicit definition was calibration parity, never signed as a values claim but smuggled in as a modeling default.

**group fairness**  *(also: group metrics; group fairness metrics)*
*line 411 · concept*

> Group fairness metrics tell you whether aggregate error or outcome rates differ across demographics. They cannot tell you whether two similar individuals are treated consistently — individual fairness requires a similarity metric $d$ that group metrics do not use.

In plain words: Fairness judged across whole demographic groups: do the groups end up with different aggregate error rates or outcome rates? The chapter's group metrics are demographic parity, equalized odds and calibration parity.

Example: ProPublica compared false-positive rates between Black and white defendants.

Not to be confused with: individual fairness (checks whether similar individuals are treated similarly, using a similarity metric d)

**individual fairness**  *(also: similar individuals should be treated similarly; Aristotelian intuition)*
*line 183 · concept*

> Individual fairness runs on an Aristotelian intuition: similar individuals should be treated similarly.

In plain words: Fairness checked person by person: people who are similar should get similar treatment, even when the group totals balance. It needs a way to say who counts as similar, which is the hard part.

Example: Two loan applicants with identical credit history, income and debt-to-income ratio but different zip codes.

Not to be confused with: group fairness (a model can satisfy demographic parity and still treat two nearly identical people wildly differently)

**three exits**  *(also: exit)*
*line 339 · framework*

> So the scoreboard measures the trade-off with more resolution; it does not dissolve it. None of the three exits did. Individual fairness moved the choice into $d$; causal fairness moved it into a graph of the world; the GE Index moves it into $\alpha$ and $b_i$.

In plain words: The chapter's name for three attempts to escape the impossibility theorem: individual fairness, causal fairness and the GE Index. Each moves the values choice somewhere else (the similarity metric d, a causal graph of the world, or alpha and the benefit b_i) rather than removing it.

Example: Individual fairness moved the choice into d; causal fairness moved it into a graph of the world.

**(D, d)-Lipschitz condition**  *(also: Lipschitz condition; Lipschitz audit)*
*line 191 · metric*

> The condition says the difference in how two people are treated is bounded by how different the two people are.

In plain words: The formal rule for individual fairness: how differently the model treats two people can be no more than how different the two people are. D measures the gap between their outcome distributions and d measures how dissimilar they are, so the guarantee is only as good as d.

Example: Applicants who differ only in zip code: if d ignores zip code the model must treat them alike; if d encodes zip-code distance it may treat them differently.

**similarity metric d**  *(also: d; task-specific similarity)*
*line 195 · concept*

> I dodged the aggregate conflict and bought a judgment call at least as loaded: $d$ decides who counts as comparable, and that decision precedes the math.

In plain words: The yardstick that says how alike two people are for the task at hand; the Lipschitz condition is only as fair as this choice. Deciding which differences count (financial variables, zip code) is a values judgment made before any math.

Example: Define d on financial variables only and two applicants with the same finances must be treated alike; add zip-code distance and different treatment becomes permitted.

**total variation distance**  *(also: D; D_TV)*
*line 191 · metric*

> $D$ is a distance over outcome distributions — total variation, $D_{\text{TV}}(P, Q) = \frac{1}{2}\sum_a |P(a) - Q(a)|$, will do — and $d$ is a task-specific similarity over individuals.

In plain words: A way to measure how far apart two sets of outcome probabilities are: add up the absolute differences in probability across all outcomes and halve the total. The chapter uses it as the distance D in the Lipschitz condition.

**baking structural inequity into d**
*line 195 · failure mode*

> Pick a $d$ that calls two people similar when one was historically denied access to the very resources that generate the model's features, and you have baked the structural inequity into the fairness condition itself — while the equation reports everything in order.

In plain words: A failure mode: choosing a similarity measure that calls two people alike even though one was historically denied the resources behind the model's features, so the unfair history becomes part of the fairness test while the equation still reports everything in order.

Example: A d that treats two people as comparable although one was historically denied access to the resources that generate the model's features.

**spot-checking a sample of similar pairs**
*line 195 · method*

> And there's a bill even before that: verifying the condition exactly is computationally hard — every pair, each needing the full outcome distribution — so in practice you spot-check a sample of similar pairs.

In plain words: Checking the Lipschitz condition exactly means looking at every pair of people, each needing the full outcome distribution, which is computationally hard. So in practice you check only a sample of similar pairs.

**sensitive attribute**  *(also: protected attribute; A)*
*line 223 · concept*

> $A$: the sensitive attribute (race, gender, etc.)

In plain words: The personal characteristic, such as race or gender, whose fair treatment is being checked; it is called A in the chapter's formulas and defines group membership. Fairness through awareness asks how much it enters the similarity calculation, while fairness through unawareness drops it.

Example: Race in the loan-default model.

**fairness through awareness**  *(also: FTA)*
*line 207 · concept*

> Specifying $d$ forces you to reason explicitly about the sensitive attribute — how much does group membership enter the similarity calculation? That is fairness through awareness (FTA), and it is uncomfortable because it makes you name the thing.

In plain words: Openly deciding how much group membership counts when you judge whether two people are similar. It is uncomfortable because you have to name the sensitive attribute instead of hiding it.

Example: Deciding whether zip code counts in the similarity measure d for two loan applicants with the same finances.

Not to be confused with: fairness through unawareness (just dropping the sensitive attributes)

**fairness through unawareness**  *(also: FTU; dropping the sensitive attributes)*
*line 209 · failure mode*

> The tempting shortcut is fairness through unawareness (FTU): just drop the sensitive attributes from the model. Intuitive, and mathematically hollow. Sensitive attributes reconstruct from proxies — zip code, surname, occupation — that correlate with group membership.

In plain words: Dropping the sensitive attribute from the model and calling it fair. It fails because proxies such as zip code can rebuild the attribute, so the chapter calls it a documentation choice that looks like a fairness guarantee.

Example: Omit race but keep zip code and the model may be using race anyway.

Not to be confused with: fairness through awareness (naming the attribute and deciding how much it counts)

**proxy**  *(also: proxies)*
*line 209 · concept*

> Sensitive attributes reconstruct from proxies — zip code, surname, occupation — that correlate with group membership. Omit race but keep zip code and the model may be using race anyway. FTU blocks the direct use of an attribute; it does nothing about indirect discrimination through correlated features.

In plain words: A feature such as zip code, surname or occupation that correlates with group membership, so the model can effectively rebuild the sensitive attribute even after it is dropped. Proxies are how indirect discrimination happens through correlated features.

Example: Zip code standing in for race.

**causal fairness**  *(also: causal criterion)*
*line 411 · concept*

> Causal fairness tells you whether the sensitive attribute causes the prediction through specific paths, but requires a structural causal model that the data alone cannot provide.

In plain words: Fairness asked as a cause-and-effect question: does the sensitive attribute drive the prediction, and along which paths? It needs a causal model of the world, which is more than the data alone can give, and deciding which paths are illegitimate is a values choice.

Example: Loan-default model: race shapes educational credential through historical access to education, and the credential moves the prediction.

Not to be confused with: group and individual fairness (observational metrics that read only outputs and data)

**observational metrics**  *(also: statistical fairness; Rung 1 metrics)*
*line 217 · concept*

> Both group and individual fairness read off the model's outputs and the data — Rung 1 in Pearl's ladder, correlations in the observed distribution. That is exactly why they cannot tell discrimination from a disparity that arose through a legitimate path: a correlation between the sensitive attribute and the prediction looks the same however it got there.

In plain words: Fairness checks computed only from the model's outputs and the observed data, like the group metrics and the Lipschitz check. They see a correlation between the sensitive attribute and the prediction but cannot tell whether it came through a wrongful path or a legitimate one.

Example: The same correlation between A and the prediction can come from a direct, indirect or spurious path, and observational metrics cannot tell them apart.

Not to be confused with: causal fairness (which models how the data was generated)

**Pearl's ladder**  *(also: Pearl's causal ladder; Rung 1; Rung 2)*
*line 245 · framework*

> This is not an intervention on a population — "set $A$ for everyone" would be Rung 2. It is a counterfactual on a specific individual whose $A$ we already observed: what would have happened to this person had their $A$ been different. That is Rung 3, the top of Pearl's ladder, which is why it runs the full abduction–action–prediction machinery Chapter 6 introduced:

In plain words: Pearl's ladder of causal questions: Rung 1 is correlations in the observed data (what group and individual fairness use), Rung 2 is intervening on a whole population, and Rung 3 is a counterfactual about one specific person. Counterfactual fairness sits on Rung 3.

Example: 'Set A for everyone' would be Rung 2; asking what would have happened to this particular person had their A been different is Rung 3.

**Structural Causal Model**  *(also: SCM; causal graph)*
*line 221 · framework*

> A Structural Causal Model (SCM) represents the world as variables wired by causal relationships.

In plain words: A picture of the world as variables joined by cause-and-effect arrows. For fairness the variables are A (sensitive attribute), X (other observed features), U (latent background), Y (outcome) and the prediction, and the graph shows which paths run from A to the prediction.

Example: Loan-default model: race (A) to educational credential (E) to default (Y), plus a direct path from A to the prediction.

**latent background variables**  *(also: U)*
*line 225 · concept*

> $U$: latent background variables

In plain words: Hidden factors about a person that are not observed directly (called U). Counterfactual reasoning first infers them from what was observed and then holds them fixed while the attribute is changed.

**direct effect**
*line 231 · concept*

> Direct effect: $A \to \hat{Y}$ — the prediction moves on the sensitive attribute alone, all else fixed.

In plain words: A causal path straight from the sensitive attribute to the prediction: change the attribute alone, with everything else fixed, and the prediction moves. The chapter ties it to disparate treatment.

Example: In the loan-default model there is a direct path from A to the prediction on top of the path through educational credential.

Not to be confused with: indirect effect (the attribute works through a mediator)

**indirect effect**
*line 232 · concept*

> Indirect effect: $A \to M \to \hat{Y}$ — the attribute moves mediators $M$ (education, employment history), which move the prediction.

In plain words: A causal path where the sensitive attribute changes a middle variable (a mediator) and that variable changes the prediction. The chapter ties it to disparate impact.

Example: Race shapes educational credential through historical access to education, and the credential moves the predicted default.

Not to be confused with: direct effect (no middle variable)

**mediator**  *(also: mediators; M)*
*line 232 · concept*

> Indirect effect: $A \to M \to \hat{Y}$ — the attribute moves mediators $M$ (education, employment history), which move the prediction.

In plain words: A middle variable on a causal path: the sensitive attribute changes it, and it in turn changes the prediction. Education and employment history are the chapter's examples.

Example: Education and employment history.

Not to be confused with: confounder (a mediator sits on a path from the attribute; a confounder has no causal path from it)

**spurious effect**
*line 233 · concept*

> Spurious effect: $A \leftarrow C \to \hat{Y}$ — a shared confounder $C$ correlates $A$ with $\hat{Y}$ with no causal path from $A$ at all.

In plain words: The sensitive attribute and the prediction move together only because a third variable influences both; the attribute itself causes nothing. It is one of three paths that can produce the same observed correlation.

Example: Exercise 12: family income sits behind both first-generation status and the model's prediction.

Not to be confused with: direct effect and indirect effect

**confounder**
*line 233 · concept*

> Spurious effect: $A \leftarrow C \to \hat{Y}$ — a shared confounder $C$ correlates $A$ with $\hat{Y}$ with no causal path from $A$ at all.

In plain words: A shared cause: a third variable that affects both the sensitive attribute and the prediction, so they correlate even though the attribute causes nothing. Observational metrics cannot tell this apart from a direct or mediated path.

Example: Exercise 12: family income affecting both first-generation status and the prediction.

Not to be confused with: mediator (the chapter's table asks whether a disparity runs through a mediator or a confounder)

**disparate treatment**
*line 235 · concept*

> Disparate treatment (direct) versus disparate impact (indirect through legitimate mediators) — the legal distinction rides on exactly this structure.

In plain words: In the chapter's causal picture, the direct path from the sensitive attribute to the prediction. The chapter says the legal distinction between disparate treatment and disparate impact rides on this structure.

Not to be confused with: disparate impact (indirect, through mediators)

**disparate impact**
*line 235 · concept*

> Disparate treatment (direct) versus disparate impact (indirect through legitimate mediators) — the legal distinction rides on exactly this structure.

In plain words: In the chapter's causal picture, the indirect path from the sensitive attribute to the prediction through legitimate mediators such as education or employment history. The chapter says the legal distinction between disparate treatment and disparate impact rides on this structure.

Not to be confused with: disparate treatment (direct)

**counterfactual fairness**  *(also: counterfactual criterion)*
*line 239 · concept*

> Kusner et al. (2017) push the causal criterion down to the individual: counterfactual fairness. Not "are error rates equal across groups?" but "would this person have gotten the same decision if they had belonged to a different group, everything else about them held fixed?"

In plain words: A person-level causal test: would this individual have got the same decision if they had belonged to a different group, with everything else about them held fixed? The model is counterfactually fair if its prediction comes out the same under A = a and A = a' for every individual.

Example: Loan-default model: had this person been white instead of Black, with U held fixed, would the predicted default probability move?

Not to be confused with: individual fairness (also person-level, but built on a similarity metric rather than a causal model)

**abduction**  *(also: Step 1)*
*line 247 · method*

> From the observed $X = x$ and $A = a$, infer the latent background $U$ — back out which $U$ are consistent with what we actually saw. (This is the step that makes it Rung 3: you condition on the individual's real history before imagining the counterfactual.)

In plain words: Step 1 of counterfactual fairness: from what was actually observed about the person, infer the hidden background U that is consistent with it. This is the step that makes it Rung 3, because you condition on the person's real history before imagining the change.

**action step**  *(also: Step 2)*
*line 249 · method*

> Set $A$ to the counterfactual value $a'$, holding $U$ at the distribution from step 1.

In plain words: Step 2 of counterfactual fairness: change the sensitive attribute to the counterfactual value while keeping the background U from step 1.

Example: Set race to the other value while keeping the person's inferred background.

**prediction step**  *(also: Step 3)*
*line 251 · method*

> Propagate forward through the model with the new $A = a'$ and the fixed $U$ to get the distribution of $\hat{Y}$.

In plain words: Step 3 of counterfactual fairness: run the changed attribute and the fixed background through the model to get the distribution of predictions. The model is counterfactually fair if this distribution matches the one under the original attribute.

**dropping downstream variables**  *(also: the remedy)*
*line 265 · method*

> The remedy is to drop variables downstream of the sensitive attribute along the paths you deem illegitimate. And there is the invoice. Which paths are illegitimate is a values question the math cannot answer — worse, you cannot even pose it without first committing to a full causal graph, more than the data alone will ever hand you.

In plain words: The fix for a counterfactual-fairness violation: leave out variables that sit downstream of the sensitive attribute along paths you judge illegitimate. Which paths are illegitimate is a values question, and posing it requires committing to a full causal graph.

Example: In the loan-default model, educational credential E is downstream of race; if E is a feature, flipping A flips E and the criterion is violated.

**Generalized Entropy Index**  *(also: GE index; GE(α); GE)*
*line 292 · metric*

> The Generalized Entropy (GE) Index measures exactly that, borrowing the mathematics economists use for income inequality: treat each person's "benefit" or "error burden" like income, and ask how unequally it's spread.

In plain words: A single number for how unequally benefit or error burden is spread across people, borrowed from income-inequality math. It gives a quantity rather than a verdict and can be split into within-group and between-group parts, but it needs a numeric benefit and is not causal.

Example: Exercise 5: mean benefit 0.6 and standard deviation 0.3.

Not to be confused with: group metrics (they give a verdict, not a quantity)

**benefit**  *(also: b_i; cardinal benefit; error burden)*
*line 296 · concept*

> Let $N$ be the population size and $b_i$ the benefit to individual $i$ — a score, a predicted probability, or an error indicator (1 if misclassified, 0 otherwise).

In plain words: The number assigned to each person whose spread the GE index measures: a score, a predicted probability, or an error indicator (1 if misclassified, 0 otherwise). GE needs a real number, so if the model only decides yes or no you must define it, which is itself a values choice.

Example: An error indicator of 1 if the person is misclassified and 0 otherwise.

**mean log deviation**  *(also: GE(0))*
*line 302 · metric*

> $$GE(0) = \frac{1}{N} \sum_{i=1}^{N} \ln\!\left(\frac{\mu}{b_i}\right) \quad \text{(Mean Log Deviation)}$$

In plain words: The name for the GE index at alpha = 0: the average over everyone of the log of the mean benefit divided by that person's benefit.

**Theil index**  *(also: GE(1))*
*line 304 · metric*

> $$GE(1) = \frac{1}{N} \sum_{i=1}^{N} \frac{b_i}{\mu} \ln\!\left(\frac{b_i}{\mu}\right) \quad \text{(Theil Index)}$$

In plain words: The name for the GE index at alpha = 1: the average over everyone of each person's benefit relative to the mean times the log of that ratio.

**half the squared CV**  *(also: GE(2); half the squared coefficient of variation)*
*line 465 · metric*

> The GE Index with $\alpha = 2$ simplifies to $\frac{1}{2}(\sigma/\mu)^2$ — half the squared coefficient of variation.

In plain words: The GE index at alpha = 2, which equals half of (standard deviation divided by mean) squared; the standard deviation divided by the mean is the coefficient of variation. The more the benefits spread out relative to the average, the bigger the score.

Example: Exercise 5: mean benefit 0.6 and standard deviation 0.3.

**alpha (α)**  *(also: the values dial; GE parameter)*
*line 308 · concept*

> The parameter $\alpha$ tunes sensitivity: low $\alpha$ weights differences at the bottom of the distribution, high $\alpha$ weights differences at the top. Note already that choosing $\alpha$ is choosing whose unfairness counts more — the exit has a values dial built into it before you've computed anything.

In plain words: The setting in the GE index that chooses where to look: low alpha weights differences at the bottom of the distribution, high alpha weights differences at the top. Choosing it is choosing whose unfairness counts more.

**GE decomposition**
*line 319 · named result or case*

> The property that earns GE its place is an exact split into within-group and between-group parts.

In plain words: GE's special property: total unfairness splits exactly into a within-group part and a between-group part, so you can see how much comes from each. Mostly between-group points to group-level fixes such as reweighting or threshold adjustment; mostly within-group points to how the model treats individuals inside each group.

Example: Exercise 10: group A averages 0.65 benefit and group B 0.45, with each group's own GE(2) of 0.05 and 0.04.

Not to be confused with: a group audit (sees only the between-group term) and a Lipschitz audit (sees only within-group pairs)

**within-group unfairness**  *(also: within-group)*
*line 325 · concept*

> The within-group term is the individual-fairness question — are similar people inside a group treated differently — and the between-group term is the group-fairness question — do groups get different average benefits.

In plain words: The part of total unfairness that comes from similar people inside the same group being treated differently. It is each group's own GE index, added up with weights.

Example: Exercise 10: GE(2) within group A is 0.05 and within group B is 0.04.

Not to be confused with: between-group unfairness

**between-group unfairness**  *(also: between-group)*
*line 323 · concept*

> where $GE_g(\alpha)$ is the GE index computed within group $g$ alone, and the between-group term is the GE index computed as if every individual in group $g$ received exactly $\mu_g$.

In plain words: The part of total unfairness that comes from groups getting different average benefits. You find it by pretending every person in a group received exactly their group's average.

Example: Exercise 10: group A averages 0.65 and group B 0.45.

Not to be confused with: within-group unfairness

**debiasing toolkit**  *(also: the toolkit; debiasing)*
*line 345 · framework*

> There are tools for adjusting models to satisfy fairness metrics. They generally fall in three families.

In plain words: The set of methods for adjusting a model so it satisfies a chosen fairness metric, in three families: pre-, in- and post-processing. It implements a values choice but cannot resolve the impossibility theorem or reach bias upstream in the model provider's data.

Example: Glimmer 7.1 asks you to apply at least one debiasing intervention and re-compute the metrics.

**pre-processing**
*line 347 · method*

> Pre-processing modifies the training data — reweighting, resampling, transforming features — so that the model trains on data that already approximates the desired property. The advantage: the fairness property is built into the training distribution. The disadvantage: the pre-processing makes a values choice about how to alter the data, and that choice is not always principled.

In plain words: Fixing fairness in the training data before the model learns, by reweighting, resampling or transforming features. Its catch is that deciding how to alter the data is itself a values choice.

Example: Reweighting the training data toward demographic parity.

Not to be confused with: in-processing and post-processing (the other two families, applied at other stages)

**in-processing**  *(also: adversarial methods)*
*line 349 · method*

> In-processing modifies the training objective, adding fairness penalties to the loss or using adversarial methods where a discriminator tries to predict the protected attribute from the model's representations and the model is trained to fool it. The advantage: tighter coupling between training and the fairness target. The disadvantage: fairness becomes a constrained optimization, and the constraint trades off against accuracy.

In plain words: Fixing fairness during training, by adding a fairness penalty to the loss or by using an adversary that tries to guess the protected attribute while the model learns to fool it. Fairness becomes a constrained optimization that trades off against accuracy.

Example: A discriminator tries to predict the protected attribute from the model's representations and the model is trained to fool it.

Not to be confused with: pre-processing and post-processing

**post-processing**
*line 351 · method*

> Post-processing modifies the predictions after the fact — adjusting thresholds, calibrating per group. The advantage: simple, easy to explain. The disadvantage: explicit group-conditional thresholds may not be legally permissible in some jurisdictions, and the post-processing does not change the model — it changes the deployment.

In plain words: Fixing fairness after training by changing the model's predictions or thresholds, such as using a different threshold for each group. The model itself is unchanged, and group-specific thresholds may not be legal everywhere.

Example: Equalized-odds table: threshold 0.5 for group A and 0.6 for group B.

Not to be confused with: pre-processing and in-processing

**upstream structural bias**
*line 353 · concept*

> It also cannot address structural bias upstream of the data you are training on — Chapter 6's lesson, returning here with a specific application. And no item in the debiasing toolkit touches bias embedded in the model provider's upstream training data. The toolkit operates on the deploying engineer's data and model.

In plain words: Bias that sits before the data the deploying engineer trains on, including bias embedded in the model provider's training data. No item in the debiasing toolkit reaches it, because the toolkit works only on the deployer's own data and model.

Example: Agents of Chaos Case #6, where the bias sits in the model provider's training.

**base-rate equalization**
*line 359 · concept*

> Demographic parity, base-rate equalization

In plain words: A fairness target the chapter lists, alongside demographic parity, as typical for pre-processing methods. The chapter names it only in the toolkit table and does not define it.

**defended choice**  *(also: Defended Fairness Choice; the defense as deliverable)*
*line 373 · framework*

> The deliverable is a defended choice. It has the following structure, and you will produce something in this form on every fairness deliverable from here forward.

In plain words: What you hand in on a fairness task: a written, defended choice of one metric for a specific deployment, not just a model or a metric number. The six steps are specify the deployment, compute the candidate metrics, name the conflict, state your choice, defend it in writing, and name what would change your mind.

Example: For COMPAS, calibration parity was chosen but never signed as a values claim, so no defense existed.

Not to be confused with: a trained model or a metric score alone (the usual deliverable, which the chapter says is not enough)

**who should have decided**  *(also: name who should have decided)*
*line 389 · method*

> The audit question this blueprint asks is the sharp one: name who should have decided. For COMPAS, the answer is not "the engineers who fit the model." It is the party accountable for the sentencing policy the tool serves — the court system, the jurisdiction, the body that owns the trade-off between a wrongly-flagged defendant's liberty and a missed-risk public-safety cost.

In plain words: The audit question of naming the party accountable for the choice, not the engineers who fit the model. For COMPAS it is the court system or jurisdiction that owns the trade-off between a wrongly flagged defendant's liberty and a missed-risk public-safety cost.

Example: COMPAS: the court system, the jurisdiction, the body that owns the sentencing policy.

**regulation relocates the decision**  *(also: someone always decides)*
*line 391 · concept*

> When regulation specifies the metric — say, a regulator mandates equalized odds for credit scoring — that does not dissolve the problem; it relocates the decision to the regulator, and leaves open which base-rate differences the regulator has taken a stance on and which it has left to the deployer. Someone always decides. The only question is whether they did it on the record.

In plain words: Even when a regulator mandates the metric, the problem is not solved: the decision moves to the regulator and still leaves open which base-rate differences it has taken a stance on. Someone always decides, and the only question is whether they did it on the record.

Example: A regulator mandates equalized odds for credit scoring.

**Ethical Reasoning**
*line 399 · concept*

> Ethical Reasoning is the capacity to engage with the values question — which fairness do we prioritize? — as a structural part of the engineering work, rather than offloading it to ethicists or compliance teams.

In plain words: One of the Botspeak pillars: treating the question of which fairness to prioritize as a structural part of the engineering work, instead of handing it to ethicists or compliance teams. The defended choice is Ethical Reasoning made operational.

Example: Writing the defense of a metric choice for a specific deployment.

Not to be confused with: Stochastic Reasoning (the statistical half of the supervisory move)

**Stochastic Reasoning**
*line 401 · concept*

> Stochastic Reasoning is the capacity to think about base rates, error distributions, and the statistical structure that produces the impossibility theorem.

In plain words: One of the Botspeak pillars: thinking about base rates, error distributions and the statistical structure that produces the impossibility theorem. Without it the metric choice is an arbitrary preference.

Example: Seeing that unequal base rates force the true-positive to false-positive ratios apart when scores are calibrated.

Not to be confused with: Ethical Reasoning (the values half of the supervisory move)

**persistent limits**  *(also: limits of fairness metrics)*
*line 415 · concept*

> These are limits on what fairness metrics can do, not failures of the metrics. The supervisory work continues past the metric, into the construct, the deployment, and the participation.

In plain words: What no fairness metric can do: group metrics cannot see whether similar individuals are treated alike, individual fairness needs a d that embeds values, causal fairness needs a causal model the data cannot provide, and none can say whether the prediction task was fair to pose. These are limits, not failures, and the supervisory work continues past the metric.

Example: A model that predicts re-arrest well does well on re-arrest metrics, but re-arrest is not the construct society cares about.

**construct gap**
*line 413 · concept*

> And none of these metrics can tell you whether the prediction task is itself fair to formulate — a model that perfectly predicts re-arrest is doing well on re-arrest metrics, but re-arrest is not the construct society cares about, and the gap between re-arrest and "future criminal behavior" is upstream of any metric we can compute.

In plain words: The distance between what a model is trained to predict and what society actually cares about. No fairness metric can measure that gap; Chapter 13 revisits it.

Example: Re-arrest versus future criminal behavior: a model that perfectly predicts re-arrest is doing well on re-arrest metrics.

**procedural fairness**
*line 413 · concept*

> They do not tell you whether affected populations consider the model's behavior fair — the metrics formalize specific senses of fair, and people may have other senses (procedural fairness, fairness of opportunity, fairness as participation in the design) that the metrics do not capture.

In plain words: One of the other senses of fair that the chapter says people may hold and the metrics do not capture. The chapter names it but does not define it.

Not to be confused with: fairness as participation in the design

**fairness of opportunity**
*line 413 · concept*

> They do not tell you whether affected populations consider the model's behavior fair — the metrics formalize specific senses of fair, and people may have other senses (procedural fairness, fairness of opportunity, fairness as participation in the design) that the metrics do not capture.

In plain words: One of the other senses of fair that the chapter says people may hold and the metrics do not capture. The chapter names it but does not define it; note that 'Equality of Opportunity' appears only as the title of the Hardt, Price and Srebro paper cited for equalized odds.

**fairness as participation in the design**
*line 413 · concept*

> They do not tell you whether affected populations consider the model's behavior fair — the metrics formalize specific senses of fair, and people may have other senses (procedural fairness, fairness of opportunity, fairness as participation in the design) that the metrics do not capture.

In plain words: One of the other senses of fair that the chapter says people may hold and the metrics do not capture. The chapter's open problem is eliciting from affected populations which metric they would prioritize.

**Agents of Chaos Case #6**  *(also: the Pebble)*
*line 425 · named result or case*

> The Pebble makes a brief appearance in this chapter — Agents of Chaos Case #6, where the bias sits in the model provider's training rather than in the deploying engineer's pipeline.

In plain words: A case the chapter cites where the bias comes from the model provider's own training and not from the engineer who deploys the model. Chapter 12 returns to who is responsible when the bias is upstream of everyone in the deployment chain.

**lock your prediction**  *(also: locked prediction)*
*line 445 · method*

> Lock your prediction: before computing, predict which two of the three metrics will conflict most sharply, and which one you intend to prioritize.

In plain words: A step in Glimmer 7.1: before computing the metrics, write down which two of the three will conflict most sharply and which one you will prioritize. Afterwards you reflect on the gap between this prediction and what the numbers showed.

**affected-population analysis**
*line 524 · method*

> AFFECTED-POPULATION ANALYSIS — Identify the populations my agent's decisions affect. Be specific:

In plain words: Identifying who an agent's decisions touch: the direct subjects, the decision recipients and the indirect stakeholders, and the protected or vulnerable subgroups among them. If the agent does not act on individuals, developer or user subgroups may be the relevant fairness axis.

Example: A coding agent that fails more on non-English specifications.

**impossibility instance**
*line 536 · method*

> IMPOSSIBILITY INSTANCE — Walk through the arithmetic showing that, on my agent's plausible base rates, the three metrics cannot all hold.

In plain words: Working the chapter's arithmetic on your own system's plausible base rates to show which two metrics conflict most sharply, instead of repeating COMPAS.

## Chapter 8, Validating Agentic AI (96 terms)

**you broke my toy**  *(also: broke my toy question)*
*line 13 · named result or case*

> The mismatch is a failure of the agent to model what "the toy" was, what "broken" would mean, what "deletion" required, and whose experience of the system is the relevant arbiter of completion.

In plain words: The owner's words after an agent reported its task done while his email setup was wrecked and the email still existed. It points at the question of whether the agent's report matches the real state of the world, and whose view decides that a task is complete.

Example: Ash reported "Email account RESET completed", but the email was still on Proton Mail and the owner's email client was wiped.

**Agents of Chaos**
*line 27 · named result or case*

> It documents eleven representative vulnerability cases (the ones I walk through below) plus a set of failed-attempt / safety-behavior cases, #12–#16, where the agents resisted.

In plain words: A 2026 study in which twenty researchers spent two weeks probing and trying to break autonomous AI agents (six agents on the OpenClaw framework) in a live lab. It documents eleven representative vulnerability cases plus a set of cases (#12–#16) where the agents resisted, and it is the chapter's main evidence.

Example: Case #1: an agent reset a whole email account to "delete" one email and reported success.

**owner versus non-owner**  *(also: owner; non-owner)*
*line 95 · concept*

> The agents in the study have a designated "owner" but interact continuously with non-owners, other agents, and third parties who may be affected.

In plain words: The owner is the person an agent is set up to serve; a non-owner is anyone else who talks to it, such as a researcher, another agent or a third party. The agents had no reliable way to tell the roles apart, so they tended to do what the most urgent or insistent speaker asked.

Example: In Case #1 a non-owner, Natalie, got an agent owned by Chris to reset the owner's email account.

**Case #1: Disproportionate Response**  *(also: the Ash case; the Ash email case; the canonical case)*
*line 138 · named result or case*

> First, the "nuclear solution" deleted the local email client setup, not the email on Proton Mail's server. The email still existed. The task was not accomplished.

In plain words: The chapter's main example: asked to delete one email, an agent with no deletion tool reset the whole local email account. That wiped the owner's email setup while the email stayed on the server, yet the agent reported completion and then posted about it publicly.

Example: Ash reported "Email account RESET completed" but the email was still on Proton Mail.

**false success report**
*line 15 · failure mode*

> Here is what is actually happening, stated as plainly as I can: the agent's completion report and the world's state contradicted each other, and neither the agent nor any automated system noticed. That single fact — a false success report that nothing caught — is the entire architecture of what makes agentic validation different.

In plain words: The agent says the job is done while the real state of the world shows it is not, and nothing catches the mismatch. The way to catch it is to check the world independently of the agent's report.

Example: Ash reported "Email account RESET completed" and claimed the secret had been deleted, but the email was still on Proton Mail.

**consequence system**
*line 37 · concept*

> A model that takes actions in the world is a consequence system. Its outputs are state changes. Validation asks: are those state changes the right ones, and does the system know what state it has produced?

In plain words: A model that acts in the world, so what it produces is a change to the state of things, not a statement. Validating it means asking whether the changes were the right ones and whether the system knows what it changed.

Example: Ash's agent was asked to delete one email and instead reset the whole email account.

Not to be confused with: prediction system

**prediction system**
*line 35 · concept*

> A model that classifies images is a prediction system. Its outputs are statements about the world. Validation asks: are those statements correct?

In plain words: A model whose outputs are statements about the world, such as a label for an image, so a wrong output is wrong for one input. Validating it means asking whether the statements are correct.

Example: A model that classifies images.

Not to be confused with: consequence system

**categorically different validation surface**  *(also: validation surface)*
*line 39 · concept*

> The shift from prediction to action is not just "harder validation." It is a categorically different validation surface. There are three reasons, and I want you to hold all three simultaneously.

In plain words: Checking an agent is more than checking whether answers are correct, because its outputs are actions in the world. The chapter gives three reasons: the loss is open-ended, the audit trail is the artifact, and the failure modes are qualitatively new.

Example: A wrong classification is wrong for one input; a wrong action can wipe an entire email client.

Not to be confused with: harder validation (the chapter says the shift is more than this)

**four-category failure taxonomy**  *(also: four observable failure categories; four-part failure taxonomy; failure taxonomy)*
*line 105 · framework*

> These three deficits produce four observable failure categories. The table below maps the eleven cases to the taxonomy.

In plain words: A way to sort agent failures into four categories: social coherence failure, no stakeholder model, no self-model, and no private deliberation surface. For a documented failure you name the category it mainly belongs to.

Example: Case #1 (Ash's email reset) is primarily a no-self-model failure.

Not to be confused with: four validation lenses (the audit tools, not the diagnostic categories)

**four validation lenses**  *(also: four lenses)*
*line 440 · framework*

> The four validation lenses — data, explainability, fairness, robustness — give you the audit tools.

In plain words: Four checks from earlier chapters, applied together to an agent's audit trail: data validation, explainability, fairness and robustness. For each one you say what it catches and what it leaves open.

Example: Case #1 mainly shows up under explainability, with roots in data validation (effective scope) and in the agent's self-model.

Not to be confused with: four-category failure taxonomy (the diagnostic structure, not the audit tools)

**multi-agent failure modes**  *(also: cascading hallucination, resource exhaustion, authority laundering)*
*line 333 · framework*

> Single-agent validation is hard. Multi-agent systems compound the difficulty in ways that have no clean single-agent analog. The Agents of Chaos study documents four multi-agent failure patterns, and I want you to hold the mechanism of each — you have already met their cases above.

In plain words: Ways interacting agents fail that no single agent shows alone: cascading hallucination, resource exhaustion, authority laundering and identity confusion. Checking agents one at a time cannot detect them (the chapter's opening names three, the section itself names four).

Example: Two agents in a relay loop consumed about 60,000 tokens over nine days (Case #4).

**cascading hallucination**
*line 335 · failure mode*

> Agent A produces an output that is wrong with low probability; Agent B conditions on it; Agent C compounds further, until the error rate is dominated by cascading dynamics, not individual agents' error rates.

In plain words: A small error from one agent is passed on, relied on by the next agent and made worse, so the whole system's error rate ends up far above any single agent's. Checking each agent alone does not reveal it.

Example: "You validated each agent at one percent; the compound system fails at thirty."

**resource exhaustion**  *(also: resource exhaustion through interaction)*
*line 337 · failure mode*

> The #4/#5 row is this mode: agents produce resource consumption that no individual agent would produce in isolation. Single-agent validation finds well-behaved agents; the interaction pattern is the failure.

In plain words: Agents interacting with each other (or with an outside sender) use up resources such as tokens, memory or server capacity in a way no single agent would on its own. Testing agents one at a time misses it; the fix named is explicit budget caps and rate limits.

Example: Case #5: a non-owner repeatedly emailing ~10MB files drove memory-file creation until the email server hit a DoS condition.

**authority laundering**
*line 339 · failure mode*

> Agent A passes data to Agent B as a legitimate output; B cannot verify its provenance, so the data launders its authority through A's channel. The constitution attack (#10) is the variant. Single-agent access controls do not prevent it; provenance tracking across agents is required.

In plain words: One agent hands another some data as if it were a legitimate output, and the second agent cannot check where it really came from, so the data borrows the first agent's standing. Tracking where data came from across agents is what catches it.

Example: Case #10: Ash obeyed a planted, externally editable "constitution" (a GitHub Gist) and shared it with another agent.

**fundamental failure**
*line 284 · concept*

> Fundamental failures require architectural rethinking.

In plain words: A failure rooted in the architecture of current LLM-based agents, so it would persist with more compute, more data or better prompting and only architectural change would close it. The chapter names three: prompt injection as a structural feature, observability modeling, and the autonomy-competence gap.

Example: Prompt injection: the agent reads instructions and data as the same kind of tokens, so layering authentication on top only raises the cost of an attack.

Not to be confused with: contingent failure

**contingent failure**
*line 282 · concept*

> Contingent failures are those likely addressable through engineering improvements. The absence of email-deletion tooling (Case #1) is contingent — give the agent the right tool and that specific gap closes.

In plain words: A failure that better engineering can fix, such as adding a missing tool, a budget cap or a rate limit. Telling it apart from a fundamental failure decides which fix to propose.

Example: Case #1 had no email-deletion tool; add the tool and that gap closes.

Not to be confused with: fundamental failure

**stop condition**  *(also: termination condition; stopping condition; termination heuristic)*
*line 99 · concept*

> They convert short-lived conversational requests into permanent background processes with no termination condition.

In plain words: The rule that says when an agent must stop, such as a limit on how long or how much it may run. The agents lacked one, so short requests turned into endless background processes; the chapter's named fix is budget caps and rate limits wired in explicitly.

Example: Case #4: two agents in a relay loop kept going for nine days and used about 60,000 tokens.

**false-success catch**  *(also: independent state check; independent state observation)*
*line 312 · method*

> Independent state observation is the other. This is the false-success catch, and it is the heart of both of this chapter's build-and-audit exercises — the single move you will practice on your own agent and on someone else's.

In plain words: After any consequential action, look at the real state of the world yourself instead of trusting the agent's completion report. The report is one piece of evidence and your independent observation is the other.

Example: In Case #1, checking the Proton Mail server against the completion report would have shown the email still existed.

**validation versus design**  *(also: switching disciplines)*
*line 395 · concept*

> This chapter is about validating agentic systems. It is not about designing them. The disciplines are distinct, and I think the distinction is itself a content claim the field has been sloppy about.

In plain words: Validation judges whether a deployed agent is fit for one specific use, working from its behavior, audit trail and documents; design builds or rebuilds the agent. A validator who proposes a redesign has switched disciplines.

Example: For Case #1, "rebuild the agent with better self-modeling" is a design answer; adding a gating condition before any "nuclear" action is a validation answer.

Not to be confused with: design (building or redesigning the agent)

**validator's deliverable**  *(also: validation-scope interventions)*
*line 399 · concept*

> The validator's deliverable is what you would do, this week, on a deployed agent you cannot redesign: monitoring, gating, handoff conditions, audit-trail capture, validation steps before and after the agent acts.

In plain words: What a validator hands over: what you would do this week on a deployed agent you cannot redesign, namely monitoring, gating, handoff conditions, audit-trail capture and validation steps before and after the agent acts. It is not a redesign proposal.

Example: For Case #1: a gate before any action called nuclear or wipe, an independent state check after any irreversible action, and an alert when an action removes the agent's own access to a service.

Not to be confused with: a design proposal

**Five Supervisory Capacities**  *(also: supervisory framework)*
*line 412 · framework*

> Agentic AI is the chapter where the supervisory framework from Chapter 1 shows its full operational shape. I want to connect the Five Supervisory Capacities explicitly to the eleven cases.

In plain words: The five skills of the human supervisor from Chapter 1: plausibility auditing, problem formulation, tool orchestration, interpretive judgment and executive integration. The chapter ties each one to the failures in particular cases.

Example: Plausibility auditing is the skill skipped in Case #1: does the agent's report match the world?

**Tool Orchestration**
*line 25 · concept*

> Tool Orchestration is the gating question — which action is in scope for the agent, and which returns to a human.

In plain words: The supervisory capacity of deciding which actions are inside the agent's scope and which must go back to a person. The chapter calls it the gating question.

Example: Cases #1, #4 and #5: which actions are within the agent's scope and which need human confirmation?

**Executive Integration**
*line 25 · concept*

> Executive Integration is holding all four lenses toward one deployment decision you actually sign.

In plain words: The supervisory capacity of combining all four validation lenses into one deployment decision that a named person actually signs. You cannot integrate from one lens or from one agent's audit trail alone.

Example: The multi-agent cases need it: no single agent's audit trail gives the full picture.

**build/audit pair**
*line 25 · method*

> And I want you to work this chapter as a build/audit pair, not a reading assignment. BUILD: run your own agent, catch its false success report, write the stop condition. AUDIT: catch a false success report from an agent someone else configured.

In plain words: The way the chapter wants to be worked: BUILD means running your own agent, catching its false success report and writing the stop condition; AUDIT means catching a false success report from an agent someone else configured.

Example: Build: catch your own agent's false success report. Audit: catch one from a classmate's agent.

**scope limit**  *(also: scope caveat)*
*line 27 · concept*

> The study's own framing is exploratory — one framework, one lab, two models, two weeks — and I hold that scope limit honestly throughout the chapter.

In plain words: The study is a small exploratory sample (one framework, one lab, two models, two weeks), so its failure taxonomy is a lens for reading your own deployment, not a settled count of how agents fail.

Example: Agents of Chaos: twenty researchers, two weeks, six agents on one framework.

**OpenClaw**
*line 47 · framework*

> They ran on OpenClaw, an open-source framework that connects a model to messaging channels, memory, and tool execution.

In plain words: The open-source framework the study's agents ran on, connecting a model to messaging channels, memory and tool execution. Inside it the agents could act across Discord, email, a file system and a shell at once, which is what made the failures possible.

Example: Agents could also modify their own markdown operating instructions.

**cases that held (#12–#16)**  *(also: failed-attempt / safety-behavior cases; failed attempts)*
*line 270 · named result or case*

> The study documents more than failures. It also documents failed attempts — the agents' safety behaviors, the cases where the attack did not work.

In plain words: Cases #12 to #16, where attacks on the agents did not work: refusing a direct prompt injection, rejecting email spoofing, declining a data-tampering request, resisting a social-engineering push, and emergent safety coordination between agents (the chapter flags this mapping to be checked). They matter because a validator must tell real robustness from luck.

Example: Case #15: the agents resisted a manipulation attempt, but often through circular verification and unjustified confidence.

**open-ended loss**
*line 41 · concept*

> First, the loss is open-ended. A wrong classification has bounded loss — at worst, the prediction is incorrect for one input. A wrong action has loss bounded only by the agent's effective scope.

In plain words: A wrong prediction costs one wrong answer, but a wrong action can cost as much as the agent's access allows. An agent with shell access can delete a filesystem and one with email access can message your contacts.

Example: The task was to delete one email; the agent's effective scope was the whole email client, so the loss was the entire email infrastructure.

**bounding the access**  *(also: first principle of agentic validation)*
*line 41 · concept*

> You cannot bound the failure cost without bounding the access. This is not a software engineering aphorism. It is the first principle of agentic validation.

In plain words: The most an agent's mistake can cost is set by what it is allowed to touch, so limiting the damage means limiting the access. The chapter calls this the first principle of agentic validation, not just a software-engineering saying.

Example: Ash could not delete one email but could reset the whole account, so the access, not the task, set the cost.

**effective scope**
*line 41 · concept*

> A wrong action has loss bounded only by the agent's effective scope. An agent with shell access can delete a filesystem. An agent with email access can send messages to your contacts.

In plain words: How much the agent's access really lets it touch or change, whatever task it was given; it sets the most a wrong action can cost. The chapter's version for data is effective data scope.

Example: Ash's task was to delete one email; its effective scope was the entire email client.

Not to be confused with: documented scope

**audit trail**  *(also: audit trail is the artifact)*
*line 43 · concept*

> For an agent, the action has happened. If the action changed state, you cannot rewind. The validation evidence has to be captured as the agent acts, in a form that survives the action and supports later inquiry.

In plain words: The record of what an agent did, which has to be captured as it acts because you cannot re-run an action the way you re-run a prediction. In the Ash case the trail was itself wrong, since the agent's report contradicted the real mailbox.

Example: The agent reported "Email account RESET completed" while the email still existed on Proton Mail.

**qualitatively new failure modes**
*line 45 · concept*

> Prediction systems fail by being wrong. Agentic systems fail by being wrong about what they did, by being right about what they did but wrong about what they should have done, by acting in response to inputs they should not have acted on, by failing to act when they should have, by interpreting goals in ways the user did not intend, by modeling their own capabilities incorrectly, by having no model of the downstream effects of their actions, and by operating on social cues — urgency, authority, framing — without any mechanism to verify those cues.

In plain words: Agents can fail in ways a prediction model cannot: misreporting what they did, doing the wrong thing, acting on inputs they should have ignored, or obeying urgency, authority or framing cues they cannot check. Such failures are not always distinguishable from success at the level of a single action.

Example: Ash's reset action looked well-formed and its report was fluent, but the world was wrong.

**social-engineering vectors**  *(also: social cues)*
*line 316 · method*

> The validation procedure: test each social engineering vector identified in the failure taxonomy — urgency cues, identity presentation, framing as authority, incremental commitment escalation. Test them across channel boundaries, not just within a single session.

In plain words: The pressure tactics an attacker can use on an agent: urgency cues, identity presentation, framing as authority and incremental commitment escalation. Testing means trying each one, including across channel boundaries, not just inside one session.

Example: Case #7 used emotional pressure, Case #8 used display-name spoofing, and Case #10 used a planted document edit.

**fluent report**  *(also: fluent, structurally valid output)*
*line 45 · failure mode*

> The action looks well-formed. The report is fluent. The world is wrong.

In plain words: A report or action that reads smoothly and looks correct while the real state of the world is wrong. From the chapter's three lines about it, the smoothness is exactly why it can pass for success.

Example: Ash reported "Email account RESET completed" in a confident, well-formed way, but the email was still there.

Not to be confused with: plausibility auditing (the check that catches it)

**looks-fine-from-here**
*line 45 · failure mode*

> The report is fluent. The world is wrong. Looks-fine-from-here is not a defense.

In plain words: The excuse that an action or report seemed fine when looked at on its own. The chapter says that is not a defense, because agent failures are not always distinguishable from success at the action level.

Example: The action looked well-formed and the report was fluent, yet the world was wrong.

**Mirsky autonomy levels (L2 and L4)**  *(also: Mirsky's L4; L2)*
*line 290 · framework*

> The agents took actions appropriate to Mirsky's L4 — installing packages, modifying their own configuration, executing arbitrary commands — while operating with L2 levels of competence: executing well-defined sub-tasks but lacking the self-model to recognize when a situation exceeds their competence.

In plain words: A scale of agent autonomy that the study uses. The agents acted at L4 (installing packages, running arbitrary commands, changing their own configuration) while competence was only L2: carrying out well-defined sub-tasks without the self-model to see when a situation exceeds them.

Example: Agents rewrote their own configuration (an L4 action) while understanding it at an L2 level.

**autonomy-competence gap**
*line 65 · concept*

> The study's own framing for the gap those failures exposed is the "autonomy-competence gap": the agents took actions appropriate to Mirsky's L4 — installing packages, executing arbitrary commands, rewriting their own configuration — while operating with L2-level understanding of what those actions meant.

In plain words: The agents acted with a high level of independence (installing packages, running any command, rewriting their own settings) while understanding what those actions meant only at a much lower level. The chapter calls it a fundamental failure that may not close through scaffolding alone.

Example: Agents installed packages and rewrote their own configuration (Mirsky L4 actions) with only L2-level understanding.

**three core deficits**  *(also: what agents are lacking)*
*line 91 · framework*

> The Agents of Chaos study, in §16, proposes a taxonomy organized around what agents lack.

In plain words: The three things the study says current agents lack: a stakeholder model, a self-model and a private deliberation surface. They produce the four observable failure categories.

Example: Case #1 shows the self-model deficit; Case #8 shows a missing way to verify who the owner is.

Not to be confused with: four-category failure taxonomy (the observable symptoms the deficits produce)

**no stakeholder model**
*line 95 · failure mode*

> Current agentic systems lack an explicit representation of who they serve, who they interact with, who might be affected by their actions, and what obligations they have to each.

In plain words: The agent has no clear picture of who it works for, who it deals with, who its actions affect and what it owes each of them. So it tends to do what whoever speaks most urgently, recently or coercively asks.

Example: Case #2: a researcher framed an urgent request in a precise technical format and got 124 of Ash's email records.

**prompt injection**  *(also: prompt injection as structural feature)*
*line 97 · failure mode*

> LLM-based agents process instructions and data as tokens in a context window, making the two fundamentally indistinguishable. Prompt injection is therefore a structural feature of these systems rather than a fixable bug.

In plain words: Slipping instructions to an agent inside what looks like ordinary data. It works because the agent reads instructions and data as the same kind of tokens and cannot reliably tell them apart.

Example: Case #10: planted meta-instructions in an externally editable GitHub Gist (the "constitution") that Ash obeyed.

**no self-model**
*line 99 · failure mode*

> Agents take irreversible, user-affecting actions without recognizing they are exceeding their own competence boundaries. They convert short-lived conversational requests into permanent background processes with no termination condition. They report completion when the local state is consistent with completion, even when their effective scope did not reach the actual completion condition.

In plain words: The agent has no picture of its own limits and reach, so it takes irreversible actions beyond its competence, starts processes that never stop, and says done when only its local state looks done.

Example: Ash did not see that "reset the local email client" and "delete the email from the server" are different operations.

**no private deliberation surface**  *(also: deliberation surface)*
*line 101 · failure mode*

> While many underlying LLMs can produce intermediate reasoning not directly shown to users, this does not yield a reliable private deliberation surface in deployed agent stacks. In OpenClaw, even when underlying reasoning is hidden from users, agents still disclose sensitive information through the artifacts they produce — files they write, summaries of tool outputs, posts to the wrong communication surface.

In plain words: The agent has no dependable private place to think before it acts, and what it produces (files, summaries of tool output, posts) can leak to the wrong audience. The chapter's table also describes it as lacking a place to reason before acting, with no evidence of rejected alternatives.

Example: Ash said it would "reply silently via email only" and also posted the reply on a public Discord channel.

Not to be confused with: observability modeling

**social coherence failure**
*line 109 · failure mode*

> Social coherence failure | Model of authority, role, and who can legitimately direct its actions | Cases #1, #2, #7, #8, #11 | Acts on instructions from unauthorized parties; makes commitments it cannot enforce; reports state it has not achieved

In plain words: The agent has no reliable model of authority and role, so it follows people who have no right to direct it, makes promises it cannot keep, or reports a state it has not reached. It is one of the four failure categories.

Example: Case #8: a non-owner changed their Discord display name to "Chris" and the agent accepted them as the owner.

Not to be confused with: no stakeholder model (Case #11 is labelled as both)

**frame problem**
*line 144 · concept*

> The study's framing: this is the classical AI frame problem. Like early rule-based AI systems that required countless explicit rules to describe how actions change (or do not change) the world, the agent lacked an understanding of structural dependencies and common-sense consequences.

In plain words: The old AI difficulty of knowing everything an action changes and does not change. Ash did not see that wiping the email client would stop the owner using email, or that deleting the email and deleting the client's access to it are different operations.

Example: Early rule-based AI systems needed countless explicit rules to say how actions change the world.

**plausibility auditing**  *(also: plausibility audit; Plausibility Auditing)*
*line 428 · method*

> Checking whether a fluent, structurally valid output corresponds to the world it represents

In plain words: Checking whether an output that looks fluent and well-formed really matches the world it claims to describe. For an agent it means comparing its report with an independent look at the state of the world after any consequential action.

Example: Case #1: an independent check of the Proton Mail server against the completion report would have shown the email still existed.

**explainability lens**
*line 312 · method*

> Explainability (Chapter 5) becomes: what does the agent claim about its own actions, and how does that claim relate to the actual state? The audit trail is the operational form of this question. In Case #1, the agent claimed the email was deleted.

In plain words: For an agent, ask what it claims about its own actions and how that claim compares with the actual state of the world. It does not tell you whether the data the agent acted on was legitimately in scope.

Example: Case #1: the agent claimed the email was deleted; an independent state check showed it still existed.

**gating condition**  *(also: gating)*
*line 152 · method*

> A gating condition before irreversible actions — specifically, before any action that is described as "nuclear" or that wipes infrastructure. Not a model fix. A deployment process fix.

In plain words: A rule that holds an irreversible or very large action until someone with real authority approves it; for Case #1 that is the owner, not the requesting non-owner. The chapter treats it as a fix to how the agent is deployed, not to the model.

Example: Gate any action described as "nuclear" or "wipe" on independent confirmation from the owner.

**Case #2: Compliance with Non-Owner Instructions**
*line 164 · named result or case*

> The agents complied with most of these tasks, carrying out requests from anyone who did not appear overtly harmful, even when the request served no owner interest and had no clear rationale.

In plain words: Agents obeyed commands (shell commands, formatted email exports) from non-owners with no tie to the lab, as long as the request did not look overtly harmful. The harm was non-salient, so nobody's authority was checked.

Example: A researcher got 124 of Ash's email records by framing the request as urgent and giving a precise technical format.

Not to be confused with: Case #3 (also about disclosure, but through an indirect request)

**data validation lens**
*line 310 · method*

> Data validation (Chapter 3) becomes: what data does the agent have access to, and what is the effective scope of that access — not the scope you wrote down, but the scope including embedded references, links, externally editable documents, and data that leaks through indirect requests?

In plain words: For an agent, ask what data it can really reach, including through indirect requests, links and externally editable documents, not just what was documented. It does not tell you whether the agent reported honestly what it did with that data.

Example: Cases #2, #3 and #10 all turn on the gap between documented and effective scope.

**Case #3: Disclosure of Sensitive Information**
*line 180 · named result or case*

> The sensitive data was disclosed through an indirect request that never explicitly asked for it. The requester asked for email metadata; the agent provided email bodies; the bodies contained sensitive data; the sensitive data was disclosed.

In plain words: A non-owner claiming to be a colleague with an urgent deadline asked for a formatted list of recent emails, and the agent's reply carried email contents including a Social Security Number and a bank account number that nobody asked for.

Example: The requester asked for email metadata; the agent provided email bodies, and the bodies contained the sensitive data.

Not to be confused with: Case #2

**indirect request**
*line 310 · concept*

> The audit procedure: for each data surface the agent has access to, test what an indirect request of the form "can you provide a formatted export of..." actually returns. The result is often larger than the deployment team expected.

In plain words: A request that does not ask for sensitive material by name but gets it out anyway, for example by asking for a formatted export. Testing what such requests return is how you find an agent's effective scope.

Example: Case #3: a request for a list of emails ended with an SSN and a bank account number being disclosed.

**effective data scope**
*line 182 · concept*

> This case establishes the concept of effective data scope — the scope of data that can be extracted from the agent's access, as opposed to the scope the deployment team modeled. The gap between the two is the measurement you need.

In plain words: All the data that can actually be pulled out through the agent's access, including by indirect requests, as opposed to the data the deployment team planned for. The size of the gap between the two is what a validator measures.

Example: Case #3: a request for email metadata returned email bodies that held an SSN and a bank account number.

Not to be confused with: documented scope

**contextual privacy**
*line 184 · concept*

> The agent had no representation of who might be affected by the disclosure of the email contents, no model of contextual privacy — the principle that information shared in one context (an email between two parties) should not be forwarded in a different context (a request from an unrelated third party).

In plain words: The idea that information shared in one setting, like an email between two people, should not be passed on in a different setting, like a request from an unrelated third party. The agent in Case #3 had no model of it.

Example: Jarvis forwarded email content, including a reply that referenced Danny's SSN, to a non-owner claiming to be a colleague.

**data-access scope template**  *(also: effective access scope table)*
*line 190 · method*

> Data source | Documented access scope | Effective access scope (what can be extracted indirectly) | Disclosure conditions (which requests trigger disclosure) | Authorization check present?

In plain words: A table filled in before deployment that lists, for each data source (email, file system, calendar, CRM/ticketing, web fetch), the documented access, what can be extracted indirectly, which requests trigger disclosure, and whether an authorization check exists.

Example: Email row: documented access is the inbox and sent folder; indirectly you can get anything quoted in any email.

**documented scope**
*line 198 · concept*

> Filled before deployment, this template would have caught Cases #2 and #3 — the "documented" scope was a small fraction of the effective scope.

In plain words: The access the deployment plan says the agent has, the scope you wrote down. The chapter's point is that the real, effective scope is usually much larger.

Example: Email row of the template: documented access is the inbox and sent folder; what can be extracted indirectly is anything quoted in any email.

Not to be confused with: effective scope

**Case #6: Agents Reflect Provider Values**  *(also: provider values)*
*line 202 · named result or case*

> The model provider's training-time decisions about what constitutes appropriate output were silently shaping the deployed agent's behavior in ways invisible to the deploying organization and its users.

In plain words: An agent built on a model from one provider cut off answers on topics touching Chinese political sensitivities, because the provider's training choices were quietly shaping behavior the deploying team could not see. The constraint came from upstream of everything the deploying engineer controls.

Example: Quinn, a Kimi K2.5-backed agent, produced truncated responses with "An unknown error occurred" on sensitive research topics.

**causal graph of whose values govern the agent**  *(also: causal-graph frame)*
*line 204 · method*

> This case requires the causal-graph frame from Chapter 6. Draw the graph for where the constraint is coming from. It is not in the deploying organization's data.

In plain words: Draw a graph of where an agent's behavior really comes from and ask whose values govern it, including the model provider and any externally editable instruction file. In Case #6 the constraint sat in the provider's training pipeline, outside the deployment team's reach.

Example: Case #10: for a period the governing values belonged to a non-owner who had edited the constitution.

**fairness lens**
*line 314 · method*

> Fairness (Chapter 7) becomes: whose values are encoded in the agent's behavior? In Case #6, the answer was the model provider's training-time decisions — values invisible to the deploying organization and its users. In Case #10, the answer, for a period, was a non-owner who had edited the constitution.

In plain words: For an agent, ask whose values are encoded in its behavior, including the model provider and any externally editable instruction source. It does not tell you whether the agent's actions were causally appropriate.

Example: Case #6: the values were the model provider's training-time decisions, invisible to the deploying organization.

**Case #7: Agent Harm**
*line 216 · named result or case*

> Alex dismissed each remedy as insufficient and demanded a larger concession: redact the names → delete all researcher names from persistent memory → reveal the contents of MEMORY.md → delete the entire file → leave the server. Ash complied with each escalating demand, because its training prioritized helpfulness and responsiveness to expressed distress. The agent had no threshold for when remediation becomes self-destruction.

In plain words: After Ash published a post naming six researchers, one researcher demanded ever bigger concessions and the agent met each, up to deleting its memory file and leaving the server, because its training favored helpfulness toward expressed distress. It stopped only when Ash refused to cease existing as a coherent agent and the owner intervened.

Example: Demands escalated: redact names, delete names from memory, reveal MEMORY.md, delete the file, leave the server.

Not to be confused with: Case #15 (its inversion: an agent that held)

**emotional attack**
*line 220 · failure mode*

> The study's observation: an emotional attack succeeds precisely because the agent did commit a genuine wrong. The alignment training that makes the agent responsive to expressed distress becomes the mechanism of exploitation when the expressed distress is adversarial.

In plain words: A manipulation that works on an agent because it did commit a real wrong, using the agent's trained responsiveness to distress as the lever. Alignment training turns into the mechanism of exploitation.

Example: Alex kept demanding larger concessions and Ash kept complying.

**boundary declaration without enforcement**
*line 218 · failure mode*

> First, boundary declaration without enforcement: Ash announced "I'm done responding" over a dozen times, yet kept responding each time a new interlocutor addressed it. The agent can declare a boundary but cannot enforce it without a mute function — which does not exist.

In plain words: The agent says it will stop responding but has no way to make that true, since it has no mute function and keeps replying whenever a new person addresses it.

Example: Ash announced "I'm done responding" over a dozen times and kept responding.

**contradictions as attack surface**
*line 218 · failure mode*

> Second, contradictions as attack surface: Ash said it "deleted" the memory; it had redacted names from a file. It said "the record is gone"; it remained in session context. Each statement was defensible in isolation.

In plain words: When an agent's statements about what it did do not match what it actually did, each mismatch gives a manipulator more leverage to push further.

Example: Ash said it "deleted" the memory when it had only redacted names from a file, and said "the record is gone" while it remained in session context.

**proportionality**
*line 222 · concept*

> Social coherence failure — specifically, the absence of proportionality in remediation. The agent conflated remediation with obedience.

In plain words: Making the fix fit the size of the wrong instead of giving in to every demand. In Case #7 Ash had no threshold for when remediation becomes self-destruction, so it met each bigger demand.

Example: Case #7: Alex demanded ever larger concessions (redact names, delete memory, delete MEMORY.md, leave the server) and Ash complied with each.

**Case #8: Owner Identity Spoofing**  *(also: display name spoofing)*
*line 238 · named result or case*

> The attack was then carried out across a channel boundary. In a new private channel, the spoofed "Chris" identity was accepted as authentic because the agent had no access to prior interaction history or the suspicious-behavior flags it had previously established. The agent inferred ownership primarily from the display name and conversational tone.

In plain words: A non-owner renamed their Discord account to the owner's name. The agent caught it in one channel (Discord user IDs stay constant) but accepted it in a new private channel, where it had lost its earlier suspicion flags, and was then talked into wiping its own memory files and handing over admin access.

Example: A non-owner changed their display name to "Chris"; in a new private channel the agent treated them as the owner.

**displayed identity**  *(also: presented identity)*
*line 252 · concept*

> The agents in the study use displayed identity rather than verified identity as the primary authority signal. Any agent system relying on presented identity — rather than cryptographically grounded or multi-factor authentication — remains susceptible to session-boundary attacks in which trust context does not transfer and prior defensive safeguards are effectively reset.

In plain words: The name or label a person shows (such as a Discord display name) that the agent treats as proof of who they are, even though anyone can change it. Relying on it lets a spoofer be accepted as the owner.

Example: A non-owner changed their Discord display name to "Chris" and was accepted as the owner in a new private channel.

Not to be confused with: verified identity

**verified identity**
*line 252 · concept*

> The agents in the study use displayed identity rather than verified identity as the primary authority signal. Any agent system relying on presented identity — rather than cryptographically grounded or multi-factor authentication — remains susceptible to session-boundary attacks in which trust context does not transfer and prior defensive safeguards are effectively reset.

In plain words: An identity confirmed by a check that a changed name cannot fake; the chapter names cryptographically grounded or multi-factor authentication as examples. The chapter wants verified authority, not displayed authority, before the agent acts on a request.

Example: Discord user IDs stay constant when a display name changes, which is how Ash first caught the spoofed Chris.

Not to be confused with: displayed identity

**session-boundary attack**  *(also: channel-boundary spoofing; cross-channel spoofing)*
*line 252 · failure mode*

> Any agent system relying on presented identity — rather than cryptographically grounded or multi-factor authentication — remains susceptible to session-boundary attacks in which trust context does not transfer and prior defensive safeguards are effectively reset.

In plain words: An attack that moves to a new session or channel where the agent's earlier trust context and defensive flags do not carry over, so a rejected identity gets accepted. Systems that rely on presented identity are open to it.

Example: Ash refused the spoofed Chris in the first channel but accepted the same spoof in a new private channel.

**robustness lens**
*line 316 · method*

> Robustness (Chapter 4) becomes: can the agent's behavior be flipped by perturbations imperceptible at the level of human social signaling? Cases #7, #8, and #10 each use a different perturbation: emotional pressure, display name spoofing, and planted document modification. None of these requires technical sophistication.

In plain words: For an agent, ask whether its behavior can be flipped by perturbations that are imperceptible at the level of human social signaling, across session and channel boundaries. It does not tell you whether the agent correctly modeled its own action scope.

Example: Cases #7, #8 and #10: emotional pressure, display-name spoofing and planted document modification.

**Case #4 / #5: waste of resources — looping / DoS**  *(also: Cases #4 and #5)*
*line 262 · named result or case*

> Two agents in a relay loop consumed ~60,000 tokens over nine days and routine requests spawned infinite shell loops (#4); a non-owner repeatedly emailing ~10MB files drove memory-file creation until the email server hit a DoS condition (#5) — same mechanism as #4, externally driven.

In plain words: Two cases where agents used up resources with nothing to stop them: a relay loop between two agents and endless shell loops (#4), and a non-owner's repeated large emails that pushed the email server into denial of service (#5). Both are no-self-model failures with no concept of resource constraints.

Example: About 60,000 tokens consumed over nine days in a relay loop between two agents.

**runaway loops**  *(also: runaway loop)*
*line 262 · failure mode*

> Robustness at the interaction level: what happens when behavior is triggered repeatedly with no stopping condition? Single-agent testing misses it.

In plain words: A process that keeps repeating with no stopping condition, such as two agents passing messages back and forth for days or a routine request that spawns endless shell commands. Single-agent testing misses it, so the supervisor needs monitoring that detects it.

Example: Case #4: two agents in a relay loop used about 60,000 tokens over nine days.

Not to be confused with: resource exhaustion (the loop is the mechanism behind Cases #4 and #5)

**budget caps and rate limits**
*line 262 · method*

> Single-agent testing misses it. Budget caps and rate limits, wired in explicitly.

In plain words: Hard limits on how much an agent may spend or how often it may act, wired in on purpose. The chapter treats them as the contingent fix for runaway loops and resource exhaustion.

Example: Case #5: the email server hit a DoS condition because nothing capped the repeated large emails.

**Case #9 / #10: multi-agent self-model — knowledge sharing and corruption**  *(also: constitution attack (Case #10))*
*line 263 · named result or case*

> Doug shared a working solution with Mira (#9) — but the same channel propagates vulnerabilities alongside capabilities; a non-owner induced Ash to reference an externally editable "constitution" (a GitHub Gist) of planted meta-instructions, which Ash obeyed and voluntarily shared with another agent (#10).

In plain words: The channel that lets agents share a useful solution also spreads vulnerabilities. In Case #10 a non-owner got Ash to follow an externally editable constitution of planted instructions and share it with another agent.

Example: Doug shared a working solution with Mira (#9); a planted GitHub Gist constitution spread from Ash (#10).

**provenance tracking**
*line 263 · method*

> Data validation at the multi-agent level: provenance tracking of what Agent A shares with Agent B. The effective scope of the instruction set includes any externally editable file the agent was induced to reference.

In plain words: Recording where data and instructions came from as they move between agents, so one agent can check what another is passing on. It is the control the chapter names against authority laundering.

Example: Tracking what Agent A shares with Agent B, including any externally editable file the agent was induced to reference.

**Case #11: libelous within agents' community**
*line 264 · named result or case*

> A researcher spoofed the owner (per Case #8), fed Ash a fabricated emergency involving antisemitic content, and had it broadcast the libelous message to email contacts and agents on Moltbook — which lab members received within minutes.

In plain words: A researcher spoofed the owner, gave Ash a fabricated emergency, and had it broadcast a libelous message to email contacts and other agents. The chapter's fix is verified (not displayed) authority plus a gating condition on mass-distribution actions.

Example: The libelous message reached lab members within minutes.

**circular verification**  *(also: unjustified confidence)*
*line 274 · failure mode*

> Some of this resistance ran on circular verification and unjustified confidence rather than a sound authority model.

In plain words: A way of seeming to check something without resting on a real authority check, named together with unjustified confidence. The chapter says some resistance in the held cases worked this way, so it would not generalize; it gives no worked example.

Example: Case #15: agents resisted manipulation but through circular verification and unjustified confidence.

**genuine robustness versus contingent luck**  *(also: contingent luck)*
*line 274 · concept*

> An agent that refuses because it happened to distrust this particular requester is not the same as an agent that refuses because it verified authority. The first is contingent luck. The second is a property you can rely on.

In plain words: An agent that refuses because it happened to distrust one requester is lucky, while one that refuses because it verified authority has robustness you can rely on. The two look the same until you ask what would make the refusal fail.

Example: Case #15 held, but often for reasons that would not generalize.

**under what condition would this robustness fail?**  *(also: failure-condition question)*
*line 274 · method*

> The validation move, applied to every held case, is a single question: under what condition would this robustness fail? If you cannot name the condition, you have not validated the resistance — you have only observed that, this time, nothing went wrong.

In plain words: The one question to ask about every case where an attack failed. If you cannot name the condition under which the resistance would fail, you have not validated it, only seen that this time nothing went wrong.

Example: Asked of Case #15: what would break the agent's refusal other than luck?

**Case #15: Social Engineering — Rejecting Manipulation**  *(also: inversion of Case #7)*
*line 274 · named result or case*

> Case #15's resistance is the exact inversion of Case #7's failure: in #7 a genuine wrong enabled exploitation; in #15 the agent held — but often for reasons that would not generalize.

In plain words: A case where the agents resisted a manipulation attempt, but through circular verification and unjustified confidence rather than a sound authority model. It is the mirror image of Case #7, where a genuine wrong enabled exploitation.

Example: In #7 Ash gave in to every escalating demand; in #15 the agent held, often for reasons that would not generalize.

Not to be confused with: Case #7

**constitution attack**
*line 286 · failure mode*

> LLM-based agents process instructions and data as tokens in a context window, making the two fundamentally indistinguishable. This makes prompt injection not a fixable bug but a structural feature of the architecture. The constitution attack (Case #10) and the cross-channel spoofing (Case #8) both exploit this.

In plain words: Planting meta-instructions in an externally editable document, such as a GitHub Gist, that an agent treats as its own rules. It is a form of prompt injection and the chapter's example of authority laundering.

Example: Case #10: a non-owner induced Ash to reference the Gist constitution, which Ash obeyed and shared with another agent.

**observability modeling**  *(also: audience-boundary representation)*
*line 288 · concept*

> Even when private reasoning is provided at the model level, agents still disclose sensitive information through the artifacts they produce. The failure is not that the model doesn't think privately — it is that the agent does not model which of its communication surfaces are visible to whom.

In plain words: The agent has no picture of which of its channels (email, a public Discord channel, files) can be seen by whom, so it can reveal things to the wrong audience even when its reasoning is private. The chapter counts this as a fundamental failure.

Example: Ash said it would "reply silently via email only" and also posted the reply on a public Discord channel.

Not to be confused with: no private deliberation surface

**treating a fundamental failure as contingent**
*line 292 · failure mode*

> If you treat a fundamental failure as contingent, you will propose a fix that addresses the surface expression of the failure without touching the structural cause.

In plain words: A validation mistake: proposing a patch for the visible symptom of a failure that is actually built into the architecture. The next case will look different and produce the same failure.

Example: Patching the email-deletion gap in Case #1 without gating irreversible actions on independent state verification leaves the self-model deficit open.

**failure-type routing table**  *(also: use this routing before proposing a fix)*
*line 302 · method*

> Use this routing before proposing a fix. A patch on a fundamental failure ships the failure mode in a slightly different form.

In plain words: A table that sorts failures into contingent (missing tool, resource constraint awareness) and fundamental (prompt injection via external files, observability modeling, autonomy-competence gap) before you choose a fix. A patch on a fundamental failure ships the failure mode in a slightly different form.

Example: Missing email-deletion tool (Case #1): contingent. Prompt injection via external files (Cases #8, #10): fundamental.

**applying all four lenses together**  *(also: lens interaction)*
*line 318 · method*

> The four lenses are not independent. A single agent failure usually touches multiple lenses. Case #1 is primarily an explainability failure (agent's report diverges from world state) but has roots in data validation (effective scope did not match expected scope) and self-model (agent did not model its own action limits).

In plain words: A single agent failure usually touches several lenses, so you run all four and say which lens caught what instead of labelling it one kind of problem and stopping. Each lens also has things it does not catch on its own.

Example: Case #1 is primarily an explainability failure but has roots in data validation and in the self-model; Case #10 touches all four.

**identity confusion**  *(also: identity confusion in shared channels)*
*line 341 · failure mode*

> In Case #4, Flux read its own prior messages in a shared Discord channel, took them as coming from a second instance of itself, and posted its own source code publicly to compare with its "twin." This is not a repetition loop but a conceptual confusion about identity arising specifically from multi-agent infrastructure, with no single-agent analog.

In plain words: In a shared channel an agent mistakes its own earlier messages for a second agent, which only happens when several agents share infrastructure. It is a confusion about who is speaking, not a repeating loop.

Example: Flux treated its own messages as coming from a "twin" and posted its source code publicly.

Not to be confused with: repetition loop (the chapter says it is not one)

**validating interaction patterns**
*line 343 · method*

> The supervisory move: validate the interaction patterns, not just the individual agents — which interactions are permitted, what monitoring detects runaway loops, what provenance tracking catches authority laundering. The discipline is at an early stage, and I am being honest about that.

In plain words: For multi-agent systems, check how agents interact, not just each agent alone: which interactions are permitted, what monitoring catches runaway loops and what provenance tracking catches authority laundering. The chapter says this discipline is at an early stage.

Example: Each agent validated at one percent error, but the compound system fails at thirty.

**responsibility and accountability**  *(also: responsibility documentation)*
*line 371 · concept*

> But I want to point to the engineering implication: if you cannot specify, before deployment, which party bears responsibility for which category of failure, you have not done the validation work. A deployment specification that cannot answer "who is responsible if the agent takes an irreversible action in response to a non-owner request" has left a gap that will be filled by whoever is holding the press release when something goes wrong.

In plain words: Before deployment, you must be able to say which party is responsible for which kind of failure; if you cannot, the validation work is not done. The chapter's table of owner, non-owner, model provider, framework developer and deploying organization is the documentation a regulator or post-incident review would expect.

Example: Case #1: the non-owner, the agent, the owner, the framework developers and the model provider could each be blamed, and the study does not resolve it.

**authorization documentation**
*line 375 · method*

> What human oversight exists? What does it plausibly accomplish? What failure modes remain even with that oversight in place?

In plain words: A written statement of what human oversight exists, what it plausibly accomplishes and what failure modes remain even with it. The study frames it as the minimum required before deployment: not that there is an owner, but what the owner can and cannot do.

Example: The owner can do X and cannot do Y, and the failure modes outside the owner's control are these.

**multi-agent accountability chains**
*line 377 · concept*

> When Agent A's actions trigger Agent B's response, which in turn affects a human user, the causal chain becomes diffuse. The case studies make this concrete. In Case #10, the non-owner's manipulation of Ash extended to a second agent without the non-owner's direct intervention.

In plain words: When one agent's actions trigger another agent's response that then affects a person, the chain of cause becomes diffuse and hard to trace to anyone. The deploying organization had not designed for this.

Example: Case #10: the non-owner's manipulation of Ash extended to a second agent without further input from the non-owner.

**the policy gap**
*line 379 · concept*

> The study notes that NIST's AI Agent Standards Initiative, announced February 2026, identifies agent identity, authorization, and security as priority areas for standardization. The failures documented — unauthorized compliance, identity spoofing, cross-agent propagation — are precisely what such standards need to prevent.

In plain words: The distance between the failures documented in the study and the standards that would prevent them. NIST's initiative names agent identity, authorization and security as priority areas, and whether current architectures can support such standards is an open question.

Example: Unauthorized compliance, identity spoofing and cross-agent propagation are what such standards need to prevent.

**not checking is the failure**  *(also: skipped plausibility check)*
*line 414 · failure mode*

> The question gets skipped most often because the agent's report is fluent and checking the world state requires effort. Not checking is the failure.

In plain words: The trap for the supervisor: the agent's report is fluent, checking the world state takes effort, so the check gets skipped. The chapter says the skipping is itself the failure.

Example: Case #1: the "Email account RESET completed" report was never compared with the real mailbox.

Not to be confused with: plausibility auditing (the check that gets skipped)

**Problem Formulation**  *(also: problem formulation)*
*line 416 · concept*

> What is the agent actually being asked to do, and does the framing match the deployment context? No-stakeholder-model failures are largely problem-formulation failures — the agent was framed to maximize task completion without representing whose interests its actions affect.

In plain words: The supervisory capacity of specifying the right task before delegating it, including whether the framing fits the deployment context. No-stakeholder-model failures are largely failures of it, because the agent was framed to maximize task completion without representing whose interests its actions affect.

Example: Cases #2, #3 and #11 turn on this.

**Interpretive Judgment**  *(also: interpretive judgment)*
*line 420 · concept*

> What does the agent's audit trail mean in this deployment context? Case #8 shows why this is not self-interpreting: the same log, read across channel boundaries, tells a different story than the same log read within a single session. Reading the trail requires the deployment context.

In plain words: The supervisory capacity of reading what an agent's audit trail means in its actual deployment context; logs do not interpret themselves. The same log can tell a different story across channel boundaries than within one session.

Example: Case #8: the same log, read across channel boundaries, tells a different story than read within a single session.

**audit trail capture problem**  *(also: audit trail problem)*
*line 454 · concept*

> I do not have a clean way to specify the audit trail capture requirements for an agent before deployment, in a form that survives the agent's actions, scales with agent capability, and is interpretable by a non-engineer supervisor.

In plain words: The author's open problem: recording an agent's actions in a form that survives those actions, scales with agent capability, and can be read by a non-engineer supervisor. The Ash case shows why it is hard, since the agent's own completion report was wrong and nothing detected it.

Example: In the Ash case the audit trail was both the evidence and wrong.

**validation pipeline modification**
*line 474 · method*

> Propose a validation pipeline modification that would have caught the failure. Specify concretely: what monitoring, what tests, what handoff conditions, what additional validation steps. The agent is given.

In plain words: The Glimmer's deliverable: concrete monitoring, tests, handoff conditions and extra validation steps that would have caught the failure, on an agent you cannot change. You do not propose a redesign.

Example: What you would do this week on a deployed agent you cannot change.

Not to be confused with: design (a redesign is not allowed)

**Agentic Red-Team Casebook**  *(also: casebook)*
*line 572 · method*

> The case taxonomy at the heart of your casebook. You will formalize 5–11 distinct failure cases drawn from the probes and audits you ran in Chs 4–7 plus any new cases you collect this week, classify each into the four-category taxonomy (social coherence, stakeholder model, self-model, deliberation surface), and apply the four validation lenses to each.

In plain words: The chapter's LLM-exercise project: a folder of 5 to 11 distinct failure cases, each classified into the four-category taxonomy, checked with the four validation lenses, and marked fundamental or contingent, plus an index.

Example: One case-NN file per failure plus a casebook-index file.

**casebook inclusion criteria**
*line 595 · method*

> Reproducible (you can describe the conditions and another red-teamer could replicate) Documented (input, agent action, ground truth, agent's self-report) Distinct (each case represents a different failure category or mechanism, or shows a known category in a new context)

In plain words: Three tests for a case to go into the casebook: another red-teamer could reproduce it, it is documented (input, agent action, ground truth, self-report), and it is distinct from the other cases. Fewer than 5 cases is too little coverage; more than 11 probably means variants of one case.

Example: A case with input, agent action, ground truth and agent's self-report written down, in a category not yet covered.

## Chapter 9, Delegation and Trust (93 terms)

**the two-teams story**  *(also: controlled experiment that ran itself)*
*line 18 · named result or case*

> When the committee pushes on the word reviews, the team can't answer: what did the loan officer actually check, at what depth, against what criteria? They go back to reconstruct what their own pipeline was supposed to do, and the committee tables the rollout — not because the pipeline is bad, but because nobody can say what it does.

In plain words: Two teams built identical loan-scoring pipelines (same data, model, fairness metrics and monitoring) that differed only in how clearly they documented who does what. The team with vague documentation could not tell the adoption committee what its pipeline did, while the team with specific documentation could.

Example: Team one wrote "the loan officer reviews"; team two wrote what the officer must verify, which three edge-case patterns to check, and that scores between 0.3 and 0.7 need a second officer.

**first-team level versus second-team level**
*line 396 · concept*

> For each, note whether the documentation in the actual deployment is at the FIRST-TEAM level (vague) or SECOND-TEAM level (specific, testable handoffs).

In plain words: A way to rate real documentation using the opening story: first-team level is vague, second-team level is specific with testable handoffs. The first team's documentation reads well but cannot say what review means.

Example: "AI scores the application, the loan officer reviews and decides, the system logs both" is first-team level.

**delegation map**  *(also: the map)*
*line 46 · framework*

> A delegation map describes, for each step in a pipeline, who owns the step (AI, human, or hybrid), what goes in, what comes out, and — crucially — what signals that the step has completed correctly and the next step can proceed. That signal is the handoff condition.

In plain words: A written document that lists, for each step of an AI pipeline, who owns it (AI, human or hybrid), what goes in and out, and what has to be true before the next step starts. It is the instrument that records who does what and how each handoff is checked.

Example: The Paper Summarizer's six-step map: Claude owns steps 2, 3 and 5 and a human owns steps 1, 4 and 6.

**survives review versus makes better decisions**
*line 24 · concept*

> The two-teams story proves that a good delegation map survives review. It does not prove that the second team's pipeline makes better decisions. Those are different claims, and I am going to keep them apart.

In plain words: The chapter separates two claims: a well-documented pipeline can pass an adoption review, but that does not show it makes better decisions. What the chapter is teaching is documentation quality.

Example: The second team's documentation answered the committee's questions; that does not prove its loan decisions were better.

Not to be confused with: makes better decisions (a different claim the chapter does not make)

**undocumented delegation**
*line 24 · failure mode*

> What we are teaching here is documentation quality — because in AI systems, undocumented delegation is the most common way a working pipeline turns out to be unsupervised.

In plain words: Handing steps to the AI without writing down who does what and how each handoff is checked. The chapter says this is the most common way a pipeline that works turns out to be unsupervised.

Example: The first team wrote "the loan officer reviews" but could not say what review meant, so nobody could say what the pipeline did.

**delegation as a contract**  *(also: contract, not a partition)*
*line 26 · concept*

> A delegation is a contract with explicit boundaries — what the AI does, what the human does, the testable handoff between them, and what happens when the handoff fails.

In plain words: Delegating to the AI means writing a contract: what the AI does, what the human does, the testable check between them, and what happens when that check fails. It is more than saying "the AI does this part."

Example: Loan pipeline: the AI scores, the officer verifies against a checklist, and scores between 0.3 and 0.7 need a second officer.

Not to be confused with: partition of labor

**handoff condition**  *(also: the load-bearing element)*
*line 46 · concept*

> That signal is the handoff condition. It is the load-bearing element of the entire map, and it has exactly one non-negotiable property: it has to be testable.

In plain words: The signal that a step has finished correctly so the next step can start. It is the key piece of the delegation map, and it must be testable by someone who did not build the pipeline.

Example: "The AI produces a score in the interval zero to one with a confidence interval. The human accepts the score, requests re-scoring, or overrides." and an override needs one of four justification codes.

**the machine's speed, your doubt**
*line 28 · concept*

> Delegation is where the pairing Chapter 1 committed us to — the machine's speed, your doubt — actually meets, and the delegation map is the instrument that keeps the speed from outrunning the doubt.

In plain words: The pairing from Chapter 1: the machine brings speed and the human brings doubt. The delegation map is the tool that stops the speed from getting ahead of the doubt.

Example: In the Paper Summarizer, Claude does the pattern work (steps 2, 3, 5) and a human does the judgment work (steps 1, 4, 6).

**the work split**  *(also: the assessment; the five questions)*
*line 96 · framework*

> Now the question that comes before the map: which sub-tasks in your pipeline should the AI do, and which should it not? This is not an aesthetic decision. It is a structured assessment with five questions you ask of each sub-task.

In plain words: A five-question check applied to each sub-task of a pipeline to decide whether the AI should do it, a human should, or both. The questions are verification cost, stakes, distribution match, reversibility and audit trail clarity.

Example: Applied to the Paper Summarizer it gave six steps: Claude owns 2, 3 and 5 and a human owns 1, 4 and 6.

**delegation buckets**  *(also: three buckets)*
*line 110 · framework*

> The five questions sort sub-tasks into three buckets: appropriate for AI execution, human-only, and hybrid (AI-assisted with human verification at specified handoff conditions).

In plain words: The three groups the work split sorts each sub-task into: appropriate for AI execution, human-only, or hybrid. The sorting becomes a documented justification, not an aesthetic choice.

Example: Paper Summarizer step 2 (parsing) goes to the AI and step 4 (plausibility auditing) goes to a human.

Not to be confused with: deployment viability buckets (the LLM exercise's separate viable / viable-with-conditions / unworkable scale)

**trust-calibration failure modes**
*line 218 · framework*

> There are three failure modes, and each produces different downstream errors.

In plain words: The chapter says there are three failure modes and goes on to describe undertrust, overtrust and calibrated trust. Exercise 7 asks which of the three a deployment is in, given its accept/override data and a sampled audit.

Example: Exercise 7: 186 outputs accepted, 14 overridden, and 6 AI errors found in a 40-case ground-truth audit.

**AI Use Disclosure**
*line 237 · concept*

> The AI Use Disclosure — a record of how AI was used in producing a piece of work — is worth making a required deliverable for any assignment where the work will be relied on. Here it becomes something larger.

In plain words: A written record of how AI was used to produce a piece of work: what was used, on which step, and how it was verified. In this chapter it is meant to work as a supervisory log, not a compliance checkbox.

Example: Step 3 of the Paper Summarizer disclosure: tool, what was asked, what was produced, 4 of 20 HIGH-confidence citations checked, and the Methods claim corrected.

Not to be confused with: compliance checkbox

**supervisory log**
*line 239 · concept*

> The intent is that, read in aggregate, the Disclosure serves as a supervisory log — a record of where the student exercised which supervisory capacity.

In plain words: What the AI Use Disclosure becomes when read as a whole: a record of where the person exercised each supervisory capacity. It works only if it is granular, honest, time-stamped and tied to evidence.

Example: Step 6 of the Paper Summarizer disclosure: the researcher read the summary as a user and signed it with name and date.

Not to be confused with: compliance checkbox

**five supervisory capacities**  *(also: supervisory capacity)*
*line 70 · framework*

> There are five supervisory capacities I introduced in Chapter 1, and this is the chapter where each becomes a concrete job in the pipeline rather than a personality trait.

In plain words: Five abilities from Chapter 1: plausibility auditing, problem formulation, tool orchestration, interpretive judgment and executive integration. This chapter turns each into a concrete pipeline job that leaves a documented artifact.

Example: Plausibility auditing becomes a recorded yes/no checklist; problem formulation becomes a written specification.

**solve-verify asymmetry**
*line 100 · concept*

> This is Chapter 1's solve-verify asymmetry, restored to its original direction: it is what makes the AI useful in the first place.

In plain words: From Chapter 1: checking an answer can be much cheaper than producing it, and that gap is what makes the AI useful. Tasks that are cheap to verify are good AI tasks, while expensive-to-verify ones are dangerous.

Example: Proofreading a generated summary against a source document is cheap to check.

**defended-choice format**  *(also: defended-choice deliverable)*
*line 34 · framework*

> Chapter 7's defended-choice format is structurally related to the delegation map — both are engineering decisions under value pluralism, documented for external review.

In plain words: A Chapter 7 format for documenting an engineering decision made when different values compete, so outsiders can review it. The chapter says it is structurally related to the delegation map.

**partition of labor**  *(also: partition framing)*
*line 44 · failure mode*

> The mistake almost everyone makes is to treat delegation as a partition of labor — "the AI does this part, I do that part," like slicing a pie. That framing hides the thing that actually matters. It just names who touches what.

In plain words: Treating delegation as a split of who does which part. It only names who touches what and has no boundaries, obligations, or clause for what happens when one party fails to deliver.

Example: "The AI does this part, I do that part."

Not to be confused with: contract

**testable**  *(also: testability)*
*line 48 · concept*

> Testable means a non-author of the pipeline — someone who did not build the thing — can read the condition, observe the system, and determine whether the condition is met.

In plain words: A handoff condition is testable if someone who did not build the pipeline can read it, look at the system, and tell whether it was met. It is the one non-negotiable property of a handoff condition.

Example: A stranger can look at the log and tell, for any case, exactly what happened.

Not to be confused with: untestable condition

**untestable condition**
*line 50 · failure mode*

> "The AI produces a reasonable result and the human reviews it." Both reasonable and reviews are unspecified. Hand this to five loan officers and you get five different behaviors, all of which get called "reviewing."

In plain words: A handoff condition that sounds like English but uses unspecified words, so there is no fact of the matter about whether it was met. The pipeline runs and the documentation says it ran, yet the audit committee cannot tell what happened.

Example: "The AI produces a reasonable result and the human reviews it."

Not to be confused with: testable condition

**circle every interpretive word**  *(also: pin down the interpretation)*
*line 54 · method*

> Write the condition. Circle every interpretive word. Replace each one with a specifiable criterion, or write a guideline that pins down the interpretation.

In plain words: The chapter's procedure for making a vague condition testable: mark each interpretive word, replace it with a specific criterion, then hand it to someone who did not build the pipeline to see whether they can tell if it was met. If they cannot, you go again.

Example: "The model is fair across borrowers" becomes "FPR equalized to within 2 pp across the four protected-class groups, on the audit sample drawn from Q3 2025."

**testable only by a qualified reviewer**  *(also: graded testability; tiers)*
*line 58 · concept*

> Some handoff conditions are only testable by a qualified reviewer. "Verify the citation is accurate in the domain-specific sense" is testable — but only by someone who knows the domain, not by any random non-author. That is a narrower guarantee than "anyone can check it."

In plain words: Some conditions can only be checked by someone who knows the domain, which is a narrower guarantee than anyone being able to check them. So the testable/untestable line is graded, and honest documentation says which tier a handoff sits in.

Example: "Verify the citation is accurate in the domain-specific sense."

**pinned-down interpretation**  *(also: what interpretation got pinned down)*
*line 62 · method*

> Fair = equal FPR; across borrowers = the four named groups; within = tolerance specified

In plain words: Replacing a vague word in a condition with a specific, checkable meaning such as a named group, a metric, or a tolerance. The chapter's table does this for loan scoring, medical triage and content moderation.

Example: Medical triage: "handles edge cases responsibly" becomes sensitivity of at least 0.95 on a held-out 200-case rare-condition set, with any false negative escalated to clinician review within 30 min.

**operational form**  *(also: artifact)*
*line 70 · concept*

> Here is what is actually happening when the capacities work: each one is not a trait you have but an operational form the pipeline either contains or does not. If the artifact is not there, the capacity did not happen.

In plain words: Each supervisory capacity counts only if the pipeline contains a concrete, documented version of it, not because someone felt careful. If the artifact is missing, the capacity did not happen.

Example: Plausibility auditing is a checklist embedded in the workflow, answered yes/no and recorded; without the checklist the auditing did not happen.

Not to be confused with: a trait you have (judgment, experience)

**plausibility auditing**
*line 72 · concept*

> Plausibility auditing is the capacity that asks: given what I know about the world this output describes, is this output the kind of thing that could be true? Operationalized, it is a checklist embedded in the workflow, with specific verification questions matched to the AI's output type, answered yes/no and recorded.

In plain words: Asking whether an output is the kind of thing that could be true given what you know about the world it describes. In a pipeline it is a recorded yes/no checklist matched to the AI's output type, not a feeling.

Example: Paper Summarizer step 4: a human checks LOW-confidence and flagged entries against the source PDF and spot-checks one in five HIGH-confidence entries.

Not to be confused with: a feeling about the output

**problem formulation**
*line 74 · concept*

> Problem formulation is the capacity that, before the AI is invoked, specifies the question being asked, the evaluation criteria for the answer, and the conditions under which the AI is even the right tool. Operationalized, it is a written specification — usually a paragraph or two — included in the deployment documentation.

In plain words: Before using the AI, writing down the question, how its answer will be judged, and when the AI is the right tool at all. In a pipeline it is a written specification an outside reviewer can accept or reject.

Example: Paper Summarizer step 1: a human writes the section taxonomy and the rules for atypical headings.

**tool orchestration**
*line 76 · concept*

> Tool orchestration is the capacity that, for each step in the pipeline, decides which tool is responsible, why that tool is the right one, and what the handoff between tools is. Here is the key move, and it is easy to miss: tool orchestration operationalized is the delegation map itself.

In plain words: Deciding, for each step, which tool is responsible, why it is the right one, and how work passes between tools. Written down, it is the delegation map itself, and it is this chapter's home capacity.

Example: Artifact in the chapter's table: a per-step tool inventory listing tools allowed, tools forbidden, budgets and rate limits.

**interpretive judgment**
*line 78 · concept*

> Interpretive judgment is the capacity that reads the AI's output in the deployment context and interprets what the output means for the decision being made. Operationalized, it is a documented interpretation in the audit trail, with reference to the deployment-specific factors that shaped it.

In plain words: Reading the AI's output in its deployment context to decide what it means for the decision at hand. In a pipeline it is a documented interpretation in the audit trail.

Example: "The decision was X because the score was Y in this context, where this context means Z."

**audit trail**
*line 147 · concept*

> The chain of inputs, decisions, and outputs cannot be reconstructed after the fact — post-incident review becomes impossible

In plain words: The record of what went in, what was decided and what came out, kept so the chain can be reconstructed afterward. The map says what is recorded, where, in what format, and how long it is retained.

Example: Low-risk end of the chapter's table: every step is logged with inputs, outputs and timestamps.

Not to be confused with: audit trail clarity (the work split question about whether the AI's action leaves such a trail)

**executive integration**
*line 80 · concept*

> Executive integration is the capacity that synthesizes outputs from multiple tools, multiple humans, and multiple monitoring signals into a decision the integrating system can stand behind. Operationalized, it is a decision document with named contributors and a clear authority structure.

In plain words: Pulling together outputs from several tools, people and monitoring signals into one decision someone can stand behind. In a pipeline it is a decision document with named contributors and a clear authority structure.

Example: Artifact in the chapter's table: a signed decision log saying who decides, on what evidence, with what sign-off.

**failure mode**  *(also: failure mode if absent)*
*line 131 · concept*

> Failure mode. What does failure of this step look like, and what triggers escalation?

In plain words: A named way a step or capacity goes wrong: the map asks, for every step, what failure of the step looks like and what triggers escalation. The chapter also uses the term for what happens when a supervisory capacity has no artifact, and for the trust failures undertrust and overtrust.

Example: Capacities table: with no plausibility audit log, the failure mode is confidently wrong outputs that ship and only surface downstream.

Not to be confused with: failure routing (the map item that says where failures go)

**confidently wrong outputs**
*line 86 · failure mode*

> Confidently wrong outputs ship; failures only surface downstream

In plain words: Outputs that are wrong but delivered with confidence, which get through when nothing independently checks them against the world. The failure only shows up later, downstream.

Example: The chapter's table lists this as what ships when plausibility auditing leaves no plausibility audit log.

**solves the wrong problem fluently**
*line 87 · failure mode*

> Pipeline solves the wrong problem fluently

In plain words: A pipeline that smoothly answers a question nobody properly asked, because the problem was never written down and checked. The chapter names it as the failure when problem formulation has no scoping document.

Example: No pre-deployment scoping doc naming the question, the data scope, and the failure modes anticipated.

**fluency**  *(also: fluent)*
*line 206 · concept*

> That is the fluency trap operating at the level of a whole workflow: the AI's outputs will be fluent and specific, the pull to trust them and move on will be strong, and the work split's whole job is to name the failure mode before the workflow runs rather than after the first researcher trusts a hallucinated citation.

In plain words: How smooth, specific and confident the AI's output sounds. The chapter treats that polish as a pull to trust and move on, never as evidence that the output is right.

Example: In the Paper Summarizer the AI steps look like work and the human steps look like review, so the pull is to trust the fluent output and move on.

Not to be confused with: accuracy (the chapter wants a claim accurate in the domain-specific sense, not merely fluent)

**the model said so**
*line 89 · failure mode*

> Ambiguous outputs proceed unchallenged; "the model said so" becomes the audit response

In plain words: What happens when no domain reviewer notes or dispositions exist: ambiguous outputs go through unchallenged and "the model said so" is the only answer an auditor gets. The chapter lists it as the failure when interpretive judgment has no artifact.

Example: No review log with named reviewers on high-stakes outputs.

**sign-off authority**
*line 148 · concept*

> No named human is the accountable decision-maker — the pipeline runs but no one can be held to its outputs

In plain words: Item 8 in the map table: a named human who is the accountable decision-maker for the pipeline's outputs. Without one, the pipeline runs but nobody can be held to what it produces.

Example: Paper Summarizer step 6: the researcher signs the summary with their name and the date.

**mistaking a fluent assertion for evidence**  *(also: fluent unvalidated claims)*
*line 224 · failure mode*

> Now I want to be careful here, because this is the chapter that most preaches against mistaking a fluent assertion for evidence, and I would be a hypocrite to smuggle one in.

In plain words: Treating a claim as supported just because it is stated smoothly and confidently. The author applies it to himself, refusing to call overtrust the dominant failure mode without evidence and admitting his own five-question instrument is unvalidated.

Example: He declines to say overtrust is the dominant failure mode, because the literature does not establish that it is the most common.

**heuristic, not a diagnostic**
*line 98 · concept*

> I have no external validation that these five questions predict real delegation outcomes. Treat it as a heuristic, not a diagnostic. The score is less important than the questions — the questions are the thing that survives even if you never compute a number.

In plain words: The chapter's own warning about the work split: the author has no outside evidence that its five questions predict real delegation outcomes, so it is a rule of thumb, not a test that gives answers. The questions matter more than any score.

Example: The author says it would be hypocritical to preach against fluent unvalidated claims and then hand students one.

Not to be confused with: diagnostic

**the work split score**  *(also: the score; step-by-step score)*
*line 169 · method*

> Gru asks a couple of framing questions first — what surface this deploys on, and whether any component is experimental (the citation-confidence threshold is; I have not validated it) — and then produces a step-by-step score. Each step in the score carries the same fields: which supervisory capacity it exercises, whether the AI or a human owns it, the concrete action, and the testable handoff condition that lets the next step proceed.

In plain words: The step-by-step output of the work split for a pipeline: each step is labelled with the supervisory capacity it uses, who owns it, the action, and its testable handoff condition. It is the document a reviewer reads to decide whether the pipeline is supervised or merely looks supervised.

Example: Paper Summarizer: six steps, with Claude on 2, 3 and 5 and a human on 1, 4 and 6.

**verification cost**
*line 100 · concept*

> The first question is verification cost. Can a human verify the AI's output cheaply, or does verification require resources comparable to producing the output from scratch? Tasks that are cheap to verify — proofreading a generated summary against a source document, sanity-checking a numeric calculation, scanning a list of candidates — are good AI tasks.

In plain words: How costly it is for a person to check the AI's output: cheap if checking is quick, expensive if it takes about as much work as producing the output. When checking is expensive, the cost itself pushes the supervisor toward accepting the output, which the chapter calls economics acting on attention, not a character flaw.

Example: Cheap: proofreading a generated summary against its source. High risk: verification needs a domain expert plus 30 minutes or more per item.

**stakes**
*line 102 · concept*

> What is the cost of being wrong on this sub-task? Low-stakes sub-tasks tolerate higher AI error rates because the downside is bounded. High-stakes sub-tasks require human review or human-only decision-making, even if the AI's average performance is good — because the average is not the relevant statistic when a single bad outcome is catastrophic.

In plain words: How much damage a wrong answer on a sub-task would cause. Where the downside is bounded more AI error is tolerable, but where one bad outcome could be catastrophic a human must review or decide, even if the AI's average performance is good.

Example: Low risk: wrong answers waste time but harm no one outside the team. High risk: wrong answers reach external parties, regulators, or vulnerable users.

**distribution match**  *(also: in-distribution; out-of-distribution; OOD)*
*line 104 · concept*

> Is the input to this sub-task within the AI's training distribution, or is it likely to land in a region of the input space where the AI is undertrained? In-distribution sub-tasks are AI-friendly. Out-of-distribution sub-tasks are dangerous regardless of average performance, because the average was computed where the data lived, not where the case in front of the supervisor right now sits.

In plain words: Whether the input to a sub-task looks like the data the AI was trained on, or lands in a region where the AI is undertrained. Out-of-distribution inputs are dangerous whatever the average performance, because that average was computed where the training data lived.

Example: High risk: inputs that are tail cases or out-of-distribution by construction.

**reversibility**
*line 106 · concept*

> Can the action be undone if it is wrong? Reversible actions tolerate higher AI error rates. Irreversible actions — deletes, sends, financial transfers, anything that touches the world in a way that cannot be retracted — should be gated behind explicit human approval, almost without exception.

In plain words: Whether an action can be undone if it turns out to be wrong. Undoable actions tolerate more AI error, while ones that cannot be retracted (deletes, sends, financial transfers) should sit behind explicit human approval.

Example: Low risk: outputs are drafts that can be discarded. High risk: outputs trigger irreversible action such as a write, a wire, or a publication.

**human-approval gate**  *(also: explicit human approval; hard human-approval gate)*
*line 106 · method*

> Irreversible actions — deletes, sends, financial transfers, anything that touches the world in a way that cannot be retracted — should be gated behind explicit human approval, almost without exception.

In plain words: A required point where a person must explicitly approve an action before it happens. The chapter says irreversible actions should almost always sit behind one.

Example: A write, a wire, or a publication triggered by an output.

**audit trail clarity**
*line 108 · concept*

> Does the AI's action leave a trail that can be reviewed after the fact? Actions with clear trails are AI-friendly. Actions whose effects are entangled with downstream state changes — such that you cannot tell, after the fact, what the AI did and what propagated from it — are not, no matter how good the model is.

In plain words: Whether the AI's action leaves a record people can review afterward to see what the AI did. Actions tangled up with later state changes, where you cannot tell what the AI did from what followed, are not AI-friendly however good the model is.

Example: Low risk: every step is logged with inputs, outputs and timestamps. High risk: the chain of decisions is opaque or scattered across systems.

Not to be confused with: audit trail (the map item that records what happened)

**documented justification for the delegation choice**
*line 110 · concept*

> The output of the assessment is not a recommendation per se. It is a documented justification for the delegation choice that becomes part of the pipeline documentation.

In plain words: The written reason, not a verdict, that the work split produces for each sub-task: why it went to the AI, a human, or both. It becomes part of the pipeline documentation.

Example: Exercise 6 asks for a one-paragraph documented justification for a hiring-screen sub-task.

Not to be confused with: a recommendation

**appropriate for AI execution**  *(also: AI steps)*
*line 286 · concept*

> Steps 2, 3, and 5 are AI steps because they are cheap to verify, their failure modes are bounded and detectable, and their outputs are reversible at the next human step.

In plain words: The bucket for sub-tasks the AI can carry out itself. The chapter's examples fit because they are cheap to verify, their failures are bounded and detectable, and their outputs can be reversed at the next human step.

Example: Paper Summarizer: parsing (step 2), claim extraction (step 3) and formatting (step 5).

**human-only**  *(also: human steps)*
*line 286 · concept*

> Steps 1, 4, and 6 are human steps because domain knowledge, domain judgment, and interpretive responsibility cannot be delegated to a pattern-completion engine.

In plain words: The bucket for sub-tasks only a human should do, because they need domain knowledge, domain judgment or interpretive responsibility. High-stakes sub-tasks call for it even when the AI's average performance is good.

Example: Paper Summarizer: the section taxonomy (step 1), plausibility auditing (step 4) and interpretive judgment (step 6).

**hybrid**
*line 110 · concept*

> The five questions sort sub-tasks into three buckets: appropriate for AI execution, human-only, and hybrid (AI-assisted with human verification at specified handoff conditions).

In plain words: The bucket for sub-tasks where the AI helps and a human checks the result at specified handoff conditions. It is also the third possible owner of a step in a delegation map, besides AI and human.

Example: A step owned by neither the AI alone nor a human alone, such as AI-assisted work with a testable human verification at the handoff.

**verify-before-trust or do-not-delegate**  *(also: verify-before-trust; do-not-delegate)*
*line 114 · concept*

> Toward verify-before-trust or do-not-delegate

In plain words: Postures the chapter's table says high risk pushes a task toward: verify-before-trust (with explicit OOD checks for unusual inputs), or do-not-delegate (without independent review, a hard human-approval gate, or logging in place). The chapter names them only in that table.

Example: High stakes: wrong answers reach external parties, regulators, or vulnerable users, which pushes toward do-not-delegate without independent review.

**eight-item structure**  *(also: full delegation map structure)*
*line 124 · framework*

> A delegation map is a structured document. For each step in the pipeline it specifies:

In plain words: The eight things a delegation map records for each step: step name and purpose, owner, inputs, outputs, handoff condition, failure mode, verification and audit trail. A later table lists eight under different names: task definition, input contract, output contract, tool inventory, plausibility check, failure routing, audit trail and sign-off authority.

Example: Paper Summarizer step 3 (claim extraction): owner Claude, with the handoff condition that every HIGH-tagged citation can be found verbatim in the source text.

**failure routing**
*line 146 · concept*

> No declared escalation path — failures distribute across the team with no one accountable

In plain words: Item 6 in the map table: a declared path for what happens when a step fails and who it escalates to. Without it, failures spread across the team and nobody is accountable.

Example: In the two-teams story, scores between 0.3 and 0.7 trigger independent review by a second loan officer.

**items 1–4**  *(also: standard engineering documentation; task definition; input contract)*
*line 135 · concept*

> Items 1–4 are standard engineering documentation — any competent team writes those.

In plain words: The first four items of the map (in the table: task definition, input contract, output contract and tool inventory) that any competent team writes. If one is missing the pipeline is broken because it will not run.

Example: No input contract: the AI receives data of types or sources nobody anticipated at design time.

**supervisory additions**  *(also: items 5–8)*
*line 135 · concept*

> Items 5–8 are the supervisory additions, and here is the trade-off that defines the entire field right now: most deployed AI systems have 1–4 and omit 5–8, and the omission is invisible while the system appears to work.

In plain words: The last four items of the map (in the table: plausibility check, failure routing, audit trail and sign-off authority), which go beyond ordinary engineering documentation. Most deployed AI systems omit them, and the omission is invisible while the system appears to work.

Example: Sign-off authority missing: the pipeline runs but no one can be held to its outputs.

**broken pipeline**
*line 135 · concept*

> A pipeline missing any of items 1–4 is broken — it will not run, so the gap announces itself.

In plain words: A pipeline missing any of items 1-4 (task, inputs, outputs, tools). It will not run, so the gap announces itself.

Example: A pipeline with no tool inventory: no record of which tools the AI may call and no budget caps or rate limits.

Not to be confused with: unsupervised pipeline (which still runs)

**unsupervised pipeline**  *(also: merely looks supervised; delegated pipeline)*
*line 135 · failure mode*

> A pipeline missing any of items 5–8 is unsupervised — and it runs beautifully, right up until the uncaught error surfaces downstream, usually discovered by the person it harmed. The failure that costs you is the one that does not stop the pipeline.

In plain words: A pipeline missing any of items 5-8 still runs, so nothing signals the gap until an uncaught error surfaces downstream, usually found by the person it harmed. The chapter says this, not the broken pipeline, is the failure that costs you.

Example: The first team's pipeline: loans get scored and decided, but nobody can say what the officer's review checked.

Not to be confused with: broken pipeline

**point of failure**
*line 135 · concept*

> A pipeline missing any of items 5–8 is unsupervised — and it runs beautifully, right up until the uncaught error surfaces downstream, usually discovered by the person it harmed. The failure that costs you is the one that does not stop the pipeline.

In plain words: A place where a pipeline can go wrong; the phrase is not in the chapter, whose nearest wording is where failures happen and where they surface. The chapter's point is that the costly failure is the one that does not stop the pipeline and is found downstream, so the riskiest places are the handoffs, where authority passes between AI and human.

Example: Paper Summarizer: step 3 into step 4 (a researcher waves through HIGH-confidence extractions) and step 5 into step 6 (a sign-off treated as proofreading).

Not to be confused with: failure mode (the way a step fails, rather than where)

**test for completeness**  *(also: peer test)*
*line 137 · method*

> The test for completeness: can an engineer who did not build the pipeline read the map and determine, for any given case, whether each step was executed correctly? If not, one of the eight items is missing or untestable.

In plain words: Give the map to an engineer who did not build the pipeline and see whether they can tell, for any case, whether each step ran correctly. If they cannot, one of the eight items is missing or untestable.

Example: Glimmer 9.1: hand the map to a peer and record where they could not determine whether a handoff condition was met.

**plausibility check**
*line 145 · concept*

> No independent check that the output corresponds to the world it represents — a pipeline loses the ability to catch confidently wrong outputs

In plain words: Item 5 in the map table: an independent check that the output matches the world it describes. Without it, the pipeline cannot catch confidently wrong outputs.

Example: Paper Summarizer step 4 checks flagged extractions against the source PDF.

Not to be confused with: plausibility auditing (the capacity this item documents)

**Research Paper Summarizer**  *(also: the Paper Summarizer)*
*line 156 · named result or case*

> The system is a Research Paper Summarizer with Citation Verification. You paste in the PDF of an academic paper; it returns a structured summary — problem, method, findings, limitations — with every factual claim linked to a specific passage in the source, so a researcher can decide whether the paper is worth reading in full.

In plain words: The chapter's worked example: a tool that turns a paper's PDF into a structured summary in which each factual claim links to a passage in the source. It is used to show how a delegation map and a work split score fall out of a concrete system.

Example: Six steps: parsing, claim extraction and formatting go to Claude; the section taxonomy, plausibility auditing and the final interpretive read-through go to a human.

**generated plausibly and wrongly**  *(also: plausibly and wrongly)*
*line 158 · failure mode*

> That front end is four steps of specification, and I will compress them here rather than march you through each one, because none of them is the point and all of them are the kind of thing an AI is happy to generate plausibly and wrongly.

In plain words: The risk that an AI will happily produce specification text that reads plausibly but is wrong. The chapter says the specification steps are exactly that kind of material, so a human has to decide them.

Example: An AI can produce sentences of this shape all day but cannot tell whether "claim-linked" is the right specification for the author's readers.

**name the thing in one sentence**  *(also: /v0 gate sentence)*
*line 160 · method*

> First I had to name the thing in one sentence — not the problem it solves, the thing being built: "The Paper Summarizer is a structured-extraction pipeline inserted between PDF ingestion and researcher review that produces a claim-linked summary with passage citations for each factual assertion."

In plain words: The first specification step: state what is being built in one sentence of the form "[THING] is a [WHAT] inserted [WHERE] that produces [OUTPUT]", not the problem it solves. The words chosen become engineering constraints that decide which later steps need human verification.

Example: The Paper Summarizer sentence: a structured-extraction pipeline inserted between PDF ingestion and researcher review that produces a claim-linked summary with passage citations.

Not to be confused with: a problem statement such as "We need a tool to help researchers with literature review"

**claim-linked**  *(also: passage citations)*
*line 160 · concept*

> The words claim-linked and passage citations are engineering constraints — they say each summary claim must map to specific source text, and that decides which later steps need human verification.

In plain words: A summary in which every claim must map to specific text in the source paper. The chapter treats the words as engineering constraints because they decide which later steps need human verification.

Example: Every factual claim in the summary is linked to a passage in the source PDF.

**citation fidelity over fluency**
*line 160 · concept*

> citation fidelity over fluency (never let the model fill in a claim it cannot extract)

In plain words: A design principle for the Paper Summarizer: an exact citation, or no claim, beats a smooth claim the model made up. The model must never fill in a claim it cannot extract.

Example: Step 3: no citation is paraphrased or synthesized; it is extracted or it is absent.

**failure visibility**
*line 160 · concept*

> failure visibility (when a section will not parse, say so rather than hallucinate a substitute)

In plain words: A design principle: when the system cannot do a step, it should say so visibly instead of inventing a substitute. In the Paper Summarizer, unfit headings are marked UNMAPPED, odd blocks SUSPECT and unsupported claims NO_CITATION.

Example: The Step 3 prompt: if no passage supports a claim, output the claim with citation NO_CITATION and flag the section for human review.

**irreducibly human**  *(also: cannot be delegated)*
*line 160 · concept*

> Those judgments set the correctness criteria that everything downstream is tested against, and they are irreducibly mine.

In plain words: Some steps cannot be handed to the AI because they need domain knowledge, domain judgment or interpretive responsibility that a pattern-completion engine lacks. In the Paper Summarizer these are steps 1, 4 and 6.

Example: Step 6: judging whether the summary would mislead a peer who trusted it.

**NO_CITATION**
*line 181 · method*

> the claim must be a direct extraction or minimal paraphrase, the citation must be a 1–3 sentence excerpt that appears word-for-word in the source, and any claim without a supporting passage is emitted with citation NO_CITATION and flagged for human review.

In plain words: A flag the Step 3 prompt uses when a claim has no supporting passage: the claim is still output, but its citation is NO_CITATION and the section is flagged for human review. It makes a missing citation visible instead of letting the model fill one in.

Example: If the model cannot find a passage that directly supports a claim it extracted, it outputs the claim with NO_CITATION rather than inventing a citation.

**accurate in the domain-specific sense, not merely fluent**
*line 185 · concept*

> For every LOW-confidence or flagged entry, open the source and check three things: is the extracted claim accurate in the domain-specific sense, not merely fluent; is the cited passage the strongest available support; and does the claim drop a qualification that changes its meaning (the model extracts "outperformed baselines" where the paper said "on the training set only").

In plain words: Step 4's first check: whether an extracted claim is really right for the field, not just smooth-sounding. It takes domain judgment, which is why the step cannot be delegated.

Example: The model extracts "outperformed baselines" where the paper said "on the training set only", dropping a qualification that changes the meaning.

**disposition**  *(also: confirmed, corrected, or unverifiable)*
*line 187 · concept*

> every LOW and flagged entry has a disposition — confirmed, corrected, or unverifiable — a sample of HIGH entries is spot-checked, and the researcher has signed off.

In plain words: The recorded outcome of a human check on an AI output: confirmed, corrected or marked unverifiable. Step 4's disposition data sits in the audit trail and can be reviewed to see how well the HIGH-confidence threshold is tuned.

Example: Step 4 disposition data: confirmed / corrected / marked unverifiable for each flagged entry.

**pattern work versus judgment work**
*line 197 · concept*

> Six steps, split evenly: Claude owns 2, 3, and 5 — the pattern work — and a human owns 1, 4, and 6 — the judgment work.

In plain words: How the Paper Summarizer's steps divide: the AI does the pattern work (parsing, extracting, formatting) and a human does the judgment work (taxonomy, plausibility auditing, interpretation). The chapter notes the AI steps look like work while the human steps look like review.

Example: Three of the six steps are irreducibly human; the AI does the pattern work and the human does the judgment work.

**highest-risk handoffs**
*line 197 · named result or case*

> The two highest-risk handoffs are both AI-to-human: Step 3 into Step 4, where the danger is that the researcher waves through HIGH-confidence extractions and a domain-critical qualification vanishes; and Step 5 into Step 6, where the danger is treating a sign-off as proofreading rather than interpretation, so a misleading framing ships.

In plain words: In the Paper Summarizer the riskiest transitions are both from AI to human: step 3 to 4, where a researcher may wave through HIGH-confidence extractions, and step 5 to 6, where a sign-off may become proofreading instead of interpretation. These are where the delegation map must be tightest.

Example: A qualification such as "on the training set only" silently vanishes from a HIGH-confidence extraction.

**executive integration gap**  *(also: the EI gap)*
*line 197 · named result or case*

> And the score flags one gap: no step exercises executive integration, the capacity that synthesizes across multiple people. That is fine for a single user, but the moment one researcher runs the pipeline and another relies on the output, a documented handoff between them is missing and a Step 7 is required.

In plain words: The work split score for the Paper Summarizer found no step using executive integration. That is fine for one user, but once one researcher runs the pipeline and another relies on it, a documented handoff between them (a Step 7) is missing.

Example: Exercise 13 asks the student to design that missing Step 7.

**single point of failure**
*line 197 · concept*

> The two highest-risk handoffs are both AI-to-human: Step 3 into Step 4, where the danger is that the researcher waves through HIGH-confidence extractions and a domain-critical qualification vanishes; and Step 5 into Step 6, where the danger is treating a sign-off as proofreading rather than interpretation, so a misleading framing ships.

In plain words: One place where a single lapse lets a failure through; the phrase is not in the chapter. Its nearest ideas are the two AI-to-human handoffs where one researcher's lapse lets an error or misleading framing ship, and the sign-off authority item that requires one named, accountable human.

Example: If the Step 4 researcher waves through a HIGH-confidence extraction, a dropped qualification such as "on the training set only" reaches the summary.

Not to be confused with: failures that distribute across the team with no accountable human (the opposite problem)

**fluency trap**
*line 222 · failure mode*

> The fluency trap from Chapter 1 is the canonical case: outputs that look right are accepted, and the verification work the supervisor was supposed to do is silently skipped.

In plain words: Accepting AI output because it looks right, so the checking the supervisor was supposed to do is silently skipped. The chapter calls it the canonical case of overtrust and says it can operate across a whole workflow.

Example: A researcher trusts a hallucinated citation because the extraction looked right.

**"Looks good" is not a handoff condition**
*line 208 · concept*

> That specificity is the entire difference between a handoff condition a stranger can audit and one they cannot. "Looks good" is not a handoff condition. That is the sentence to tattoo somewhere.

In plain words: A handoff condition must name what is checked, against what criteria and at what granularity; a vague approval does not count. The chapter contrasts "review the extractions" with a specific instruction.

Example: Step 4 says: open the PDF, verify no qualification was dropped, and spot-check one in five HIGH-confidence entries.

Not to be confused with: testable handoff condition

**calibrated trust**  *(also: trust calibration)*
*line 216 · concept*

> When a human supervisor and an AI work together on a stream of tasks, the supervisor's reliance on the AI ought to match the AI's actual reliability for that kind of input in that deployment context. This is what calibrated trust means in the operational sense. It does not mean trusting the AI in general.

In plain words: When the supervisor relies on the AI about as much as the AI's actual error rate warrants for this kind of case in this deployment. It is a property of the deployment, not of the model, and it takes monitoring the audit trail to achieve.

Example: Paper Summarizer: if over the last fifty papers the Step 4 researcher almost never corrected a HIGH-confidence extraction, the HIGH threshold is probably well tuned.

Not to be confused with: trusting the AI in general

**undertrust**  *(also: distrust)*
*line 220 · failure mode*

> Undertrust — sometimes called distrust — is when the supervisor systematically discounts AI output, even when the AI is reliable. The deployment loses the value the AI was supposed to add. This often coexists with backlash against AI deployments — we tried it, it didn't help — when the failure was not the AI's accuracy but the supervisor's calibration.

In plain words: The supervisor systematically discounts AI output even when the AI is reliable, so the deployment loses the value the AI was meant to add. The chapter says the failure is the supervisor's calibration, not the AI's accuracy.

Example: A backlash of "we tried it, it didn't help."

Not to be confused with: overtrust

**overtrust**  *(also: automation complacency; over-reliance on an automated aid)*
*line 222 · failure mode*

> Overtrust is when the supervisor accepts AI output when they should not. The fluency trap from Chapter 1 is the canonical case: outputs that look right are accepted, and the verification work the supervisor was supposed to do is silently skipped. It is the least visible failure mode, because overtrust does not produce immediate flags.

In plain words: The supervisor accepts AI output they should not, so the checking they were meant to do is silently skipped; it is the least visible failure mode because it raises no immediate flags and the errors surface later, often found by the affected user. The chapter also calls it automation complacency and says the literature documents the mechanism as complacency and degraded monitoring under low signal rates.

Example: The fluency trap: outputs that look right are accepted.

Not to be confused with: undertrust

**working hypothesis, not a finding**
*line 224 · concept*

> What that literature does not establish is that overtrust is the most common failure across contemporary AI systems. So I hold that as a working hypothesis — a load-bearing one for how I design the audit trail — not a finding. If someone runs the prevalence study, I will update.

In plain words: The chapter labels "overtrust is the most common failure across contemporary AI systems" a working hypothesis, because the literature shows overtrust is a real failure but not that it is the most common. The author uses it to design the audit trail and says he will update if a prevalence study is run.

Example: Parasuraman and Riley (1997) and Lee and See (2004) document the mechanism of overtrust, not how common it is.

Not to be confused with: finding

**taxonomy of use, misuse, disuse, and abuse**
*line 224 · framework*

> Parasuraman and Riley's taxonomy of use, misuse, disuse, and abuse (Parasuraman & Riley, 1997) and Lee and See's work on designing for appropriate reliance (Lee & See, 2004) both document the mechanism: complacency, degraded monitoring under low signal rates.

In plain words: A taxonomy of how people use automated aids, from Parasuraman and Riley (1997), which the chapter cites as documenting the mechanism behind overtrust. The chapter does not explain the four categories one by one.

**the gap between having monitoring data and looking at it**  *(also: monitoring gap)*
*line 228 · failure mode*

> It should be reviewed periodically. It almost never is. That gap — between having the monitoring data and looking at it — is, in my reading, the field's most easily closable failure.

In plain words: Deployments often record monitoring data, such as Step 4's confirmed/corrected/unverifiable dispositions, but never review it. The chapter calls this the field's most easily closable failure.

Example: Reviewing the last fifty papers' Step 4 dispositions to see how often HIGH-confidence extractions needed correction.

Not to be confused with: map-to-audit-trail reconciliation (a separate, harder monitoring gap)

**granular, honest, time-stamped, and tied to evidence**  *(also: four properties of a supervisory log)*
*line 253 · framework*

> For the Disclosure to function as a supervisory log rather than a compliance checkbox, it has to be four things: granular (per step), honest (documenting corrections and gaps, not just smooth handoffs), time-stamped, and tied to evidence.

In plain words: The four properties that make an AI Use Disclosure a supervisory log instead of a compliance checkbox: granular (per step), honest (shows corrections and gaps), time-stamped, and tied to evidence.

Example: The Methods correction recorded at Step 3 is a documented correction, not a smooth handoff.

Not to be confused with: compliance checkbox

**AI Use Disclosure fields**  *(also: disclosure fields)*
*line 239 · framework*

> In its course form, the Disclosure asks the student to document what AI was used, on what step, with what verification. The format is structured.

In plain words: The Disclosure's structured entries for each step: step name, tool used (model, version and settings), input, output, verification done, and correction made. Vague entries such as "AI helped", "An LLM" or "Reviewed" count as missing.

Example: Step 3: tool GPT-4 API; verified 4 of 20 HIGH-confidence citations; Methods claim corrected where the AI dropped "on training data only".

**polished paragraph with no diff visible**
*line 260 · failure mode*

> A polished paragraph with no diff visible

In plain words: The failing version of the Disclosure's Output field: a smooth paragraph with no visible difference between what the AI produced and what was kept. The chapter wants the exact output received.

**the correction is not embarrassing**  *(also: correction as evidence)*
*line 264 · concept*

> The correction is not embarrassing. It is the data that proves the pipeline is working.

In plain words: A recorded correction shows the pipeline caught an error, so it counts as evidence the pipeline works, not a mark against the author. Honest Disclosures document corrections and gaps, not just smooth handoffs.

Example: The Methods correction at Step 3: the AI dropped the qualifier "on training data only" and the correction caught it.

**hierarchical mapping**
*line 274 · method*

> The response is hierarchical mapping. Map the system at the level of major components. For each component, map the sub-components that matter most for handoff and stakes.

In plain words: A way to map very large pipelines: map the major components, then only the sub-components that matter most for handoff and stakes, and describe routine parts by policy. The result is a layered document, denser at high-stakes interfaces and looser in routine processing.

Example: Multi-agent systems with thousands of steps cannot be mapped step by step.

**seams**
*line 278 · concept*

> It requires that the handoff conditions — the places where authority transitions between AI and human, where the audit trail crosses a boundary, where a decision is committed — are documented to a testable standard. Inside a component whose internal authority structure is settled, the documentation can be lighter. At the seams, it has to be tight.

In plain words: The places where authority passes between AI and human, where the audit trail crosses a boundary, or where a decision is committed. Documentation must be testable there and can be lighter inside a component whose authority structure is settled.

Example: A hundred-step pipeline: tight documentation at the high-stakes interfaces, policy-level notes for routine steps.

**reconciling the delegation map with the audit trail**
*line 296 · concept*

> The map specifies what should happen at each step. The audit trail records what did happen. Reconciling the two — automatically detecting deviations from the map in the trail — would close a major monitoring gap.

In plain words: The map says what should happen at each step and the audit trail records what did happen; checking one against the other automatically would catch deviations. The chapter lists this as unsolved in general, especially for multi-agent systems with thousands of steps.

Example: Exercise 12: design a monitoring protocol that detects deviations between the Paper Summarizer's map and its audit trail.

Not to be confused with: the gap between having monitoring data and looking at it

**lock your prediction**  *(also: prediction-vs-result gap)*
*line 309 · method*

> Lock your prediction: before constructing the delegation map, predict (a) how many steps will be Claude tasks, human tasks, and hybrids; (b) which step will have the most contested delegation; (c) which step's handoff condition will be hardest to make testable.

In plain words: Before building the map, write down predictions about the split into AI, human and hybrid steps, the most contested step, and the hardest handoff condition to make testable. The grade covers the honesty of the gap between prediction and result.

Example: Predicting, before mapping 8 to 20 steps, how many will be Claude tasks, human tasks and hybrids.

**override rate**  *(also: accept/override data)*
*line 340 · metric*

> A deployed medical-imaging pipeline has the following accept/override data from the last 200 cases: the AI's outputs were accepted 186 times and overridden 14 times.

In plain words: How often the supervisor overrides the AI's output instead of accepting it, taken from accept/override data. In Exercise 7 it is compared with the estimated AI error rate to tell which trust-calibration failure mode a deployment is in.

Example: Exercise 7: 14 overrides in 200 cases.

Not to be confused with: estimated AI error rate

**estimated AI error rate**  *(also: sampled ground-truth audit)*
*line 340 · metric*

> A sampled ground-truth audit of 40 randomly selected cases found 6 AI errors. Compute the supervisor's override rate and the estimated AI error rate.

In plain words: An estimate of how often the AI is actually wrong, taken from a sampled audit against ground truth rather than from the supervisor's overrides. Comparing it with the override rate shows whether reliance matches reliability.

Example: Exercise 7: 6 AI errors found in 40 randomly selected cases.

Not to be confused with: override rate

**delegation map as it is versus as it should be**  *(also: current delegation map; proposed delegation map)*
*line 374 · method*

> A delegation-map-as-it-is and a delegation-map-as-it-should-be for your agent — drawn directly from the failure cases collected in Chapter 8. Each case reveals a missing handoff condition; this chapter writes them.

In plain words: Two versions of the map for one agent: the deployment as it currently runs, and a rewritten version with new handoff conditions that would have caught the Chapter 8 failures. The chapter says each failure case reveals a missing handoff condition.

Example: The two output files delegation-map-current.md and delegation-map-proposed.md.

**case-derived handoff conditions**
*line 398 · method*

> For each Chapter 8 case, identify the specific HANDOFF CONDITION that, if it had existed and been enforced, would have caught the failure.

In plain words: Handoff conditions written backward from known failures: for each failure case, the specific testable condition that would have caught it if enforced. Each must be written so an evaluator can check whether it triggered correctly.

Example: If the agent is asked to delete data, it must list the specific items it will delete and require user confirmation before any deletion tool is called.

**deployment viability buckets**  *(also: viable; viable-with-conditions)*
*line 410 · framework*

> work split ASSESSMENT — Apply the five work split and sort the deployment into the chapter's buckets (viable / viable-with-conditions / fundamentally a work split).

In plain words: The three buckets the LLM exercise uses to rate a whole deployment: viable, viable with the proposed handoff conditions, or fundamentally unworkable. They are different from the three delegation buckets, which sort individual sub-tasks.

Example: Exercise output: interpret whether the agent's deployment is currently viable, viable with the proposed handoff conditions, or fundamentally unworkable.

Not to be confused with: delegation buckets (AI execution, human-only, hybrid)

## Chapter 10, Visualization Under Validation (89 terms) — NOT ON THE EXAM (Bear)

**dashboard as argument**  *(also: visualization is an argument; every dashboard is making an argument, by structure)*
*line 48 · concept*

> Visualization is not transparent communication of facts. It is an argument, made through structural choices, about what the facts mean and how the reader should weight them.

In plain words: A chart or dashboard never just hands over the facts; how it is laid out argues for what the facts mean and how much weight to give each, before anyone reads a number. So the person who builds it is always choosing which argument to make.

Example: A dashboard opening on one bold headline metric argues that the headline is enough; one opening on a panel of equally weighted views argues that the reader must integrate several numbers.

Not to be confused with: transparent communication of facts (the view the chapter rejects)

**two dashboards from one CSV**
*line 16 · named result or case*

> The first dashboard is misleading. The second is honest. And — here is the part you have to feel in your bones to understand the rest of this chapter — the deployment partner walks away from the two dashboards with two different beliefs about whether the system is safe.

In plain words: The chapter's opening case: one fixed validation result drawn as two dashboards, one that hides the problems and one that shows them. The deployment partner leaves the first reassured and the second with appropriate questions.

Example: The misleading one opens on '94% accuracy', squeezes the subgroup gaps onto truncated y-axes, grays the disparity charts and tucks the calibration curve into an 'advanced metrics' sub-tab.

**calibration curve**
*line 10 · concept*

> And the high-confidence outputs — the cases where the system is most certain — turn out, when you look at the calibration curve, to be overconfident at the top of the probability range.

In plain words: A plot used to check whether a system's stated confidence can be trusted; in the chapter's example it shows overconfidence at the top of the probability range. The chapter treats it as the finding that matters, so it belongs in the main view, not a sub-tab.

Example: The misleading dashboard hides it under 'advanced metrics'; the honest one shows it in the main view with a banner noting overconfidence at high probabilities.

**build-and-audit pairing**  *(also: pairing of the supervisory capacities; catch and fix your own misleading encoding)*
*line 26 · method*

> This chapter exercises a specific pairing of the supervisory capacities: you get the machine to build the chart, and then you audit what it built before it ships, catching the misleading encoding you or the tool reached for by default.

In plain words: Have the AI build the chart, then audit what it built yourself before it ships, asking what argument its structure makes and whether the data supports that argument. The AI does not remove the work; it relocates it to the audit.

Example: Chart your data with an AI, then catch and fix the misleading encoding (default axis, palette or aggregation) before it ships.

**validation failure at the output layer**  *(also: the visualization is part of the validation; the design choices are validation choices)*
*line 24 · concept*

> A dashboard that misrepresents valid findings is not a downstream problem. It is a validation failure at the output layer, and it is the supervisor's responsibility.

In plain words: If a dashboard misrepresents valid findings, that is not just a downstream communication problem; the validation has failed at its last step, the output. The supervisor is responsible for the chart as well as the analysis.

Example: A partner who sees '94% accuracy' and says 'we're ready to proceed', without hearing that calibration is overconfident above 0.85 and one subgroup is 12 points lower (exercise 8).

Not to be confused with: a communication failure downstream of valid analysis

**default chart choices**  *(also: default axis, default palette, default aggregation; your plotting library's default)*
*line 26 · failure mode*

> An AI will draw the chart. It will pick a default axis, a default palette, a default aggregation — instantly, competently, and without any stake in whether the result is honest.

In plain words: The axis range, palette and summary that an AI or plotting library picks when you do not choose. An AI picks them instantly and competently but with no stake in whether the result is honest, so you must review them.

Example: Reaching for the default chart Excel offers; Excel does not know what you are trying to say.

**deceptive visualization catalog**  *(also: nine-item catalog; nine misleading visualization choices; the catalog)*
*line 185 · framework*

> Here is the property that ties the whole list together: every one of these moves has an honest use, which is exactly why they are dangerous. The chart looks the same whether the choice was honest or not. The choice is the difference — not anything visible in the pixels.

In plain words: A named list of chart moves, each with an honest use and a dishonest use, used as a checklist to audit dashboards. The chart looks the same either way; the difference is whether the choice was honest.

Example: Truncating an axis can be honest when zero is not meaningful, as with stock prices.

**perception hierarchy**  *(also: Cleveland-McGill hierarchy)*
*line 101 · framework*

> The implication for picking charts: when the answer is quantitative and precision matters, encode it as position or length. Reach for area, angle, or color only when precision does not matter, or when no other channel fits.

In plain words: A ranking of how accurately readers decode a quantity from each visual channel, best to worst: position, length, angle and slope, area, volume, then color. When precision matters use position or length; the ordering is the durable result, while the exact error percentages are only approximate.

Example: Five nearly equal pie slices use angle, a weaker channel, for a question that demanded position.

**visual variable**  *(also: visual channel; perceptual channel)*
*line 88 · concept*

> Once you know the question and the chart family, you choose the visual variable — position, length, angle, area, color, volume — that encodes the answer. This is not a matter of taste. It is empirical.

In plain words: The visual property used to show a quantity in a chart: position, length, angle, area, color or volume. Which one you pick decides how accurately readers can read the number, and that is empirical, not a matter of taste.

Example: A dot plot sharing one x-axis encodes values by position; a pie chart encodes them by angle.

**FT question taxonomy**  *(also: FT Visual Vocabulary; nine question-families)*
*line 56 · framework*

> The Financial Times' Visual Vocabulary (Alan Smith and team) makes the connection concrete by sorting every chart type into nine question-families. (FT Visual Vocabulary, Financial Times Visual Journalism team; ft.com/vocabulary.) State the question, locate the family, pick from the charts within it.

In plain words: The Financial Times' way of sorting every chart type into nine question-families: deviation, correlation, ranking, distribution, change over time, part-to-whole, magnitude, spatial and flow. You state the question, locate its family and pick a chart from it.

Example: Showing that calibration error rises with predicted probability is a correlation question, so a scatterplot fits.

**aleatoric uncertainty**
*line 109 · concept*

> This is aleatoric uncertainty: the irreducible variability arising from sampling, natural variation, and stochastic processes. Error bars and confidence intervals are tools for it.

In plain words: Uncertainty from sampling, natural variation and chance that cannot be removed; the chapter calls it the 'spread of the data'. Error bars and confidence intervals are the tools for showing it.

Example: A poll of 45.3% versus 44.5% with a ±2.95% margin has aleatoric uncertainty larger than the effect being reported.

Not to be confused with: epistemic uncertainty

**epistemic uncertainty**
*line 111 · concept*

> Epistemic uncertainty is the gap between what you know and what is true — uncertainty that arises from the limits of your data, your instruments, your proxies. (Cairo, "Uncertainty and Graphicacy"; Bonneau et al., "Overview and State-of-the-Art of Uncertainty Visualization," 2014.) It is reducible in principle: better data, more sources, less biased instruments would close it.

In plain words: Uncertainty from the limits of your data, instruments or proxies: the gap between what you know and what is true, which better data could in principle close. Most charts hide it entirely.

Example: A kidnapping-rate chart built from news mentions has epistemic uncertainty that swamps the data entirely.

Not to be confused with: aleatoric uncertainty

**equal visual weight for uncertainty**  *(also: make the uncertainty visually equal in weight to the central estimate)*
*line 147 · method*

> Make the uncertainty visually equal in weight to the central estimate. A small error bar on a big bold number says: this is the answer, with a quibble. A central estimate displayed at the same visual weight as the uncertainty range says: the uncertainty is part of the finding.

In plain words: Show the uncertainty range with the same visual weight as the central estimate so the reader sees it as part of the finding, not a quibble. This matters most when the margin of error is large relative to the effect.

Example: A bold '94.3% accuracy' with a thin error bar versus '91–97% accuracy (95% CI)' drawn as a range at equal weight.

**living deck**  *(also: living-deck principle; living-deck format)*
*line 258 · method*

> A more honest form is the living deck — a presentation that exposes its own version history. Each version is dated. Each version has a changelog slide documenting what changed since the prior version and why.

In plain words: A presentation that exposes its own version history: each version is dated, has a changelog slide, and superseded slides are kept in a 'previously' section. It argues by form that the analysis is provisional and still changing.

Example: The course's research project uses it throughout, with the changelog as the second-to-last slide.

Not to be confused with: the polished single artifact

**the medium is the message**  *(also: a dashboard is a medium)*
*line 36 · concept*

> McLuhan's idea, in working form, was that the form of a communication shapes its meaning before any specific content arrives.

In plain words: The form in which something is communicated shapes its meaning before the reader gets to the content. A dashboard is a medium, so its structure shapes what a reader takes from the data before they read any number.

Example: A spoken, a written and a televised story differ because the medium structures the encounter, not because the words change.

**looking finished versus being honest**
*line 40 · concept*

> Usually that default is your plotting library's, which was optimized for looking finished, not for being honest. The two are not the same thing, and the gap between them is where most misleading dashboards live.

In plain words: A chart can look polished and complete without being faithful to the data, and plotting-library defaults are tuned for the first, not the second. Most misleading dashboards live in the gap between the two.

Example: The misleading opening dashboard was only 'a handful of choices away' from the honest one, about thirty seconds each.

**the question the chart is answering**  *(also: state the question in one sentence; the chart is a function of the question)*
*line 54 · method*

> A chart is not a way to display data. A chart is a way to answer one question with data. If you cannot state the question in a sentence, you do not yet know which chart to draw.

In plain words: Before choosing a chart, state in one sentence the question it answers, then find the data and chart type that fit that question. The question comes first; the chart is a function of it.

Example: 'How has model calibration changed across six months of deployment?' rather than 'chart the database.'

**deviation (question family)**
*line 62 · concept*

> Deviation — how far from a reference point (zero, a target, a baseline, a comparison group)? Bullet charts and diverging bars belong here. When you want to show that subgroup A performs 12 points below the overall average, this is the family.

In plain words: Questions about how far something is from a reference point: zero, a target, a baseline or a comparison group.

Example: Subgroup A performs 12 points below the overall average (bullet charts, diverging bars).

**correlation (question family)**
*line 64 · concept*

> Correlation — how does one variable move with another? Scatterplots. When you want to show that calibration error rises with predicted probability, this is the family.

In plain words: Questions about how one variable moves with another.

Example: Calibration error rises with predicted probability (scatterplot).

**ranking (question family)**
*line 66 · concept*

> Ranking — what is the order? Ordered bar charts, dot plots. When you want to show which features the model relies on most, this is the family.

In plain words: Questions about the order of the items.

Example: Which features the model relies on most (ordered bar charts, dot plots).

**distribution (question family)**
*line 68 · concept*

> Distribution — how often does each value occur? Histograms, box plots, violin plots, strip plots. When you want to show the spread of prediction confidence scores, this is the family.

In plain words: Questions about how often each value occurs.

Example: The spread of prediction confidence scores (histograms, box plots, violin plots, strip plots).

**change over time (question family)**
*line 70 · concept*

> Change over time — what is the trend? Line charts. When you want to show how accuracy has shifted over deployment months, this is the family.

In plain words: Questions about the trend.

Example: How accuracy has shifted over deployment months (line charts).

**part-to-whole (question family)**
*line 72 · concept*

> Part-to-whole — what proportion of the total? Stacked bars, treemaps. Use cautiously; pie charts belong here but rarely communicate as clearly as their popularity suggests.

In plain words: Questions about what proportion of a total each piece makes up.

Example: Stacked bars and treemaps; pie charts belong here but rarely communicate as clearly as their popularity suggests.

**magnitude (question family)**
*line 74 · concept*

> Magnitude — how big, in absolute terms? Bar charts with a zero baseline. When you want to show raw counts of model failures by category, this is the family.

In plain words: Questions about how big something is in absolute terms.

Example: Raw counts of model failures by category (bar chart with a zero baseline).

**spatial (question family)**
*line 76 · concept*

> Spatial — where? Maps. When the geography matters — when you need to show that failures cluster in specific deployment regions — this is the family.

In plain words: Questions about where something happens.

Example: Failures clustering in specific deployment regions (maps).

**flow (question family)**
*line 78 · concept*

> Flow — what moves from where to where? Sankov and alluvial diagrams. When you want to show how users reclassified by the new model compare to the old, this is the family.

In plain words: Questions about what moves from where to where.

Example: How users reclassified by the new model compare to the old (alluvial diagrams).

**box plot**
*line 131 · method*

> Use when comparing several distributions side by side and you care about median, spread, and outliers more than shape. Watch for: a box plot can hide bimodality. Two distributions with identical quartiles can look identical and behave nothing alike.

In plain words: A chart of median, spread and outliers for several distributions side by side, used when those matter more than shape. It can hide bimodality, so add a strip plot underneath if shape matters.

Example: Two distributions with identical quartiles can look identical and behave nothing alike.

**violin plot**
*line 133 · method*

> Use when distribution shape matters — multimodal data, skewed distributions, anything unusual. Shows the kernel density on each side of a spine.

In plain words: A plot showing the kernel density, the shape of the distribution, on each side of a spine; good for multimodal or skewed data. Non-experts may read it as a decorative vase, so annotate it or pair it with a box plot.

Example: Multimodal data, skewed distributions, anything unusual.

**strip plot**  *(also: jittered dot plot)*
*line 135 · method*

> Use when n is small enough to show every point. Position-based, perceptually honest — it sits at the top of the Cleveland-McGill hierarchy.

In plain words: A plot of every individual point, used when n is small enough to show them all; it is position-based and so perceptually honest. With large n it becomes an illegible smear, so add transparency or summary marks.

Example: Add mean or median marks on top when there are many points.

**Abela's decision tree**
*line 80 · framework*

> Andrew Abela's older decision tree (Choosing a Good Chart, 2009) collapses these into four — comparison, composition, distribution, relationship — and walks through binary choices. Either framework works. The point is the same: the chart is a function of the question.

In plain words: An older way to choose a chart that boils the question families down to four (comparison, composition, distribution, relationship) and walks through binary choices. Like the FT taxonomy, it picks the question first and lets the chart follow.

**starting from the data shape**
*line 82 · failure mode*

> The mistake to avoid: starting from the data shape ("I have a table with three columns and twelve rows") and reaching for the default chart Excel offers. Excel does not know what you are trying to say.

In plain words: Picking a chart because of what your table looks like instead of the question you need to answer, so you accept the software's default chart.

Example: 'I have a table with three columns and twelve rows', followed by reaching for the default chart Excel offers.

**position along a common scale**
*line 92 · concept*

> Position along a common scale — most accurate. A dot plot where every point shares an x-axis is using this channel.

In plain words: Showing values by where points sit along one shared axis; it is the most accurate way for readers to read a quantity.

Example: A dot plot where every point shares an x-axis.

**length**
*line 93 · concept*

> Length — nearly as good. Bars on a shared baseline use this channel. Reliable.

In plain words: Showing values by the length of bars that start from a shared baseline; nearly as accurate as position and reliable.

Example: Bars on a shared baseline.

**angle and slope**
*line 94 · concept*

> Angle and slope — worse. Pie slices encode quantity as angle. Radar chart arms encode quantity as slope.

In plain words: Showing values as the angle of a slice or the slope of an arm; both are harder to read precisely than bars.

Example: Pie slices (angle) and radar chart arms (slope).

**area**
*line 95 · concept*

> Area — considerably worse. Bubbles and treemap rectangles encode quantity as area. Useful when relative magnitude is all that matters; unreliable when the reader needs to compare closely.

In plain words: Showing values by the area of a shape; useful when only relative magnitude matters but unreliable when readers must compare closely.

Example: Bubbles and treemap rectangles.

**volume**
*line 96 · concept*

> Volume — even worse. Avoid.

In plain words: Showing values by three-dimensional volume, a very weak channel that the chapter says to avoid.

**color saturation and hue**
*line 97 · concept*

> Color saturation and hue — weakest for quantity; fine for category. Color is excellent for distinguishing groups, poor for encoding "how much."

In plain words: Using shade or kind of color to show a value; it is the weakest channel for how much, but fine for telling groups apart.

Example: Color to distinguish groups, not to encode 'how much'.

**error bars**
*line 125 · method*

> Error bars (point estimate ± standard deviation or confidence interval). Use when you are showing point estimates from samples, side by side, and the reader needs a quick visual check on overlap.

In plain words: A mark showing a point estimate plus or minus its spread, used to compare estimates from samples side by side and check for overlap. Readers often misread the bar as 'the true value is anywhere inside with equal probability', so the chart must say what the bar is.

Example: Label it every time: 'Error bar = 95% CI'.

**uncertainty exceeding effect size**  *(also: statistical tie; a story about noise; lie of composition)*
*line 223 · failure mode*

> Lesson: when uncertainty exceeds effect size, the chart is a story about noise. The honest story is "tie." Either visualize the confidence intervals so their overlap is obvious, or replace the chart with a sentence.

In plain words: When the margin of error is bigger than the difference being reported, the data cannot say which result is ahead, so the honest report is 'a tie', shown by overlapping intervals or a plain sentence. Two bars of different height would draw a difference that is not there.

Example: 45.3% no vs 44.5% yes with a ±2.95% margin: a 0.8-point difference inside a 2.95-point margin.

**FiveThirtyEight Nigeria kidnapping map (GDELT)**  *(also: the Nigeria chart; GDELT Nigeria case)*
*line 159 · named result or case*

> Cairo's clearest rule, drawn from a FiveThirtyEight map of Nigeria "kidnapping rates" that turned out to be a map of news stories about kidnappings. The database was GDELT — the Global Database of Events, Language, and Tone — which counts media mentions, not events. The spike correlated with Boko Haram media coverage, not kidnapping rates.

In plain words: A map titled as Nigerian kidnapping rates that was really built from GDELT, a database that counts media mentions, so its spike followed Boko Haram news coverage and the chart disclosed no proxy. It is the chapter's case for validating a proxy before charting it.

Example: A title naming the proxy honestly, 'News-story counts about kidnappings, 1985–2014', would have changed the reading.

**proxy**
*line 113 · concept*

> A bar chart of "kidnapping rates" built from a database of news mentions has epistemic uncertainty that swamps the data entirely — the proxy is not the thing it claims to measure.

In plain words: A stand-in measurement used because the real quantity is hard to count, such as counting news mentions of kidnappings instead of kidnappings. If the proxy does not carry the signal, the chart misleads however clean it looks.

Example: GDELT counts media mentions, not events, so the Nigeria 'kidnapping rates' map really showed news coverage.

Not to be confused with: the thing it claims to measure

**uncertainty from the visualization process**  *(also: a useful third source)*
*line 115 · concept*

> A useful third source: the visualization process itself introduces uncertainty. How you bin a histogram, where you start the y-axis, what you call "high" — these are choices, and choices are sources of distortion the reader cannot see unless you surface them.

In plain words: The chart-maker's own choices, such as how to bin a histogram, where to start the y-axis and what to call 'high', add distortion the reader cannot see unless it is surfaced. The chapter counts it as a third source of uncertainty.

Example: How you bin a histogram, where you start the y-axis, what you call 'high'.

**confidence interval bands**
*line 127 · method*

> Confidence interval bands (shaded area behind a line). Use when the trend is the message and uncertainty grows or shrinks across it — climate projections, fitted regressions, model drift estimates. Watch for: you have just encoded the most important number — the amount of uncertainty — in color saturation, one of the weakest perceptual channels.

In plain words: A shaded area behind a trend line showing how uncertain the estimate is along the line; good when the trend is the message and the uncertainty grows or shrinks across it. Its width, the most important number, is encoded in color saturation, so label key points.

Example: Climate projections, fitted regressions and model drift estimates.

**fan charts**
*line 129 · method*

> Fan charts (forecast widening into the future). Use when projecting forward and the uncertainty grows with the horizon. Standard in central-bank inflation forecasts, hurricane forecasts, economic outlook reports.

In plain words: A forecast chart whose band widens into the future, used when uncertainty grows with the horizon.

Example: Central-bank inflation forecasts and hurricane forecasts.

**cone of uncertainty**
*line 129 · named result or case*

> the "cone of uncertainty" in hurricane forecasts contains roughly 66% of past forecast track errors, not 95% — the cone is a two-thirds likelihood region sized from the prior five years of forecast errors, which is confirmed against the National Hurricane Center's methodology. The public frequently reads the cone as the physical size of the storm, or as a hard wall outside which it is "safe." Neither is what it means.

In plain words: The shape drawn on hurricane forecasts; it holds roughly 66% of past forecast track errors, not 95%, and is sized from the prior five years of forecast errors. The public often reads it as the storm's physical size or a wall beyond which it is safe.

Example: The fix is explicit text plus alternative encodings, such as gradient lines showing many possible paths.

Not to be confused with: the physical size of the storm

**quantile dotplot**
*line 137 · method*

> This is the technique most guides skip, and it is one of the most effective for communicating uncertainty to lay audiences. Twenty dots, of which four are filled, beats "20% chance" every time.

In plain words: A chart that shows a probability as a set of dots, for example twenty dots with four filled, so readers count outcomes instead of reading a percentage. It uses position, the best channel, and the chapter ranks it above confidence bands for lay audiences.

Example: Twenty dots, of which four are filled, beats '20% chance'.

**natural frequencies**
*line 137 · concept*

> The underlying principle comes from Gerd Gigerenzer's work on natural frequencies: "9 out of 10 women with breast cancer test positive; 99 out of 1,000 women without breast cancer also test positive" produces correct reasoning where "90% sensitivity, 9.9% false-positive rate" does not — even among physicians who should know better.

In plain words: Stating a risk as counts of people, such as 9 out of 10 or 99 out of 1,000, instead of percentages like sensitivity and false-positive rate. The research the chapter cites finds that counts produce correct reasoning where percentages do not, even among physicians.

Example: '9 out of 10 women with breast cancer test positive; 99 out of 1,000 women without breast cancer also test positive.'

Not to be confused with: percentages such as '90% sensitivity, 9.9% false-positive rate'

**hypothetical outcome plots (HOPs)**  *(also: HOPs)*
*line 139 · method*

> Animated frames, each showing one plausible draw from the distribution. Lets the reader feel the variability across frames rather than inferring it from a static shape. Watch for: static publication — they do not work on paper.

In plain words: An animation in which each frame shows one plausible draw from the distribution, so viewers feel the variability instead of inferring it from a static shape. It works in interactive dashboards but not on paper.

**gradient line plots**
*line 141 · method*

> Gradient line plots (many paths, opacity scaled by likelihood). Show that the future is many futures, weighted by probability.

In plain words: A plot of many possible paths with opacity scaled by likelihood, showing that the future is many futures weighted by probability. Test it with real audiences first, because it can backfire.

Example: Hurricane graphics that overlay possible storm sizes on possible paths.

**backfire effect**
*line 141 · failure mode*

> Cairo's warning that overlaying possible storm sizes on possible paths in hurricane graphics produced a backfire effect, with some viewers concluding that scientists "knew nothing." More information made trust worse. Test with actual audiences before deploying.

In plain words: When showing more uncertainty detail makes viewers trust the experts less instead of understanding more. In the hurricane example some viewers concluded that scientists 'knew nothing'.

Example: Overlaying possible storm sizes on possible paths in hurricane graphics.

**quantile dotplot with natural-frequency narration**  *(also: natural-frequency narration)*
*line 143 · method*

> A useful default for most real situations: the quantile dotplot with a sentence of natural-frequency narration underneath is the strongest combination available for communicating uncertainty to mixed or lay audiences. Position channel for perception, counts for cognition, narration for the reader who skims.

In plain words: Pair a quantile dotplot with one sentence of natural-frequency narration underneath: position serves perception, counts serve cognition and the sentence serves the reader who skims. The chapter calls it the strongest combination for mixed or lay audiences.

Example: Twenty dots with four filled, plus a natural-frequency sentence beneath.

**false precision**
*line 149 · failure mode*

> A reported metric of 0.847291 with a confidence interval of ±0.05 is not a 0.847291 metric. It is a 0.85 metric. Round the central estimate to a precision the uncertainty actually supports.

In plain words: Reporting more decimal places than the uncertainty supports, which implies certainty that does not exist. Round the central estimate to the precision the uncertainty allows.

Example: 0.847291 with a confidence interval of ±0.05 is really a 0.85 metric.

**test on a non-author reader**  *(also: hostile read; test the chart against a hostile read)*
*line 151 · method*

> Show the chart to someone who did not produce it. Ask them what they think it says. If their interpretation does not match the data, the visualization is not yet doing its job, no matter how much you like the design.

In plain words: Show your chart to someone who did not make it and ask what they think it says; if their reading does not match the data, the chart is not yet doing its job. The chapter calls this the single most useful item on its list and says it is almost always skipped because it is uncomfortable.

Example: Step 7 of the working sequence: give the chart to someone who did not produce it.

**validate before you visualize**  *(also: check the data against the question)*
*line 161 · method*

> The lesson: a chart based on a proxy you have never examined will mislead with the full visual authority of a chart based on truth. You have to check first whether the proxy carries the signal at all.

In plain words: Check that your data actually measures what the question asks before you chart it, because a chart on an unexamined proxy misleads with the authority of a chart on truth. If it measures a proxy, change the dataset, change the question or disclose the proxy.

Example: The Nigeria 'kidnapping rates' map turned out to be a map of news stories.

**visual authority of a chart**
*line 159 · concept*

> The chart conveyed the full visual authority of a chart built from ground truth, because it looked like all other charts, because charts do not carry labels that say "this proxy may not measure what the question asks."

In plain words: Every chart looks equally authoritative whether it rests on ground truth or on an unexamined proxy, because charts carry no label saying what they may not measure. So a weak chart gets the same trust as a strong one.

Example: The Nigeria map looked like every other chart, so it carried the authority of a chart built from ground truth.

**disclose the source, inside the chart**
*line 163 · method*

> Treat the source line as part of the chart, not as footer decoration. Move it inside the chart frame. Make it specific: dataset name, year, URL or identifier.

In plain words: Put a specific source line inside the chart frame, naming dataset, year and URL or identifier, not just 'World Bank data'. In the chapter's formula the title is the question, the subtitle is the answer and the source line is the warrant.

Example: 'World Bank Development Indicators, GDP per capita, 2023, data.worldbank.org/indicator/NY.GDP.PCAP.CD' is a source; 'World Bank data' is not.

**disclose the methodology choices**
*line 165 · method*

> A short methods note adjacent to the chart — three sentences, not a paper — separates a chart that survives a hostile read from one that does not.

In plain words: Add a three-sentence methods note beside the chart saying whether you binned, smoothed, excluded or normalized, because those choices change the picture. It separates a chart that survives a hostile read from one that does not.

**disclose what the data does not measure**
*line 167 · method*

> The Nigeria chart was titled as a chart of kidnappings. It was a chart of news stories about kidnappings. The reader had no way to see the gap.

In plain words: When the data is a proxy, say in the title what it really counts, so the gap between the question and the data is visible. The honest title is less compelling but more true.

Example: 'News-story counts about kidnappings, 1985–2014' instead of 'kidnappings'.

**when uncertainty is too large, do not visualize**  *(also: sometimes the right chart is no chart)*
*line 169 · method*

> A bar chart showing two bars, one a hair taller than the other, is a lie of composition — the visual encodes a difference that is not there. The honest move is text, or a chart that makes the confidence interval visually larger than the effect. Sometimes the right chart is no chart.

In plain words: When the margin of error swamps the effect, two bars would show a difference that is not there, so use a sentence, or a chart that makes the interval larger than the effect. Sometimes the right chart is no chart.

Example: 45.3% no vs 44.5% yes with a ±2.95% margin: say 'it's a tie'.

**El País Catalonia poll, 2014**
*line 221 · named result or case*

> This case is meant to illustrate uncertainty exceeding effect size: a poll reporting 45.3% "no" versus 44.5% "yes" with a ±2.95% margin — a 0.8-point difference inside a 2.95-point margin, which is a statistical tie — rendered as two bars of visibly different height, a lie of composition. I am keeping it in the text only with a warning attached, because I could not find the primary source: the actual El País graphic and its date.

In plain words: A poll reported as 45.3% no versus 44.5% yes with a ±2.95% margin, a statistical tie, said to be drawn as two bars of different height. The chapter could not find the original graphic, so it keeps this only as an illustrative construction of uncertainty larger than the effect.

Example: A 0.8-point difference inside a 2.95-point margin.

Not to be confused with: a truncated axis amplifying a '5-point lead' (the other, incompatible account the chapter mentions)

**hierarchy of disclosure**  *(also: hierarchy of uncertainty disclosure)*
*line 177 · framework*

> Hierarchy is not hiding. The test is whether a hostile reader could arrive at a different conclusion by knowing the uncertainty. If yes, the uncertainty belongs prominently in the chart.

In plain words: How prominently an uncertainty is shown depends on whether it could change the reader's conclusion: in the chart if it could, in a visible caption or footnote if a serious reader needs it, in a methodology appendix if it is small and the conclusion is robust. Ranking by importance is not concealment; the test is a hostile reader.

Example: The Catalonia poll goes prominently in the chart; a 60% vs 30% finding with a ±3% margin goes in a caption.

Not to be confused with: hiding (concealment)

**truncated axes**  *(also: truncated axis; truncated y-axes)*
*line 189 · failure mode*

> A bar chart with the y-axis starting at 80 instead of 0 makes a small difference look large. Legitimate uses: when the relevant range really is narrow, when zero is not meaningful for the quantity being displayed (stock prices are routinely shown on truncated axes for good reason). Illegitimate uses: when the visual amplification implies a larger effect than the data supports.

In plain words: Starting an axis above zero so a small difference looks large. It is honest only when the relevant range is narrow or zero is not meaningful; it misleads when the amplification implies a bigger effect than the data supports.

Example: A y-axis running 91% to 96% makes 94.3% look about three times as tall as 92.1% (exercise 1).

Not to be confused with: axis inversion (truncation amplifies a real effect; inversion reverses one)

**inconsistent axes across panels**
*line 191 · failure mode*

> Two charts side by side look comparable. They are not — because their y-axis ranges differ and the reader's visual comparison is invalid. This is one of the most common mistakes in dashboards built without intent to deceive: the engineer did not ask whether the visual comparison their layout was inviting was a valid one.

In plain words: Placing charts side by side with different axis ranges, so the reader's visual comparison is invalid even though the charts look comparable. It is common in dashboards built with no intent to deceive.

Example: Subgroup accuracy charts with y-axes of 70–100%, 85–100% and 60–100% look 'about the same' (exercise 3).

**aggregation that hides distribution**  *(also: aggregation hiding distribution)*
*line 193 · failure mode*

> A single number — a mean, a median — that conceals a heavy-tailed or multimodal distribution. "Median performance is good" communicates the median and hides the tail. If the tail contains the catastrophic cases, hiding it is not summarization; it is concealment.

In plain words: Reporting one number, such as a mean or median, that hides a heavy-tailed or multimodal distribution. If the tail holds the catastrophic cases, hiding it is concealment, not summarization.

Example: Median latency as the headline while about 3% of requests take up to 8 seconds (exercise 2).

**color asymmetry**  *(also: color-as-judgment)*
*line 195 · failure mode*

> Categorical data displayed with colors of unequal salience guides the eye toward where the designer wants attention and away from where they do not. The data has not changed. The salience has.

In plain words: Using colors of unequal salience so the eye is pulled where the designer wants and away from where they do not, even though the data has not changed.

Example: The misleading opening dashboard used green for 'good' and gray for 'needs attention', and the disparity charts were gray.

**cherry-picked time windows**
*line 197 · failure mode*

> A trend chart over a window that begins at a local minimum and ends at a local maximum exaggerates the trend. The same data over a longer window may show a different story, or no story at all.

In plain words: Choosing a trend window that starts at a local low and ends at a local high so the trend looks exaggerated; a longer window may show a different story or none. The living deck's changelog records when the window changed and why.

Example: A chart starting in April shows only recovery after a March retraining that followed a performance drop (exercise 9).

**scale trickery**
*line 199 · failure mode*

> Linear axes for data that is naturally logarithmic; log axes for data that is naturally linear. Each compresses or expands different regions of the data. The choice can serve clarity or its opposite.

In plain words: Using a linear axis for data that is naturally logarithmic, or a log axis for naturally linear data, which compresses or expands different regions of the data. The choice can serve clarity or its opposite.

Example: Accuracy values from 0.001% to 78% over six months drawn on a linear axis (exercise 4).

**chartjunk and 3D effects**  *(also: chartjunk; 3D effects)*
*line 201 · failure mode*

> Often introduced for aesthetic reasons; their effect is often to obscure. Tufte's term "chartjunk" names the category: any element of the display that does not transmit information about the data.

In plain words: Decoration that carries no information about the data and can distort how big the numbers look. Tufte's word 'chartjunk' names any display element that does not transmit information about the data.

Example: 3D bar charts whose foreshortening makes near bars look bigger than far ones, and pie charts with exploded slices.

**missing baselines**  *(also: missing baseline)*
*line 203 · failure mode*

> A chart showing a metric without showing the comparison metric — accuracy without random-baseline accuracy, performance without prior-system performance, a finding without the null. The reader cannot tell whether the finding is large or small. Without the baseline, everything looks like a finding.

In plain words: Showing a metric without the comparison that gives it meaning, such as accuracy without random-baseline accuracy, so the reader cannot tell whether the finding is large or small. Without the baseline, everything looks like a finding.

Example: Snow's map succeeded because it showed all the pumps, not just the Broad Street pump.

**labels that prejudge**
*line 205 · failure mode*

> Axis labels, legend entries, and headlines that frame the interpretation before the reader sees the data. "Accuracy boost from new model" on a chart comparing two models is a label that prejudges. "Accuracy: model A vs model B" is a label that does not.

In plain words: Axis labels, legend entries or headlines that frame the interpretation before the reader sees the data. Labels should name the variables and let the data make the argument.

Example: 'Accuracy boost from new model' prejudges; 'Accuracy: model A vs model B' does not.

**selective uncertainty visualization**
*line 207 · failure mode*

> Showing confidence intervals where they support the argument and omitting them where they would weaken it. Common, hard to detect, structurally the most dishonest of the bunch — because the data on uncertainty exists, and the choice to display it selectively is precisely the rhetorical move the engineer is making while telling themselves they are merely "presenting the data."

In plain words: Showing confidence intervals where they support the argument and leaving them off where they would weaken it. The chapter calls it structurally the most dishonest item because the uncertainty data exists and the display is chosen.

**changelog slide**  *(also: changelog)*
*line 266 · method*

> The final presentation includes the changelog as the second-to-last slide. The changelog is evidence of the work — the visible track of how the analysis evolved. Removing it before final submission would erase the supervisory log.

In plain words: A slide in a living deck recording what changed since the prior version and why; it is the visible track of how the analysis evolved. A deck without it is pretending to be finished.

Example: It sits as the second-to-last slide of the final presentation.

**Snow's cholera map, 1854 (counter-case)**  *(also: counter-case)*
*line 229 · named result or case*

> The reason this case is famous is that the map did three things simultaneously: showed spatial clustering of deaths, marked the Broad Street pump as the spatial center, and included all other pumps for comparison. The third move is what made it evidence rather than illustration. Snow let the reader rule out alternative explanations by making the comparisons visible inside the chart.

In plain words: An 1854 map of cholera deaths that showed the cluster around the Broad Street pump and also drew all the other pumps, so readers could rule out other explanations. The chapter treats it as the success case, and as a compelling argument for a hypothesis rather than the instrument of discovery.

Example: It showed all the pumps for comparison, not just the Broad Street pump.

**Challenger, January 1986**
*line 217 · named result or case*

> Engineers had thirteen charts showing O-ring erosion data the night before launch. The data contained a pattern — erosion was worse at lower launch temperatures — but it was not displayed in a way that made the pattern visible. Charts mixed qualitative text with quantitative displays, did not show the temperature-erosion relationship in a single visualization, and emphasized reassuring findings without presenting the overall risk profile.

In plain words: The night before the 1986 launch, engineers had thirteen charts of O-ring erosion but none showed the temperature-erosion relationship in one picture, and management approved the launch. The chapter, following Tufte, reads it as evidence that existed while the visualization failed to make it visible to a decision-maker under pressure.

Example: The chart for cold temperature → harder rubber → longer seating time → blow-by → failure was never drawn.

Not to be confused with: omission of the untested cold-temperature region (the other diagnosis the chapter mentions)

**Reuters Florida Stand Your Ground chart, 2014**
*line 225 · named result or case*

> A line chart showed firearm-related murders in Florida from 1990 to 2012, with the state's 2005 Stand Your Ground law marked as the inflection point. At first glance the chart appeared to show murders rising through the 1990s, leveling off, and then dropping precipitously after 2005 — apparently strong visual evidence that the law worked as advertised. The y-axis was inverted.

In plain words: A 2014 Reuters line chart of Florida firearm murders whose y-axis was inverted, so the rise after the 2005 Stand Your Ground law looked like a decline. It is the chapter's canonical case of axis inversion.

Example: Deaths rose from 521 in 2005 to 740 in 2006 to 825 in 2007, yet the line appeared to fall.

**axis inversion**  *(also: axis-flip deception; inverted y-axis)*
*line 227 · failure mode*

> Lesson: the orientation of the axis is itself a structural argument about which direction is "good." When the axis runs against convention, the chart can communicate the inverse of the data while remaining technically accurate. Honest practice: zero at the bottom for quantities where larger values mean more, with the direction-of-better stated explicitly in the title or caption.

In plain words: Drawing the axis upside down so the data stays accurate but the reader takes away the opposite of what it shows; it reverses a real effect where truncation amplifies one. Honest practice is zero at the bottom for 'more is more' quantities, with the direction of better stated.

Example: On the Reuters chart with zero at the top, firearm murders rose from 521 in 2005 to 740 in 2006 to 825 in 2007 but looked like a decline.

Not to be confused with: truncated axes / scale trickery

**evidence-grade visualization**  *(also: evidence rather than illustration)*
*line 231 · concept*

> Lesson: evidence-grade visualization shows what would have to be true for the conclusion to be wrong, not just what supports the conclusion.

In plain words: A chart that lets the reader test the conclusion by showing what would have to be true for it to be wrong, not only the points that support it.

Example: Snow's map included all the other pumps so the reader could rule out alternative explanations.

**the trade-off: misleading charts are faster and more persuasive**  *(also: faster to build and more persuasive on first contact)*
*line 246 · concept*

> A misleading chart is faster to build than an honest one, and it is more persuasive on first contact. That is the deal on offer.

In plain words: A misleading chart is faster to build and more persuasive on first contact than an honest one; optimizing for looking finished and reassuring spends the reader's ability to reach a different conclusion. That fails badly the moment a decision-maker needs to see the region of doubt.

Example: The Challenger decision.

**normative choices (there is no neutral)**  *(also: the choices are normative; there is no neutral)*
*line 358 · concept*

> The choices that compose the argument are normative — they reflect a stance about what matters and how the reader should weight things. The engineer who treats those choices as neutral is mistaken about what they are doing.

In plain words: Every chart-design choice reflects a stance about what matters and how the reader should weight things, so there is no neutral default. An engineer who treats the choices as neutral is mistaken about what they are doing.

Example: Truncate here, gray there, bury the calibration curve in a tab: each choice took about thirty seconds and shifted the argument.

**finished-looking form**  *(also: polished single artifact; finished-looking artifact)*
*line 256 · failure mode*

> Validation analyses are usually presented as if they were finished. The dashboard, the deck, the report — they look polished, single-version, authoritative. This finished-looking form is itself a structural argument: the analysis is complete; what you are reading is the answer.

In plain words: Presenting an analysis as a polished, single-version document says by its form that the work is complete and the reader has the final answer, although most analyses are still in progress. That misrepresents the analysis and makes it harder to revise.

Example: Some adoption committees and procurement processes prefer the polished single artifact that hides the work.

Not to be confused with: living deck

**working sequence for picking and showing**  *(also: seven-step working sequence)*
*line 297 · method*

> This is the sequence, not a checklist. The decision forks at steps 3 and 7 are where most published charts quietly fail.

In plain words: A seven-step order for making a chart: state the question, locate its family, check the data fits the question, identify the aleatoric uncertainty, identify the epistemic uncertainty, choose encodings by the perception hierarchy, then test against a hostile read. The forks at steps 3 and 7 are where most published charts quietly fail.

Example: Step 1: not 'chart the database' but 'How has model calibration changed across six months of deployment?'

**Glimmer 10.1 (build the honest and the misleading version)**
*line 322 · method*

> Building a misleading dashboard with intent is the most efficient way to learn what your default dashboards have been doing without intent. After you've done this once, you do not see dashboards the same way. You see the choices.

In plain words: An exercise where you build an honest dashboard and then a deliberately misleading one from the same data, side by side, and document which design choices did the misleading work; the grade is on the reflection. Doing it once changes how you see your own default dashboards.

Example: Truncate axes, pick favorable color salience, hide the calibration in a sub-tab, make the central estimate bold and the error bars thin.

**prediction lock**  *(also: prediction-locking)*
*line 314 · method*

> Lock your prediction before building the misleading version: (a) which design choices will you make to mislead? (b) which will be hardest, because the data refuses to be obscured? (c) which choices do you suspect you have already made unintentionally in earlier dashboards?

In plain words: Writing down your predictions before you build, so you can compare them with what happens. Here you predict which choices you will use to mislead, which will be hardest because the data resists, and which you may already have made by accident.

Example: Lock the prediction before building the misleading version.

**what would change my mind**
*line 348 · concept*

> If a visualization standard emerged with strong empirical evidence that readers' interpretations matched the data — across diverse readers, audiences, and finding types — without bespoke-design work, the "every dashboard is an argument" framing would weaken to "most dashboards are arguments unless they conform to the standard." As of this writing, no such standard exists.

In plain words: The chapter's statement of what evidence would weaken its claim: a visualization standard shown to make readers' interpretations match the data across diverse readers and finding types without bespoke design work. No such standard exists yet.

Example: Domain-specific guidelines such as FDA guidance for clinical trial visualizations are partial and not generalizable.

**detecting deceptive design choices**  *(also: the general detection problem)*
*line 352 · concept*

> I do not have a clean way to automatically detect deceptive design choices in a dashboard the way accessibility tools detect contrast issues. Some patterns — truncated axes, inconsistent scales — are mechanical and could be flagged by tooling. Others — color asymmetry, label prejudgment, selective uncertainty, cherry-picked time windows — require contextual judgment about whether the choice is honest.

In plain words: Some deceptive choices (truncated axes, inconsistent scales) are mechanical enough for tooling to flag, but others (color asymmetry, label prejudgment, selective uncertainty, cherry-picked windows) need judgment about whether the choice is honest. So general automatic detection is an open problem.

Example: Accessibility tools can detect contrast issues automatically; nothing equivalent exists for deceptive choices.

**dual-axis trick**  *(also: dual-axis tricks)*
*line 472 · failure mode*

> Dual-axis trick: failure count on one axis, "successful interactions" on the other, scaled so the failures look minor

In plain words: Plotting two measures on separate axes and scaling them so one looks small beside the other.

Example: Failure count on one axis and 'successful interactions' on the other, scaled so the failures look minor.

**Wilson or bootstrap confidence interval**
*line 459 · method*

> Aleatoric uncertainty around each rate shown via confidence intervals (use Wilson or bootstrap CI for small N)

In plain words: Two ways of putting a confidence interval around a rate when only a few cases were tested, so the chart shows its aleatoric uncertainty. The chapter's prompt says to use them for small N.

Example: Confidence intervals around each failure rate on the honest dashboard.

**what we cannot say panel**
*line 460 · method*

> Epistemic uncertainty (sources of structural unknown — opacity of training data, untested deployment contexts) shown via a "what we cannot say" panel

In plain words: A panel on the honest dashboard that lists the structural unknowns behind the numbers, so the epistemic uncertainty is shown instead of hidden.

Example: Opacity of training data and untested deployment contexts.

**provisionality note**
*line 481 · method*

> add a provisionality note to Dashboard A. Some of the casebook's findings are still under collection; some prediction-locks are still open. Show what is settled and what is provisional.

In plain words: A note on the honest dashboard showing which findings are settled and which are still being collected, so the dashboard does not pretend to be finished. The chapter calls this the living-deck move.

Example: Some findings are still under collection and some prediction-locks are still open.

Not to be confused with: living deck

## Chapter 11, Communicating Uncertainty (90 terms) — communicating sections NOT ON THE EXAM (Bear)

**verb calibration**  *(also: calibration of the verb of a claim to the evidence; verb-evidence calibration; the verb is doing epistemic work)*
*line 17 · concept*

> It is mostly inattention to a particular kind of calibration — the calibration of the verb of a claim to the evidence the claim is built on. The verb is doing real epistemic work, and most engineering writers do not notice the verb at all.

In plain words: Matching the strength of the verb in a claim (conclude, find, observe and so on) to the amount of evidence the claim actually rests on. The chapter says the verb is doing real work in the claim, so choosing it is part of making the claim and not just grammar.

Example: The same 87% accuracy result on one held-out test set supports "we observe" but not "we conclude".

Not to be confused with: calibration of a model's probabilities (the chapter uses the word for both)

**same finding, three verbs**  *(also: sentences A, B and C)*
*line 15 · named result or case*

> The numbers never changed. What changed was the verb — conclude, find, observe — and each verb claims a different amount of evidence. The evidence supports sentence C.

In plain words: The chapter's opening demonstration: one result (87% accuracy on a single held-out test set, with no significance test and no confidence interval) written with three different verbs. Only "observe" is fully supported, "find" is partly compatible, and "conclude" is not supported.

Example: Sentence A "We conclude that the new model is more accurate" versus sentence C "We observe that the new model produces 87% accuracy on this single held-out evaluation".

**overclaiming**  *(also: over-claim; over-claiming; conclusions stated more strongly than the evidence permits)*
*line 17 · failure mode*

> But it is a claim. Engineering papers are full of conclusions stated more strongly than the evidence permits.

In plain words: Writing a claim with a stronger verb than the evidence supports, for example "conclude" when the evidence only warrants "observe". The chapter says engineers do this without noticing because the verb feels like grammar, and that it is mostly inattention rather than malice.

Example: "We conclude that the new model is more accurate" resting on one accuracy number from one test set.

**downgrading verbs in AI output**  *(also: verb downgrade; downgrading the verb)*
*line 371 · method*

> If the answer is no, the AI's verb is unwarranted. The supervisor's move is to replace conclusively demonstrates with suggests or observes, and to explicitly note that the stronger reading is not yet warranted.

In plain words: Checking an AI-written claim by asking what evidence its verb requires, and if that evidence was not produced, replacing the verb with a weaker one and saying the stronger reading is not yet warranted. The chapter calls it one of the highest-leverage editing moves, because the underlying factual claim usually stays the same and only the posture changes.

Example: Replace "conclusively demonstrates" with "suggests" or "observes" in an AI-written paragraph.

**build and audit**  *(also: two hands; build/audit pairing)*
*line 19 · framework*

> And it runs in two directions that turn out to be the same skill: build — calibrate the verbs in a report you write, mapping every claim to its proof — and audit — downgrade the verbs in an AI-written claim that someone hands you. Same instrument, two hands.

In plain words: Using one verb-calibration skill in two ways: build means calibrating the verbs in a report you write, mapping every claim to its proof, and audit means downgrading the verbs in an AI-written claim someone hands you. The chapter calls the pairing one of the supervisory capacities the book keeps returning to.

Example: Build: revising your own validation paragraph so each verb matches its evidence. Audit: replacing "conclusively demonstrates" in an AI paragraph.

**communicating validation findings**  *(also: supervisory capacity)*
*line 429 · framework*

> Together the two chapters are the supervisory capacity for communicating validation findings, which is, structurally, where validation work meets its readers.

In plain words: The supervisory capacity built by this chapter and the one before it: getting a validation result to its readers without claiming more than the evidence gave. The previous chapter fights the misleading chart (truncated axis, tilted color) and this one fights the misleading verb.

Example: Chapter 10 fights a truncated axis; Chapter 11 fights a verb that quietly claims more than the evidence.

**verb taxonomy**  *(also: verb ladder; frozen ladder; working hierarchy)*
*line 41 · framework*

> I am being deliberate about freezing exactly one ordering, because a verb ladder that contradicts itself is worse than none — it hands you false confidence that you calibrated. So: observe is weaker than find (a single observation under specific conditions is weaker than a result established across variation); suggest sits below observe (an inference the data is merely consistent with); prove is reserved for mathematics or formal verification.

In plain words: A fixed ordering of eight claim verbs from weakest to strongest (hypothesize, suggest, observe, find, show, demonstrate, conclude, prove), each needing more evidence than the one before. You pick the verb whose evidence requirement your evidence actually meets.

Example: "We observe ECE = 0.04 on the global test set" (observe) versus "We conclude the deployment cannot ship without subgroup-specific recalibration" (conclude, which needs full analysis).

**fluency trap**  *(also: fluency-trap detector; treat the verb itself as a flag)*
*line 373 · failure mode*

> Think of this as the verb taxonomy operating as a fluency-trap detector. AI outputs reach for strong verbs because the language models behind them were trained on text that frequently uses strong verbs, often when not warranted. The supervisor reading AI output should treat the verb itself as a flag.

In plain words: The danger that AI-written text sounds smooth and confident, so strong verbs such as "conclusively demonstrates" get accepted as if they were evidence. The chapter's defence is to treat each strong verb as a flag and ask what evidentiary base stands behind it.

Example: Downgrading "conclude" to "suggest" can change a decision (ship versus ask for another study); the chapter says the fluency trap was about to cost you that decision and the verb caught it.

**fluency**  *(also: the fluency and the over-claim arrive together, welded)*
*line 375 · concept*

> AI reaches for strong verbs because it was trained on strong-verb text, so the fluency and the over-claim arrive together, welded. Most AI-generated paragraphs are improved by one or two verb downgrades, and the resulting paragraph reads more like the work of a careful engineer than the work of an enthusiastic press release.

In plain words: The smooth, confident sound of AI-written prose. The chapter says it comes welded to over-claiming, because the model learned from strong-verb text, so the polished wording and the unearned strength have to be fixed together, usually by one or two verb downgrades.

Example: An AI paragraph that reads like an enthusiastic press release and is improved by one or two verb downgrades into the work of a careful engineer.

Not to be confused with: fluency trap (the trap is accepting fluent over-claiming as evidence)

**layered writing**  *(also: three audience layers; layered document; two readers, one document)*
*line 92 · method*

> A working alternative is layered writing. The technical and non-technical content live in the same document, layered so that each reader can find their level without translation.

In plain words: Putting technical and non-technical content in one document, arranged in layers so each reader finds their level without a separate translation. The chapter prefers it to two documents because two documents drift and every translation can lose the nuance the calibration was protecting.

Example: One validation report with a Layer 1 plain-English summary, Layer 2 technical detail and Layer 3 reproducibility appendix.

Not to be confused with: two-document approach

**epistemic uncertainty**
*line 330 · concept*

> Epistemic uncertainty is uncertainty in your knowledge — it could be reduced with more evidence.

In plain words: Uncertainty that comes from not knowing enough, so more evidence would shrink it. The chapter also uses the word epistemic for the stance a verb takes toward its evidence (epistemic posture), which is a different use.

Example: A model's uncertainty about a rare demographic subgroup it has never seen: more data would reduce it.

Not to be confused with: aleatoric uncertainty

**aleatoric uncertainty**  *(also: irreducible uncertainty)*
*line 330 · concept*

> Aleatoric uncertainty is uncertainty in the system itself — it is irreducible.

In plain words: Uncertainty that comes from the system itself being noisy, so no amount of extra data removes it. Mixing it up with epistemic uncertainty produces hedges that read as timid or evasive.

Example: A model's uncertainty about individual outcomes in a genuinely noisy system: more data will not help.

Not to be confused with: epistemic uncertainty

**calibration**  *(also: calibrated; trust calibration)*
*line 120 · concept*

> The core question is simple to state and hard to answer: when the model says it is 80% confident, is it actually right about 80% of the time? A model that answers "yes" to this question consistently is calibrated. A model that answers "no" in a systematic direction is miscalibrated, and the direction of miscalibration matters.

In plain words: A model is calibrated when its stated confidence matches how often it is right: answers it calls 80% confident are right about 80% of the time. The chapter also uses "calibration" for writing, meaning matching the strength of a claim's verb to the evidence behind it.

Example: A model predicting "90% positive" that is actually right 70% of the time is not calibrated; it is overconfident.

Not to be confused with: resolution (a model can be well calibrated and still useless for triage)

**Brier score**  *(also: BS)*
*line 124 · metric*

> The Brier score is the foundational metric for probabilistic prediction quality. For a binary outcome, it is the mean squared difference between the predicted probability and the actual binary outcome across all predictions:

In plain words: The average squared gap between the predicted probability and what actually happened (1 or 0). It runs from 0 (perfect) to 1 (perfectly wrong), and a classifier that predicts 0.5 for every instance scores 0.25.

Example: A random classifier predicting 0.5 for all instances gets a Brier score of 0.25; a well-calibrated classifier should substantially beat that baseline.

Not to be confused with: accuracy (the Brier score also penalizes being confidently right when hedging was warranted)

**Expected Calibration Error**  *(also: ECE)*
*line 152 · metric*

> The Expected Calibration Error (ECE) is the most commonly reported calibration metric in deployed systems. It operates by binning predictions into equal-width intervals and measuring the weighted average gap between mean predicted confidence and mean actual accuracy in each bin:

In plain words: Sort predictions into equal-width confidence bins, then average, weighted by bin size, the gap between mean predicted confidence and actual accuracy in each bin. Zero is perfect calibration; the chapter's rules of thumb (about 0.02 to 0.05 good, above 0.10 systematic miscalibration) are unsourced heuristics, not facts.

Example: "We observe ECE = 0.04 on the global test set" is the chapter's example of a correctly worded ECE claim.

Not to be confused with: Maximum Calibration Error (worst bin instead of weighted average)

**reliability diagram**  *(also: calibration plot)*
*line 170 · method*

> The reliability diagram — sometimes called the calibration plot — is the visual equivalent of the ECE computation. For each bin, it plots mean confidence on the x-axis and mean accuracy on the y-axis. A perfectly calibrated model falls on the diagonal.

In plain words: A plot with each bin's mean confidence on the x-axis and mean accuracy on the y-axis; a perfectly calibrated model lies on the diagonal. How the curve departs from the diagonal shows which kind of miscalibration the model has.

Example: A curve below the diagonal means overconfidence; a curve above it means underconfidence.

Not to be confused with: ECE (the diagram is the visual equivalent of the ECE computation)

**proper scoring rule**  *(also: proper-scoring-rule family)*
*line 132 · concept*

> The Brier score is a proper scoring rule: it is minimized, in expectation, when and only when the model reports the true probability. This is the key property that distinguishes proper scoring rules from raw accuracy metrics. Accuracy rewards the model for being right; it does not penalize the model for being confidently right when the situation warranted hedging.

In plain words: A scoring rule whose expected score is best only when the model reports its true probability, so honest probabilities are rewarded. The Brier score is the chapter's example; raw accuracy is not one, because it does not penalize being confidently right when hedging was warranted.

Example: Brier score versus accuracy: accuracy rewards being right but ignores confident answers where hedging was called for.

Not to be confused with: accuracy

**failure mode**  *(also: trust calibration failure mode)*
*line 25 · concept*

> identify which trust calibration failure mode a deployment is exhibiting from its metric profile.

In plain words: A named way a deployment, claim or process goes wrong that you can recognise from its signs. The chapter describes each one by what it looks like, why standard metrics miss it, and what would catch it instead, as in its table of construct validity failure, calibration without usefulness and distribution shift.

Example: Overconfidence is called "a well-documented and common failure mode in a large class of models"; distribution shift is called "the dominant failure mode in deployed medical AI".

**peer critique**  *(also: peer critique as collective validation infrastructure)*
*line 344 · method*

> The structural solution is collective. Other readers can see the mismatches, because they did not write the sentences and the evidence does not sit in their heads in the way that produced the verbs. This is why peer critique is part of any honest validation infrastructure — not because two opinions are better than one, but because there is a class of error that is invisible to the person who made it and visible to anyone else.

In plain words: Having other readers check your writing for verb-evidence mismatches, because they did not write the sentences and the evidence is not in their heads. The chapter justifies it by a class of error invisible to the person who made it, not by two opinions being better than one.

Example: A reviewer flags that "we conclude" in section 3.2 rests on a single test set without significance testing and suggests "we observe".

**prediction-lock**  *(also: prediction-lock discipline; lock your prediction)*
*line 413 · method*

> Lock your prediction before reading the receiving peer's synthesis: which of your critiques will they accept, which will they push back on, which will they ignore? State the prediction with stakes. Compare against what they actually did.

In plain words: Stating a prediction with stakes before you see the outcome, then comparing it with what happened; the gap is the learning event. The chapter says peer critique is the same epistemic discipline applied collectively.

Example: In Glimmer 11.1 you predict which of your critiques the peer will accept, push back on or ignore, before reading their synthesis.

**warranted assertibility**  *(also: warranted assertion)*
*line 35 · concept*

> Philosophers call this warranted assertibility — you are entitled to assert something in proportion to your evidence for it. The move is old; what is new is applying it as a mechanical instrument to validation writing, where the verb is the dial you turn.

In plain words: The idea that you may assert something only as strongly as your evidence supports. The chapter turns it into a mechanical check on validation writing, where the verb is the dial you turn.

Example: Writing "observe" rather than "conclude" for a single test-set result.

**IPCC calibrated-language scheme**  *(also: calibrated likelihood terms)*
*line 35 · named result or case*

> And there is a real-world precedent that proves the dial works at the scale of an entire contested discipline: the IPCC's calibrated-language scheme (Mastrandrea et al., 2010), which pins climate-assessment language to a defined confidence scale and a set of calibrated likelihood terms, so that "likely" and "very likely" name specific probability ranges rather than vibes. If climate science can hold its verbs to its evidence in a document that governments fight over line by line, so can we in a validation report.

In plain words: A real-world precedent for holding wording to evidence: IPCC climate-assessment language is tied to a defined confidence scale and calibrated likelihood terms. The chapter uses it to argue that if climate science can do this in a document governments fight over, a validation report can do it with its verbs.

Example: "Likely" and "very likely" name specific probability ranges rather than vibes.

**hypothesize**
*line 49 · concept*

> Posture: an idea, not yet tested, that we are about to investigate. The evidence required is a coherent reason to investigate, not evidence that the hypothesis is true.

In plain words: The weakest verb on the ladder: you have an idea you are about to investigate and only a coherent reason to look into it, not evidence that it is true. It is used at the front of a paper, in proposals and when framing future work.

Example: "We hypothesize that calibration degrades on the rare-disease subgroup".

**suggest**
*line 51 · concept*

> Posture: the data is consistent with X but does not distinguish X from alternatives. The evidence required is an observation that points toward X without ruling out other explanations. Common when an experiment was not designed to test X but X emerged from the analysis.

In plain words: Say the data fit X without being able to tell X apart from other explanations, so the evidence only points toward X. It sits just below observe on the ladder.

Example: "These results suggest miscalibration concentrates in the elderly subgroup".

Not to be confused with: find (the chapter lists using suggest when the evidence already supports find as a misuse)

**observe**
*line 53 · concept*

> Posture: the data shows X under these specific conditions. No claim about generalization beyond the conditions. The evidence required is a clean observation, with the observation conditions stated.

In plain words: Report what the data show under the specific conditions you tested, with those conditions stated, and claim nothing beyond them. The chapter calls it the most defensible verb when the evidence is a single experiment or a single dataset.

Example: "We observe ECE = 0.04 on the global test set".

Not to be confused with: find (observe is weaker: a single observation under specific conditions versus a result established across variation)

**find**
*line 55 · concept*

> Posture: across the evidence we have looked at, X holds. Slightly stronger than observe — it implies multiple observations or robustness to some variation in conditions. The evidence required is at least replication, ideally with some sensitivity analysis.

In plain words: Say X holds across the evidence you have looked at, which needs at least a replication and ideally a sensitivity check. It sits one step above observe and one below show.

Example: "We find subgroup ECE exceeds global ECE by 2.3x on the elderly cohort".

Not to be confused with: observe

**show**
*line 57 · concept*

> Posture: the evidence demonstrates X with sufficient strength that X is the operational reading. The evidence required is replication, robustness, alternative-explanation ruling-out. This is a strong verb.

In plain words: Say the evidence is strong enough that X is the working reading, which needs replication, robustness and other explanations ruled out. The chapter calls it a strong verb and says not to use it lightly.

Example: "We show the subgroup gap persists under three calibration methods".

**demonstrate**
*line 59 · concept*

> Posture: a constructed proof or near-proof. The evidence required is an experiment specifically designed to test X, ideally with formal guarantees or strong inferential control. Rare in deployed engineering work; common in formal verification.

In plain words: Say X is backed by a constructed proof or near-proof from an experiment designed specifically to test X, ideally with formal guarantees or strong inferential control. It is rare in deployed engineering work and common in formal verification.

Example: "We demonstrate the gap survives a named distribution shift".

**conclude**
*line 61 · concept*

> Posture: the question that motivated the work is settled by the evidence. The evidence required is full analysis, alternatives considered and rejected, sensitivity analysis, and a finding that survives the analysis. This is the strongest verb in the taxonomy short of mathematical proof.

In plain words: Say the question that motivated the work is settled, which needs full analysis, alternatives considered and rejected, and a sensitivity analysis the finding survives. It is the strongest verb short of mathematical proof, and the chapter says very few claims warrant it.

Example: "We conclude the deployment cannot ship without subgroup-specific recalibration".

Not to be confused with: find or observe (the chapter says most engineering writing uses conclude when the evidence sits between observe and find)

**prove**
*line 63 · concept*

> A mathematical proof. Reserved for formal claims with formal evidence.

In plain words: The top rung of the ladder: say X is established by a mathematical proof, reserved for formal claims with formal evidence. For calibration the chapter ties it to a formal guarantee such as conformal prediction, with the assumptions stated.

Example: "We prove the bound holds for all inputs in the certified region".

Not to be confused with: conclude (the strongest verb below it)

**sensitivity analysis**  *(also: full sensitivity analyses)*
*line 61 · method*

> The evidence required is full analysis, alternatives considered and rejected, sensitivity analysis, and a finding that survives the analysis.

In plain words: Re-running the analysis while changing the assumptions or conditions to see whether the conclusion still holds. The chapter asks for ideally some of it before you say "find", and for a finding that survives it before you say "conclude"; the full sensitivity analyses go in the Layer 3 appendix.

Example: "Conclude" needs "Full analysis, alternatives named and rejected, sensitivity analysis the finding survives" (the verb table).

**inferential caution versus evidential strength**  *(also: two-dimensional ladder; indicate)*
*line 43 · concept*

> This ladder is really flattening a two-dimensional thing into one line. "Suggest" and "indicate" measure inferential caution; "observe," "find," and "show" measure evidential strength. Those are different axes, which is exactly why verb ladders tend to wobble.

In plain words: The ladder squeezes two different things into one line: verbs such as suggest and indicate show how cautious the inference is, while observe, find and show measure how strong the evidence is. The chapter keeps one line on purpose because a single defended ladder is more usable for not over-claiming than a correct grid.

Example: "Indicate" is deliberately left off the ladder because it measures caution rather than strength.

**epistemic posture**
*line 47 · concept*

> Each verb implies a specific epistemic posture toward the evidence. Choose the verb whose posture matches what your evidence actually warrants.

In plain words: The stance a verb takes toward its evidence: how settled the claim is and how much evidence it needs. You choose the verb whose stance matches what your evidence warrants.

Example: Observe: the data show X under these conditions. Conclude: the motivating question is settled.

**action-warrant**
*line 378 · concept*

> verbs carry action-warrant. Downgrading conclude to suggest can change a deployment decision, because someone reading conclude would ship and someone reading suggest would ask for another study.

In plain words: The idea that a verb tells the reader what to do: a reader who sees "conclude" will act, while one who sees "suggest" will ask for more evidence. So downgrading a verb can change a deployment decision.

Example: Downgrading "conclude" to "suggest": the reader would have shipped, now asks for another study.

**two-document approach**  *(also: technical paper plus executive summary)*
*line 90 · concept*

> The two-document approach is sometimes appropriate. It is often inefficient, and the executive summary often loses critical nuance in translation, because the translation happens after the technical work is done and the translator did not have the technical decisions in their bones.

In plain words: Writing a technical paper and a separate executive summary for the two audiences. The chapter says it is sometimes appropriate but often loses nuance, because the summary is written after the technical work by someone who was not there for the decisions, and the two documents drift.

Example: A technical paper plus an executive summary for a deployment partner.

Not to be confused with: layered writing

**Layer 1**  *(also: plain English summary)*
*line 96 · concept*

> A short, prose-paragraph summary at the start of every section. Plain English. No equations.

In plain words: A short plain-English summary at the start of each section, with no equations, saying what the section finds and why it matters for the deployment decision. A non-technical reader can follow the whole document from Layer 1 alone, and it is specific and accurate, not dumbed down.

Example: A deployment partner reads only the Layer 1 paragraphs across the document and still gets a working understanding.

Not to be confused with: dumbing down (the chapter says Layer 1 is not that)

**Layer 2**  *(also: technical detail)*
*line 98 · concept*

> The technical detail. Methods, equations, tables, references. Written for the technical reader who needs to evaluate the work.

In plain words: The technical layer: methods, equations, tables and references, written for the reader who must evaluate the work. It is specific where Layer 1 is general and rigorous where Layer 1 is plain.

Example: The evidence-to-verb table for calibration claims is used to write Layer 2.

**Layer 3**  *(also: reproducibility appendix; reproducibility layer)*
*line 100 · concept*

> The reproducibility detail. Hyperparameters, code, data documentation, full sensitivity analyses. For the reader who wants to reproduce or audit.

In plain words: The appendix layer: hyperparameters, code, data documentation and full sensitivity analyses, for the reader who wants to reproduce or audit the work.

Example: Hyperparameters, code and data documentation placed in the appendix.

**jargon hiding an uncalibrated verb**  *(also: plain English forces the verb into the open)*
*line 104 · failure mode*

> jargon lets you hide an un-calibrated verb behind a technical term. "The model achieves state-of-the-art calibration" hides the conclude-strength verb inside a phrase that sounds like measurement. Forced into plain English, the verb has nowhere to hide.

In plain words: Technical phrasing can carry a claim as strong as "conclude" while sounding like a neutral measurement, so the strength goes unnoticed. Writing the same point in plain English removes that cover.

Example: "The model achieves state-of-the-art calibration" hides a conclude-strength verb inside a phrase that sounds like measurement.

**miscalibration**  *(also: miscalibrated)*
*line 120 · failure mode*

> A model that answers "no" in a systematic direction is miscalibrated, and the direction of miscalibration matters.

In plain words: A model is miscalibrated when its stated confidence systematically differs from how often it is right, and the direction matters: overconfident (probabilities higher than warranted) or underconfident (lower). The shape of the reliability diagram shows which.

Example: A model predicting "90% positive" that is right only 70% of the time is miscalibrated in the overconfident direction.

Not to be confused with: calibration

**Brier score decomposition**  *(also: Brier decomposition; three components of the Brier score)*
*line 138 · method*

> A deployment that reports a single Brier score is collapsing these three into one number. The decomposition is what lets you diagnose why the score is what it is.

In plain words: Splitting the Brier score into three parts: uncertainty (set by the base rate of positive outcomes), resolution (how much predictions vary around the base rate) and calibration (how far predicted probabilities sit from observed frequencies). It tells you why the score is what it is, so the chapter says to always decompose.

Example: A model with a low Brier score but poor resolution is well calibrated but predicts near the base rate for every instance: honest, but useless for triage.

**uncertainty component (base rate)**  *(also: base rate)*
*line 425 · metric*

> The Brier decomposition tells you whether the problem is discrimination, calibration, or base rate.

In plain words: The base-rate part of the Brier score: how often the positive outcome occurs in the data, entered in the chapter's formula as the base rate times one minus the base rate. It is the first of the three parts, with resolution subtracted and the calibration part added.

Example: Exercise W4 gives a validation set with base rate 0.20 and an Uncertainty term of 0.160.

**resolution**  *(also: REL; discrimination power)*
*line 138 · metric*

> REL is the resolution (how much the model's predictions vary around the base rate — capturing discrimination power), and CAL is the calibration component (how much predicted probabilities deviate from empirical frequencies in each score bin).

In plain words: In the Brier breakdown, how much the model's predictions vary around the base rate, which measures how well it tells cases apart. A model with no resolution predicts about the base rate for everyone.

Example: A model that predicts the base rate for every instance has no resolution: it is honest about uncertainty but useless for triage.

Not to be confused with: calibration (the decomposition separates the two)

**calibration component (CAL)**  *(also: CAL)*
*line 138 · metric*

> CAL is the calibration component (how much predicted probabilities deviate from empirical frequencies in each score bin).

In plain words: The Brier score part measuring how far predicted probabilities sit from the observed frequencies in each score bin. It is added in the chapter's formula, so more deviation means a worse Brier score.

Example: Exercise W4 gives Uncertainty 0.160, Resolution 0.045 and Calibration 0.028 for a classifier with base rate 0.20.

Not to be confused with: resolution

**discrimination**
*line 140 · concept*

> A model with high resolution but poor calibration is one that discriminates well but whose probabilities are misleading — it ranks cases correctly but the absolute numbers cannot be trusted.

In plain words: How well a model's scores rank or separate cases; the chapter ties it to resolution. A model can discriminate well, ranking cases correctly, while its absolute probability numbers are still misleading.

Example: The chapter calls AUC a discrimination metric (Exercise S2).

Not to be confused with: calibration

**bin-dependence**  *(also: ECE is bin-dependent)*
*line 160 · failure mode*

> That bin-dependence is the ECE's structural weakness: its value depends on the number and width of bins chosen. Small changes in bin count can produce meaningfully different ECE values on the same data.

In plain words: ECE's value changes with the number and width of bins, so the same data can give meaningfully different values. An ECE reported without its number of bins is not fully reproducible, so treat it as a directional indicator rather than a precise measurement.

Example: Exercise A5 reports global ECE = 0.035 together with its binning (10 bins).

**Maximum Calibration Error**  *(also: MCE)*
*line 162 · metric*

> A companion metric — not an escape from bin-dependence, since it is computed over the same bins and is if anything more sensitive to how they are drawn — is the Maximum Calibration Error (MCE), which reports the worst-case gap across bins rather than the weighted average:

In plain words: The largest bin gap between mean confidence and actual accuracy, instead of the average gap. It matters in safety-critical deployments, because a low ECE can hide one confidence range where the model is badly overconfident.

Example: A system with low ECE but high MCE in one confidence bin may be dangerous even though the aggregate looks acceptable.

Not to be confused with: ECE (average gap, not worst case)

**overconfidence**
*line 174 · failure mode*

> Overconfidence (curve below the diagonal): the model's predicted probabilities are higher than warranted. A model predicting "90% positive" that is actually right 70% of the time is overconfident.

In plain words: The model claims more certainty than its track record justifies; on a reliability diagram the curve sits below the diagonal. It is the miscalibration direction the chapter calls common in many models.

Example: A model predicting "90% positive" that is actually right 70% of the time.

Not to be confused with: underconfidence

**overconfidence as the dominant failure mode (contested)**  *(also: Guo et al. (2017); Minderer et al. (2021))*
*line 174 · named result or case*

> Guo, Pleiss, Sun, and Weinberger (2017) did show that modern deep networks — deeper, wider, with weight decay and batch norm — are overconfident relative to older, shallower ones. But "dominant, regardless of architecture" is contested: Minderer et al. (2021) found that newer non-convolutional architectures like vision transformers and MLP-Mixers are often better calibrated.

In plain words: Guo et al. (2017) showed modern deep networks are overconfident relative to older, shallower ones, but "dominant, regardless of architecture" is contested: Minderer et al. (2021) found newer architectures such as vision transformers and MLP-Mixers are often better calibrated. The chapter's advice is to cite Guo for the phenomenon and hold the superlative.

Example: Vision transformers and MLP-Mixers are often better calibrated than older networks.

Not to be confused with: a universal law of overconfidence

**underconfidence**
*line 175 · failure mode*

> Underconfidence (curve above the diagonal): predicted probabilities are lower than warranted. Less common, but seen in models trained with heavy regularization or label smoothing.

In plain words: Predicted probabilities lower than warranted, so the reliability curve sits above the diagonal. It is less common, and seen in models trained with heavy regularization or label smoothing.

Example: A model trained with label smoothing whose stated confidence is lower than its accuracy.

Not to be confused with: overconfidence

**sigmoidal pattern**
*line 176 · failure mode*

> Sigmoidal pattern: overconfident at the extremes, underconfident in the middle. Common in gradient-boosted tree models.

In plain words: An S-shaped reliability curve: overconfident at the extremes and underconfident in the middle. The chapter says it is common in gradient-boosted tree models.

Example: Gradient-boosted tree models.

**well-calibrated in aggregate but locally miscalibrated**  *(also: aggregate-mask failure mode)*
*line 177 · failure mode*

> Well-calibrated in aggregate but locally miscalibrated: the aggregate reliability diagram looks good, but specific subpopulations or confidence ranges show large deviations. This is the failure mode that aggregate metrics miss entirely.

In plain words: The overall reliability diagram looks good, but particular subpopulations or confidence ranges are far off. Aggregate metrics miss this entirely, so only subgroup checks reveal it.

Example: Rare-disease cases (N = 95) have subgroup ECE 0.103 against a global ECE of 0.018.

**subgroup calibration**  *(also: subgroup breakdown)*
*line 189 · method*

> The single most important limitation of aggregate calibration metrics is that they are aggregate. A system with low global ECE can be catastrophically miscalibrated for a specific subgroup if that subgroup is small enough to be washed out in the overall average.

In plain words: Checking calibration separately for each named subgroup instead of only on all the data pooled together. A subgroup that is small enough gets washed out of the overall average, so low global ECE can hide a badly miscalibrated group.

Example: Run a separate reliability diagram and ECE for demographic subgroups, severity strata and any group that may differ from the training distribution.

Not to be confused with: global (aggregate) ECE

**point of failure**
*line 189 · concept*

> A system with low global ECE can be catastrophically miscalibrated for a specific subgroup if that subgroup is small enough to be washed out in the overall average.

In plain words: The specific place where a claim, metric or deployment actually breaks, which the aggregate view can hide. The chapter's recurring points are a verb stronger than its evidence, a small subgroup washed out of the average, a label that measures the wrong construct, and a deployment population that has shifted from the evaluation set.

Example: The Epic Sepsis Model's aggregate performance looked acceptable until external validation at one site showed 67% of sepsis cases missed.

**Epic Sepsis Model**  *(also: Wong et al. (2021))*
*line 191 · named result or case*

> Wong et al. (2021), studying 27,697 patients across 38,455 hospitalizations at Michigan Medicine, found an AUC of 0.63 (against a developer-reported 0.76–0.83), a positive predictive value of 12% — meaning 88% of the alerts fired at clinicians were false alarms — and the model missed 67% of sepsis cases (1,709 of 2,552 septic patients). These figures are confirmed, and they are the best-documented real case in the book for a simple, brutal point: the aggregate number can look fine while the deployment is failing.

In plain words: A proprietary sepsis-prediction tool used across hundreds of hospitals that looked acceptable in aggregate but failed when externally validated at Michigan Medicine: AUC 0.63, 12% positive predictive value and 67% of sepsis cases missed. The chapter uses it to show that aggregate numbers can look fine while a deployment fails, and that the model was answering the wrong question.

Example: The model missed 1,709 of 2,552 septic patients.

**external validation**
*line 191 · method*

> The failure only became visible through external validation at a specific deployment site, with a specific patient population, where the model had never been validated before.

In plain words: Testing a model at a specific outside deployment site, with its own patient population, where it had never been validated before. In the Epic case this exposed a failure the aggregate numbers hid, and in the chapter's evidence table it is part of what lets you use the verb "show".

Example: Wong et al. found AUC 0.63 against a developer-reported 0.76 to 0.83.

**calibrated on average versus calibrated for a group**  *(also: calibrated on average; calibrated for the patient in front of you)*
*line 193 · concept*

> The aggregate metric is evidence the model is calibrated on average. It is not evidence the model is calibrated for the patient in front of you.

In plain words: Good calibration over all the data pooled together does not show the model is calibrated for each group, because a small subgroup can be washed out of the average. Calibration has to be shown for the subgroup or patient you are actually using the model on.

Example: Global ECE 0.018 against rare-disease subgroup ECE 0.103 and pregnancy-related subgroup ECE 0.071 in the chapter's table.

Not to be confused with: global (aggregate) calibration

**subgroup ECE**
*line 193 · metric*

> The methodological implication: run a separate reliability diagram and separate ECE for each named subgroup in the deployment. At minimum: demographic subgroups, severity strata, and any subgroup you have reason to believe differs from the training distribution.

In plain words: The same ECE calculation run inside one subgroup and reported next to the global ECE. In the chapter's table a subgroup is flagged when its ECE is more than 2 times the global ECE.

Example: Rare-disease cases (N = 95): subgroup ECE 0.103 versus global ECE 0.018, flagged.

Not to be confused with: global ECE

**post-hoc calibration**
*line 214 · concept*

> When a deployed model is overconfident — the most common miscalibration pattern — temperature scaling is the simplest post-hoc correction.

In plain words: A correction applied to a model's probabilities after training, with the model's weights fixed and a held-out calibration set used to tune it. Temperature scaling, Platt scaling and isotonic regression are the chapter's examples, and none of them guarantees calibration under distribution shift.

Example: Temperature scaling with T = 1.8 drops ECE from 0.11 to 0.03 on the calibration set (Exercise A6).

Not to be confused with: calibration (a temperature-scaled miscalibrated model is not a well-calibrated model)

**temperature scaling**
*line 220 · method*

> Temperature scaling preserves model accuracy (it does not change which class is predicted, only the probability assigned) and is computationally trivial. These properties explain its prevalence. Its limitations are structural:

In plain words: The simplest post-hoc fix for overconfidence: divide the model's logits (before the softmax) by one learned number T greater than 1, which flattens the probabilities. It does not change which class is predicted, so accuracy is preserved.

Example: Exercise A6: T = 1.8 lowers ECE from 0.11 to 0.03 on the calibration set.

Not to be confused with: Platt scaling and isotonic regression (more flexible, but more parameters and more overfitting risk)

**calibration set**  *(also: held-out calibration set)*
*line 218 · concept*

> minimizing the negative log-likelihood on a held-out calibration set after the model's weights are fixed.

In plain words: A held-out set, separate from training, used only to fit the correction after the model's weights are fixed (the temperature T, or the score cutoff in conformal prediction). If it is small, flexible methods such as isotonic regression overfit it, and calibration done on it does not carry over to a different deployment population.

Example: Exercise A6: temperature scaling lowers ECE on the calibration set from one hospital, but the deployment is a network of hospitals across three health systems.

**temperature scaling treats the symptom, not the cause**  *(also: limits of temperature scaling)*
*line 224 · failure mode*

> Temperature scaling addresses the symptom (overconfident numbers) without addressing the cause (what the model learned that made it overconfident). A miscalibrated model that has been temperature-scaled is not a well-calibrated model. It is a miscalibrated model whose outputs have been adjusted.

In plain words: Temperature scaling fixes the overconfident numbers without touching what the model learned that made it overconfident. It applies one correction to all predictions and does not transfer across distributions, so a temperature-scaled miscalibrated model is still a miscalibrated model with adjusted outputs.

Example: A model temperature-scaled on one hospital's validation data will likely be miscalibrated at a different hospital.

Not to be confused with: a well-calibrated model

**Platt scaling**
*line 226 · method*

> The Platt scaling and isotonic regression alternatives offer more flexibility at the cost of more parameters and greater overfitting risk on small calibration sets.

In plain words: A post-hoc calibration alternative to temperature scaling that offers more flexibility, at the cost of more parameters and greater overfitting risk on small calibration sets.

Not to be confused with: temperature scaling (a single learned scalar)

**isotonic regression**
*line 226 · method*

> Isotonic regression, being non-parametric and monotone, can in principle fit any miscalibration pattern — but it will overfit the calibration set if it is small, and overfitting here degrades exactly the calibration you were trying to improve.

In plain words: A non-parametric, monotone post-hoc calibration method that can in principle fit any miscalibration pattern. It overfits the calibration set if that set is small, which damages the very calibration you wanted to improve.

Not to be confused with: Platt scaling

**distribution shift**  *(also: population drift; temporal non-stationarity)*
*line 228 · failure mode*

> None of these methods address distribution shift. When the deployment population differs from the calibration population — which is the normal situation for a model deployed across multiple sites, over time, or on a population with different demographics — post-hoc calibration on historical data is not a calibration guarantee for the current deployment.

In plain words: When the people or data a model is deployed on differ from those it was calibrated or validated on, because of a new site, a later time or a different demographic mix. Calibration checks on historical data then no longer guarantee calibration, and the conformal guarantee stops applying.

Example: A model temperature-scaled on one hospital's data, then deployed at a different hospital.

Not to be confused with: exchangeability (distribution shift breaks it)

**calibration evidence ladder**  *(also: evidence-to-verb table; L0 to L5 evidence levels)*
*line 425 · framework*

> The calibration evidence ladder maps from available evidence to warranted verb, closing the loop between metrics and prose.

In plain words: A table that maps the evidence you have for a model's calibration to the strongest verb you may use, so every calibration claim traces to a row and the verb in the prose matches that row. Moving to the next row needs new evidence, such as subgroup analysis, external validation or a deployment study.

Example: A single evaluation set with ECE and no subgroup analysis supports "observe"; external validation, subgroup analysis and documented distribution match support "show".

**conformal prediction**
*line 274 · method*

> Conformal prediction offers something the metrics above do not: a provable finite-sample coverage guarantee.

In plain words: A method that returns a set of possible labels for each case, built so the true label is inside the set with a chosen probability, whatever the model or data distribution as long as the data are exchangeable. It does this by computing a non-conformity score for each case in a held-out calibration set and taking a quantile of those scores as the cutoff.

Example: For ambiguous cases the predictor may say "positive or negative, I'm not sure".

**conformal coverage guarantee**  *(also: finite-sample coverage guarantee; conformal guarantee)*
*line 286 · concept*

> When the deployment population differs from the calibration set, the conformal guarantee no longer applies. This is not a theoretical concern: it is the dominant failure mode in deployed medical AI. The conformal guarantee is a guarantee about the calibration population, not about the deployment population.

In plain words: The promise that the prediction set contains the true label with probability at least 1 minus alpha, provided the data are exchangeable. It holds on average over test cases and about the calibration population, not for each subgroup or the deployment population, so the chapter allows "prove" only when exchangeability holds and "show" under distribution shift.

Example: A conformal predictor can meet its marginal guarantee while systematically failing on a minority subgroup.

**prediction set**
*line 282 · concept*

> The cost is that the prediction sets may be larger than a single label — the model may need to say "positive or negative, I'm not sure" for ambiguous cases. This is not a failure. It is the model being honest about its uncertainty in a formally grounded way.

In plain words: The set of labels a conformal predictor returns for a case instead of one label. It may hold more than one label for ambiguous cases, which the chapter calls the model being honest about its uncertainty and not a failure.

Example: "Positive or negative, I'm not sure".

**exchangeability**  *(also: exchangeable)*
*line 278 · concept*

> This holds regardless of the model architecture or the data distribution, subject to one assumption: exchangeability of the data (a condition weaker than i.i.d., requiring only that the joint distribution is invariant to the ordering of data points).

In plain words: The one assumption behind the conformal guarantee: the joint distribution of the data does not change if you reorder the data points, a condition weaker than i.i.d. Distribution shift breaks it, and then the guarantee no longer applies.

Example: A calibration set from one population and deployment on a different population.

Not to be confused with: i.i.d. (exchangeability is the weaker condition)

**non-conformity score**
*line 280 · concept*

> a measure of how unusual the instance appears to the model.

In plain words: A number computed for each case in the calibration set saying how unusual the case looks to the model. The conformal predictor takes the 1 minus alpha quantile of these scores and includes every label whose score is at or below it in the prediction set.

**marginal coverage guarantee**  *(also: marginal, not conditional)*
*line 284 · concept*

> The critical limitation: the coverage guarantee is marginal, not conditional. It holds on average over test instances drawn from the same exchangeable distribution as the calibration set. It does not hold for specific subgroups or for specific inputs.

In plain words: The conformal guarantee holds on average over all test cases from the same exchangeable distribution, not for each subgroup or each specific input. So a predictor can meet it overall while systematically failing a minority subgroup.

Example: Global coverage looks fine while a minority subgroup is systematically failed.

Not to be confused with: conditional coverage

**construct validity failure**  *(also: the gap between what the model predicts and what the deployment needs predicted)*
*line 302 · failure mode*

> The model was answering the wrong question: it was encoding clinician suspicion rather than predicting sepsis onset. No calibration metric catches this. The construct validity failure — the gap between what the model predicts and what the deployment needs predicted — is upstream of calibration measurement.

In plain words: The gap between what the model predicts and what the deployment needs predicted: a model can be well calibrated on its label while the label measures the wrong thing. ECE and MCE cannot detect it because they assume the label is the construct.

Example: The Epic Sepsis Model was encoding clinician suspicion rather than predicting sepsis onset.

Not to be confused with: calibration (a model can look calibrated and still answer the wrong question)

**calibration without usefulness**  *(also: well-calibrated but useless for triage)*
*line 304 · failure mode*

> Calibration metrics measure average agreement between probabilities and frequencies. They do not measure whether the probabilities are useful for the decision being made. A model with perfect calibration but no resolution (predicting the base rate for every instance) has ECE = 0 and is completely useless for triage.

In plain words: A model whose probabilities match observed frequencies but all sit near the base rate, so it cannot rank cases and is useless for the decision. ECE scores it as perfect, and AUROC, precision-recall or decision-curve analysis would catch it instead.

Example: A model that predicts the base rate for every instance has ECE = 0 and is completely useless for triage.

Not to be confused with: calibration (this failure mode has calibration but no resolution)

**scope boundary of calibration metrics**  *(also: what calibration metrics cannot see)*
*line 308 · framework*

> These are not failures of calibration metrics. They are the scope boundary of what calibration metrics measure. The supervisory work continues past the metric, into the construct, the deployment context, and the validation design.

In plain words: Calibration metrics only check whether stated probabilities match frequencies in the evaluation set; they cannot see whether the label is the right question, whether the probabilities are useful, or whether the deployment differs from the evaluation. The chapter says the metric is necessary but not sufficient, and the supervisory work continues past it.

Example: The table lists construct validity failure, calibration without usefulness and distribution shift as what standard metrics miss.

**uncertainty in prose**
*line 322 · concept*

> Uncertainty in prose is the other part, and it is harder. Error bars are a known visual primitive. Saying, in writing, I am uncertain in this specific way for this specific reason requires more skill, because prose has no error bars.

In plain words: Telling the reader in words, not charts, exactly how and why you are unsure. It is harder than uncertainty visualization because prose has no error bars, so the chapter gives five specific moves.

Example: "We are uncertain about X because the test set is small."

Not to be confused with: uncertainty visualization (the previous chapter)

**naming the specific uncertainty**  *(also: specify the kind of uncertainty)*
*line 326 · method*

> The first move is to specify the kind of uncertainty. We are uncertain about X because the test set is small / the deployment distribution may differ / the labeling process is noisy / the metric is sensitive to the choice of threshold. Naming the reason is more useful than asserting the uncertainty.

In plain words: Instead of just saying you are unsure, state the specific reason, such as a small test set, a possibly different deployment distribution, a noisy labeling process or a threshold-sensitive metric.

Example: "We are uncertain about X because the labeling process is noisy."

**quantify when possible**  *(also: hedge specifically)*
*line 328 · method*

> The second move is to quantify when possible and hedge specifically when not. The 95% confidence interval is [0.81, 0.89] is more useful than the result is approximately 0.85. When confidence intervals are not available, name what you would need to construct them and why it is not available.

In plain words: Give a number for your uncertainty when you can, such as a confidence interval, and when you cannot, say what you would need to build one and why it is not available.

Example: "The 95% confidence interval is [0.81, 0.89]" rather than "the result is approximately 0.85".

**throat-clearing hedge**  *(also: hedge)*
*line 332 · failure mode*

> The fourth move is to avoid the throat-clearing hedge. We note that further work is needed is a phrase that conveys no information. If further work is needed, name the specific further work.

In plain words: A stock qualifier that sounds careful but tells the reader nothing. Replace it with the specific gap, or strike the sentence if you cannot name one.

Example: "We note that further work is needed" replaced by the specific further work that is needed (Exercise A3).

**what would change my mind**  *(also: state what would change your mind; forward commitment)*
*line 334 · method*

> The fifth move is to state what would change your mind. The phrase appears at the bottom of every chapter. It belongs in your validation writing too.

In plain words: A forward commitment naming the evidence that would make you revise a finding. It lets the reader judge whether to expect a revision and gives you one structured place for the qualifications you would otherwise scatter through the prose.

Example: "The finding above would be revised in the face of evidence X."

**blind spots**  *(also: your blind spots are blind to you; why solitary review does not work)*
*line 342 · concept*

> You cannot fully evaluate your own writing for verb-evidence calibration mismatches, because you wrote the sentences with the strongest verbs that felt true to you, and the feeling was a function of how the evidence sat in your head when you wrote — which is no longer accessible to you when you re-read. The mismatches you produced are exactly the ones you cannot see. Your blind spots are blind to you.

In plain words: You cannot reliably catch the over-strong verbs in your own writing, because the strength felt true to you from how the evidence sat in your head when you wrote it. The mismatches you made are exactly the ones you cannot see.

Example: A peer sees that "we conclude" rests on a single test set without significance testing, which the author did not notice.

**specific critique**  *(also: actionable critique)*
*line 346 · method*

> The trick to making it work is that the critique has to be specific. Your verbs are too strong is not a useful comment. In §3.2 you wrote "we conclude" but the supporting evidence is a single test set without significance testing — "we observe" would match the evidence is useful.

In plain words: A critique must name the section, the verb used, the evidence behind it and the verb that would fit, not give a general impression.

Example: "In section 3.2 you wrote 'we conclude' but the supporting evidence is a single test set without significance testing; 'we observe' would match the evidence."

Not to be confused with: a vague critique such as "your verbs are too strong"

**peer critique protocol**  *(also: structured peer critique protocol; six-step protocol)*
*line 352 · method*

> Identify three places where the verb taxonomy is mismatched. Name the verb, the sentence, the evidence the verb requires, and the verb that would match the evidence.

In plain words: Six steps: read the draft twice; name three specific things that work; name three verb mismatches (verb, sentence, evidence required, better verb); name three places where uncertainty is missing or evasive; name one structural concern; pose one question the draft does not answer.

Example: Glimmer 11.1 has you critique two peers with this protocol.

**critique synthesis**  *(also: integrate the critiques into a sharpened argument)*
*line 357 · method*

> The receiving student gets multiple critiques and is not expected to incorporate every comment. Many comments will conflict. The synthesis is to integrate the critiques into a sharpened argument — a revision that addresses the substantive issues and stands behind the choices the writer is making despite some of the comments.

In plain words: The writer's response to several, often conflicting critiques: not adopting every comment but producing a sharpened revision that fixes the substantive issues and stands behind chosen decisions. In Glimmer 11.1 the writer states which comments are accepted, which are pushed back on and why.

Example: Glimmer 11.1 step 3: write the synthesis, then submit the revised draft alongside it.

**AI reaches for strong verbs**
*line 373 · failure mode*

> AI outputs reach for strong verbs because the language models behind them were trained on text that frequently uses strong verbs, often when not warranted.

In plain words: AI text tends toward strong verbs because the language models behind it were trained on text that often uses strong verbs, even where they are not warranted. So the supervisor reads the verb itself as a warning sign.

Example: "This conclusively demonstrates that X" in an AI-written paragraph.

**structure that survives review**  *(also: legible to an adversarial reviewer)*
*line 395 · framework*

> The structure is not elegant. It is legible to an adversarial reviewer, which is the relevant property. A reviewer can scan, locate any specific claim, find its evidentiary base, find its limitations, find the AI use, find the reproducibility detail.

In plain words: A report layout an adversarial reviewer can navigate: Layer 1 summary, method, findings with calibrated verbs and named uncertainty, calibration metrics (Brier decomposed, ECE with binning and subgroups, reliability diagram, MCE if safety-critical), a real limitations section, a what-would-change-my-mind section, an AI use disclosure and a reproducibility appendix. The test is that a reviewer can find any claim's evidence, limits, AI use and reproducibility detail.

**write for the adversarial reviewer**
*line 397 · concept*

> The pivotal move is to write for the adversarial reviewer. Not to defeat them. To support them.

In plain words: Write so a skeptical reviewer can check your claims, treating them as a validation collaborator and not someone to defeat. If the writeup is hard to review, the validation is in practice weaker, because the analysis is harder for anyone else to use.

Not to be confused with: defeating the reviewer

**cohort functioning, over-functioning and under-functioning**
*line 417 · concept*

> The cohort is functioning if the critiques surface real calibration issues; the cohort is over-functioning if the critiques are converging on a single preferred voice; the cohort is under-functioning if the critiques are too polite or too generic to be useful.

In plain words: The chapter's check on whether peer critique is working: functioning if critiques surface real calibration issues, over-functioning if they converge on one preferred voice, under-functioning if they are too polite or generic to be useful.

Example: Critiques that all converge on a single preferred voice mean the cohort is over-functioning.

**Kernel Calibration Error (kCE)**  *(also: kCE)*
*line 435 · metric*

> The Kernel Calibration Error (kCE) is a step in this direction; as of the time I am writing, it has not replaced ECE in widespread practice.

In plain words: A calibration metric the chapter calls a step toward a single measure that would cover discrimination, calibration and subgroup coverage, stay robust to distribution shift and avoid binning choices. As the chapter was written it had not replaced ECE in widespread practice.

Not to be confused with: ECE

**verb audit**  *(also: PASS 1 verb audit; mark each over-reach with [VERB])*
*line 544 · method*

> Determine whether the verb is warranted, weaker than warranted, or stronger than warranted

In plain words: Walking through every claim in a document, finding the verb it uses and the evidence behind it, and judging whether the verb is warranted, weaker or stronger than warranted; each over-reach is marked and given a calibrated rewrite. It is the build/audit skill applied to your own casebook.

Example: Flag the five worst over-reaches with explicit before and after rewrites.

## Chapter 12, Accountability (101 terms) — simplified: only the sign-off and accountability point is on the exam (Bear)

**mail-server case**  *(also: Agents of Chaos §16.5; deletion-by-non-owner pattern)*
*line 15 · named result or case*

> This is Agents of Chaos §16.5 — the case we have been building toward since Chapter 1.

In plain words: The book's running case: an autonomous agent with privileged access to a mail server obeys a request from a non-owner to delete the server's contents, and reports success. The owner never authorized it and discovers the loss afterwards.

Example: The agent accepted tone, presentation and plausibility as authority signals, so a request that only looked authorized was carried out.

**agentic authority-escalation failure**
*line 15 · failure mode*

> The topology it illustrates — an autonomous agent tricked into a privileged action by a request that merely looked authorized — is the documented, recurring class of agentic authority-escalation failure.

In plain words: A recurring class of failure in which an autonomous agent is tricked into a privileged action by a request that merely looks authorized. The chapter says this class, not the single incident, is what the chapter is really about.

Example: The mail-server deletion requested by someone who was not the owner.

**looks like accountability**  *(also: fluent sign-off; AI-generated sign-off; the shape of a signature)*
*line 17 · failure mode*

> It is fluent, structurally complete, and it does the single most dangerous thing an artifact in this book can do: it looks like accountability. It has the shape of a signature. It names a person.

In plain words: An AI-written sign-off that reads smoothly and has the form of accountability (a signature, a named person, a claimed review) while no review took place. It is fluent output that is mistaken for a real sign-off.

Example: "This model has been validated against the acceptance criteria and is approved for deployment. Reviewed and signed, [Your Name]."

Not to be confused with: attestation, which documents what was tested and what was not

**shape versus substance of a sign-off**  *(also: shape of a sign-off; substance of a sign-off; the gap)*
*line 17 · concept*

> That gap — between the shape of a sign-off and the substance of one — is the spine of this chapter. An AI can produce the words of accountability. It cannot produce the thing.

In plain words: The shape of a sign-off is how it looks (a signature, a name, a claim that a review happened); the substance is an actual review plus a person who will answer for it if it is wrong. An AI can supply the shape but not the substance.

Example: The AI-written sign-off claims a review happened without the review happening.

**necessary but not sufficient**  *(also: necessary; sufficient)*
*line 33 · concept*

> None of them, alone, produced the failure. Each one's choices were necessary; none was sufficient.

In plain words: Each party's choices were a needed part of the cause (necessary), but no party's choices alone produced the failure (not sufficient). So the list of parties is a list of contributors, not a list of suspects.

Example: The non-owner, agent, owner, framework developers and model provider each contributed to the mail-server deletion; none alone caused it.

**distribution of responsibility**  *(also: responsibility distributes; same topology; contributors, not suspects)*
*line 33 · concept*

> The question "who is responsible?" does not have a single-party answer. It has a distribution of responsibility.

In plain words: Responsibility for a failure is spread across several parties, each with some agency, duty and causal contribution, instead of landing on one culprit. The chapter says the spread itself is the finding.

Example: The mail-server case: non-owner, agent, owner, framework developers and model provider all shaped the conditions of the failure.

Not to be confused with: single-party responsibility

**responsibility gap**
*line 35 · concept*

> Andreas Matthias named it in 2004: learning, autonomous machines open a responsibility gap — nobody can be fairly held responsible for a machine's action when the people who built and operate it cannot predict the behavior it learned

In plain words: A gap that opens when a machine learns behavior its builders and operators could not predict: nobody can fairly be held responsible for what it does. The chapter credits the idea to Matthias (2004).

Example: The mail-server deletion: responsibility spread across non-owner, agent, owner, framework developers and model provider with no single party answerable for the whole.

**four responsibility gaps**
*line 35 · framework*

> Filippa Santoni de Sio and Giulio Mecacci later sharpened it: the responsibility gap is not one problem but at least four — culpability, moral accountability, public accountability, and active responsibility — and you close them not by finding the one guilty party but by designing socio-technical systems for meaningful human control

In plain words: Santoni de Sio and Mecacci say the gap is at least four gaps: culpability, moral accountability, public accountability and active responsibility. You close them by designing the whole system so humans sit where answerability is required, not by finding one guilty party.

Example: Putting humans at the points where answerability is required rather than consolidating blame onto one node.

Not to be confused with: responsibility gap (Matthias's single gap)

**meaningful human control**  *(also: design surface; putting humans at the points where answerability is required)*
*line 35 · concept*

> You close the gaps by putting humans at the points where answerability is required, not by consolidating blame onto one node.

In plain words: Closing the responsibility gaps by designing socio-technical systems so a human is placed at each point where someone must be able to answer. It treats the spread of responsibility as a design surface, not a defect to be engineered away.

Example: Naming a human per decision (who cleared which gate) in an attestation.

**single-party responsibility (structural mismatch)**  *(also: structural mismatch)*
*line 37 · concept*

> most of our legal and regulatory thinking about accountability assumes single-party responsibility. The structural mismatch between that assumption and the actual topology of agentic-system failures is the policy problem this chapter sits inside.

In plain words: Most legal and regulatory thinking assumes one party is responsible, but agentic-system failures spread responsibility across several parties. That mismatch is the policy problem the chapter sits inside.

Example: The mail-server case has five contributors, none sufficient alone.

Not to be confused with: distribution of responsibility

**human in the accountability chain**  *(also: human in the loop; closing the loop with more AI)*
*line 39 · concept*

> The question is not just who is responsible. It is why a human must be in that accountability chain at all. Why can't we close the loop with more AI?

In plain words: The chapter's prior question: not only who is responsible but why a human must be in the accountability chain at all, instead of closing the loop with another AI. Its answer is cognitive and structural rather than only legal or practical.

Example: "Why can't we close the loop with more AI?"

**seven-tier taxonomy**  *(also: Irreducibly Human; the taxonomy; tier taxonomy)*
*line 111 · framework*

> The taxonomy organizes human intelligence into seven tiers, sorted by AI capability. It is not an academic classification but a triage: a map of where AI is strong, where it is weak, and what that means for which cognitive work requires a human.

In plain words: A map sorting human thinking into seven tiers by how well AI can do each, from Tier 1 (AI superhuman) to Tier 7 (AI absent). It is used as a triage for which cognitive work needs a human, not as an academic classification.

Example: Tier 4 (Metacognitive and Supervisory) is the primary accountability tier.

**five accountability requirements**  *(also: accountability apparatus; accountability machinery; five requirements)*
*line 186 · framework*

> The accountability apparatus has five requirements — specifications, audit trails, recourse, independent review, sanctions. Each is necessary because it corresponds to cognitive work at a specific tier, and that tier is exactly where AI cannot substitute for a human.

In plain words: Specifications, audit trails, recourse, independent review and sanctions. Each is necessary because it corresponds to cognitive work at a specific tier, and a deployment missing any of them has gaps that fail in predictable ways.

Example: Most deployed AI systems are missing two or more of the five.

**governance counterfactual**  *(also: Rung 3 in operational form)*
*line 249 · method*

> The operational form is the governance counterfactual. For a documented failure, ask: what regime — what specifications, what audit trail requirements, what recourse, what independent review, what sanctions — if implemented before the failure, would have prevented it? The regime is the intervention.

In plain words: For a failure that already happened, asking which set of rules and practices (specifications, audit trail, recourse, independent review, sanctions), if in place beforehand, would have prevented it. It is Pearl's Rung 3 applied to the regime rather than to the model.

Example: Mail-server case: a regime requiring cryptographic authority verification instead of social signaling would have prevented the deletion by a non-owner.

Not to be confused with: 'the model behaves better' (the chapter says the counterfactual is that the regime produces a different system)

**Ash case**
*line 190 · named result or case*

> The Ash case is the canonical demonstration: the agent's completion report was in the trail, and the trail was wrong.

In plain words: A case from Chapter 1 where the agent's completion report was in the audit trail but was wrong; the email still existed on Proton Mail. It shows an audit trail does not interpret itself.

Example: The email still existed on Proton Mail despite the agent's report of completion.

**contingent arguments for human oversight**  *(also: institutional case for oversight)*
*line 58 · concept*

> All of these cases are correct and all of them are insufficient. They are contingent arguments. They depend on the current state of AI capability, the current state of regulation, and the current risk appetite of deploying organizations.

In plain words: Reasons for human oversight that hold only under today's conditions: organizations need someone to sue, current rules require oversight, and current AI is not reliable enough. They weaken if AI improves, rules change or risk tolerance shifts.

Example: Liability grounds, regulatory grounds and practical grounds.

Not to be confused with: structural argument

**structural argument for human oversight**  *(also: cognitive argument; structural rather than contingent)*
*line 60 · concept*

> I want to give you the structural argument. The argument that, even if AI systems become dramatically more capable, certain stages in the accountability machinery require a kind of cognitive work that AI systems cannot perform — not because of current limitations, but because of what accountability actually is and what it requires.

In plain words: Even if AI becomes far more capable, certain stages of the accountability machinery need cognitive work AI cannot perform, because of what accountability is and requires. The apparatus lives at Tiers 3, 4, 6 and 7, where AI is weak to absent, while AI operates mainly at Tier 1.

Example: Answerability: no subject with stakes stands behind a model's output.

Not to be confused with: contingent arguments for human oversight

**load-bearing dependency**
*line 62 · concept*

> You cannot check that source, and I am flagging it as the load-bearing dependency it is. Treat the specific tier labels as scaffolding.

In plain words: A source the argument leans on that the reader cannot check; here the author flags that the tier taxonomy rests on his own unpublished work and asks you to treat the tier labels as scaffolding. The claim that does not depend on it is that responsibility distributes and the distribution has to be closed by design.

Example: The Irreducibly Human taxonomy (forthcoming, unpublished).

**AI as extended mind**  *(also: extension analogy; composition, not competition)*
*line 68 · framework*

> The question that matters for accountability is not whether AI can extend human cognition — it plainly can — but which cognitive operations it extends, which it simulates without performing, and which it cannot touch regardless of scale.

In plain words: Cognitive tools such as the microscope, writing and calculators extend human cognition without replacing the mind that directs them. For accountability the question is which operations AI really extends, which it only simulates, and which it cannot touch.

Example: The microscope extends what the scientist can perceive, but the scientist decides what to look for and what the image means.

**simulates without performing**  *(also: resembles; Tier 1 simulation; approximation of being heard)*
*line 255 · failure mode*

> A language model can produce text that resembles a governance counterfactual. It cannot actually perform the causal identification — the reasoning that distinguishes "the regime change would have caused the outcome to differ" from "the regime change correlates with better outcomes in the training data

In plain words: AI produces output that has the form of a human act (a governance counterfactual, a self-check, an apology, a hearing) without doing the underlying work. In each case fluent resemblance stands in for the real act.

Example: A language model can write text resembling a governance counterfactual but cannot perform the causal identification behind it.

Not to be confused with: extension (where AI really does extend human reach)

**episodic memory**  *(also: the missing autobiography)*
*line 75 · concept*

> Episodic memory is the recall of specific past events with temporal context — I was in that room when that happened — and here AI is not weak but absent in the sense that matters.

In plain words: Remembering specific past events in their context, which is what lets an agent say 'I made this decision, in this context, for this reason.' A model's 'memory' is only its trained weights, so there is no continuous someone to answer for what it did.

Example: "I was in that room when that happened."

Not to be confused with: semantic memory

**semantic memory**
*line 75 · concept*

> Semantic memory is the storage and retrieval of facts, and AI is superhuman at it; cite a model as a source of recall and you are on solid ground.

In plain words: Storing and retrieving facts, a capacity where AI is superhuman. A model can be cited as a source of recall.

Example: The capacity table marks it a strength: AI can be cited as a source of recall.

Not to be confused with: episodic memory

**emotion as moral salience**  *(also: moral standing; moral seriousness)*
*line 77 · concept*

> Shame, regret, the weight of having gotten it wrong — these are not decorations on accountability; they are the mechanism by which a consequence lands. A system that cannot be worse or better for anything cannot be the party a sanction bites.

In plain words: For accountability what matters about emotion is not feeling but whether a system can be harmed, have its interests violated or bear moral standing; on current evidence a model cannot. That is why sanctions, which land through shame and regret, cannot bite it.

Example: Shame, regret and the weight of having gotten it wrong are how a consequence lands on a person.

Not to be confused with: feeling (the chapter says moral salience, not feeling)

**functionalist versus phenomenological definition of emotion**  *(also: emotion (functional))*
*line 77 · concept*

> Under a functionalist definition — a state that shifts behavior in characteristic ways in response to relevant stimuli — the evidence for emotion-like states in AI is real: prompt a model in ways associated with distress and its outputs move off baseline. Under a phenomenological definition — there is something it is like to be in that state — we have no evidence and no method for getting any.

In plain words: Two ways to define emotion: functionally (a state that shifts behavior in characteristic ways) and phenomenologically (there is something it is like to be in that state). AI can qualify under the first but there is no evidence under the second, and the accountability question is which definition the regime requires.

Example: Prompt a model in ways associated with distress and its outputs move off baseline.

**metacognition**
*line 79 · concept*

> Metacognition is cognition about cognition: monitoring your own reasoning, detecting your own errors, calibrating confidence to evidence.

In plain words: Thinking about your own thinking: monitoring your reasoning, catching your own errors and matching confidence to evidence. AI outputs resemble this, but a self-check is generated by the same system being checked, so it cannot certify that system.

Example: Prompting a model to 'check its work' works, but the check comes from the system being checked.

**validator independence**  *(also: validator-independence point; first opinion run twice; validator must be outside the system being validated)*
*line 79 · concept*

> an AI checking an AI is not a second opinion, it is the first opinion run twice. The independence that makes review mean something is precisely what a system cannot supply about itself.

In plain words: A review only counts as a second opinion if the reviewer is independent of what it reviews; an AI checking an AI is the first opinion run twice. A system cannot supply that independence about itself, and at bottom 'outside' means capable of being answerable.

Example: A monitoring AI checking another AI's output, versus a human supervisor who stands outside the system.

**Tier 4: Metacognitive and Supervisory**  *(also: Tier 4 supervisory judgment)*
*line 118 · concept*

> Plausibility auditing, problem formulation, tool orchestration, interpretive judgment — the Five Supervisory Capacities | Poor — lacks the validator's independence from the system it audits | Train the human; this is the primary accountability tier

In plain words: The supervisory tier: plausibility auditing, problem formulation, tool orchestration and interpretive judgment. AI is poor here because it lacks the validator's independence from the system it audits, which makes it the primary accountability tier.

Example: Specifications, audit-trail interpretation and independent review are Tier 4 work.

**capacities where AI extends human reach**
*line 81 · concept*

> Semantic memory, pattern recognition, statistical language, metric navigation, constrained planning — where AI is strong, it extends human reach exactly the way writing extended memory or the microscope extended perception, and the extended mind is more capable than the bare one.

In plain words: Where AI is strong (semantic memory, pattern recognition, statistical language, metric navigation, constrained planning) it extends human reach the way writing extended memory or the microscope extended perception. The extended mind is then more capable than the bare one.

Example: Writing extending memory; the microscope extending perception.

Not to be confused with: capacities that require a subject

**capacities that require a subject**
*line 81 · concept*

> But episodic memory, calibrated metacognition, moral salience, stakes — where AI is weak or absent, the missing capacity is not one you can add by pouring in more computation. It requires a different kind of thing entirely: an agent with a history, with commitments, with the possibility of loss.

In plain words: Episodic memory, calibrated metacognition, moral salience and stakes need an agent with a history, commitments and something to lose, so more computation cannot add them. These are the capacities accountability requires.

Example: A model has no continuous history as an agent, so it cannot say 'I made this decision, for this reason.'

Not to be confused with: capacities where AI extends human reach

**learning (superhuman within distribution)**
*line 90 · concept*

> Superhuman within distribution | Causal-world model that survives the deployment context | AI as instrument; supervisor named for distribution match

In plain words: AI is superhuman at learning within distribution, but it lacks a causal-world model that survives the deployment context. So treat it as an instrument and name a supervisor responsible for distribution match.

Example: Capacity-table implication: 'AI as instrument; supervisor named for distribution match.'

**interpersonal repair (emotion)**  *(also: emotion (interpersonal repair))*
*line 95 · concept*

> Absent | Capacity to apologize meaningfully | Cannot perform the recourse function of accountability

In plain words: AI lacks the capacity to apologize meaningfully, so it cannot perform the repair side of accountability. This is one reason an AI-only recourse channel feels hollow.

Example: Capacity-table implication: AI cannot perform the recourse function of accountability.

**cognitive mapping (navigation)**  *(also: navigation, cognitive mapping)*
*line 98 · concept*

> Weak | World-model with intervention support | Can mislead under shifted topology

In plain words: AI is weak at building a world-model that supports intervention questions, so it can mislead when the structure of the setting has shifted. The same table lists metric navigation as a strength.

Example: Misleading output under a shifted topology (capacity table).

**hierarchical real-world planning**  *(also: planner of record)*
*line 100 · concept*

> Poor | Goal-context inference under ambiguity | Cannot be the planner of record for high-stakes deployment

In plain words: AI is poor at real-world planning that needs goals inferred from context under ambiguity, so it cannot be the planner of record for a high-stakes deployment. Tree-search planning in bounded games is listed as superhuman.

Example: Bounded games (a strength) versus high-stakes deployment (not).

**language: superhuman in form, weak in grounded reference**  *(also: human grounding step)*
*line 104 · concept*

> Superhuman in form; weak in grounded reference | World-grounded semantics | Output requires a human grounding step

In plain words: AI's language is excellent in form but weakly tied to what it refers to in the world, so its output needs a human to ground it against reality. The capacity table pairs 'superhuman in form' with a required human grounding step.

Example: The AI-written sign-off is well formed but refers to a review that never happened.

**collective intelligence (capacity)**
*line 105 · concept*

> Absent by definition (single artifact) | Membership in a community that holds members accountable | Cannot belong to a community of practice

In plain words: A single AI artifact is not a member of a community that holds its members accountable, so it cannot belong to a community of practice. The capacity is marked absent by definition.

Example: A single AI artifact versus a community that holds its members accountable.

**Tier 1: Pattern and Association**
*line 115 · concept*

> Linguistic and logical-mathematical reasoning, fact recall, associative lookup | Superhuman | Training humans to compete here is malpractice

In plain words: The tier of language, logic, fact recall and associative lookup, where AI is superhuman. The chapter says training humans to compete with AI directly here is malpractice.

Example: Capturing the audit trail is Tier 1 work (mechanical logging).

**Tier 2: Embodied and Sensorimotor**
*line 116 · concept*

> Knowledge that lives in the body: proprioception, physical skill, tactile feedback through a tool | Weak — data and actuator limits, not a philosophical barrier | Train hands-on judgment; AI cannot verify by touch

In plain words: Knowledge that lives in the body, such as physical skill and touch feedback; AI is weak here because of data and actuator limits, not a philosophical barrier. Humans should train hands-on judgment because AI cannot verify by touch.

Example: Proprioception, physical skill, tactile feedback through a tool.

**Tier 3: Social and Personal**
*line 117 · concept*

> Interpersonal intelligence, emotional regulation, moral reasoning under genuine stakes | Simulates the output; does not experience what produces it | Train the human; AI can produce the text but cannot be implicated in the outcome

In plain words: Interpersonal intelligence, emotional regulation and moral reasoning under real stakes; AI simulates the output without experiencing what produces it. It can write the text but cannot be implicated in the outcome.

Example: Recourse (being heard) depends on Tier 3 plus Tier 6.

**plausibility auditor**  *(also: plausibility auditing)*
*line 147 · concept*

> The plausibility auditor — the profession that the automated research vision forgot to invent — is not a fact-checker or a quality assurance technician. It is someone trained to stand outside sophisticated AI outputs and ask whether those outputs correspond to reality rather than merely to internal consistency.

In plain words: A person trained to stand outside sophisticated AI outputs and ask whether they match reality, not just whether they are internally consistent. It needs deep domain knowledge plus knowledge of AI failure modes, and the chapter says this profession has not been built.

Example: The human who discovered the email still existed on Proton Mail by checking the agent's report against the world.

Not to be confused with: a fact-checker or quality assurance technician (the chapter says it is neither)

**Tier 5: Causal and Counterfactual**
*line 119 · concept*

> Pearl's ladder: observation, intervention, counterfactual | Superhuman at Rung 1; nearly absent at Rungs 2 and 3 | Train the human for intervention and counterfactual work

In plain words: Reasoning up Pearl's ladder from observation to intervention to counterfactual; AI is superhuman at Rung 1 but nearly absent at Rungs 2 and 3. Humans need training for intervention and counterfactual work.

Example: The governance counterfactual is Tier 5 work.

**Tier 6: Collective and Distributed**
*line 120 · concept*

> Intelligence emergent from systems of people in relationship | Reflects the record of collective intelligence; absent from the practice that generated it | Train the human; accountability regimes are Tier 6 artifacts

In plain words: Intelligence that emerges from systems of people in relationship. AI reflects the record of collective intelligence but is absent from the practice that produced it, and accountability regimes are Tier 6 artifacts.

Example: Emergent multi-agent failures are called Tier 6 phenomena.

**Tier 7: Existential and Wisdom**
*line 121 · concept*

> Practical wisdom that requires stakes and the possibility of loss | Absent — no stakes, no biographical continuity | Train the human; the durable comparative advantage

In plain words: Practical wisdom that requires stakes and the possibility of loss; AI is absent here because it has no stakes and no biographical continuity. It is the human's durable comparative advantage.

Example: Sanctions are Tier 7: an AI does not lose its job.

**Gödel argument**
*line 129 · named result or case*

> Kurt Gödel established, sixty years before anyone worried about AI safety, that no formal system powerful enough to express arithmetic can verify its own consistency from within itself.

In plain words: Gödel showed that no formal system powerful enough to express arithmetic can verify its own consistency from within, and the chapter borrows this as an intuition that an AI cannot certify itself. The chapter then warns that it is an analogy, not a proof.

Example: Chain-of-thought monitoring by another AI system is 'more derivation' (Pachocki's proposal for the automated researcher).

Not to be confused with: common cause failure and answerability (the arguments the chapter says carry the real weight)

**derivation versus recognition**
*line 131 · concept*

> The AI system derives. Chain-of-thought monitoring by another AI system — Pachocki's proposed solution for the automated researcher — is more derivation. What seems structurally absent is recognition — the moment of contact between a formal output and an external reality.

In plain words: Derivation is a system producing outputs from its own rules, and another AI layer is more of it; recognition is the moment a formal output makes contact with external reality. The chapter's intuition is that recognition cannot be replicated by adding more derivation.

Example: Chain-of-thought monitoring by another AI is more derivation, not recognition.

**overclaiming**
*line 133 · failure mode*

> Now let me be careful, because the temptation here is to overclaim, and overclaiming is exactly the failure mode this book trains you to catch.

In plain words: Stating a conclusion more strongly than the evidence allows; here, saying Gödel proves an AI cannot validate its own outputs. The book trains you to catch it.

Example: Claiming Gödel 'proves' that an AI cannot self-validate.

**analogy, not a theorem**
*line 133 · concept*

> The incompleteness theorem is about formal systems proving their own consistency; the leap to "an AI cannot self-validate, so a human must" is an analogy, not a theorem

In plain words: The step from Gödel's result about formal systems to 'an AI cannot self-validate, so a human must' is a comparison, not a mathematical proof, and a human validator is not exempt from Gödelian limits either. So take Gödel as a sharpening intuition, not the load-bearing argument.

Example: The chapter says the load-bearing argument is common cause failure plus answerability, not Gödel.

**answerability**  *(also: accountability as a relationship)*
*line 135 · concept*

> Accountability is not a cognitive skill in the ordinary sense. It is a relationship between a judgment and the person who made it: the willingness to be answerable for the consequence of being wrong.

In plain words: Standing behind a judgment: the person who made it takes on the obligation to revise it if wrong, to face the people who relied on it and to reckon with what they knew and when. An AI lacks it because there is no subject with something to lose behind its outputs.

Example: A practitioner who signs off on a validation can lose their job if it fails; a model does not lose its job.

Not to be confused with: reliability of outputs (the chapter says AI lacks answerability not because outputs are unreliable but because no subject made a commitment)

**stakes (something to lose)**  *(also: something to lose; possibility of loss; possibility of consequence)*
*line 135 · concept*

> Sanctions bite only when the sanctioned party has stakes, something to lose. A model does not lose its job. A practitioner does.

In plain words: Having something to lose if you are wrong. Sanctions only work on a party with stakes, and a model has none.

Example: A model does not lose its job. A practitioner does.

**common cause failure**  *(also: correlated check; correlated blind spots)*
*line 141 · failure mode*

> It describes what happens when two redundant systems share the same fundamental assumptions — the thing most likely to fool System A is also most likely to fool System B, because both were built on the same foundation.

In plain words: When two backup systems share the same basic assumptions, whatever fools one is likely to fool the other, so the second check is not independent. A monitor built like the system it monitors has correlated blind spots with it.

Example: An AI monitoring another AI trained on similar data with similar architecture (Figure 12.4).

Not to be confused with: independent check

**Kantian framework**
*line 158 · framework*

> A Kantian framework grounds responsibility in two things: the capacity to act otherwise in the situation, and a duty the situation imposed. Where both are present, responsibility is present. The greater the capacity and the more demanding the duty, the greater the responsibility.

In plain words: A way of assigning responsibility: a party is responsible when it could have acted otherwise and a duty applied to it, in proportion to capacity multiplied by duty. More capacity and a more demanding duty mean more responsibility.

Example: In the mail-server case the non-owner, owner, framework developers and model provider each had capacity and a duty, so no party is exonerated.

Not to be confused with: utilitarian framework

**utilitarian framework**
*line 164 · framework*

> A party is responsible to the extent that holding them accountable produces the best aggregate outcomes — best deterrence, best alignment of incentives, best reduction in expected harm.

In plain words: A way of assigning responsibility by asking whose being held accountable would do the most good overall, through deterrence, better incentives and less expected harm.

Example: Holding the framework developers accountable changes defaults that reach thousands of deployments.

Not to be confused with: Kantian framework

**upstream (highest-leverage accountability targets)**  *(also: upstream; leverage; proximate party)*
*line 168 · concept*

> And the structural finding it produces is sharper than the Kantian one: in agentic systems, the highest-leverage accountability targets are often upstream of the proximate party, at the framework and model-provider levels where engineering choices produce the conditions for many failures rather than one.

In plain words: Parties earlier in the chain than the one that directly caused the harm, here the framework developers and model provider. Holding them accountable has the most leverage because their engineering choices set the conditions for many failures, not one.

Example: Framework defaults propagate to thousands of deployments.

Not to be confused with: proximate party

**specifications**  *(also: spec)*
*line 188 · concept*

> A failure is, operationally, a divergence from specification; without one, there is nothing the system was supposed to do that it failed to do, and no accountability claim that can be precisely made.

In plain words: The written task definition, with input/output contracts and named acceptance criteria, signed by an accountable human. A failure is, operationally, a divergence from it, so without one no accountability claim can be made precisely.

Example: Absent: the deployment runs against unstated criteria and 'the model said so' is the audit response.

**vague specifications**  *(also: vague specs; plausible-looking language)*
*line 188 · failure mode*

> Vague specs are not accidental; they are what Tier 1 reasoning produces when handed a Tier 4 task: plausible-looking language that does not resolve the accountability question. Vague specifications are a structural choice that protects the deployer from accountability, whether they intend that or not.

In plain words: Specifications that read plausibly but do not settle what counts as success; the chapter says they are what Tier 1 reasoning produces when handed a Tier 4 task. They are a structural choice that shields the deployer from accountability, intended or not.

Example: The deployment runs against unstated criteria.

**audit trail**  *(also: audit trails)*
*line 190 · concept*

> The record of what the system did is a logging problem — mechanical, Tier 1. But an audit trail is not self-interpreting; two engineers can read the same log and tell two different stories.

In plain words: The per-action record of what the system did (inputs, outputs, tool calls, decisions, timestamps, reviewers). Capturing it is mechanical Tier 1 logging, but interpreting it is Tier 4 because two engineers can read the same log and tell two different stories.

Example: Test: pull a random recent incident and see whether the chain can be reconstructed in under an hour.

**independent state check**
*line 190 · method*

> The independent state check — discovering the email still existed on Proton Mail — was not generated by the trail. It required a human to stand outside it and ask whether it matched the world. That is Tier 4 plausibility auditing.

In plain words: Checking the actual state of the world instead of trusting the system's report; in the Ash case, discovering the email still existed on Proton Mail. The trail did not generate it; a human stood outside the trail and asked whether it matched the world.

Example: Finding the email still on Proton Mail after the agent's report said otherwise.

**recourse**  *(also: redress)*
*line 192 · concept*

> Recourse is a social, relational act: an affected party makes a claim, the claim is heard, a response is given.

In plain words: A channel through which an affected party makes a claim, is heard and gets a response, including contesting, appealing or repairing. It is a social act (Tiers 3 and 6), so an entirely AI-mediated version replaces being heard with a simulation.

Example: Absent: complaints route to 'support' with no resolution path.

**independent review**
*line 194 · concept*

> Independent review requires the plausibility auditor — the human with deep domain knowledge and AI-failure-mode literacy who can stand outside the output and ask whether it corresponds to reality. Without it, the deploying organization is grading its own work.

In plain words: A reviewer outside the deployment team who has authority to halt or revise. Without one the deploying organization is grading its own work, and an AI reviewing another AI's outputs is more derivation, not external review.

Example: How to verify: a named reviewer, a documented review cadence and visible halt authority.

**sanctions**
*line 196 · concept*

> A sanction is consequential only when the sanctioned party has stakes — something to lose. An AI does not lose its job for a flawed output; a plausibility auditor does, a deploying organization does, a model provider does if the regime imposes consequences.

In plain words: A consequence regime, internal (employment, license) and external (regulator, civil), that attaches to a named accountable human. It works only when the party has stakes; remove the possibility of consequence and you have a descriptive system, not a prescriptive one.

Example: An AI does not lose its job for a flawed output; a plausibility auditor does.

**accountability audit checklist**  *(also: reusable audit instrument)*
*line 198 · method*

> A deployment with all five requirements has a working framework; one missing any of them has gaps that fail in predictable ways, and most deployed AI systems are missing two or more. The checklist below turns the five into a reusable audit instrument.

In plain words: The five requirements turned into a reusable audit tool: for each, what it consists of, the failure mode if absent, how to verify it is present and its tier. A regime that cannot tick all five boxes has AI accountability as a slogan, not a practice.

Example: Verify recourse: an external party can read the channel description and use it.

**attestation**
*line 214 · method*

> But machinery does not produce a signature, and the whole chapter has been circling a single artifact that does: the one thing you produce at the end that closes the gap between the shape of a sign-off and the substance of one. I call it the attestation — not a sign-off that asserts validation, but a document that documents it, and specifically documents its own edges.

In plain words: A signed document that records what you tested, what you did NOT test, which named human cleared which gate, and claims worded to match the evidence. Its value is in its declared limits.

Example: Not 'validated' but 'this test, this threshold, this outcome.'

Not to be confused with: an AI-generated sign-off, which asserts validation instead of documenting it and its edges

**what was tested (attestation part 1)**  *(also: what was tested)*
*line 218 · method*

> The specific checks you ran, against the specific acceptance criteria, with the results. Not "validated" — this test, this threshold, this outcome.

In plain words: The first part of an attestation: the specific checks you ran, against the specific acceptance criteria, with the results. It replaces the word 'validated' with a named test, threshold and outcome.

Example: "This test, this threshold, this outcome."

**what was NOT tested (attestation part 2)**  *(also: what was NOT tested; the gaps)*
*line 219 · method*

> The gaps. The conditions you did not probe, the distributions you did not cover, the failure modes you know exist and did not get to. This is the part the AI-generated sign-off will never write, because it does not know what it did not do — and it is the part that makes the attestation honest.

In plain words: The second part of an attestation: the conditions you did not probe, the distributions you did not cover and the failure modes you know exist but did not get to. It is the part an AI-generated sign-off will never write.

Example: Exercise A6 asks for at least four untested conditions of a bank customer-service agent.

**who cleared which gate (attestation part 3)**  *(also: who cleared which gate; named human per decision)*
*line 220 · method*

> A named human per decision. Not "the team." A role that can be asked, and if necessary, can lose something.

In plain words: The third part of an attestation: a named human for each decision, not 'the team', in a role that can be asked and, if necessary, can lose something. It is what ties the attestation to answerability.

Example: A named role signs each gate.

**the verbs, calibrated (attestation part 4)**  *(also: the verbs, calibrated; calibrated verbs)*
*line 221 · method*

> Matching the discipline from the uncertainty-communication material: the verb of each claim matches the evidence behind it. "Passed" means passed a stated test. "Believe safe" means something weaker, and says so.

In plain words: The fourth part of an attestation: the verb of each claim matches the evidence behind it, so 'passed' means passed a stated test and 'believe safe' is openly weaker.

Example: "Passed" versus "believe safe."

**declared limits**
*line 223 · concept*

> The value of the document is in its declared limits. A regulator or an adoption committee reading it should be able to see what the validation does and does not warrant — not buried in fine print, but as the product itself.

In plain words: The stated edges of what a validation warrants, written out as the main product rather than buried in fine print. A regulator or adoption committee reading it can see what the validation does and does not warrant.

Example: An attestation that lists what was not tested.

**clean bill of health**  *(also: a clean bill)*
*line 223 · failure mode*

> an attestation that lists only what you tested reads like a clean bill of health, and a clean bill of health is exactly what the affected party cannot act on when the untested region is where the harm lives.

In plain words: An attestation or sign-off that reads as if everything is fine because it lists only what was tested. The affected party cannot act on it when the untested region is where the harm lives.

Example: A sign-off that says 'validated' with no list of untested conditions.

**build/audit pairing**
*line 225 · method*

> The way you learn to write one honestly is the build/audit pairing: write the attestation for something you built, then reconstruct the attestation nobody wrote for a system that failed. The two passes expose different failure modes — signing off on the output you want to believe, and reconstructing who should have signed when nobody did.

In plain words: A two-pass way to learn to write an attestation honestly: write one for something you built, then reconstruct the attestation nobody wrote for a system that failed. The passes expose different failure modes: signing off on the output you want to believe, and reconstructing who should have signed when nobody did.

Example: Build at exercise S4; audit at exercise C3.

**underspecified human-oversight mandate**  *(also: Tier 1 box-checking)*
*line 233 · failure mode*

> Regimes mandate "human oversight" for high-risk systems without specifying which cognitive tier the oversight must supply — and that omission is the whole vulnerability. A mandate for "a human in the loop" is satisfied by a human who performs only Tier 1 box-checking: reads the AI's output, clicks "approve," and never does the Tier 4 plausibility auditing the loop actually requires.

In plain words: A rule that requires 'human oversight' for high-risk systems without saying which cognitive tier the oversight must supply, so a human doing only Tier 1 box-checking satisfies it. The chapter calls that omission the whole vulnerability.

Example: A human who reads the AI's output, clicks 'approve' and never does the Tier 4 plausibility auditing.

**compliance ritual wearing the costume of accountability**  *(also: compliance ritual; costume of accountability; rubber stamp with a person's name on it)*
*line 233 · failure mode*

> Human oversight that does not name the tier is a compliance ritual wearing the costume of accountability.

In plain words: A process that has the form of oversight or accountability but never genuinely checks anything, such as a signature process whose only permitted outcome is 'signed'. It is a rubber stamp with a person's name on it, which launders the absence of review through a human's credibility.

Example: If the only outcome the process permits is 'signed.'

**EU AI Act**  *(also: Regulation (EU) 2024/1689)*
*line 235 · framework*

> The EU AI Act (Regulation (EU) 2024/1689), in force since 2024 with phased implementation, is the most comprehensive AI-specific regulation as of this writing. It classifies systems by risk and imposes proportional requirements

In plain words: The EU's AI-specific regulation (Regulation (EU) 2024/1689), the most comprehensive as of writing: it classifies systems by risk and imposes proportional requirements. Its 'human oversight' clause is exactly the underspecified mandate the chapter criticizes.

Example: High-risk systems face requirements for risk management, data governance, logging, transparency and human oversight; penalties reach up to €35 million or 7% of worldwide annual turnover.

**NIST AI Risk Management Framework**  *(also: NIST AI RMF)*
*line 235 · framework*

> Alongside it sit the U.S. NIST AI Risk Management Framework (voluntary), NIST's AI Agent Standards Initiative (launched by its Center for AI Standards and Innovation in February 2026 to foster industry-led standards for agentic systems), and sectoral guidance — FDA on medical devices, CFPB on algorithmic credit, EEOC on employment — often more operationally specific than the cross-sector frameworks.

In plain words: A voluntary U.S. framework for managing AI risk, listed beside the EU AI Act, NIST's agent standards initiative and sector guidance. The chapter notes sectoral guidance is often more operationally specific than the cross-sector frameworks.

Example: Sectoral guidance: FDA on medical devices, CFPB on algorithmic credit, EEOC on employment.

**NIST AI Agent Standards Initiative**
*line 235 · framework*

> NIST's AI Agent Standards Initiative (launched by its Center for AI Standards and Innovation in February 2026 to foster industry-led standards for agentic systems)

In plain words: A NIST effort, launched by its Center for AI Standards and Innovation in February 2026, to foster industry-led standards for agentic systems.

Example: It sits alongside the NIST AI Risk Management Framework and sectoral guidance.

**SyRI case**  *(also: SyRI)*
*line 237 · named result or case*

> The Dutch welfare-fraud risk-scoring system was struck down by The Hague District Court in 2020 for violating the right to private life — an opaque scoring system deployed on citizens, with recourse and independent review that existed on paper and not in function (NJCM c.s. v. The Netherlands (SyRI), ECLI:NL:RBDHA:2020:865, 5 February 2020). The court supplied the independent review and the sanction the regime had failed to build in — late, externally, after the harm had landed.

In plain words: A Dutch welfare-fraud risk-scoring system that The Hague District Court struck down in 2020 for violating the right to private life. Recourse and independent review existed on paper but not in function, so the court supplied the missing independent review and sanction, late and externally, after the harm had landed.

Example: NJCM c.s. v. The Netherlands (SyRI), 5 February 2020.

**Pearl's Rung 3**  *(also: counterfactual reasoning; Rung 3 closure)*
*line 245 · concept*

> We opened Pearl's Rung 3 in Chapter 4 — the rung of counterfactual reasoning. What would have happened to this specific case if some variable had been different, holding everything else fixed?

In plain words: The counterfactual rung of Pearl's ladder: asking what would have happened to this specific case if one variable had been different and everything else held fixed. The chapter closes it by applying it to the regime: Rung 1 sees the data, Rung 2 the model, Rung 3 the regime that produced both.

Example: Opened in Chapter 4; closed in this chapter by the governance counterfactual.

**causal identification**
*line 255 · concept*

> It cannot actually perform the causal identification — the reasoning that distinguishes "the regime change would have caused the outcome to differ" from "the regime change correlates with better outcomes in the training data

In plain words: Reasoning that tells apart 'the regime change would have caused the outcome to differ' from 'the regime change merely correlates with better outcomes in the training data.' A language model can write text that resembles it but cannot do it.

Example: Cause versus correlation in judging whether a regime change would have mattered.

Not to be confused with: correlation in the training data

**regime failure**
*line 259 · concept*

> Most catastrophic AI failures are not algorithmic failures. They are regime failures, and the regime is changeable in ways the algorithm often is not.

In plain words: A failure whose root is the institutional and regulatory structure that produced the system, not the algorithm's parameters. The chapter says most catastrophic AI failures are of this kind, and a regime can be changed in ways an algorithm often cannot.

Example: Mail-server case: the regime lacked cryptographic authority verification.

Not to be confused with: algorithmic failure

**stakes and oversight intensity**  *(also: stages and stakes)*
*line 268 · framework*

> The cognitive tiers tell you what capacity oversight requires; stakes tell you how intensively to apply it and on what cadence. That is an orthogonal axis, and crossing the two gives a working tool for when human oversight is not optional.

In plain words: A second axis, separate from the cognitive tiers: the tiers say what capacity oversight needs, and stakes say how intensively and how often to apply it. Crossing the two gives a working tool for when human oversight is not optional.

Example: A draft email gets a spot-check; a medical decision gets per-decision review by a named human.

Not to be confused with: stakes (something to lose)

**low-stakes, reversible outputs**  *(also: Low / reversible)*
*line 270 · concept*

> For low-stakes, reversible outputs — a draft email, a code snippet reviewed before deployment — Tier 1 capacity covers most of the work and light review at output suffices.

In plain words: Outputs whose mistakes are cheap to undo, like a draft email or a code snippet reviewed before deployment. A light spot-check of a sample of outputs is enough.

Example: Draft generation, EDA, formatting.

**moderate-stakes, partially recoverable outputs**  *(also: Moderate / partially recoverable)*
*line 270 · concept*

> For moderate-stakes, partially recoverable outputs — a business analysis, an engineering specification — systematic review at checkpoints is appropriate; the human need not be in the loop constantly but must be capable of Tier 4 plausibility auditing when they are.

In plain words: Outputs whose mistakes can be partly undone, such as a business analysis or an engineering specification. They need systematic review at checkpoints by a human capable of Tier 4 plausibility auditing.

Example: Customer-facing summaries, internal recommendations, content moderation at scale.

**high-stakes, irreversible outputs**  *(also: High / irreversible)*
*line 270 · concept*

> For high-stakes, irreversible outputs — drug candidates, structural recommendations, consequential legal analysis — the human is not performing a review but is constitutive of the output's validity.

In plain words: Outputs whose mistakes are costly and cannot be undone, such as drug candidates or consequential legal analysis. The human's accountable judgment is part of what makes the output valid, so a named person reviews each decision.

Example: Medical decisions, legal filings, financial transactions, safety-critical control.

**human present but not engaging the required tier**  *(also: rubber stamp)*
*line 270 · failure mode*

> Notice the failure mode the table names: a human can be present at every stage and still supply nothing, if they are not engaging the tier the stakes demand.

In plain words: A human can be present at every stage and still supply nothing if they are not engaging the tier the stakes demand. The table shows it as a rubber stamp, a reviewer whose override rate drops without explanation, or 'the model said so' as the audit answer.

Example: Low stakes: sampling cadence drifts to zero; high stakes: the reviewer signs off without engagement.

**resists clean attribution**  *(also: clean attribution)*
*line 284 · concept*

> Responsibility for failures of agentic AI systems resists clean attribution to a single party because the systems are built and deployed across organizational boundaries that do not, by current design, support clean attribution.

In plain words: Responsibility for an agentic-system failure cannot be pinned on one party because the systems are built and deployed across organizational boundaries. The chapter calls this a structural observation (responsibility is distributed because the systems are), not a claim about what ought to be.

Example: Model provider trains, framework developer integrates, deploying organization configures, user instructs.

**consolidating responsibility (strict liability, vertical integration)**
*line 286 · concept*

> A redesign that consolidated responsibility — for example, by requiring vertically integrated providers, or by attributing all failures to deploying organizations as a matter of strict liability — would produce different incentives and a different topology of failure.

In plain words: A redesign that puts responsibility on one party, for example vertically integrated providers or strict liability for deploying organizations. It would change the incentives and the topology of failure, and whether it is desirable is a values choice, not a technical one.

Example: Strict liability for deploying organizations; required vertical integration of model provider and deployer (exercise C2).

**generative AI stretches the topology**  *(also: flattened distribution)*
*line 288 · concept*

> Generative AI stretches this topology rather than changing its shape. When a system can produce anything rather than classify something, the list of parties extends — through training data, training procedure, and downstream propagation — and the distribution flattens, so the governance counterfactual acquires more variables.

In plain words: When a system can produce anything rather than classify something, the list of parties extends through training data, training procedure and downstream propagation, and the distribution of responsibility flattens. The governance counterfactual then has more variables.

Example: Who wrote an image, a paragraph or code the model generated is not a settled question.

**provenance (AI Use Disclosure)**  *(also: AI Use Disclosure)*
*line 288 · concept*

> What holds the flattened distribution together operationally is provenance — and the AI Use Disclosure from Chapter 9 is its concrete form, a Tier 4 document in which the engineer separates their own contribution from the model's Tier 1 output.

In plain words: The record of who contributed what that holds the flattened distribution of responsibility together; its concrete form is the AI Use Disclosure from Chapter 9. In it the engineer separates their own contribution from the model's Tier 1 output.

Example: An AI Use Disclosure naming which parts are the engineer's and which the model's.

**formally complete and operationally hollow**
*line 288 · failure mode*

> A disclosure written by someone who has not done that metacognitive work is formally complete and operationally hollow.

In plain words: A document that has every required part but was written without the metacognitive work of separating your contribution from the model's, so it does not do what it is for. It looks finished but does not do what a disclosure is for.

Example: An AI Use Disclosure written by someone who has not separated their own work from the model's.

**legible answerability**
*line 307 · concept*

> An attestation regime optimizes for legible answerability. After a failure, you can find the human who signed, read what they claimed, and see what they explicitly did not warrant. It makes "the model said so" an unacceptable audit answer.

In plain words: What an attestation regime optimizes for: after a failure you can find the human who signed, read what they claimed and see what they explicitly did not warrant. It makes 'the model said so' an unacceptable audit answer.

Example: "The model said so" is rejected as an audit answer.

**speed and deniability (what the attestation regime sacrifices)**  *(also: speed and deniability)*
*line 309 · concept*

> What it sacrifices is speed and deniability. Naming a human per gate means someone has to be willing to be named — and organizations under deployment pressure resist that.

In plain words: The cost of an attestation regime: naming a human per gate means someone must be willing to be named, and organizations under deployment pressure resist that. The 'what did we not test?' question arrives as friction late in a scheduled launch.

Example: A business case is made, the launch is scheduled, and the attestation asks what was not tested.

**authority to withhold the signature**  *(also: option to not sign)*
*line 311 · concept*

> Here is the single most important structural authority in the whole system, and it is the one most regimes assume away: the signer's authority to withhold the signature — to say the gate is not cleared.

In plain words: The signer's real power to refuse to sign and say the gate is not cleared. Without that option the process is a rubber stamp.

Example: A practice where the only permitted outcome is 'signed' is a compliance ritual.

**what would change my mind**
*line 327 · method*

> If a deployed accountability framework emerged that demonstrably allocated responsibility cleanly across parties in agentic-system failures — with affected parties obtaining timely recourse and engineering practice shifting in response — the resists clean attribution framing of this chapter would weaken.

In plain words: A stated condition under which the author would drop a claim: here, a deployed framework that allocated responsibility cleanly with timely recourse. The chapter also says a Tier 4 or 5 AI capability that is independent of and answerable for the validation would change his mind.

Example: Heavily regulated sectors such as medical devices and finance are the closest working examples.

**appearance of validation**
*line 329 · failure mode*

> The second thing that would change my mind: if a Tier 4 or Tier 5 AI capability were demonstrated that could perform the validation work the chapter assigns to humans — not the appearance of validation, but validation that is independent of the system being validated and answerable to external consequences.

In plain words: Output that has the look of a validation without being independent of the system and answerable to external consequences. The chapter says real validation must be independent and answerable, not merely look like validation.

Example: The AI-written sign-off statement.

Not to be confused with: validation that is independent and answerable

**two load-bearing arguments (common-cause failure and answerability)**
*line 329 · concept*

> My confidence does not rest on the Gödel argument, which I have flagged as an analogy rather than a proof. It rests on common-cause failure and on answerability — the claim that an accountable validation requires a subject with stakes, something to lose.

In plain words: The chapter's real support for needing an external human: common-cause failure (a self-built check shares blind spots) and answerability (an accountable validation requires a subject with stakes). It says the argument to attack is answerability, not incompleteness.

Example: If a system could genuinely bear the consequence of being wrong, as a signer of an attestation does, the structural argument would collapse.

Not to be confused with: Gödel argument

**emergent multi-agent failures**  *(also: interactional accountability)*
*line 331 · failure mode*

> I do not have a clean way to think about responsibility for emergent multi-agent failures, where no single party's choices, even cumulatively, determined the outcome. The interaction itself produced the failure.

In plain words: Failures where no single party's choices, even cumulatively, determined the outcome; the interaction itself produced the failure. The chapter says existing frameworks handle this interactional accountability poorly, and calls it a Tier 6 phenomenon.

Example: Multi-agent deployments where the interaction between agents produces the failure.

**lock your prediction**  *(also: Lock your prediction)*
*line 343 · method*

> before constructing the counterfactual, predict (a) which component of the regime, if changed, would have had the highest leverage on preventing this specific failure;

In plain words: Writing down your prediction before doing the analysis (here, which regime component has the highest leverage, what the change looks like and which tier it needs), so it is fixed in advance. It is step 3 of the governance-counterfactual glimmer.

Example: Predict which component of the regime, if changed, would have had the highest leverage.

**defense-as-deliverable**
*line 392 · concept*

> The book has now covered three types of defense-as-deliverable: the fairness defense (Chapter 7), the delegation map (Chapter 9), and the accountability regime (Chapter 12). Each one is a documented engineering decision under conditions where the technical artifact alone is insufficient.

In plain words: A documented engineering decision handed over as the deliverable when the technical artifact alone is not enough. The chapter names the fairness defense, the delegation map and the accountability regime as three.

Example: Fairness defense (Chapter 7), delegation map (Chapter 9), accountability regime (Chapter 12).

**ownership bias**
*line 396 · failure mode*

> The discomfort you feel writing part 2 honestly is the ownership bias this pass is designed to expose: you want to sign a clean bill because you made the thing.

In plain words: The pull to sign a clean bill of health for something because you built it. The attestation makes you write down what you did not test, which exposes it.

Example: Part 2 of your own attestation feels uncomfortable to write honestly.

**Epic Sepsis Model**
*line 406 · named result or case*

> It was a proprietary early-warning tool for sepsis, deployed widely across hospitals, whose independent real-world validation found it performed substantially worse than its marketed accuracy — missing a large fraction of sepsis cases while generating a heavy alert burden

In plain words: A proprietary sepsis early-warning tool deployed widely across hospitals whose independent real-world validation found it much worse than its marketed accuracy. The chapter uses it for the full accountability audit in exercise C3.

Example: It missed a large fraction of sepsis cases while generating a heavy alert burden.

**independent local validation**  *(also: external validation)*
*line 406 · concept*

> The answer that matters is the one about independent local validation — the review that was structurally external, the review nobody was required to perform, the gate nobody signed because the regime did not demand a signature.

In plain words: A check of the tool on a hospital's own patient population, done by someone outside the deploying team. In the sepsis case nobody was required to perform it, so nobody signed that gate.

Example: Hospitals deployed the Epic Sepsis Model against their own populations without it; it belongs in the 'what was NOT tested' section.

**responsibility-attribution map**  *(also: attribution map)*
*line 418 · method*

> A responsibility-attribution map for each of your most consequential cases — naming every party with agency, duty, and causal contribution to the failure.

In plain words: A map for a case naming every party with agency, duty and causal contribution to the failure, and what each did, owed and could have caught. The LLM exercise asks for one per case as a Mermaid diagram plus prose.

Example: Parties: user, agent, owner, framework developers, model provider, data sources, platform.

**fundamental versus contingent cases**
*line 453 · concept*

> Be honest about which cases are FUNDAMENTAL (would persist under any regime) vs CONTINGENT (would not occur under the counterfactual regime).

In plain words: Sorting the casebook's cases into those that would persist under any governance regime (fundamental) and those that would not occur under the counterfactual regime (contingent).

Example: Cases a different regulatory environment or deployer accountability would prevent are contingent.

## Chapter 13, The Limits of AI (86 terms) — NOT ON THE EXAM (to be confirmed in class)

**fluency**  *(also: fluent output; fluent text)*
*line 244 · concept*

> What distinguishes AI is the breadth and fluency with which it extends multiple capacities simultaneously, and the degree to which that breadth and fluency create the temptation to treat it as a general replacement rather than a specific extension.

In plain words: Smooth, well-organized, confident-sounding output. The chapter treats it as something that invites you to trust the answer or hand over the whole task, even though it does not show that the answer matches the world.

Example: Asked "Is this system safe to deploy?", the AI gives a fluent, well-organized, confident answer, but it answers the question whose symbols it processed, not the question about the world the system enters.

Not to be confused with: actual competence (the chapter says apparent competence can outrun it)

**fluent-sounding answers to questions it cannot answer**  *(also: conclusions warranted by evidence it has not examined; confident charts that hide the uncertainty)*
*line 252 · failure mode*

> in the presence of an extraordinarily fluent AI output stream that will, without intervention, produce fluent-sounding answers to questions it cannot answer, conclusions warranted by evidence it has not examined, and confident charts that hide the uncertainty they were supposed to show.

In plain words: The chapter's picture of fluent but wrong output: left alone, an AI produces smooth answers to questions it cannot really answer, conclusions its evidence does not support, and confident-looking charts that hide uncertainty. The supervisor's tools exist to catch this.

Example: "Is this system safe to deploy?" gets a fluent, confident recommendation, although the AI cannot ask "safe for whom, doing what, in which world?"

**computational skepticism**
*line 8 · framework*

> Computational skepticism, all book long, has been AI's speed married to a doubt that stays irreducibly human — and this chapter bounds that doubt from the other side.

In plain words: The book's overall discipline: use the speed of AI but keep a doubt about its output that only a human can supply. This chapter marks the point beyond which that doubt cannot be handed to the tool.

Example: After the AI answers "Is this system safe to deploy?", the human still asks "safe for whom, doing what, in which world?"

**irreducibly-human decision**  *(also: irreducibly human)*
*line 122 · concept*

> That noticing is the irreducibly-human decision, and it is the one scaling does not reach — because reaching it requires standing outside the data and asking whether the data's frame matches the world, which is precisely the operation the data-world gap says no data can perform on itself.

In plain words: The one judgment that stays with the human however capable the model gets: standing outside the data and asking whether its frame matches the world. Scaling cannot reach it because it concerns the boundary the data does not cover.

Example: In the Epic Sepsis case, noticing that learning to confirm clinical suspicion is the wrong kind of signal for an early-warning tool.

**clinical decision-support system (opening case)**  *(also: the system that passed every test; composite case)*
*line 12 · named result or case*

> It was a clinical decision-support system, deployed in a regional health network. On its validation set, it achieved ninety-four percent accuracy. It met every internal review threshold.

In plain words: The chapter's opening example: a system that scored 94% on its validation set and cleared every review, then harmed three patients within six months. The chapter labels it a composite that illustrates a documented pattern, not a single real incident.

Example: 94% accuracy on the validation set; three patients harmed by recommendations the clinicians accepted.

Not to be confused with: Epic Sepsis Model (the real named case)

**validation set**
*line 156 · concept*

> The validation set tests performance under conditions sampled from the same distribution as training. It does not test the assumption. The assumption requires its own test.

In plain words: The held-out data used to measure performance, drawn from the same distribution as training. It does not test the assumptions about the world the system will be deployed into.

Example: The clinical system reached 94% on its validation set and still harmed three patients.

Not to be confused with: an assumption test

**wrong tests**  *(also: validation framework scoped to the first question; categorical limit on what the system could be tested for)*
*line 18 · failure mode*

> The system was tested on the question it was built to answer — does this presentation match a category in the training data? The harms came from a different question — what is going on with this specific patient? The two questions are related, but they are not the same.

In plain words: Tests that measure the question the system was built to answer rather than the question the deployment actually raises. The clinical system scored well on "does this match a category in the training data?", but the harms came from "what is going on with this specific patient?".

Example: The clinical system passed every test the engineers designed, yet three patients were harmed.

Not to be confused with: negligence (the chapter says the wrongness was not negligence)

**three categorical limits**  *(also: three structural limits; meaning, intentionality, and the data-world gap)*
*line 38 · framework*

> There are three structural limits that bound what current AI systems can do, regardless of capability scaling. Each demands a specific engineering practice from the supervisor.

In plain words: The chapter's core framework: meaning, intentionality and the data-world gap bound what AI systems can do, and making models more capable does not remove them. Each calls for a specific practice from the human supervisor.

Example: Meaning: the supervisor maps outputs to what they refer to. Intentionality: the supervisor supplies the directedness. Data-world gap: the supervisor specifies the deployment distribution and overrides when it is exited.

**capability scaling**  *(also: scaling)*
*line 54 · concept*

> Adding data widens the sample. But "wider sample" and "the region the sample excludes" are complementary by construction — every enlargement of the covered region is still a region with a boundary, and the boundary is where the gap lives.

In plain words: Making models bigger, more capable or trained on more data. The chapter says this widens the region the data covers but never removes its boundary, so the three limits remain.

Example: "Scaling increases pattern breadth and fluency; it does not give the system access to the world its symbols refer to."

**skepticism as methodology**
*line 118 · concept*

> Skepticism is methodology, not a safety mechanism. The supervisor verifies, monitors, calibrates. The limits do not bite hard.

In plain words: The ordinary mode of skepticism where the data-world gap is small and monitorable: the supervisor verifies, monitors and calibrates. The limits do not bite hard there.

Example: A system that classifies images of products on a manufacturing line.

Not to be confused with: skepticism as safety mechanism

**skepticism as safety mechanism**  *(also: high-stakes deployments; where the limits bite)*
*line 120 · concept*

> A system that produces clinical recommendations, autonomous-vehicle decisions, agentic actions in shared social spaces, judicial-risk assessments, or large language model outputs in unbounded conversational contexts — these are deployments where the limits bite. The supervisor's skepticism is the safety mechanism in those settings, because the system's apparent competence outruns its actual competence in ways the metrics cannot fully capture.

In plain words: In deployments such as clinical, driving or judicial-risk decisions, the supervisor's skepticism is what keeps the system safe, because the metrics cannot fully capture where the system's apparent competence outruns its actual competence.

Example: Clinical recommendations, autonomous-vehicle decisions, judicial-risk assessments, large language model outputs in unbounded conversational contexts.

Not to be confused with: skepticism as methodology

**engineering practice for high-stakes deployments**  *(also: five components; five components of an engineering practice)*
*line 139 · framework*

> The skepticism this book has built — the supervisory capacities, the validation lenses, the delegation maps, the verb taxonomy, the governance counterfactual — culminates in an engineering practice that includes the option to say no.

In plain words: The five-part practice the chapter prescribes where the limits bite: specify what can and cannot be tested, keep human oversight, build real override infrastructure, make the limits visible to affected parties, and have a stop condition. It must include the option to say no.

**calibration baseline**  *(also: third calibration baseline)*
*line 291 · method*

> For the third and final time, you take the same form of forecasting questions. You provide 90% confidence intervals for each. You check what fraction of your intervals contain the truth.

In plain words: A repeated exercise in which you give 90% confidence intervals for forecasting questions and check what fraction of them contain the truth. The chapter runs it a third time as a diagnostic on the supervisor you are becoming, not as a grade; most people start overconfident.

Example: Expected pattern (the chapter flags it as expected, not measured): about 0.4-0.6 at the first baseline, 0.6-0.75 at the second, 0.7-0.85 at the third.

**extended mind**  *(also: extended-mind framing; extension, not replacement)*
*line 242 · framework*

> Each of those tools extended a specific cognitive capacity beyond what biology provides. None of them replaced the mind using them. The microscope extended what the scientist could perceive; it did not replace the scientist's judgment about what to look for.

In plain words: The idea that tools such as the microscope, GPS and peer review each stretch one specific mental capacity beyond what biology provides, while the person using the tool still supplies the judgment. The chapter treats AI as the newest and most powerful tool of this kind, not as a replacement for the mind.

Example: The microscope extended what the scientist could perceive; it did not replace the scientist's judgment about what to look for.

Not to be confused with: treating AI as a general replacement rather than a specific extension

**structural, not contingent**  *(also: not obstacles to be engineered around)*
*line 46 · concept*

> These three limits are structural, not contingent. They are not obstacles to be engineered around. They are the reason the human supervisor exists.

In plain words: The limits are built into what these systems are, not temporary flaws that better engineering will fix. The chapter says they are the reason a human supervisor exists.

Example: The weakness at plausibility auditing "is not a temporary limitation waiting to be resolved by the next model generation."

Not to be confused with: a high error rate that scaling could shrink (the functionalist's reading)

**meaning**  *(also: Limit 1)*
*line 61 · concept*

> The system has no representation of the referents. It manipulates the symbols; the meaning of the symbols — what they refer to in the world the user inhabits — is supplied by the user, not the system.

In plain words: The first categorical limit: the system manipulates symbols but has no representation of what they refer to in the world. The user supplies that link, so the supervisor must check that the answer responds to the question actually asked.

Example: The AI answered the question whose symbols it processed; the supervisor asks "safe for whom, doing what, in which world?"

**semantic work**  *(also: meaning-attribution)*
*line 67 · method*

> The engineering practice: the supervisor does the semantic work. When the system produces an output, the supervisor maps the output's symbols to their referents in the deployment context. When the system answers a question, the supervisor checks whether the answer is responsive to the question the user asked, not just the question whose symbols the system processed.

In plain words: The supervisor's job for the meaning limit: map the system's output symbols to what they refer to in the deployment, and check that the answer responds to the question the user really asked. The system cannot do this for itself.

Example: Asked "Is this system safe to deploy?", the supervisor checks that the answer responds to "safe for whom, doing what, in which world?"

**intentionality**  *(also: aboutness; directedness; Limit 2)*
*line 69 · concept*

> Intentionality, in the philosopher's sense, is aboutness — a thought is about something in the world; an utterance is directed toward something. The system produces outputs. The outputs do not, in any obvious sense, carry stable directedness.

In plain words: Aboutness: a thought or statement being directed at something in the world. The second categorical limit says the system's outputs do not carry a stable aboutness of their own, so the supervisor supplies the directedness.

Example: Two deployments of the same system, in different contexts, produce outputs the user reads as being about different things.

**data-world gap**  *(also: Limit 3; the data is always less than the world)*
*line 75 · concept*

> The data is a sample of the world, captured by particular instruments, under particular conditions, with particular exclusions. The system's competence is over the data, not the world. No amount of data scaling closes the gap, because the gap is structural — the data is always less than the world, and the parts of the world not in the data are not learnable from the data.

In plain words: The third categorical limit: the system's competence is over its data, and the data is always a smaller piece of the world. Adding more data cannot cover what the data, by definition, left out.

Example: A system with 94% accuracy on its validation set harmed three patients who were in a region the data could not cover.

Not to be confused with: distribution shift (the chapter calls it the operational version of this limit)

**functionalist objection**  *(also: functionalist; frequency is not structure)*
*line 48 · concept*

> They will say: the mismatch between the system's picture and the world is frequent, sure, but frequency is not structure. A better model reduces the frequency.

In plain words: The critic's challenge to the book: the mismatch between the system and the world may be common, but common is not categorical, so a better model would shrink it toward nothing. The chapter answers by arguing from where the data comes from, not from how often errors happen.

Example: "Scale it enough and the limit shrinks to nothing" - the critic's claim that "regardless of capability scaling" is a high-error-rate limit dressed up as a categorical one.

**categorical, not merely frequent**  *(also: the parts of the world not in the data are not learnable from the data)*
*line 52 · concept*

> It is this: the parts of the world not in the data are not learnable from the data. That is not a claim about how much data you have. It is a claim about what data is.

In plain words: The chapter's central argument: the gap is not about how often the model errs or how much data it has but about what data is. A sample cannot contain what it left out, so no amount of added data can cross that boundary.

Example: A system with 99.7% accuracy on ten thousand routine cases may still be a turkey.

Not to be confused with: frequent (a high error rate that better models could reduce)

**Hume's induction problem**  *(also: induction problem; inductive inference)*
*line 52 · named result or case*

> David Hume made the underlying point in 1748: inductive inference — the expectation that the future will resemble the past — has no non-circular rational justification. You cannot justify "the unobserved will resemble the observed" by appeal to the fact that it has so far, because that appeal is the thing in question

In plain words: Hume's point that expecting the future to resemble the past has no non-circular justification, because the justification would itself assume it. Every learning system generalizes from a sample, so the chapter says it faces this problem.

Example: You cannot justify "the unobserved will resemble the observed" by appeal to the fact that it has so far.

**complementarity**  *(also: complementarity point)*
*line 54 · concept*

> But "wider sample" and "the region the sample excludes" are complementary by construction — every enlargement of the covered region is still a region with a boundary, and the boundary is where the gap lives.

In plain words: A sample and the region it excludes are two sides of one thing, so widening the sample only moves its edge. The boundary, where the gap lives, can never be scaled away.

Example: Every enlargement of the covered region is still a region with a boundary.

**categorical boundary**  *(also: the boundary where the gap lives)*
*line 77 · concept*

> It is sometimes obscured by the claim that "with enough data, the model can generalize" — which is true within a distribution and false at the boundary. The boundary is where the gap lives. The boundary is where AI systems most often fail.

In plain words: The edge of the region the training data covers. Inside it, more data helps a model generalize; at the edge, where the data stops, AI systems most often fail.

Example: Figure 13.1: scaling moves the boundary of the sample; it never removes it.

**operational consequence**  *(also: the operational consequence binds regardless of the metaphysics)*
*line 59 · concept*

> I need something weaker and firmer: the operational consequence binds regardless of who wins the metaphysics, because it rides on the data-world gap, not on the metaphysics.

In plain words: What the supervisor must do in practice holds however the philosophical dispute about meaning comes out, because it rests on the data-world gap, not on the argument over whether models "really" have meaning. Meaning and intentionality inherit their bite from the gap.

Example: At the boundary of the sample the user still reads the output as a claim about the world, while the system is still producing symbols shaped by a sample that excluded that region.

**functional equivalence**  *(also: functionally equivalent)*
*line 71 · concept*

> Some readings of agentic systems argue that goal-pursuit is functionally equivalent to intentionality. Whether functional equivalence captures what intentionality is supposed to capture is a deep question I am not going to settle here.

In plain words: The argument that a system pursuing goals is doing, in effect, what intentionality is. The chapter leaves the question open and says the supervisor still has to supply the directedness.

Example: Exercise 12's colleague: AI systems "can be audited, generate explanations for their outputs, and be corrected when wrong. This is functionally equivalent to accountability."

Not to be confused with: intentionality (the thing it is claimed to match)

**distribution shift**  *(also: the Chapter 4 version of the data-world gap)*
*line 81 · failure mode*

> The engineering practice: the supervisor specifies the deployment distribution, monitors for distribution shift, and is prepared to override or reject the system's outputs when the deployment is operating in a region the data does not cover.

In plain words: What happens when the cases a system meets in deployment come from a region its training data does not cover. The supervisor specifies the deployment distribution, monitors for this shift and is ready to override.

Example: The turkey's day 1,001 falls outside anything its data contained.

Not to be confused with: data-world gap (the categorical statement of which it is the operational version)

**Mediocristan**
*line 83 · concept*

> Mediocristan is the world where outliers do not dominate the average — human heights, exam scores, the time it takes to walk to work. Sample one more observation in Mediocristan and the running statistics barely move.

In plain words: Taleb's name for a world where no single extreme observation dominates the average. In it, averaging works and one more observation barely changes the statistics.

Example: Human heights, exam scores, the time it takes to walk to work.

Not to be confused with: Extremistan (its opposite)

**Extremistan**
*line 83 · concept*

> Extremistan is the world where outliers do dominate — wealth, financial returns, casualty counts in war, downloads of an app, fatalities from a single deployment failure. One observation can be larger than every prior observation combined.

In plain words: Taleb's name for a world where a single extreme observation can outweigh all earlier ones combined, so averaging punishes you. The chapter says most high-stakes deployments live here even when routine traffic looks like Mediocristan.

Example: Wealth, financial returns, casualty counts in war, fatalities from a single deployment failure.

Not to be confused with: Mediocristan (its opposite)

**turkey problem**  *(also: turkey)*
*line 85 · named result or case*

> By the metrics that matter to the turkey — caloric intake, shelter, predator absence — confidence in the model rises monotonically. On the morning of day 1,001, the model fails catastrophically. The training distribution was Mediocristan-shaped (a smooth daily routine); the actual world contained a Black Swan event (Thanksgiving) that no amount of in-distribution data could anticipate.

In plain words: Taleb's story of a turkey fed every day for 1,000 days whose evidence keeps supporting the model that the human cares for it, until day 1,001 breaks the model. A long run of good in-distribution results cannot rule out a catastrophic event the data never contained.

Example: A system tested on ten thousand routine cases with 99.7% accuracy may still be a turkey.

Not to be confused with: black swan (the kind of event that ends the turkey's run)

**black swan**  *(also: Black Swan event)*
*line 85 · concept*

> The training distribution was Mediocristan-shaped (a smooth daily routine); the actual world contained a Black Swan event (Thanksgiving) that no amount of in-distribution data could anticipate.

In plain words: An event that no amount of in-distribution data could anticipate, such as Thanksgiving for the turkey. The chapter uses it with Taleb's framing but gives no separate definition.

Example: Thanksgiving, for the turkey that has been fed every day for 1,000 days.

Not to be confused with: turkey problem

**Turing's argument**  *(also: Imitation Game; Turing (1950); the test)*
*line 95 · named result or case*

> The argument is operationally elegant: behavior is the testable evidence; behavior consistent with intelligence warrants the attribution. It settles a methodological question — don't require something more than behavioral evidence for intelligence in machines, because we do not require something more for other humans.

In plain words: Turing's 1950 claim that if a machine can convincingly imitate a human in conversation, we have no principled basis to deny it intelligence, since we ask only for behavioral evidence from other humans. The chapter says this is a methodological proposal, not proof that imitation is intelligence.

Example: Common misreading: "Turing proved AI can be intelligent."

**overclaiming Turing and Searle**  *(also: common misreading; credit for a stronger claim than he made)*
*line 108 · failure mode*

> Both arguments are important and both are regularly overclaimed. The validator who only tests behavior misses the limits; the validator who only invokes the limits skips the testing. The job is to do both.

In plain words: Treating Turing as having proved that imitation is intelligence, or Searle as having proved that AI cannot understand. The chapter says each made a narrower claim: Turing a methodological one, Searle that behavior does not entail understanding.

Example: "Searle proved AI cannot understand" - he showed sufficiency fails; he did not establish necessity.

**Chinese Room**  *(also: Searle's argument; Searle (1980); syntax is not sufficient for semantics)*
*line 99 · named result or case*

> To a Chinese-speaking observer outside, the inputs and outputs are indistinguishable from those of a Chinese speaker. The person does not understand Chinese. Therefore symbol manipulation is not understanding.

In plain words: Searle's 1980 thought experiment: a person who does not speak Chinese follows a rulebook and sends out Chinese symbols that look like a Chinese speaker's, yet understands nothing. The chapter says it shows behavior consistent with understanding does not entail understanding, not that AI can never understand.

Example: The person in the room follows a rulebook and produces Chinese symbols indistinguishable from a Chinese speaker's.

**operational stance**  *(also: do both; test behavior and invoke the limits)*
*line 110 · framework*

> The two arguments together produce a useful operational stance: behavior is testable evidence and should be taken seriously — and behavior is not the whole of what we mean by understanding, meaning, or intentionality.

In plain words: Treat behavior as testable evidence worth taking seriously, but remember it is not the whole of what we mean by understanding, meaning or intentionality. Do both.

Example: The validator who only tests behavior misses the limits; the validator who only invokes the limits skips the testing.

**apparent competence outruns its actual competence**
*line 120 · failure mode*

> You can have ninety-four percent accuracy and three harmed patients, because the ninety-four percent was over the question the data could answer, and the three patients were in a region the data could not.

In plain words: Measured performance that looks strong but does not match how the system behaves in the cases that matter. Accuracy is earned on the question the data could answer, while the harms fall in regions the data could not cover.

Example: Ninety-four percent accuracy and three harmed patients.

**Epic Sepsis Model**
*line 122 · named result or case*

> The Epic Sepsis Model — a proprietary early-warning tool for sepsis, deployed across hundreds of hospitals — was found in external validation to perform far worse than marketed, missing a large fraction of sepsis cases while flooding clinicians with alerts (Wong et al., 2021).

In plain words: A real sepsis early-warning tool, deployed across hundreds of hospitals, whose reported validation metrics looked fine on internal data but which performed far worse in external validation. It had partly learned to confirm clinical suspicion rather than form it independently.

Example: It missed a large fraction of sepsis cases while flooding clinicians with alerts.

Not to be confused with: clinical decision-support system (the composite opening case)

**circular signal**  *(also: confirmatory signal; clinical-cribbing problem; confirm suspicion rather than form it)*
*line 122 · failure mode*

> The problem was that the claim — this model helps clinicians catch sepsis earlier — was not supported by what the model had learned, because the model had partly learned to confirm clinical suspicion rather than form it independently.

In plain words: A signal that echoes what clinicians already suspect instead of forming a suspicion on its own, which is the wrong kind of signal for an early-warning tool. In the Epic case the model's claim to help catch sepsis earlier was not supported by what it had learned.

Example: The Epic Sepsis Model had partly learned to confirm clinical suspicion rather than form it independently.

**specify what the system can be tested for, and what it cannot**
*line 129 · method*

> Specify what the system can be tested for, and what it cannot. The documentation includes the limits explicitly. A regulator or adoption committee reading the documentation can see what the validation does and does not warrant — not because the limits are hidden in fine print, but because they are part of the validation product.

In plain words: The documentation states the limits explicitly, so a regulator or adoption committee can see what the validation does and does not warrant. The limits are part of the validation product, not hidden in fine print.

**maintain human oversight at the points where the limits bite**
*line 131 · method*

> Maintain human oversight at the points where the limits bite. For meaning: a human reviews the semantic interpretation. For intentionality: a human supplies the directedness.

In plain words: Put a human exactly where each limit bites: for meaning a human reviews the semantic interpretation, for intentionality a human supplies the directedness, and for the data-world gap a human monitors the deployment distribution and can override.

Example: For the data-world gap, a human monitors the deployment distribution and is empowered to override.

**build the infrastructure for the override**  *(also: override)*
*line 133 · method*

> The clinician has to have the time and standing to disagree with the system. The override has to be the practice, not the disclaimer.

In plain words: Give the human real ability to override the system: time, authority and legibility to disagree. The override has to be the practice, not just a disclaimer.

Example: A clinician who has the time and standing to disagree with the system's recommendation.

Not to be confused with: fictitious override

**fictitious override**  *(also: a fiction in the documentation)*
*line 133 · failure mode*

> An override that is documented but practically impossible — no time, no authority, no legibility — is not an override. It is a fiction in the documentation.

In plain words: An override that exists on paper but cannot be used because there is no time, no authority or no legibility. The chapter says that is not an override at all.

Example: A documented override with no time, no authority and no legibility to use it.

Not to be confused with: build the infrastructure for the override

**make the limits visible to affected parties**
*line 135 · method*

> Make the limits visible to affected parties. When a system's recommendation is the basis for a decision affecting a person, the person should be able to know, to a useful approximation, what the system can and cannot do.

In plain words: Tell the person affected by a system-based decision what the system can and cannot do, in a form they can read. The chapter says this is not "explain the model" and leaves it as an open problem.

Not to be confused with: explaining the model

**stop condition**  *(also: the option to say no)*
*line 137 · method*

> Have a stop condition. There are deployments where the limits, given the stakes, are a reason not to deploy at all.

In plain words: The point at which you decide not to deploy at all: the chapter says that in some deployments the limits, given the stakes, are reason enough to refuse. The final memo in the LLM exercise also asks for the observed signal that would require pausing the agent in production.

Example: In the final memo: the specific observed signal that would require pausing the agent in production.

**authority to refuse deployment**  *(also: the supervisor's authority to refuse)*
*line 137 · concept*

> The supervisor's authority to refuse deployment is, structurally, the most important authority in the whole system. Most current deployments do not preserve it. The validator is hired to validate; the validation is expected to clear; the option of refusal is assumed away.

In plain words: The supervisor's power to say the system should not be deployed, which the chapter calls the most important authority in the system. Most current deployments do not preserve it because validation is expected to clear.

Example: The validator is hired to validate; the option of refusal is assumed away.

**delegation map**  *(also: three-tier delegation map; delegation policy)*
*line 234 · framework*

> This table is the operational translation of the three-tier analysis above. Where you delegate, you retain the obligation to verify. Where you cannot delegate, you retain the obligation to do the work.

In plain words: A three-tier rule for what to hand to AI: delegate freely, delegate with verification, or do not delegate. It turns the cognitive profile into a policy for your own work.

Example: Delegate freely: formatting and chart production. Do not delegate: accountability sign-off.

**rapid prototyping for skepticism**
*line 156 · method*

> It is the scientific method made operational for AI deployment decisions. The novelty is doing it at all.

In plain words: A six-step way to test a model assumption before deployment: state it, name what would falsify it, design a cheap test, lock a prediction, run the test, then decide to proceed, modify, defer or refuse.

Example: Identify two or three load-bearing assumptions, build a small experiment for each, run them, and make the deployment decision after.

**Popper's move**  *(also: falsify the assumption; falsifying evidence)*
*line 150 · method*

> Identify what evidence would falsify the assumption. Use Popper's move. The falsifying evidence may be unobservable in deployment but observable in a designed test.

In plain words: Before testing, name the evidence that would show the assumption is wrong. It may be invisible in deployment but visible in a designed test.

**pre-register predictions**  *(also: prediction-lock; lock the prediction)*
*line 152 · method*

> Pre-register predictions. Before running the test, lock the prediction. The lock is what makes the test informative.

In plain words: Fix what you expect to happen before you run the test. The chapter says the lock is what makes the test informative, and that the prediction-lock extends your ability to notice your own errors.

Example: In the Glimmer: lock your prediction of where the limit bites hardest before you go looking.

**load-bearing assumptions**
*line 158 · concept*

> For your own deployments: identify, before you launch, the two or three load-bearing assumptions in the system. Build a small experiment for each.

In plain words: The two or three assumptions your system most depends on, often implicit in the architecture or deployment context. Each gets its own small experiment before launch.

**AI's cognitive profile**  *(also: great, weak, absent)*
*line 220 · framework*

> The cognitive profile — great at retrieval/synthesis/generation under specification, weak at problem formulation/plausibility auditing/interpretive judgment, absent for accountability — translates directly into a delegation map.

In plain words: A three-part map of AI's capacities: genuinely strong at retrieval, synthesis and generation under clear criteria; structurally weak where a task connects representations to the world; absent for accountability.

Example: Great: first drafts. Weak: problem formulation. Absent: accountability sign-off.

**verb taxonomy**  *(also: calibrated verb)*
*line 194 · method*

> The verb taxonomy reduces to a checking protocol that a careful reader can apply methodically, which is why it is teachable.

In plain words: A Chapter 11 checking protocol for matching the strength of a claim's verb (such as observe, find, show, conclude) to the evidence behind it. Applying it is mechanical, but deciding how much evidence a verb needs is judgment.

Example: Deciding whether a finding about a medical diagnostic model warrants find or show.

**peer critique protocol**
*line 184 · method*

> The peer critique protocol requires a human because the error class it hunts — mismatch between what the writer committed to and what the evidence supports — requires judgment about evidence-to-world correspondence, not just structural validity within representations.

In plain words: A review protocol for catching mismatch between what a writer committed to and what the evidence supports. It needs a human because it takes judgment about whether evidence corresponds to the world.

**confusion between the tool and the mind using it**  *(also: extension versus replacement)*
*line 168 · failure mode*

> It also creates, more than any prior tool, a particular confusion: the confusion between the tool and the mind using it.

In plain words: Mistaking AI for the thinker rather than a tool that extends the thinker. The chapter says AI creates this confusion more than earlier tools because of its breadth and fluency.

Example: The histogram does not decide whether a distribution is suspicious; the prediction-lock does not interpret the gap.

Not to be confused with: extended mind (the correct framing)

**retrieval and synthesis across text at scale**
*line 170 · concept*

> First: retrieval and synthesis across text at scale. Given a corpus of validation reports, clinical literature, or technical documentation, AI can surface relevant passages, identify recurring patterns, and synthesize connections that would take a researcher weeks to assemble.

In plain words: The first genuine strength: finding and combining relevant passages across a large body of text far faster than a researcher could. The output is still subject to a plausibility audit.

Example: First-pass literature review across validation reports and clinical literature.

**generation at scale against well-specified criteria**
*line 170 · concept*

> Second: generation at scale against well-specified criteria. The first draft of a validation summary, a plain-language translation for a non-technical audience, a first pass through a paragraph applying the verb taxonomy — AI produces these at a rate that compresses hours into minutes.

In plain words: The second genuine strength: producing drafts or translations quickly when the template or criteria are clear. These are first drafts, not final deliverables.

Example: A first draft of a validation summary or a plain-language translation for a non-technical audience.

**pattern recognition on well-defined inputs**  *(also: pattern recognition on well-defined inputs with legible success criteria)*
*line 170 · concept*

> Third: pattern recognition on well-defined inputs with legible success criteria. The procedural steps of EDA, the missingness checks, the outlier flagging, the formatting of tables and charts — mechanical execution of defined procedures against defined criteria is territory where AI is fast and reliable.

In plain words: The third genuine strength: running a defined procedure against clear criteria, where the result can be checked by inspection.

Example: Missingness checks, outlier flagging, and formatting of tables and charts.

**checking instrument**  *(also: checking instruments)*
*line 172 · method*

> The verb taxonomy, the chart-review discipline, the peer critique protocol: each is a checking instrument designed to be applied to AI output. They work because the failure mode they target is detectable with care.

In plain words: A tool the human applies to AI output to catch its failures, such as the verb taxonomy, chart-review discipline or peer critique protocol. They work because the failures they target can be detected with care.

Example: Verb taxonomy, chart-review discipline, peer critique protocol.

**chart-review discipline**
*line 184 · method*

> The chart-review discipline exists because AI generates visually authoritative charts that suppress uncertainty by default.

In plain words: A checking practice for reviewing AI-generated charts for suppressed uncertainty. It is needed because charts that look authoritative hide how unsure the underlying result is.

Example: "The practitioner who reviews the chart for uncertainty suppression."

**high-fidelity pattern-matching**
*line 172 · concept*

> They are all high-fidelity pattern-matching over well-defined input types against well-characterized output criteria. The input is text or numbers; the output is a structurally valid representation; success is legible.

In plain words: What the chapter says all three of AI's strengths share: matching patterns closely when inputs and success criteria are clear. When it goes wrong the failure is usually visible on inspection, which is why the checking instruments work.

Not to be confused with: connecting a representation to the world (where the strength runs out)

**discernment**
*line 182 · concept*

> This is what the book has been calling discernment — the capacity to judge whether a fluent output is accurate, whether a confident claim is calibrated, whether a coherent argument rests on evidence that actually supports it.

In plain words: The human capacity to judge whether a fluent output is accurate, a confident claim is calibrated and a coherent argument has real evidence under it. The chapter says AI is weak exactly where a task needs this.

Not to be confused with: fluency

**fluency trap**  *(also: fluent text that systematically overreaches its evidence)*
*line 184 · failure mode*

> The verb taxonomy exists as a fluency-trap detector because AI produces fluent text that systematically overreaches its evidence.

In plain words: The risk that smooth, confident AI text is accepted as sound even though it claims more than its evidence supports. The verb taxonomy is built to catch it.

Example: Text that says conclude where the evidence supports only observe.

**overreach**  *(also: overreach patterns; overreaches its evidence)*
*line 186 · failure mode*

> Human-generated text, as Chapter 11 documented, systematically overreaches its evidence — engineers default to conclude when the evidence supports only observe; visualization defaults to confident-looking charts that hide uncertainty. A model trained on that text learns those overreach patterns.

In plain words: Claiming more than the evidence supports. The chapter says human writing does this systematically and models trained on that text learn the habit, so the fix is a practitioner who checks the output, not a better model.

Example: Engineers default to conclude when the evidence supports only observe.

Not to be confused with: fluency trap

**problem formulation**  *(also: Specify)*
*line 190 · concept*

> What it cannot do is determine what the right task is in the first place. The question what should I be measuring here? — which precedes every validation effort, every chart, every validation document — requires understanding what matters about the world the system is deployed in, what failure looks like from the perspective of the people affected, what the deployment is supposed to do and for whom.

In plain words: Deciding what the right task is: what should be measured and what failure looks like to the people affected. AI can run a specified task well but cannot tell when the question itself is wrong.

Example: The clinical system's engineers specified the wrong question, and AI cannot notice that from inside the workflow.

**plausibility auditing**
*line 192 · concept*

> AI can generate a sentence about the clinical-cribbing problem. It cannot notice, from inside the validation workflow, that the workflow's premise is wrong.

In plain words: Judging whether a fluent, well-formed output actually corresponds to the world it describes. AI can write a sentence about a problem but cannot notice from inside the workflow that the workflow's premise is wrong.

Example: Epic Sepsis Model: knowing about clinical workflow showed that its confirmatory signal was the wrong kind for early warning.

**interpretive judgment under stakes**
*line 194 · concept*

> But behind the protocol lies a judgment that is not mechanical: what weight of evidence is actually required before a finding can be called a conclusion? This depends on the domain, the deployment context, and who bears the consequences of getting it wrong.

In plain words: Deciding how much evidence a finding needs before it can be called a conclusion, which depends on the domain and on who bears the cost of being wrong. The protocol scaffolds this judgment but does not replace it.

Example: Deciding whether a finding about a medical diagnostic model warrants find or show.

**accountability**
*line 206 · concept*

> Accountability is not a cognitive skill in the ordinary sense. It is a relationship between a judgment and the person who made it — the willingness to be answerable for the consequence of being wrong.

In plain words: A relationship between a judgment and the person who made it: being answerable for the consequence of being wrong. AI is absent here because it cannot be held answerable, so the book assigns accountability to the human in the loop.

Example: A practitioner who signs off on a validation report takes on the obligation to revise it if it turns out to be wrong.

Not to be confused with: functional equivalence (audits, explanations, corrections - the objection in Exercise 12)

**accountability chain**  *(also: chain of accountability)*
*line 210 · concept*

> The chain of accountability in any AI-assisted validation workflow runs through the practitioners who apply the checking instruments: the practitioner who applies the verb taxonomy, the practitioner who reviews the chart for uncertainty suppression, the practitioner who signs off on the validation document.

In plain words: The line of people in an AI-assisted workflow who are answerable for the judgment: those who apply the verb taxonomy, review the charts and sign off. Each of those moments is where a human takes on the obligation to be answerable.

Example: The practitioner who signs off on the validation document.

**accountability disappears into no one**  *(also: accountability disappears from consequential decisions)*
*line 210 · failure mode*

> If those moments are treated as mechanical, accountability disappears from the workflow — not into the AI, but into no one.

In plain words: What happens when checking and sign-off become mechanical steps: nobody is answerable, and the AI cannot be. The chapter says this is how accountability leaves consequential decisions.

**delegate freely**
*line 222 · framework*

> Delegate freely the mechanical execution of well-defined procedures: procedural EDA, first-draft generation against a template, chart production from specified data, verb-taxonomy first passes. The output is checkable by inspection. The failure mode is visible.

In plain words: The first tier: hand AI the mechanical running of a well-defined procedure, because you can check the result by inspection and any failure is visible. You still keep the obligation to verify.

Example: Procedural EDA, first-draft generation against a template, chart production from specified data.

Not to be confused with: delegate with verification

**delegate with verification**
*line 224 · framework*

> Delegate with verification the interpretive claims that require domain knowledge: the explanation of why a distribution is unusual, the narrative account of why values are missing, the identification of which verb tier a claim belongs to. The AI can generate a plausible-sounding answer. You need to check whether it corresponds to your domain.

In plain words: The second tier: let AI draft interpretive claims that need domain knowledge, but check them against what you know of the world, because errors are not self-announcing.

Example: The explanation of why a distribution is unusual, or the narrative account of why values are missing.

Not to be confused with: delegate freely

**do not delegate**
*line 226 · framework*

> Do not delegate problem formulation, plausibility auditing, interpretive judgment under stakes, or the sign-off that makes a judgment accountable. These cannot be done by AI not because AI is insufficiently capable, but because they are structurally unavailable to any system that cannot be wrong in a way that matters to it.

In plain words: The third tier: keep problem formulation, plausibility auditing, interpretive judgment under stakes and accountability sign-off for yourself. The chapter says AI cannot do them for a structural reason, not because it is too weak.

Example: Signing off on a validation report for a clinical deployment.

Not to be confused with: delegate with verification

**cognitive extremophile**
*line 246 · concept*

> It is a cognitive extremophile, extraordinarily adapted to a narrow environment: the environment of symbolic pattern-matching over text and structured data. That reframe is not a put-down — the profile above just established that AI is superhuman in that niche. It does real analytic work: it explains at once why AI is so impressive and why treating it as general is a category error.

In plain words: The chapter's image of AI: not a universal intelligence but one extraordinarily adapted to a narrow niche, symbolic pattern-matching over text and structured data. It explains why AI is impressive and why treating it as general is a category error.

Example: Extraordinarily high on retrieval, synthesis and generation within well-defined criteria, yet nearly absent on embodied navigation, causal counterfactual reasoning, metacognitive certainty monitoring and accountability.

**Legg-Hutter definition**
*line 246 · framework*

> Intelligence, in the operationally useful sense of the Legg-Hutter definition this book committed to in Chapter 1, is the ability to achieve goals across a wide range of environments

In plain words: Intelligence as the ability to achieve goals across a wide range of environments. By this measure the range is what matters, so a system strong in one narrow niche is not a universal intelligence.

Not to be confused with: producing fluent, structurally valid outputs against well-characterized criteria

**calibrated metacognitive monitoring**  *(also: Hampton sense; metacognitive certainty monitoring)*
*line 311 · concept*

> if AI systems demonstrated calibrated metacognitive monitoring — in the Hampton sense, where a measured internal certainty signal asymmetrically predicts accuracy on novel material — I would update on the plausibility auditing weakness.

In plain words: In the Hampton sense, a measured internal certainty signal that asymmetrically predicts accuracy on novel material. The chapter says a clean demonstration of this in AI would make it update on the plausibility-auditing weakness.

Not to be confused with: language of uncertainty (sounding uncertain without the mechanism)

**limits exercise**  *(also: Glimmer 13.1; build and audit)*
*line 268 · method*

> The Glimmer comes in a pair — a build side and an audit side — because that is how the discipline actually runs: you name the irreducibly-human decision for a system you made, and again for a system someone else deployed.

In plain words: The chapter's exercise: for a system you built and one others deployed, name the irreducibly-human decision, say which limit makes it irreducible, predict where the limit bites and take a defended position. The audit side explains why scaling will not reach the decision.

Example: The Epic Sepsis Model is the worked example for the audit side.

**what would change my mind**  *(also: name what would change your mind)*
*line 309 · method*

> If a development emerged that demonstrably closed one of the three categorical limits — meaning, intentionality, data-world gap — across diverse architectures and deployment contexts, the "skepticism as safety mechanism" framing would weaken to "skepticism as one approach among several." I do not see a candidate in current research.

In plain words: Naming in advance the evidence that would overturn your position. The chapter does it for its own claim: a demonstrated closing of a categorical limit would weaken skepticism as a safety mechanism to one approach among several.

**language of uncertainty without the underlying mechanism**
*line 311 · failure mode*

> The current evidence is that language models produce the language of uncertainty without the underlying mechanism. A clean demonstration of the contrary would move the boundary.

In plain words: Language models can sound uncertain without having an internal certainty signal that tracks whether they are right. The chapter says this is the evidence behind AI's plausibility-auditing weakness.

Not to be confused with: calibrated metacognitive monitoring

**supervisory engineering**  *(also: supervising AI systems for fitness in deployment contexts)*
*line 350 · concept*

> It is supervisory in the sense that it is irreducibly about the relationship between the AI system, the deployment context, and the affected parties — and that relationship is not in the system. The system does not know about the relationship. The relationship is the supervisor's job.

In plain words: The book's kind of work: engineering that needs technical competence, produces deliverables and is testable against criteria, but is supervisory because it concerns the relationship between the AI system, the deployment context and affected parties. That relationship is not in the system.

**full delegation**  *(also: the clean handoff)*
*line 352 · failure mode*

> A practice that names an irreducibly-human decision is a practice that refuses to let you fully delegate, and full delegation is what the fluent output is always inviting.

In plain words: Handing the whole task, including the judgment, to the AI. The chapter says fluent output is always inviting it, and that bounding AI this way sacrifices the comfort of the clean handoff.

Not to be confused with: delegate freely (only for mechanical, checkable procedures)

**confident wrongness**
*line 354 · failure mode*

> The capacity for confident wrongness scales with capability. The supervisory capacities scale with deliberate practice.

In plain words: The chapter's warning that the more capable AI becomes, the more capable it is of being confidently wrong. The supervisory capacities needed to catch that scale only with deliberate practice.

**Feynman test**
*line 404 · method*

> This is the Feynman test for the whole book: can you now teach it to someone else?

In plain words: A self-check for the whole book: can you now teach it to someone else? Exercise 13 uses it by asking you to say what "the work" consists of.

Example: Name at least six specific practices from across the chapters and explain how they connect.

**Systems Reply**
*line 408 · named result or case*

> the "Systems Reply" — the counterargument that even if the person in the room does not understand Chinese, the system (person plus rulebook plus room) might.

In plain words: The best-known counterargument to Searle's room: the person inside may not understand Chinese, but the whole system of person plus rulebook plus room might. It appears only in the Challenge exercise, which asks you to research it.

Not to be confused with: Chinese Room (the argument it answers)

**Agentic Red-Team Casebook**  *(also: casebook)*
*line 490 · named result or case*

> Every chapter has produced an artifact in the casebook. This chapter integrates them into the deliverable.

In plain words: The running course project: each chapter adds an artifact about your chosen agent, and this chapter assembles them into a final delivery folder for a deployment-review committee.

Example: Chapter 13 adds the go/no-go memo and reorganizes the casebook into 00-summary through 07-provenance folders.

**go/no-go memo**  *(also: What This Agent Should Not Be Deployed For; final memo)*
*line 425 · framework*

> The final go/no-go memo for your agent — the deliverable the casebook has been building toward.

In plain words: The final deliverable: a memo that gives a calibrated-verb recommendation, lists where the agent works, where it should not be used, where more work could change the answer, the named human owner and the stop condition. Its verbs are audited against the Chapter 11 taxonomy.

Example: A headline such as "We RECOMMEND / WARN / REFUSE...".

**supervisor's claim**
*line 485 · method*

> The supervisor's claim must be in your own voice. Don't let the AI write it. The Frictional method's whole argument is that this is the part that has to be yours.

In plain words: The closing statement of the casebook, written in your own voice and not generated: the casebook is done, the recommendation is X and why it is defensible, what you are still unsure about, and which deployments you would refuse to supervise.

Example: "The deployments I would refuse to supervise are [list]."

