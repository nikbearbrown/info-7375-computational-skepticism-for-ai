"""scenes.py — claude-liam-cs-02-confident-and-wrong Manim scenes (STD retrofit)

10 TELLS beats: B01 B02 B04 B05 B07 B08 B09 B10 B11 B12
Topic: Bias — more data makes wrong answer more confident

Render:
  python3 -m manim scenes.py <ClassName> -r 1920,1080 --fps 30 --format mp4
  mv media/videos/scenes/1080p30/<ClassName>.mp4 media/<BXX>.mp4
"""
import json, pathlib
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
        line1 = serif("More data.", sz=70, clr=INK)
        line2 = serif("More confidence.", sz=70, clr=INK)
        line3 = serif("More wrong.", sz=70, clr=CRIMSON)
        g = VGroup(line1, line2, line3).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.4)
        self.play(FadeIn(line3, shift=UP*0.1), run_time=0.5)
        underline = Line(line3.get_left()+DOWN*0.18, line3.get_right()+DOWN*0.18, color=ACCENT, stroke_width=4)
        self.play(GrowFromPoint(underline, underline.get_left()), run_time=0.5)
        self.wait(max(0.01, d - 2.2))


class B02_ScatterTighteningOffCenter(Scene):
    def construct(self):
        d = dur("B02")
        eyebrow = caps("Literary Digest 1936 — 2.4M responses", sz=24, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        axes = Axes(x_range=[0, 12, 2], y_range=[40, 70, 5], x_length=8, y_length=5,
                    axis_config={"color": INK, "stroke_width": 2},
                    x_axis_config={"label_direction": DOWN},
                    y_axis_config={"label_direction": LEFT})
        axes.move_to([0, -0.3, 0])

        x_lbl = caps("million responses", sz=18, clr=MUTE).next_to(axes.x_axis, DOWN, buff=0.3)
        y_lbl = caps("predicted % for Roosevelt", sz=18, clr=MUTE).next_to(axes.y_axis, LEFT, buff=0.2).rotate(PI/2)

        # True value (actual result: FDR won ~61%)
        true_val = axes.plot_line_graph(x_values=[0, 12], y_values=[61, 61],
                                         line_color=TEAL, stroke_width=3)
        true_lbl = caps("ACTUAL RESULT (61%)", sz=16, clr=TEAL).next_to(axes.c2p(10, 61), UP, buff=0.1)

        # Biased estimate that converges to wrong value (~43%)
        wrong_vals = [43 + (i - 6) * 0.3 for i in range(7)]
        wrong_pts_x = [i * 2 for i in range(7)]
        scatter_pts = VGroup()
        for x, y in zip(wrong_pts_x, wrong_vals):
            dot = Dot(axes.c2p(x, y), radius=0.08, color=CRIMSON, fill_opacity=0.8)
            scatter_pts.add(dot)

        wrong_estimate_line = axes.plot_line_graph(x_values=[0, 12], y_values=[43, 43],
                                                    line_color=CRIMSON, stroke_width=2, stroke_opacity=0.6)
        wrong_lbl = caps("MAGAZINE ESTIMATE (43%) — WRONG", sz=16, clr=CRIMSON).next_to(axes.c2p(7, 43), DOWN, buff=0.1)

        self.play(Create(axes), FadeIn(x_lbl), run_time=0.8)
        self.play(Create(true_val), FadeIn(true_lbl), run_time=0.5)
        self.play(FadeIn(scatter_pts), Create(wrong_estimate_line), FadeIn(wrong_lbl), run_time=0.8)

        note = serif("2.4 million responses — and still confident in the wrong answer", sz=34, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.6)
        self.wait(max(0.01, d - 8.0))


class B04_UnbiasedVsBiasedCenter(Scene):
    def construct(self):
        d = dur("B04")
        eyebrow = caps("unbiased vs biased estimator", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Two bullseyes
        def bullseye(center, rings=3, color=INK):
            g = VGroup()
            for i in range(rings, 0, -1):
                c = Circle(radius=i*0.5, color=color, stroke_width=2, fill_opacity=0)
                c.move_to(center)
                g.add(c)
            return g

        left_center = [-3.5, 0.2, 0]
        right_center = [3.5, 0.2, 0]
        left_eye = bullseye(left_center, color=INK)
        right_eye = bullseye(right_center, color=INK)

        left_lbl = caps("UNBIASED", sz=22, clr=TEAL).move_to([-3.5, -1.8, 0])
        right_lbl = caps("BIASED", sz=22, clr=CRIMSON).move_to([3.5, -1.8, 0])
        target = caps("↑ true value", sz=18, clr=INK).move_to([-3.5, 1.7, 0])
        wrong_target = caps("↑ wrong target", sz=18, clr=CRIMSON).move_to([3.5, 0.9, 0])

        import random
        random.seed(42)
        left_dots = VGroup(*[Dot([-3.5 + random.gauss(0, 0.25), 0.2 + random.gauss(0, 0.25), 0],
                                  radius=0.1, color=TEAL) for _ in range(8)])
        right_dots = VGroup(*[Dot([2.8 + random.gauss(0, 0.15), 0.9 + random.gauss(0, 0.15), 0],
                                   radius=0.1, color=CRIMSON) for _ in range(8)])

        self.play(Create(left_eye), Create(right_eye), run_time=0.7)
        self.play(FadeIn(left_lbl), FadeIn(right_lbl), FadeIn(target), FadeIn(wrong_target), run_time=0.5)
        self.play(FadeIn(left_dots), run_time=0.6)
        self.play(FadeIn(right_dots), run_time=0.6)

        note = serif("Unbiased: scattered around truth. Biased: tight cluster at wrong value.", sz=34, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))


class B05_ConvergenceToWrongValue(Scene):
    def construct(self):
        d = dur("B05")
        eyebrow = caps("as you add data — scatter shrinks, bias stays", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        axes = Axes(x_range=[0, 100, 20], y_range=[-2, 2, 1], x_length=8, y_length=4,
                    axis_config={"color": INK, "stroke_width": 2})
        axes.move_to([0, 0, 0])
        x_lbl = caps("data points added", sz=18, clr=MUTE).next_to(axes.x_axis, DOWN, buff=0.3)
        y_lbl = caps("error from truth", sz=18, clr=MUTE).next_to(axes.y_axis, LEFT, buff=0.2).rotate(PI/2)
        self.play(Create(axes), FadeIn(x_lbl), run_time=0.7)

        # Unbiased: scatter shrinks to 0 (converges to truth)
        unbiased_line = axes.plot(lambda x: 1.5 / (1 + x*0.05) * 0.5 if x > 0 else 0,
                                   x_range=[1, 99], color=TEAL, stroke_width=3)
        unbiased_lbl = caps("unbiased — converges to truth", sz=18, clr=TEAL).move_to([3.5, 1.5, 0])

        # Biased: scatter shrinks but converges to WRONG value (e.g. -1.0)
        bias_offset = -1.0
        biased_line = axes.plot(lambda x: bias_offset + (1.5 / (1 + x*0.05) * 0.3 if x > 0 else 0),
                                 x_range=[1, 99], color=CRIMSON, stroke_width=3)
        biased_lbl = caps("biased — converges to WRONG value", sz=18, clr=CRIMSON).move_to([3.5, -0.8, 0])

        self.play(Create(unbiased_line), FadeIn(unbiased_lbl), run_time=0.8)
        self.play(Create(biased_line), FadeIn(biased_lbl), run_time=0.8)

        arrow = Arrow(axes.c2p(90, 0), axes.c2p(90, bias_offset + 0.05),
                      color=ACCENT, stroke_width=3, buff=0.05)
        gap_lbl = caps("bias gap — data can't close this", sz=16, clr=ACCENT).next_to(arrow, RIGHT, buff=0.1)
        self.play(GrowArrow(arrow), FadeIn(gap_lbl), run_time=0.6)
        self.wait(max(0.01, d - 7.0))


class B07_BullseyeAccumulation(Scene):
    def construct(self):
        """TERRACOTTA MOMENT — the key bullseye animation"""
        d = dur("B07")
        eyebrow = caps("the bullseye — bias vs variance", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        center = [0, 0.3, 0]
        # Draw rings
        rings = VGroup()
        for i in [3, 2, 1]:
            c = Circle(radius=i*0.7, color=INK, stroke_width=2.5, fill_opacity=0)
            c.move_to(center)
            rings.add(c)
        # True value ring (teal) at center
        true_ring = Circle(radius=0.15, color=TEAL, stroke_width=4, fill_opacity=0)
        true_ring.move_to(center)
        true_lbl = caps("TRUE VALUE", sz=18, clr=TEAL).next_to(true_ring, UP*4, buff=0.1).move_to([0, 2.1, 0])

        self.play(Create(rings), Create(true_ring), FadeIn(true_lbl), run_time=0.8)

        import random
        random.seed(7)

        # Stage 1: small data — unbiased, big scatter near truth
        dots_small = VGroup(*[Dot([random.gauss(0, 0.6), 0.3 + random.gauss(0, 0.6), 0],
                                   radius=0.1, color=TEAL, fill_opacity=0.7) for _ in range(5)])
        stage_lbl = caps("small sample — scattered around truth", sz=20, clr=TEAL).to_corner(DL, buff=0.4)
        self.play(FadeIn(dots_small), FadeIn(stage_lbl), run_time=0.7)
        self.wait(0.5)

        # Stage 2: more data — biased, scatter tightens at WRONG spot
        wrong_center = [1.8, -1.0, 0]
        dots_large = VGroup(*[Dot([1.8 + random.gauss(0, 0.2), -1.0 + random.gauss(0, 0.2), 0],
                                   radius=0.1, color=CRIMSON, fill_opacity=0.8) for _ in range(10)])
        # TERRACOTTA moment: accent ring on the wrong cluster
        wrong_ring = Circle(radius=0.6, color=ACCENT, stroke_width=4, fill_opacity=0)
        wrong_ring.move_to(wrong_center)
        wrong_lbl = caps("more data — tight cluster\nat WRONG target", sz=20, clr=CRIMSON).next_to(wrong_ring, RIGHT, buff=0.2)

        self.remove(stage_lbl)
        self.play(FadeIn(dots_large), Create(wrong_ring), FadeIn(wrong_lbl), run_time=0.8)

        note = serif("Data volume kills variance. Bias stays.", sz=38, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 8.5))


class B08_BiasVarianceNaming(Scene):
    def construct(self):
        d = dur("B08")
        eyebrow = caps("bias and variance — the two error types", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        items = [
            ("BIAS", "Expected distance from true value", INK),
            ("VARIANCE", "Scatter around the estimate", INK),
        ]
        rows = []
        for i, (term, defn, clr) in enumerate(items):
            term_lbl = Text(term, font="Montserrat", font_size=44, color=TEAL if i==0 else CRIMSON, weight=BOLD)
            defn_lbl = serif(defn, sz=36, clr=clr)
            row = VGroup(term_lbl, defn_lbl).arrange(RIGHT, buff=0.5)
            row.move_to([0, 1.0 - i * 1.2, 0])
            rows.append(row)
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.7)
            self.wait(0.2)

        separator = Line([-7, -0.3, 0], [7, -0.3, 0], color=MUTE, stroke_width=1, stroke_opacity=0.5)
        self.play(Create(separator), run_time=0.4)

        key_line = serif("More data ↓ variance. It cannot ↓ bias.", sz=44, clr=INK)
        key_line.move_to([0, -1.2, 0])
        self.play(FadeIn(key_line, shift=UP*0.1), run_time=0.6)
        self.wait(max(0.01, d - 6.5))


class B09_TrainingDataBiasTrap(Scene):
    def construct(self):
        d = dur("B09")
        eyebrow = caps("AI trained on biased data — the trap", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Pipeline: biased data → model → biased predictions
        nodes = ["BIASED\nTRAINING DATA", "AI MODEL", "BIASED\nPREDICTIONS"]
        colors = [CRIMSON, MUTE, CRIMSON]
        boxes = []
        for i, (text, color) in enumerate(zip(nodes, colors)):
            bg = card(2.5, 1.4, fill=WHITE, stroke=color, sw=2.5)
            lbl = Text(text, font="Montserrat", font_size=28, color=color, weight=BOLD)
            lbl.move_to(bg.get_center())
            grp = VGroup(bg, lbl)
            grp.move_to([(i - 1) * 4.0, 0.5, 0])
            boxes.append(grp)
            self.play(FadeIn(grp, shift=RIGHT*0.1), run_time=0.5)
            if i < 2:
                arr = Arrow(grp.get_right(), boxes[i-1].get_left() if i > 0 else grp.get_right() + RIGHT*0.5,
                             color=INK, stroke_width=3, buff=0.1)
                if i == 0:
                    arr = Arrow(grp.get_right() + RIGHT*0.1, [grp.get_right()[0] + 1.4, 0.5, 0], color=INK, buff=0.1)
                else:
                    arr = Arrow(boxes[0].get_right(), boxes[1].get_left(), color=INK, buff=0.1)
                self.add(arr)

        arr2 = Arrow(boxes[1].get_right(), boxes[2].get_left(), color=INK, stroke_width=3, buff=0.1)
        self.add(arr2)

        trap = serif("More data → more confidence → still wrong direction", sz=34, clr=INK)
        trap.move_to([0, -1.2, 0])
        self.play(FadeIn(trap, shift=UP*0.1), run_time=0.6)

        note = serif("You cannot data-volume your way out of a structural bias.", sz=34, clr=CRIMSON)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.6)
        self.wait(max(0.01, d - 9.0))


class B10_DataProvenanceQuestion(Scene):
    def construct(self):
        d = dur("B10")
        eyebrow = caps("the provenance question — ask before trusting data volume", sz=24, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        questions = [
            "Who generated this data, and how?",
            "What mechanism could bias collection?",
            "Where might the source systematically misrepresent?",
        ]
        rows = []
        for i, q in enumerate(questions):
            num = serif(f"{i+1}.", sz=44, clr=MUTE)
            txt = serif(q, sz=38, clr=INK)
            row = VGroup(num, txt).arrange(RIGHT, buff=0.3)
            row.move_to([0, 1.2 - i * 1.0, 0])
            rows.append(row)
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.5)
            self.wait(0.15)

        note = serif("High n with structural bias → high-confidence wrong answer.", sz=34, clr=CRIMSON)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))


