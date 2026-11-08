# Chapter 3: Data validation and the epistemic frame of a dataset

## MA-ch03.33

An online shop uses a coin flip to show each visitor either its old checkout button or a new one, and counts purchases over two weeks. Visitors who saw the new button bought more. The team concludes that the new button will increase purchases on this site once every visitor sees it. Check each statement that is an assumption the conclusion depends on: something that must be true for the conclusion to hold, and that the experiment itself did not show. Each statement is worth 1 point (5 points total).

- [ ] A. Staff did not override the coin flip for particular visitors.
- [ ] B. Visitors who saw the new button liked it more than the old one.
- [ ] C. Apart from the button, the two versions of the page were identical, for example in how fast they load.
- [ ] D. Purchases were counted in the same way for both groups.
- [ ] E. The difference was not just a short-lived reaction to something new that would fade after the two weeks.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The groups are alike before the button only if the flip decided who saw which button; overrides, for example for visitors who looked like big spenders, would break that.
- B: The conclusion is about purchases, not liking. Liking may be part of why, but it is not something the conclusion needs.
- C: If the new version also loaded faster, the extra purchases could be due to speed, not the button.
- D: If one group's purchases were recorded more completely, the difference could come from the counting.
- E: The conclusion is about the future, after the novelty wears off, so it assumes the gain lasts.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.34

A school district offers an AI tutoring program to any school that signs up. Twenty schools signed up and sixty did not. At the end of the year, the signed-up schools' average scores had risen more than the others'. The district concludes that the AI tutor raised scores. Check each statement that describes a possible problem for the conclusion. Each statement is worth 1 point (5 points total).

- [ ] A. The program was free for schools.
- [ ] B. Schools that sign up for new programs may have more motivated leaders, who would raise scores in other ways too.
- [ ] C. The district gave the same test in all schools.
- [ ] D. Signed-up schools may have started with lower scores, so they had more room to improve.
- [ ] E. Twenty schools signed up and sixty did not.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: A free program does not make the comparison misleading.
- B: Motivation could cause both signing up and improvement, so the gap may not be due to the tutor.
- C: Using the same test is a strength of the comparison, not a problem.
- D: Schools that start low often gain more for reasons unrelated to the program.
- E: Unequal group sizes are not by themselves a problem for the conclusion.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.35

A lab reports that its new language model, Model A, scores 82% on a public coding benchmark and a competitor's Model B scores 74%. The lab concludes that Model A is better at coding. Check each statement that is an assumption the conclusion depends on: something that must be true for the conclusion to hold, and that the experiment itself did not show. Each statement is worth 1 point (5 points total).

- [ ] A. Model A scored higher than Model B.
- [ ] B. Both models were given the questions in the same format with the same instructions.
- [ ] C. Model A's score was not the best of many attempts at the benchmark.
- [ ] D. The benchmark's questions were not in Model A's training data.
- [ ] E. The benchmark's questions resemble the coding tasks people actually want help with.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: That is the observed result, not an assumption behind the conclusion.
- B: Different prompts could produce different scores for reasons unrelated to ability.
- C: Reporting the best of many tries overstates what the model does on a single run.
- D: If the model had seen the answers, the score would reflect memory, not coding skill.
- E: 'Better at coding' in general needs the benchmark to measure the skills that matter.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.36

Researchers send an AI résumé-screening tool 400 pairs of résumés. In each pair the two résumés are identical except for the applicant's first name, chosen to suggest different ethnic backgrounds. The tool gives one group of names lower scores on average. The researchers conclude that the tool scores applicants lower because of the ethnic background the names suggest. Check each statement that is an assumption the conclusion depends on: something that must be true for the conclusion to hold, and that the experiment itself did not show. Each statement is worth 1 point (5 points total).

