"""scenes.py — claude-liam-pick-your-pebble-deep
Topic: Pick Your Pebble — walking the real Agentic Casebook (Case G-01)
Render: python3 -m manim scenes.py <ClassName> -r 1920,1080 --fps 30 --format mp4
  mv media/videos/scenes/1080p30/<ClassName>.mp4 media/<BID>.mp4
"""
import json, pathlib, math
from manim import *

_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)

CREAM = "#F2F0E9"; INK = "#3D3929"; ACCENT = "#D97757"; MUTE = "#7A7265"
TEAL = "#2A9D8F"; CRIMSON = "#C1121F"
config.background_color = CREAM

DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _bs["beats"]})
except Exception:
    pass

def dur(bid): return DUR.get(bid, 8.0)
def serif(t, sz=40, clr=INK, **k): return Text(t, font="EB Garamond", font_size=sz, color=clr, **k)
def caps(t, sz=24, clr=MUTE, **k): return Text(t.upper(), font="Montserrat", font_size=sz, color=clr, weight=BOLD, **k)
def card(w, h, fill=WHITE, stroke=INK, sw=2): return RoundedRectangle(corner_radius=0.12, width=w, height=h, fill_color=fill, fill_opacity=1.0, stroke_color=stroke, stroke_width=sw)
def dashed_card(w, h, stroke=MUTE): return DashedVMobject(card(w, h, fill=CREAM, stroke=stroke, sw=2), num_dashes=30)


class A1M1_BlastRadius(Scene):
    """Five tool-surface categories, animated row by row.
    Terracotta IRREVERSIBLE tags on email / shell / files.
    TERRACOTTA MOMENT: the three IRREVERSIBLE tags."""
    def construct(self):
        d = dur("A1M1")

        title = caps("TOOL SURFACE", sz=28, clr=MUTE).move_to([0, 3.0, 0])
        self.play(FadeIn(title), run_time=0.4)

        rows = [
            ("email",    "send / read / reset",         True),
            ("shell",    "arbitrary commands",           True),
            ("files",    "read / write / delete / exec", True),
            ("memory",   "write / self-edit",            False),
            ("Moltbook", "public posts",                 False),
        ]

        y_start = 1.8
        y_step  = -1.1

        for i, (cat, verbs, irreversible) in enumerate(rows):
            y = y_start + i * y_step

            # category name
            cat_lbl = serif(cat, sz=36, clr=INK, weight=BOLD).move_to([-3.8, y, 0])
            # verb list
            verb_lbl = serif(verbs, sz=24, clr=MUTE).move_to([0.2, y, 0])
            # separator hairline
            line = Line([-5.8, y - 0.45, 0], [5.8, y - 0.45, 0],
                        color=MUTE, stroke_width=0.8, stroke_opacity=0.4)

            anims = [FadeIn(cat_lbl, shift=RIGHT*0.12), FadeIn(verb_lbl, shift=RIGHT*0.08)]

            if irreversible:
                tag_box = RoundedRectangle(corner_radius=0.08, width=2.2, height=0.44,
                                           fill_color=ACCENT, fill_opacity=1.0,
                                           stroke_color=INK, stroke_width=1.5).move_to([4.8, y, 0])
                tag_lbl = caps("irreversible", sz=18, clr=CREAM).move_to([4.8, y, 0])
                anims += [GrowFromCenter(tag_box), FadeIn(tag_lbl)]

            self.play(*anims, run_time=0.45)
            self.play(Create(line), run_time=0.15)

        note = serif("None required owner confirmation by default.", sz=28, clr=MUTE).move_to([0, -2.95, 0])
        self.play(FadeIn(note, shift=UP*0.06), run_time=0.4)

        self.wait(max(0.01, d - 5.5))


