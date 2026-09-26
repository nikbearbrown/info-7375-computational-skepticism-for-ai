# greenhouse-watch demo: Professor Bear watches Figma

## Executive summary

**What this is.** A worked example of the Reallocation Engine's `greenhouse-watch` skill. It checks one company's public job board, finds the postings that are new since the last check, and keeps only the ones that match a résumé, with a written reason for each one it keeps. The résumé is Professor Bear's CV with every piece of personal information removed. The company is Figma.

**Why read it.** This is the smallest honest version of the engine's argument. The slow part of a job search is not clicking Apply. It is the research that decides where to apply. A tool that does that research leaves you time for networking and for building things people can see (the 3-3-2 split: three hours networking, three building credibility, two researching and applying).

**What it found.**
- **Four days of watching:** Figma posted 11 new jobs between September 19 and September 23, and took down 3. **None of the 11 match Professor Bear.** That is the normal, healthy result: most of what a company posts is not for you, and the tool told you so in seconds.
- **The whole board, treated as new:** out of 160 postings, the rules flag **3** (AI Applied Scientist, Software Engineer – Machine Learning, Software Engineer – AI Product) and skip 157.
- **What the rules miss:** the roles a teaching professor might actually want, such as *Designer Advocate* or *Researcher, Figma Agentic Experiences*, are skipped. They share almost no keywords with the CV. The rules also drop every Director role on principle. The tool is only as good as its matching scheme, and fixing that scheme is the student's job.
- **A bug found and fixed:** while building this demo, the report's "why" lines did not add up to the score. The skill was fixed and a test added (details below).

**What it did not do.** It did not apply anywhere, contact anyone, or judge whether any job is good. Every verdict is a word-for-word match between the résumé and the posting. Deciding which job, if any, is worth a day of your life stays with the person.

---

## What is in this folder

| Path | What it is |
|---|---|
| `resumes/professor-bear.json` | The CV in the skill's résumé format. Contact details, links, other people's names, grant numbers, and URLs removed. Skills list only what the CV text states (no Python, for example, because the CV never says it). Marked `attested: false`. |
| `snapshots/figma-2026-09-19.json` | Figma's public board as fetched on 2026-09-19 (152 postings). Board data only, no résumé. |
| `snapshots/figma-2026-09-23.json` | Figma's public board as fetched live on 2026-09-23 at 19:54 UTC (160 postings). |
| `runs/` | **The two-day watch.** Run 1 is the baseline from the 09-19 snapshot. Run 2 reads the 09-23 snapshot and reports only what is new. Each run has a JSON record (for the agent) and a Markdown report (for you). |
| `whole-board/` | **The whole-board view.** One dry run with an empty "already seen" list, so all 160 postings count as new. This shows what the scheme flags and what it misses. |

The two snapshots are indented for reading. Figma's API sends one minified line; the data was checked identical before and after, and re-running both runs on the indented files gives the same results. The `raw-*.json` files in `runs/` and `whole-board/` are links to the matching snapshot. The skill saves a copy of the board response on every run, and those copies hold the same data as the snapshot, so they are linked instead of duplicated.

## How to reproduce it

