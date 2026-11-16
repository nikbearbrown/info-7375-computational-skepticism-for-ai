"""scenes.py — claude-liam-cs-04-clean-but-broken (STD retrofit)
Topic: Silent join drops — EDA passes on amputated data
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
        l1 = serif("The EDA ran clean.", sz=60, clr=INK)
        l2 = serif("The model still failed.", sz=60, clr=CRIMSON)
        l3 = serif("The broken rows were never there to check.", sz=44, clr=INK)
        VGroup(l1, l2, l3).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        for l in [l1, l2, l3]: self.play(FadeIn(l, shift=UP*0.1), run_time=0.5)
        u = Line(l2.get_left()+DOWN*0.18, l2.get_right()+DOWN*0.18, color=ACCENT, stroke_width=4)
        self.play(GrowFromPoint(u, u.get_left()), run_time=0.5)
        self.wait(max(0.01, d - 2.8))

class B02_SilentDropParadox(Scene):
    def construct(self):
        d = dur("B02")
        eyebrow = caps("EDA ran clean — but checked the WRONG data", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        # Two panels: full dataset vs surviving data
        for i, (lbl, color, rows) in enumerate([("FULL DATASET\n(before join)", TEAL, 14), ("SURVIVING DATA\n(after join)", CRIMSON, 9)]):
            x = (i*2 - 1) * 3.2
            bg = card(4.0, 5.0, fill=WHITE, stroke=color, sw=2.5).move_to([x, -0.2, 0])
            title = Text(lbl, font="Montserrat", font_size=24, color=color, weight=BOLD).next_to(bg, UP, buff=0.15)
            self.play(FadeIn(bg), FadeIn(title), run_time=0.4)
            for r in range(rows):
                c = CRIMSON if (i==0 and r >= 9) else color
                bar = Rectangle(width=3.4, height=0.23, fill_color=c, fill_opacity=0.7, stroke_width=0)
                bar.move_to([x, 1.8 - r*0.35, 0])
                self.add(bar)
        dropped = caps("5 rows silently dropped by join — EDA never sees them", sz=20, clr=CRIMSON).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(dropped, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 8.0))

class B04_JoinFunnelDrop(Scene):
    def construct(self):
        d = dur("B04")
        eyebrow = caps("three-table join — rows fall through", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        tables = ["CUSTOMERS\n(10,000 rows)", "TRANSACTIONS\n(9,800 rows)", "REGISTRATIONS\n(9,650 rows)"]
        boxes = []
        for i, t in enumerate(tables):
            bg = card(3.2, 1.6, fill=WHITE, stroke=TEAL, sw=2).move_to([(i - 1)*4.2, 2.0, 0])
            lbl = Text(t, font="Montserrat", font_size=24, color=INK, weight=BOLD).move_to(bg.get_center())
            boxes.append(VGroup(bg, lbl))
            self.play(FadeIn(boxes[-1]), run_time=0.4)
        # Arrows pointing down into join
        for b in boxes:
            arr = Arrow(b.get_bottom(), b.get_bottom()+DOWN*0.8, color=INK, stroke_width=2.5, buff=0.05)
            self.add(arr)
        join_box = card(4.0, 1.2, fill=WHITE, stroke=MUTE, sw=2).move_to([0, -0.3, 0])
        join_lbl = Text("JOIN", font="Montserrat", font_size=32, color=MUTE, weight=BOLD).move_to(join_box.get_center())
        self.play(FadeIn(join_box), FadeIn(join_lbl), run_time=0.4)
        result = card(4.5, 1.2, fill=WHITE, stroke=CRIMSON, sw=2.5).move_to([0, -2.2, 0])
        result_lbl = Text("SURVIVING: 8,900 rows", font="Montserrat", font_size=28, color=CRIMSON, weight=BOLD).move_to(result.get_center())
        arr_out = Arrow([0, -1.0, 0], [0, -1.7, 0], color=CRIMSON, stroke_width=3, buff=0.05)
        self.play(GrowArrow(arr_out), FadeIn(result), FadeIn(result_lbl), run_time=0.5)
        drop_note = caps("1,100 rows dropped — encoding mismatch in join key", sz=20, clr=CRIMSON).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(drop_note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))

class B05_EDAPassesOnAmputatedData(Scene):
    def construct(self):
        d = dur("B05")
        eyebrow = caps("EDA on surviving data — all checks pass", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        checks = [
            ("Null check", "PASS", TEAL),
            ("Duplicate check", "PASS", TEAL),
            ("Column distribution", "PASS", TEAL),
            ("Outlier detection", "PASS", TEAL),
            ("Schema validation", "PASS", TEAL),
        ]
        for i, (name, result, color) in enumerate(checks):
            name_lbl = serif(name, sz=36, clr=INK)
            result_lbl = Text(result, font="Montserrat", font_size=36, color=color, weight=BOLD)
            row = VGroup(name_lbl, result_lbl).arrange(RIGHT, buff=3.0)
            row.move_to([0, 1.5 - i*0.8, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.25)
        note = serif("All clean — because the broken rows aren't in the dataset.", sz=34, clr=CRIMSON)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))

class B07_JoinFunnelAnimation(Scene):
    """TERRACOTTA MOMENT"""
    def construct(self):
        d = dur("B07")
        eyebrow = caps("three tables flow into join — crimson rows drop out", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        # Animate rows flowing through join, crimson ones falling out
        n_rows = 10
        rows = []
        drop_indices = [2, 5, 8]
        for i in range(n_rows):
            color = CRIMSON if i in drop_indices else MUTE
            bar = Rectangle(width=5.0, height=0.25, fill_color=color, fill_opacity=0.8, stroke_width=0)
            bar.move_to([0, 3.5 - i*0.4, 0])
            rows.append(bar)
            self.play(FadeIn(bar, shift=DOWN*0.2), run_time=0.12)

        # Join filter
        filter_line = Line([-4, 0.8, 0], [4, 0.8, 0], color=ACCENT, stroke_width=5)
        filter_lbl = caps("JOIN FILTER", sz=22, clr=ACCENT).next_to(filter_line, RIGHT, buff=0.2)
        self.play(GrowFromPoint(filter_line, filter_line.get_left()), FadeIn(filter_lbl), run_time=0.5)

        # Crimson rows fall out the side
        for idx in drop_indices:
            self.play(rows[idx].animate.move_to([7.0, rows[idx].get_center()[1], 0]).set_opacity(0),
                      run_time=0.4)

        note = serif("Dropped rows vanish silently — no warning in the log.", sz=34, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 8.0))

class B08_SystematicDropConcentration(Scene):
    def construct(self):
        d = dur("B08")
        eyebrow = caps("systematic drop — concentrated in one subpopulation", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        # Bar chart: subpopulation A vs B, showing drop rate
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 1, 0.2], x_length=7, y_length=4,
                    axis_config={"color": INK, "stroke_width": 2})
        axes.move_to([0, -0.2, 0])
        self.play(Create(axes), run_time=0.5)
        bars = [
            (0.8, 0.05, TEAL, "SUBPOP A\n2% dropped"),
            (2.0, 0.55, CRIMSON, "SUBPOP B\n55% dropped"),
        ]
        for x, h, color, lbl in bars:
            bar = axes.get_riemann_rectangles(axes.plot(lambda t: h, x_range=[x-0.25, x+0.25]),
                                               x_range=[x-0.25, x+0.25], dx=0.5,
                                               color=color, fill_opacity=0.85, stroke_width=0)
            lbl_txt = caps(lbl, sz=18, clr=color).next_to(axes.c2p(x, h), UP, buff=0.2)
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl_txt), run_time=0.7)
        note = serif("The encoding inconsistency is systematic — not random.", sz=34, clr=INK)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 8.0))

class B09_PreJoinRowCountCheck(Scene):
    def construct(self):
        d = dur("B09")
        eyebrow = caps("standard checks are post-join — wrong place", sz=24, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        timeline = [
            ("Table A: 10,000 rows", INK),
            ("Table B: 9,800 rows", INK),
            ("JOIN ← standard EDA starts here", MUTE),
            ("Surviving: 8,900 rows — EDA runs here", TEAL),
            ("Missing: 1,100 rows — never checked", CRIMSON),
        ]
        for i, (text, color) in enumerate(timeline):
            lbl = serif(text, sz=36, clr=color)
            lbl.move_to([0, 1.8 - i*0.9, 0])
            self.play(FadeIn(lbl, shift=RIGHT*0.1), run_time=0.3)
        note = serif("The check you need is PRE-join row count reconciliation.", sz=34, clr=ACCENT)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))

class B10_ProductionExtrapolationFail(Scene):
    def construct(self):
        d = dur("B10")
        eyebrow = caps("training gap → production failure", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        l1 = serif("Training data: subpop B largely absent (55% dropped)", sz=36, clr=CRIMSON)
        l2 = serif("Model learns subpop B features poorly", sz=36, clr=CRIMSON)
        l3 = serif("Production: subpop B is 40% of real users", sz=36, clr=INK)
        l4 = serif("→ Model fails on 40% of production cases", sz=44, clr=CRIMSON)
        for i, l in enumerate([l1, l2, l3, l4]):
            l.move_to([0, 1.5 - i*1.0, 0])
            self.play(FadeIn(l, shift=RIGHT*0.1), run_time=0.4)
        self.wait(max(0.01, d - 6.0))

class B11_PipelineLineageAudit(Scene):
    def construct(self):
        d = dur("B11")
        eyebrow = caps("pipeline lineage trace — the audit that catches it", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        steps = [
            "Log row count at every pipeline step",
            "Compare: rows_in vs rows_out per join",
            "If rows_out < rows_in: investigate before training",
            "Stratify the drop by subpopulation",
        ]
        for i, step in enumerate(steps):
            num = serif(f"{i+1}.", sz=40, clr=MUTE)
            txt = serif(step, sz=36, clr=INK)
            row = VGroup(num, txt).arrange(RIGHT, buff=0.3)
            row.move_to([0, 1.3 - i*0.85, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.4)
        note = serif("EDA checks properties of surviving data — not what's missing.", sz=32, clr=CRIMSON)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))

class B12_HospitalReadmissionExample(Scene):
    def construct(self):
        d = dur("B12")
        eyebrow = caps("hospital readmission model — silent join drop", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        # Timeline: data sources → join → model → failure
        nodes = ["EHR Records\n(50K patients)", "Billing Data\n(48K records)", "JOIN\n(44K matched)", "Model trained\non 44K", "Failed on\n6K gap patients"]
        colors = [TEAL, TEAL, MUTE, INK, CRIMSON]
        boxes = []
        for i, (text, color) in enumerate(zip(nodes, colors)):
            bg = card(2.8, 1.4, fill=WHITE, stroke=color, sw=2).move_to([(i-2)*3.2, 0.5, 0])
            lbl = Text(text, font="Montserrat", font_size=22, color=color, weight=BOLD).move_to(bg.get_center())
            boxes.append(VGroup(bg, lbl))
            self.play(FadeIn(boxes[-1]), run_time=0.3)
            if i > 0:
                arr = Arrow(boxes[i-1].get_right(), boxes[i].get_left(), color=INK, stroke_width=2.5, buff=0.05)
                self.add(arr)
        note = serif("6,000 patients with complex coding were silently excluded.", sz=32, clr=CRIMSON)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))
