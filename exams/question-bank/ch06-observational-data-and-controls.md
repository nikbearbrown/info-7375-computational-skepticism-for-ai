# Chapter 6: Bias, where it enters and who is responsible

## MA-ch06.72

A health researcher lists studies that have been done on the effect of a treatment. Check each study that uses observational data. Each statement is worth 1 point (5 points total).

- [ ] A. Researchers pull a hospital's past records and compare patients who were given an antibiotic by their doctors with patients who were not.
- [ ] B. A survey asks adults whether they take a daily vitamin and whether they had a fracture this year.
- [ ] C. An analyst compares test scores of students in schools that chose to adopt a new curriculum with schools that did not.
- [ ] D. A website randomly shows half of its visitors a new layout and then measures purchases.
- [ ] E. A bank compares repayment of customers who chose to use its mobile app with customers who did not.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Doctors and circumstances, not the researchers, decided who got the antibiotic; the researchers only observed what happened, so the data are observational.
- B: The researchers did not assign the vitamin; people chose for themselves, so the data are observational.
- C: The schools chose the treatment; nobody assigned it for the purpose of the study, so the data are observational.
- D: The website assigns the layout by chance. Assigning the treatment at random is an experiment, not observation.
- E: Customers chose whether to use the app, so the treatment was not assigned by the investigator.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.73

A policy group collects the following studies of a workplace or school program. Check each description that is observational data. Each statement is worth 1 point (5 points total).

- [ ] A. Researchers draw names from a hat to decide which of 200 employees will be offered a four-day week, then track their output.
- [ ] B. A transport agency compares commute times of people who chose to switch to a new train line with those of people who did not.
- [ ] C. An online course randomly gives half of new learners a reminder email and measures completion.
- [ ] D. A bank analyses past loan records to compare repayment for customers whom loan officers did or did not offer a payment plan.
- [ ] E. Researchers use a random number generator to decide which schools receive tutoring grants, then compare scores.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The researchers assign the treatment by chance, so this is an experiment.
- B: Commuters chose the treatment, so the data are observational.
- C: The course assigns the email by chance, so this is an experiment.
- D: Loan officers, not the analysts, decided who was offered the plan, and the analysis looks back at records, so the data are observational.
- E: The researchers assign the grants by chance, so this is an experiment.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.74

A health agency has the following sources. Check each source that provides observational data about whether a treatment works. Each statement is worth 1 point (5 points total).

- [ ] A. A trial in which a computer randomly assigns each patient to a drug or a placebo.
- [ ] B. Insurance claims that show which patients filled a prescription and who was later hospitalised.
- [ ] C. A national survey asking people whether they smoke and whether they have lung disease.
- [ ] D. Electronic health records of patients whose doctors chose which blood-pressure drug to prescribe.
- [ ] E. Fitness-tracker records of users who decided on their own to join a walking challenge.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Random assignment by the investigators makes this experimental data.
- B: Patients and doctors decided who filled the prescription; the claims only record it.
- C: Nobody assigned smoking; people chose it, so the data are observational.
- D: The doctors chose the treatment, not an investigator, so the data are observational.
- E: Users chose the treatment, so the data are observational.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.75

Check each statement that is true about observational data. Each statement is worth 1 point (5 points total).

- [ ] A. In observational data the investigator did not assign the treatment; people or circumstances determined who received it.
- [ ] B. Any dataset taken from existing records is observational, even if the treatment in those records was assigned by chance.
- [ ] C. A dataset with millions of rows can still be observational.
- [ ] D. Observational data records the treatment but not the outcome.
- [ ] E. Whether data is observational depends on how the treatment came about, not on how carefully the variables were measured.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: That is what makes data observational.
- B: What matters is how the treatment was assigned. Records of a trial in which the treatment was assigned by chance are experimental data.
- C: Many rows do not change who chose the treatment.
- D: Observational data usually records both; what is missing is the investigator's assignment of the treatment.
- E: Careful measurement does not turn chosen treatments into assigned ones.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.76

A trial randomly assigns 2,000 patients to take a new drug or a placebo and compares recovery. Check each statement that is true about what randomization does in this trial. Each statement is worth 1 point (5 points total).

- [ ] A. On average, factors such as age and prior health end up similar in the two groups.
- [ ] B. In a trial of ten patients, it ensures that the two groups match closely on age.
- [ ] C. It breaks the link between a patient's prior health and whether the patient receives the drug, so prior health is not a confounder here.
- [ ] D. It makes the recovery measurements more accurate.
- [ ] E. It lets researchers estimate the drug's effect without having measured every factor that affects recovery.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Chance assignment spreads such factors across the groups in the same way on average.
- B: With very few patients, chance can leave the groups quite different; the balance holds on average and improves with size.
- C: A confounder must affect the treatment as well as the outcome; chance assignment means prior health no longer affects who gets the drug.
- D: Randomization concerns who gets the treatment, not how well the outcome is measured.
- E: Because assignment is by chance, unmeasured factors are not tied to the treatment either.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.77