- [ ] A. The tool is accurate at predicting who will do the job well.
- [ ] B. The tool's developers intended it to treat names differently.
- [ ] C. The first names suggest the ethnic backgrounds the researchers intended, and nothing else about the applicant.
- [ ] D. The résumés describe people who would be good at the job.
- [ ] E. Four hundred pairs is enough to find any difference the tool has.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: The conclusion is about what the score responds to, not about whether the scores predict performance.
- B: Intent is not needed; the conclusion concerns the tool's behaviour.
- C: If a name also suggested, say, age or social class, the gap might reflect that instead of ethnic background.
- D: The comparison is between names on identical résumés, whatever their quality.
- E: The researchers observed a difference; how many pairs would be needed to detect smaller ones is not an assumption behind this conclusion.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.37

In a randomized trial, 500 patients receive a new drug and 500 receive a placebo. After a year, 80% of patients who stayed in the study on the drug had recovered, against 60% on the placebo. In the drug group 120 patients left the study early; in the placebo group 20 did. The researchers conclude that the drug will raise recovery rates for the patients who are prescribed it in future. Check each statement that is an assumption the conclusion depends on: something that must be true for the conclusion to hold, and that the experiment itself did not show. Each statement is worth 1 point (5 points total).

- [ ] A. Each group started with 500 patients.
- [ ] B. The patients who left the drug group early were not mostly patients who were doing badly.
- [ ] C. Recovery was judged in the same way in both groups.
- [ ] D. The 80% and 60% recovery rates are exactly the true rates for all future patients.
- [ ] E. The patients in the study are similar to the patients who will be prescribed the drug.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: That is stated in the description, not something the conclusion has to assume.
- B: If the sickest patients left, the remaining drug group looks healthier than it should.
- C: A looser standard in one group would create a difference that is not due to the drug.
- D: The conclusion is that the drug raises recovery, not that these numbers are exact.
- E: A result in this group carries over to others only if the study patients resemble the people who will use the drug.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.38

A company tests whether a chatbot resolves customer issues faster than human agents. Each incoming chat goes to the chatbot when no human agent is free and to a human agent when one is free. Chats handled by the chatbot were resolved faster on average. The company concludes that the chatbot is faster than humans. Check each statement that describes a possible problem for the conclusion. Each statement is worth 1 point (5 points total).

- [ ] A. Chats arrive at peak times, when agents are busy, and the kinds of questions may differ from quiet times.
- [ ] B. The chatbot can answer in more than one language.
- [ ] C. The company employs more human agents than chatbots.
- [ ] D. The chatbot may pass hard issues to a human, so the chats it 'resolves' are the easy ones.
- [ ] E. Resolution time was recorded by the same system for both kinds of chat.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Who gets the chatbot depends on how busy the agents are, which relates to the kind of chat, so the groups are not comparable.
- B: That does not undermine a comparison of resolution speed.
- C: The number of agents is not a problem for the comparison.
- D: If hard cases leave the chatbot's count, its average speed is flattered.
- E: Measuring both the same way is a strength.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.39

A social app switches on a new 'share to friends' button for a random half of its users and compares how many posts each user sees from friends. Users with the button saw more posts. The company concludes that the button increases the number of posts a user sees. Check each statement that describes a possible problem for the conclusion. Each statement is worth 1 point (5 points total).

- [ ] A. Users without the button who are friends of users with it also receive the extra shared posts, so the comparison group is also affected.
- [ ] B. The random half was chosen by a computer.
- [ ] C. Users given a new button may click it out of curiosity at first, and that interest may fade.
- [ ] D. Some users have more friends than others.
- [ ] E. Posts seen were counted the same way for every user.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The control group is not untouched; one user's treatment spills over to others, which muddies the comparison.
- B: Random assignment by a computer is not a problem.
- C: An early burst of curiosity can overstate the lasting effect on the posts a user sees.
- D: Differences in friend counts are not by themselves a problem when assignment is random.
- E: Consistent counting is a strength.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.40

A hospital builds a model to spot pneumonia in chest X-rays and reports 96% accuracy on a test set of 2,000 images held back from training. It concludes that the model will correctly identify pneumonia in patients at its own clinics next year. Check each statement that is an assumption the conclusion depends on: something that must be true for the conclusion to hold, and that the experiment itself did not show. Each statement is worth 1 point (5 points total).

