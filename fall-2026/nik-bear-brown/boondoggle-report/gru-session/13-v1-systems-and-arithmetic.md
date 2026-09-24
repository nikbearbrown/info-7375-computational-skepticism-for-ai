# Gru turn 13-v1-systems-and-arithmetic

## Professor Bear typed

```
1. OQ-8: your wording is better. Confirmed: refuse unless the output path is gitignored, or the input résumé is one of the personas under search/examples/.

2. Agreed. Job-text isolation goes in the script, before any scheme scores, and no scheme can turn it off. Otherwise every student who already replaced the default keeps the 51/51 bug.

3. You're right, and it was my arithmetic. The script's pause is 0.05 s. The rest is the request itself: 3.5 minutes over 248 postings is about 0.8 s per detail call, and that's inferred from the total, not measured per request. It's also worse than that. Each request has a 30-second timeout, so a slow board could in principle take 248 × 30 s, about two hours, and overlap the next scheduled run. That goes to /s4 and /p4.

8. Three systems, for Priya (illustrative, since she's a persona):
- The spreadsheet: the watcher sits beside it. Today she'd copy a match in by hand. The JSON log could feed it, but no import exists, and I'm not adding one here. Part of the chore stays, and the document should say so.
- The role scorer: no bridge exists. It reads a roles.json file; the watcher writes a different format. To get the engine's Apply/Consider/Skip on a match, she'd build that input by hand. That's the gap the "notice, not a verdict" decision leaves open.
- LinkedIn: the watcher takes over nothing there. Finding the person to talk to about a role is the networking time this tool is meant to protect, not replace.
```

## Gru replied (verbatim, unedited)

All three are confirmed and logged. Your answer to question 8 does what I wanted: it says plainly what the tool **doesn't** take over. The spreadsheet chore is still there, and so is the manual step to the scorer. A document that states that is better than one that implies Priya's whole workflow gets automated. Two consequences before the last question.

**1. Overlapping runs are worse than slow runs.**
You found the two-hour worst case yourself. The more serious problem comes after it. If run A is still fetching when cron starts run B, both runs compare against the **same saved list of ids from the last run**, and both write it back. Depending on which finishes last, the next run either reports as "new" postings Priya has already seen, or never reports ones she hasn't. That silently breaks the "new is a fact" claim you gave me in question 4. Logged for /s4 as **Must-Fix**: a run needs a lock, or has to refuse to start while another run is going. Also logged for /p4.

**2. The missing bridge to the scorer is a deliberate gap, so it gets recorded as one.**
You chose "a notice, not a verdict," and the price is this: when the watcher finds a match, Priya has to build the scorer's `roles.json` by hand to get Apply/Consider/Skip. That's defensible. The watcher solves detection, and scoring comes after. But here's the risk to watch: if hand-building that input takes longer than the bookmarks used to, a student gets a notice and never acts on it. So in /p2 this isn't just "out of scope." It's out of scope with a **condition for reopening**. For example: *reopen if students report building `roles.json` by hand for watcher matches, or if the assignment requires scored output.* Name your own condition if you'd rather.

**Open Questions Log (updated):**
- **OQ-8: Decided (2026-09-24).** Refuse unless the output path is gitignored, or the input résumé is a persona under `search/examples/`.
- **Principle candidate for /v2:** job-text isolation happens in the script, before scoring, and no scheme can turn it off.
- **Deferred to /s4 (Must-Fix):** overlapping runs corrupt the saved list of ids; no run lock exists. **Deferred to /s4 and /p4:** worst-case runtime is 248 × 30 s timeout, about 2 hours; the ~0.8 s per request is inferred from the total, not measured.
- **For /p2:** a spreadsheet import (not added; the chore remains); a bridge to the scorer (reopen condition pending); LinkedIn and networking (never in scope; that's the time the tool protects); student scheme files; a public keyword input (a different product).

**9. The last intake question. Name one existing system you're explicitly *not* trying to copy, and say what specifically you're rejecting from it.**

The obvious answer is "LinkedIn job alerts," but I'd push you toward a harder one. What you're building, a scored comparison of résumé text against job-posting text, is the core of the **résumé-to-job-description keyword matchers** that job seekers already use. Those tools give you a match percentage and tell you which keywords to add. Two things in your design already push against that: cited reasons instead of a single percentage, and the tool telling Priya *which postings to look at*, not *how to rewrite her résume*. Is that the rejection? Or is the system you most need to stay distinct from a different one? Name it, and name exactly what you're refusing to copy.
