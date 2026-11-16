"""scenes.py — claude-liam-cs-27-five-culprits (STD retrofit)
Topic: Distributed accountability — five culprits and no culprit
Render: python3 -m manim scenes.py <ClassName> -r 1920,1080 --fps 30 --format mp4
  mv media/videos/scenes/1080p30/<ClassName>.mp4 media/<BXX>.mp4
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
        lines = ['Five parties.', 'Zero culprit.']
        b01_clr = CRIMSON
        rendered = []
        for i, l in enumerate(lines):
            color = b01_clr if i == len(lines)-1 else INK
            lbl = serif(l, sz=55 if len(lines) <= 2 else 48, clr=color)
            rendered.append(lbl)
        VGroup(*rendered).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        for l in rendered:
            self.play(FadeIn(l, shift=UP*0.1), run_time=0.5)
        if b01_clr != INK:
            last = rendered[-1]
            u = Line(last.get_left()+DOWN*0.18, last.get_right()+DOWN*0.18, color=ACCENT, stroke_width=4)
            self.play(GrowFromPoint(u, u.get_left()), run_time=0.5)
        self.wait(max(0.01, d - len(lines)*0.5 - 1.0))


class B02_HookScene(Scene):
    def construct(self):
        d = dur("B02")
        eyebrow = caps("the opening case", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        for i, (title, content, color) in enumerate([
            ("EXPECTED", "System behaves as documented", TEAL),
            ("ACTUAL", "Hidden failure emerges in production", CRIMSON),
        ]):
            bg = card(4.5, 3.0, fill=WHITE, stroke=color, sw=2.5).move_to([(i*2-1)*2.8, 0, 0])
            t_lbl = Text(title, font="Montserrat", font_size=30, color=color, weight=BOLD)
            c_lbl = serif(content, sz=30, clr=INK)
            grp = VGroup(t_lbl, c_lbl).arrange(DOWN, buff=0.4).move_to(bg.get_center())
            self.play(FadeIn(VGroup(bg, grp), shift=RIGHT*0.1), run_time=0.5)
        note = serif("The mechanism that causes the gap is the subject.", sz=34, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))


class B04_MechanismExplanation(Scene):
    def construct(self):
        d = dur("B04")
        eyebrow = caps("the mechanism", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        items = [
            "The structural property that causes failure",
            "Why adding more data or patching does not fix it",
            "The mathematical or logical basis for the failure",
        ]
        for i, item in enumerate(items):
            num = serif(f"{i+1}.", sz=44, clr=MUTE)
            txt = serif(item, sz=36, clr=INK)
            row = VGroup(num, txt).arrange(RIGHT, buff=0.3).move_to([0, 1.2 - i*0.95, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.45)
        note = serif("Understanding the mechanism is the prerequisite to the fix.", sz=34, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))


class B05_MechanismDeepening(Scene):
    def construct(self):
        d = dur("B05")
        eyebrow = caps("the deeper structure", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        intuition = card(4.5, 2.0, fill=WHITE, stroke=MUTE, sw=2).move_to([-3.0, 0.5, 0])
        reality = card(4.5, 2.0, fill=WHITE, stroke=CRIMSON, sw=2.5).move_to([3.0, 0.5, 0])
        i_lbl = Text("INTUITION", font="Montserrat", font_size=26, color=MUTE, weight=BOLD).next_to(intuition, UP, buff=0.1)
        r_lbl = Text("REALITY", font="Montserrat", font_size=26, color=CRIMSON, weight=BOLD).next_to(reality, UP, buff=0.1)
        i_txt = serif("System should work\nas designed", sz=26, clr=MUTE).move_to(intuition.get_center())
        r_txt = serif("Structural property\nproduces hidden failure", sz=26, clr=CRIMSON).move_to(reality.get_center())
        for o in [intuition, i_lbl, i_txt, reality, r_lbl, r_txt]:
            self.play(FadeIn(o), run_time=0.3)
        note = serif("The gap between intuition and reality is the mechanism.", sz=34, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))


class B07_KeyAnimation(Scene):
    """TERRACOTTA MOMENT"""
    def construct(self):
        d = dur("B07")
        eyebrow = caps("the core visualization", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        labels = ["EXPECTED\nBEHAVIOR", "ACTUAL\nBEHAVIOR"]
        heights = [3.5, 1.2]
        colors = [TEAL, CRIMSON]
        for i, (label, height, color) in enumerate(zip(labels, heights, colors)):
            x = (i*2 - 1) * 2.5
            bar = Rectangle(width=2.2, height=height, fill_color=color, fill_opacity=0.85, stroke_width=0)
            bar.move_to([x, -1.5 + height/2, 0])
            lbl = Text(label, font="Montserrat", font_size=24, color=color, weight=BOLD)
            lbl.next_to(bar, DOWN, buff=0.2)
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl), run_time=0.8)
        # TERRACOTTA: accent bracket showing gap
        gap_arrow = DoubleArrow([-1.1, heights[1]-1.5, 0], [-1.1, heights[0]-1.5, 0],
                                  color=ACCENT, stroke_width=4, buff=0.05)
        gap_lbl = caps("THE GAP", sz=22, clr=ACCENT).next_to(gap_arrow, LEFT, buff=0.2)
        self.play(GrowArrow(gap_arrow), FadeIn(gap_lbl), run_time=0.6)
        note = serif("The gap between expected and actual is the failure to explain.", sz=32, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))


class B08_NamedMechanism(Scene):
    def construct(self):
        d = dur("B08")
        eyebrow = caps("the mechanism has a name", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        bg = card(9.5, 2.5, fill=WHITE, stroke=INK, sw=2).move_to([0, 0.3, 0])
        quote = serif("The failure mode is structural,\nnot accidental — and has a name.", sz=40, clr=INK)
        quote.move_to(bg.get_center())
        self.play(FadeIn(bg), FadeIn(quote, shift=UP*0.1), run_time=0.7)
        note = serif("Naming the failure mode is the first step to preventing it.", sz=34, clr=ACCENT).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 5.5))


class B09_AIImplication(Scene):
    def construct(self):
        d = dur("B09")
        eyebrow = caps("for AI systems — the implication", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        items = [
            ("Domain", "Where this failure mode appears in AI systems"),
            ("Why it matters", "The operational consequence at scale"),
            ("Who is at risk", "Practitioner, user, or downstream stakeholder"),
        ]
        for i, (label, desc) in enumerate(items):
            label_lbl = Text(label, font="Montserrat", font_size=30, color=TEAL, weight=BOLD)
            desc_lbl = serif(desc, sz=34, clr=INK)
            row = VGroup(label_lbl, desc_lbl).arrange(RIGHT, buff=0.5).move_to([0, 1.2 - i*1.0, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.4)
        note = serif("The theoretical becomes operational at deployment scale.", sz=34, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))


class B10_ImplicationQuote(Scene):
    def construct(self):
        d = dur("B10")
        eyebrow = caps("the practical implication", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        for i, (label, content, color) in enumerate([
            ("DON'T", "Apply standard metric without checking this failure mode", CRIMSON),
            ("DO", "Apply the specific audit this episode describes", TEAL),
        ]):
            bg = card(4.5, 2.5, fill=WHITE, stroke=color, sw=2.5).move_to([(i*2-1)*2.7, 0, 0])
            l = Text(label, font="Montserrat", font_size=40, color=color, weight=BOLD)
            c = serif(content, sz=26, clr=INK)
            VGroup(l, c).arrange(DOWN, buff=0.3).move_to(bg.get_center())
            self.play(FadeIn(VGroup(bg, l, c), shift=RIGHT*0.1), run_time=0.5)
        note = serif("The audit is specific to the failure mode — not generic.", sz=34, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 6.5))


class B11_TheFix(Scene):
    def construct(self):
        d = dur("B11")
        eyebrow = caps("the fix", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        steps = [
            "Identify the structural property causing failure",
            "Measure it before assuming it is benign",
            "Apply the specific mitigation for this failure mode",
            "Re-measure after the intervention",
        ]
        for i, step in enumerate(steps):
            num = serif(f"{i+1}.", sz=40, clr=MUTE)
            txt = serif(step, sz=34, clr=INK)
            row = VGroup(num, txt).arrange(RIGHT, buff=0.3).move_to([0, 1.3 - i*0.9, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.4)
        ck = Text("V", font="Helvetica", font_size=60, color=TEAL).to_corner(DR, buff=0.8)
        self.play(FadeIn(ck), run_time=0.3)
        note = serif("Structural fixes outlast one-off patches.", sz=36, clr=ACCENT).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(max(0.01, d - 7.5))


class B12_WorkedExample(Scene):
    def construct(self):
        d = dur("B12")
        eyebrow = caps("worked example — the failure in a real system", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        stages = [
            ("Setup", "Real system deployed with this failure mode latent", INK),
            ("Trigger", "Structural property activates under real conditions", CRIMSON),
            ("Consequence", "Operational failure — costs measured", CRIMSON),
            ("Detection", "How the failure mode was eventually found", MUTE),
            ("Prevention", "What audit would have caught it at validation time", TEAL),
        ]
        for i, (phase, desc, color) in enumerate(stages):
            p_lbl = Text(phase, font="Montserrat", font_size=26, color=color, weight=BOLD)
            d_lbl = serif(desc, sz=26, clr=INK)
            row = VGroup(p_lbl, d_lbl).arrange(RIGHT, buff=0.5).move_to([0, 1.6 - i*0.85, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.3)
        note = serif("Every failure mode in this series has a corresponding audit.", sz=30, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(max(0.01, d - 8.5))