A data scientist explains why most of her work uses observational data instead of randomized trials. Check each statement that is a reason she could give. Each statement is worth 1 point (5 points total).

- [ ] A. Randomly assigning a harmful exposure, such as smoking, to people would be unethical.
- [ ] B. Many questions concern events that have already happened, so who received the treatment cannot be reassigned.
- [ ] C. Randomized trials usually give less reliable causal answers than observational data.
- [ ] D. Running a randomized trial can be slow and expensive.
- [ ] E. Records of what people chose already exist in many settings and can be studied without running a new trial.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Some treatments cannot be assigned for ethical reasons, so they can only be observed.
- B: Past events can be studied only as they happened.
- C: Randomization is what makes a trial a strong way to answer causal questions; its limits are cost, ethics and practicality.
- D: Cost and time often make a trial impractical.
- E: Existing records are an available source of observational data.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.78

A career site records whether 1,000 applicants had a personal website and whether they were interviewed. Experience is grouped as little, moderate or a lot, and more experience raises the chance of an interview. Among the 500 applicants with a website, 10% have little experience, 30% moderate and 60% a lot; among the 500 without a website, 60% have little, 30% moderate and 10% a lot. Interview rates for applicants with and without a website are: little experience 20% and 10%; moderate 40% and 30%; a lot 70% and 60%. Overall, 56% of applicants with a website and 21% of those without were interviewed. The treatment is having a website and the outcome is being interviewed. Check each statement that follows from these numbers. Each statement is worth 1 point (5 points total).

- [ ] A. The overall difference of 35 points shows that a website raises the chance of an interview by 35 points.
- [ ] B. Within each experience group, having a website goes with an interview rate 10 points higher.
- [ ] C. Because experience raises the chance of an interview, the website has no effect.
- [ ] D. The overall difference of 35 points overstates the website's effect, because website owners tend to be more experienced.
- [ ] E. Averaging the three within-group differences gives an effect of about 10 points.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Applicants with websites are more experienced, and experience raises the chance of an interview, so the overall difference mixes the website's effect with the effect of experience.
- B: The rates are 20 against 10, 40 against 30, and 70 against 60: a 10-point difference in every group.
- C: Within each group, where experience is held about the same, applicants with websites still do better by 10 points.
- D: Experience affects both whether someone has a website and whether they are interviewed, so it is a confounder and inflates the overall difference.
- E: Each group shows 10 points, so any average of the three is about 10 points.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.79

In records of 10,000 adults, people in poor health are more likely to get a flu shot and also more likely to have a serious case of flu. The treatment is getting the flu shot and the outcome is having a serious case of flu. Check each comparison that compares like with like on health status. Each statement is worth 1 point (5 points total).

- [ ] A. Comparing serious-flu rates of vaccinated and unvaccinated people who are all in poor health.
- [ ] B. Comparing serious-flu rates of all vaccinated people with all unvaccinated people, ignoring health.
- [ ] C. Doing the within-group comparison separately for people in poor health and for people in good health, then combining the two group results by weighting each group by its size.
- [ ] D. Comparing serious-flu rates of vaccinated and unvaccinated people who are all in good health.
- [ ] E. Comparing vaccinated people in poor health with unvaccinated people in good health.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Everyone compared has the same health status, so health cannot explain the difference.
- B: Ignoring health mixes the shot's effect with the effect of health status.
- C: Comparing within each health group and then averaging across groups is how the effect is controlled for health and combined.
- D: Again everyone compared has the same health status, so the comparison controls for it.
- E: The two groups differ in health status as well as in the shot, so health is not controlled for.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.80

Check each statement that is true about controlling for a variable, which is also called adjusting for it. Each statement is worth 1 point (5 points total).

- [ ] A. It means deleting that variable's column from the dataset.
- [ ] B. It means comparing treated and untreated people who have the same value of that variable.
- [ ] C. "Controlling for" and "adjusting for" are two names for the same thing.
- [ ] D. It requires that the variable was measured.
- [ ] E. It requires the investigator to assign the treatment at random.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Controlling uses the variable to form comparison groups; deleting it would leave the confounding in place.
- B: Comparing within groups of similar people is how the variable is held constant.
- C: They are used interchangeably.
- D: Without a measurement there is no way to group people by it.
- E: Random assignment is a different way to handle confounders; controlling is done on the data after the fact.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.81

Imagine a hidden fair coin U flipped for each person. Think of U as qualification, X as a referral and Y as an interview. In both of two worlds, a person's referral X equals the coin. In world 1, whether the person is interviewed (Y) follows the referral X. In world 2, Y follows the coin U directly and ignores the referral. In the data from either world, X and Y agree for every person, half zeros and half ones. Check each step that would let us tell the two worlds apart. Each statement is worth 1 point (5 points total).

