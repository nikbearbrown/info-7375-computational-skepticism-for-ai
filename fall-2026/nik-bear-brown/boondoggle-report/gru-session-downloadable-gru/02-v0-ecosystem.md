# Gru turn 02-v0-ecosystem

## Professor Bear typed

```
Claude Code, running in a person's terminal, where skills are folders of instructions and scripts that Claude Code discovers inside a repository. The toolkit is a public GitHub repository modelled on my brutalist.art video toolkit (one entry-point script, a skills/ folder, standard-library scripts); the people who install it are my INFO 7375 students and Humanitarians AI fellows, and anyone else who clones it.

On your third point, so you know where I stand before question 3: the scan feeds the interview. It never replaces it.
```

## Gru replied (verbatim, unedited)

Accepted. Here is the ecosystem I'll record:

> Claude Code running in a user's terminal, where skills are folders of instructions and scripts that Claude Code finds inside a repository. The toolkit ships as a public GitHub repository built like the brutalist.art toolkit, and it is installed by INFO 7375 students, Humanitarians AI fellows, and anyone else who clones it.

I'm also logging your answer to the third point as a design decision. It will become an architecture principle in /v2:

> **The scan feeds the interview; it never replaces it.** The repo scan can pre-fill context, suggest answers, and surface contradictions. It cannot confirm the /v0 sentence, pass a phase gate, or write an SDD section the user hasn't answered.

Keep it in that form, because you'll be tempted to weaken it later. The first time a student complains that the interview is slow, someone will suggest a `--skip-interview` flag. With this principle written down, that stops being a convenience request and becomes a principle violation that needs a documented exception.

"Anyone else who clones it" matters too. Your students have heard the Irreducibly Human argument, but a stranger has not. The toolkit has to enforce the gates by how it's built, because you can't count on the user understanding why the gates exist.

**Question 2: What already exists that this proposal touches, depends on, or extends?**

Name specific components, not general systems. For each one, tell me which of these it is:

- **depends on:** the toolkit breaks if it's missing or changes
- **extends:** the toolkit adds to something that already exists
- **copies the pattern of:** the toolkit borrows the shape and shares no code

Here are the candidates I can see. Confirm, strike, or add to them:

- The Gru prompt document itself. Is it the single source of truth the skills are generated from, or will the skills fork it and drift?
- The brutalist.art toolkit. From what you said, I read this as "copies the pattern of," but confirm.
- Claude Code's skill discovery. That's an external contract you don't own.
- The Snickerdoodle CLI and the `recipes/` standard format, since `/recipe`, `/snickerdoodle` and `/audit` all assume they exist.
- The repo being scanned. What does Gru expect to find there: `CLAUDE.md`, `AGENTS.md`, `DATA_CONTRACT.md`, a `recipes/` folder, or nothing at all?

The last one matters most. If Gru has to work on a repo with none of those files, the scan has very little to feed the interview, and you should know that before the one-sentence question.
