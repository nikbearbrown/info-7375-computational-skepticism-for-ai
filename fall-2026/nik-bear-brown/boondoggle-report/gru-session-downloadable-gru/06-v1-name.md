# Gru turn 06-v1-name

## Professor Bear typed

```
/g3 too: its own file, no section. Correct.

1. The name is gru, everywhere. The toolkit folder and entry script are gru, the hub skill is gru, the phase skills are gru-scan, gru-v0, gru-intake and so on, and the command is /gru. For now the toolkit lives in my course's public repository, in my example folder, so a student downloads it by cloning that repository; whether it later gets its own repository is a decision for after v1 ships.
```

## Gru replied (verbatim, unedited)

Question 1 is recorded. The name is **gru** everywhere: the toolkit folder, the entry script, the hub skill `gru`, the phase skills `gru-*`, and the command `/gru`. /g3 is logged as its own file with no section.

Two things before question 2.

**Naming inconsistency: `gru-v0` next to `gru-intake`.** The first is named after the command code, the second after the command alias. Gru's menu gives every command both (`/v1 or /intake`), so if the skill folders mix the two, a student will guess wrong about half the time. That means `/gru intake` works but `gru-intake` isn't where they expect, or the other way around. Pick one scheme for the folder names. The translation layer can accept both spellings at the prompt. For example, codes everywhere: `gru-v0`, `gru-v1`, `gru-s1`, `gru-claude`. Or aliases everywhere: `gru-brief`, `gru-intake`, `gru-components`, `gru-boondoggle`. It doesn't need to be settled now. I'm logging it as OQ4, and it has to close before /s1 names the components.

**Install source.** The toolkit currently sits in an example folder inside a larger public course repository. That means "installed by one command" really means: clone the whole course repository, then run the entry script, which copies `gru` into *a different* repository. That's two repos and a copy step. It shapes the install instructions, the update path (how a student gets a new Gru prompt file), and what happens when the course repo reorganizes its folders. I'm logging it as OQ5. The owner is you, the decision point is "after v1 ships," and it goes to /p3. It doesn't block intake.

---

**Question 2: In one sentence, not a paragraph, what problem does this system solve?**

State the problem, not the technology or the features.

I'll push back if the answer is really describing the absence of the solution, for example "students can't run Gru in their own repo," or "the pasted prompt doesn't see their files." Those describe the gap your tool fills, not the problem. Ask yourself what goes wrong for a student today that makes a local, repo-reading Gru worth building. Name the failure, not the missing tool.
