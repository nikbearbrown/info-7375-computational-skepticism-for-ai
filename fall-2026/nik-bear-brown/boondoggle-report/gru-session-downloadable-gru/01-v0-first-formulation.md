# Gru turn 01-v0-first-formulation

## Professor Bear typed

```
/v0 I want to make a downloaded version of Gru that is not a project but a set of skills and scripts that can see folders and info in a downloaded repo, and that generates the design document and the Boondoggle report.
```

## Gru replied (verbatim, unedited)

You've given me more than most people do on a first /v0, so here's what I heard before I ask anything:

- **Where it runs:** skills and scripts, presumably Claude Code, installed on someone's machine. That replaces a Claude.ai Project where the prompt gets pasted in.
- **What it reads:** the folders and files in a repo that has been downloaded.
- **What it produces:** a Software Design Document and a Boondoggle Score. I'm going to call it a Score, not a report. That word is used precisely everywhere else in Gru, and a "report" usually means something that describes what already happened. A Score says who does what next.

Three things are still unclear. I'm naming them now because each one changes what you're building.

1. **"Downloaded" has two meanings here.** One is the Gru toolkit that gets downloaded and installed. The other is the repo Gru reads. Those are separate objects. I'm assuming you mean both, but the one sentence we write has to keep them apart.

2. **"See folders and info" doesn't say which repo.** It could be an existing codebase, where Gru works out an SDD from code that already exists. It could be a mostly empty repo for a new build, where Gru has almost nothing to read and has to interview the person. Or it could be a repo of recipes, like the ones `/audit` handles. Each of those is a different tool.

3. **"Generates the design document" may conflict with Gru's core principle.** In this prompt the SDD is proof that the person did the thinking. It isn't the goal. A tool that scans a repo and writes the SDD skips `/v0`, skips the phase gates, and hands over something that looks rigorous when nobody formulated anything. You can still build this. But you need to decide now whether the repo scan feeds the interview or replaces it. If it replaces it, you've built a documentation generator, not Gru. That's a legitimate product, but it's a different one.

We'll take the three /v0 questions one at a time.

**Question 1: In two sentences at most, what ecosystem or platform does this live inside?**

Keep it to context only, not the proposal. For example, is it Claude Code with a skills folder? A plugin marketplace? The Madison / Snickerdoodle toolchain the recipes already assume? Something else? And who installs it: you, your fellows, or anyone who clones a repo?