- [ ] A. Collecting ten times as many rows from each world.
- [ ] B. Measuring the coin value for each person without changing anything.
- [ ] C. Forcing everyone to receive a referral and then recording who is interviewed.
- [ ] D. Checking whether X and Y agree in the data.
- [ ] E. Recording the referral status of more people.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: More rows from either world show the same pattern, so they cannot separate the worlds.
- B: X already equals the coin, so measuring it adds no new information.
- C: In world 1 everyone would be interviewed; in world 2 only those whose coin is 1 would be. Changing the treatment reveals how the outcome is generated.
- D: They agree for every person in both worlds.
- E: Referral status matches the coin in both worlds, so more of it looks the same in both.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.82

A recruiter draws arrows between experience, having a website, and getting an interview to describe how these variables are related. Check each statement that is true about where the arrows come from. Each statement is worth 1 point (5 points total).

- [ ] A. They can be read directly off a table of rows by any statistical program.
- [ ] B. They come from assumptions about how the variables are generated, such as that experience comes before making a website.
- [ ] C. Once enough rows are collected, a single set of arrows is consistent with the data.
- [ ] D. Different assumptions about the arrows can fit the same table equally well.
- [ ] E. They are estimated from the rows by the same method that estimates an average interview rate.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The same table can be produced by different arrow structures.
- B: The arrows are assumptions about the setting, not findings from the table.
- C: More rows of the same kind do not rule out other arrow structures.
- D: That is why knowledge about how the data were generated is needed.
- E: Averages are computed from rows, but the arrows are assumptions about how the variables are generated, which the rows alone do not contain.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.83

Imagine a hidden fair coin U flipped for each person. Think of U as qualification, X as a referral and Y as an interview. In both of two worlds, a person's referral X equals the coin. In world 1, whether the person is interviewed (Y) follows the referral X. In world 2, Y follows the coin U directly and ignores the referral. Check each statement that is true about the data from the two worlds. Each statement is worth 1 point (5 points total).

- [ ] A. In the data from both worlds, X and Y agree for every person.
- [ ] B. The data alone show that the referral caused the interview.
- [ ] C. The data alone show that qualification caused the interview.
- [ ] D. Both worlds produce the same pattern: half zeros and half ones, matching in every row.
- [ ] E. Enough rows would eventually make the data from the two worlds look different.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: In world 1 Y equals X; in world 2 Y equals U, and X equals U, so Y equals X in both.
- B: World 2 produces the same data, and there the referral plays no role.
- C: World 1 produces the same data, and there qualification affects the interview only through the referral.
- D: The coin is fair and X, Y and U coincide, so the pattern is identical.
- E: The worlds give the same data however many rows are collected.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.84

Suppose that, after controlling for experience, 32% of applicants without a website and 70% of applicants with one were interviewed, and the difference is the website's effect. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The website raised the chance of an interview by 38 percentage points.
- [ ] B. Every applicant who made a website was interviewed.
- [ ] C. An applicant without a website had no chance of an interview.
- [ ] D. The effect is the number of interviews divided by the number of websites.
- [ ] E. The effect describes how much the chance changed, not whether any single applicant was interviewed.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: 70 minus 32 is 38 percentage points.
- B: The chance rose to 70%, not 100%; the website did not guarantee an interview.
- C: Applicants without a website were interviewed at a rate of 32%.
- D: The effect is the change in the chance of an interview, not a count of interviews per website.
- E: The effect is a degree of change in the probability of the outcome.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.85

Two career sites each report the change in interview rate from having a personal website, after controlling for experience. Site A: 32% without a website, 70% with. Site B: 5% without, 12% with. Assume each difference is the website's effect. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Site B's website raised the interview chance by more percentage points than site A's.
- [ ] B. Site A's website raised the interview chance by more percentage points than site B's.
- [ ] C. Site A's relative increase (70% compared with 32%) is larger than site B's (12% compared with 5%).
- [ ] D. Because site B's chances are low, its website had no effect.
- [ ] E. The effect of site B's website cannot be expressed as a difference in percentage points.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Site B's change is 7 points and site A's is 38 points.
- B: 38 points against 7 points.
- C: 70 divided by 32 is about 2.2, and 12 divided by 5 is 2.4, so site B's relative increase is larger.
- D: The chance rose from 5% to 12%, which is an effect even though both numbers are low.
- E: It can: 12 minus 5 is 7 percentage points.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.86

A recruiter notices that applicants with a personal website get more interviews, and wonders whether the website or the applicant's experience is responsible. Check each step that would help separate the two. Each statement is worth 1 point (5 points total).

- [ ] A. Collecting ten times as many applicants in the same way.
- [ ] B. Randomly assigning websites to applicants and comparing interview rates.
- [ ] C. Computing the correlation between having a website and being interviewed more precisely.
- [ ] D. Asking the applicants which of the two they think mattered.
- [ ] E. Comparing applicants with and without websites within groups of similar experience.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: More of the same observational data keeps the website and experience tangled together.
- B: Chance assignment breaks the link between experience and having a website.
- C: A more precise association does not say whether experience or the website is responsible.
- D: Opinions are not a way of separating the effects in the data.
- E: Holding experience about the same controls for it.

**Source:** Pearl's Ladder — Rungs 1 and 2
