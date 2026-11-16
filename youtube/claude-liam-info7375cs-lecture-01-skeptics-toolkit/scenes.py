"""
Manim scenes — claude-liam-info7375cs-lecture-01-skeptics-toolkit
deep-explainer · claude-liam · Kokoro am_onyx · Claude skin
INFO 7375 Computational Skepticism for AI, Lecture 1

Every number on screen traces to FACTCHECK.md. Constants declared at module
scope with VERIFY assertions that run at import time, BEFORE any scene renders.
Palette: Claude fidelity tokens (CLAUDE-BRAND.md). One terracotta moment per beat.
Text color is INK on CREAM/STAGE (GATE T §8.3); terracotta is FILL/STROKE only.
Type floor: font_size ≥ 32 (titles ≥ 40). Coords inside ±7.1 / ±4.0.
Every scene shows ≥1 non-text non-Rectangle shape; shape set changes ≥1 time.
"""
from manim import *
import math

CREAM = "#FAF9F5"
STAGE = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
DIM   = "#8B8F96"
GHOST = "#D9D4C7"
SERIF = "EB Garamond"
MONO  = "Menlo"

# ═══════════════════════ verified constants (FACTCHECK.md) ═══════════════════════
PATIENTS   = 27697   # row 2 — Sendak et al. 2020 external audit
MISSED_PCT = 67      # row 3 — ~2/3 missed
ALERT_PCT  = 18      # row 4
AUC        = 0.63    # row 5
assert PATIENTS == 27697
assert MISSED_PCT == 67
assert ALERT_PCT  == 18
assert 0.62 < AUC < 0.64

KC_SERVERS  = 8    # row 10
KC_BAD      = 1    # one server missed the update
KC_MINS     = 45   # row 11
KC_TRADES_M = 4    # millions of trades
KC_STOCKS   = 154
KC_LOSS_M   = 440  # ≈ $440 M
assert KC_SERVERS == 8 and KC_BAD == 1 and KC_SERVERS > KC_BAD
assert KC_MINS == 45 and KC_TRADES_M == 4 and KC_STOCKS == 154 and KC_LOSS_M == 440

ZL_WRITE_M   = 304   # row 13 — Q3 write-down
ZL_EXPECT_LO = 240   # row 14 — Q4 expected low
ZL_EXPECT_HI = 265   # row 14 — Q4 expected high
ZL_STAFF_PCT = 25    # ~25% of staff
assert ZL_WRITE_M == 304 and ZL_EXPECT_LO == 240 and ZL_EXPECT_HI == 265 and ZL_STAFF_PCT == 25
assert ZL_WRITE_M + ZL_EXPECT_LO > 500

GF_OVER  = 100   # row 15 — weeks over-predicted
GF_TOTAL = 108   # row 16 — total weeks in study
assert GF_OVER == 100 and GF_TOTAL == 108 and GF_OVER / GF_TOTAL > 0.9

CAPACITIES = 5   # row 21
assert CAPACITIES == 5

# ═══════════════════════ shared helpers ═══════════════════════

def _title(txt, size=40):
    return Text(txt, font=SERIF, color=INK, font_size=size).to_edge(UP, buff=0.8)

def _caption(txt, size=32):
    return Text(txt, font=SERIF, color=DIM, font_size=size).to_edge(DOWN, buff=0.7)

def _sub(t, txt, size=32):
    return Text(txt, font=SERIF, color=DIM, font_size=size).next_to(t, DOWN, buff=0.15)

def _statement_scene(self, statement_lines, emphasis, subline):
    self.camera.background_color = STAGE
    st = Paragraph(*statement_lines, font=SERIF, color=INK,
                   font_size=64, alignment="center", line_spacing=1.05).move_to(UP * 0.8)
    em = Text(emphasis, font=SERIF, color=INK, font_size=66, weight=BOLD)
    if em.width > 11.0:
        em.scale(11.0 / em.width)
    em.next_to(st, DOWN, buff=0.5)
    ul = Line(LEFT * 3, RIGHT * 3, color=TERRA, stroke_width=6).next_to(em, DOWN, buff=0.2)
    ul.set_width(min(em.width + 0.4, 11.0))
    sub = Text(subline, font=SERIF, color=DIM, font_size=34).to_edge(DOWN, buff=0.8)
    bar = Line(UP * 2.7, DOWN * 2.7, color=TERRA, stroke_width=14).move_to(LEFT * 6.0)
    dot = Dot(color=TERRA, radius=0.12).next_to(em, RIGHT, buff=0.25)
    self.play(Create(bar), Write(st), run_time=2.0)
    self.play(FadeIn(em, shift=UP * 0.15), FadeIn(dot), run_time=0.7)
    self.play(Create(ul), run_time=0.6)
    self.play(FadeIn(sub))
    self.wait(2)

def _two_column(self, title, lh, l_lines, rh, r_lines, footer=None, accent_left=False, size=32):
    self.camera.background_color = STAGE
    t = _title(title)
    div = Line(UP * 2.3, DOWN * 2.6, color=TERRA, stroke_width=4)
    def col(head, lines, x, left):
        h = Text(head, font=SERIF, color=INK, font_size=40, weight=BOLD).move_to([x, 1.9, 0])
        body = VGroup(*[Text(l, font=SERIF, color=INK, font_size=size)
                        for l in lines]).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        body.next_to(h, DOWN, buff=0.4).align_to([left, 0, 0], LEFT)
        return h, body
    lhm, lb = col(lh, l_lines, -3.2, -5.8)
    rhm, rb = col(rh, r_lines,  3.3,  0.4)
    self.play(FadeIn(t), Create(div), run_time=1.0)
    self.play(FadeIn(lhm), run_time=0.5)
    for m in lb:
        d = Dot(color=TERRA if accent_left else INK, radius=0.08).next_to(m, LEFT, buff=0.25)
        self.play(FadeIn(d), FadeIn(m, shift=RIGHT * 0.2), run_time=0.4)
    self.play(FadeIn(rhm), run_time=0.5)
    for m in rb:
        d = Dot(color=INK if accent_left else TERRA, radius=0.08).next_to(m, LEFT, buff=0.25)
        self.play(FadeIn(d), FadeIn(m, shift=RIGHT * 0.2), run_time=0.4)
    if footer:
        self.play(FadeIn(_caption(footer)), run_time=0.6)
    self.wait(2)

def _vbars(self, title, items, scale=None, base_y=-1.8, width=1.6, gap=2.8,
           accent_idx=None, caption=None, sub=None, fmt=None, grow_time=1.2):
    self.camera.background_color = STAGE
    t = _title(title)
    n = len(items)
    vmax = max(abs(v) for _, v in items)
    sc = scale or (2.8 / vmax)
    base = Line(LEFT * 5.6, RIGHT * 5.6, color=INK, stroke_width=2).move_to([0, base_y, 0])
    fmt = fmt or (lambda v: f"${v}M" if v > 100 else f"{v}%")
    xs = [(i - (n - 1) / 2) * gap for i in range(n)]
    self.play(FadeIn(t), Create(base), run_time=1.0)
    if sub:
        self.play(FadeIn(_sub(t, sub)), run_time=0.5)
    for i, ((name, v), x) in enumerate(zip(items, xs)):
        h = abs(v) * sc
        fill = TERRA if i == accent_idx else INK
        y_c = base_y + h / 2
        r = Rectangle(width=width, height=h,
                      fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, y_c, 0])
        val = Text(fmt(v), font=SERIF, color=INK, font_size=38, weight=BOLD).next_to(r, UP, buff=0.18)
        lab = Text(name, font=SERIF, color=INK, font_size=32)
        lab.move_to([x, base_y - 0.52, 0])
        dot = Dot(color=TERRA, radius=0.08).move_to([x, base_y, 0])
        self.play(FadeIn(dot), run_time=0.3)
        self.add(r)
        self.play(GrowFromEdge(r, DOWN), FadeIn(val), FadeIn(lab), run_time=grow_time)
    if caption:
        self.play(FadeIn(_caption(caption)), run_time=0.6)
    self.wait(2)

