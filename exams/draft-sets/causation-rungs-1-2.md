# INFO 7375 Computational Skepticism for AI: causation practice set: association and intervention

**DRAFT FORM. Covers rung 1 (association), rung 2 (intervention) and why the difference matters. No counterfactuals. Not the real exam; not signed off by the instructor.**

20 questions, 5 points each, 100 points. Name: ______________________

**Scoring.** Five statements, each true or false, 1 point each. The student checks the statements they believe are true. A statement scores 1 point if it is checked and true, or unchecked and false; otherwise 0. Read every statement on its own and decide whether it is true by itself. Strong words (always, never, every, proves) are often what makes a statement false, but a strong-sounding statement is not false for sounding strong.

---

**1.** Check each statement that is true about controlling for a variable, which is also called adjusting for it.  *(5 points)*

- [ ] A. It means deleting that variable's column from the dataset.
- [ ] B. It means comparing treated and untreated people who have the same value of that variable.
- [ ] C. "Controlling for" and "adjusting for" are two names for the same thing.
- [ ] D. It requires that the variable was measured.
- [ ] E. It requires the investigator to assign the treatment at random.

**2.** A city compares the end-of-year exam scores of students who attended a free after-school tutoring program with those who did not, to learn whether tutoring raises scores. Families choose whether to enrol; places are not assigned by lottery. Here the treatment is attending the tutoring program and the outcome is the exam score. Check each variable that is a confounder in this situation.  *(5 points)*

- [ ] A. The student's grades in the previous year, which influence whether a family enrols the child and also influence this year's exam score.
- [ ] B. The number of tutoring sessions the student attends after enrolling, which tutoring produces and which in turn raises the exam score.
- [ ] C. Whether the student later wins a scholarship, which is more likely both for students who were tutored and for students with high exam scores.
- [ ] D. How involved the parents are in schoolwork, which makes enrolment more likely and also raises exam scores.
- [ ] E. The student's sleep on the night before the exam, which affects the exam score but is unrelated to whether the family enrolled the child.

**3.** A data scientist explains why most of her work uses observational data instead of randomized trials. Check each statement that is a reason she could give.  *(5 points)*

- [ ] A. Randomly assigning a harmful exposure, such as smoking, to people would be unethical.
- [ ] B. Many questions concern events that have already happened, so who received the treatment cannot be reassigned.
- [ ] C. Randomized trials usually give less reliable causal answers than observational data.
- [ ] D. Running a randomized trial can be slow and expensive.
- [ ] E. Records of what people chose already exist in many settings and can be studied without running a new trial.

**4.** A recruiter notices that applicants with a personal website get more interviews, and wonders whether the website or the applicant's experience is responsible. Check each step that would help separate the two.  *(5 points)*

- [ ] A. Collecting ten times as many applicants in the same way.
- [ ] B. Randomly assigning websites to applicants and comparing interview rates.
- [ ] C. Computing the correlation between having a website and being interviewed more precisely.
- [ ] D. Asking the applicants which of the two they think mattered.
- [ ] E. Comparing applicants with and without websites within groups of similar experience.

**5.** Each statement classifies a question. Check each statement that classifies correctly.  *(5 points)*

- [ ] A. 'If every patient were required to take the drug, what share would recover?' is an association question.
- [ ] B. 'Do customers who saw recommendations buy more?' is an association question.
- [ ] C. 'Would customers buy more if we started showing them recommendations?' is an association question.
- [ ] D. 'What is the correlation between hours studied and grade?' is an association question.
- [ ] E. 'Among patients who took the drug, what share recovered?' is an association question.

**6.** A student writes a definition of a confounder for a causal question about a treatment and an outcome. Check each statement that is true.  *(5 points)*

- [ ] A. Randomizing the treatment removes the link between the treatment and the confounder.
- [ ] B. A confounder influences both who receives the treatment and the outcome.
- [ ] C. Collecting more data of the same kind leaves the confounding in place.
- [ ] D. A confounder is any variable that the treatment itself causes.
- [ ] E. A confounder can make the observed association differ from the effect of the treatment.

**7.** A product team finds that users who turn on notifications are retained more often, and asks whether switching notifications on for everyone would raise retention. Check each statement that is true.  *(5 points)*

