# Gru turn 10-v1-deployment-why

## Professor Bear typed

```
Category: accepted as you wrote it, a local, scheduled change-detector with a scored, explainable filter.

Why local: the résumé. search/resume.json is a real person's résumé, gitignored on purpose; the engine's rules say it is never committed, never copied into a fixture or a log, and the course has had privacy incidents from exactly that. A hosted service would have to hold every student's résumé. Running on her laptop means it never leaves. Second reason, the course: students are meant to read and change the matching scheme themselves, which is easier when the code and the scheme sit in front of them. Third, it costs nothing.

Why Claude Code: you're right to push. Claude does no work at runtime. The skill is a stored Python script; fetching, diffing, and scoring are deterministic, and the scheme file is the whole rule. Claude Code is how a student launches it, reads the report back, and is told to stop at the human gate. A scheduled run can call the script directly with no Claude at all, and that's what a cron line or GitHub Action should do.
```

## Gru replied (verbatim, unedited)

Category is locked. The answer on Claude Code is the clearest thing you've told me: **the runtime is deterministic, and Claude only launches the run and reads the report back.** I'm taking that forward as a candidate for an architecture principle in /v2. It also settles a scheduling detail: scheduled runs call the script directly, and Claude isn't involved.

Your privacy answer creates **two contradictions with things you've already confirmed**. I can't absorb either of them. Both involve the one rule you told me has already caused incidents in this course.

**Contradiction 1: a GitHub Action versus "the résumé never leaves her laptop."**
In /v1 question 6 you listed a GitHub Action as a supported scheduler. A GitHub Action runs on GitHub's machines, not Priya's. For it to score postings against her résumé, the résumé has to be in the repo, which your rules forbid, or be stored as a repository secret, which still means it leaves her laptop and sits on GitHub's infrastructure. You can't have both "a hosted service would have to hold the résumé, so we run locally" and "schedule it with a GitHub Action." One of these has to go:
- **(a)** Drop GitHub Actions as a supported scheduler. Only launchd and cron, both local.
- **(b)** Keep GitHub Actions, but only with a reduced input that isn't the résumé. For example, a keyword list the student writes by hand and agrees to make public. Then it's a different input with a different privacy boundary, and it has to be documented as that.
- **(c)** Allow it as a secret and write down an explicit exception to the privacy rule. I'd push hard against this one given the incident history. But it's your decision, and a documented exception is better than a silent one.

**Contradiction 2: "never copied into a log" versus the output you confirmed in /v0.**
Your /v0 sentence says the JSON log lists each match "with the résumé field and posting field behind every match." If that citation includes the résumé field's **value** ("PyTorch, 3 years, Wayfair"), then every run copies parts of her résumé into a log file. Your rule says that can never happen. Whether it's a real violation depends on three things I don't know:
- Does the citation record the **path** (`skills[3]`) or the **value**?
- Where do the log and report go, and are those folders gitignored?
- Does the Markdown report she reads follow the same rule as the JSON log, or a different one? A report shown to her on her own screen is different from a log file that might get committed, shared, or pasted into a course submission.

This isn't a small detail. The feature you named as the main advantage over bookmarks ("cited reasons") is the one most likely to break the privacy rule. That's exactly the kind of design argument that ends up in the wrong place, between two engineers in an incident review. It needs a decision now, not in implementation.

Resolve both, and then we go to question 7 (build scale: who builds and maintains the corrective version, the timeline, and whether there's any budget).

**Open Questions Log (additions, pending your answer):**
- **OQ-6: GitHub Actions scheduling contradicts local-only résumé handling.** Options a, b, and c above. Owner: you. Due: now. Blocks: /v1 closure.
- **OQ-7: Match citations may copy résumé values into the log and report.** Needs: path versus value; where outputs go and whether they're gitignored; whether the report and the log follow different rules. Owner: you. Due: now. Blocks: /v1 closure.
