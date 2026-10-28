# CLAUDE.md — nik-bear-brown/ (Professor Bear's example folder)

This folder is the instructor's public example work for INFO 7375 Computational Skepticism for AI, Fall 2026. It keeps the same process record students keep. **Every substantive change here is logged in `FRICTIONAL.md`, and every push adds a line to it.** The repo-root `AGENTS.md` still governs everything else.

## Rule 0 — this folder is the canonical master for three classes

The same job-search tool is live-coded in Computational Skepticism, Branding and AI, and Prompt Engineering. **The shared files live here and are copied out.** Read [`SYNC.md`](SYNC.md) before editing anything in `lectern/`, `facts/`, `figma/`, or `greenhouse-watch-demo/`.

- **Edit a shared file here, never downstream.** After editing, run `./lectern/ops/sync.sh --check`, then `./lectern/ops/sync.sh`.
- **Never copy** `FRICTIONAL.md`, `README.md`, `CLAUDE.md`, an `assignment-*/` folder, or a dated run output between classes. A log overwritten by another class's log is a destroyed record.
- **`sync.sh` does not commit.** Each repo is committed by hand with its own message and its own `FRICTIONAL.md` entry.
- If a shared file was edited in the wrong repo during a class, follow the recovery steps in `SYNC.md` — and log the drift, because it is a finding about the workflow.

## Rule 1 — log every substantive change in FRICTIONAL.md

Before you report a task in this folder as done, update `FRICTIONAL.md` in the same change set.

**Substantive** means anything a reader of the log would need in order to understand the work:
- a new or deleted file or folder;
- a change to what a result says (a new Gru turn, a changed verdict, a new section of the design document);
- a decision, a reversal, or something that went wrong.

**Not substantive:** typo, wording, or formatting fixes that don't change meaning. Leave those out rather than padding the log.

**How to log it:**
- **Same day, same work:** extend that day's entry. Don't start a second entry for the same session.
- **New day or new piece of work:** add a new entry under `## Entries`, newest last, headed `### YYYY-MM-DD — <what it was>`, using the course's seven fields, verbatim and in order:
  - Date and what I was working on
  - I tried / expected
  - What happened
  - What I did
  - What Claude or another person contributed
  - What I understand now / still do not understand
  - Evidence and next step
- **Write what happened, not what was hoped.** Include what failed. Name the files that serve as evidence. Never invent a prediction, a result, an approval, or an understanding Professor Bear didn't state.
- **Credit honestly.** Say what Claude Code did and what Professor Bear decided. If he hasn't reviewed something, say so.
- Keep the executive summary at the top current.

## Rule 2 — Gru's words are never edited

Files in `03-week-2-boondoggle-report/gru-session/` and `03-week-2-boondoggle-report/gru-session-downloadable-gru/` (renamed from `boondoggle-report/` on 2026-10-18) hold Gru's replies verbatim. So do the blocks under "Gru's section outputs" in `FRICTIONAL.md`, which are sliced from those files by script. They are copied from the conversation transcript by script, never retyped or cleaned up. The brief says Gru's errors and pushback are part of the submission.

## Rule 3 — one line per GitHub push

Every push that touches this folder adds a row to the `## GitHub pushes` table, **in the same commit being pushed**:

```
| YYYY-MM-DD | <commit subject, exactly as committed> |
```

- The note is the commit subject, copied exactly. The repo uses conventional subjects (`feat(fall-2026): …`, `docs(fall-2026): …`).
- No commit ID in the row: a commit can't contain its own ID, and `git log` holds it.

## Rule 4 — new possible listings are posted to Discord automatically

**Standing rule (Professor Bear, 2026-10-19):** every time a run finds new possible listings, post them to the public `#professor-bear` channel of the SEIS AI Lab Discord server without being asked, so he can see them whenever he looks. This is not a question to ask each time.

- **How:** `lectern/ops/daily.sh` does it (`publish_delta.py --write --post`, then `faculty_feed.py --send`). A run you start by hand uses `publish_delta.py --post`, or `--post-only` for a run already collected. Both go through `lectern/publish/notify.py`.
- **What goes in a post:** only listings from companies still on the watch list, most-wanted employers first, each with its link and the words that matched, newly watched companies marked, and the line "A person decides; the machine only ranks words." Posted ids are remembered, so nothing is posted twice.
- **What never does:** a local path, an email address, a webhook URL, or an unlisted YouTube link. The webhook stays in the home folder.
- **Posting is not pushing.** Posting a run's listings to Discord needs no word; pushing its delta to GitHub still does.

## Rule 5 — great-fit labs are posted to Discord, and nothing is approached before Professor Bear has looked

**Standing rule (Professor Bear, 2026-10-19):** when a lab or research group looks like a great fit, post its page to the public `#professor-bear` channel so he can look at it. For a company such as Moderna that is a research group's page, not a job posting. Then he, as a person, reads the page and decides. No lab is approached, drafted to or written to before he has looked, and the emails are his to write and send.

