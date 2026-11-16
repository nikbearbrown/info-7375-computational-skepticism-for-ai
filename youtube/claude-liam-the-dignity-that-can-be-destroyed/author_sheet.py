#!/usr/bin/env python3
"""author_sheet.py — beat sheet for claude-liam-the-dignity-that-can-be-destroyed.

Films Brown's essay on the anthropological contradiction in Magnifica Humanitas.
Every encyclical quotation on screen is the VATICAN wording (FACTCHECK.md §correction).
Every theological claim is attributed, never asserted by the film.
"""
import json
from pathlib import Path

SLUG  = "claude-liam-the-dignity-that-can-be-destroyed"
TITLE = "The Dignity That Can Be Destroyed"
TOPIC = "POLITICS AND AI · EXAMINED"
SEG   = TITLE
HERE  = Path(__file__).resolve().parent
assert HERE.name == SLUG, f"wrong folder: {HERE.name}"
WPS = 2.9
beats = []

def dur(t): return round(max(2.5, len(t.split()) / WPS), 1)

def beat(bid, act, lane, narr, vis, shot, show, **extra):
    b = {"beat_id": bid, "act": act, "lane": lane, "narration_text": narr,
         "estimated_duration_s": dur(narr), "voice": "am_onyx", "engine": "kokoro",
         "voice_kokoro": "am_onyx", "new_visual_element": vis, "shot": shot,
         "show": show, "build": {"status": "PENDING", "src": "", "filled_by": "", "at": ""}}
    b.update(extra); beats.append(b)

def rem(p, props, motion="drawon"):
    return {"type": "REMOTION", "source": "own", "motion": motion,
            "remotion": {"pattern": p, "component": p, "props": props,
                         "rendered": {"out": "", "at": ""}}}

def ask(cmd, out, greeting, running):
    return rem("ClaudeComposerAsk", {"greeting": greeting, "command": cmd, "segment": SEG,
        "topic": TOPIC, "runningText": running, "output": out,
        "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5", "effortLabel": "High"}, motion="type")

def card(title, index):
    return rem("ReqSegmentCard", {"title": title, "index": index}, motion="hold")

VATICAN = "MAGNIFICA HUMANITAS · LEO XIV · MAY 2026 · VERBATIM"

# ══ BOOKENDS ═══════════════════════════════════════════════════════════════
beat("B00", "COLD OPEN", "BOOKEND",
 "Namaste — this is Liam, in for Bear. In May, a pope wrote an encyclical about artificial intelligence, and it opens with a claim: human dignity is inalienable. Nothing can touch it. It closes with a prayer that God lift up the lowly. Bear read it closely enough to notice those two things cannot both be true.",
 "ClaudeComposerAsk — the ask, answered",
 ask("Leo XIV says dignity is untouchable, then prays for the lowly to be raised. Which is it?",
     ["A claim that cannot be diminished.", "A prayer that something be repaired.",
      "Between them, a contradiction."],
     "Namaste, Liam", "reading the encyclical…"),
 [{"at": 0.0, "event": "Composer types the ask"},
  {"at": 0.62, "event": "Send arms terracotta"},
  {"at": 0.75, "event": "Three output lines land"}])

beat("B01", "THE OVERVIEW", "BOOKEND",
 "Here is the whole argument in one breath. The encyclical's prescriptions for governing AI are right. Bear's claim is that they are right for reasons the document does not know it has — and that its own foundation is not holding them up.",
 "BrutalistHesitantWriter — the overview, corrected on screen",
 rem("BrutalistHesitantWriter", {
   "text": "This is an essay about whether the encyclical is wrong.\nIt is about a foundation doing\nless work than the building thinks.",
   "triggerWords": "whether the encyclical is wrong",
   "replacementWords": "why being right is not the same as being grounded",
   "face": "serif", "fontSize": 58, "lineSpacing": 1.32, "align": "center",
   "charMs": 42, "mistakeRate": 7, "seed": "the-dignity-that-can-be-destroyed"}, motion="type"),
 [{"at": 0.0,  "event": "Caret blinks on cream (lead silence)"},
  {"at": 0.2,  "event": "'…whether the encyclical is wrong.' types out"},
  {"at": 0.52, "event": "The clause turns terracotta and deletes"},
  {"at": 0.64, "event": "'why being right is not the same as being grounded' types in"},
  {"at": 0.86, "event": "Corrected overview holds"}],
 lead_silence_s=0.8)

