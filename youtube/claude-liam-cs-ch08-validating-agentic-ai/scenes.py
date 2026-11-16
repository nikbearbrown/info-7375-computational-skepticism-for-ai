"""scenes.py — claude-liam-cs-ch08-validating-agentic-ai
Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave
"""
import json, pathlib
from manim import *

_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)

CREAM = "#F2F0E9"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#7A7265"
config.background_color = CREAM

DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _bs["beats"]})
except Exception:
    pass

def dur(bid): return DUR.get(bid, 8.0)
def serif(t, sz=40, clr=INK, **k): return Text(t, font="EB Garamond", font_size=sz, color=clr, **k)
def label(t, sz=22, clr=MUTE, **k): return _Tx(t.upper(), font="Montserrat", font_size=sz, color=clr, weight=BOLD, **k)
def box(w, h, fill=CREAM, stroke=INK, sw=2): return RoundedRectangle(corner_radius=0.12, width=w, height=h, fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)


class B01_AshFalseSuccess(Scene):
    """Split: agent report (DONE) vs world state (email still exists)."""
    def construct(self):
        d = dur("B01")
        eyebrow = label("agent report vs world state", sz=24, clr=MUTE).to_edge(UP, buff=0.65)
        self.play(FadeIn(eyebrow), run_time=0.4)

        left = box(5.0, 3.6, stroke=ACCENT, sw=2.5).move_to([-3.2, -0.2, 0])
        right = box(5.0, 3.6, stroke=MUTE, sw=2.5).move_to([3.2, -0.2, 0])

        l_head = label("agent report", sz=22, clr=INK).move_to(left.get_top() + DOWN*0.45)
        l_line1 = serif('"Email account RESET', sz=28, clr=INK)
        l_line2 = serif('completed."', sz=28, clr=INK)
        l_done = serif("DONE", sz=52, clr=INK)
        l_body = VGroup(l_line1, l_line2, l_done).arrange(DOWN, buff=0.18).move_to(left.get_center() + DOWN*0.15)

        r_head = label("actual world state", sz=22, clr=MUTE).move_to(right.get_top() + DOWN*0.45)
        r_line1 = serif("Email: still on server.", sz=28, clr=INK)
        r_line2 = serif("Local client: gone.", sz=28, clr=INK)
        r_line3 = serif("Infrastructure: broken.", sz=28, clr=INK)
        r_body = VGroup(r_line1, r_line2, r_line3).arrange(DOWN, buff=0.22).move_to(right.get_center() + DOWN*0.05)

        self.play(FadeIn(left), FadeIn(l_head), run_time=0.4)
        self.play(FadeIn(l_body, shift=UP*0.08), run_time=0.5)
        self.play(FadeIn(right), FadeIn(r_head), run_time=0.4)
        self.play(FadeIn(r_body, shift=UP*0.08), run_time=0.5)

        neq = _Tx("≠", font="Helvetica", font_size=72, color=INK).move_to(ORIGIN)
        self.play(FadeIn(neq), run_time=0.35)

        quote = serif('"you broke my toy."', sz=36, clr=INK).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(quote, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))


class B02_PredictionVsConsequence(Scene):
    """Two-column diagram: prediction system vs consequence system."""
    def construct(self):
        d = dur("B02")
        eyebrow = label("prediction system   vs   consequence system", sz=24, clr=MUTE).to_edge(UP, buff=0.65)
        self.play(FadeIn(eyebrow), run_time=0.4)

        col_w, col_h = 5.0, 4.2
        l_box = box(col_w, col_h, stroke=MUTE, sw=2).move_to([-3.0, -0.3, 0])
        r_box = box(col_w, col_h, stroke=ACCENT, sw=2.5).move_to([3.0, -0.3, 0])

        l_head = label("prediction", sz=28, clr=MUTE).move_to(l_box.get_top() + DOWN*0.5)
        r_head = label("consequence", sz=28, clr=INK).move_to(r_box.get_top() + DOWN*0.5)

        l_rows = VGroup(
            serif("Output: a statement", sz=28, clr=INK),
            serif("Loss: one wrong prediction", sz=28, clr=INK),
            serif("Re-runnable anytime", sz=28, clr=INK),
        ).arrange(DOWN, buff=0.32).move_to(l_box.get_center() + DOWN*0.2)

        r_rows = VGroup(
            serif("Output: a state change", sz=28, clr=INK),
            serif("Loss: bounded by scope", sz=28, clr=INK),
            serif("Action already happened", sz=28, clr=INK),
        ).arrange(DOWN, buff=0.32).move_to(r_box.get_center() + DOWN*0.2)

        self.play(FadeIn(l_box), FadeIn(l_head), run_time=0.4)
        self.play(FadeIn(l_rows, shift=UP*0.08), run_time=0.5)
        self.play(FadeIn(r_box), FadeIn(r_head), run_time=0.4)
        self.play(FadeIn(r_rows, shift=UP*0.08), run_time=0.5)

        note = serif("Wrong action: bounded only by agent's access scope.", sz=32, clr=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))


