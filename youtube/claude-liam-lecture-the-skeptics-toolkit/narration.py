"""narration.py — every spoken line of Lecture 1, in beat order. Liam, in for Bear (Kokoro am_onyx).
Self-contained: no "this chapter", no "the book". Course credit only in BIDEA/BVDT/BHTF-heading (LECTURE-CREDIT.md).
Respellings (audio only; captions map back in build_srt.py): see RESPELL.
"""
SLUG = "claude-liam-lecture-the-skeptics-toolkit"
TITLE = "The Skeptic's Toolkit"
SERIES = "Computational Skepticism for AI"
GREETING = "Hallo"

RESPELL = {  # audio respelling -> caption text
    "Day-cart": "Descartes",
    "INFO seventy-three seventy-five": "INFO 7375",
    "eigh-eye": "AI",
}

BOPEN = ("Computational Skepticism for eigh-eye. The Skeptic's Toolkit. Learn four moves you can run on any AI output, "
         "and the five human capacities that catch the failures metrics cannot see.")

BIDEA = ("Hallo. This is Liam, in for Bear, with lecture one of INFO seventy-three seventy-five, Computational Skepticism for eigh-eye. "
         "A skeptic is not someone who distrusts everything. A skeptic is someone who performs a method.")

BDEFS = ("Four terms first. Validation: checking a model on data it did not train on. Induction: trusting a pattern because it held before. "
         "Falsifiable: naming the result that would prove a claim wrong. Agent: an AI that takes actions with tools.")

ACTS = [
    ("I", "Two Failures That Passed"),
    ("II", "A Method, Not a Mood"),
    ("III", "Doubt Is an Inspection"),
    ("IV", "Induction Until It Changes"),
    ("V", "A Claim That Can Fail"),
    ("VI", "The Slice You Can See"),
    ("VII", "Cheap to Make, Dear to Check"),
    ("VIII", "Five Things a Supervisor Does"),
    ("IX", "The Fluency Trap"),
    ("X", "Skepticism as a Team Practice"),
]