- **Tiers:** `great` fits first. `pretty_good` fits are posted only when he says so, after great fits have come to nothing. Do not widen on your own.
- **How:** `lectern/publish/notify.py` `post_labs()` (tested with made-up labs in `lectern/tests/test_notify.py`). It reads only the lab's public name, institution, page link, tier, kind and the lab's own words (300 characters at most).
- **What never goes in a post:** the principal investigator, a lab manager or any other person; an email address or phone number; a local path; a webhook URL. A lab named for a person is shown as "A lab at <institution>" with its link. The lab records themselves name people and stay local (`lectern/labs/`, `lectern/lab-records/`, gitignored).
- **Not built yet:** the reader that turns lab pages into candidates (see `lectern/lab-outreach/LAB-RECORD.md`). Until it exists there is nothing to post.
- **Posting is not pushing**, as in Rule 4.

## Rule 6 — `lectern/HISTORY.md` is the daily log of the code

**Standing instruction (Professor Bear, 2026-10-20):** keep `lectern/HISTORY.md` as a daily log of what was added to `lectern/` and when, and how the tool is being built up, alongside `FRICTIONAL.md`. Whenever a file in `lectern/` is added, removed or changed in what it does, add a dated entry (date, what, why) **in the same change**, and keep the tables in `lectern/README.md` true. Write what happened, including what failed; never a result nobody ran. The same goes for `lectern/forms/n8n/` (the n8n form, kept beside the Python form): its README says what is tested. **Also keep `lectern/TARGETS.md` true:** when a target is added, removed or reclassified, or a reader for one is built or fails, change its row in the same change.

## Rule 7 — one list of targets, read by every form

**Standing instruction (Professor Bear, 2026-10-20):** the companies, schools and research groups Lectern looks at have **one** source of truth, `lectern/config/targets.json`; every form of Lectern (the Python, `lectern/forms/n8n/` and the others) reads it and none copies it. Change a target there, then run `python3 lectern/ops/build_from_targets.py`; it regenerates `sources.json`, the schools in `faculty_config.json`, the seeds in `biolabs.json` and the tables in `lectern/TARGETS.md` (`--check` says whether anything differs, and `tests/test_targets.py` fails if it does). A form may collect its own data and may propose a new target in its own `proposed-targets.jsonl` with a link to a public page that backs the claim, but never edits `targets.json`; a person promotes it. A removed target stays, with its reason and date.

## Rule 8 — early-career game, engine and real-time listings are for #games-3d-simulations, and posting is OFF until Professor Bear says go

**Standing instruction (Professor Bear, 2026-10-28):** *"any game jobs that an early-career person who knows Unreal or Godot or Unity, or has any experience there, could take"* go to a second Discord channel, #games-3d-simulations, not to #professor-bear. **Dry run only until he says go.**

- **How:** `lectern/publish/games_feed.py` (a dry run is its default); the rules are `engine_rule` in `lectern/config/keywords.json`, judged by `lectern/collect/engine_jobs.py`. Three locks keep it from posting by accident: the rules say `"posting": "off"`; `--send` must be on the command line; and a first send with no memory of earlier posts needs `--post-all` (or `--baseline` first). Posted ids are remembered in `runs/posted-games-to-discord.json`, so nothing is posted twice.
- **The studio list** (added 2026-10-28, at his word, reviewed company by company): the `games` section of `lectern/config/targets.json`, one list with the rest (Rule 7), status `active` = on the list. Only `lectern/collect/engine_jobs.py` reads it; `collect.py` never fetches these studios, because `build_from_targets.py` turns only the `boards` section into `sources.json`. Section H of `lectern/TARGETS.md` shows every verdict and its reason.
- **Where it reads:** the ai-jobs snapshot (every posting on the boards it reads), because none of the watched companies is a game studio. Rights for posting from it are a decision of his (see `lectern/HISTORY.md`, 2026-10-28).
- **What goes in a post:** the title, company, place and link of the employer's own public posting, the words that matched, and the line "A person decides; the machine only ranks words." **What never does:** a local path, an email address, a webhook URL. The webhook stays in the home folder (`~/.discord-webhooks/games-3d-simulations`) and is never printed.
- **One place posts.** If an always-on server is ever the poster, the Mac must not post to this channel (it would not know what the server posted). The country rule and the K-12 rule apply here too.

## Pushing from this folder

- **Each push needs Professor Bear's word.** He approved the first push on 2026-09-24. There is no standing approval for this folder yet.
- Git on his machine is already authenticated. Never ask for, accept, or write down a GitHub token.
- Stage **only** `fall-2026/nik-bear-brown/` (and the one `.gitignore` line that tracks it). The repo often has other uncommitted instructor edits; never sweep them in.
- Run `python3 scripts/validate_course.py` from the repo root before committing.

## Privacy

This repo is public. The person here is **"Professor Bear."** No contact details, profile links, or other people's names. No absolute local paths (`/Users/…`) in anything committed. The personas named in the report (Priya Nair, Aarav Patel) are fictional, from the Reallocation Engine's `search/examples/`.
