# Gru turn 12-v1-build-scale

## Professor Bear typed

```
Accepted: both obligations from OQ-6 and OQ-7 go on the task list, and the paste-into-submission risk goes in /p4 as accepted, with the banner as a weak mitigation.

OQ-8, and it's worse than "a default can change": the script has no default at all. --out is a required argument and accepts any path; search/greenhouse-watch/ appears only in the documented command. So today the boundary is a convention in the docs. Option (b): output can go anywhere, but the script refuses a tracked path when the input is the real résumé. That keeps persona runs flexible (they are meant to be committed as examples) and puts the check where the risk is.

7. Build scale:
- Who builds it: I decide and review; Claude Code writes the changes and tests, the way the report-line fix went in. Students don't maintain this document's scheme. Each student's own scheme file replaces the default, and editing it is their assignment, so student schemes are out of scope here. This document covers the script and the default scheme.
- Timeline: no fixed date. But a Fall assignment already points students at this skill, so every week it ships with the boilerplate problem is a week of students trusting a bad match count.
- Budget: nothing paid. No paid APIs; building runs under my existing Claude subscription. The real limit is politeness to the boards: SmartRecruiters needs one detail call per posting, spaced about 0.05 seconds apart, so a 248-posting board takes about three and a half minutes.
```

## Gru replied (verbatim, unedited)

All of it goes on the list. Your answer to question 7 gives me what the Boondoggle Score will need later: **you decide and review, Claude Code writes the changes and the tests.** Three things before question 8. One is a precision problem in OQ-8, one is a consequence of the scope you just set, and one is arithmetic.

**1. OQ-8: Decided, option (b). But "tracked" is the wrong test.**
Now that you've confirmed there's no default output path, the boundary exists only in the docs, so this fix is necessary, not optional. The rule as you worded it has two gaps, though:
- **"Tracked path."** A new file in a folder that isn't gitignored isn't tracked *yet*. Nothing stops a run from writing it, and the next `git add .` commits it. The test should be "**is this path gitignored**," not "is this path tracked." In git terms, that's `git check-ignore`, not `git ls-files`.
- **"When the input is the real résumé."** If "real" means the path `search/resume.json`, a student who copies their résumé to `~/Desktop/me.json` gets past the check. It's safer to turn the rule around: **only the persona files in `search/examples/` are allowed to write to a non-ignored path. Any other résumé input must write to a gitignored path.** Name the safe inputs, not the one unsafe one.

Taken together, the rule becomes: *refuse unless the output path is gitignored, or the input résumé is one of the personas under `search/examples/`.* Confirm that wording, or tell me why yours is better. I'm logging OQ-8 as Decided (b), with the exact rule pending your confirmation.

**2. Taking student schemes out of scope means the boilerplate fix has to live in the script.**
You've scoped this document to *the script plus the default scheme*, and each student's scheme **replaces** the default. So wherever the Writer fix goes decides who gets it:
- **If it's in the default scheme** (a list of excluded fields, say), every student who has already replaced the default keeps the 51/51 bug. Their scheme is out of scope, so the fix never reaches them.
- **If it's in the script** (it separates the job's own text before *any* scheme scores it), every scheme gets it, including students' own.

Given what you said about timeline, that students are trusting a bad match count *now*, this isn't a question of style. I'm recording it as a constraint on corrective claim 1: **job-text isolation belongs in the script, before scoring, and no scheme can turn it off.** If you disagree, tell me now. Otherwise it goes into /v2 as a principle.

**3. Your SmartRecruiters numbers don't add up.**
248 postings × 0.05 s = about **12 seconds**, not three and a half minutes. For 3.5 minutes, each posting has to take about **0.85 s**. So either the spacing isn't 0.05 s, or the delay is mostly the detail request itself taking roughly 0.8 s, not the spacing you add. This matters for two reasons. It's the only real runtime limit you have, and a cron job that runs past a timeout, or overlaps the next run, is a problem you only find in the logs. Which is it: the spacing you set, or how long each detail request takes to come back?

**Recorded from question 7:**
- **Builders:** you (decide and review) and Claude Code (changes and tests).
- **Scope:** the script and the default scheme. Student scheme files go to /p2 as out of scope.
- **Timeline:** no date, but it's urgent. The Fall assignment is already sending students to a tool with a bad match count. That argues for shipping corrective claim 1 on its own, first. I'll raise it in /p1, not decide it here.
- **Budget:** $0 at runtime. The build runs on your existing subscription. The limit is courtesy to the boards and the time each request takes (pending the arithmetic above).

**8. Name three systems Priya already relies on in her search, and for each one, the specific capability this tool has to work with or replace.** Her bookmarks and spreadsheet are obvious candidates, but go further than "replaces the bookmarks":
- **The spreadsheet.** Does the watcher's output go into it, replace it, or sit beside it? If she still copies matches into the spreadsheet by hand, part of the chore is still there.
- **The role scorer.** It isn't a system *she* uses directly, but it's the engine's other opinion about the same posting. What's her workflow when the watcher reports a match: does she run the scorer on it by hand?
- **Whatever else she really uses:** LinkedIn, Handshake, her school's career portal. Name one, and what the watcher does *not* take over from it.
