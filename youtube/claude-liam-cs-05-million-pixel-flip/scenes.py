"""scenes.py — claude-liam-cs-05-million-pixel-flip (STD retrofit)
Topic: Adversarial perturbations — invisible pixel nudges flip model outputs
"""
import json, pathlib, math
from manim import *

_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)

CREAM="#F2F0E9"; INK="#3D3929"; ACCENT="#D97757"; MUTE="#7A7265"; TEAL="#2A9D8F"; CRIMSON="#C1121F"
config.background_color = CREAM

DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _bs["beats"]})
except Exception: pass

def dur(bid): return DUR.get(bid, 8.0)
def serif(t, sz=40, clr=INK, **k): return Text(t, font="EB Garamond", font_size=sz, color=clr, **k)
def caps(t, sz=24, clr=MUTE, **k): return Text(t.upper(), font="Montserrat", font_size=sz, color=clr, weight=BOLD, **k)
def card(w, h, fill=WHITE, stroke=INK, sw=2): return RoundedRectangle(corner_radius=0.12, width=w, height=h, fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)

class B01_Title(Scene):
    def construct(self):
        d = dur("B01")
        l1 = serif("You can't see what changed.", sz=60, clr=INK)
        l2 = serif("The model saw it everywhere.", sz=60, clr=CRIMSON)
        l3 = serif("And flipped.", sz=60, clr=CRIMSON)
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        for l in [l1, l2, l3]: self.play(FadeIn(l, shift=UP*0.1), run_time=0.5)
        u = Line(l2.get_left()+DOWN*0.18, l2.get_right()+DOWN*0.18, color=ACCENT, stroke_width=4)
        self.play(GrowFromPoint(u, u.get_left()), run_time=0.5)
        self.wait(max(0.01, d - 2.8))

class B02_PandaGibbonParadox(Scene):
    def construct(self):
        d = dur("B02")
        eyebrow = caps("panda → gibbon: invisible perturbation flips answer", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        # Three columns: original, perturbation, result
        cols = [
            ("ORIGINAL\nIMAGE", "PANDA\n57.7% confidence", TEAL),
            ("+ ε perturbation\n(invisible to eye)", "± 0.007 per pixel", MUTE),
            ("MODEL OUTPUT\nFLIPS", "GIBBON\n99.3% confidence", CRIMSON),
        ]
        for i, (title, result, color) in enumerate(cols):
            bg = card(3.8, 3.5, fill=WHITE, stroke=color, sw=2.5).move_to([(i-1)*4.2, 0.2, 0])
            title_lbl = Text(title, font="Montserrat", font_size=26, color=color, weight=BOLD)
            result_lbl = serif(result, sz=28, clr=INK)
            grp = VGroup(title_lbl, result_lbl).arrange(DOWN, buff=0.4).move_to(bg.get_center())
            self.play(FadeIn(VGroup(bg, grp), shift=RIGHT*0.1), run_time=0.5)
            if i < 2:
                arr = Arrow([(i-1)*4.2 + 2.0, 0.2, 0], [(i)*4.2 - 2.0, 0.2, 0], color=INK, stroke_width=3, buff=0.1)
                self.add(arr)
        note = serif("Goodfellow et al. 2014 — no human can see the change.", sz=34, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))

class B04_DimensionalityAccumulation(Scene):
    def construct(self):
        d = dur("B04")
        eyebrow = caps("high dimensionality — small nudges accumulate", sz=24, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        # Equation: total = ε × D
        eq1 = serif("Typical image: 300 × 300 × 3 = 270,000 dimensions", sz=36, clr=INK).move_to([0, 1.5, 0])
        eq2 = serif("Per-pixel nudge ε = 0.007 (invisible)", sz=36, clr=INK).move_to([0, 0.7, 0])
        eq3 = serif("Total perturbation = ε × D", sz=40, clr=INK).move_to([0, -0.2, 0])
        eq4 = serif("= 0.007 × 270,000 = 1,890 units", sz=44, clr=CRIMSON).move_to([0, -1.2, 0])
        for eq in [eq1, eq2, eq3, eq4]:
            self.play(FadeIn(eq, shift=RIGHT*0.1), run_time=0.5)
            self.wait(0.2)
        note = serif("Each nudge invisible. Combined: a large directed force.", sz=34, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))

