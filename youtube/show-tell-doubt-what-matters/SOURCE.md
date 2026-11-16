# SOURCE — "Doubt What Your Work Depends On"

**What this is.** The verbatim source for this film: Bear's dictated request (2026-09-27, from `../SHOW-TELL-THREE-MOVES.md`) and the relevant lines of `info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md` (Chapter 1, "The Skeptic's Toolkit", section "What I mean by skepticism": lines 33–49, the framing and the Descartes move, and line 97, the close), copied read-only on 2026-09-27. The chapter file carries Bear's uncommitted edits and was not modified. **Why.** Every narration line traces to these words or to Descartes' own texts (`SOURCES.md`, `sources/`). **Found.** The chapter frames Descartes' move as "what would have to be true for this claim to be wrong?" and says outright it is teaching "the move", not Cartesian philosophy; the film keeps that framing ("this course borrows his move"). Bear's addition, risk (doubt in proportion to what being wrong costs), is his rule, not Descartes'; Descartes' own texts limit doubt for a different reason (action can't wait), and the film says each as its source says it.

## Bear's words (2026-09-27, dictated; lightly cleaned, as quoted in the brief)

> Make individual show-tell films on radical doubt, induction and falsifiability. Mention the philosophers they are associated with; they are in the chapter.
>
> **Radical doubt.** Talk about Descartes. Talk about how you can't doubt everything, and add risk to that: you should doubt the things that are important to doubt. You can't doubt everything, but you should doubt what your job depends on — health, important things.

## Chapter 1, lines 33–49 (verbatim)

## What I mean by skepticism

When I say *skepticism*, I do not mean the disposition. I do not mean the rolling of the eyes, the cynicism dressed up as a virtue, the man at the back of the meeting who is against everything. Engineers know what to do with that, which is not very much, and they are right to know it.

I mean a method. Skepticism in this book is a set of moves you can perform on a claim, and the moves can be taught, and you can see whether someone did them. Three philosophers donate moves to the toolkit. None of them gets credit beyond the move itself; the move is the thing.

But before I hand you the three moves, I want to say something about what skepticism is *for*, because this is the part that gets dropped in most technical education, and dropping it is precisely what makes engineers trust AI outputs they should not trust.

Skepticism is not the rejection of evidence. That would be insane. I have excellent evidence, accumulated over decades, that the chair I am sitting on will hold my weight. I do not doubt the chair. Skepticism is not the refusal to form beliefs. It is the *discipline of knowing how you formed them*, so you can notice when the conditions that made them reliable have changed. When the conditions change and you do not notice — when the model's confidence carries forward unchanged into a world the model has never seen — that is not just a technical failure. That is a failure of method. The method is what this chapter teaches.

Here is the thing that took me years to really feel, and I want you to feel it too rather than just nod at it: the difficulty is not in performing the moves when you know something is suspicious. The difficulty is in performing them when the output looks right. When it is fluent, when it is specific, when it arrives in a format that pattern-matches to "trustworthy answer" — that is when the moves matter most, and that is exactly when the instinct to perform them is weakest. We are going to come back to this in the section on the fluency trap. For now: keep it in the back of your mind that the primary enemy of skepticism is not laziness. It is confidence.

**Descartes** donates *radical doubt*. You take a claim — say, the triage score of "low-acuity" — and you ask: what would have to be true for this claim to be wrong about the patient in front of me? Not as a ranking exercise. As a diagnostic. If the answer is "well, the score is the score," then you have confused the artifact for the world, and we are back where we started. If the answer is "the training data would have had to underweight cases like this one, or the input features would have to be missing the relevant signal, or the deployment context would have to differ from the validation context" — *now* you have something. You have a list of conditions you can check.

Descartes used this move in the seventeenth century for a different purpose — he was trying to find something he could be certain of, and he ended up at the famous *cogito*, the one thing left standing when he doubted everything else. I am not teaching you Cartesian philosophy. I am teaching you the move, which is this: *treat every claim as a conjecture and ask what it would take to falsify it, before the world does the falsifying for you.* The triage nurse who asks "what would have to be true for this score to be wrong?" is performing Descartes's move. The one who trusts the score because it was right the last eight hundred times is performing no move at all.

What makes the Cartesian move powerful is that it produces a *checklist*. When you ask "what would have to be true for this to be wrong?", the answers are checkable. The training data either underrepresented cases like this one or it did not. The input features either include the relevant signal or they do not. The deployment context either matches the validation context or it does not. None of these are metaphysical questions. They are engineering questions. Descartes hands you a method for turning philosophical doubt into a practical inspection protocol.

## Chapter 1, line 97 (verbatim)

I want to be clear about something. You do not have to think Descartes was right about anything to use his move. You do not have to be a Humean or a Popperian. The moves are tools. A structural engineer does not have to believe in the metaphysics of steel to perform a load test on a beam. You perform the move. The move either reveals something or it does not. If it does, you have learned something about the system. If it does not, you have learned that this particular check came back clean. Either is useful.