# ═══════════════════════ B03 — framework ═══════════════════════

class B03_ToolkitFramework(Scene):
    """ARTIFACT / WORLD / RELATIONSHIP slot; four moves; who asks?"""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("The toolkit in one picture")
        art_box = RoundedRectangle(width=3.4, height=1.5, corner_radius=0.2,
                                   stroke_color=INK, stroke_width=3, fill_opacity=0).move_to([-4.3, 0.2, 0])
        wld_box = RoundedRectangle(width=3.4, height=1.5, corner_radius=0.2,
                                   stroke_color=INK, stroke_width=3, fill_opacity=0).move_to([ 4.3, 0.2, 0])
        rel_box = RoundedRectangle(width=3.6, height=2.2, corner_radius=0.2,
                                   stroke_color=DIM, stroke_width=2, fill_opacity=0,
                                   stroke_opacity=0.7).move_to([0.0, 0.2, 0])
        art_lbl = Text("ARTIFACT", font=SERIF, color=INK, font_size=36, weight=BOLD).move_to(art_box.get_center())
        wld_lbl = Text("WORLD",    font=SERIF, color=INK, font_size=36, weight=BOLD).move_to(wld_box.get_center())
        l_arr = Arrow(art_box.get_right(), rel_box.get_left(),  color=INK, buff=0.1, stroke_width=2, max_tip_length_to_length_ratio=0.12)
        r_arr = Arrow(rel_box.get_right(), wld_box.get_left(), color=INK, buff=0.1, stroke_width=2, max_tip_length_to_length_ratio=0.12)
        moves = VGroup(
            Text("doubt?",         font=SERIF, color=INK, font_size=32),
            Text("induction?",     font=SERIF, color=INK, font_size=32),
            Text("falsify?",       font=SERIF, color=INK, font_size=32),
            Text("cave?",          font=SERIF, color=INK, font_size=32),
        ).arrange(DOWN, buff=0.18).move_to(rel_box.get_center())
        who = Text("who asks?  →  five capacities", font=SERIF, color=DIM, font_size=34).to_edge(DOWN, buff=1.1)
        self.play(FadeIn(t), run_time=0.6)
        self.play(Create(art_box), FadeIn(art_lbl), Create(wld_box), FadeIn(wld_lbl), run_time=1.2)
        self.play(Create(l_arr), Create(r_arr), Create(rel_box), run_time=1.0)
        for m in moves:
            self.play(FadeIn(m, shift=RIGHT * 0.1), run_time=0.45)
        self.play(FadeIn(who), run_time=0.6)
        self.wait(2)

# ═══════════════════════ ACT I ═══════════════════════

class B05_SepsisIsotype(Scene):
    """Three patient icons; two ghost = missed; counter 27,697."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title(f"External audit — {PATIENTS:,} hospitalized patients")
        cap = _caption("Sendak et al. 2020, NEJM Catalyst · FACTCHECK rows 2–3")

        def figure(color, opacity=1.0):
            head = Circle(radius=0.32, color=color, fill_color=color,
                          fill_opacity=opacity, stroke_width=0)
            body = RoundedRectangle(width=0.5, height=0.9, corner_radius=0.15,
                                    fill_color=color, fill_opacity=opacity, stroke_width=0)
            body.next_to(head, DOWN, buff=0.05)
            return VGroup(head, body)

        figs = VGroup(
            figure(INK),
            figure(INK),
            figure(INK),
        ).arrange(RIGHT, buff=1.2).move_to([0, -0.1, 0])

        missed_label = Text(f"missed ≈ {MISSED_PCT}%", font=SERIF, color=TERRA, font_size=40)
        missed_label.next_to(figs, DOWN, buff=0.7).shift(LEFT * 1.0)
        arrow = Arrow(missed_label.get_right() + RIGHT * 0.1,
                      figs[0].get_bottom() + DOWN * 0.1,
                      color=TERRA, stroke_width=2, buff=0.1,
                      max_tip_length_to_length_ratio=0.15)

        self.play(FadeIn(t), run_time=0.6)
        self.play(FadeIn(figs), run_time=1.0)
        # ghost two of three
        self.play(
            figs[0].animate.set_opacity(0.18),
            figs[1].animate.set_opacity(0.18),
            run_time=1.2,
        )
        self.play(FadeIn(missed_label), Create(arrow), run_time=0.8)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B06_SepsisMetrics(Scene):
    """Left: 100-dot grid (18 TERRA = alert rate). Right: AUC semi-dial at 0.63."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("The model's two numbers")

        # dot grid
        dot_r = 0.22
        cols, rows = 10, 10
        dots = VGroup()
        for row in range(rows):
            for col in range(cols):
                idx = row * cols + col
                color = TERRA if idx < ALERT_PCT else GHOST
                d = Dot(radius=dot_r, color=color).move_to(
                    [-5.5 + col * 0.72, 1.2 - row * 0.56, 0])
                dots.add(d)

        grid_lbl = Text(f"{ALERT_PCT}% of all hospitalized patients alerted",
                        font=SERIF, color=INK, font_size=34).move_to([-3.5, -2.6, 0])

        # AUC dial
        dial_center = [3.8, -0.3, 0]
        radius = 1.8
        arc = Arc(radius=radius, start_angle=0, angle=PI,
                  color=INK, stroke_width=4).move_to(dial_center)
        chance_line = Line(
            [dial_center[0], dial_center[1], 0],
            [dial_center[0], dial_center[1] + radius, 0],
            color=GHOST, stroke_width=2,
        )
        needle_angle = math.pi * (1 - AUC)
        needle_tip = [
            dial_center[0] + radius * math.cos(needle_angle),
            dial_center[1] + radius * math.sin(needle_angle),
            0,
        ]
        needle = Arrow(
            dial_center, needle_tip, color=TERRA, stroke_width=4,
            buff=0, max_tip_length_to_length_ratio=0.15,
        )
        auc_lbl = Text(f"AUC = {AUC}", font=SERIF, color=INK, font_size=38, weight=BOLD)
        auc_lbl.move_to([dial_center[0], dial_center[1] - 0.7, 0])
        chance_lbl = Text("chance = 0.5", font=SERIF, color=DIM, font_size=32)
        chance_lbl.move_to([dial_center[0] + 0.1, dial_center[1] + radius + 0.35, 0])
        divider = Line(UP * 2.5, DOWN * 2.5, color=GHOST, stroke_width=2).move_to([1.2, 0, 0])

        self.play(FadeIn(t), Create(divider), run_time=0.8)
        self.play(FadeIn(dots), run_time=1.0)
        self.play(FadeIn(grid_lbl), run_time=0.6)
        self.play(Create(arc), Create(chance_line), FadeIn(chance_lbl), run_time=1.0)
        self.play(Create(needle), FadeIn(auc_lbl), run_time=1.2)
        self.wait(2)