class B11_PrecisionVsAccuracyCheck(Scene):
    def construct(self):
        d = dur("B11")
        eyebrow = caps("the practical test — check for structural bias", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Confidence interval check
        ci_lbl = caps("LOOK FOR:", sz=24, clr=INK).move_to([-5.0, 1.5, 0])
        ci_desc = serif("Confidence interval that narrows with more data", sz=36, clr=INK).move_to([0.5, 1.5, 0])
        self.play(FadeIn(ci_lbl), FadeIn(ci_desc, shift=RIGHT*0.1), run_time=0.6)

        # If CI is narrow but pointing away from truth → biased
        warning_lbl = caps("WARNING SIGN:", sz=24, clr=CRIMSON).move_to([-4.5, 0.2, 0])
        warning_desc = serif("Narrow CI but estimate consistently away from known truth", sz=34, clr=CRIMSON)
        warning_desc.move_to([0.5, 0.2, 0])
        self.play(FadeIn(warning_lbl), FadeIn(warning_desc, shift=RIGHT*0.1), run_time=0.6)

        separator = Line([-7, -0.5, 0], [7, -0.5, 0], color=MUTE, stroke_width=1, stroke_opacity=0.5)
        self.play(Create(separator), run_time=0.3)

        fix = serif("Ask: does more data make the estimate move toward\nor away from external benchmarks?", sz=34, clr=INK)
        fix.move_to([0, -1.3, 0])
        self.play(FadeIn(fix, shift=UP*0.1), run_time=0.6)
        self.wait(max(0.01, d - 7.5))


class B12_BankLendingBiasExample(Scene):
    def construct(self):
        d = dur("B12")
        eyebrow = caps("bank loan model — 10 years of biased historical data", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)

        # Timeline: data grows, bias stays
        axes = Axes(x_range=[0, 10, 2], y_range=[0, 1.1, 0.25], x_length=8, y_length=4,
                    axis_config={"color": INK, "stroke_width": 2})
        axes.move_to([0, -0.2, 0])
        x_lbl = caps("years of training data", sz=18, clr=MUTE).next_to(axes.x_axis, DOWN, buff=0.3)
        y_lbl = caps("denial rate for minority applicants", sz=16, clr=MUTE).next_to(axes.y_axis, LEFT, buff=0.2).rotate(PI/2)
        self.play(Create(axes), FadeIn(x_lbl), run_time=0.7)

        # Actual denial rate (truth): ~30%
        true_line = axes.plot_line_graph(x_values=[0, 10], y_values=[0.3, 0.3],
                                          line_color=TEAL, stroke_width=3)
        true_lbl = caps("ACTUAL BASE RATE (30%)", sz=16, clr=TEAL).move_to([3.5, axes.c2p(0, 0.3)[1] + 0.3, 0])
        self.play(Create(true_line), FadeIn(true_lbl), run_time=0.5)

        # Model's prediction: starts high, tightens at 60% (biased)
        model_line = axes.plot(lambda x: 0.6 + 0.05 * (1 - x/10),
                                x_range=[0.1, 10], color=CRIMSON, stroke_width=3)
        model_lbl = caps("MODEL DENIAL RATE — BIASED AT 60%", sz=16, clr=CRIMSON).move_to([3.5, axes.c2p(0, 0.6)[1] + 0.3, 0])
        self.play(Create(model_line), FadeIn(model_lbl), run_time=0.7)

        note = serif("More historical data → more confident at the wrong rate.", sz=34, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.5))