# ══ ACT I — THE CLAIM AND THE PRAYER ═══════════════════════════════════════
beat("B02", "ACT I — THE CLAIM AND THE PRAYER", "CARD",
 "Start with the document, because the argument only works if you take it seriously first.",
 "ReqSegmentCard — Act I", card("The Claim and the Prayer", "I"),
 [{"at": 0.0, "event": "Eyebrow ACT · I"},
  {"at": 0.35, "event": "Serif title, terracotta period"},
  {"at": 0.6, "event": "Hairline rule draws"}])

beat("B03", "ACT I — THE CLAIM AND THE PRAYER", "REMOTION",
 "Magnifica Humanitas is Leo the Fourteenth's first encyclical, promulgated in May, on protecting the human person in the age of artificial intelligence. Bear used it in his own book as a witness — a third road arriving at the same place as Pearl and Hayek. Not a judge. A witness.",
 "ReqLevers — the three independent roads to one conclusion",
 rem("ReqLevers", {
   "title": "Three roads, one conclusion",
   "levers": [
     {"name": "Pearl", "sub": "the causal ladder — judgment is counterfactual, not associative"},
     {"name": "Hayek", "sub": "the knowledge good decisions need is local, and moving it upward destroys it"},
     {"name": "The encyclical", "sub": "authority belongs with the person closest to the problem"},
   ],
   "blocked": [], "blockedLabel": "",
   "note": "Its value: independence. Bear called it a witness, not a judge.",
   "spark": "An unexpected door."}),
 [{"at": 0.1, "event": "Title lands"},
  {"at": 0.3, "event": "Three columns rise, terracotta top rules, staggered"},
  {"at": 0.62, "event": "Each subtitle types under its name"},
  {"at": 0.85, "event": "Note lands"}])

beat("B04", "ACT I — THE CLAIM AND THE PRAYER", "REMOTION",
 "So here is the claim the document opens with. Dignity is ontological. It belongs to you by existing, and nothing you do or suffer can reach it.",
 "ReqRingWord — para 50, verbatim from the Vatican text",
 rem("ReqRingWord", {
   "before": "Human dignity does not depend on a person's abilities, wealth or position in life, nor on the right or wrong choices made; instead, it is ",
   "word": "a gift that precedes and transcends each person",
   "after": ".",
   "attribution": VATICAN + " · PARA. 50",
   "note": "The firewall: dignity outside the register AI operates in.",
   "spark": "Not earned."}),
 [{"at": 0.1, "event": "Verbatim sentence types up in serif"},
  {"at": 0.5, "event": "Terracotta ring draws around the gift clause"},
  {"at": 0.78, "event": "Attribution and note land"}])

beat("B05", "ACT I — THE CLAIM AND THE PRAYER", "REMOTION",
 "And it is the right move against a real danger. If your worth tracks your capability, then a machine that out-performs you has a claim on your worth. An account of dignity immune to capability comparison survives this century better than one built on output.",
 "ReqLedger — capacity-grounded vs capacity-independent worth",
 rem("ReqLedger", {
   "title": "Why the firewall matters",
   "rows": [
     {"tier": "If worth is", "label": "measured in capability, output, efficiency", "verdict": "A machine can take it", "accent": True},
     {"tier": "If worth is", "label": "a gift that precedes capability", "verdict": "No system can reach it"},
   ],
   "note": "Capacities vary and can be exceeded. Right move, needed foundation.",
   "spark": "The right move."}),
 [{"at": 0.1, "event": "Title lands"},
  {"at": 0.32, "event": "First row arrives; terracotta stamp — a machine can take it"},
  {"at": 0.58, "event": "Second row arrives, grey stamp"},
  {"at": 0.84, "event": "Note lands"}])