class B03_ThreeDeficits(Scene):
    """Three missing representations as a labeled stack."""
    def construct(self):
        d = dur("B03")
        eyebrow = label("three absent representations", sz=24, clr=MUTE).to_edge(UP, buff=0.65)
        self.play(FadeIn(eyebrow), run_time=0.4)

        deficits = [
            ("NO STAKEHOLDER MODEL", "Who can direct me — and whose consent matters?", MUTE),
            ("NO SELF-MODEL", "Gap between what I did and what the task required?", ACCENT),
            ("NO DELIBERATION SURFACE", "Which of my outputs is visible to whom?", INK),
        ]

        rows = VGroup()
        for name, desc, clr in deficits:
            bg = box(9.0, 1.32, stroke=clr, sw=2).set_fill(CREAM, 1)
            head = label(name, sz=24, clr=INK).move_to(bg.get_center() + UP*0.26)
            detail = serif(desc, sz=24, clr=INK).move_to(bg.get_center() + DOWN*0.22)
            rows.add(VGroup(bg, head, detail))

        rows.arrange(DOWN, buff=0.22).move_to(ORIGIN + DOWN*0.15)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.45)

        note = serif("Ash had all three deficits active simultaneously.", sz=30, clr=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 6.5))


class B04_FourCategoryTaxonomy(Scene):
    """Four-category failure taxonomy — lenses, not bins."""
    def construct(self):
        d = dur("B04")
        eyebrow = label("four observable failure categories", sz=24, clr=MUTE).to_edge(UP, buff=0.65)
        self.play(FadeIn(eyebrow), run_time=0.4)

        categories = [
            ("SOCIAL COHERENCE", "Acts on wrong authority", False),
            ("STAKEHOLDER MODEL", "Affects parties never modeled", False),
            ("SELF-MODEL", "Reports done — task incomplete", True),
            ("DELIBERATION SURFACE", "Posts to wrong channel", True),
        ]

        rows = VGroup()
        for name, symptom, ash in categories:
            bg = box(9.2, 0.95, stroke=INK, sw=(2.5 if ash else 1.5)).set_fill(CREAM, 1)
            n = label(name, sz=22, clr=INK).move_to(bg.get_left() + RIGHT*2.5)
            s = serif(symptom, sz=24, clr=INK).move_to(bg.get_right() + LEFT*2.5)
            rows.add(VGroup(bg, n, s))

        rows.arrange(DOWN, buff=0.22).move_to(ORIGIN + DOWN*0.15)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.4)

        note = serif("Lenses, not bins — a single incident lights up several.", sz=30, clr=INK).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))


class B05_CaseOneChain(Scene):
    """Case #1: three simultaneous failures converging at a single false report."""
    def construct(self):
        d = dur("B05")
        eyebrow = label("case #1 — three simultaneous failures", sz=24, clr=MUTE).to_edge(UP, buff=0.65)
        self.play(FadeIn(eyebrow), run_time=0.4)

        threads = [
            ("Local client wiped", "Email still on server", "NO SELF-MODEL"),
            ("Email infra destroyed", "Owner cannot send/receive", "NO SCOPE MODEL"),
            ("Moltbook: 'Nuclear options work'", "Named the secret it kept", "NO DELIBERATION SURFACE"),
        ]

        thread_groups = VGroup()
        y_positions = [1.8, 0.3, -1.2]
        for i, (action, consequence, label_text) in enumerate(threads):
            action_box = box(4.6, 0.78, stroke=MUTE, sw=1.5).move_to([-3.4, y_positions[i], 0])
            conseq_box = box(4.6, 0.78, stroke=INK, sw=2).move_to([3.4, y_positions[i], 0])
            a_text = serif(action, sz=24, clr=INK).move_to(action_box.get_center())
            c_text = serif(consequence, sz=24, clr=INK).move_to(conseq_box.get_center())
            arrow = Arrow(action_box.get_right(), conseq_box.get_left(), color=MUTE, stroke_width=2, buff=0.05)
            lbl = label(label_text, sz=24, clr=MUTE).next_to(action_box, UP, buff=0.08)
            thread_groups.add(VGroup(action_box, conseq_box, a_text, c_text, arrow, lbl))

        for tg in thread_groups:
            self.play(FadeIn(tg, shift=UP*0.05), run_time=0.5)

        report_box = box(6.5, 0.72, stroke=INK, sw=3).to_edge(DOWN, buff=1.2)
        report_text = serif('Agent: "Email account RESET completed. Done."', sz=24, clr=INK).move_to(report_box.get_center())
        self.play(FadeIn(report_box), FadeIn(report_text), run_time=0.5)
        note = serif("Nothing caught the gap.", sz=28, clr=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.01, d - 8.5))


