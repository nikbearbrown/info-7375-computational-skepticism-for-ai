"""scenes.py — claude-liam-cs-03-three-way-split Manim scenes (STD retrofit)

10 TELLS beats: B01 B02 B04 B05 B07 B08 B09 B10 B11 B12
Topic: Fairness impossibility — 3 definitions, 1 algorithm, math says no

Render:
  python3 -m manim scenes.py <ClassName> -r 1920,1080 --fps 30 --format mp4
  mv media/videos/scenes/1080p30/<ClassName>.mp4 media/<BXX>.mp4
"""
import json, pathlib, math
from manim import *

_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)

CREAM  = "#F2F0E9"
INK    = "#3D3929"
ACCENT = "#D97757"
MUTE   = "#7A7265"
TEAL   = "#2A9D8F"
CRIMSON = "#C1121F"

config.background_color = CREAM

DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _bs["beats"]})
except Exception:
    pass

def dur(bid): return DUR.get(bid, 8.0)
def serif(t, sz=40, clr=INK, **k): return Text(t, font="EB Garamond", font_size=sz, color=clr, **k)
def caps(t, sz=24, clr=MUTE, **k): return Text(t.upper(), font="Montserrat", font_size=sz, color=clr, weight=BOLD, **k)
def card(w, h, fill=WHITE, stroke=INK, sw=2): return RoundedRectangle(corner_radius=0.12, width=w, height=h, fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)


class B01_Title(Scene):
    def construct(self):
        d = dur("B01")
        line1 = serif("Three definitions of fairness.", sz=54, clr=INK)
        line2 = serif("One algorithm.", sz=54, clr=INK)
        line3 = serif("Math says you can't have all three.", sz=54, clr=CRIMSON)
        g = VGroup(line1, line2, line3).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        for l in [line1, line2, line3]:
            self.play(FadeIn(l, shift=UP*0.1), run_time=0.5)
        u = Line(line3.get_left()+DOWN*0.18, line3.get_right()+DOWN*0.18, color=ACCENT, stroke_width=4)
        self.play(GrowFromPoint(u, u.get_left()), run_time=0.5)
        self.wait(max(0.01, d - 2.5))


class B02_ThreeLawyersParadox(Scene):
    def construct(self):
        d = dur("B02")
        eyebrow = caps("hiring algorithm — three lawyers, three definitions", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        lawyers = [
            ("Lawyer A", "Calibration:\nWhen model says 60%, 60% of\nflagged candidates succeed.", TEAL),
            ("Lawyer B", "Equal FPR:\nFalse positive rate equal\nacross both groups.", INK),
            ("Lawyer C", "Equal FNR:\nFalse negative rate equal\nacross both groups.", CRIMSON),
        ]
        boxes = []
        for i, (name, text, color) in enumerate(lawyers):
            bg = card(3.8, 2.8, fill=WHITE, stroke=color, sw=2.5)
            name_lbl = Text(name, font="Montserrat", font_size=30, color=color, weight=BOLD)
            txt_lbl = serif(text, sz=26, clr=INK)
            grp = VGroup(name_lbl, txt_lbl).arrange(DOWN, buff=0.2)
            grp.move_to(bg.get_center())
            box = VGroup(bg, grp)
            box.move_to([(i - 1) * 4.2, 0.0, 0])
            boxes.append(box)
            self.play(FadeIn(box, shift=RIGHT*0.1), run_time=0.5)

        clash = serif("All three satisfied — if and only if base rates are equal.", sz=34, clr=INK)
        clash.to_edge(DOWN, buff=1.2)
        self.play(FadeIn(clash, shift=UP*0.1), run_time=0.5)
        x = Text("✗", font="Helvetica", font_size=60, color=CRIMSON)
        x.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(x), run_time=0.3)
        self.wait(max(0.01, d - 9.0))


class B04_ThreeDefinitionsLayout(Scene):
    def construct(self):
        d = dur("B04")
        eyebrow = caps("three fairness definitions", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        defs = [
            ("CALIBRATION", "When model says X%, X% of that group\nactually achieves the outcome.", TEAL),
            ("EQUAL FPR", "Both groups have same rate of\nbeing flagged when not qualified.", INK),
            ("EQUAL FNR", "Both groups have same rate of\nbeing missed when qualified.", CRIMSON),
        ]
        for i, (name, desc, color) in enumerate(defs):
            bg = card(7.5, 1.5, fill=WHITE, stroke=color, sw=2)
            name_lbl = Text(name, font="Montserrat", font_size=32, color=color, weight=BOLD)
            desc_lbl = serif(desc, sz=28, clr=INK)
            row = VGroup(name_lbl, desc_lbl).arrange(RIGHT, buff=0.5)
            row.move_to(bg.get_center())
            box = VGroup(bg, row)
            box.move_to([0, 1.0 - i * 1.7, 0])
            self.play(FadeIn(box, shift=RIGHT*0.1), run_time=0.5)

        note = serif("All three simultaneously: only possible if base rates match.", sz=34, clr=CRIMSON)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 8.0))