beat("B06", "ACT I — THE CLAIM AND THE PRAYER", "REMOTION",
 "Now the prayer at the other end. The Magnificat — God scatters the proud and lifts up the lowly. Which only means anything if the lowly are genuinely low. If real damage was done to real people, and something needs reversing.",
 "ReqRingWord — the prayer set against the claim",
 rem("ReqRingWord", {
   "before": "The claim says nothing can diminish you. The prayer asks that ",
   "word": "the lowly be lifted up",
   "after": ".",
   "attribution": "THE MAGNIFICAT · THE ENCYCLICAL'S CLOSING PRAYER",
   "note": "A prayer to repair what cannot be damaged is a strange prayer.",
   "spark": "Genuinely low."}),
 [{"at": 0.1, "event": "Sentence types up"},
  {"at": 0.5, "event": "Ring draws around 'the lowly be lifted up'"},
  {"at": 0.8, "event": "Note lands — the tension stated plainly"}])

beat("BASK1", "ACT I — THE ASK", "BOOKEND",
 "So what exactly does artificial intelligence threaten, if the human cannot be dehumanised?",
 "ClaudeComposerAsk micro — the question the essay turns on",
 ask("If dignity prevails beyond every circumstance, what is left for AI to damage?", [],
     "The ask,", "holding the two claims together…"),
 [{"at": 0.0, "event": "Composer micro-beat; command typed; running indicator arms"}])

# ══ ACT II — THE FOUR REGISTERS ════════════════════════════════════════════
beat("B07", "ACT II — THE FOUR REGISTERS", "CARD",
 "The document has an answer. It is careful, and it almost works.",
 "ReqSegmentCard — Act II", card("The Four Registers", "II"),
 [{"at": 0.0, "event": "Eyebrow ACT · II"},
  {"at": 0.35, "event": "Title lands, terracotta period"},
  {"at": 0.6, "event": "Rule draws"}])

beat("B08", "ACT II — THE FOUR REGISTERS", "REMOTION",
 "Paragraph fifty-two splits dignity into four. How you direct your choices. Your living conditions and the respect you actually receive. Your own sense of your worth. And the dignity you have simply by existing. The first three can be raised or lowered. The fourth cannot.",
 "ReqDefinitionDrop — the four registers; the fourth is the one that cannot move",
 rem("ReqDefinitionDrop", {
   "title": "Four registers of dignity",
   "parts": ["moral — how you direct your choices",
             "social — your conditions, and the respect you receive",
             "existential — how you perceive your own worth",
             "ontological — yours by existing at all"],
   "missing": "only the fourth is untouchable",
   "missingLabel": "the other three move",
   "note": "A real distinction — AI threatens the first three.",
   "spark": "Three move. One doesn't."}),
 [{"at": 0.1, "event": "Title lands; the four registers arrive one at a time"},
  {"at": 0.6, "event": "The fourth is held; the summary line ghosts in terracotta"},
  {"at": 0.78, "event": "Rule strikes; 'the other three move' appears"},
  {"at": 0.9, "event": "Note lands"}])

beat("B09", "ACT II — THE FOUR REGISTERS", "REMOTION",
 "That is a clean resolution. Algorithmic discrimination damages the social register — how you are treated, what you can reach. It leaves the ontological one untouched. You keep your worth; the world stops acknowledging it.",
 "ReqLedger — what the resolution assigns to each register",
 rem("ReqLedger", {
   "title": "The resolution, as offered",
   "rows": [
     {"tier": "AI reaches", "label": "social — conditions, treatment, access", "verdict": "Damaged", "accent": True},
     {"tier": "AI reaches", "label": "existential — your sense of your own worth", "verdict": "Damaged", "accent": True},
     {"tier": "AI cannot reach", "label": "ontological — what you are", "verdict": "Intact"},
   ],
   "note": "Coherent taxonomy. Whether the document holds to it is the question.",
   "spark": "Clean, so far."}),
 [{"at": 0.1, "event": "Title lands"},
  {"at": 0.3, "event": "Two 'Damaged' rows arrive, terracotta stamps"},
  {"at": 0.62, "event": "'Intact' row arrives, grey"},
  {"at": 0.86, "event": "Note lands — the hinge of the essay"}])