- [ ] A. Users who choose notifications may already be more engaged, which could produce the gap on its own.
- [ ] B. The observed retention gap answers the question directly, because it compares two groups of real users.
- [ ] C. Randomly turning notifications on for some users and comparing would address the question.
- [ ] D. Waiting for ten times as many self-selected users would not remove the problem.
- [ ] E. The question asks what would happen if the team set the treatment, so it is an intervention question.

**8.** Researchers find that cities with more protected bike lanes have lower adult obesity rates, and ask whether bike lanes reduce obesity. Each city decides for itself how many lanes to build. Here the treatment is the number of bike lanes and the outcome is the obesity rate. Check each variable that is a confounder in this situation.  *(5 points)*

- [ ] A. City wealth, since richer cities can afford more lanes and also tend to have lower obesity rates.
- [ ] B. Climate, since mild-weather cities are more likely to build lanes and also have residents who exercise outdoors more.
- [ ] C. The share of residents who cycle to work, which the lanes encourage and which burns calories.
- [ ] D. The number of news stories about obesity published in the city, which rises when obesity rates are high.
- [ ] E. A city health department that funds active-living programs, which leads the city both to build lanes and to run other programs that lower obesity.

**9.** A retailer trains a model on past orders to predict who buys, and plans to use it to decide which customers to give a discount. Check each statement that is true.  *(5 points)*

- [ ] A. Acting on the model's predictions changes the system, so the old association may not hold afterwards.
- [ ] B. The model's score for a customer is the effect of the discount on that customer.
- [ ] C. A small randomized test of the discount would answer the effect question directly.
- [ ] D. Past orders reflect earlier decisions by people, so the model learned from associations produced by those choices.
- [ ] E. High accuracy on held-out past data guarantees the discount will raise sales.

**10.** In records of 10,000 adults, people in poor health are more likely to get a flu shot and also more likely to have a serious case of flu. The treatment is getting the flu shot and the outcome is having a serious case of flu. Check each comparison that compares like with like on health status.  *(5 points)*

- [ ] A. Comparing serious-flu rates of vaccinated and unvaccinated people who are all in poor health.
- [ ] B. Comparing serious-flu rates of all vaccinated people with all unvaccinated people, ignoring health.
- [ ] C. Doing the within-group comparison separately for people in poor health and for people in good health, then combining the two group results by weighting each group by its size.
- [ ] D. Comparing serious-flu rates of vaccinated and unvaccinated people who are all in good health.
- [ ] E. Comparing vaccinated people in poor health with unvaccinated people in good health.

**11.** A manager asks why it matters to separate association questions from intervention questions. Check each statement that is true.  *(5 points)*

- [ ] A. Answering an intervention question needs only a larger observational sample.
- [ ] B. A decision changes something in the world, so the question that matters for a decision is usually an intervention question.
- [ ] C. A model can predict an outcome accurately and still give harmful advice if its inputs are acted on.
- [ ] D. Intervention questions can be answered from observational data with no assumptions beyond the data.
- [ ] E. Any model that predicts the outcome well from X also tells us what happens to the outcome when we change X.

**12.** A researcher finds that counties with more police officers per resident report more crime per resident, and asks whether employing more officers increases crime. Here the treatment is the number of officers per resident and the outcome is the crime rate. Check each variable that is a confounder in this situation.  *(5 points)*

- [ ] A. The number of arrests made last year, which depends both on how many officers there are and on how much crime occurs.
- [ ] B. Public satisfaction with the police, measured in a survey after the officers were hired.
- [ ] C. How much crime the county had in earlier years, which led its government to hire more officers and also predicts crime today.
- [ ] D. Officers' overtime hours, which rise when there are more crimes to respond to.
- [ ] E. A state grant that pays for officers' salaries, which lets a county hire more officers and has no other path to crime than through those officers.

**13.** Check each statement that is true about observational data.  *(5 points)*

- [ ] A. In observational data the investigator did not assign the treatment; people or circumstances determined who received it.
- [ ] B. Any dataset taken from existing records is observational, even if the treatment in those records was assigned by chance.
- [ ] C. A dataset with millions of rows can still be observational.
- [ ] D. Observational data records the treatment but not the outcome.
- [ ] E. Whether data is observational depends on how the treatment came about, not on how carefully the variables were measured.

