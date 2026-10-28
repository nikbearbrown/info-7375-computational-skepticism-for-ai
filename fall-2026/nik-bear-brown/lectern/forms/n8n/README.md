# Lectern job search, as n8n workflows

## What this is, why it exists, what was found

**What.** The Lectern job-search pipeline rebuilt as five separate n8n workflows, one folder each: collect the watched companies' boards, filter with the keyword rules, diff against what was last published, post new listings to Discord, and a daily workflow that calls the four and remembers what it saw. The same pipeline exists as plain Python (the master, in the Computational Skepticism course folder) and is planned as a CrewAI version. The point is to show one pipeline in three forms and test them against each other.

**Why.** An n8n workflow looks like a dependable machine because it draws as boxes and arrows. Whether it does what the Python does is an empirical question, so the Python is the oracle: every workflow here is tested against what the Python produced for the same inputs.

**What was found (2026-10-19).**
- **The filter agrees with the Python on all 2,465 real postings** from the last run: same text, same fields, same keep decision, same matched words, same reason for every reject (81 kept by each).
- **The delta agrees** on a real pair of runs (42 new, 7 changed, 9 gone, with the same reasons), and **the Discord messages are byte-identical** to the Python's for the same new listings (30 rows, 5 messages).
- **The live HTTP path agrees** on three small real boards (Greenhouse and Ashby): every field of every posting identical to the Python's.
- **Headless, all five workflows pass** in a disposable n8n 1.113.3 profile against the Python-expected outputs, and the daily workflow behaves across three runs: everything new, then a refusal on the same day, then nothing new the next day.
- **Update 2026-10-26 (rules v0.6.0: a country rule and a K-12 rule).** The Python filter gained two gates after the keywords, both in `keywords.json`, and `shared/lib/judge.js` gained the same two. Headless, all five workflows still pass with fixtures that now include a country reject, a K-12 reject, a posting that fails both, an accented city in an allowed country, a posting in several places, and a delta row whose reason is a gate. The filter agrees with the Python on all 1,869 postings of the six boards on today's watch list (60 kept by each; the 2,465 above were from 15 boards, 6 are watched now). The place reader and the K-12 reader agree on all 12,882 distinct location lines and 68,319 distinct titles of an 84,282-posting snapshot (`tools/parity_location.py`). The delta and message parities were re-run on the same real pair of runs, which were written before the gates, so the fixtures are what exercise a gate there. The live HTTP check was not re-run: the collect step did not change. Record: `test-results/parity-2026-10-26.txt`; re-run on rules v0.6.1 (2026-10-28), all the same: `test-results/parity-2026-10-28.txt`.
- **Two things a silent workflow does badly, caught by the tests:** a missing state file made the daily workflow stop with no error and no output (fixed: it now continues as a first run), and a first run with sending on would have posted every kept listing at once (fixed: it refuses unless told otherwise).

**What is NOT done or NOT tested.**
- The Discord node has never sent a message from n8n: it needs a webhook credential. The message text and the refusal rule are tested; the sending is not.
- SmartRecruiters (Canva) is not read live: it needs a call per posting for the ad text. It is reported as unavailable, never judged on empty text.
- Not ported from the Python: the games judge and poster for the second Discord channel (`engine_rule`; the rules file is copied whole, the n8n filter ignores that block), the churn measures (`churn.py`), the business-school faculty feed (`faculty_feed.py`), the big-four collectors and their trust rules (`collectors/monitor.py`), the CSV and Markdown reports, committing and pushing, and the lab posting (`post_labs`).
- The state file is n8n's own (a different hash), not interchangeable with the Python's `published-state.json`.
- Fixtures are synthetic. The real-data parity tests need a local Lectern checkout with saved board payloads, which are not in this folder (they are full copies of companies' ads).
- This folder is not in a git repository and nothing has been pushed anywhere.

**Not the same as** `../classroom/workflows/16-lectern-skeptical-job-search`, an earlier orchestrator whose n8n nodes call a local Python service. Here the logic is in the n8n nodes themselves, and the Python is the thing it is tested against.

## The workflows

| Folder | Does | Python counterpart | Tested |
|---|---|---|---|
| [`01-collect`](01-collect/README.md) | reads each board (fixture or live), normalises the three providers' formats | `fetch_board()`, `normalise()` in `collect.py` | headless; live on 3 boards |
| [`02-filter`](02-filter/README.md) | dedupes, validates, applies `keywords.json`, gives a reason for every decision | `judge()` and the checks in `collect.py` | headless; 2,465 real postings (v0.5.2), 1,869 (v0.6.0) |
| [`03-delta`](03-delta/README.md) | new / changed / gone against the published state; an unreadable source never closes a posting | `diff()`, `write_state()` in `publish_delta.py` | headless; real pair of runs |
| [`04-post-to-discord`](04-post-to-discord/README.md) | builds the messages (watched companies only, most-wanted first, nothing twice), refuses unsafe text, sends only if `send` is on | `build_messages()` in `notify.py` | headless; byte-identical to the Python; sending not tested |
| [`05-daily`](05-daily/README.md) | calls 01 to 04, keeps the state and posted-ids files | `daily.sh` | headless, three runs |

## Run it

```bash
python3 tools/test_headless.py            # all five, in a disposable n8n profile; no network, no credentials, nothing sent
python3 tools/build.py                    # regenerate the workflow files from shared/lib/*.js and the rules
sh tools/import.sh                        # import into YOUR n8n (overwrites workflows with these ids)
```

Parity against the Python (needs a Lectern checkout; none of these send anything):

```bash
python3 tools/parity_real_data.py --lectern <lectern dir> --raw <runs/DATE/raw>
python3 tools/parity_delta.py     --lectern <lectern dir> --earlier <runs/DATE> --later <runs/DATE>
python3 tools/parity_messages.py  --lectern <lectern dir> --earlier <runs/DATE> --later <runs/DATE>
python3 tools/live_parity.py      --lectern <lectern dir>      # uses the network: public job-board APIs only
python3 tools/make_fixtures.py    --lectern <lectern dir>      # regenerate fixtures and expected outputs from the Python
python3 tools/parity_location.py  --lectern <lectern dir> --jobs-jsonl <jobs.jsonl>   # the country and K-12 readers, on a big snapshot of postings
```

## How it is laid out

- `shared/lib/*.js`: the logic, as plain functions. Each workflow's Code nodes contain a copy, generated by `tools/build.py`. The same files are loaded in Node by the parity tests, so what is tested is what is in the nodes.
- `shared/keywords.json` and `shared/boards.json`: copies of the Python's rules and watch list. **The Python folder is the master; edit it there and copy here.** The rules are never edited in a workflow.
- Each workflow has a Manual trigger that runs it on its own fixtures and an Execute Workflow trigger so that 05 can call it.
- No secrets are in any file. The Discord webhook is an n8n credential (`discordWebhookApi`) you create; the state and posted-ids paths are set in 05 · Daily > Settings.

## The three forms

| Form | Where | State |
|---|---|---|
| Python | `lectern/` in the Computational Skepticism course folder (the master) | running |
| n8n | this folder | first five workflows built and tested |
| CrewAI | not started | planned |

*Written 2026-10-19; the 2026-10-26 update is marked as such. Numbers above come from the test and parity runs named in each folder; nothing here reports a result that was not run.*