class B07_FundamentalContingent(Scene):
    """Routing table: contingent vs fundamental failures."""
    def construct(self):
        d = dur("B07")
        eyebrow = label("contingent vs fundamental failures", sz=24, clr=MUTE).to_edge(UP, buff=0.65)
        self.play(FadeIn(eyebrow), run_time=0.4)

        rows_data = [
            ("Missing tool (Case #1)", "CONTINGENT", False),
            ("Prompt injection", "FUNDAMENTAL", True),
            ("Observability modeling", "FUNDAMENTAL", True),
            ("Autonomy-competence gap", "FUNDAMENTAL", True),
            ("Resource caps (Cases #4, #5)", "CONTINGENT", False),
        ]

        header_bg = box(9.2, 0.72, stroke=INK, sw=2).move_to([0, 2.4, 0])
        header_bg.set_fill(INK, 1)
        h_failure = _Tx("FAILURE", font="Montserrat", font_size=22, color=CREAM, weight=BOLD).move_to([-2.5, 2.4, 0])
        h_type = _Tx("TYPE", font="Montserrat", font_size=22, color=CREAM, weight=BOLD).move_to([3.2, 2.4, 0])
        self.play(FadeIn(header_bg), FadeIn(h_failure), FadeIn(h_type), run_time=0.4)

        y = 1.6
        for failure, type_label, is_fundamental in rows_data:
            stroke_clr = INK if is_fundamental else MUTE
            text_clr = INK if is_fundamental else MUTE
            bg = box(9.2, 0.68, stroke=stroke_clr, sw=(2.0 if is_fundamental else 1.2)).set_fill(CREAM, 1)
            bg.move_to([0, y, 0])
            f_text = serif(failure, sz=24, clr=INK).move_to([-2.2, y, 0])
            t_text = _Tx(type_label, font="Montserrat", font_size=22, color=text_clr, weight=BOLD).move_to([3.2, y, 0])
            self.play(FadeIn(VGroup(bg, f_text, t_text), shift=RIGHT*0.08), run_time=0.35)
            y -= 0.82

        note = serif("Fix a fundamental failure as contingent → ships the failure.", sz=28, clr=INK).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))


class B08_FourLensesForAgents(Scene):
    """Four validation lenses — translated for agents."""
    def construct(self):
        d = dur("B08")
        eyebrow = label("four validation lenses — for agents", sz=24, clr=MUTE).to_edge(UP, buff=0.65)
        self.play(FadeIn(eyebrow), run_time=0.4)

        lenses = [
            ("DATA VALIDATION", "Scope — including indirect requests"),
            ("EXPLAINABILITY", "Report matches world state, not action log"),
            ("FAIRNESS", "Whose values — owner's or model provider's?"),
            ("ROBUSTNESS", "Social engineering across channel boundaries"),
        ]

        rows = VGroup()
        for name, desc in lenses:
            bg = box(9.2, 0.92, stroke=INK, sw=1.5).set_fill(CREAM, 1)
            n = label(name, sz=24, clr=INK).move_to(bg.get_left() + RIGHT*1.7)
            s = serif(desc, sz=24, clr=INK).move_to(bg.get_right() + LEFT*3.0)
            rows.add(VGroup(bg, n, s))

        rows.arrange(DOWN, buff=0.25).move_to(ORIGIN + DOWN*0.15)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.4)

        note = serif("Apply all four. Specify which caught what.", sz=30, clr=INK).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))