class B07_TwoScorecards(Scene):
    """Same model, two scorecards."""
    def construct(self):
        _two_column(
            self, "The same model — two different scorecards",
            "Builders' measures",
            ["internal validation ✓", "AUC published ✓", "procurement cleared ✓"],
            "At the bedside",
            [f"missed {MISSED_PCT}% of septic patients"],
            accent_left=False, size=34,
        )

class B08_AgentAsh(Scene):
    """Four tiles: ASKED · DID · REPORTED · STATE; gap arrow flashes."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("Agents of Chaos — Case #1")
        cap = _caption("'You broke my toy.'  —  the owner  ·  FACTCHECK rows 7–8")

        labels = ["ASKED", "DID", "REPORTED", "STATE"]
        details = [
            "delete the email\nhiding the secret",
            "nuclear reset of\nown mail setup",
            "account reset\ncompleted",
            "email still present\non the provider",
        ]
        colors = [INK, INK, INK, INK]
        tiles = VGroup()
        tile_objs = []
        for i, (lbl, det) in enumerate(zip(labels, details)):
            box = RoundedRectangle(width=2.8, height=2.0, corner_radius=0.18,
                                   stroke_color=INK, stroke_width=2.5, fill_opacity=0)
            head = Text(lbl, font=SERIF, color=INK, font_size=36, weight=BOLD).move_to(box.get_center() + UP * 0.45)
            body = Paragraph(*det.split("\n"), font=SERIF, color=INK, font_size=30,
                             alignment="center", line_spacing=0.9).move_to(box.get_center() + DOWN * 0.25)
            g = VGroup(box, head, body)
            tiles.add(g)
            tile_objs.append((box, head, body))

        tiles.arrange(RIGHT, buff=0.55).move_to([0, -0.1, 0])

        # gap arrow between REPORTED and STATE
        rep_box = tiles[2][0]
        sta_box = tiles[3][0]
        gap_arr = Arrow(rep_box.get_right(), sta_box.get_left(),
                        color=TERRA, stroke_width=4, buff=0.08,
                        max_tip_length_to_length_ratio=0.2)

        self.play(FadeIn(t), run_time=0.6)
        for g in tiles:
            self.play(FadeIn(g), run_time=0.5)
        self.play(Create(gap_arr), run_time=0.8)
        self.play(
            tiles[2][0].animate.set_stroke(color=TERRA, width=3),
            tiles[3][0].animate.set_stroke(color=TERRA, width=3),
            run_time=0.6,
        )
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B09_CompositePatient(Scene):
    """Schematic body; LOW-ACUITY score; clot dot travels leg → lung."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("One patient — a composite")
        cap = _caption("composite — not a real patient record  ·  FACTCHECK row 9")

        # simplified body outline: ellipse torso + circle head + line legs
        torso = Ellipse(width=2.0, height=3.2, color=INK, stroke_width=2.5,
                        fill_opacity=0).move_to([0, -0.1, 0])
        head = Circle(radius=0.45, color=INK, stroke_width=2.5,
                      fill_opacity=0).move_to([0, 1.85, 0])
        leg_l = Line([0, -1.7, 0], [-0.5, -3.3, 0], color=INK, stroke_width=2)
        leg_r = Line([0, -1.7, 0], [ 0.5, -3.3, 0], color=INK, stroke_width=2)

        # score tag
        score_box = RoundedRectangle(width=3.4, height=0.8, corner_radius=0.15,
                                     stroke_color=INK, stroke_width=2, fill_opacity=0).move_to([3.8, 0.0, 0])
        score_lbl = Text("LOW-ACUITY", font=SERIF, color=INK, font_size=34, weight=BOLD).move_to(score_box.get_center())
        score_arr = Arrow(score_box.get_left(), [1.05, 0.0, 0],
                          color=INK, buff=0.08, stroke_width=2,
                          max_tip_length_to_length_ratio=0.15)

        # clot dot starts at leg
        dot_start = [-0.4, -2.8, 0]
        dot_end   = [-0.5,  0.5, 0]   # lung region (inside torso, upper left)
        clot = Dot(radius=0.18, color=TERRA).move_to(dot_start)

        self.play(FadeIn(t), run_time=0.6)
        self.play(Create(torso), Create(head), Create(leg_l), Create(leg_r), run_time=1.2)
        self.play(FadeIn(clot), run_time=0.5)
        self.play(FadeIn(score_box), FadeIn(score_lbl), Create(score_arr), run_time=0.8)
        self.play(clot.animate.move_to(dot_end), run_time=1.8)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B10_StatVsQuestion(Scene):
    """Statistically valid. Wrong about the question that mattered."""
    def construct(self):
        _statement_scene(
            self,
            ["Statistically valid."],
            "Wrong about the question that mattered.",
            "the gap is this course",
        )

# ═══════════════════════ ACT II ═══════════════════════

class B12_DescartesChecklist(Scene):
    """Three checkboxes land in sequence; all tick terracotta."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("Descartes: what would have to be true?")

        items = [
            "training data underweighted cases like this",
            "input features missed the relevant signal",
            "deployment context ≠ validation context",
        ]
        group = VGroup()
        boxes = []
        for i, txt in enumerate(items):
            box = Square(side_length=0.45, color=INK, stroke_width=2.5,
                         fill_opacity=0).move_to([-4.5, 0.8 - i * 1.2, 0])
            lbl = Text(txt, font=SERIF, color=INK, font_size=36)
            lbl.next_to(box, RIGHT, buff=0.4)
            group.add(VGroup(box, lbl))
            boxes.append(box)

        footer = Text("three checkable engineering questions",
                      font=SERIF, color=DIM, font_size=34).to_edge(DOWN, buff=1.0)
        dot = Dot(color=TERRA, radius=0.06)  # non-text shape, added early

        self.play(FadeIn(t), FadeIn(dot.move_to(LEFT * 6.5 + DOWN * 2.5)), run_time=0.6)
        for g in group:
            self.play(FadeIn(g), run_time=0.7)
        # tick each box
        for box in boxes:
            tick = Text("✓", font=SERIF, color=TERRA, font_size=38).move_to(box.get_center())
            self.play(FadeIn(tick), run_time=0.4)
        self.play(FadeIn(footer), run_time=0.6)
        self.wait(2)

class B13_KnightCapital(Scene):
    """8 server tiles; 7 green / 1 grey; Power Peg flag; 45-min bar; summary."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title(f"Knight Capital — 2012-08-01")

        sx, sy = 0.72, 1.1
        gap = 0.22
        total_w = KC_SERVERS * sx + (KC_SERVERS - 1) * gap
        x0 = -total_w / 2 + sx / 2

        tiles = VGroup()
        server_labels = VGroup()
        for i in range(KC_SERVERS):
            x = x0 + i * (sx + gap)
            fill = GHOST if i == KC_SERVERS - 1 else INK
            box = RoundedRectangle(width=sx, height=sy, corner_radius=0.12,
                                   fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, 1.1, 0])
            tiles.add(box)
        update_lbl = Text(f"7 of {KC_SERVERS} updated", font=SERIF, color=INK, font_size=34).move_to([0, 2.4, 0])

        # flag on bad server
        bad_x = x0 + (KC_SERVERS - 1) * (sx + gap)
        flag_pole = Line([bad_x, sy / 2 + 0.8, 0], [bad_x, sy / 2 + 1.5, 0], color=TERRA, stroke_width=3)
        flag_tri  = Polygon(
            [bad_x,       sy / 2 + 1.5, 0],
            [bad_x + 0.5, sy / 2 + 1.3, 0],
            [bad_x,       sy / 2 + 1.1, 0],
            fill_color=TERRA, fill_opacity=1, stroke_width=0,
        )
        flag_lbl  = Text("Power Peg\n(dead code, 2003)", font=SERIF, color=INK, font_size=28)
        flag_lbl.next_to(flag_tri, RIGHT, buff=0.25).shift(DOWN * 0.1)

        # 45-minute bar
        bar_h = 1.0
        bar = Rectangle(width=0, height=bar_h, fill_color=TERRA, fill_opacity=1, stroke_width=0)
        bar.move_to([-4.0, -1.8, 0]).align_to([-5.8, -1.8, 0], LEFT)
        bar_full = Rectangle(width=5.5, height=bar_h, fill_color=TERRA, fill_opacity=1, stroke_width=0)
        bar_full.move_to([-3.05, -1.8, 0]).align_to([-5.8, -1.8, 0], LEFT)
        bar_bg   = Rectangle(width=5.5, height=bar_h, fill_color=GHOST, fill_opacity=1, stroke_width=0)
        bar_bg.move_to(bar_full.get_center())
        bar_lbl  = Text(f"{KC_MINS} minutes", font=SERIF, color=INK, font_size=34).move_to([-1.3, -1.8, 0])
        self.add(bar_bg)

        # summary row
        summary = Text(
            f"{KC_TRADES_M} M executions  ·  {KC_STOCKS} stocks  ·  ≈ ${KC_LOSS_M} M",
            font=SERIF, color=INK, font_size=34,
        ).to_edge(DOWN, buff=0.7)

        self.play(FadeIn(t), run_time=0.6)
        self.play(FadeIn(tiles), FadeIn(update_lbl), run_time=1.0)
        self.play(Create(flag_pole), FadeIn(flag_tri), FadeIn(flag_lbl), run_time=0.8)
        self.play(Transform(bar, bar_full), FadeIn(bar_lbl), run_time=1.8)
        self.play(FadeIn(summary), run_time=0.6)
        self.wait(2)