- [ ] A. The model is a neural network.
- [ ] B. The test set contained 2,000 images.
- [ ] C. The model takes less than a second to read each image.
- [ ] D. Next year's patients and X-ray machines will resemble those in the test set.
- [ ] E. Hospitals in other countries use similar machines.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: The type of model is not what the conclusion depends on.
- B: That is a stated fact, not an assumption.
- C: Speed is unrelated to whether its readings will be correct.
- D: Accuracy on the test set carries over only if the future cases look like the test cases.
- E: The conclusion is about the hospital's own clinics.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.41

A bank's fraud model flags 100 transactions a day. Investigators review only the flagged ones and confirm that 90 of them are fraud. A manager says: 'The model catches 90% of fraud.' Check each statement that the evidence supports. Each statement is worth 1 point (5 points total).

- [ ] A. The model catches 90% of all fraud.
- [ ] B. Of the flagged transactions that were reviewed, 90% turned out to be fraud.
- [ ] C. The model rarely misses fraud.
- [ ] D. Investigators confirmed that the transactions the model did not flag were genuine.
- [ ] E. The review says nothing about fraud that the model did not flag.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The investigators looked only at flagged transactions, so the number of frauds the model missed is unknown.
- B: That is exactly what the review shows.
- C: Missed fraud was never counted, so the evidence is silent on it.
- D: They did not review unflagged transactions.
- E: Frauds outside the flagged set are not in the data.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.42

A district gives laptops to a random 10 of 20 classrooms. At the end of the year it compares test scores of the 250 students with laptops and the 250 without, treating each student as one independent data point, and finds a small advantage that it describes as very strong evidence. It concludes that laptops raise scores. Check each statement that describes a possible problem for the conclusion. Each statement is worth 1 point (5 points total).

- [ ] A. Students in the same classroom share a teacher and other influences, so 250 students are not 250 independent pieces of evidence.
- [ ] B. Only half of the classrooms received laptops.
- [ ] C. The classrooms were chosen by chance.
- [ ] D. With only ten classrooms in each group, one unusually strong teacher could drive the difference.
- [ ] E. The same tests were given to both groups.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The assignment was by classroom, so the evidence is closer to 10 against 10 classrooms than to 250 against 250 students.
- B: Giving laptops to half the classrooms is a normal design.
- C: Random assignment is a strength.
- D: A few classrooms can be swayed by one teacher or one cohort.
- E: Using the same tests is a strength.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.43

An advertiser randomly assigns browsers (identified by cookie) to see either its ad or a charity ad, then counts purchases made by the same browsers over the next week. Browsers shown its ad bought more. The advertiser concludes that its ad leads people to make purchases they would not otherwise have made. Check each statement that is an assumption the conclusion depends on: something that must be true for the conclusion to hold, and that the experiment itself did not show. Each statement is worth 1 point (5 points total).

- [ ] A. Every browser in the test made at least one purchase.
- [ ] B. The extra purchases were not just purchases moved up from later weeks.
- [ ] C. Customers prefer ads from companies to ads from charities.
- [ ] D. Seeing the charity ad does not change how much a person buys.
- [ ] E. Purchases were recorded in the same way for browsers shown either ad.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Many browsers buy nothing; the comparison is of purchase rates.
- B: If the ad only pulled purchases forward, later weeks would show a drop and the ad would add nothing.
- C: Which kind of ad people prefer is not something the conclusion depends on.
- D: The comparison measures the ad against the charity ad; if the charity ad itself changes buying, the effect is misjudged.
- E: Different recording could create a gap that is not due to the ad.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.44

A social platform introduces a new moderation policy in March. In April it reports that harassment reports fell 30% compared with February. It concludes that the policy reduced harassment. Check each statement that describes a possible problem for the conclusion. Each statement is worth 1 point (5 points total).

- [ ] A. Other things changed between February and April, such as the number of active users or news events.
- [ ] B. The platform measured reports in both months.
- [ ] C. The policy began in March.
- [ ] D. Users may file fewer reports if they think the new policy will not act on them, even if harassment did not fall.
- [ ] E. There was no comparable platform or group of users without the policy to compare against.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Any of those could account for the change without the policy.
- B: Measuring both months is what makes the comparison possible.
- C: The start date is a fact of the design, not a problem.
- D: Reports measure reporting, which can change for reasons unrelated to harassment.
- E: Without a comparison, anything that changed over time is mixed with the policy.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.45