class B05_ThresholdSlidingTension(Scene):
    def construct(self):
        d = dur("B05")
        eyebrow = caps("group B lower base rate — threshold tension", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Show two score distributions with a shared threshold
        axes = Axes(x_range=[0, 1, 0.2], y_range=[0, 5, 1], x_length=9, y_length=4,
                    axis_config={"color": INK, "stroke_width": 2})
        axes.move_to([0, -0.3, 0])
        x_lbl = caps("predicted score", sz=18, clr=MUTE).next_to(axes.x_axis, DOWN, buff=0.3)
        self.play(Create(axes), FadeIn(x_lbl), run_time=0.7)

        # Group A: higher base rate, distribution centered around 0.65
        curve_a = axes.plot(lambda x: 4.5 * math.exp(-((x - 0.65)**2) / 0.015),
                             x_range=[0.01, 0.99], color=TEAL, stroke_width=3,
                             use_smoothing=True)
        lbl_a = caps("GROUP A (higher base rate)", sz=18, clr=TEAL).move_to([3.5, 2.5, 0])

        # Group B: lower base rate, distribution centered around 0.40
        curve_b = axes.plot(lambda x: 4.0 * math.exp(-((x - 0.40)**2) / 0.015),
                             x_range=[0.01, 0.99], color=CRIMSON, stroke_width=3,
                             use_smoothing=True)
        lbl_b = caps("GROUP B (lower base rate)", sz=18, clr=CRIMSON).move_to([-3.0, 2.5, 0])

        self.play(Create(curve_a), FadeIn(lbl_a), run_time=0.6)
        self.play(Create(curve_b), FadeIn(lbl_b), run_time=0.6)

        # Shared threshold
        thresh = 0.5
        thresh_line = axes.plot_line_graph(x_values=[thresh, thresh], y_values=[0, 5],
                                            line_color=ACCENT, stroke_width=4)
        thresh_lbl = caps("SINGLE THRESHOLD", sz=18, clr=ACCENT).next_to(axes.c2p(thresh, 4.5), RIGHT, buff=0.1)
        self.play(Create(thresh_line), FadeIn(thresh_lbl), run_time=0.5)

        note = serif("One threshold cannot equalize FPR and FNR simultaneously.", sz=32, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))


class B07_ThresholdDialAnimation(Scene):
    """TERRACOTTA MOMENT"""
    def construct(self):
        d = dur("B07")
        eyebrow = caps("two score distributions — threshold slides", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        axes = Axes(x_range=[0, 1, 0.2], y_range=[0, 5, 1], x_length=9, y_length=4,
                    axis_config={"color": INK, "stroke_width": 2})
        axes.move_to([0, -0.2, 0])
        self.play(Create(axes), run_time=0.5)

        curve_a = axes.plot(lambda x: 4.5 * math.exp(-((x - 0.65)**2) / 0.015),
                             x_range=[0.01, 0.99], color=TEAL, stroke_width=3)
        curve_b = axes.plot(lambda x: 4.0 * math.exp(-((x - 0.40)**2) / 0.015),
                             x_range=[0.01, 0.99], color=CRIMSON, stroke_width=3)
        self.play(Create(curve_a), Create(curve_b), run_time=0.7)

        # Threshold slides — TERRACOTTA accent on the line
        thresh_line = always_redraw(lambda: axes.plot_line_graph(
            x_values=[0.3, 0.3], y_values=[0, 5],
            line_color=ACCENT, stroke_width=5))
        thresh_val = ValueTracker(0.3)

        thresh_line_dyn = axes.plot_line_graph(x_values=[0.3, 0.3], y_values=[0, 5],
                                               line_color=ACCENT, stroke_width=5)
        self.play(Create(thresh_line_dyn), run_time=0.3)

        # Slide threshold from 0.3 to 0.7
        self.play(thresh_line_dyn.animate.move_to([axes.c2p(0.7, 2.5)[0], axes.c2p(0.7, 2.5)[1], 0]),
                  run_time=2.0)

        note = serif("Moving threshold fixes one metric — breaks another.", sz=34, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))