From a clone of [the-reallocation-engine](https://github.com/nikbearbrown/the-reallocation-engine), with this folder as `DEMO`:

```bash
GW=.claude/skills/greenhouse-watch/scripts/greenhouse_watch.py

# run 1: baseline, records every posting, reports none
python3 $GW --board figma --resume $DEMO/resumes/professor-bear.json \
  --state $DEMO/runs/figma.state.json --out $DEMO/runs/ \
  --fixture $DEMO/snapshots/figma-2026-09-19.json

# run 2: four days later, reports only postings not seen on 09-19
python3 $GW --board figma --resume $DEMO/resumes/professor-bear.json \
  --state $DEMO/runs/figma.state.json --out $DEMO/runs/ \
  --fixture $DEMO/snapshots/figma-2026-09-23.json
```

Drop `--fixture` to fetch today's board live instead. That is one request to Figma's public Greenhouse API, and the skill refuses any other host.

## The two-day watch

| | Seen | New since last check | Relevant | Skipped |
|---|---:|---:|---:|---:|
| Run 1 (baseline, 09-19) | 152 | — | — | — |
| Run 2 (09-23) | 160 | 11 | 0 | 11 |

The 11 new postings were a data platform engineer, a data engineering internship, a PhD data science internship, an early-career product designer, a product design director, sales and office roles in Singapore and Bengaluru, an HR analyst, an executive assistant, and a machine-learning engineer in London. Three were dropped by title rule before scoring (two internships, one director). The rest either shared no skill with the CV or scored below the threshold of 3.0. Full table: `runs/report-*` (the file without `-baseline`).

## The whole-board view: what the rules flag, and what they miss

**Flagged (3 of 160):**

| Posting | Score | Why, in short |
|---|---:|---|
| AI Applied Scientist | 6.5 | seven CV skills in the posting (machine learning, deep learning, reinforcement learning, prompt engineering, generative AI, mentoring, C++); not in Boston, −1 |
| Software Engineer – Machine Learning | 3.5 | machine learning in the title; generative AI, mentoring, and C++ in the text |
| Software Engineer – AI Product | 3.0 | machine learning, generative AI, and mentoring; the posting mentions a PhD |

Every line of every justification in `whole-board/report-*.md` names the résumé field and the posting field that produced it, and the lines add up to the score.

**Missed, and why that is the lesson:**
- **Designer Advocate** scores 0: no CV skill appears in it. **Researcher, Figma Agentic Experiences** scores 0.5. A person reads "teaches, runs workshops, builds AI course assistants" and sees an advocate or researcher. A keyword scheme does not. That is a false negative, and the fix is to the scheme (the rules), not to the code or the CV.
- **Director, Research – AI Evals** is dropped before scoring. The default scheme excludes every *Director* and *VP* title because it was written for students. For a senior candidate, that rule throws away exactly the right level of role.
- **Location is a soft penalty.** Every flagged job is in San Francisco or New York, and the Boston CV only loses one point for that. For an F-1 student who must stay in one city, location should be a gate (`location_mode: hard` in the scheme), not a vote.

Each of those is a one-line change to a copy of `scheme.default.json`. Making them, and writing down why, is the part of the Fall 2026 assignment the reference skill leaves to the student.

## A bug this demo caught

The first run for an example student showed a match with justification lines of +3.0, +3.0, +1.0 and −1.0, which add up to 6.0, but a score of 3.5. The arithmetic was right and the explanation was wrong:
- The title rule is credited once, but the report printed "+3.0" for every past job title that matched.
- The small bonus for "at least one skill matched" (+0.5) was added to the score but never printed.

A reader who checked the math would stop trusting the tool, and they would be right to. The fix, [commit `015843d`](https://github.com/nikbearbrown/the-reallocation-engine/commit/015843d5047dbadff05068495e4c5db5cd9945f4) in the-reallocation-engine (`.claude/skills/greenhouse-watch/scripts/greenhouse_watch.py`):
- repeat title matches now read "already counted, +0";
- the +0.5 bonus now gets its own line;
- a new test, `test_justification_lines_sum_to_score`, fails on the old code (lines 10.0, score 7.5) and passes on the new one. All 23 skill tests pass.

## Honest limits

- **Only two data points.** Two snapshots four days apart. The live fetch happened once, on 2026-09-23; every run in this folder replays a saved snapshot offline. "Daily" has not been scheduled or tested.
- **One board, one company.** The skill also reads Ashby and SmartRecruiters boards; this demo does not exercise them.
- **The CV-to-JSON conversion was done by Claude Code.** Its owner read the full facts file on 2026-09-23 and found it accurate. The shorter résumé used for matching, and especially its skills list, is Claude's selection from that file and hasn't been separately reviewed (`attested: false`). A different selection would produce different matches.
- **Keyword matching is not fit.** A score of 6.5 means seven words matched, not that the job is a good one.