beat("B10", "ACT II — THE FOUR REGISTERS", "REMOTION",
 "Then comes the passage everyone quotes as the philosophical high point. What the machines lack.",
 "ReqRingWord — the capacity inventory, verbatim",
 rem("ReqRingWord", {
   "before": "So-called artificial intelligences do not undergo experiences, do not possess a body, do not feel joy or pain, ",
   "word": "do not mature through relationships",
   "after": ".",
   "attribution": VATICAN,
   "note": "Careful, and largely persuasive. Bear says so plainly before taking it apart.",
   "spark": "What machines lack."}),
 [{"at": 0.1, "event": "Verbatim sentence types up"},
  {"at": 0.5, "event": "Ring draws around the maturing clause"},
  {"at": 0.8, "event": "Attribution and note land"}])

beat("B11", "ACT II — THE FOUR REGISTERS", "REMOTION",
 "But look at what that list is doing. It separates us from machines by naming capacities. And the foundation said dignity does not depend on capacities. You cannot have both. Either dignity is capacity-independent, and the list proves nothing about dignity — or it is capacity-grounded, and the firewall was never as strong as advertised.",
 "ReqLedger — the two arguments, side by side, incompatible",
 rem("ReqLedger", {
   "title": "Two arguments, one document",
   "rows": [
     {"tier": "Foundation", "label": "dignity does not depend on capacities", "verdict": "Para. 50"},
     {"tier": "Applied", "label": "we differ from machines BY our capacities", "verdict": "The AI passage"},
     {"tier": "Therefore", "label": "the capacity list only proves what the foundation denies", "verdict": "Both cannot hold", "accent": True},
   ],
   "note": "The encyclical needs both arguments and examines neither.",
   "spark": "Both, never one."}),
 [{"at": 0.08, "event": "Title lands"},
  {"at": 0.28, "event": "Foundation row, then applied row"},
  {"at": 0.62, "event": "The 'Therefore' row lands, stamp fills terracotta"},
  {"at": 0.88, "event": "Note lands"}])

# ══ ACT III — WHERE THE SEPARATION FAILS ═══════════════════════════════════
beat("B12", "ACT III — WHERE THE SEPARATION FAILS", "CARD",
 "The taxonomy could still save it — if the document held to it. Watch what happens when the writing gets urgent.",
 "ReqSegmentCard — Act III", card("Where the Separation Fails", "III"),
 [{"at": 0.0, "event": "Eyebrow ACT · III"},
  {"at": 0.35, "event": "Title lands"},
  {"at": 0.6, "event": "Rule draws"}])

beat("B13", "ACT III — WHERE THE SEPARATION FAILS", "REMOTION",
 "Here is the encyclical on algorithms deciding who deserves. Read the last clause. That is not language about treatment or conditions. Redefining the boundaries of human possibilities is language about what people fundamentally are.",
 "ReqRingWord — the algorithm passage, VATICAN wording (essay's rendering corrected)",
 rem("ReqRingWord", {
   "before": "Entrusting an algorithm entirely with the power to declare who deserves and who does not means ",
   "word": "redefining the boundaries of human possibilities",
   "after": ".",
   "attribution": VATICAN,
   "note": "An ontological claim wearing social-register clothing.",
   "spark": "Boundaries of what we are."}),
 [{"at": 0.1, "event": "Verbatim sentence types up"},
  {"at": 0.5, "event": "Ring draws around the redefining clause"},
  {"at": 0.8, "event": "Note lands"}])