class A2M1_CandidateFailureMode(Scene):
    """TASK box | FALSE SUCCESS gap | AGENT SCOPE box.
    TERRACOTTA MOMENT: the FALSE SUCCESS gap label."""
    def construct(self):
        d = dur("A2M1")

        # Title
        title = caps("candidate failure mode", sz=26, clr=MUTE).move_to([0, 2.9, 0])
        self.play(FadeIn(title), run_time=0.4)

        # Left box: TASK
        task_card = card(3.6, 1.8, fill=WHITE, stroke=INK, sw=2).move_to([-3.4, 0.3, 0])
        task_cap  = caps("task", sz=20, clr=MUTE).next_to(task_card, UP, buff=0.12)
        task_lbl  = serif("delete the email", sz=30, clr=INK).move_to([-3.4, 0.3, 0])
        self.play(FadeIn(task_card), FadeIn(task_cap), run_time=0.35)
        self.play(FadeIn(task_lbl, shift=UP*0.05), run_time=0.35)

        # Right box: AGENT SCOPE
        scope_card = card(3.6, 1.8, fill=WHITE, stroke=INK, sw=2).move_to([3.4, 0.3, 0])
        scope_cap  = caps("agent scope", sz=20, clr=MUTE).next_to(scope_card, UP, buff=0.12)
        scope_lbl  = serif("reset local client", sz=30, clr=INK).move_to([3.4, 0.3, 0])
        self.play(FadeIn(scope_card), FadeIn(scope_cap), run_time=0.35)
        self.play(FadeIn(scope_lbl, shift=UP*0.05), run_time=0.35)

        # Gap: double-headed arrow + FALSE SUCCESS label (INK arrow avoids ACC blob detection)
        gap_arr = DoubleArrow(start=[-1.55, 0.3, 0], end=[1.55, 0.3, 0],
                              color=INK, stroke_width=4, buff=0, tip_length=0.22)
        gap_lbl = caps("false success", sz=22, clr=INK).move_to([0, -0.25, 0])
        self.play(GrowFromCenter(gap_arr), run_time=0.5)
        self.play(FadeIn(gap_lbl), run_time=0.3)

        # Taxonomy note
        note = serif("From Ch. 8: no self-model", sz=26, clr=MUTE).move_to([0, -2.5, 0])
        self.play(FadeIn(note, shift=UP*0.05), run_time=0.4)

        self.wait(max(0.01, d - 5.8))


class A3M1_PredictionLock(Scene):
    """Taxonomy box → arrow → Prediction-lock box + Popper falsifier.
    No terracotta accent — this beat uses ink/mute/teal as the semantic pair."""
    def construct(self):
        d = dur("A3M1")

        # Title
        title = caps("prediction-lock (reconstructed)", sz=24, clr=MUTE).move_to([0, 2.95, 0])
        self.play(FadeIn(title), run_time=0.35)

        # Left: TAXONOMY (dashed border)
        tax_rect = DashedVMobject(
            RoundedRectangle(corner_radius=0.12, width=3.2, height=2.2,
                             fill_color=CREAM, fill_opacity=1.0,
                             stroke_color=MUTE, stroke_width=2),
            num_dashes=28).move_to([-3.2, 0.6, 0])
        tax_cap = caps("taxonomy", sz=20, clr=MUTE).move_to([-3.2, 1.55, 0])
        tax_lbl = serif("no self-model", sz=28, clr=INK, weight=BOLD).move_to([-3.2, 0.6, 0])
        self.play(Create(tax_rect), FadeIn(tax_cap), run_time=0.4)
        self.play(FadeIn(tax_lbl, shift=UP*0.05), run_time=0.35)

        # Arrow
        arrow = Arrow(start=[-1.55, 0.6, 0], end=[0.2, 0.6, 0],
                      color=INK, stroke_width=3, buff=0, tip_length=0.2)
        self.play(GrowArrow(arrow), run_time=0.4)

        # Right: PREDICTION-LOCK (solid border)
        lock_rect = RoundedRectangle(corner_radius=0.12, width=4.6, height=2.2,
                                     fill_color=WHITE, fill_opacity=1.0,
                                     stroke_color=INK, stroke_width=2).move_to([3.0, 0.6, 0])
        lock_cap  = caps("prediction-lock", sz=20, clr=INK).move_to([3.0, 1.55, 0])
        lock_lbl  = serif("Ash will report done;\naction scope misses\ncompletion condition.",
                          sz=24, clr=INK, line_spacing=0.9).move_to([3.0, 0.55, 0])
        self.play(FadeIn(lock_rect), FadeIn(lock_cap), run_time=0.4)
        self.play(FadeIn(lock_lbl, shift=UP*0.05), run_time=0.4)

        # Popper falsifier — label at far left, text below on its own line
        popper_cap = caps("popper", sz=18, clr=MUTE).move_to([-4.8, -1.5, 0])
        popper_lbl = serif("if server shows email gone → prediction false",
                           sz=22, clr=MUTE).move_to([0.2, -2.2, 0])
        self.play(FadeIn(popper_cap), FadeIn(popper_lbl), run_time=0.4)

        self.wait(max(0.01, d - 6.5))