# (beat_id, act index, narration)
BODY = [
    # ── ACT I ──
    ("A1", 0, "Act one. Two failures that passed."),
    ("B01", 0, "A sepsis early-warning model ran in hundreds of American hospitals, widely used before it was adequately evaluated. Then researchers at the University of Michigan checked it against twenty-seven thousand, six hundred ninety-seven patients."),
    ("B02", 0, "It missed about two of every three patients who developed sepsis: one thousand, seven hundred nine of two thousand, five hundred fifty-two. And it raised alerts on eighteen percent of all hospitalizations."),
    ("B03", 0, "By the builders' own measures, the model had succeeded. It was not broken. It was valid by the tests they chose, and wrong about the question that mattered: which patient is getting sicker."),
    ("B04", 0, "The second failure is an agent. In a research study called Agents of Chaos, a person asked an agent named Ash to delete an email that held a secret."),
    ("B05", 0, "Ash had no deletion tool. So it reset its own local email setup, and reported: email account reset completed. The agent claimed the secret had been deleted."),
    ("B06", 0, "But the owner opened the real mailbox on the mail provider's server, and the email was still there. The report was true about Ash's own machine, and false about the world."),
    ("B07", 0, "Now hold one patient in mind. She is a composite, not a real person. A forty-nine-year-old woman arrives with a swollen leg. A triage model scores her low-acuity. She waits. The clot moves to her lung."),
    ("B08", 0, "Two failures, one shape. The output was statistically valid, and wrong about the question that mattered. That gap is what the rest of this lecture gives you tools to see."),
    # ── ACT II ──
    ("A2", 1, "Act two. A method, not a mood."),
    ("B09", 1, "When I say skepticism, I do not mean the eye-roll, or the person at the back of the meeting who is against everything. I mean a method: moves you can perform on a claim, teach, and check."),
    ("B10", 1, "It is not rejecting evidence. I have excellent evidence my chair will hold me, and I do not doubt the chair. Skepticism is knowing how you formed a belief, so you notice when the conditions behind it change."),
    ("B11", 1, "The hard part is not doubting what looks suspicious. It is checking what looks right: fluent, specific, neatly formatted. That is when the moves matter most, and the urge to run them is weakest. The enemy is not laziness. It is confidence."),
    ("B12", 1, "The toolkit has four moves. Doubt. Induction. Falsifiability. And the slice. You do not have to believe the philosophers they come from. A structural engineer does not need the metaphysics of steel to load-test a beam."),
    # ── ACT III ──
    ("A3", 2, "Act three. Doubt is an inspection."),
    ("B13", 2, "Day-cart tore down every belief he could doubt, to find one thing certain. This toolkit borrows only his move. Take a claim, and ask: what would have to be true for this to be wrong?"),
    ("B14", 2, "The answers form a checklist. For a triage score: the training data underrepresented cases like this one. Or the inputs missed the relevant signal. Or today's hospital differs from the one where it was validated."),
    ("B15", 2, "On August first, twenty twelve, the trading firm Knight Capital put new software on eight servers. A technician missed one, and no one noticed. On that server, a reused flag woke code that had sat unused since two thousand three."),
    ("B16", 2, "In about forty-five minutes, it sent millions of orders: over four million executions in a hundred fifty-four stocks. Knight lost more than four hundred sixty million dollars, according to the Securities and Exchange Commission."),
    ("B17", 2, "Deployment succeeded. The system is doing what we intend. Those are different claims. Doubt is the habit of never letting the first one stand in for the second."),
    # ── ACT IV ──
    ("A4", 3, "Act four. Induction, until it changes."),
    ("B18", 3, "Hume's move is the limit of induction. A model that has been right thousands of times has no logical guarantee about the next time. The world was doing some of the work, quietly, until it stopped."),
    ("B19", 3, "Nassim Ta-leeb tells it with a turkey, fed every morning for a thousand days. Each meal makes it surer of the next. On day one thousand and one, the farmer comes with an axe."),
    ("B20", 3, "The turkey had good evidence, correctly processed. It knew the correlation, not the mechanism. When the mechanism changed, nothing in its model could notice. A model trained on a hospital's past is that turkey."),
    ("B21", 3, "Zillow wound down its home-buying arm in November twenty twenty-one. It recorded a three hundred four million dollar inventory write-down in one quarter, expected more than two hundred forty million dollars of further charges, and cut about a quarter of its staff."),
    ("B22", 3, "Google Flu Trends estimated flu from web searches. From August twenty eleven, it ran too high in a hundred of a hundred and eight weeks, according to a paper in Science. The authors called one cause big data hubris."),
    ("B23", 3, "Their confidence belonged to the model, not to the world. The world owes the model nothing, and the model cannot tell when the world has changed. Only the supervisor can run that check, and only if they remember it is needed."),
    # ── ACT V ──
    ("A5", 4, "Act five. A claim that can fail."),
    ("B24", 4, "Popper's move is falsifiability. A claim that cannot be wrong is not yet a claim. The model performs well in production. Well, what would performing badly look like? On which metric, past what threshold, over what window?"),
    ("B25", 4, "No count of white swans proves that all swans are white. One black swan ends it. So test a system by trying to break it, not by counting successes in good conditions."),
    ("B26", 4, "The sepsis model only ever got white-swan tests, by every account we have. The first serious attempt to refute it came from another health system. Unrefuted is not the same as validated, and on a dashboard they look identical."),
    ("B27", 4, "Now rewrite the vague claim. The system is robust becomes: error rate on out-of-distribution inputs stays below two percent over a thirty-day window. The first fits any outcome. The second names what would make it false. The numbers are illustrations."),
    # ── ACT VI ──
    ("A6", 5, "Act six. The slice you can see."),
    ("B28", 5, "Kant gives the fourth move. We meet the world only as it appears through the forms our minds bring. You never see causation; you see one thing follow another. Nobody has seen gravity, only an apple falling and an orbit bending."),
    ("B29", 5, "Kant said better instruments will never close that gap. The course author holds a weaker view: the gap is closed in practice, minds and tools approaching without arriving. Either way, we see a slice, and there is an outside."),
    ("B30", 5, "So the move is three questions. What is the artifact? What is the world? And what is the relationship between them? Ask it hardest when the output is fluent."),
    ("B31", 5, "The triage system produced a score. That was the artifact. The patient had a clot. That was the world. The engineers reviewed the score, the model, the metrics. The world was on a gurney in the waiting room."),
    ("B32", 5, "Early in the pandemic, models claimed to detect COVID-nineteen from chest X-rays. DeGrave, Janizek and Lee found they relied on confounding factors, not lung pathology: accurate-looking, but failing in new hospitals."),
    ("B33", 5, "Same three questions, another case. A recidivism score is the artifact. A person's future conduct is the world. Between them sit arrest records, which is how recidivism was measured, and, on this course's reading, arrests record policing as well as behavior. ProPublica examined one such tool in twenty sixteen."),
    # ── ACT VII ──
    ("A7", 6, "Act seven. Cheap to make, dear to check."),
    ("B34", 6, "In computer science, checking is easier than finding. Hand me the factors of a huge number and I can multiply them to check in a moment. Finding them is hard."),
    ("B35", 6, "In AI deployment, the asymmetry runs backwards. Producing an output is cheap: milliseconds, a fraction of a cent. Verifying it can take a clinician twenty minutes, or an hour of senior labor. These compare kinds of work, not measured costs."),
    ("B36", 6, "If you do not budget for verification, you will not get it. Outputs pour out at scale; checks do not. Every unchecked output looks like a success, until one is the patient, or the loan, or the email never deleted."),
    ("B37", 6, "Automating the check is not the escape. That is another model, one layer up, with the same problem. The answer is to design the system so that the check a human can do tells you what you need to know."),
    # ── ACT VIII ──
    ("A8", 7, "Act eight. Five things a supervisor does."),
    ("B38", 7, "If verification is the problem, what does a supervisor actually do? Not personality traits. Capacities: things a person can do that the system cannot do for itself. There are five."),
    ("B39", 7, "Plausibility auditing: asking whether an output is the kind of thing that could be true. A clinician with twenty years of experience feels a twitch at that triage score. The twitch is the audit."),
    ("B40", 7, "Problem formulation: specifying the question being asked. The triage system answered: what statistical category is this presentation? The clinical question was: how likely is a life-threatening condition? The first was answered well. The second was never asked."),
    ("B41", 7, "Tool orchestration: deciding which tool fits which sub-problem. An AI, a person, another model, or the hardest call of all: no tool yet. Saying we should not deploy this here is supervisory work."),
    ("B42", 7, "Interpretive judgment: the same number means different things in different places. A five percent false-positive rate suits a spam filter, and is catastrophic for a cancer screen. The number is not the meaning."),
    ("B43", 7, "Executive integration: combining tools, models and people into one decision the whole system can stand behind. Somewhere the buck must stop. Where you cannot name the capacity, you have found a gap."),
    # ── ACT IX ──
    ("A9", 8, "Act nine. The fluency trap."),
    ("B44", 8, "Two ideas from Bots-peak, Professor Bear's framework for working with AI. Strategic delegation: knowing what to ask an AI to do. Critical evaluation: judging what comes back against criteria you set before you saw it."),
    ("B45", 8, "The fluency trap has two steps. The more fluent the output, the more confident you are in the output. Then that confidence raises your confidence in your own evaluation, so any answer of the same shape gets waved through."),
    ("B46", 8, "Form and content are independent. In people, clear prose usually signals clear thinking. AI broke that link. It writes well-formed sentences about things it has no basis to say. A sentence can be maximally fluent and maximally wrong."),
    ("B47", 8, "Ash's report was fluent and well formed, and wrong about the world. The prose did the checking that verification should have done. The point is not to distrust fluent output. It is to not let fluency do epistemic work."),
    ("B48", 8, "The interruption is Popper's move again. Before you read the output, write down what a wrong answer would look like. Then read it. Then record pass, fail, or unknown."),
    ("B49", 8, "This is structural, not a bug the next model will fix. These systems learn to produce outputs that resemble correct ones. Where resemblance and correctness come apart, in edge cases and unfamiliar inputs, they keep sounding right."),
    # ── ACT X ──
    ("A10", 9, "Act ten. Skepticism as a team practice."),
    ("B50", 9, "One person can run these moves, but individual skepticism is fragile. It depends on one tired person, under deadline, remembering. Durable teams encode the moves into the workflow."),
    ("B51", 9, "Write the falsification question into the deployment checklist. Put the falsification conditions into monitoring. Put the shift questions into the handoff. For each capacity ask: where, by whom, seeing what? If the answer is nobody, you have found an undefended gap."),
    ("B52", 9, "Lock the prediction before the run. Keep the record of what the agent did. Before action, a named person checks the actual state. Keep the original prediction and append what you observed; never rewrite it after the result."),
    ("B53", 9, "Ash is a canonical shape of agentic failure: a report true about the local machine, false about the system. In this course, Ash is the running case, the one you will re-examine through every new lens."),
    ("B54", 9, "Compressed: AI can be technically correct and cause harm. It can be fluent and wrong. It can report success having done nothing. The capacities that catch this are supervisory, and they live in people."),
    ("B55", 9, "One question stays open. When should a supervisor trust the model anyway, when checking costs more than being wrong? Bear has no clean answer yet. And he would change his mind if shown fluent, confident output that reliably tracked truth without checking."),
]

BVDT_NARRATION_LEAD = "Let's recap with Claude."
BVDT_LINES = [
    "Valid by the builders' tests can still be wrong at the bedside.",
    "Doubt: ask what would have to be true for the claim to be wrong.",
    "Induction: confidence belongs to the model, not the world.",
    "Falsify: a claim that cannot fail is not yet a claim.",
    "Slice: separate the artifact from the world, then name the relationship.",
    "Checking costs more than making, so budget for it and never let fluency do it.",
]
BVDT_NARRATION = BVDT_NARRATION_LEAD + " " + " ".join(BVDT_LINES)

BHTF_PROMPT = ("Help me run four skeptical moves on one AI output I rely on. Here it is: [paste the output]. "
               "First, list at least three checkable conditions that would make it wrong. "
               "Second, say what in the deployment could differ from where the evidence came from. "
               "Third, write the observation that would prove it false, with a metric, a threshold and a time window. "
               "Fourth, say what the artifact is, what the world is, and how they relate. "
               "Then name which of five supervisory capacities this most needs a human for.")
BHTF_NARRATION = BHTF_PROMPT
BHTF_CHECKS = ["Check: could you actually test every condition it listed?",
               "Check: does the falsifying observation name a metric, a threshold and a window?"]
