# CLAUDE.md — nik-bear-brown/ (Professor Bear's example folder)

This folder is the instructor's public example work for INFO 7375 Computational Skepticism for AI, Fall 2026. It keeps the same process record students keep. **Every substantive change here is logged in `FRICTIONAL.md`, and every push adds a line to it.** The repo-root `AGENTS.md` still governs everything else.

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

Files in `boondoggle-report/gru-session/` and `boondoggle-report/gru-session-downloadable-gru/` hold Gru's replies verbatim. So do the blocks under "Gru's section outputs" in `FRICTIONAL.md`, which are sliced from those files by script. They are copied from the conversation transcript by script, never retyped or cleaned up. The brief says Gru's errors and pushback are part of the submission.

## Rule 3 — one line per GitHub push

Every push that touches this folder adds a row to the `## GitHub pushes` table, **in the same commit being pushed**:

```
| YYYY-MM-DD | <commit subject, exactly as committed> |
```

- The note is the commit subject, copied exactly. The repo uses conventional subjects (`feat(fall-2026): …`, `docs(fall-2026): …`).
- No commit ID in the row: a commit can't contain its own ID, and `git log` holds it.

## Pushing from this folder

- **Each push needs Professor Bear's word.** He approved the first push on 2026-09-24. There is no standing approval for this folder yet.
- Git on his machine is already authenticated. Never ask for, accept, or write down a GitHub token.
- Stage **only** `fall-2026/nik-bear-brown/` (and the one `.gitignore` line that tracks it). The repo often has other uncommitted instructor edits; never sweep them in.
- Run `python3 scripts/validate_course.py` from the repo root before committing.

## Privacy

This repo is public. The person here is **"Professor Bear."** No contact details, profile links, or other people's names. No absolute local paths (`/Users/…`) in anything committed. The personas named in the report (Priya Nair, Aarav Patel) are fictional, from the Reallocation Engine's `search/examples/`.