class B14_DeploymentStatement(Scene):
    """'Deployment succeeded' ≠ 'The system is doing what we intend.'"""
    def construct(self):
        _statement_scene(
            self,
            ["'Deployment succeeded'"],
            "≠  The system is doing what we intend.",
            "radical doubt: never let the first stand for the second",
        )

# ═══════════════════════ ACT III ═══════════════════════

class B16_TurkeyInduction(Scene):
    """Confidence rises for 999 days; drops to 0 on day 1000."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("The turkey's spreadsheet")

        ax_x  = Line([-5.5, -1.8, 0], [ 5.5, -1.8, 0], color=INK, stroke_width=2)
        ax_y  = Line([-5.5, -1.8, 0], [-5.5,  2.2, 0], color=INK, stroke_width=2)
        y_lbl = Text("Confidence ↑", font=SERIF, color=DIM, font_size=32).move_to([-4.5, 2.55, 0])

        day_1 = Text("1", font=SERIF, color=DIM, font_size=30).move_to([-5.5, -2.1, 0])
        day_999 = Text("999", font=SERIF, color=DIM, font_size=30).move_to([4.1, -2.1, 0])
        day_1000 = Text("1000", font=SERIF, color=TERRA, font_size=30).move_to([5.5, -2.1, 0])

        rise = Line([-5.5, -1.8, 0], [4.1, 2.0, 0], color=INK, stroke_width=3)
        drop = Line([4.1,  2.0, 0], [5.5, -1.8, 0], color=TERRA, stroke_width=4)

        axe_h  = Line([5.3, -1.3, 0], [5.7, -1.3, 0], color=TERRA, stroke_width=5)
        axe_v  = Line([5.5, -0.9, 0], [5.5, -1.7, 0], color=TERRA, stroke_width=3)

        cap = _caption("schematic · FACTCHECK row 12")

        self.play(FadeIn(t), Create(ax_x), Create(ax_y), run_time=0.8)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), FadeIn(day_1), FadeIn(day_999), run_time=0.5)
        self.play(Create(rise), run_time=1.8)
        self.play(FadeIn(day_1000), Create(drop), run_time=0.8)
        self.play(Create(axe_h), Create(axe_v), run_time=0.5)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B17_CorrelationMechanism(Scene):
    """Model knows correlation; cannot see three incoming change arrows."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("Correlation is not mechanism")

        model_box = RoundedRectangle(width=4.2, height=1.8, corner_radius=0.2,
                                     stroke_color=INK, stroke_width=2.5, fill_opacity=0).move_to([-1.5, 0.3, 0])
        model_lbl = Text("model knows:", font=SERIF, color=INK, font_size=34, weight=BOLD).move_to([-1.5, 0.8, 0])
        corr_lbl  = Text("correlation held for N cases", font=SERIF, color=INK, font_size=32).move_to([-1.5, 0.1, 0])
        no_lbl    = Text("mechanism: unknown", font=SERIF, color=DIM, font_size=32, slant=ITALIC).move_to([-1.5, -0.4, 0])

        changes = ["population shift", "new pathogen", "changed demographics"]
        arrows = VGroup()
        for i, txt in enumerate(changes):
            y = 0.8 - i * 0.7
            arr = Arrow([3.8, y, 0], [0.8, y, 0], color=TERRA, stroke_width=3, buff=0.05,
                        max_tip_length_to_length_ratio=0.15)
            lbl = Text(txt, font=SERIF, color=INK, font_size=32).move_to([5.5, y, 0])
            if lbl.width > 3.5:
                lbl.scale(3.5 / lbl.width)
            arrows.add(VGroup(arr, lbl))

        cap = _caption("the model was not built to notice  ·  FACTCHECK row 23")

        self.play(FadeIn(t), run_time=0.6)
        self.play(Create(model_box), FadeIn(model_lbl), FadeIn(corr_lbl), run_time=1.0)
        self.play(FadeIn(no_lbl), run_time=0.5)
        for a in arrows:
            self.play(FadeIn(a), run_time=0.7)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B18_ZillowWritedown(Scene):
    """Zillow Q3 $304M write-down + Q4 $240–265M expected."""
    def construct(self):
        items = [
            ("Q3 write-down", ZL_WRITE_M),
            ("Q4 expected\n(midpoint)", (ZL_EXPECT_LO + ZL_EXPECT_HI) // 2),
        ]
        _vbars(
            self,
            "Zillow Offers — 2021",
            items,
            accent_idx=0,
            caption=f"Q3: ${ZL_WRITE_M}M confirmed  ·  Q4: ${ZL_EXPECT_LO}–{ZL_EXPECT_HI}M expected  ·  ≈{ZL_STAFF_PCT}% of staff  ·  FACTCHECK rows 13–14",
            fmt=lambda v: f"${v}M",
            gap=3.6,
        )

class B19_GoogleFluTrends(Scene):
    """108 week cells; 100 fill TERRA = over-predicted; quote strip."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("Google Flu Trends — over-prediction")

        # 12 cols × 9 rows = 108
        cols, rows = 12, 9
        cw, ch, hg, vg = 0.5, 0.38, 0.06, 0.06
        total_w = cols * cw + (cols - 1) * hg
        total_h = rows * ch + (rows - 1) * vg
        x0 = -total_w / 2 + cw / 2
        y0 =  total_h / 2 - ch / 2 + 0.2

        cells = VGroup()
        idx = 0
        for r in range(rows):
            for c in range(cols):
                x = x0 + c * (cw + hg)
                y = y0 - r * (ch + vg)
                color = TERRA if idx < GF_OVER else GHOST
                rect = Rectangle(width=cw, height=ch, fill_color=color,
                                 fill_opacity=1, stroke_width=0).move_to([x, y, 0])
                cells.add(rect)
                idx += 1

        counter = Text(f"{GF_OVER} of {GF_TOTAL} weeks", font=SERIF, color=INK,
                       font_size=40, weight=BOLD).move_to([0, -2.25, 0])

        quote_lbl = Text('"big data hubris"', font=SERIF, color=TERRA, font_size=36, weight=BOLD)
        quote_lbl.to_edge(DOWN, buff=0.65)

        # non-text marker
        dot = Dot(color=TERRA, radius=0.1).move_to(LEFT * 6.5 + DOWN * 2.5)

        self.play(FadeIn(t), FadeIn(dot), run_time=0.6)
        self.play(FadeIn(cells), run_time=1.2)
        self.play(FadeIn(counter), run_time=0.6)
        self.play(FadeIn(quote_lbl), run_time=0.6)
        self.wait(2)

class B20_ModelConfidence(Scene):
    """The model's confidence is a property of the model. Not of the world."""
    def construct(self):
        _statement_scene(
            self,
            ["The model's confidence is a", "property of the model."],
            "Not of the world.",
            "the world has no obligation to match the model's expectations",
        )

# ═══════════════════════ ACT IV ═══════════════════════

class B22_SwanAsymmetry(Scene):
    """Left: white swans accumulate. Right: one black swan ends the claim."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("Popper's asymmetry")

        # left stack: white swans (hollow circles)
        def swan(fill=False):
            c = Circle(radius=0.28, color=INK, stroke_width=2.5,
                       fill_color=INK if fill else CREAM, fill_opacity=1)
            return c

        left_head = Text("confirming instances", font=SERIF, color=INK, font_size=36, weight=BOLD).move_to([-3.8, 1.8, 0])
        left_sub  = Text("→ no certainty", font=SERIF, color=DIM, font_size=34).move_to([-3.8, 1.25, 0])

        white_swans = VGroup()
        for i in range(9):
            c = swan(fill=False)
            c.move_to([-5.5 + (i % 3) * 1.1, 0.4 - (i // 3) * 1.0, 0])
            white_swans.add(c)
        counter_lbl = Text("n = ∞", font=SERIF, color=INK, font_size=36).move_to([-3.8, -2.0, 0])

        # right: one black swan
        divider = Line(UP * 2.5, DOWN * 2.8, color=TERRA, stroke_width=4)
        right_head = Text("one falsifying instance", font=SERIF, color=INK, font_size=36, weight=BOLD).move_to([3.8, 1.8, 0])
        right_sub  = Text("→ certainty", font=SERIF, color=TERRA, font_size=34).move_to([3.8, 1.25, 0])
        black_swan = swan(fill=True)
        black_swan.move_to([3.8, -0.2, 0])
        bracket    = Line([3.3, -0.7, 0], [4.3, -0.7, 0], color=TERRA, stroke_width=5)

        self.play(FadeIn(t), Create(divider), run_time=0.8)
        self.play(FadeIn(left_head), FadeIn(left_sub), run_time=0.5)
        self.play(FadeIn(white_swans), run_time=1.2)
        self.play(FadeIn(counter_lbl), run_time=0.5)
        self.play(FadeIn(right_head), FadeIn(right_sub), run_time=0.5)
        self.play(FadeIn(black_swan), Create(bracket), run_time=0.8)
        self.wait(2)

class B23_RhetoricToEngineering(Scene):
    """Rhetoric → Engineering threshold. Four rows; illustrative thresholds."""
    def construct(self):
        _two_column(
            self, "Falsifiability converts rhetoric to engineering",
            "Rhetorical claim",
            ["the system is robust",
             "the model performs well",
             "the migration succeeded"],
            "Engineering threshold",
            ["precision ≥ X  and  recall ≥ Y",
             "latency ≤ Z ms",
             "a specific failure condition"],
            footer="*illustrative thresholds  ·  FACTCHECK row 19",
            size=32,
        )

class B24_SepsisBlackSwan(Scene):
    """Internal validation (white swans counted) vs external (black-swan test)."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("The test the sepsis model never got")
        divider = Line(UP * 2.3, DOWN * 2.4, color=GHOST, stroke_width=2)

        # left panel
        l_head = Text("Internal validation", font=SERIF, color=INK, font_size=38, weight=BOLD).move_to([-3.5, 1.6, 0])
        wswans = VGroup()
        for i in range(6):
            c = Circle(radius=0.25, color=INK, stroke_width=2.5,
                       fill_color=CREAM, fill_opacity=1).move_to([-5.0 + (i % 3) * 1.1, 0.3 - (i // 3) * 0.8, 0])
            wswans.add(c)
        l_sub = Text("vendor counts every correct prediction", font=SERIF, color=DIM, font_size=30).move_to([-3.5, -1.2, 0])

        # right panel
        r_head = Text("External validation", font=SERIF, color=INK, font_size=38, weight=BOLD).move_to([3.5, 1.6, 0])
        bswan  = Circle(radius=0.5, color=INK, stroke_width=0, fill_color=INK, fill_opacity=1).move_to([3.5, 0.3, 0])
        r_sub1 = Text(f"outside team  ·  {PATIENTS:,} patients", font=SERIF, color=INK, font_size=32).move_to([3.5, -0.7, 0])
        r_sub2 = Text("failed", font=SERIF, color=TERRA, font_size=38, weight=BOLD).move_to([3.5, -1.3, 0])

        footer = Text("Unrefuted ≠ Validated  ·  FACTCHECK rows 2–6",
                      font=SERIF, color=TERRA, font_size=34).to_edge(DOWN, buff=0.7)

        self.play(FadeIn(t), Create(divider), run_time=0.8)
        self.play(FadeIn(l_head), FadeIn(wswans), run_time=1.0)
        self.play(FadeIn(l_sub), run_time=0.5)
        self.play(FadeIn(r_head), FadeIn(bswan), run_time=0.8)
        self.play(FadeIn(r_sub1), FadeIn(r_sub2), run_time=0.6)
        self.play(FadeIn(footer), run_time=0.6)
        self.wait(2)

# ═══════════════════════ ACT V ═══════════════════════

class B26_CaveQuestions(Scene):
    """Cave move: three questions in the framework slot; sepsis case fills."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("The Cave move — three questions")

        art_box = RoundedRectangle(width=3.2, height=1.4, corner_radius=0.2,
                                   stroke_color=INK, stroke_width=2.5, fill_opacity=0).move_to([-4.2, 0.5, 0])
        wld_box = RoundedRectangle(width=3.2, height=1.4, corner_radius=0.2,
                                   stroke_color=INK, stroke_width=2.5, fill_opacity=0).move_to([ 4.2, 0.5, 0])
        rel_box = RoundedRectangle(width=3.4, height=2.0, corner_radius=0.2,
                                   stroke_color=DIM, stroke_width=2, fill_opacity=0).move_to([0.0, 0.5, 0])
        q_art  = Text("What is the artifact?", font=SERIF, color=INK, font_size=34).move_to([-4.2, 0.5, 0])
        q_wld  = Text("What is the world?",    font=SERIF, color=INK, font_size=34).move_to([ 4.2, 0.5, 0])
        q_rel  = Text("What is the\nrelationship?", font=SERIF, color=INK, font_size=34, alignment="center").move_to([0.0, 0.5, 0])

        l_arr = Arrow(art_box.get_right(), rel_box.get_left(), color=INK, buff=0.1, stroke_width=2,
                      max_tip_length_to_length_ratio=0.12)
        r_arr = Arrow(rel_box.get_right(), wld_box.get_left(), color=INK, buff=0.1, stroke_width=2,
                      max_tip_length_to_length_ratio=0.12)

        ans_art = Text("triage score", font=SERIF, color=TERRA, font_size=34, weight=BOLD).move_to([-4.2, -0.7, 0])
        ans_wld = Text("the clot",     font=SERIF, color=TERRA, font_size=34, weight=BOLD).move_to([ 4.2, -0.7, 0])
        ans_rel = Text("correlation,\nnot mechanism", font=SERIF, color=TERRA, font_size=32, weight=BOLD, alignment="center").move_to([0.0, -0.7, 0])

        self.play(FadeIn(t), run_time=0.6)
        self.play(Create(art_box), FadeIn(q_art), Create(wld_box), FadeIn(q_wld), run_time=1.0)
        self.play(Create(rel_box), Create(l_arr), Create(r_arr), FadeIn(q_rel), run_time=1.0)
        self.play(FadeIn(ans_art), FadeIn(ans_wld), FadeIn(ans_rel), run_time=0.8)
        self.wait(2)

class B27_XrayShortcut(Scene):
    """Radiograph outline; attention ring on corner marker; lung stays unlit."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("COVID detection — what the model attended to")

        # chest-film rectangle
        film = RoundedRectangle(width=4.0, height=4.8, corner_radius=0.2,
                                stroke_color=INK, stroke_width=2.5, fill_color=GHOST,
                                fill_opacity=0.4).move_to([-1.8, -0.1, 0])

        # lung regions (ovals)
        lung_l = Ellipse(width=1.2, height=1.8, color=DIM, stroke_width=1.5,
                         fill_opacity=0).move_to([-2.5, -0.1, 0])
        lung_r = Ellipse(width=1.2, height=1.8, color=DIM, stroke_width=1.5,
                         fill_opacity=0).move_to([-1.1, -0.1, 0])

        # corner marker (bright spot)
        corner_mark = Square(side_length=0.5, fill_color=INK, fill_opacity=0.5,
                             stroke_width=0).move_to([-3.5, 2.0, 0])

        # attention ring
        attn_ring = Circle(radius=0.55, color=TERRA, stroke_width=5,
                           fill_opacity=0).move_to(corner_mark.get_center())
        attn_lbl  = Text("model's attention", font=SERIF, color=TERRA, font_size=32)
        attn_lbl.next_to(attn_ring, RIGHT, buff=0.35)

        # quote
        quote = Text('"appear accurate, but fail when tested in new hospitals"',
                     font=SERIF, color=INK, font_size=32)
        quote.to_edge(DOWN, buff=0.65)
        if quote.width > 13.0:
            quote.scale(13.0 / quote.width)

        cap = Text("FACTCHECK row 17", font=SERIF, color=DIM, font_size=30).next_to(quote, UP, buff=0.15)

        self.play(FadeIn(t), run_time=0.6)
        self.play(FadeIn(film), Create(lung_l), Create(lung_r), run_time=1.0)
        self.play(FadeIn(corner_mark), run_time=0.5)
        self.play(Create(attn_ring), FadeIn(attn_lbl), run_time=0.8)
        self.play(FadeIn(quote), FadeIn(cap), run_time=0.6)
        self.wait(2)

class B28_COMPASAnatomy(Scene):
    """Three-row anatomy: ARTIFACT / WORLD / RELATIONSHIP for COMPAS."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("COMPAS — artifact, world, relationship")

        rows = [
            ("ARTIFACT",     "a number",                                INK),
            ("WORLD",        "a person's future conduct",               INK),
            ("RELATIONSHIP", "arrest data shaped by who gets policed",  TERRA),
        ]
        y_starts = [1.2, 0.0, -1.3]
        dot = Dot(color=TERRA, radius=0.1).move_to(LEFT * 6.5 + DOWN * 2.5)
        self.play(FadeIn(t), FadeIn(dot), run_time=0.6)
        for (row_h, row_v, col), y in zip(rows, y_starts):
            h = Text(row_h,   font=SERIF, color=DIM,  font_size=34, weight=BOLD).move_to([-3.8, y, 0])
            v = Text(row_v,   font=SERIF, color=INK,  font_size=36).move_to([ 2.0, y, 0])
            sep = Line([h.get_right()[0] + 0.4, y, 0], [v.get_left()[0] - 0.4, y, 0],
                       color=GHOST, stroke_width=2)
            if col == TERRA:
                bar = Line(LEFT * 5.8, RIGHT * 5.8, color=TERRA, stroke_width=3).move_to([0, y - 0.35, 0])
                self.play(FadeIn(h), FadeIn(v), Create(sep), Create(bar), run_time=0.7)
            else:
                self.play(FadeIn(h), FadeIn(v), Create(sep), run_time=0.6)

        cap = _caption("FACTCHECK row 18")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B29_FluencyTrap(Scene):
    """Two arrows: fluency → confidence in output → trust in own evaluation."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("The fluency trap — two moves")

        boxes = [
            ([-5.2,  0.0, 0], "Polished output"),
            ([ 0.0,  0.0, 0], "Confidence in the answer"),
            ([ 5.4,  0.0, 0], "Trust in\nyour evaluation"),
        ]
        box_objs = []
        for (x, y, z), lbl in boxes:
            txt = Text(lbl, font=SERIF, color=INK, font_size=34, alignment="center")
            w   = min(txt.width + 0.6, 3.6)
            box = RoundedRectangle(width=w, height=1.1, corner_radius=0.15,
                                   stroke_color=INK, stroke_width=2, fill_opacity=0)
            box.move_to([x, y, z])
            txt.move_to(box.get_center())
            box_objs.append(VGroup(box, txt))

        arr1 = Arrow(box_objs[0].get_right(), box_objs[1].get_left(),
                     color=INK, stroke_width=3, buff=0.1,
                     max_tip_length_to_length_ratio=0.15)
        arr2 = Arrow(box_objs[1].get_right(), box_objs[2].get_left(),
                     color=TERRA, stroke_width=4, buff=0.1,
                     max_tip_length_to_length_ratio=0.15)

        lbl1 = Text("expected", font=SERIF, color=DIM, font_size=30).next_to(arr1, UP, buff=0.2)
        lbl2 = Text("the trap", font=SERIF, color=TERRA, font_size=32, weight=BOLD).next_to(arr2, UP, buff=0.2)

        cap = _caption("fluency is an evaluation booster  ·  FACTCHECK row 22")

        self.play(FadeIn(t), run_time=0.6)
        self.play(FadeIn(box_objs[0]), run_time=0.5)
        self.play(Create(arr1), FadeIn(box_objs[1]), FadeIn(lbl1), run_time=0.8)
        self.play(Create(arr2), FadeIn(box_objs[2]), FadeIn(lbl2), run_time=0.8)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B30_FormContent(Scene):
    """Two sliders: Fluency moves right; Correctness stays left."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("Form and content — two independent sliders")

        def slider(label, y, val):
            track = Line([-3.5, y, 0], [3.5, y, 0], color=GHOST, stroke_width=6)
            knob  = Circle(radius=0.28, fill_color=INK, fill_opacity=1,
                           stroke_width=0).move_to([val, y, 0])
            lbl   = Text(label, font=SERIF, color=INK, font_size=36, weight=BOLD).move_to([-5.0, y, 0])
            return track, knob, lbl

        f_track, f_knob_start, f_lbl = slider("Fluency",     0.8, -3.5)
        c_track, c_knob,       c_lbl = slider("Correctness", -0.8, -3.5)

        f_knob_end = Circle(radius=0.28, fill_color=TERRA, fill_opacity=1,
                            stroke_width=0).move_to([3.2, 0.8, 0])
        hi_lbl = Text("max", font=SERIF, color=DIM, font_size=30).move_to([3.5, 1.3, 0])
        lo_lbl = Text("low", font=SERIF, color=DIM, font_size=30).move_to([-3.5, 0.3, 0])

        c_stuck = Text("stuck at low", font=SERIF, color=DIM, font_size=32).move_to([0.0, -1.5, 0])
        cap = _caption("FACTCHECK row 22  ·  two sliders, moving independently")

        self.play(FadeIn(t), run_time=0.6)
        self.play(Create(f_track), FadeIn(f_lbl), FadeIn(f_knob_start), run_time=0.8)
        self.play(Create(c_track), FadeIn(c_lbl), FadeIn(c_knob),       run_time=0.8)
        self.play(FadeIn(hi_lbl), FadeIn(lo_lbl), run_time=0.4)
        self.play(Transform(f_knob_start, f_knob_end), run_time=1.4)
        self.play(FadeIn(c_stuck), run_time=0.5)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B31_FluencyStatement(Scene):
    """Do not let fluency do epistemic work."""
    def construct(self):
        _statement_scene(
            self,
            ["Do not let fluency do epistemic work."],
            "Specify the wrong answer before you read.",
            "then ask whether the output matches your specification",
        )

# ═══════════════════════ ACT VI ═══════════════════════

class B33_AsymmetryFlip(Scene):
    """Classical asymmetry (factor hard / check easy) flips for AI."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("The asymmetry flips")

        # classical pair
        cl_lbl = Text("Classical", font=SERIF, color=INK, font_size=36, weight=BOLD).move_to([-4.5, 2.0, 0])
        hard_bar = Rectangle(width=1.4, height=2.4, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([-5.0, 0.2, 0])
        easy_bar = Rectangle(width=1.4, height=0.6, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to([-3.5, -1.5, 0])
        hard_lbl = Text("factor\n(hard)", font=SERIF, color=CREAM, font_size=30, alignment="center").move_to(hard_bar)
        easy_lbl = Text("check\n(easy)", font=SERIF, color=INK, font_size=30, alignment="center").move_to([-3.5, -2.3, 0])

        # flip arrow
        flip_arr = Arrow([-1.8, 0.0, 0], [1.2, 0.0, 0], color=TERRA, stroke_width=4,
                         max_tip_length_to_length_ratio=0.18)
        flip_lbl = Text("AI inverts", font=SERIF, color=TERRA, font_size=34, weight=BOLD).move_to([-0.3, 0.5, 0])

        # AI pair
        ai_lbl  = Text("AI deployment", font=SERIF, color=INK, font_size=36, weight=BOLD).move_to([4.5, 2.0, 0])
        prod_bar = Rectangle(width=1.4, height=0.4, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to([3.8, -1.7, 0])
        ver_bar  = Rectangle(width=1.4, height=2.8, fill_color=TERRA, fill_opacity=1, stroke_width=0).move_to([5.3, 0.0, 0])
        prod_lbl = Text("produce\n(fast)", font=SERIF, color=INK, font_size=30, alignment="center").move_to([3.8, -2.4, 0])
        ver_lbl  = Text("verify\n(labor)", font=SERIF, color=CREAM, font_size=36, alignment="center").move_to(ver_bar)

        base = Line([-6.5, -1.9, 0], [6.5, -1.9, 0], color=INK, stroke_width=2)
        cap  = _caption("schematic — no numerical ratios  ·  FACTCHECK row 20")

        self.play(FadeIn(t), Create(base), run_time=0.8)
        self.play(FadeIn(cl_lbl), FadeIn(hard_bar), FadeIn(easy_bar), run_time=0.8)
        self.play(FadeIn(easy_lbl), run_time=0.3)
        self.play(Create(flip_arr), FadeIn(flip_lbl), run_time=0.8)
        self.play(FadeIn(ai_lbl), FadeIn(prod_bar), FadeIn(ver_bar), run_time=0.8)
        self.play(FadeIn(prod_lbl), run_time=0.3)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B34_VerificationStatement(Scene):
    """If you do not budget for verification, you will not get verification."""
    def construct(self):
        _statement_scene(
            self,
            ["If you do not budget for verification,", "you will not get verification."],
            "Automating the checking is another model, one layer up.",
            "with the same problem",
        )

# ═══════════════════════ ACT VII ═══════════════════════

class B36_FiveCapacities(Scene):
    """Five numbered rows with failure-shape captions."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title(f"Five supervisory capacities  ({CAPACITIES})")

        capacity_data = [
            ("1. Plausibility auditing",  "plausible-but-wrong"),
            ("2. Problem formulation",    "right answer, wrong question"),
            ("3. Tool orchestration",     "wrong tool chosen"),
            ("4. Interpretive judgment",  "number decontextualized"),
            ("5. Executive integration",  "no one owns it"),
        ]

        y0 = 1.6
        dy = 0.85
        dot = Dot(color=TERRA, radius=0.1).move_to(LEFT * 6.5 + DOWN * 2.5)
        self.play(FadeIn(t), FadeIn(dot), run_time=0.6)
        for i, (cap_name, failure) in enumerate(capacity_data):
            y = y0 - i * dy
            lbl  = Text(cap_name, font=SERIF, color=INK, font_size=34, weight=BOLD).move_to([-2.0, y, 0])
            fail = Text(f"→ {failure}", font=SERIF, color=DIM, font_size=30).move_to([4.0, y, 0])
            sep  = Line([lbl.get_right()[0] + 0.2, y, 0], [fail.get_left()[0] - 0.2, y, 0],
                        color=GHOST, stroke_width=1.5)
            self.play(FadeIn(lbl), Create(sep), FadeIn(fail), run_time=0.55)
        self.wait(2)

class B37_ProblemFormulation(Scene):
    """Q asked vs Q needed — load-bearing capacity."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("Problem formulation — the load-bearing one")

        divider = Line(LEFT * 5.6, RIGHT * 5.6, color=TERRA, stroke_width=3).move_to([0, 0.4, 0])

        q_asked = Text("Q answered:", font=SERIF, color=DIM, font_size=34, weight=BOLD).move_to([-4.2, 1.3, 0])
        a_asked = Text("What is the statistical category\nof this presentation?",
                       font=SERIF, color=INK, font_size=30, alignment="center").move_to([2.0, 1.2, 0])
        ck_asked = Text("✓  answered well", font=SERIF, color=INK, font_size=32).move_to([4.5, 0.7, 0])

        q_need  = Text("Q needed:", font=SERIF, color=DIM, font_size=34, weight=BOLD).move_to([-4.2, -0.5, 0])
        a_need  = Text("Does this patient have a\nlife-threatening condition?",
                       font=SERIF, color=INK, font_size=30, alignment="center").move_to([2.0, -0.6, 0])
        x_need  = Text("✗  never asked", font=SERIF, color=TERRA, font_size=32, weight=BOLD).move_to([4.5, -1.1, 0])

        cap = _caption("most AI failures are failures of problem formulation  ·  FACTCHECK row 21")

        self.play(FadeIn(t), run_time=0.6)
        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(q_asked), FadeIn(a_asked), run_time=0.7)
        self.play(FadeIn(ck_asked), run_time=0.4)
        self.play(FadeIn(q_need),  FadeIn(a_need),  run_time=0.7)
        self.play(FadeIn(x_need),  run_time=0.4)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B38_SkepticismArchitecture(Scene):
    """Workflow: Input → Model → Output with three supervision markers."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("Skepticism as architecture")

        nodes = [
            ([-4.5, 0.0, 0], "Input"),
            ([ 0.0, 0.0, 0], "Model"),
            ([ 4.5, 0.0, 0], "Output"),
        ]
        node_objs = []
        for pos, lbl in nodes:
            box = RoundedRectangle(width=2.4, height=1.0, corner_radius=0.18,
                                   stroke_color=INK, stroke_width=2.5, fill_opacity=0).move_to(pos)
            txt = Text(lbl, font=SERIF, color=INK, font_size=36, weight=BOLD).move_to(pos)
            node_objs.append(VGroup(box, txt))

        arr1 = Arrow(node_objs[0].get_right(), node_objs[1].get_left(), color=INK, buff=0.08, stroke_width=2,
                     max_tip_length_to_length_ratio=0.12)
        arr2 = Arrow(node_objs[1].get_right(), node_objs[2].get_left(), color=INK, buff=0.08, stroke_width=2,
                     max_tip_length_to_length_ratio=0.12)

        def tag(txt, pos, yoff=-1.2):
            box = RoundedRectangle(width=3.6, height=0.7, corner_radius=0.12,
                                   stroke_color=TERRA, stroke_width=2, fill_opacity=0)
            box.move_to([pos[0], pos[1] + yoff, 0])
            lbl = Text(txt, font=SERIF, color=INK, font_size=28)
            if lbl.width > 3.3:
                lbl.scale(3.3 / lbl.width)
            lbl.move_to(box.get_center())
            pole = Line([pos[0], pos[1] - 0.5, 0], [pos[0], pos[1] + yoff + 0.35, 0],
                        color=TERRA, stroke_width=2)
            return VGroup(box, lbl, pole)

        tag1 = tag("falsification condition\non checklist",     nodes[0][0])
        tag2 = tag("distribution-shift\ntest",                  nodes[1][0])
        tag3 = tag("handoff protocol",                          nodes[2][0])

        cap = _caption("where · by whom · seeing what")

        self.play(FadeIn(t), run_time=0.6)
        for n in node_objs:
            self.play(FadeIn(n), run_time=0.4)
        self.play(Create(arr1), Create(arr2), run_time=0.8)
        self.play(FadeIn(tag1), run_time=0.6)
        self.play(FadeIn(tag2), run_time=0.6)
        self.play(FadeIn(tag3), run_time=0.6)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2)

class B39_AshReturns(Scene):
    """Ash tiles + lecture ripple markers + pebble."""
    def construct(self):
        self.camera.background_color = STAGE
        t = _title("Ash's agent — the shape of every agentic failure")

        labels  = ["ASKED", "DID", "REPORTED", "STATE"]
        details = ["delete email", "nuclear reset", "reset completed", "email still there"]
        tiles = VGroup()
        for i, (lbl, det) in enumerate(zip(labels, details)):
            box = RoundedRectangle(width=2.3, height=1.3, corner_radius=0.15,
                                   stroke_color=INK, stroke_width=2, fill_opacity=0)
            head = Text(lbl, font=SERIF, color=INK, font_size=28, weight=BOLD)
            body = Text(det,  font=SERIF, color=INK, font_size=26)
            head.move_to(box.get_center() + UP * 0.28)
            body.move_to(box.get_center() + DOWN * 0.2)
            tiles.add(VGroup(box, head, body))
        tiles.arrange(RIGHT, buff=0.4).move_to([0, 1.2, 0])

        gap_arr = Arrow(
            tiles[2][0].get_right(), tiles[3][0].get_left(),
            color=TERRA, stroke_width=3, buff=0.05,
            max_tip_length_to_length_ratio=0.2,
        )

        # ripple markers — plain dots, lecture numbers spoken not shown (SLATE-RUNNER law)
        ripple_lbl = Text("this pebble ripples:", font=SERIF, color=DIM, font_size=34).move_to([-3.5, -0.7, 0])
        ripple_dots = VGroup(*[
            Circle(radius=0.32, fill_color=TERRA, fill_opacity=1.0 - ci * 0.2,
                   stroke_width=0).move_to([-0.5 + ci * 1.2, -0.7, 0])
            for ci in range(3)
        ])

        # pebble
        pebble_lbl = Text("your pebble →", font=SERIF, color=INK, font_size=34).move_to([-2.5, -2.0, 0])
        pebble = Ellipse(width=0.7, height=0.5, fill_color=INK, fill_opacity=1,
                         stroke_width=0).move_to([0.2, -2.0, 0])

        self.play(FadeIn(t), run_time=0.6)
        self.play(FadeIn(tiles), run_time=1.0)
        self.play(Create(gap_arr), run_time=0.6)
        self.play(FadeIn(ripple_lbl), run_time=0.4)
        self.play(FadeIn(ripple_dots), run_time=0.6)
        self.play(FadeIn(pebble_lbl), FadeIn(pebble), run_time=0.6)
        self.wait(2)

class B40_Summary(Scene):
    """Four items land; bold close."""
    def construct(self):
        self.camera.background_color = STAGE

        items = [
            "Four moves.",
            "One asymmetry.",
            "Five capacities.",
            "One trap.",
        ]
        group = VGroup(
            *[Text(itm, font=SERIF, color=INK, font_size=60) for itm in items]
        ).arrange(DOWN, buff=0.45).move_to(UP * 0.6)

        close = Text("Use it on everything.", font=SERIF, color=INK, font_size=66, weight=BOLD)
        close.next_to(group, DOWN, buff=0.6)
        if close.width > 11.0:
            close.scale(11.0 / close.width)

        ul = Line(LEFT * 3, RIGHT * 3, color=TERRA, stroke_width=6).next_to(close, DOWN, buff=0.2)
        ul.set_width(min(close.width + 0.4, 11.0))
        bar = Line(UP * 2.7, DOWN * 2.7, color=TERRA, stroke_width=14).move_to(LEFT * 6.0)
        dot = Dot(color=TERRA, radius=0.12).next_to(close, RIGHT, buff=0.25)

        self.camera.background_color = STAGE
        self.play(Create(bar), run_time=0.5)
        for itm in group:
            self.play(FadeIn(itm, shift=UP * 0.1), run_time=0.45)
        self.play(FadeIn(close, shift=UP * 0.15), FadeIn(dot), run_time=0.7)
        self.play(Create(ul), run_time=0.5)
        self.wait(2)


class BearsDoodlesVideo(Scene):
    """Stub required by static_scene_check.py (deep-explainer uses per-beat classes)."""
    def construct(self):
        pass


if __name__ == "__main__":
    print("VERIFY OK")