Researchers recruit 300 adults through a fitness app to wear a sleep tracker for a month and find that people who went to bed before 11 p.m. reported better mood. They conclude that going to bed earlier improves mood for adults in general. Check each statement that is an assumption the conclusion depends on: something that must be true for the conclusion to hold, and that the experiment itself did not show. Each statement is worth 1 point (5 points total).

- [ ] A. All 300 participants live in the same time zone.
- [ ] B. Going to bed earlier was not itself caused by something else that also lifts mood, such as a calm job.
- [ ] C. The tracker recorded bedtimes correctly.
- [ ] D. Early and late sleepers used the mood scale in comparable ways.
- [ ] E. People who join through a fitness app resemble adults in general in how bedtime relates to mood.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Where people live is not something the conclusion requires.
- B: Otherwise the mood difference may come from that other factor, not from bedtime.
- C: The comparison depends on who really went to bed early.
- D: If one group rates itself more generously, the difference may not be real.
- E: Generalizing from volunteers to all adults assumes the volunteers are not special in this respect.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.46

A company asks 50 raters to compare answers from its chatbot and a competitor's chatbot to the same 200 questions. Each answer is labelled with the name of the chatbot that wrote it. Raters preferred the company's chatbot's answers 70% of the time. The company concludes that its chatbot gives better answers. Check each statement that describes a possible problem for the conclusion. Each statement is worth 1 point (5 points total).

- [ ] A. Both chatbots answered the same questions.
- [ ] B. Raters who see the brand name may favour the brand they already know.
- [ ] C. Some of the raters may be the company's own employees, who may favour their employer's chatbot.
- [ ] D. Fifty raters is a large number of raters.
- [ ] E. If the company's answer is always shown first, position may favour it.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Answering the same questions is a strength of the design.
- B: The label can sway the rating regardless of the answer's quality.
- C: Raters with a stake in the result are a source of bias.
- D: Having many raters is not a problem.
- E: Order effects can create a preference unrelated to quality.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.47

A team lowers the decision threshold for one group of loan applicants until that group's approval rate matches the other group's, choosing the threshold by trying many values on a dataset of 5,000 past applicants. It then reports that on the same 5,000 applicants the two groups' approval rates are now equal, and concludes that the model is fair. Check each statement that describes a possible problem for the conclusion. Each statement is worth 1 point (5 points total).

- [ ] A. The threshold was tuned on the same applicants used to check the result, so the match may not hold for new applicants.
- [ ] B. Equal approval rates do not show that equally qualified applicants are treated equally.
- [ ] C. The dataset has 5,000 applicants.
- [ ] D. The two groups have different numbers of applicants.
- [ ] E. The team did not check what happens to the error rates for each group.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: A result tuned and tested on the same data tends to look better than it will on fresh data.
- B: Matching rates is one definition of fairness; it can leave other disparities in place.
- C: The size is not a problem in itself.
- D: Groups of different sizes are normal and not a problem here.
- E: Equal approval rates can come with different rates of wrongly denying qualified applicants.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.48

A team runs an A/B test that was planned for four weeks and checks the results every morning. On day six the new version shows a statistically significant improvement, so the team stops the test, ships the new version, and concludes that it is better. Check each statement that describes a possible problem for the conclusion. Each statement is worth 1 point (5 points total).

- [ ] A. Checking repeatedly and stopping when the result looks good gives chance many opportunities to produce a misleading win.
- [ ] B. Users were assigned to the two versions at random.
- [ ] C. The improvement was reported as statistically significant.
- [ ] D. Six days may not cover weekly patterns such as weekends.
- [ ] E. The team may have tracked many measures and reported the one that improved.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The more times you look, the likelier a lucky streak crosses the threshold.
- B: Random assignment is a strength.
- C: Reporting significance is not a problem; how and when it was reached is.
- D: Behaviour differs by day of the week, so a short test may miss it.
- E: Looking at many measures and reporting the winner makes a chance improvement likely.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.49