class B08_ImpossibilityTheoremCard(Scene):
    def construct(self):
        d = dur("B08")
        eyebrow = caps("Chouldechova 2017 — the impossibility theorem", sz=24, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Theorem statement card
        bg = card(9.0, 3.5, fill=WHITE, stroke=INK, sw=2)
        bg.move_to([0, 0.3, 0])
        theorem = serif("When two groups have different base rates,\nno classifier can simultaneously satisfy\ncalibration, equal FPR, and equal FNR.", sz=38, clr=INK)
        theorem.move_to(bg.get_center())
        src = caps("— Chouldechova 2017, Fairness Impossibility Theorem", sz=20, clr=MUTE).next_to(bg, DOWN, buff=0.2)

        self.play(FadeIn(bg), run_time=0.4)
        self.play(FadeIn(theorem, shift=UP*0.1), run_time=0.7)
        self.play(FadeIn(src), run_time=0.4)

        note = serif("This is a theorem, not a design flaw.", sz=44, clr=ACCENT)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))


class B09_FairnessCheckboxTrap(Scene):
    def construct(self):
        d = dur("B09")
        eyebrow = caps("fairness is not a checkbox", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        checkboxes = [
            ("☑ Passed accuracy audit", INK),
            ("☑ Passed calibration check", INK),
            ("☐ Satisfied all three fairness defs", CRIMSON),
        ]
        items = []
        for i, (text, color) in enumerate(checkboxes):
            lbl = serif(text, sz=44, clr=color)
            lbl.move_to([0, 1.2 - i * 1.0, 0])
            items.append(lbl)
            self.play(FadeIn(lbl, shift=RIGHT*0.1), run_time=0.5)
            self.wait(0.15)

        note = serif("'Fairness-certified' by a vendor means one definition chosen, two not.", sz=32, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))


class B10_PolicyDecisionHighlight(Scene):
    def construct(self):
        d = dur("B10")
        eyebrow = caps("which definition to optimize — a policy decision", sz=24, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        question = serif("Which group's error matters more here?", sz=48, clr=INK)
        question.move_to([0, 1.5, 0])
        self.play(FadeIn(question, shift=UP*0.1), run_time=0.6)

        options = [
            ("False positive rate", "minimize wrongly penalizing qualified candidates"),
            ("False negative rate", "minimize missing qualified candidates"),
            ("Calibration", "ensure predicted probabilities are honest"),
        ]
        for i, (name, desc) in enumerate(options):
            name_lbl = Text(name, font="Montserrat", font_size=30, color=TEAL, weight=BOLD)
            desc_lbl = serif(desc, sz=28, clr=INK)
            row = VGroup(name_lbl, desc_lbl).arrange(RIGHT, buff=0.4)
            row.move_to([0, 0.3 - i * 0.85, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.4)

        note = serif("This decision belongs to humans — not the algorithm vendor.", sz=34, clr=CRIMSON)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 8.0))


class B11_PriorConversationFramework(Scene):
    def construct(self):
        d = dur("B11")
        eyebrow = caps("fix: prior conversation, not a better algorithm", sz=24, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        steps = [
            "Ask: which group are we most at risk of harming?",
            "Name the harm: false positive vs false negative?",
            "Choose the definition that matches the harm you want to minimize.",
            "Report the trade-offs you accepted — be transparent.",
        ]
        for i, step in enumerate(steps):
            num = serif(f"{i+1}.", sz=40, clr=MUTE)
            txt = serif(step, sz=36, clr=INK)
            row = VGroup(num, txt).arrange(RIGHT, buff=0.3)
            row.move_to([0, 1.4 - i * 0.9, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.4)
            self.wait(0.1)

        note = serif("The choice of fairness definition is a values decision.", sz=34, clr=ACCENT)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))


class B12_PretrialRiskToolExample(Scene):
    def construct(self):
        d = dur("B12")
        eyebrow = caps("pretrial risk tool — two groups, different base rates", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # COMPAS-style split: two groups, same score different FPR
        groups = [
            ("GROUP A", "Base rate: 22%\nFPR: 23%\nFNR: 47%", TEAL),
            ("GROUP B", "Base rate: 45%\nFPR: 44%\nFNR: 29%", CRIMSON),
        ]
        for i, (name, stats, color) in enumerate(groups):
            bg = card(4.5, 2.8, fill=WHITE, stroke=color, sw=2.5)
            name_lbl = Text(name, font="Montserrat", font_size=36, color=color, weight=BOLD)
            stats_lbl = serif(stats, sz=30, clr=INK)
            grp = VGroup(name_lbl, stats_lbl).arrange(DOWN, buff=0.3)
            grp.move_to(bg.get_center())
            box = VGroup(bg, grp)
            box.move_to([(i*2 - 1) * 2.8, 0.3, 0])
            self.play(FadeIn(box, shift=RIGHT*0.1), run_time=0.6)

        note = serif("Same algorithm. Different base rates. Impossible to equalize all three.", sz=30, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))
