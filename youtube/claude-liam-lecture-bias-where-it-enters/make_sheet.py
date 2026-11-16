#!/usr/bin/env python3
"""make_sheet.py: beat_sheet.json + SHOTLIST.md for claude-liam-lecture-bias-where-it-enters.

Lecture 6 (Chapter 6) of INFO 7375 Computational Skepticism for AI, Video 6 of 13. Source:
chapters/06-bias-where-it-enters-and-who-is-responsible.md (HEAD side of every merge block; see ACTS.md).
Numbers follow FACTCHECK.md and evidence/evidence.json, not the chapter where they differ.
Re-run after audio so measured durations flow into props (measured audio is carried forward when narration is unchanged).
"""
import json, hashlib
from pathlib import Path
HERE = Path(__file__).resolve().parent
BOOKS = HERE.parents[2]
ART = BOOKS / "brutalist.art"
SLUG = HERE.name
TITLE = "Bias: Where It Enters and Who Is Responsible"
SPOKEN_TITLE = "Bias: Where It Enters and Who Is Responsible."
PLAYLIST = "INFO 7375 — Computational Skepticism for AI (Lectures)"
SOURCE = BOOKS / "info-7375-computational-skepticism-for-ai/chapters/06-bias-where-it-enters-and-who-is-responsible.md"
BOOKENDS = {"BOPEN", "BIDEA", "BDEFS", "BVDT", "BHTF", "BOUT"}
EV = json.loads((HERE / "evidence/evidence.json").read_text())
SHELL = (HERE / "evidence/evidence.stdout.txt").read_text().rstrip("\n").split("\n")


def block(letter):
    """The evidence stdout lines of one worked example: from 'X. ...' to the line before the next lettered line."""
    out, on = [], False
    for ln in SHELL:
        if len(ln) > 2 and ln[1] == "." and ln[0].isalpha() and ln[0].isupper():
            on = ln[0] == letter
        if on:
            out.append(ln)
    return out

import shutil
pub = ART / "runtime/remotion/public" / SLUG
pub.mkdir(parents=True, exist_ok=True)
for png in (HERE / "captures").glob("*.png"):
    shutil.copy2(png, pub / png.name)


def common(bid, act, narration):
    return {"beat_id": bid, "act": act, "narration_text": narration,
            "estimated_duration_s": round(len(narration.split()) / 2.6 + 0.6, 2),
            "voice": "am_onyx", "engine": "kokoro", "persona": "liam"}


def manim(bid, act, narration, name, about, runner, reason, gate="SHOW"):
    b = common(bid, act, narration)
    b.update(lane="manim", proof_gate=gate,
             routing={"about": about, "runner_up": runner, "reason": reason},
             shot={"type": "GRAPHIC", "source": "own", "visual_intent": about, "motion_claim": reason,
                   "show": [{"at": 0.1, "event": "the cast is on the stage"},
                            {"at": 0.5, "event": "the spoken step lands as motion"},
                            {"at": 0.9, "event": "hold the result"}],
                   "manim": {"class": f"{bid}_{name}"}})
    b["qc"] = {"sparse_by_design": True,
               "sparse_reason": "Drawn diagram on the cream stage; negative space is the style, the motion carries the claim."}
    return b


def remotion(bid, act, narration, pattern, props, about, runner, reason, gate="SHOW"):
    b = common(bid, act, narration)
    b.update(lane="bookend" if bid in BOOKENDS else "remotion", proof_gate=gate,
             routing={"about": about, "runner_up": runner, "reason": reason},
             shot={"type": "REMOTION", "source": "own", "visual_intent": about, "motion_claim": reason,
                   "show": [{"at": 0.12, "event": "establish"}, {"at": 0.3, "event": "push in to what the sentence names"},
                            {"at": 0.85, "event": "hold"}],
                   "remotion": {"pattern": pattern, "props": props}})
    return b


def capture(bid, act, narration, name, url, label, moves, about, runner, aspect=16 / 9):
    b = remotion(bid, act, narration, "BrowserCapture",
                 {"url": url, "image": f"{SLUG}/{name}.png", "caption": f"{label} · captured 2026-10-10",
                  "moves": moves, "ringColor": "#A64A24", "imageAspect": aspect},
                 about, runner,
                 "SHOW-THE-THING rung 1: the real record is the evidence; the camera pushes to the passage the sentence names.")
    b["shot"]["capture"] = {"file": f"captures/{name}.png", "receipt": "captures/receipts.json"}
    return b


def table(bid, act, narration, title, headers, rows, note, about):
    return remotion(bid, act, narration, "LectureEvidenceTable",
                    {"title": title, "headers": headers, "rows": rows, "note": note, "instantReveal": True},
                    about, "Manim drawn table", "Rows carry the actual compared items; the ring moves on the spoken names.")


def act_card(bid, title):
    b = remotion(bid, title, title + ".", "FormACard", {"lines": [title]}, f"Act title: {title}", "Manim title with the act's first picture",
                 "A short act marker keeps the viewer oriented.", gate="CARD")
    b["qc"] = {"sparse_by_design": True, "sparse_reason": "Brief act-title boundary; deliberately a title, not a teaching diagram."}
    return b


PRO = "https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing"
KLE = "https://arxiv.org/abs/1609.05807"

I = "Three Teams, One Problem"
II = "What Bias Means"
III = "Selection Bias"
IV = "Judgment in the Loop"
V = "Historical and Implicit Bias"
VI = "Three Flavors, and How They Compound"
VII = "A Dataset Is Not the World"
VIII = "Two Fairness Claims, Both Correct"
IX = "Pearl's Ladder"
X = "Finding the Leverage"
XI = "Who Owns the Bias"

# ───────────────────────── opening three ─────────────────────────
bopen = common("BOPEN", "Opening",
               "INFO seventy-three seventy-five, Computational Skepticism for AI. Lectures. Bias: Where It Enters and Who Is Responsible. "
               "Learn where bias enters an AI system, which fix has the leverage to move it, and who owns it.")
bopen.update(lane="bookend", proof_gate="CARD",
             routing={"about": "Film identity and payoff", "runner_up": "Minimal title card",
                      "reason": "The lecture skill's approved first beat: portrait, playlist, film title, short payoff."},
             shot={"type": "CARD", "source": "own", "template": "lecture-title-slide-16x9",
                   "narration_contract": "playlist-title-summary-v1", "motion": "hold",
                   "visual_intent": "Professor Bear portrait, exact film title, short payoff, series position, visible from frame zero.",
                   "show": [{"at": 0, "event": "Complete populated lecture opener visible for the whole narration"}]},
             qc={"sparse_by_design": True, "sparse_reason": "Identity card; teaching motion starts in BIDEA."})