beat("B14", "ACT III — WHERE THE SEPARATION FAILS", "REMOTION",
 "And the conclusion. Never replaced, never surpassed. That is not a sentence about being misrecognised. It says replacement would be a genuine loss — that something real would be destroyed. But what cannot be diminished cannot be lost. And what cannot be lost cannot be destroyed.",
 "ReqRingWord — the closing claim, verbatim",
 rem("ReqRingWord", {
   "before": "Humanity — in all its grandeur and woundedness — ",
   "word": "must never be replaced or surpassed",
   "after": ".",
   "attribution": VATICAN,
   "note": "You cannot destroy what cannot be diminished. The title is in here.",
   "spark": "Destroyed, not misread."}),
 [{"at": 0.1, "event": "Verbatim sentence types up"},
  {"at": 0.48, "event": "Ring draws around 'must never be replaced or surpassed'"},
  {"at": 0.8, "event": "Note lands — the essay's title surfaces"}])

beat("B15", "ACT III — WHERE THE SEPARATION FAILS", "REMOTION",
 "There is a repair available. Kant's move: separate the dignity you have, which is unconditional, from the respect it commands, which can be violated. Then AI violates a duty without damaging a being. It is defensible. The document just does not hold to it.",
 "ReqLevers — the Kantian repair, and why it does not take",
 rem("ReqLevers", {
   "title": "The repair the document does not make",
   "levers": [
     {"name": "Dignity you have", "sub": "unconditional, metaphysical, untouched by any act"},
     {"name": "Respect it commands", "sub": "a duty owed — and duties can be violated"},
   ],
   "blocked": ["but the urgent passages claim more than violated duty"],
   "blockedLabel": "where it breaks",
   "note": "Philosophically defensible. Held only intermittently.",
   "spark": "Kant's move."}),
 [{"at": 0.1, "event": "Title lands; two columns rise"},
  {"at": 0.5, "event": "Subtitles type in"},
  {"at": 0.66, "event": "The right column ghosts in, struck through"},
  {"at": 0.86, "event": "Note lands"}])

beat("B16", "ACT III — WHERE THE SEPARATION FAILS", "REMOTION",
 "And then the passage Bear calls the most honest in the document. Limitation is not a defect to be engineered away. It is part of what a human life is made of.",
 "ReqRingWord — limitation as constitutive, verbatim",
 rem("ReqRingWord", {
   "before": "…humanity ",
   "word": "flourishes not despite limitations, but often through them",
   "after": ".",
   "attribution": VATICAN,
   "note": "If limitation is constitutive, conditions matter — and can be taken.",
   "spark": "Through, not despite."}),
 [{"at": 0.1, "event": "Sentence types up"},
  {"at": 0.46, "event": "Ring draws around the flourishing clause"},
  {"at": 0.78, "event": "Note lands — the implication the document does not follow"}])

# ══ ACT IV — THE WALL THAT WASN'T LOAD-BEARING ═════════════════════════════
beat("B17", "ACT IV — THE WALL", "CARD",
 "Which brings us to the part Bear did not set out to prove, and proved anyway.",
 "ReqSegmentCard — Act IV", card("The Wall That Wasn't Load-Bearing", "IV"),
 [{"at": 0.0, "event": "Eyebrow ACT · IV"},
  {"at": 0.35, "event": "Title lands"},
  {"at": 0.6, "event": "Rule draws"}])

beat("BASK2", "ACT IV — THE ASK", "BOOKEND",
 "Show me every prescription in the encyclical, next to what it actually rests on.",
 "ClaudeComposerAsk micro — the ask before the ledger",
 ask("Take each governance prescription and name what it is actually derived from.", [],
     "The ask,", "tracing the derivations…"),
 [{"at": 0.0, "event": "Composer micro-beat; command typed; running indicator arms"}])

