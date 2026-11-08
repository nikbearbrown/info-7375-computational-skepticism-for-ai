# Chapter 6: Bias, where it enters and who is responsible

## MA-ch06.52

A city compares the end-of-year exam scores of students who attended a free after-school tutoring program with those who did not, to learn whether tutoring raises scores. Families choose whether to enrol; places are not assigned by lottery. Here the treatment is attending the tutoring program and the outcome is the exam score. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The student's grades in the previous year, which influence whether a family enrols the child and also influence this year's exam score.
- [ ] B. The number of tutoring sessions the student attends after enrolling, which tutoring produces and which in turn raises the exam score.
- [ ] C. Whether the student later wins a scholarship, which is more likely both for students who were tutored and for students with high exam scores.
- [ ] D. How involved the parents are in schoolwork, which makes enrolment more likely and also raises exam scores.
- [ ] E. The student's sleep on the night before the exam, which affects the exam score but is unrelated to whether the family enrolled the child.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: It affects both the treatment (whether a family enrols) and the outcome (the exam score), so it is a confounder.
- B: It lies on the path from tutoring to the score (tutoring causes it), so it is part of how tutoring would work, not a confounder.
- C: The scholarship is an effect of both tutoring and the score, not a cause of either; a variable caused by both is not a confounder.
- D: Involved parents both enrol their children and help with schoolwork, so this variable affects both the treatment and the outcome and is a confounder.
- E: It affects the outcome but is unrelated to the treatment, so it cannot confound the comparison.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.53

A hospital switches on an AI discharge-planning tool in some wards and not others; each ward chose whether to adopt it. Wards that adopted it have lower 30-day readmission rates, and management asks whether the tool reduces readmissions. Here the treatment is a ward adopting the tool and the outcome is its readmission rate. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The number of follow-up calls made after discharge, which the tool triggers and which then lower readmissions.
- [ ] B. How sick the typical patient in the ward is, since wards with sicker patients were less likely to adopt the tool and also have more readmissions.
- [ ] C. The number of readmission entries that appear in next year's hospital database, which is produced by the readmissions themselves.
- [ ] D. The staff-satisfaction score for the tool, which is reported by wards that use the tool.
- [ ] E. The seniority of the ward's physicians, since wards led by senior physicians adopted the tool earlier and also manage patients' care more effectively.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: The tool causes the calls and the calls lower readmissions, so the variable is on the path from tool to outcome (a mediator), not a confounder.
- B: It influences both which wards adopt the tool and the readmission rate, so it is a confounder.
- C: It is an effect of the outcome, not a cause of the tool's adoption or of readmissions.
- D: It exists as a result of using the tool, so it follows the treatment; it cannot be a cause of it.
- E: Physician seniority shapes both adoption and readmission outcomes, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.54

A company compares performance ratings of employees who work remotely with those who work on site, to learn whether remote work raises performance. Employees negotiate with their managers about who works remotely. Here the treatment is working remotely and the outcome is the performance rating. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. Seniority, since senior staff are more likely to be allowed to work remotely and also tend to receive higher ratings.
- [ ] B. Hours of uninterrupted focus time, which remote work increases and which in turn raises the rating.
- [ ] C. Whether the role is mainly software engineering, since engineers are more often remote and are rated against different norms that shift their ratings.
- [ ] D. The size of the year-end bonus, which is paid partly according to the performance rating.
- [ ] E. The employee's commute length, which affects who asks to work remotely but has no effect on the rating.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Seniority influences both who works remotely and the rating, so it is a confounder.
- B: It is caused by the treatment and then affects the outcome (a mediator), so it is part of the effect, not a confounder.
- C: Role influences who works remotely and how ratings come out, so it is a confounder.
- D: It is an effect of the outcome, not a cause of remote work or of the rating.
- E: It affects the treatment only. A variable related to the treatment but not to the outcome cannot confound the comparison.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.55

A registry shows that adults who take a daily vitamin D supplement have fewer bone fractures than adults who do not. Researchers ask whether the supplement prevents fractures. People decide for themselves whether to take it. Here the treatment is taking the supplement and the outcome is having a fracture. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. Bone density measured a year after starting, which the supplement raises and which lowers the risk of fracture.
- [ ] B. The brand of supplement bought by those who take it, which varies among users and has no effect on fracture risk.
- [ ] C. How health-conscious the person is, since health-conscious people are more likely to take supplements and also less likely to be injured.
- [ ] D. Whether the person is later prescribed a walking aid, which is more likely after a fracture.
- [ ] E. Age, since older adults are more likely to take the supplement and also more likely to fracture a bone.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The supplement causes it and it then affects fractures, so it is on the path from treatment to outcome, not a confounder.
- B: It is a detail of the treatment and is unrelated to the outcome, so it does not confound.
- C: It influences both taking the supplement and the chance of a fracture, so it is a confounder.
- D: It is an effect of the outcome, so it cannot be a cause of either variable.
- E: Age influences both the treatment and the outcome, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.56