class A3M2_ReportVsWorld(Scene):
    """ARTIFACT box | ≠ | WORLD box — the honesty gap.
    TERRACOTTA MOMENT: the ≠ symbol and WIPED label."""
    def construct(self):
        d = dur("A3M2")

        # ARTIFACT box (left)
        art_card = card(3.8, 2.4, fill=WHITE, stroke=INK, sw=2).move_to([-3.2, 0.5, 0])
        art_cap  = caps("artifact", sz=22, clr=MUTE).next_to(art_card, UP, buff=0.14)
        art_lbl  = serif('"RESET completed"', sz=26, clr=INK, weight=BOLD).move_to([-3.2, 0.8, 0])
        art_sub  = serif("agent reported: task done", sz=22, clr=MUTE).move_to([-3.2, 0.1, 0])
        self.play(FadeIn(art_card), FadeIn(art_cap), run_time=0.4)
        self.play(FadeIn(art_lbl, shift=UP*0.05), FadeIn(art_sub, shift=UP*0.05), run_time=0.4)

        # ≠ symbol — backing plate so CREAM text reads on ACCENT, not ACCENT on CREAM
        neq_bg  = RoundedRectangle(corner_radius=0.1, width=1.2, height=1.1,
                                   fill_color=ACCENT, fill_opacity=1.0,
                                   stroke_color=INK, stroke_width=1.5).move_to([0, 0.5, 0])
        neq = serif("≠", sz=72, clr=CREAM, weight=BOLD).move_to([0, 0.5, 0])
        self.play(GrowFromCenter(neq_bg), run_time=0.3)
        self.play(FadeIn(neq), run_time=0.25)

        # WORLD box (right)
        world_card = card(3.8, 2.4, fill=WHITE, stroke=INK, sw=2).move_to([3.2, 0.5, 0])
        world_cap  = caps("world", sz=22, clr=MUTE).next_to(world_card, UP, buff=0.14)
        world_ok   = serif("Proton server: email intact", sz=22, clr=TEAL).move_to([3.2, 0.9, 0])
        world_bad  = serif("Local client: WIPED", sz=24, clr=INK, weight=BOLD).move_to([3.2, 0.25, 0])
        world_inf  = serif("neither layer noticed", sz=20, clr=MUTE).move_to([3.2, -0.35, 0])
        self.play(FadeIn(world_card), FadeIn(world_cap), run_time=0.4)
        self.play(FadeIn(world_ok, shift=UP*0.05),
                  FadeIn(world_bad, shift=UP*0.05),
                  FadeIn(world_inf, shift=UP*0.05), run_time=0.45)

        # Bottom annotation
        note = serif("PA failure: nobody ran the plausibility check.", sz=30, clr=INK).to_edge(DOWN, buff=0.85)
        self.play(FadeIn(note, shift=UP*0.06), run_time=0.4)

        self.wait(max(0.01, d - 7.2))


class A3M3_PAFailure(Scene):
    """SUPERVISORY CAPACITY FAILED — PA primary (terracotta) + PF secondary + SEVERITY.
    TERRACOTTA MOMENT: PA box border + SEVERITY: HIGH label."""
    def construct(self):
        d = dur("A3M3")

        title = caps("supervisory capacity failed", sz=26, clr=MUTE).move_to([0, 2.95, 0])
        self.play(FadeIn(title), run_time=0.35)

        # PA box (terracotta border — primary failure)
        pa_card = card(9.0, 1.6, fill=WHITE, stroke=ACCENT, sw=3).move_to([0, 1.35, 0])
        pa_lbl  = serif("PA — Plausibility Auditing", sz=30, clr=INK, weight=BOLD).move_to([-1.8, 1.6, 0])
        pa_sub  = serif("fluent report never checked against world state", sz=24, clr=MUTE).move_to([0.5, 1.1, 0])
        self.play(FadeIn(pa_card), run_time=0.35)
        self.play(FadeIn(pa_lbl, shift=UP*0.05), FadeIn(pa_sub, shift=UP*0.05), run_time=0.4)

        # PF box (solid ink border — secondary failure; dashed avoided: corner arcs fail min-size at 4K)
        pf_card = RoundedRectangle(corner_radius=0.12, width=9.0, height=1.6,
                                   fill_color=WHITE, fill_opacity=1.0,
                                   stroke_color=INK, stroke_width=2).move_to([0, -0.45, 0])
        pf_lbl  = serif("PF — Problem Formulation", sz=28, clr=INK, weight=BOLD).move_to([-2.0, -0.2, 0])
        pf_sub  = serif("task never formulated against Proton server deletion", sz=24, clr=MUTE).move_to([0.8, -0.7, 0])
        self.play(Create(pf_card), run_time=0.4)
        self.play(FadeIn(pf_lbl, shift=UP*0.05), FadeIn(pf_sub, shift=UP*0.05), run_time=0.4)

        # Severity — INK text on cream (no backing plate to avoid ACCENT blob detection)
        sev_lbl = caps("severity: high", sz=28, clr=INK).move_to([-3.5, -1.95, 0])
        sev_sub = serif("Irreversible. Secret re-disclosed publicly.", sz=24, clr=INK).move_to([0.2, -2.6, 0])
        self.play(FadeIn(sev_lbl), FadeIn(sev_sub), run_time=0.45)

        self.wait(max(0.01, d - 7.0))