beat("B18", "ACT IV — THE WALL", "REMOTION",
 "In his own book, Bear derived the encyclical's prescriptions from somewhere else entirely. Subsidiarity from Hayek — local knowledge dies when you move it upward. The trust gap from Pearl and Polanyi. The Magnificat's redistribution from collective intelligence research. Same conclusions. No theology.",
 "ReqLedger — each prescription and its actual derivation",
 rem("ReqLedger", {
   "title": "What grounds each prescription",
   "rows": [
     {"tier": "Subsidiarity", "label": "authority with the person closest to the problem", "verdict": "Hayek", "accent": True},
     {"tier": "The trust gap", "label": "fluency is not judgment", "verdict": "Pearl · Polanyi", "accent": True},
     {"tier": "The Magnificat", "label": "redistribute authority downward", "verdict": "Collective intelligence", "accent": True},
     {"tier": "Grounding used", "label": "the inalienable dignity of the person", "verdict": "Not required"},
   ],
   "note": "A utilitarian could accept every prescription here and none of the metaphysics.",
   "spark": "Same answers. No theology."}),
 [{"at": 0.06, "event": "Title lands"},
  {"at": 0.24, "event": "Three prescription rows arrive, terracotta stamps"},
  {"at": 0.7, "event": "The grounding row lands last, stamped 'Not required' in grey"},
  {"at": 0.9, "event": "Note lands"}])

beat("B19", "ACT IV — THE WALL", "REMOTION",
 "And that is the finding, stated as plainly as Bear states it. A foundation whose removal leaves the building standing was never the foundation.",
 "ReqRingWord — the essay's central image",
 rem("ReqRingWord", {
   "before": "A foundation whose removal leaves the building standing ",
   "word": "was never the foundation",
   "after": ".",
   "attribution": "BROWN · THE DIGNITY THAT CAN BE DESTROYED",
   "note": "The building stands without its load-bearing wall.",
   "spark": "Never load-bearing."}),
 [{"at": 0.1, "event": "The line types up, full frame"},
  {"at": 0.5, "event": "Ring draws around 'was never the foundation'"},
  {"at": 0.8, "event": "Attribution and note land"}])

beat("B20", "ACT IV — THE WALL", "REMOTION",
 "Now — this is a critique, not a demolition. Bear's verdict is that the prescriptions are correct, the theology is sincere, and the foundation is secure as a theological claim. What fails is the connective argument between them. That is a narrower charge, and a harder one to dismiss.",
 "ReqLedger — what survives the critique and what does not",
 rem("ReqLedger", {
   "title": "What the essay does and does not claim",
   "rows": [
     {"label": "The governance prescriptions are correct", "verdict": "Stands"},
     {"label": "The theological foundation is secure as theology", "verdict": "Stands"},
     {"label": "The account of what AI lacks is careful and persuasive", "verdict": "Stands"},
     {"label": "The argument connecting foundation to prescription", "verdict": "Missing", "accent": True},
   ],
   "note": "A failure of exposition, not of conviction. Three of four survive.",
   "spark": "Narrower. Harder."}),
 [{"at": 0.06, "event": "Title lands"},
  {"at": 0.26, "event": "Three 'Stands' rows arrive in grey"},
  {"at": 0.7, "event": "The last row lands, 'Missing' fills terracotta"},
  {"at": 0.9, "event": "Note lands"}])

beat("B21", "ACT IV — THE WALL", "REMOTION",
 "And the closing turn is the good one. The prayer was more honest than the theology. It never asks that an untouchable fact be recognised. It asks that conditions be changed — that something genuinely damaged be genuinely repaired.",
 "ReqLevers — the prayer against the theology",
 rem("ReqLevers", {
   "title": "The prayer knew first",
   "levers": [
     {"name": "The theology says", "sub": "dignity prevails beyond every circumstance — nothing to repair"},
     {"name": "The prayer asks", "sub": "that the lowly be raised — that conditions actually change"},
   ],
   "blocked": [],
   "note": "What is at stake is the journey, not the ground.",
   "spark": "The journey, not the ground."}),
 [{"at": 0.1, "event": "Title lands; two columns rise"},
  {"at": 0.5, "event": "Subtitles type in beneath each"},
  {"at": 0.84, "event": "Note lands — the essay's final position"}])