A company randomly sends half of its customers a reminder email about renewing and sends nothing to the others. To measure the effect of the email it looks only at customers who opened the email and compares their renewal rate with that of customers who were sent nothing. The email group renewed more. The company concludes that the email raises renewals. Check each statement that describes a possible problem for the conclusion. Each statement is worth 1 point (5 points total).

- [ ] A. People who open emails may be more engaged customers who would have renewed anyway.
- [ ] B. The customers were assigned to get the email by chance.
- [ ] C. Customers who disliked the email may have deleted it unopened, so they are left out of the email group.
- [ ] D. Customers can renew without opening the email.
- [ ] E. Renewals were counted for both groups.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Opening is chosen by the customer, so the openers differ from the rest.
- B: Random assignment is a strength; the problem is the comparison made afterwards.
- C: Dropping the people who reacted badly makes the email group look better than the email deserves.
- D: That is true of both groups and is not a problem for the comparison.
- E: Counting both groups is needed for the comparison.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.50

A team evaluates Model A on customer questions collected in March and Model B on questions collected in April. Model A scores 88% and Model B scores 79%. Check each statement that the evidence supports. Each statement is worth 1 point (5 points total).

- [ ] A. Model A scored higher on its March questions than Model B did on its April questions.
- [ ] B. Model A is the better model.
- [ ] C. Part of the 9-point gap may come from differences between the March and April questions.
- [ ] D. Model B would have scored 79% on the March questions.
- [ ] E. The two models were tested on identical questions.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: That is the observed result.
- B: The models were tested on different questions, so the gap does not isolate the models.
- C: Different question sets can differ in difficulty or topic.
- D: Nothing was measured for Model B on those questions.
- E: They were tested on questions from different months.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.51

A state gives extra funding and coaching to its 20 lowest-scoring schools. The next year, those schools' average score rose by 8 points, while the state average rose by 1 point. The state concludes that the program raised scores. Check each statement that describes a possible problem for the conclusion. Each statement is worth 1 point (5 points total).

- [ ] A. The program included both funding and coaching.
- [ ] B. Schools picked because they scored unusually low in one year tend to score closer to average the next year even without help.
- [ ] C. The state average also rose, by 1 point.
- [ ] D. There was no group of similarly low-scoring schools that did not get the program.
- [ ] E. The lowest-scoring schools may also have received other help from the state or their districts that year.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Bundling two parts affects which part worked, not whether the conclusion about the program is misleading.
- B: Part of a low score is luck, which does not repeat; this alone can produce a rise.
- C: A small rise elsewhere is not a problem.
- D: Without such a group, the rise cannot be separated from what would have happened anyway.
- E: Other help could explain the rise without the program.

**Source:** Hidden assumptions that hide in plain sight

## MA-ch03.52

A health system tests a new blood-pressure program in 10 clinics and compares them with 10 other clinics. To save money, the program clinics also switched to a new brand of blood-pressure monitor. After six months, program clinics report lower blood pressure. The system concludes that the program lowers blood pressure. Check each statement that is an assumption the conclusion depends on: something that must be true for the conclusion to hold, and that the experiment itself did not show. Each statement is worth 1 point (5 points total).

- [ ] A. The new brand of monitor gives the same readings as the old one for the same patient.
- [ ] B. Patients at the program clinics and the comparison clinics were similar at the start.
- [ ] C. The patients measured at six months were not a healthier subset of those who started in the program clinics.
- [ ] D. Patients enjoyed visiting the clinics.
- [ ] E. The new brand of monitor costs less than the old one.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: If the new monitor reads lower, the difference could come from the device, not the program.
- B: Otherwise the clinics may have differed in blood pressure before the program.
- C: If sicker patients dropped out of the program clinics, the remaining group looks better than the program deserves.
- D: Enjoyment is not something the conclusion depends on.
- E: Cost is a reason for the switch, not something the conclusion depends on.

**Source:** Hidden assumptions that hide in plain sight