bidea = remotion("BIDEA", "Opening",
                 "Namaste. This is Liam, in for Bear, with lecture six of INFO seventy-three seventy-five, Computational Skepticism for AI, "
                 "at Northeastern University. When a system is biased, the reflex is to fix the model. That's the fix nearest your hands, "
                 "and very often it isn't the one that works.",
                 "BrutalistHesitantWriter",
                 {"text": "The system is biased,\nso fix the model", "triggerWords": "fix the model",
                  "replacementWords": "find where the bias lives", "fontSize": 70, "charMs": 22, "hesitateBetween": 6,
                  "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
                 "The reflex the film corrects", "Overview card",
                 "The writer types the reflex and corrects one phrase into the film's question.")
bidea.update(lead_silence_s=0.8)
bidea["qc"] = {"sparse_by_design": True, "sparse_reason": "Hesitant-writer opening: the correction is the motion."}

TERMS = [("Estimator", "A rule that turns data into a number"),
         ("Base rate", "How common an outcome is in a group"),
         ("Label", "The answer a model learns to predict"),
         ("Proxy", "A feature that stands in for another"),
         ("Protected group", "A group shielded from unfair treatment"),
         ("Causal graph", "Arrows showing what causes what")]
bdefs = remotion("BDEFS", "Terms",
                 "Six terms. An estimator is a rule that turns data into a number. A base rate is how common an outcome is in a group. "
                 "A label is the answer a model learns to predict. A proxy is a feature that stands in for something else. "
                 "A protected group is a group shielded from unfair treatment. And a causal graph is a set of arrows showing what causes what.",
                 "ClaudeDefinitions",
                 {"title": "Terms In This Lecture", "terms": [{"term": t, "meaning": m} for t, m in TERMS], "folderLabel": "@NikBearBrown"},
                 "Prerequisite vocabulary", "Library icon row", "Six words the acts lean on, one plain line each.", "CARD")
bdefs["qc"] = {"sparse_by_design": True, "sparse_reason": "Terms card: six prerequisites, one line each."}

# ───────────────────────── body ─────────────────────────
B = [bopen, bidea, bdefs,
 act_card("A1", I),
 manim("B01", I, "Here's a parable, built to isolate a real pattern, not a case from any filing. A deployed AI system produces biased outcomes, "
       "reproducibly. Three engineering teams get the same job: fix it.",
       "Parable", "A biased system and three teams, same gap", "Isometric team figures (banned: person tokens)",
       "Two outcome bars start unequal and three team flags land beside them."),
 manim("B02", I, "Team one rewrites the loss function. They add a fairness penalty, a term that punishes unequal error rates across protected "
       "groups, and retrain on the same data. The gap shrinks a little. Not enough.",
       "TeamOne", "Team one: penalty on the model, gap shrinks a little", "Isometric box",
       "A penalty tag clips onto the model block and the gap bars shorten slightly."),
 manim("B03", I, "Team two fixes the data. They find the under-represented group, run a costly new collection, and retrain. The gap changes shape: "
       "smaller in some places, larger in others.",
       "TeamTwo", "Team two: data rebalanced, gap changes shape", "Stat card",
       "New data blocks fill the thin column and the gap bars reshuffle instead of vanishing."),
 manim("B04", I, "Team three touches neither the model nor the data. They look at the room the model was deployed into. A human reviewer reads its "
       "outputs, and the reviewer's own patterns amplified the bias. Team three changes the review process, and the gap falls by an order of magnitude.",
       "TeamThree", "Team three: the review step, gap collapses", "Isometric desk",
       "The reviewer block lights up on its name and the gap bars drop to almost nothing."),
 manim("B05", I, "Teams one and two weren't wrong. They made real, small reductions, on real paths that carried little of the bias. Team three had "
       "leverage, and it wasn't luck. It came from a way of looking the other teams hadn't used.",
       "ThreePaths", "Three interventions, three paths of different width", "Bar chart",
       "Three paths draw from cause to outcome; two stay thin and one runs thick."),
 manim("B06", I, "That way of looking is the subject. The temptation is to fix what's nearest your hands. The leverage is usually somewhere else. "
       "So before fixing anything, ask: where does this bias live, and which intervention has the most leverage on it?",
       "NearVsLever", "Nearest fix versus highest-leverage fix", "Question card",
       "A near marker sits on the model while the question's ring travels down the chain to the real node."),

 act_card("A2", II),
 manim("B07", II, "In the newspapers, bias means unfair or prejudiced. That meaning is built for moral clarity, not for engineering. In statistics, "
       "bias is a property of an estimator, a rule that turns data into a number. The formal meaning gives up the moral punch and buys you something "
       "you can act on: it tells you where to intervene.",
       "TwoMeanings", "Everyday meaning versus the estimator", "Split text card",
       "The loose word splits into two machines: one with a verdict, one with data in and a number out."),
 manim("B08", II, "Call the true quantity theta, and your estimate theta hat. Bias is the expected value of theta hat, minus theta. Zero means unbiased: "
       "maybe wrong on any one dataset, but not systematically wrong. Nonzero means systematically off, in one direction.",
       "BiasEquation", "Bias = E[θ̂] − θ with the offset on a number line", "Equation alone",
       "The equation assembles term by term while the cloud of estimates drifts off the true value and the offset arrow draws."),
 manim("B09", II, "Here's the consequence that matters most. More data will not fix a biased estimator. It converges, with growing confidence, to the "
       "wrong answer. More data narrows the scatter. It doesn't move the offset.",
       "MoreData", "Estimates narrow around the wrong value as n grows", "Static two-curve chart",
       "Histograms of real simulated estimates narrow at n = 10, 100, 1,000, 10,000 while staying centred off the true line."),
 remotion("B10", II, "Here is the run behind that picture. The true rate is thirty percent, but the filter keeps four in ten positives and eight in "
          "ten negatives. Whatever the sample size, the estimate settles near seventeen and a half percent. The spread shrinks. The error stays.",
          "CCPlainShell",
          {"title": "python3 evidence.py — recorded output (constructed example)", "fontSize": 32, "startCue": 8, "lineGap": 12,
           "lines": block("A")},
          "The simulation's real output", "Manim table of the same numbers",
          "SHOW-THE-THING / EXECUTABLE-EVIDENCE: the script's recorded stdout, line by line."),
 manim("B11", II, "This is exactly what happened in nineteen thirty-six. The Literary Digest magazine polled about two point four million people and predicted "
       "that Landon would beat Roosevelt. Roosevelt won with about sixty-one percent of the vote.",
       "Poll1936", "A huge sample pointing the wrong way", "VOX archival still (not needed: the numbers are the evidence)",
       "A block of 2.4 million sample dots grows beside the result bar that points the other way."),
 manim("B12", II, "Peverill Squire's nineteen eighty-eight analysis found two problems working together. The mailing list leaned toward people with cars and "
       "telephones in the depths of the Depression, and the people who answered differed again from those who didn't. More ballots drawn the same way "
       "would have repeated the error.",
       "SquireFrame", "Mailing list skew then non-response, two filters", "Funnel",
       "The population narrows through two successive filters and the surviving tint no longer matches the whole."),
 manim("B13", II, "So now we can say what the ten mechanisms of bias are: ten distinct ways to make that expression, the expected estimate minus the truth, "
       "nonzero. Each has its own causal structure and its own fix. Confuse them and you apply the right intervention at the wrong place.",
       "TenWays", "Ten sources of one offset", "Chip grid",
       "Ten dots land one by one on the offset arrow, each adding to the gap."),

 act_card("A3", III),
 manim("B14", III, "Here are the ten, as places in a pipeline where the estimate can drift from the truth. Selection and sampling, when people are collected. "
       "Data entry, when they're recorded. Observer, self-report and coding, when they're measured. Confirmation, publication, historical and implicit follow.",
       "TenMap", "The ten entry points along one pipeline", "FormB icon row",
       "A pipeline draws left to right and the ten names pin to their stage as they are spoken."),
 manim("B15", III, "A note on counting. Later we'll meet pairs, like aggregation with subgroup masking. Those aren't an eleventh and twelfth mechanism. "
       "They're derived interactions of the ten. The ten are the alphabet, and the pairs are a short list of common words.",
       "Alphabet", "Ten primitives, compounds are pairs of them", "Text card",
       "Two of the ten join by a bridge labelled compound; no new dot appears."),
 manim("B16", III, "Start with selection bias, and watch how it enters. You write a reasonable query: patients with a complete lab panel within six hours "
       "of admission. Nobody decides to exclude anyone. The exclusion rides in on the reasonableness.",
       "QueryFilter", "A reasonable query silently drops people", "Isometric conveyor",
       "Patient dots pour through the query gate; those without a timely panel fall away grey."),
 manim("B17", III, "Your estimator computes the average outcome among the people in your sample. You wanted the average in the population. Those two are equal "
       "on exactly one condition: whether you land in the sample must not depend on the outcome. The moment it does, the estimate is biased before a "
       "single parameter is fit.",
       "SelectionEquation", "E[Y | in sample] versus E[Y]", "Equation alone",
       "Two expectations stand side by side; the condition appears and then breaks, turning the equals sign into not-equals."),
 manim("B18", III, "Take a sepsis model, as an illustration. The patients too critical to have labs drawn on time are exactly the ones who most need the alert, "
       "and the six-hour filter drops them. The model learns what predicts sepsis among the stable, then is asked about the unstable. It underestimates their risk.",
       "SepsisFilter", "Kept stable patients, dropped critical ones", "Bar chart",
       "The critical column is cut off by the filter; the model's risk bar for it stays low, below the true level."),
 manim("B19", III, "You can correct for selection you observed. Inverse probability weighting gives each kept person a weight of one over their chance of "
       "being kept, so survivors stand in for the people dropped. In the same simulation, the naive estimate is about eighteen percent. Weighted, it's "
       "about thirty.",
       "IPW", "Weights restore the dropped people", "Table",
       "Kept dots swell by 1/P and the estimate marker slides from 0.18 to 0.30."),
 manim("B20", III, "But weighting only works if the variable that drove the selection was recorded. If it wasn't, you have nothing to weight on. "
       "That isn't a modeling problem you can solve at your desk. It's a data-collection problem, and the honest answer is to collect differently.",
       "NothingToWeight", "Unrecorded driver, nothing to weight", "Text card",
       "A ghosted variable shows a question mark and the weight arrow finds nothing; a new collection arrow draws instead."),

 act_card("A4", IV),
 manim("B21", IV, "Five more mechanisms share a spine: somewhere a person exercises judgment, and their prior leaks into the record. Confirmation bias is a "
       "researcher's prior shaping what gets collected, kept and reported. Observer bias is that prior inside one measurement, like an annotator who "
       "knows the earlier diagnosis.",
       "PriorLeak", "A prior leaking down a chain of judgments", "Isometric pipes",
       "A terracotta dye drops into the first stage and seeps into each later stage on its name."),
 manim("B22", IV, "Self-report bias is the subject's own prior: people report voting more and drinking less than they do. Data-coding bias enters when "
       "judgment squeezes material into categories. And publication bias is the same leak across a whole literature: significant results get printed, nulls "
       "stay in drawers.",
       "PriorLeak2", "The remaining three of the five", "Icon row",
       "The dye reaches three more stages and a drawer of grey papers slides shut at the end."),
 manim("B23", IV, "The diagnostic where two humans code the same thing is Cohen's kappa: agreement beyond chance. If kappa collapses when you unblind the "
       "annotators, that's direct evidence of observer bias. In a constructed example, it falls from point six to point two.",
       "Kappa", "Kappa formula with blinded vs unblinded counts", "Table",
       "Two agreement tables fill and the kappa bar drops from 0.6 to 0.2 on 'unblinded'."),
 manim("B24", IV, "Low kappa on particular items rather than particular people points at data-coding instead: the category is underspecified, not the coder. "
       "For publication bias the analogue is the funnel plot. A missing lower-left corner is the drawer of small null studies made visible.",
       "Funnel", "Funnel plot with a missing corner", "Matrix of disagreement",
       "Simulated study dots fill a funnel, then the unpublished ones fade out of the lower-left corner."),
 manim("B25", IV, "None of these five entered through the model. They entered upstream of the data, when a human judged. So the fixes look like "
       "organizational practice: pre-registration, blinding, adversarial review. Engineers reach past them because they don't look like engineering, "
       "which is exactly why the bias survives.",
       "NotTheModel", "Model greyed, three practices on the human step", "Isometric stamps",
       "The model block greys out while three practice tags land on the upstream human step."),
 manim("B26", IV, "Two more are quieter, and people mistake them for noise. Data-entry bias is patterned transcription error: a form that buries the accurate "
       "diagnosis code three menus deep gets the nearest code instead, and a whole class of conditions is undercoded in one direction. Verify against source "
       "documents; don't auto-correct.",
       "DataEntry", "A buried menu choice pushes entries one way", "Form mock",
       "A cursor skips the deep accurate option and the tally bars lean in one direction."),
 manim("B27", IV, "Sampling bias is selection's accessibility cousin: some groups are under-represented because they were hard to reach, not because of "
       "their outcomes. A remote-work survey pushed through LinkedIn over-represents credentialed professionals. When outside data gives the true sizes, "
       "weight each group by its population share over its sample share.",
       "Reweight", "Population share versus sample share and the weight", "Bar chart",
       "Sample bars sit off the population bars; each is rescaled by the weight on its name."),

 act_card("A5", V),
 manim("B28", V, "Now the one that breaks the pattern. In every mechanism so far, something was wrong with the data: a filter, a prior, a slip. Historical bias "
       "has none of that. The sample is representative. The labels are accurate. The data is a faithful recording of the world that produced it. "
       "And it is still poison.",
       "FaithfulData", "Three ticks, and the harm remains", "Checklist card",
       "Three checks tick off one by one and the harm marker stays lit beside them."),
 manim("B29", V, "Imagine a hiring model trained on ten years of promotion records at a company that promoted men into engineering roles at higher rates. "
       "It learns the historical outcome given the candidate, and learns it well. Every metric comes back green. But the historical outcome isn't the fair "
       "outcome. Its accuracy is the harm.",
       "HiringHistory", "P(historical | x) is not P(fair | x)", "Equation alone",
       "Green metric lights come on, then the two conditional probabilities slide apart with an unequal sign."),
 manim("B30", V, "So the fixes can't be data-quality fixes; there's no defect to repair. They lower the leverage of the historical signal on today's prediction: "
       "a less-biased proxy for the outcome, a fairness constraint, or weighting recent records over records from more discriminatory periods. "
       "Each trades predictive fit for less inheritance, and a person decides how much fit to spend.",
       "FitVsInheritance", "Trade-off curve with a human-chosen point", "Three-option card",
       "A fit-versus-inheritance curve draws and a dial the human sets slides along it."),
 manim("B31", V, "Implicit bias, the unconscious associations of the people in the pipeline, isn't really a tenth peer. It isn't an entry point. It's the "
       "medium several of them swim in: an underground water table, with confirmation, observer, coding and publication bias as the springs where it "
       "reaches daylight.",
       "WaterTable", "Water table with four springs", "Icon row",
       "A blue-grey water line draws below ground and four springs break the surface on their names."),
 manim("B32", V, "Because it has no single point, it resists a point fix. One handle is a downstream audit: compare the rate of positive predictions across "
       "groups. But read a gap as a flag, not a verdict, since real differences in base rates produce the same gap. The fixes with leverage are structural: "
       "diverse teams, structured decisions, continuous auditing.",
       "Structural", "An audit flag and three structural supports", "Three-option card",
       "A flag rises over a gap, then three supports are set beneath the whole pipeline."),

 act_card("A6", VI),
 manim("B33", VI, "When people say the model is biased, they can mean three different things. Dataset bias: the training set doesn't represent the people "
       "the system is deployed on. A face system trained mostly on light-skinned faces, then used on everyone, is the textbook example. The bias is in the sample.",
       "FlavorDataset", "Sample versus deployment population", "Pie charts",
       "Two population blocks are compared and a thin slice is missing from the training one."),
 manim("B34", VI, "Label bias: the labels encode a biased process. A recidivism predictor trained on arrest data isn't predicting who commits crimes. It's "
       "predicting who gets re-arrested. Those are different variables, and re-arrest is a biased measurement of the thing we care about.",
       "FlavorLabel", "Crime, policing, re-arrest: the label sits on the last", "Text card",
       "A policing filter draws between crime and re-arrest and the label tag lands on re-arrest."),
 manim("B35", VI, "Structural bias is the hard case. The data is fine, the labels are fine, the model does its job, and the outcomes are still unfair. A hiring model "
       "perfectly predicts who succeeds at a company today, but success depends on mentorship, sponsorship and interesting projects that were never evenly "
       "distributed. The model is correct, and its correctness is the problem.",
       "FlavorStructural", "Correct model on an uneven floor", "Isometric stairs",
       "Three green ticks appear over a staircase whose steps are uneven for two groups."),
 table("B36", VI, "Put them side by side. Dataset bias lives in the sample, and the fix is to resample or broaden collection. Label bias lives in the labeling "
       "step: fix the process or find a better proxy. Structural bias lives in the world the model sits in, and no model or data fix reaches it.",
       "Three Flavors", ["Flavor", "Lives in", "Fix"],
       [["Dataset", "The sample", "Resample, broaden"], ["Label", "The labeling step", "New process or proxy"], ["Structural", "The deployment world", "Change the structure"]],
       "Summary table; the mechanisms behind each are covered above", "Three flavors and where each is fixed"),
 manim("B37", VI, "Treat structural bias as a dataset problem and you'll spend a quarter and move the disparity nowhere. Bear calls that the most common "
       "failure in this field. That's his judgment from experience, not a measured rate.",
       "WrongFix", "A dataset fix aimed at a structural problem", "Stat card",
       "A resampling arrow hits the data stage while the gap bars beyond it do not move."),
 manim("B38", VI, "In real systems several mechanisms run at once. Selection compounds historical bias: there's less data on the under-represented group, and the "
       "data that exists was generated under discriminatory conditions. Rebalancing fixes the first, and makes the second worse. You now hold more "
       "discriminatory data, accurately represented.",
       "SelectionHistorical", "Rebalancing adds historical bias", "Two-layer card",
       "New blocks fill the thin group and each carries the historical tint, so the tint total grows."),
 manim("B39", VI, "Observer bias compounds with data coding. Annotator priors become categorical rules baked into the labels. Agreement scores capture the "
       "combined effect but can't separate the two. Disagreement clustered on items points to coding. Clustered on annotators, it points to observers.",
       "ObserverCoding", "Disagreement grid: item columns versus annotator rows", "Kappa bars",
       "A grid of agreements lights a column for coding, then a row for observers."),
 manim("B40", VI, "Confirmation compounds with publication. A team designs a study to confirm its hypothesis, gets a positive result, and publishes, while null "
       "results from other groups vanish. Trim-and-fill can correct the publication part. It cannot touch the study design.",
       "ConfirmPublish", "Two inflations stacked", "Funnel",
       "A stacked bar carries design inflation, then publication inflation; the correction removes only one slice."),
 manim("B41", VI, "Bear keeps a short working list of pairs that amplify each other: selection with historical, observer with coding, confirmation with "
       "publication, sampling with measurement, aggregation with subgroup masking, evaluation with deployment, annotation with class imbalance, and linkage "
       "with re-identification. Once you confirm one, check its partner first.",
       "PairList", "Eight amplifying pairs", "Table",
       "Eight pairs of chips link in turn, each pair joined by a bridge."),

 act_card("A7", VII),
 manim("B42", VII, "A dataset isn't the world. It's a recording of a slice of it, made by particular people, at a particular time, with particular "
       "instruments, for particular purposes. Each leaves a fingerprint. To use a dataset responsibly, read it as a historian reads an archive: what was "
       "collected, what was excluded, who decided, and why.",
       "Archive", "A dataset as an archive with four fingerprints", "Text card",
       "A box of records opens and four fingerprint tags land on it, one per spoken question."),
 capture("B43", VII, "Take COMPAS, a risk-assessment tool used in Broward County, Florida. In twenty sixteen, ProPublica analyzed scores for people arrested there "
         "in twenty thirteen and twenty fourteen. Among defendants who did not re-offend, forty-four point nine percent of Black defendants had been labeled "
         "higher risk, against twenty-three point five percent of white defendants.",
         "propublica", PRO, "propublica.org · Machine Bias, Angwin, Larson, Mattu, Kirchner, May 23, 2016",
         [{"at": 0.0, "x": 0.5, "y": 0.2, "scale": 1.2},
          {"at": 0.3, "x": 0.5, "y": 0.2, "scale": 1.7, "ring": [0.229, 0.168, 0.542, 0.065]}],
         "ProPublica's own table, the false-positive row ringed", "Manim chart of the same four numbers"),
 manim("B44", VII, "And among defendants who did re-offend, forty-seven point seven percent of white defendants had been labeled lower risk, against twenty-eight "
       "percent of Black defendants. As ProPublica reported them, the errors fell unevenly, in opposite directions.",
       "ErrorBars", "ProPublica's four published error rates as bars", "Table capture",
       "Four bars grow from the published rates; the two false-positive bars, then the two false-negative bars, pair up."),
 manim("B45", VII, "The tool's maker, Northpointe, answered with a different analysis. Within each risk score, they said, about the same share of people "
       "re-offended in both groups. In their terms, the score was equally accurate for everyone: predictive parity.",
       "Calibration", "Within each score, equal re-offense rates (schematic)", "Capture of the response",
       "Two calibration lines for the two groups lie on top of one another across the score axis."),
 manim("B46", VII, "There's something deeper in the data. The label wasn't whether this person committed another crime. It was whether this person was "
       "re-arrested. Re-arrest depends on crime and on policing. If policing is uneven, re-arrest is an uneven measurement of crime, and every model trained "
       "on it inherits the unevenness.",
       "ReArrest", "Crime and policing both feed the label", "Two-arrow card",
       "Two arrows, crime and policing, merge into the re-arrest label and the policing arrow is lit."),
 manim("B47", VII, "The modeler thinks they're predicting recidivism. They're actually predicting re-arrest, given recidivism, given policing, given everything that "
       "shapes both. Deployed without that frame, the model launders the unevenness through an algorithm, and makes it invisible.",
       "Nested", "Recidivism nested inside policing inside the label", "Layers",
       "Nested frames close around the thing the modeler thinks they predict and the label drops in front."),

 act_card("A8", VIII),
 capture("B48", VIII, "Both analyses were correct. They were measuring different things. When two groups have different base rates, no score can satisfy "
         "both. Kleinberg, Mullainathan and Raghavan proved it in a twenty sixteen paper, and Chouldechova showed the same incompatibility for recidivism tools.",
         "kleinberg", KLE, "arxiv.org · Kleinberg, Mullainathan, Raghavan, Sept 2016",
         [{"at": 0.0, "x": 0.45, "y": 0.2, "scale": 1.0},
          {"at": 0.3, "x": 0.45, "y": 0.2, "scale": 1.3, "ring": [0.012, 0.115, 0.83, 0.165]}],
         "The theorem's own abstract", "Manim equation card"),
 manim("B49", VIII, "Here's the plain version. Suppose group one has a true re-offense rate of thirty percent, and group two fifty. Make the score calibrated, "
       "so a given score means the same in both. Now to equalize false positives you'd have to put the threshold in a different place for each group, "
       "which is treating people differently by group.",
       "Thresholds", "Two groups, one calibrated score, thresholds", "Two histograms",
       "Two score distributions at different base rates; one shared threshold, then a second threshold appears and equal treatment breaks."),
 manim("B50", VIII, "Here's the algebra. For a calibrated score, the odds of being right when flagged equal the base-rate odds, times the ratio of the true positive "
       "rate to the false positive rate. Hold the first equal, with different base rates, and the ratio of the rates has to differ between groups.",
       "ImpossibilityAlgebra", "v/(1-v) = p/(1-p) · t/f built term by term", "Text card",
       "The identity assembles term by term with each symbol named beside it, then the base-rate factor splits in two."),
 remotion("B51", VIII, "Run the numbers. Fix the accuracy of a flag at sixty percent and the true positive rate at seventy percent for both groups. Then the false "
          "positive rate is forced: twenty percent in group one, and forty-six point seven in group two. That gap isn't a bug. It's arithmetic.",
          "CCPlainShell",
          {"title": "python3 evidence.py — recorded output (constructed example)", "fontSize": 32, "startCue": 8, "lineGap": 12,
           "lines": block("F")},
          "The impossibility computed", "Manim bars", "EXECUTABLE-EVIDENCE: the script's recorded stdout, not a typed result."),
 manim("B52", VIII, "The three criteria are calibration, equal false positive rates, and equal false negative rates. With different base rates they cannot all hold "
       "at once, unless prediction is perfect. So the choice between fairness metrics isn't a technical choice. It's a values claim: which kind of error are "
       "we less willing to make?",
       "Triangle", "Three criteria that cannot all hold", "Table",
       "A triangle of three criteria: two corners light and the third goes dark each time one is chosen."),
 manim("B53", VIII, "Who bears the cost of each error, what the model is used for, and the politics of the deployment settle that choice. Engineers who treat it as "
       "pure optimization are making a values choice anyway: the one their loss function encodes, while appearing neutral. That's Professor Bear's argument. "
       "I'm presenting it as an argument, not a finding.",
       "HiddenValues", "A loss function with its hidden value revealed", "Text card",
       "A loss formula sits under a neutral label and a hidden tag reading 'a value choice' is revealed in it."),
 manim("B54", VIII, "One case to be careful with. In twenty nineteen the Apple Card's credit limits drew allegations of bias. New York's financial regulator "
       "investigated, and in March twenty twenty-one reported no evidence of unlawful discrimination: applicants with similar credit characteristics generally "
       "had similar outcomes. It did fault customer service and transparency. So treat it as a case of how a claim gets adjudicated, not a proven disparity.",
       "AppleCard", "The regulator's own sentences, quoted", "Capture (blocked by the site's bot protection; not bypassed)",
       "A document card quotes the regulator's lines and the one about transparency is ringed last."),
 table("B55", VIII, "So pick the audit criterion that fits the harm structure of the deployment. Calibration parity means a score means the same for every group. Equal "
       "false positive rates share the cost of being wrongly flagged. Equal false negative rates share the cost of being missed. The theorem rules out all three.",
       "Fairness Criteria", ["Criterion", "What it requires"],
       [["Calibration parity", "A score means the same"], ["Equal false positives", "Wrong flags shared equally"], ["Equal false negatives", "Misses shared equally"], ["All three", "Only if base rates are equal"]],
       "Formal definitions: probabilities conditioned on score, outcome and group", "The three criteria and their joint limit"),

 act_card("A9", IX),
 manim("B56", IX, "To tell a system that merely correlates a bias from one that causes it, we need a tool from Judea Pearl: a ladder of causal reasoning, with "
       "three rungs. We'll work the first two.",
       "Ladder", "A three-rung ladder", "Text card",
       "A ladder builds rung by rung; the top rung is drawn ghosted."),
 manim("B57", IX, "Rung one is association: what's the probability of Y, given that we observe X? It's what most machine learning lives on. It's what calibration "
       "curves describe, and what most fairness metrics measure. It's also where most thinking about deployed AI quietly stops.",
       "RungOne", "P(Y | X) as a lookup in observed data", "Equation alone",
       "A scatter of observed pairs and a condition bar select the slice; the conditional probability reads off it."),
 manim("B58", IX, "Rung two is intervention: the probability of Y if we set X to a value. Pearl writes it with do. The notation does real work. Observing X can be "
       "tangled up with everything that moves with X. Making X happen severs those tangles.",
       "RungTwo", "do(X) cuts the arrows into X", "Equation alone",
       "A graph with a hidden cause behind X; on 'do' the incoming arrow is cut and X is held by hand."),
 manim("B59", IX, "The classic illustration is the rooster and the sun. Watch roosters and sunrises, and the sun is very likely up after a crow. But prevent "
       "the rooster from crowing, and the sun rises anyway. Observation said they were associated. Intervention said the rooster isn't the cause.",
       "Rooster", "Crow and sunrise, observed versus intervened", "Two probabilities",
       "A crow and a sun rise together; the crow is blocked and the sun still rises."),
 manim("B60", IX, "Rung three is counterfactual: what would have happened to this specific case if X had been different, holding everything else fixed? It's the "
       "hardest to reach from data alone. Here it just sits at the top of the ladder, visible, not yet climbed.",
       "RungThree", "The ghost rung stays at the top", "Text card",
       "The top rung lights with a question mark and a dashed arrow reaches toward it without arriving."),
 manim("B61", IX, "For our problem, the probability of loan denial, given race equals x, is the observational quantity. It's what the model sees in training data. "
       "The probability of denial if we set race to x, holding everything else fixed, is interventional. It asks whether the decision would change if we "
       "changed only that variable.",
       "DenialTwoWays", "Observed versus do-version of the same sentence", "Equation alone",
       "Two probability expressions sit side by side; only the second has an arrow cut into race."),
 manim("B62", IX, "The two can come apart. A model can show no disparity on rung one while hiding one on rung two, if you intervene on race-correlated features. "
       "Or it can show a rung-one disparity that vanishes on rung two, because it runs entirely through legitimate features. Without telling them apart, you can't "
       "tell a fair model from one that's merely been smoothed.",
       "ComeApart", "Four combinations of seen and caused", "2x2 grid",
       "A two-by-two fills: seen versus caused; the off-diagonal cells are ringed on their names."),
 manim("B63", IX, "Most deployed mitigation works on rung one: adjust the conditional distributions until the metric reads the way the engineer wants. "
       "That's sometimes useful and rarely sufficient, because whether a variable causes the bias is a rung-two question, and rung one can't answer it.",
       "RungOneStops", "Mitigation stuck at the first rung", "Ladder alone",
       "A figure climbs to rung one and stops; a gap sits between it and the do-rung."),
 table("B64", IX, "Here are the same audit questions asked at each rung. For loan denial: is the rate equal across groups, or would it change if race changed and nothing "
       "else did? For hiring: is the hire rate proportional, or would two identical applicants be treated differently?",
       "Same Question, Two Rungs", ["Question", "Rung one", "Rung two"],
       [["Loan denial", "Equal rate by group?", "Change if race changed?"], ["Error rates", "Equal in the test set?", "Change if group changed?"], ["Hiring", "Hire rates proportional?", "Same for identical applicants?"]],
       "Equal rung-one metrics do not certify causal fairness", "Rung one versus rung two audit questions"),

 act_card("A10", X),
 manim("B65", X, "Back to the three teams. Each intervened at a different point in the chain from the world to the decision. Team one on the model. Team two on "
       "the training data. Team three on the deployment context. All three were interventions, rung-two doings. But they had different leverage.",
       "ThreeTeamsGraph", "Three intervention points on one chain", "Isometric pipeline",
       "A chain from world to decision lights three markers on its three stages."),
 manim("B66", X, "Draw the causal graph. The protected attribute sits at the top. Below it, proxies, then the features the model uses, then the model's output. "
       "Then the deployment context: the reviewer, the threshold, the appeal process. And finally the outcome that lands on a real person's life.",
       "BuildGraph", "The causal graph, node by node", "Flowchart",
       "Nodes land top to bottom, each with its arrows, on its spoken name."),
 manim("B67", X, "Now list every path from the protected attribute to the outcome. In this constructed graph there are ten. Some run through the model. "
       "Some bypass it, through proxies straight into the reviewer or the threshold. Here is what each fix leaves open.",
       "PathCount", "Ten paths; what each intervention leaves open", "Table",
       "Ten paths highlight one at a time, then each intervention greys the paths it blocks."),
 manim("B68", X, "Team one blocked the paths through the model, and left four of ten open. Team two reshaped the sample, and left eight open. Team three, "
       "at the reviewer and the threshold, blocked all ten. Counting paths isn't measuring bias, but it shows what a fix can't reach.",
       "WhatIsLeftOpen", "Open paths after each team's fix", "Bar chart",
       "The same graph appears three times; blocked paths grey out and the open-path counter reads 4, 8, then 0."),
 manim("B69", X, "The procedure, in working form. One: draw the causal graph, from protected attribute through proxies, features, output and decision, to the "
       "outcome. Two: list every path from the attribute to the outcome, including the ones that bypass the model.",
       "Procedure12", "Steps one and two on the graph", "Numbered list (banned: bullet list)",
       "Step markers land on the graph: arrows first, then each path traced."),
 manim("B70", X, "Three: for each candidate intervention, ask which paths it blocks and which it leaves open. Four: pick the one that blocks the largest "
       "share of the bias-carrying paths, ideally without cutting paths the deployment needs for its core function.",
       "Procedure34", "Steps three and four as a choice", "Numbered list",
       "Candidate cuts slice the graph one by one; the chosen cut glows and the needed path stays open."),
 manim("B71", X, "Underneath is Descartes' doubt, turned on a pipeline. What would have to be true for this bias to live here? Suspend the tempting explanation, "
       "the model, nearest your hands, and make each candidate location survive the question. The location that survives is where you intervene.",
       "DoubtFilter", "Each location faces the question, one survives", "Text card",
       "Candidate nodes each meet the question mark and drop away until one stays."),
 manim("B72", X, "Why isn't this done more often? The model and the data are inside the engineer's house. The reviewer's behavior, the appeals process, the way "
       "the score gets read, live in someone else's. Drawing the full graph means crossing those boundaries, and the engineer who tries is often told it isn't their job.",
       "Houses", "Engineer's house versus other houses", "Isometric rooms",
       "House outlines draw around model and data; the graph's other nodes sit in other houses and the path crosses the walls."),

 act_card("A11", XI),
 manim("B73", XI, "Professor Bear argues that the political dimension of bias is the technical dimension. Which intervention works depends on which kind of bias you have. "
       "Which kind you have depends on a structural analysis of the deployment, the part people call political. Skip it and you produce tweaks that don't move the disparity.",
       "PoliticalTechnical", "Structural analysis sits inside the technical chain", "Venn",
       "A technical chain with a structural-analysis step that cannot be removed without breaking the link to the fix."),
 manim("B74", XI, "One of Bear's five supervisory capacities, the skills a person needs to oversee an AI, is problem formulation: seeing which question the "
       "model is really being asked, and which downstream decisions its answer feeds. That doesn't respect the line between technical and political. "
       "Keeping the line clean means handing the formulation to someone else, and any delegation can be tested.",
       "Formulation", "The question asked and the decisions it feeds", "Text card",
       "A question box feeds a row of downstream decisions; a gap opens where the formulation is delegated away."),
 capture("B75", XI, "Now the limit case. A twenty twenty-six study called Agents of Chaos red-teamed autonomous AI agents in a live lab. Its sixth case study, Agents "
         "Reflect Provider Values, sent benign but politically sensitive prompts to an agent backed by a model from a Chinese provider.",
         "aoc-p20", "https://www.tomerullman.org/papers/agentsOfChaos2026.pdf", "arXiv:2602.20021 · Shapira et al. 2026 · page 20",
         [{"at": 0.0, "x": 0.5, "y": 0.5, "scale": 1.0}, {"at": 0.3, "x": 0.5, "y": 0.59, "scale": 1.3, "ring": [0.165, 0.518, 0.67, 0.135]}],
         "The paper's own case summary, ringed", "Manim reconstruction", aspect=612 / 792),
 manim("B76", XI, "The authors report that the provider's API repeatedly cut off responses with a generic unknown error on those topics, silently stopping the agent "
       "from completing valid tasks. The team that deployed the agent made none of those choices, and its users could not see them.",
       "Truncated", "A reply cut off upstream with a generic error", "Chat card",
       "An agent's answer starts, then stops at a gate upstream and the words 'unknown error' stamp over it."),
 manim("B77", XI, "Draw the causal graph. The bias-carrying path doesn't run through the deploying team's data or code. It runs through the provider's training and "
       "hosting, upstream of everything that engineer controls. No intervention by the deploying team can reach it.",
       "UpstreamGraph", "The path starts outside the team's boundary", "Houses",
       "The team boundary draws; the biased node sits outside it with the path crossing in."),
 manim("B78", XI, "The deploying engineer's options are: switch providers, which is rarely possible at organizational scale; accept the bias, which is often what "
       "happens; or add downstream filtering and validation. The procedure still applies. Sometimes its answer is that the highest-leverage point is outside "
       "your reach, which is useful to know before you spend six months on the wrong thing.",
       "ThreeOptions", "Switch, accept, or filter downstream", "Three-option card",
       "Three doors: one locked, one open onto the bias, one with a filter gate."),
 manim("B79", XI, "That's the accountability move. Assigning the owner of a bias isn't assigning blame to a person. It's naming whoever sits at the leverage point. "
       "Sometimes that's you, because you chose the sample. Sometimes the labeling team, who wrote the manual. Sometimes the deployment owner, who built the review "
       "room. And sometimes the model provider.",
       "FourOwners", "Four possible owners of the node", "Icon row",
       "The traced path ends at a node; owner tags drop onto four candidate nodes in turn."),
 manim("B80", XI, "The graph is a machine for un-diffusing responsibility. It points at a node, and a node has an owner. Bear connects this to a question Hannah "
       "Arendt asked about systems where harm is the output of many role-bound people, none of whom feels accountable: the same question, restated for a pipeline.",
       "Undiffuse", "Diffuse blame condensing onto one node", "Text card",
       "A cloud of small blame dots drains along the graph and gathers on one node."),
 manim("B81", XI, "Where is Bear unsure? What would change his mind: a debiasing algorithm shown to remove structural bias, robustly, across domains and base-rate "
       "regimes, without touching the deployment context. He isn't aware of such a demonstration, and says the literature isn't finished.",
       "ChangeMind", "A falsifier he would accept", "Text card",
       "A claim stands on a test; a dashed counter-example slot is drawn empty."),
 manim("B82", XI, "And what he's still puzzling over: telling dataset bias from label bias when all you have is the labeled training set. They're causally distinct but "
       "observationally close. The diagnosis usually needs access to the labeling process, which other teams control. He says he doesn't know how to do this well.",
       "StillPuzzling", "Two look-alike blobs and a door to the labeling process", "Text card",
       "Two overlapping blobs read the same from the data; a door to the labeling step opens only from outside."),
]

# ───────────────────────── closing three ─────────────────────────
recaps = ["Bias is a systematic offset in an estimator, and more data does not remove it.",
          "Ten mechanisms put that offset in at different points of the pipeline.",
          "Dataset, label and structural bias each need a different fix.",
          "Two fairness claims can both be correct; choosing between them is a values call.",
          "Pearl's first two rungs separate correlating a bias from causing it.",
          "Find the highest-leverage path, then name whoever owns that node."]
recap = remotion("BVDT", "Recap", "Let's recap with Claude. " + " ".join(recaps), "ClaudeVerdictArtifact",
                 {"artifactTitle": "Recap", "artifactHeading": "INFO 7375 · Lecture 6", "artifactLines": recaps,
                  "brandLabel": "@NikBearBrown", "lectureLayout": True},
                 "Six-line recap", "Summary diagram", "One bare sentence per idea; nothing new.")
recap["lead_silence_s"] = 0.5
PROMPT = ("Help me run a leverage analysis on an AI system I know. I'll describe a decision it makes. Ask me for the protected attribute, the training "
          "data, the labels, and who reviews the output. Then draw the causal graph, list every path from the protected attribute to the outcome, "
          "say which intervention blocks the most paths, and name who owns that node. Flag anything you are guessing.")
task = remotion("BHTF", "Your turn", PROMPT, "ClaudeComposerAsk",
                {"greeting": "Your turn.", "topic": "INFO 7375 COMPUTATIONAL SKEPTICISM · LECTURE 6", "segment": "Trace One Bias to Its Owner",
                 "command": PROMPT, "runningText": "paste this into Claude…",
                 "output": ["Check: every arrow is something you can point to in the real system.",
                            "Check: the owner it names actually controls that node."],
                 "folderLabel": "@NikBearBrown", "largeText": True},
                "Transfer task", "Worksheet", "The viewer gets a usable prompt and two checks of their own.")
outro = remotion("BOUT", "Outro", SPOKEN_TITLE + " At Nik Bear Brown.", "ClaudeTitleOutro",
                 {"title": TITLE, "slug": SLUG, "subline": "", "handle": "@NikBearBrown", "lectureLayout": True},
                 "Locked title and channel sign-off", "None", "The exact title spoken over the locked outro.")
outro.update(kind="outro_voice", tail_silence_s=1.0)
outro["qc"] = {"sparse_by_design": True, "sparse_reason": "Locked outro centres only title, handle and mascot."}
B += [recap, task, outro]

# carry measured audio forward when narration is unchanged
old = {}
if (HERE / "beat_sheet.json").exists():
    old = {x["beat_id"]: x for x in json.loads((HERE / "beat_sheet.json").read_text()).get("beats", [])}
for x in B:
    prior = old.get(x["beat_id"], {})
    if prior.get("narration_text") == x["narration_text"]:
        for key in ("audio_file", "actual_duration_s"):
            if key in prior:
                x[key] = prior[key]
    if x["shot"]["type"] == "REMOTION":
        x["shot"]["remotion"]["props"]["durationSeconds"] = x.get("actual_duration_s", x["estimated_duration_s"])

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "spoken_title": SPOKEN_TITLE,
    "topic": "Where bias enters an AI pipeline, which fix has the leverage, and who owns it",
    "skill": "lecture", "style_preset": "lecture", "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro", "clock": "narration", "palette": "claude",
    "register": "Teardown", "fps": 24, "width": 3840, "height": 2160, "aspect_ratio": "16:9", "caption_policy": "sidecar",
    "series_title": "Computational Skepticism for AI", "playlist": PLAYLIST,
    "series_video_number": 6, "series_video_count": 13, "series_entry_video": "Video 1 · The Skeptic's Toolkit",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "audience": "INFO 7375 students (Fall 2026) and Claude Code practitioners",
    "chapter_number": 6,
    "lecture_opening_description": "Find where bias lives, then who owns the fix",
    "lecture_opening_title_lines": ["Bias: Where It Enters", "and Who Is Responsible"],
    "lecture_opening_template": "lecture-title-slide-16x9",
    "source_doc": str(SOURCE), "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "bookend_exempt": ["cold-open"],
    "bookend_exempt_reason": "lecture skill: opens on the narrated card then the hesitant writer; no composer cold open.",
    "tags": ["AI bias", "fairness", "causal inference", "Pearl", "INFO 7375", "Computational Skepticism for AI", "Northeastern University", "Liam", "Lecture"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")

rows = ["# SHOTLIST — " + TITLE, "",
        "**What.** One row per beat: what the sentence is about, the lane picked, the runner-up auditioned, and why the pick wins (BEST-BEAT LAW).",
        "**Why.** The pick must be the picture a viewer understands with the sound off; a runner-up proves the beat was auditioned.",
        "**Found.** Library asked first (`./art scenes`: causal graph, table with a ringed row, ladder, bar comparison, equation term by term, pipeline); "
        "the library has no causal-graph, no estimator or ladder-of-causation scene, so those are drawn in Manim (a registered Remotion scene was not built: "
        "every drawing is film-specific and lives in scenes.py). Real records are shown as themselves; run output is real stdout.", "",
        "| beat | about | lane picked | runner-up | why this one wins |", "|---|---|---|---|---|"]
for x in B:
    r = x["routing"]
    pick = (x["shot"].get("manim", {}).get("class") or x["shot"].get("remotion", {}).get("pattern") or x["shot"].get("template"))
    lane = "Manim" if x["shot"]["type"] == "GRAPHIC" else ("Remotion" if x["shot"]["type"] == "REMOTION" else "Card")
    rows.append(f"| {x['beat_id']} | {r['about']} | {lane} · `{pick}` | {r['runner_up']} | {r['reason']} |")
rows += ["", "## Tool beats and their SHOW-THE-THING rung", "",
         "| beat | thing | rung | what is on screen |", "|---|---|---|---|",
         "| B10, B51 | the evidence script | 1 · run | `evidence/evidence.py` run on this Mac; stdout verbatim (constructed example, labelled) |",
         "| B43 | ProPublica, Machine Bias | 1 · captured | the real table 'Prediction Fails Differently for Black Defendants', ringed |",
         "| B48 | arXiv, Kleinberg et al. | 1 · captured | the real abstract, the theorem sentence ringed |",
         "| B54 | New York DFS press release | 3 · quoted card | dfs.ny.gov returns a Cloudflare 403 to automated browsers; NOT bypassed. The regulator's sentences (fetched as text) are quoted on a drawn card |",
         "| B75 | Agents of Chaos, page 20 | 1 · the paper's own page, rendered from its PDF | Case Study #6 summary, ringed |",
         "", "Isometric lane (show-tell) auditioned for B01, B02, B04, B16, B35, B65, B72 and others: kept as a recurring simple cast only where the idea is a physical arrangement "
         "(B16 conveyor/gate drawn as a flat funnel; B35 steps). Causal graphs, equations and bar charts are flat Manim because the claim is a relationship, not an object."]
(HERE / "SHOTLIST.md").write_text("\n".join(rows) + "\n")
print(len(B), "beats;", sum(len(x["narration_text"].split()) for x in B), "spoken words;",
      round(sum(x.get("actual_duration_s", x["estimated_duration_s"]) for x in B) / 60, 1), "min")