class B05_EpsilonAccumulationMath(Scene):
    def construct(self):
        d = dur("B05")
        eyebrow = caps("epsilon accumulates across 270,000 dimensions", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        axes = Axes(x_range=[0, 10, 2], y_range=[0, 2000, 500], x_length=8, y_length=4,
                    axis_config={"color": INK, "stroke_width": 2})
        axes.move_to([0, -0.2, 0])
        x_lbl = caps("pixels processed (×10,000)", sz=18, clr=MUTE).next_to(axes.x_axis, DOWN, buff=0.3)
        y_lbl = caps("accumulated perturbation", sz=16, clr=MUTE).next_to(axes.y_axis, LEFT, buff=0.2).rotate(PI/2)
        self.play(Create(axes), FadeIn(x_lbl), run_time=0.7)
        line = axes.plot(lambda x: 189 * x, x_range=[0, 9.9], color=CRIMSON, stroke_width=4)
        self.play(Create(line), run_time=1.5)
        threshold_line = axes.plot_line_graph(x_values=[0, 10], y_values=[900, 900],
                                               line_color=ACCENT, stroke_width=3, stroke_opacity=0.8)
        threshold_lbl = caps("MODEL FLIP THRESHOLD", sz=16, clr=ACCENT).next_to(axes.c2p(7, 900), UP, buff=0.1)
        self.play(Create(threshold_line), FadeIn(threshold_lbl), run_time=0.5)
        note = serif("Passes flip threshold around 47,000 pixels — well before all 270K.", sz=30, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))