# ══ CLOSING BLOCK ══════════════════════════════════════════════════════════
beat("B22", "VERDICT", "BOOKEND",
 "So the verdict. This is a careful reading that ends up defending the document's conclusions while dismantling its account of why they hold. The prescriptions survive. The foundation turns out to be optional. And here is what would prove Bear wrong: a worked argument connecting inalienable dignity to those prescriptions, one a utilitarian could not simply route around. The encyclical does not contain it. Someone could write it.",
 "ClaudeVerdictArtifact — the verdict page",
 rem("ClaudeVerdictArtifact", {
   "artifactTitle": "verdict.md",
   "artifactHeading": "The Dignity That Can Be Destroyed",
   "artifactLines": [
     "The encyclical's AI governance prescriptions are correct.",
     "They are derivable from Pearl, Hayek and Polanyi with no theology.",
     "Para. 52 splits dignity four ways; only the ontological cannot move.",
     "But the urgent passages claim damage the ontological account forbids.",
     "A foundation whose removal leaves the building standing was never load-bearing.",
     "FALSIFIABLE: a worked derivation from dignity to prescription would overturn this.",
   ]}, motion="hold"),
 [{"at": 0.0, "event": "Artifact window opens on the cream stage"},
  {"at": 0.2, "event": "Verdict lines stagger in as spoken"},
  {"at": 0.9, "event": "Page holds"}])

beat("B23", "YOUR TURN", "BOOKEND",
 "Your turn. Take a document you already agree with — a mission statement, a policy, a constitution — and ask Claude to find the load-bearing wall. Which claim, if you deleted it, would leave every conclusion standing? That is the test Bear ran on an encyclical, and it works on anything that argues from a foundation. Run it on something you wrote.",
 "ClaudeComposerAsk — the viewer's prompt, read aloud",
 ask("Here is a document I agree with. Find the claim that, if deleted, would leave every one of its conclusions standing — then tell me what that says about the argument.",
     [], "Your turn.", "paste this into Claude…"),
 [{"at": 0.0, "event": "Composer types the viewer's prompt"},
  {"at": 0.62, "event": "Send arms terracotta; prompt holds while discussed"},
  {"at": 0.9, "event": "Held full-frame for the pause"}])

beat("B24", "OUTRO", "BOOKEND",
 "The Dignity That Can Be Destroyed. Liam, in for Bear.",
 "ClaudeTitleOutro — locked card, slug-seeded CLAWD mascot",
 rem("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG}, motion="hold"),
 [{"at": 0.0, "event": "Poster-serif title, terracotta terminal period"},
  {"at": 0.35, "event": "@NikBearBrown beneath — hardcoded"},
  {"at": 0.55, "event": "Slug-seeded CLAWD mascot; translation and scale only"}])

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE,
    "subtitle": "An encyclical says dignity cannot be touched, then prays for the lowly to be raised",
    "topic": TOPIC,
    "purpose": ("Films Brown's essay on the anthropological contradiction in Magnifica Humanitas: "
                "the document grounds AI governance in inalienable ontological dignity, but its "
                "strongest applied passages require dignity to be damageable — and the prescriptions "
                "are independently derivable from Pearl, Hayek and Polanyi, so the theological "
                "foundation is not load-bearing. Credits the document before criticising it, and "
                "names what would falsify the reading."),
    "source": [
      "Nik Bear Brown, 'The Dignity That Can Be Destroyed', Computational Skepticism, 2026-05-31 (primary)",
      "Leo XIV, Magnifica Humanitas, 15 May 2026 (quotations verified against vatican.va)",
    ],
    "audience": "Claude", "channel": "claude-liam", "engine": "kokoro",
    "voice_kokoro": "am_onyx", "palette": "claude", "register": "Teardown",
    "skill": "deep-explainer", "folderLabel": "@NikBearBrown", "aspect": "16:9", "fps": 30},
  "beats": beats}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")

from collections import Counter
body = [b for b in beats if b["lane"] != "BOOKEND"]
c = Counter(b["lane"] for b in body)
tot = sum(b["estimated_duration_s"] for b in beats)
print(f"beats {len(beats)} · body {len(body)} · {dict(c)} · est {int(tot//60)}:{int(tot%60):02d}")
run = prev = worst = 0
for b in body:
    run = run + 1 if b["lane"] == prev else 1
    prev = b["lane"]; worst = max(worst, run)
print(f"longest same-lane run: {worst}")