**14.** A health researcher lists studies that have been done on the effect of a treatment. Check each study that uses observational data.  *(5 points)*

- [ ] A. Researchers pull a hospital's past records and compare patients who were given an antibiotic by their doctors with patients who were not.
- [ ] B. A survey asks adults whether they take a daily vitamin and whether they had a fracture this year.
- [ ] C. An analyst compares test scores of students in schools that chose to adopt a new curriculum with schools that did not.
- [ ] D. A website randomly shows half of its visitors a new layout and then measures purchases.
- [ ] E. A bank compares repayment of customers who chose to use its mobile app with customers who did not.

**15.** Researchers randomly assign 500 volunteers to use a study app or not, then compare exam scores. Check each statement that is true.  *(5 points)*

- [ ] A. Random assignment guarantees the two groups are identical on every characteristic in any single trial.
- [ ] B. The difference in average scores is an estimate of the app's effect, with some chance error.
- [ ] C. An observational comparison of students who chose the app is weaker, because the choice itself may relate to ability.
- [ ] D. Randomization does not remove chance error, so the estimated effect still carries uncertainty.
- [ ] E. Random assignment breaks the link between a student's prior ability and whether they get the app.

**16.** A hospital model predicts readmission, and an attribution method shows that 'number of prior visits' carries the most weight. A manager proposes cutting visits to reduce readmissions. Check each statement that is true.  *(5 points)*

- [ ] A. A feature's importance in a model is the same thing as its causal effect.
- [ ] B. Acting on the attribution as if it were a causal effect treats a rung 2 result as a rung 1 answer.
- [ ] C. Frequent visits may be a sign of illness severity, which also drives readmission.
- [ ] D. The high weight shows that reducing visits would reduce readmissions.
- [ ] E. The attribution describes how the model uses the feature, which is an association learned from past data.

**17.** A trial randomly assigns 2,000 patients to take a new drug or a placebo and compares recovery. Check each statement that is true about what randomization does in this trial.  *(5 points)*

- [ ] A. On average, factors such as age and prior health end up similar in the two groups.
- [ ] B. In a trial of ten patients, it ensures that the two groups match closely on age.
- [ ] C. It breaks the link between a patient's prior health and whether the patient receives the drug, so prior health is not a confounder here.
- [ ] D. It makes the recovery measurements more accurate.
- [ ] E. It lets researchers estimate the drug's effect without having measured every factor that affects recovery.

**18.** A bank's attribution tool says income contributed most to a loan denial. A reviewer asks what that does and does not show. Check each statement that is true.  *(5 points)*

- [ ] A. It shows that raising the applicant's income would raise their real ability to repay.
- [ ] B. Varying the model's inputs shows how the model responds, not how the applicant or the world would respond.
- [ ] C. It shows how the model weighs income when it scores this applicant.
- [ ] D. Treating the attribution as a reason the applicant would repay confuses association with intervention.
- [ ] E. It cannot say whether income is a cause of repayment or a stand-in for something correlated with it.

**19.** A team writes down the quantity P(recovery | patient took the drug), estimated from hospital records in which doctors chose who got the drug. Check each statement that is true.  *(5 points)*

- [ ] A. 'What would the recovery rate be if every patient were given the drug?' is an association question.
- [ ] B. It equals the recovery rate if every patient were given the drug, as long as the sample is large.
- [ ] C. It can be estimated without anyone assigning the treatment.
- [ ] D. It answers an association question: among patients who took the drug, how often did they recover?
- [ ] E. It tells the team what would happen to a patient if the hospital assigned the drug to that patient.

**20.** A vendor says its AI tutor 'improves grades' because students who used it scored higher than students who did not. Check each statement that is true.  *(5 points)*

- [ ] A. A skeptic would ask who chose to use the tutor and what else differs between users and non-users.
- [ ] B. The claim is about an intervention, but the evidence is an association.
- [ ] C. Higher scores among users prove the tutor works.
- [ ] D. Only random assignment can strengthen the claim; no adjustment for what drives who uses the tutor ever can.
- [ ] E. The claim is safe because users and non-users were both compared.