class B07_PixelGridActivationBar(Scene):
    """TERRACOTTA MOMENT"""
    def construct(self):
        d = dur("B07")
        eyebrow = caps("pixel grid — each square nudged in gradient direction", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        # Grid of small squares, start neutral, turn crimson as ε applied
        rows, cols = 8, 14
        sq_size = 0.42
        spacing = 0.48
        squares = []
        grid_group = VGroup()
        for r in range(rows):
            for c in range(cols):
                x = (c - cols/2 + 0.5) * spacing
                y = (rows/2 - r - 0.5) * spacing
                sq = Square(side_length=sq_size, fill_color=MUTE, fill_opacity=0.4, stroke_width=0.5, stroke_color=INK)
                sq.move_to([x, y, 0])
                squares.append(sq)
                grid_group.add(sq)
        self.play(FadeIn(grid_group), run_time=0.5)

        # Bar growing to show accumulation — TERRACOTTA
        bar_bg = card(0.6, 4.0, fill=WHITE, stroke=INK, sw=2).move_to([5.5, 0, 0])
        bar_lbl = caps("ACCUMULATED ε", sz=16, clr=MUTE).next_to(bar_bg, RIGHT, buff=0.1)
        self.play(FadeIn(bar_bg), FadeIn(bar_lbl), run_time=0.3)

        # Animate squares turning crimson + bar growing
        bar_fill = Rectangle(width=0.4, height=0.01, fill_color=ACCENT, fill_opacity=1.0, stroke_width=0)
        bar_fill.align_to(bar_bg, DOWN).shift(UP*0.07).move_to([5.5, bar_bg.get_bottom()[1]+0.07, 0])
        self.add(bar_fill)
        for i in range(0, len(squares), 8):
            grp = squares[i:i+8]
            for sq in grp:
                sq.set_fill(CRIMSON, opacity=0.7)
            new_h = min(3.86, (i+8) / len(squares) * 3.86)
            new_bar = Rectangle(width=0.4, height=new_h, fill_color=ACCENT, fill_opacity=1.0, stroke_width=0)
            new_bar.align_to(bar_bg, DOWN).shift(UP*0.07)
            self.play(Transform(bar_fill, new_bar), run_time=0.12)

        flip_lbl = caps("→ MODEL FLIPS: GIBBON", sz=22, clr=CRIMSON).move_to([5.5, bar_bg.get_top()[1]+0.4, 0])
        self.play(FadeIn(flip_lbl), run_time=0.3)
        note = serif("Invisible per pixel. Decisive in aggregate.", sz=36, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(max(0.01, d - 9.0))

class B08_GradientDirectionMechanism(Scene):
    def construct(self):
        d = dur("B08")
        eyebrow = caps("gradient direction — nudge toward maximum wrong class", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        l1 = serif("Take gradient of the model's loss w.r.t. input pixels", sz=36, clr=INK).move_to([0, 1.5, 0])
        l2 = serif("Each gradient tells: 'push THIS pixel in THIS direction'", sz=36, clr=INK).move_to([0, 0.7, 0])
        l3 = serif("Direction maximizes loss on the correct class", sz=36, clr=INK).move_to([0, -0.1, 0])
        l4 = serif("= minimizes P(correct) + maximizes P(wrong)", sz=40, clr=CRIMSON).move_to([0, -1.0, 0])
        for l in [l1, l2, l3, l4]: self.play(FadeIn(l, shift=RIGHT*0.1), run_time=0.4)
        note = serif("Not random noise — targeted, directed, adversarial.", sz=34, clr=ACCENT)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(max(0.01, d - 7.0))

class B09_AdversarialEnvironmentImplication(Scene):
    def construct(self):
        d = dur("B09")
        eyebrow = caps("adversarial environments — content moderation, autonomous vehicles", sz=20, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        domains = [
            ("Content moderation", "Adversaries craft images that evade filters", CRIMSON),
            ("Autonomous vehicles", "Stop signs with stickers read as speed limits", CRIMSON),
            ("Fraud detection", "Transaction patterns crafted to score below threshold", CRIMSON),
            ("Medical imaging", "Scans altered to flip diagnosis", CRIMSON),
        ]
        for i, (domain, risk, color) in enumerate(domains):
            dom_lbl = Text(domain, font="Montserrat", font_size=30, color=INK, weight=BOLD)
            risk_lbl = serif(risk, sz=28, clr=color)
            row = VGroup(dom_lbl, risk_lbl).arrange(RIGHT, buff=0.5)
            row.move_to([0, 1.5 - i*0.9, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.35)
        note = serif("Any adversarial environment: perturbation testing is mandatory.", sz=32, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))

class B10_UnderstandingVsStatisticalSurface(Scene):
    def construct(self):
        d = dur("B10")
        eyebrow = caps("what 'understanding' means for a neural network", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        l1 = serif("Human: recognizes panda by shape, color, context", sz=38, clr=TEAL).move_to([0, 1.5, 0])
        l2 = serif("Neural network: responds to statistical texture features", sz=38, clr=CRIMSON).move_to([0, 0.5, 0])
        l3 = serif("The texture features happen to cooccur with 'panda'", sz=36, clr=INK).move_to([0, -0.5, 0])
        l4 = serif("Perturb the texture → lose the 'panda' signal", sz=38, clr=CRIMSON).move_to([0, -1.4, 0])
        for l in [l1, l2, l3, l4]: self.play(FadeIn(l, shift=RIGHT*0.1), run_time=0.45)
        note = serif("Accuracy on training data ≠ understanding of semantics.", sz=34, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(max(0.01, d - 8.0))

class B11_PerturbationTestingRequirement(Scene):
    def construct(self):
        d = dur("B11")
        eyebrow = caps("before deploying in adversarial environments", sz=24, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        steps = [
            "Run FGSM (Fast Gradient Sign Method) attacks on your test set",
            "Check: what fraction of predictions flip under ε-perturbation?",
            "Test multiple ε values — the smallest ε that causes flips",
            "If > 5% flip at invisible ε: deployment risk in adversarial contexts",
        ]
        for i, step in enumerate(steps):
            num = serif(f"{i+1}.", sz=40, clr=MUTE)
            txt = serif(step, sz=34, clr=INK)
            row = VGroup(num, txt).arrange(RIGHT, buff=0.3)
            row.move_to([0, 1.3 - i*0.85, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.4)
        note = serif("Robustness to perturbation is a separate axis from accuracy.", sz=32, clr=ACCENT)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(max(0.01, d - 8.0))

class B12_BankCheckFraudExample(Scene):
    def construct(self):
        d = dur("B12")
        eyebrow = caps("bank check fraud model — adversarial handwriting", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        timeline = [
            ("Deploy check-fraud vision model", "98% accuracy on validation set", TEAL),
            ("Attacker modifies check signature", "Adds invisible ink pattern (ε-perturbation)", CRIMSON),
            ("Model misclassifies", "'Authentic' at 96.4% confidence", CRIMSON),
            ("Fraud proceeds", "Bank processes fraudulent check", CRIMSON),
        ]
        for i, (event, detail, color) in enumerate(timeline):
            bg = card(8.5, 0.95, fill=WHITE, stroke=color, sw=1.5).move_to([0, 1.5 - i*1.1, 0])
            ev_lbl = Text(event, font="Montserrat", font_size=26, color=color, weight=BOLD)
            det_lbl = serif(detail, sz=24, clr=INK)
            row = VGroup(ev_lbl, det_lbl).arrange(RIGHT, buff=0.5).move_to(bg.get_center())
            self.play(FadeIn(VGroup(bg, row), shift=RIGHT*0.1), run_time=0.4)
        note = serif("A 98%-accurate model with 0% perturbation robustness testing.", sz=30, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(max(0.01, d - 8.0))