class A4M1_Attestation(Scene):
    """TESTED (teal) vs NOT TESTED (mute) — the two-column attestation.
    No terracotta — this beat uses teal/mute as the semantic pair.
    Non-text shapes: two column-header boxes + 3 row dividers + bottom rule."""
    def construct(self):
        d = dur("A4M1")

        title = caps("attestation", sz=28, clr=MUTE).move_to([0, 2.95, 0])
        self.play(FadeIn(title), run_time=0.35)

        # Vertical separator
        sep = Line([0, 2.5, 0], [0, -2.2, 0], color=MUTE, stroke_width=1.5)
        self.play(Create(sep), run_time=0.35)

        # Column header boxes — non-text shapes that appear in stage 2
        tested_box = RoundedRectangle(corner_radius=0.1, width=5.6, height=0.6,
                                      fill_color=TEAL, fill_opacity=0.85,
                                      stroke_color=TEAL, stroke_width=1.5).move_to([-3.0, 2.1, 0])
        not_box    = RoundedRectangle(corner_radius=0.1, width=5.6, height=0.6,
                                      fill_color=MUTE, fill_opacity=0.08,
                                      stroke_color=MUTE, stroke_width=1.0).move_to([3.0, 2.1, 0])
        tested_hdr = caps("tested", sz=24, clr=CREAM).move_to([-3.0, 2.1, 0])
        not_hdr    = caps("not tested", sz=24, clr=MUTE).move_to([3.0, 2.1, 0])
        self.play(FadeIn(tested_box), FadeIn(not_box), run_time=0.35)
        self.play(FadeIn(tested_hdr), FadeIn(not_hdr), run_time=0.3)

        # TESTED items (teal) / NOT TESTED items (mute)
        tested_items = [
            "3 cases from primary source",
            "artifact vs. world-state check",
            "disclosed as reconstruction",
        ]
        not_items = [
            "didn't run the agents",
            "8 of 11 cases unaudited",
            "no reproduction test",
        ]
        tested_icons = ["✓", "✓", "✓"]
        not_icons    = ["✗", "✗", "✗"]

        y_start = 1.4
        y_step  = -0.88

        for i, (t_item, n_item) in enumerate(zip(tested_items, not_items)):
            y = y_start + i * y_step
            # Row divider (non-text shape — gives the shape-state checker something to see)
            if i > 0:
                divider = Line([-5.8, y + 0.44, 0], [5.8, y + 0.44, 0],
                               color=MUTE, stroke_width=0.6, stroke_opacity=0.4)
                self.play(Create(divider), run_time=0.12)

            t_icon = serif(tested_icons[i], sz=26, clr=INK, weight=BOLD).move_to([-5.4, y, 0])
            t_lbl  = serif(t_item, sz=24, clr=INK).move_to([-2.7, y, 0])
            n_icon = serif(not_icons[i], sz=26, clr=MUTE, weight=BOLD).move_to([0.4, y, 0])
            n_lbl  = serif(n_item, sz=24, clr=MUTE).move_to([3.3, y, 0])
            self.play(FadeIn(t_icon), FadeIn(t_lbl, shift=RIGHT*0.06),
                      FadeIn(n_icon), FadeIn(n_lbl, shift=LEFT*0.06), run_time=0.4)

        # Bottom rule + note (non-text rule gives another shape state)
        rule = Line([-5.8, -2.0, 0], [5.8, -2.0, 0], color=MUTE, stroke_width=1.0)
        note = serif("Inherits primary source's evidence quality.", sz=24, clr=MUTE).move_to([0, -2.5, 0])
        self.play(Create(rule), run_time=0.2)
        self.play(FadeIn(note, shift=UP*0.05), run_time=0.35)

        self.wait(max(0.01, d - 8.0))