A researcher collects 60 published language models and compares coding-benchmark scores for models trained with a new technique and models trained without it, to learn whether the technique improves scores. Each lab decided whether to use the technique. Here the treatment is using the technique and the outcome is the benchmark score. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. Model size, since labs that adopt the new technique tend to train larger models, and larger models tend to score higher.
- [ ] B. The model's rank on the public leaderboard, which is assigned from the benchmark scores.
- [ ] C. The amount of training text, since well-resourced labs both adopt new techniques early and train on more text, which raises scores.
- [ ] D. The experience of the lab's engineering team, since experienced teams adopt new techniques sooner and also tune their models better.
- [ ] E. The number of citations the technique's paper receives, which grows when models using it score well.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Size is linked to the choice of technique and to the score, so it is a confounder.
- B: Rank is computed from the outcome, so it is an effect of the outcome and cannot confound.
- C: The amount of text is tied to the technique (through the lab's resources) and raises scores, so it is a confounder.
- D: Team experience influences both the adoption of the technique and the quality of the result.
- E: Citations are a downstream effect of results, not a cause of adoption or of scores.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.57

An online shop lets customers opt in to a "personalised picks" panel. Customers who opted in spent more in the following month, and the shop asks whether the panel increases spending. Customers choose whether to opt in. Here the treatment is opting in to the panel and the outcome is spending in the following month. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The number of items the customer views in the panel, which appears after a customer opts in and leads to purchases.
- [ ] B. How much the customer spent in the month before the panel was offered, which predicts both who opts in and spending afterwards.
- [ ] C. Whether the customer leaves a product review, which is more likely both for customers who used the panel and for customers who bought a lot.
- [ ] D. How often the customer visits the site, which makes opting in more likely and also leads to more purchases.
- [ ] E. Whether the customer holds a loyalty membership, which prompts customers to try new features and also brings discounts that raise spending.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: It lies between opting in and spending (a mediator), so it is part of the effect, not a confounder.
- B: Earlier spending is linked to both the choice to opt in and later spending, so it is a confounder.
- C: Reviewing is an effect of both variables, not a cause of either; a variable caused by both is not a confounder.
- D: Visit frequency influences both the treatment and the outcome, so it is a confounder.
- E: Membership influences both opting in and spending, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.58

Researchers find that cities with more protected bike lanes have lower adult obesity rates, and ask whether bike lanes reduce obesity. Each city decides for itself how many lanes to build. Here the treatment is the number of bike lanes and the outcome is the obesity rate. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. City wealth, since richer cities can afford more lanes and also tend to have lower obesity rates.
- [ ] B. Climate, since mild-weather cities are more likely to build lanes and also have residents who exercise outdoors more.
- [ ] C. The share of residents who cycle to work, which the lanes encourage and which burns calories.
- [ ] D. The number of news stories about obesity published in the city, which rises when obesity rates are high.
- [ ] E. A city health department that funds active-living programs, which leads the city both to build lanes and to run other programs that lower obesity.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Wealth influences both lane building and obesity, so it is a confounder.
- B: Climate influences both lane building and activity levels, so it is a confounder.
- C: The lanes cause it and it then affects obesity, so it is on the path from treatment to outcome.
- D: It is an effect of the outcome, not a cause of lane building or of obesity.
- E: One source drives both lane building and other obesity-reducing programs, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.59

A job board finds that applicants who paid for a résumé-writing service were hired more often than applicants who did not, and asks whether the service raises the chance of being hired. Applicants decide whether to pay. Here the treatment is paying for the service and the outcome is being hired. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The number of interviews the applicant gets, which a polished résumé produces and which leads to job offers.
- [ ] B. Years of work experience, which affect whether an applicant seeks out the service and also how attractive the applicant is to employers.
- [ ] C. Whether the applicant accepts the job offer, which follows being hired.
- [ ] D. The applicant's spare income, which makes paying for the service possible and also pays for coaching and networking that help in hiring.
- [ ] E. The number of open positions at the employer, which changes applicants' chances of being hired but is unrelated to who pays for the service.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The service causes it and it then affects hiring, so it is on the path from treatment to outcome, not a confounder.
- B: Experience influences both the choice to pay and the chance of being hired, so it is a confounder.
- C: It comes after the outcome, so it cannot be a cause of either variable.
- D: Spare income influences both the treatment and the outcome, so it is a confounder.
- E: It affects the outcome but is unrelated to the treatment, so it cannot confound the comparison.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.60

A researcher finds that counties with more police officers per resident report more crime per resident, and asks whether employing more officers increases crime. Here the treatment is the number of officers per resident and the outcome is the crime rate. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The number of arrests made last year, which depends both on how many officers there are and on how much crime occurs.
- [ ] B. Public satisfaction with the police, measured in a survey after the officers were hired.
- [ ] C. How much crime the county had in earlier years, which led its government to hire more officers and also predicts crime today.
- [ ] D. Officers' overtime hours, which rise when there are more crimes to respond to.
- [ ] E. A state grant that pays for officers' salaries, which lets a county hire more officers and has no other path to crime than through those officers.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Arrests are an effect of both the treatment and the outcome, not a cause of either; such a variable is not a confounder.
- B: It follows the treatment, so it cannot be a cause of it.
- C: Past crime drives the hiring of officers and predicts present crime, so it is a confounder.
- D: Overtime is an effect of the outcome, not a cause of either variable.
- E: It affects the treatment (how many officers a county can hire) and reaches the outcome only through that treatment, so it is not a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.61

A bank offers customers an optional budgeting app. Customers who use it have lower rates of missed loan payments, and the bank asks whether the app reduces missed payments. Customers choose whether to use it. Here the treatment is using the app and the outcome is missing loan payments. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The customer's credit score, which affects who chooses to download the app and also how likely they are to miss payments.
- [ ] B. The number of low-balance alerts the customer receives, which the app sends and which prompt customers to keep payments up.
- [ ] C. Stability of the customer's income, which affects both the habit of using budgeting tools and the ability to make payments.
- [ ] D. Whether the account is later sent to collections, which follows missed payments.
- [ ] E. How comfortable the customer is with money matters, which makes using a budgeting app more likely and also makes missed payments less likely.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Credit score influences both the treatment and the outcome, so it is a confounder.
- B: The app causes the alerts and they then affect payments, so they are on the path from treatment to outcome.
- C: Income stability influences both variables, so it is a confounder.
- D: It is an effect of the outcome, not a cause of either variable.
- E: Financial confidence influences both whether the app is used and whether payments are missed.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.62

A survey finds that adults who eat breakfast every day have a lower body-mass index (BMI) than adults who skip it, and a writer concludes that eating breakfast lowers BMI. Here the treatment is eating breakfast and the outcome is BMI. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. Working night shifts, which makes skipping breakfast likelier and also disrupts sleep in ways that raise weight.
- [ ] B. Snacking later in the morning, which is less likely after breakfast and adds calories.
- [ ] C. A genetic tendency to gain weight, which affects BMI but is unrelated to whether the person eats breakfast.
- [ ] D. Buying clothes in a larger size, which follows from a higher BMI.
- [ ] E. How health-conscious the person is, which makes eating breakfast more likely and also leads to lower weight.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Shift work influences both breakfast habits and weight, so it is a confounder.
- B: Eating breakfast changes it and it then affects weight, so it is on the path from treatment to outcome.
- C: It affects the outcome but is unrelated to the treatment, so it is not a confounder.
- D: A larger clothing size is an effect of the outcome, not a cause of either variable.
- E: Health-consciousness influences both variables, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.63

A university finds that students who used an AI writing assistant on their essays received higher grades, and asks whether using the assistant raises grades. Students decide for themselves whether to use it. Here the treatment is using the assistant and the outcome is the essay grade. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The student's earlier writing skill, which affects whether the student chooses to use the assistant and also affects essay grades.
- [ ] B. The hours the student has available for the course, which make trying the assistant more likely and also leave more time to polish essays.
- [ ] C. Whether the instructor flags the essay as AI-assisted, which is more likely both when the assistant was used and when the essay reads as polished.
- [ ] D. The student's ambition to earn a high grade, which makes using any available help more likely and also leads to more careful work.
- [ ] E. The student's major, since some majors encourage the assistant and also grade writing more generously.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Skill influences both the treatment and the outcome, so it is a confounder.
- B: Available time influences both variables, so it is a confounder.
- C: The flag is an effect of both the treatment and the quality of the work, not a cause of either; it is not a confounder.
- D: Ambition influences both the treatment and the outcome, so it is a confounder.
- E: Major influences both whether the assistant is used and how grades come out, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.64

A registry finds that women who attend regular mammogram screening die less often of breast cancer than women who do not, and asks whether screening reduces deaths from breast cancer. Women choose whether to attend. Here the treatment is attending screening and the outcome is dying of breast cancer. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The stage at which a cancer is found, which screening shifts earlier and which affects survival.
- [ ] B. How health-conscious the woman is, which makes attending screening more likely and also leads to healthier habits and earlier care.
- [ ] C. Whether the woman has health insurance that covers screening, which makes attending more likely and also gives access to better treatment.
- [ ] D. Having a regular doctor who reminds patients about preventive care, which raises attendance and also improves follow-up after any diagnosis.
- [ ] E. The number of biopsies performed, which rises after screening finds suspicious spots.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Screening causes the change in stage and stage then affects survival, so it is on the path from treatment to outcome.
- B: Health-consciousness influences both attendance and outcomes, so it is a confounder.
- C: Insurance influences both attendance and treatment quality, so it is a confounder.
- D: A regular doctor influences both attendance and outcomes, so it is a confounder.
- E: Biopsies are an effect of the treatment, so they cannot be a cause of it.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.65

Parents notice that children who play a musical instrument have higher maths scores, and ask whether learning an instrument raises maths scores. Here the treatment is playing an instrument and the outcome is the maths score. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. Hours of daily practice, which are accumulated by children who play an instrument and which may build focus.
- [ ] B. Membership in the school orchestra, which follows from playing an instrument.
- [ ] C. Whether the child enters a maths competition, which is more likely for children who already have high scores.
- [ ] D. Family income, which affects whether a family can afford lessons and instruments and also affects the resources that support learning maths.
- [ ] E. The parents' level of education, which affects whether children are steered toward music lessons and also how well they are helped with maths.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Playing causes the practice hours and they may then affect maths scores, so they are on the path from treatment to outcome.
- B: It is an effect of the treatment, so it cannot be a cause of it.
- C: It is an effect of the outcome, not a cause of either variable.
- D: Income influences both the treatment and the outcome, so it is a confounder.
- E: Parental education influences both the treatment and the outcome, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.66

An insurer finds that cars with automatic emergency braking are involved in fewer crashes per mile, and asks whether the braking system prevents crashes. Drivers choose which car to buy. Here the treatment is having automatic emergency braking and the outcome is crashes per mile. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The driver's usual caution, since careful drivers are more likely to choose safety options and also less likely to crash.
- [ ] B. The price of the car, since more expensive cars more often include the system and are more often bought by drivers who maintain them well.
- [ ] C. The number of hard-braking events the car logs, which the system triggers and which avoid collisions.
- [ ] D. Whether the car is new, since new cars are more likely to have the system and less likely to have worn brakes or tyres.
- [ ] E. The insurance premium for the next year, which rises after a crash.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Caution influences both the choice of the option and crash risk, so it is a confounder.
- B: Price is tied to both having the system and crash risk, so it is a confounder.
- C: The system causes the events and they then affect crashes, so they are on the path from treatment to outcome.
- D: Car age influences both having the system and crash risk, so it is a confounder.
- E: The premium is an effect of the outcome, not a cause of either variable.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.67

A district finds that schools which give every student a laptop have higher average test scores, and asks whether laptops raise scores. Each school decides whether to buy them. Here the treatment is a school providing laptops and the outcome is the school's average test score. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The school's funding per student, which pays for laptops and also pays for teachers, books and support.
- [ ] B. The poverty rate in the school's neighbourhood, which limits both the school's ability to buy laptops and students' test scores.
- [ ] C. An active parent association, which raises money for laptops and also supports learning at home.
- [ ] D. The time students spend on educational apps at school, which laptops make possible and which raises scores.
- [ ] E. The share of students with internet access at home, which makes a laptop programme workable and also helps students study.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Funding influences both laptop provision and scores, so it is a confounder.
- B: Neighbourhood poverty influences both variables, so it is a confounder.
- C: The association influences both laptop provision and student performance, so it is a confounder.
- D: Laptops cause the app time and it then affects scores, so it is on the path from treatment to outcome.
- E: Home internet access influences both the programme and the outcome, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.68

A company finds that teams that run an AI code scanner on every commit have fewer security breaches, and asks whether the scanner prevents breaches. Teams choose whether to run it. Here the treatment is running the scanner and the outcome is the number of breaches. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The number of scanner alerts per commit, which is produced when a team runs the scanner.
- [ ] B. How mature the team's security practices are, which leads teams to adopt scanners and also reduces breaches.
- [ ] C. The vulnerabilities fixed after scanner alerts, which the scanner prompts and which prevent breaches.
- [ ] D. Bug-bounty payouts, which rise when more breaches occur.
- [ ] E. Whether the team's code is hosted on the platform that offers the scanner as a one-click setting, which makes adoption easier and has no other path to breaches than through the scanner.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Alerts are an effect of the treatment, so they cannot be a cause of it.
- B: Security maturity influences both the adoption of the scanner and the number of breaches, so it is a confounder.
- C: The scanner causes the fixes and the fixes then affect breaches, so they are on the path from treatment to outcome.
- D: Payouts are an effect of the outcome, not a cause of either variable.
- E: It affects the treatment and reaches the outcome only through that treatment, so it is not a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.69

A fitness company finds that customers who wear its step-tracking watch lose more weight over a year than customers who do not, and asks whether wearing the watch causes weight loss. Customers choose whether to buy the watch. Here the treatment is wearing the watch and the outcome is weight loss over the year. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. The number of daily step goals met, which the watch's reminders increase and which burns calories.
- [ ] B. How strongly the customer wants to lose weight, which makes buying a tracker more likely and also leads to dieting.
- [ ] C. The customer's spare income, which pays for the watch and also for gym membership and healthier food.
- [ ] D. Existing exercise habits, such as running regularly, which make buying a tracker more likely and also produce weight loss.
- [ ] E. Membership in a running club, which leads people to buy trackers and also keeps them active.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The watch causes the goals to be met and meeting them then affects weight, so it is on the path from treatment to outcome.
- B: Motivation influences both the treatment and the outcome, so it is a confounder.
- C: Spare income influences both the treatment and the outcome, so it is a confounder.
- D: Prior habits influence both buying the watch and weight change, so they are confounders.
- E: Club membership influences both variables, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.70

A company finds that teams using a code-review bot ship fewer bugs per release, and asks whether the bot reduces bugs. Teams choose whether to use it. Here the treatment is using the bot and the outcome is the number of bugs shipped per release. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. Review comments resolved before merging, which the bot generates and which remove bugs.
- [ ] B. The experience of the team's developers, which makes adopting new tools likelier and also leads to fewer bugs.
- [ ] C. How much management values code quality, which leads teams to adopt tooling and also to test more.
- [ ] D. Customer support tickets about bugs, which are caused by the bugs that ship.
- [ ] E. How complex the project is, since simpler projects are easier to automate with a bot and also easier to keep free of bugs.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The bot causes the comments and resolving them then affects bugs, so they are on the path from treatment to outcome.
- B: Experience influences both the treatment and the outcome, so it is a confounder.
- C: A quality-minded culture influences both adoption and the number of bugs, so it is a confounder.
- D: Tickets are an effect of the outcome, not a cause of either variable.
- E: Complexity influences both the use of the bot and the number of bugs, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2

## MA-ch06.71

Runners who wore carbon-plated shoes finished a race faster on average than runners in ordinary shoes, and a magazine asks whether the shoes make runners faster. Runners chose their own shoes. Here the treatment is wearing carbon-plated shoes and the outcome is the finishing time. Check each variable that is a confounder in this situation. Each statement is worth 1 point (5 points total).

- [ ] A. Weekly training mileage, since serious runners more often buy racing shoes and also train harder.
- [ ] B. Race-day weather, which changes finishing times but is the same for runners in both kinds of shoes.
- [ ] C. Years of running experience, which shape shoe choices and also pace.
- [ ] D. Membership in a competitive club, which leads runners to racing shoes and to coaching that makes them faster.
- [ ] E. The runner's budget, which makes buying expensive shoes possible and also pays for coaching and race entries.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Training volume influences both shoe choice and finishing time, so it is a confounder.
- B: It affects the outcome but is unrelated to the treatment, so it cannot confound the comparison.
- C: Experience influences both the treatment and the outcome, so it is a confounder.
- D: Club membership influences both variables, so it is a confounder.
- E: Budget influences both the treatment and the outcome, so it is a confounder.

**Source:** Pearl's Ladder — Rungs 1 and 2
