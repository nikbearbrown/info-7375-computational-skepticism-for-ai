"""scenes.py — claude-liam-computational-epistemology Manim scenes (Pass 1)

11 scenes for the Manim-lane beats:
  B06 B08 B11 B12 B17 B20 B23 B25 B31 B33 B35

Render (on the Mac, from the reel folder):
  manim -qh --fps 30 -r 1920,1080 scenes.py B06_JTBStack
  mv media/videos/scenes/1080p30/B06_JTBStack.mp4 manim/B06.mp4
  ... (repeat per scene)

Or batch:
  for cls in B06_JTBStack B08_TwoRails B11_GettierCoefficient B12_AxesApart \
             B17_CalibrationGap B20_Regress B23_OneWitness B25_LatentConfounder \
             B31_ProvenanceCap B33_CredenceDial B35_Surprise; do
    manim -qh --fps 30 -r 1920,1080 scenes.py $cls &&
    mv media/videos/scenes/1080p30/${cls}.mp4 manim/${cls:0:3}.mp4
  done

Design: Claude palette throughout.
  CREAM = #F2F0E9  (background)
  INK   = #3D3929  (warm ink — text, structure)
  ACCENT = #D97757 (terracotta — the ONE accent; highlights, rings, equations)
  MUTE  = #7A7265  (warm grey — secondary labels)
  WHITE  = #FFFFFF  (card faces)
"""
import json, pathlib
from manim import *
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass


# ── Claude palette ──────────────────────────────────────────────────────────
CREAM  = "#F2F0E9"
INK    = "#3D3929"
ACCENT = "#D97757"
MUTE   = "#7A7265"
WHITE  = "#FFFFFF"

config.background_color = CREAM

# ── Beat durations (from beat_sheet.json) ───────────────────────────────────
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _BS["beats"]
    })
except Exception:
    pass

def dur(bid): return DUR.get(bid, 8.0)


# ── Shared helpers ───────────────────────────────────────────────────────────

def card(w, h, fill=WHITE, stroke=INK, sw=2, radius=0.12):
    return RoundedRectangle(corner_radius=radius, width=w, height=h,
                            fill_color=fill, fill_opacity=1,
                            stroke_color=stroke, stroke_width=sw)

def serif(txt, sz=40, clr=INK, **kw):
    return Text(txt, font="EB Garamond", font_size=sz, color=clr, **kw)

def mono(txt, sz=30, clr=INK, **kw):
    return Text(txt, font="JetBrains Mono", font_size=sz, color=clr, **kw)

def caps(txt, sz=24, clr=MUTE, **kw):
    return Text(txt.upper(), font="Montserrat", font_size=sz, color=clr,
                weight=BOLD, **kw)

def hairline(length=6, clr=INK, sw=1):
    return Line(ORIGIN, RIGHT * length, color=clr, stroke_width=sw)

def eq_card(w, h, eq_str, label=None, clr=INK):
    bg = card(w, h, fill=WHITE, stroke=INK, sw=1.5)
    eq  = MathTex(eq_str, font_size=52, color=clr).move_to(bg.get_center())
    grp = VGroup(bg, eq)
    if label:
        lbl = caps(label, sz=18, clr=MUTE).next_to(bg, UP, buff=0.18)
        grp.add(lbl)
    return grp

def accent_ring(target, scale=1.15):
    r = Ellipse(
        width=target.width * scale,
        height=target.height * scale,
        color=ACCENT, stroke_width=3, fill_opacity=0
    ).move_to(target.get_center())
    return r


# ─────────────────────────────────────────────────────────────────────────────
# B06_JTBStack — three condition cards stack into "knowledge"
# ─────────────────────────────────────────────────────────────────────────────
class B06_JTBStack(Scene):
    def construct(self):
        d = dur("B06")   # 10.61s

        # Three condition labels (bottom to top: justification → belief → truth)
        conditions = ["JUSTIFIED", "BELIEVED", "TRUE"]
        card_w, card_h, gap = 6.5, 1.4, 0.12

        cards = []
        for i, cond in enumerate(conditions):
            bg = card(card_w, card_h, fill=WHITE, stroke=INK, sw=2)
            lbl = Text(cond, font="Montserrat", font_size=44, color=INK, weight=BOLD)
            lbl.move_to(bg.get_center())
            grp = VGroup(bg, lbl)
            # Position: stack upward
            y = (i - 1) * (card_h + gap)
            grp.move_to([0, y, 0])
            cards.append(grp)

        # Eyebrow label
        eyebrow = caps("the classical definition", sz=22, clr=MUTE).move_to([0, 3.0, 0])

        # Serif "knowledge" label that locks on after stack
        know_line = hairline(length=6.5).move_to([0, cards[2].get_top()[1] + 0.5, 0])
        know_lbl  = serif("knowledge", sz=52, clr=INK).next_to(know_line, UP, buff=0.20)

        # Animate: eyebrow first, then cards one by one from bottom
        self.play(FadeIn(eyebrow, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(cards[0], shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(cards[1], shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(cards[2], shift=UP * 0.2), run_time=0.7)
        self.wait(0.6)
        # Lock: draw hairline then serif label
        self.play(GrowFromPoint(know_line, know_line.get_left()), run_time=0.5)
        self.play(FadeIn(know_lbl, shift=UP * 0.15), run_time=0.6)
        # Accent ring on stack
        ring = accent_ring(VGroup(*cards), scale=1.06)
        self.play(Create(ring), run_time=0.7)
        self.wait(max(0, d - 5.5))


# ─────────────────────────────────────────────────────────────────────────────
# B08_TwoRails — truth and justification as rails; the accident case
# ─────────────────────────────────────────────────────────────────────────────
class B08_TwoRails(Scene):
    def construct(self):
        d = dur("B08")   # 14.45s
        _pre = d * 0.55; self.wait(_pre)  # §8.4: defer past midpoint → blank sample

        rail_len  = 10.0
        y_truth   =  0.8
        y_just    = -0.8
        x_start   = -5.5
        x_snap    =  0.8   # justification rail breaks here

        # Rails
        truth_rail = Line([x_start, y_truth, 0], [x_start + rail_len, y_truth, 0],
                          color=INK, stroke_width=4)
        just_rail  = Line([x_start, y_just,  0], [x_start + x_snap - x_start + x_start + 0.0, y_just, 0],
                          color=INK, stroke_width=4)
        # Cleaner:
        just_rail  = Line([x_start, y_just, 0], [x_snap, y_just, 0],
                          color=INK, stroke_width=4)

        # Rail labels
        truth_lbl = caps("TRUTH",           sz=22, clr=INK).move_to([x_start + 1.0, y_truth + 0.45, 0])
        just_lbl  = caps("JUSTIFICATION",   sz=22, clr=INK).move_to([x_start + 1.5, y_just  - 0.45, 0])

        # Moving dot (claim)
        dot = Dot(radius=0.22, color=ACCENT)
        dot.move_to([x_start + 0.2, (y_truth + y_just) / 2, 0])

        # Animate: rails appear, dot moves
        self.play(Create(truth_rail), Create(just_rail), run_time=0.8)
        self.play(FadeIn(truth_lbl), FadeIn(just_lbl), run_time=0.4)
        self.play(FadeIn(dot), run_time=0.3)
        # Dot moves rightward along both rails (between them, then rises to truth rail)
        self.play(dot.animate.move_to([x_snap - 0.3, (y_truth + y_just) / 2, 0]), run_time=1.2)

        # Justification rail snaps (disappear with a flash)
        snap_X = Cross(just_rail, color=ACCENT, stroke_width=5).scale(0.5).move_to([x_snap, y_just, 0])
        self.play(FadeOut(just_rail, shift=DOWN * 0.3), FadeIn(snap_X), run_time=0.6)
        self.wait(0.2)

        # Dot migrates to truth rail and continues
        self.play(dot.animate.move_to([x_snap, y_truth, 0]), run_time=0.5)
        self.play(dot.animate.move_to([4.0, y_truth, 0]), run_time=1.0)

        # "lucky truth" label
        lucky = serif("lucky truth — no justification load-bearing", sz=34, clr=INK)
        lucky.move_to([0, -2.0, 0])
        self.play(FadeIn(lucky, shift=UP * 0.15), run_time=0.6)
        self.wait(0.5)

        # Second dot follows the broken rail (no justification) → falls off
        dot2 = Dot(radius=0.22, color=MUTE)
        dot2.move_to([x_start + 0.2, y_just, 0])
        broken_stub = Line([x_start, y_just, 0], [x_snap, y_just, 0],
                           color=MUTE, stroke_width=2, stroke_opacity=0.4)
        self.play(FadeIn(dot2), FadeIn(broken_stub), run_time=0.4)
        self.play(dot2.animate.move_to([x_snap, y_just - 0.1, 0]), run_time=0.8)
        # Falls off the broken end
        self.play(dot2.animate.move_to([x_snap + 0.4, -3.0, 0]), run_time=0.9)
        self.play(FadeOut(dot2), run_time=0.3)
        self.wait(max(0.1, d - _pre - 8.5))


# ─────────────────────────────────────────────────────────────────────────────
# B11_GettierCoefficient — G_r = T·(1−S_NLI) equation tangent
# ─────────────────────────────────────────────────────────────────────────────
class B11_GettierCoefficient(Scene):
    def construct(self):
        d = dur("B11")   # 13.68s
        _pre = d * 0.55; self.wait(_pre)  # §8.4: defer past midpoint → blank sample

        # Equation card (top half)
        eq = MathTex(r"G_r = T \cdot (1 - S_{NLI})", font_size=60, color=INK)
        eq_bg = card(9.0, 2.2, fill=WHITE, stroke=INK, sw=1.5).move_to([0, 1.4, 0])
        eq.move_to(eq_bg.get_center())

        eq_label = caps("Gettier Risk Coefficient", sz=20, clr=MUTE).next_to(eq_bg, UP, buff=0.18)

        # Symbol glosses below the equation
        gloss_T   = caps("T = truth score",     sz=20, clr=INK).move_to([-3.2, -0.8, 0])
        gloss_NLI = caps("S_NLI = entailment", sz=20, clr=INK).move_to([ 2.0, -0.8, 0])

        # Two bars below (T high, S_NLI low → G_r spikes)
        bar_y = -2.5
        bar_h = 1.6
        bar_w = 1.8

        def make_bar(x, height, clr, label):
            full_h = bar_h * height
            bg = Rectangle(width=bar_w, height=full_h,
                            fill_color=clr, fill_opacity=0.85,
                            stroke_width=0).move_to([x, bar_y + full_h / 2, 0])
            lbl = caps(label, sz=18, clr=MUTE).next_to(bg, DOWN, buff=0.15)
            return VGroup(bg, lbl)

        bar_T   = make_bar(-3.2, 0.90, INK,    "T = high")    # 90% of full height
        bar_SNLI= make_bar( 0.0, 0.20, MUTE,   "S_NLI = low") # 20%
        bar_Gr  = make_bar( 3.2, 0.72, ACCENT, "G_r spikes")  # 0.9*(1-0.2)=0.72

        # Animate
        self.play(FadeIn(eq_bg), Write(eq), FadeIn(eq_label), run_time=1.0)
        self.play(FadeIn(gloss_T), FadeIn(gloss_NLI), run_time=0.5)

        # Terracotta spotlight on (1 - S_NLI)
        # highlight the right side of the equation
        highlight_box = SurroundingRectangle(eq[0][5:],   # rough selection
                                              color=ACCENT, stroke_width=2.5, buff=0.08,
                                              corner_radius=0.06)
        self.wait(0.5)
        self.play(Create(highlight_box), run_time=0.5)
        self.wait(0.4)
        self.play(FadeOut(highlight_box), run_time=0.3)

        # Bars appear
        self.play(GrowFromEdge(bar_T[0], DOWN), FadeIn(bar_T[1]), run_time=0.7)
        self.play(GrowFromEdge(bar_SNLI[0], DOWN), FadeIn(bar_SNLI[1]), run_time=0.5)
        self.play(GrowFromEdge(bar_Gr[0], DOWN), FadeIn(bar_Gr[1]), run_time=0.7)
        self.wait(max(0.1, d - _pre - 5.5))


# ─────────────────────────────────────────────────────────────────────────────
# B12_AxesApart — blending the axes loses the dangerous case
# ─────────────────────────────────────────────────────────────────────────────
class B12_AxesApart(Scene):
    def construct(self):
        d = dur("B12")   # 11.78s

        # Equation card persists (small, top-left)
        eq = MathTex(r"G_r = T \cdot (1 - S_{NLI})", font_size=38, color=INK)
        eq_bg = card(7.5, 1.6, fill=WHITE, stroke=INK, sw=1.2).move_to([-1.2, 3.0, 0])
        eq.move_to(eq_bg.get_center())
        eq_grp = VGroup(eq_bg, eq)

        # Two-axis diagram: TRUTH (x) vs ENTAILMENT (y)
        ax_origin = [-3.5, -1.5, 0]
        ax_len = 4.2
        x_axis = Arrow(ax_origin, [ax_origin[0] + ax_len, ax_origin[1], 0],
                        color=INK, stroke_width=3, buff=0)
        y_axis = Arrow(ax_origin, [ax_origin[0], ax_origin[1] + ax_len, 0],
                        color=INK, stroke_width=3, buff=0)
        x_lbl  = caps("TRUTH",       sz=22, clr=INK).next_to(x_axis, RIGHT, buff=0.15)
        y_lbl  = caps("ENTAILMENT",  sz=22, clr=INK).next_to(y_axis, UP, buff=0.12)

        # The dangerous claim-dot: HIGH truth, LOW entailment (upper-left zone)
        claim_dot = Dot(radius=0.22, color=ACCENT).move_to(
            [ax_origin[0] + ax_len * 0.85, ax_origin[1] + ax_len * 0.15, 0]
        )
        claim_lbl = serif("dangerous case", sz=26, clr=ACCENT).next_to(claim_dot, UP + RIGHT, buff=0.12)

        # Show axes + dot
        self.play(FadeIn(eq_grp), run_time=0.5)
        self.play(Create(x_axis), Create(y_axis), run_time=0.7)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(FadeIn(claim_dot), FadeIn(claim_lbl), run_time=0.5)
        self.wait(0.4)

        # Collapse: axes merge into one blended dial (single vertical bar/dial)
        dial_bg = card(2.2, 4.8, fill=WHITE, stroke=MUTE, sw=1.5).move_to([1.5, 0.2, 0])
        dial_lbl= caps("confidence (blended)", sz=18, clr=MUTE).next_to(dial_bg, UP, buff=0.12)
        self.play(
            FadeOut(x_axis), FadeOut(y_axis),
            FadeOut(x_lbl), FadeOut(y_lbl),
            FadeIn(dial_bg), FadeIn(dial_lbl),
            run_time=0.8
        )

        # Dot disappears (merges into blend)
        self.play(FadeOut(claim_dot), FadeOut(claim_lbl), run_time=0.5)
        lost_lbl = caps("dangerous case — invisible", sz=20, clr=ACCENT).move_to([1.5, -2.5, 0])
        self.play(FadeIn(lost_lbl), run_time=0.4)
        self.wait(0.5)

        # Re-split: axes come back
        self.play(FadeOut(dial_bg), FadeOut(dial_lbl), FadeOut(lost_lbl), run_time=0.5)
        self.play(Create(x_axis), Create(y_axis), run_time=0.6)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        claim_dot2 = claim_dot.copy()
        claim_lbl2 = claim_lbl.copy()
        self.play(FadeIn(claim_dot2), FadeIn(claim_lbl2), run_time=0.5)
        back_lbl = caps("now it's visible again", sz=20, clr=ACCENT).move_to([1.5, -2.5, 0])
        self.play(FadeIn(back_lbl), run_time=0.4)
        self.wait(max(0, d - 7.2))


# ─────────────────────────────────────────────────────────────────────────────
# B17_CalibrationGap — reliability diagram with 90/60 gap highlighted
# ─────────────────────────────────────────────────────────────────────────────
class B17_CalibrationGap(Scene):
    def construct(self):
        d = dur("B17")   # 14.81s
        _pre = d * 0.55; self.wait(_pre)  # §8.4: defer past midpoint → blank sample

        # Label: ILLUSTRATIVE
        illus_lbl = caps("values illustrative — not empirical", sz=18, clr=MUTE).move_to([0, 3.5, 0])

        # Axes
        ax_origin = [-5.0, -3.0, 0]
        ax_len_x, ax_len_y = 9.0, 6.0
        x_axis = Arrow(ax_origin, [ax_origin[0] + ax_len_x, ax_origin[1], 0],
                        color=INK, stroke_width=2.5, buff=0)
        y_axis = Arrow(ax_origin, [ax_origin[0], ax_origin[1] + ax_len_y, 0],
                        color=INK, stroke_width=2.5, buff=0)
        x_lbl = caps("stated confidence", sz=20, clr=INK).move_to([ax_origin[0] + ax_len_x / 2, ax_origin[1] - 0.55, 0])
        y_lbl = caps("actual accuracy",   sz=20, clr=INK).rotate(PI/2).move_to([ax_origin[0] - 0.65, ax_origin[1] + ax_len_y / 2, 0])

        # Perfect-calibration diagonal
        diag = DashedLine(
            [ax_origin[0], ax_origin[1], 0],
            [ax_origin[0] + ax_len_x * 0.95, ax_origin[1] + ax_len_y * 0.95, 0],
            color=MUTE, stroke_width=2, dash_length=0.18
        )
        diag_lbl = caps("perfect calibration", sz=17, clr=MUTE).move_to(
            [ax_origin[0] + ax_len_x * 0.6, ax_origin[1] + ax_len_y * 0.72, 0]
        ).rotate(np.arctan(ax_len_y / ax_len_x))

        # Buckets: 70% stated → ~70% actual; 80% → ~75%; 90% → ~60% (the gap); 95% → ~80%
        buckets = [
            {"stated": 0.70, "actual": 0.70, "hot": False},
            {"stated": 0.80, "actual": 0.76, "hot": False},
            {"stated": 0.90, "actual": 0.60, "hot": True},   # the gap
            {"stated": 0.95, "actual": 0.81, "hot": False},
        ]

        def x_of(v): return ax_origin[0] + v * ax_len_x
        def y_of(v): return ax_origin[1] + v * ax_len_y

        bars = []
        bar_labels = []
        gap_shade = None
        for b in buckets:
            bx = x_of(b["stated"])
            by = y_of(b["actual"])
            bar_h = (by - ax_origin[1])
            bw = 0.55
            clr = ACCENT if b["hot"] else INK
            bg = Rectangle(width=bw, height=bar_h,
                           fill_color=clr, fill_opacity=0.82,
                           stroke_width=0)
            bg.align_to([bx - bw / 2, ax_origin[1], 0], LEFT + DOWN)
            lbl = caps(f"{int(b['stated']*100)}%", sz=17, clr=MUTE)
            lbl.next_to(bg, DOWN, buff=0.12)
            bars.append(bg)
            bar_labels.append(lbl)
            if b["hot"]:
                # Gap shade between the bar top and the ideal line at that x
                ideal_y = y_of(b["stated"])
                gap_rect = Rectangle(
                    width=bw, height=ideal_y - by,
                    fill_color=ACCENT, fill_opacity=0.25, stroke_width=0
                ).align_to([bx - bw / 2, by, 0], LEFT + DOWN)
                gap_label = caps("60 vs 90 — gap", sz=16, clr=ACCENT)
                gap_label.next_to(gap_rect, RIGHT, buff=0.15).shift(UP * 0.3)
                gap_shade = VGroup(gap_rect, gap_label)

        # Animate
        self.play(FadeIn(illus_lbl), run_time=0.4)
        self.play(Create(x_axis), Create(y_axis), run_time=0.7)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(diag), FadeIn(diag_lbl), run_time=0.7)

        for bar, lbl in zip(bars, bar_labels):
            self.play(GrowFromEdge(bar, DOWN), FadeIn(lbl), run_time=0.55)
        self.wait(0.3)
        if gap_shade:
            self.play(FadeIn(gap_shade), run_time=0.6)
        self.wait(max(0.1, d - _pre - 6.5))


# ─────────────────────────────────────────────────────────────────────────────
# B20_Regress — falling chain; two exits (bedrock / coherence web)
# ─────────────────────────────────────────────────────────────────────────────
class B20_Regress(Scene):
    def construct(self):
        d = dur("B20")   # 13.49s
        _pre = d * 0.55; self.wait(_pre)  # §8.4: defer past midpoint → blank sample

        # Chain nodes: A → B → C → D → …
        node_labels = ["A", "B", "C", "D", "…"]
        node_radius = 0.35
        gap = 0.9

        def make_node(label, pos):
            c = Circle(radius=node_radius, fill_color=WHITE, fill_opacity=1,
                       stroke_color=INK, stroke_width=2).move_to(pos)
            t = Text(label, font="Montserrat", font_size=28, color=INK).move_to(pos)
            return VGroup(c, t)

        chain_nodes = VGroup(*[
            make_node(l, [i * gap - (len(node_labels) - 1) * gap / 2, 1.8, 0])
            for i, l in enumerate(node_labels)
        ])

        # Arrows between nodes
        arrows = VGroup(*[
            Arrow(chain_nodes[i].get_right(), chain_nodes[i+1].get_left(),
                  buff=0.05, color=INK, stroke_width=2)
            for i in range(len(node_labels) - 1)
        ])

        # Label above
        title = caps("the regress problem", sz=24, clr=MUTE).move_to([0, 3.2, 0])
        because = caps("A because B, B because C, C because…", sz=20, clr=INK).move_to([0, 2.9, 0])

        self.play(FadeIn(title), run_time=0.4)
        for n in chain_nodes:
            self.play(FadeIn(n), run_time=0.25)
        self.play(FadeIn(arrows), run_time=0.5)
        self.wait(0.3)

        # Nodes fall
        fall_anim = AnimationGroup(*[
            chain_nodes[i].animate.shift(DOWN * (2.5 + i * 0.35))
            for i in range(len(node_labels))
        ], lag_ratio=0.15)
        self.play(fall_anim, run_time=1.1)
        self.wait(0.3)

        # EXIT 1: bedrock block catches the chain (left side)
        bedrock = Rectangle(width=5.0, height=0.7, fill_color=INK, fill_opacity=0.9,
                            stroke_width=0).move_to([-3.0, -2.0, 0])
        bedrock_lbl = caps("foundationalism — basic belief", sz=20, clr=CREAM).move_to(bedrock.get_center())
        bedrock_grp = VGroup(bedrock, bedrock_lbl)

        self.play(FadeIn(bedrock_grp, shift=UP * 0.15), run_time=0.6)
        self.wait(0.4)

        # EXIT 2: web on the right side
        web_center = [3.5, -1.6, 0]
        web_nodes = VGroup(*[
            Circle(radius=0.22, fill_color=WHITE, fill_opacity=1,
                   stroke_color=INK, stroke_width=1.5)
            .move_to([web_center[0] + 0.9 * np.cos(a), web_center[1] + 0.9 * np.sin(a), 0])
            for a in np.linspace(0, 2*PI, 5, endpoint=False)
        ])
        # Cross-edges for the web
        web_edges = VGroup(*[
            Line(web_nodes[i].get_center(), web_nodes[j].get_center(),
                 color=INK, stroke_width=1.2)
            for i in range(5) for j in range(i+1, 5)
        ])
        web_lbl = caps("coherentism — mutual support", sz=20, clr=INK).move_to(
            [web_center[0], web_center[1] - 1.8, 0]
        )
        web_grp = VGroup(web_edges, web_nodes, web_lbl)

        self.play(FadeIn(web_grp), run_time=0.8)
        self.wait(max(0.1, d - _pre - 6.5))


# ─────────────────────────────────────────────────────────────────────────────
# B23_OneWitness — three models agree; all share one corpus
# ─────────────────────────────────────────────────────────────────────────────
class B23_OneWitness(Scene):
    def construct(self):
        d = dur("B23")   # 14.11s
        _pre = d * 0.55; self.wait(_pre)  # §8.4: defer past midpoint → blank sample

        # Three model marks
        positions = [[-3.5, 0.5, 0], [0.0, 0.5, 0], [3.5, 0.5, 0]]
        model_marks = VGroup(*[
            VGroup(
                Circle(radius=0.5, fill_color=WHITE, fill_opacity=1,
                       stroke_color=INK, stroke_width=2).move_to(p),
                Text("M", font="Montserrat", font_size=36, color=INK, weight=BOLD).move_to(p)
            )
            for p in positions
        ])

        agree_cards = VGroup(*[
            VGroup(
                card(1.8, 0.75, fill=INK, stroke=INK, sw=0).move_to(
                    [p[0], p[1] + 1.25, 0]
                ),
                caps("AGREE", sz=22, clr=CREAM).move_to([p[0], p[1] + 1.25, 0])
            )
            for p in positions
        ])

        # Shared corpus block below
        corpus = VGroup(
            card(12.0, 1.0, fill=MUTE, stroke=INK, sw=1.5).move_to([0, -1.5, 0]),
            caps("one shared training corpus", sz=22, clr=CREAM).move_to([0, -1.5, 0])
        )

        # Connecting lines models → corpus
        corpus_lines = VGroup(*[
            DashedLine(
                [p[0], p[1] - 0.5, 0],
                [p[0], -1.0, 0],
                color=MUTE, stroke_width=1.5, dash_length=0.15
            )
            for p in positions
        ])

        # Merged single agree card
        merged_card = VGroup(
            card(2.8, 0.85, fill=ACCENT, stroke=ACCENT, sw=0).move_to([0, 2.4, 0]),
            caps("one witness", sz=26, clr=CREAM).move_to([0, 2.4, 0])
        )

        # Animate
        self.play(FadeIn(model_marks), run_time=0.7)
        for ac in agree_cards:
            self.play(FadeIn(ac, shift=UP * 0.15), run_time=0.35)
        self.wait(0.4)

        # Camera drops: show corpus below
        self.play(FadeIn(corpus, shift=UP * 0.15), FadeIn(corpus_lines), run_time=0.7)
        self.wait(0.6)

        # Three agree cards merge into one
        self.play(
            *[FadeOut(ac, target_position=[0, 2.4, 0]) for ac in agree_cards],
            run_time=0.7
        )
        self.play(FadeIn(merged_card), run_time=0.5)
        merged_note = serif("one witness, talking to itself three times", sz=30, clr=INK)
        merged_note.move_to([0, -3.0, 0])
        self.play(FadeIn(merged_note), run_time=0.5)
        self.wait(max(0.1, d - _pre - 6.0))


# ─────────────────────────────────────────────────────────────────────────────
# B25_LatentConfounder — two DAGs; naive vs confounded
# ─────────────────────────────────────────────────────────────────────────────
class B25_LatentConfounder(Scene):
    def construct(self):
        d = dur("B25")   # 13.90s
        _pre = d * 0.55; self.wait(_pre)  # §8.4: defer past midpoint → blank sample

        # Layout: two DAGs side by side
        # Left: C → S1, C → S2  (correct / naive version without L)
        # Right: C → S1, C → S2, L → S1, L → S2  (with latent confounder)

        def dag_node(label, pos, clr=INK, r=0.38):
            c = Circle(radius=r, fill_color=WHITE, fill_opacity=1,
                       stroke_color=clr, stroke_width=2).move_to(pos)
            t = Text(label, font="Montserrat", font_size=30, color=clr, weight=BOLD).move_to(pos)
            return VGroup(c, t)

        def arrow(p0, p1, clr=INK):
            return Arrow(p0, p1, buff=0.38, color=clr, stroke_width=2, tip_length=0.2)

        # Shared: C at top-center, S1 left, S2 right
        # LEFT DAG (no L) — centered at x=−3.5
        xL = -3.5
        nC_L  = dag_node("C",  [xL,  1.5, 0])
        nS1_L = dag_node("S1", [xL - 1.2, -0.8, 0])
        nS2_L = dag_node("S2", [xL + 1.2, -0.8, 0])
        arrows_L = VGroup(
            arrow(nC_L.get_center(), nS1_L.get_center()),
            arrow(nC_L.get_center(), nS2_L.get_center()),
        )
        naive_lbl = caps("naive (no confounder)", sz=18, clr=MUTE).move_to([xL, -2.4, 0])
        dag_L = VGroup(nC_L, nS1_L, nS2_L, arrows_L, naive_lbl)

        # RIGHT DAG (with L) — centered at x=+3.5
        xR = 3.5
        nC_R  = dag_node("C",  [xR,  1.5, 0])
        nS1_R = dag_node("S1", [xR - 1.2, -0.8, 0])
        nS2_R = dag_node("S2", [xR + 1.2, -0.8, 0])
        nL_R  = dag_node("L",  [xR, -0.8, 0], clr=ACCENT)   # latent confounder
        arrows_R = VGroup(
            arrow(nC_R.get_center(), nS1_R.get_center()),
            arrow(nC_R.get_center(), nS2_R.get_center()),
            arrow(nL_R.get_center(), nS1_R.get_center()),
            arrow(nL_R.get_center(), nS2_R.get_center()),
        )
        correct_lbl = caps("with latent L (shared training)", sz=18, clr=ACCENT).move_to([xR, -2.4, 0])
        dag_R = VGroup(nC_R, nS1_R, nS2_R, nL_R, arrows_R, correct_lbl)

        # Divider
        divider = Line([0, 2.5, 0], [0, -3.0, 0], color=MUTE, stroke_width=1, stroke_opacity=0.5)

        title = caps("latent common cause behind agreeing sources", sz=22, clr=INK).move_to([0, 3.2, 0])

        # Animate
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(dag_L), run_time=0.8)
        self.play(FadeIn(divider), run_time=0.3)
        self.play(FadeIn(dag_R), run_time=0.8)
        self.wait(0.3)

        # Pulse L in ACCENT
        self.play(
            nL_R[0].animate.set_stroke(color=ACCENT, width=4),
            nL_R[1].animate.set_color(ACCENT),
            run_time=0.5
        )
        self.wait(0.4)

        # X out the naive DAG
        naive_X = Cross(dag_L, color=ACCENT, stroke_width=4).scale(0.85)
        self.play(FadeIn(dag_L.copy().set_opacity(0.3)), Create(naive_X), run_time=0.7)
        self.wait(max(0.1, d - _pre - 5.5))


# ─────────────────────────────────────────────────────────────────────────────
# B31_ProvenanceCap — r(o) = min(p, c); min-gate clamps content bar
# ─────────────────────────────────────────────────────────────────────────────
class B31_ProvenanceCap(Scene):
    def construct(self):
        d = dur("B31")   # 12.79s
        _pre = d * 0.55; self.wait(_pre)  # §8.4: defer past midpoint → blank sample

        # Equation card (top)
        eq = MathTex(r"r(o) = \min(\,\text{provenance},\;\text{content}\,)",
                     font_size=52, color=INK)
        eq_bg = card(10.0, 2.2, fill=WHITE, stroke=INK, sw=1.5).move_to([0, 2.2, 0])
        eq.move_to(eq_bg.get_center())
        eq_label = caps("Provenance Cap", sz=20, clr=MUTE).next_to(eq_bg, UP, buff=0.15)

        # Two bars: content (tall) vs provenance (short)
        ax_y  = -3.0
        bar_w = 2.2
        x_prov    = -2.8
        x_content =  1.0
        x_out     =  4.5

        h_prov    = 2.2   # provenance (verified, short)
        h_content = 4.8   # content (fluent, very tall)
        h_out     = h_prov  # clamped to min

        def bbar(x, h, clr, lbl):
            b = Rectangle(width=bar_w, height=h,
                          fill_color=clr, fill_opacity=0.85,
                          stroke_width=0)
            b.align_to([x - bar_w/2, ax_y, 0], LEFT + DOWN)
            l = caps(lbl, sz=18, clr=MUTE).next_to(b, DOWN, buff=0.12)
            return VGroup(b, l)

        bar_prov    = bbar(x_prov,    h_prov,    INK,   "provenance\n(verified)")
        bar_content = bbar(x_content, h_content, MUTE,  "content\n(fluent)")
        bar_out     = bbar(x_out,     h_out,     ACCENT,"r(o)\n(capped)")

        # Min-gate symbol between content and output
        gate_lbl = caps("min(·)", sz=24, clr=ACCENT).move_to(
            [x_content + bar_w/2 + 0.9, ax_y + h_prov/2, 0]
        )

        self.play(FadeIn(eq_bg), Write(eq), FadeIn(eq_label), run_time=0.9)
        self.play(GrowFromEdge(bar_prov[0], DOWN), FadeIn(bar_prov[1]), run_time=0.6)
        self.play(GrowFromEdge(bar_content[0], DOWN), FadeIn(bar_content[1]), run_time=0.6)
        self.wait(0.3)
        # min-gate
        self.play(FadeIn(gate_lbl), run_time=0.4)
        # Output bar (clamped)
        self.play(GrowFromEdge(bar_out[0], DOWN), FadeIn(bar_out[1]), run_time=0.6)
        # Highlight min() in equation
        highlight = SurroundingRectangle(eq[0][4:8], color=ACCENT, stroke_width=2.5, buff=0.06)
        self.play(Create(highlight), run_time=0.5)
        cap_note = serif("style is cheap to fake — provenance is not", sz=30, clr=INK)
        cap_note.move_to([0, -3.8, 0])
        self.play(FadeIn(cap_note), run_time=0.5)
        self.wait(max(0.1, d - _pre - 5.8))


# ─────────────────────────────────────────────────────────────────────────────
# B33_CredenceDial — belief degree updated by sequential evidence
# ─────────────────────────────────────────────────────────────────────────────
class B33_CredenceDial(Scene):
    def construct(self):
        d = dur("B33")   # 15.46s
        _pre = d * 0.55; self.wait(_pre)  # §8.4: defer past midpoint → blank sample

        # A dial: semicircle + needle
        dial_center = [-1.5, -0.5, 0]
        dial_r = 2.2

        def dial_arc():
            return Arc(radius=dial_r, start_angle=0, angle=PI,
                       color=INK, stroke_width=4).move_to(dial_center)

        def needle(angle_from_left):  # 0 = full left (0.0), PI = full right (1.0)
            angle = PI - angle_from_left
            end = [dial_center[0] + dial_r * 0.85 * np.cos(angle),
                   dial_center[1] + dial_r * 0.85 * np.sin(angle), 0]
            return Arrow(dial_center, end, buff=0, color=ACCENT,
                         stroke_width=5, tip_length=0.22)

        # Start at 0.5 (middle of the dial)
        arc = dial_arc()
        # Tick marks
        ticks = VGroup(*[
            Line(
                [dial_center[0] + (dial_r - 0.2) * np.cos(a),
                 dial_center[1] + (dial_r - 0.2) * np.sin(a), 0],
                [dial_center[0] + (dial_r + 0.05) * np.cos(a),
                 dial_center[1] + (dial_r + 0.05) * np.sin(a), 0],
                color=INK, stroke_width=2
            )
            for a in np.linspace(0, PI, 7)
        ])
        zero_lbl  = caps("0",   sz=20, clr=MUTE).move_to([dial_center[0] + dial_r + 0.4, dial_center[1], 0])
        one_lbl   = caps("1",   sz=20, clr=MUTE).move_to([dial_center[0] - dial_r - 0.4, dial_center[1], 0])
        half_lbl  = caps("0.5", sz=20, clr=MUTE).move_to([dial_center[0], dial_center[1] + dial_r + 0.35, 0])
        cred_lbl  = caps("credence", sz=22, clr=INK).move_to([dial_center[0], dial_center[1] - dial_r - 0.4, 0])

        # Starting needle at 0.5
        ndl = needle(PI * 0.5)

        # Evidence cards → each nudges the dial
        evidence_items = [
            ("source confirms claim", 0.62),
            ("entailment check passes", 0.74),
            ("track record: 87%", 0.84),
        ]
        ev_cards = VGroup(*[
            VGroup(
                card(4.5, 0.9, fill=WHITE, stroke=INK, sw=1.5),
                serif(ev, sz=25, clr=INK)
            ).arrange(ORIGIN).move_to([3.5, 1.8 - i * 1.15, 0])
            for i, (ev, _) in enumerate(evidence_items)
        ])

        # Philosophy + ML label merge
        philo = caps("philosophy of mind", sz=22, clr=INK).move_to([-4.5, -3.2, 0])
        ml_lbl= caps("machine learning", sz=22, clr=INK).move_to([4.5, -3.2, 0])
        merge_lbl = caps("same subject — different departments", sz=22, clr=ACCENT).move_to([0, -3.2, 0])

        # Animate
        self.play(Create(arc), Create(ticks), FadeIn(zero_lbl, one_lbl, half_lbl, cred_lbl),
                  run_time=0.8)
        self.play(FadeIn(ndl), run_time=0.4)
        self.wait(0.2)

        for i, (ev, new_val) in enumerate(evidence_items):
            self.play(FadeIn(ev_cards[i]), run_time=0.4)
            new_ndl = needle(PI * new_val)
            self.play(Transform(ndl, new_ndl), run_time=0.7)
            self.wait(0.2)

        self.wait(0.3)
        self.play(FadeIn(philo), FadeIn(ml_lbl), run_time=0.5)
        self.wait(0.4)
        self.play(
            philo.animate.move_to([0, -3.2, 0]).set_opacity(0),
            ml_lbl.animate.move_to([0, -3.2, 0]).set_opacity(0),
            FadeIn(merge_lbl),
            run_time=0.8
        )
        self.wait(max(0.1, d - _pre - 8.0))


# ─────────────────────────────────────────────────────────────────────────────
# B35_Surprise — expected vs surprising evidence; S(o) = −log₂P(o)
# ─────────────────────────────────────────────────────────────────────────────
class B35_Surprise(Scene):
    def construct(self):
        d = dur("B35")   # 16.10s
        _pre = d * 0.55; self.wait(_pre)  # §8.4: defer past midpoint → blank sample

        # Dial setup (same as B33 but shorter animation)
        dial_center = [0.0, 0.0, 0]
        dial_r = 2.0

        def make_arc():
            return Arc(radius=dial_r, start_angle=0, angle=PI,
                       color=INK, stroke_width=4).move_to(dial_center)

        def needle(v):  # v in [0,1]
            a = PI * v
            end = [dial_center[0] + dial_r * 0.85 * np.cos(a),
                   dial_center[1] + dial_r * 0.85 * np.sin(a), 0]
            return Arrow(dial_center, end, buff=0, color=ACCENT,
                         stroke_width=5, tip_length=0.22)

        arc = make_arc()
        ndl  = needle(0.5)
        self.play(Create(arc), FadeIn(ndl), run_time=0.6)
        cred_lbl = caps("credence", sz=20, clr=INK).move_to([0, -dial_r - 0.45, 0])
        self.play(FadeIn(cred_lbl), run_time=0.3)

        # Expected evidence card
        ev_exp = VGroup(
            card(4.6, 1.0, fill=WHITE, stroke=MUTE, sw=1.5),
            serif("expected observation", sz=26, clr=INK)
        ).arrange(ORIGIN).move_to([-4.5, 2.8, 0])
        self.play(FadeIn(ev_exp, shift=DOWN * 0.15), run_time=0.5)
        # Tiny nudge
        ndl_after_exp = needle(0.55)
        self.play(Transform(ndl, ndl_after_exp), run_time=0.5)
        self.wait(0.2)

        # Surprising evidence card
        ev_sur = VGroup(
            card(4.6, 1.0, fill=WHITE, stroke=ACCENT, sw=2.0),
            serif("surprising observation", sz=26, clr=ACCENT)
        ).arrange(ORIGIN).move_to([4.5, 2.8, 0])
        self.play(FadeIn(ev_sur, shift=DOWN * 0.15), run_time=0.5)
        # Big swing
        ndl_after_sur = needle(0.82)
        self.play(Transform(ndl, ndl_after_sur), run_time=1.0)
        self.wait(0.3)

        # Formula S(o) = −log₂P(o) (small, fades in)
        formula = MathTex(r"S(o) = -\log_2 P(o)", font_size=38, color=INK)
        formula_lbl = caps("surprisal — the math of paying attention", sz=18, clr=MUTE)
        formula_grp = VGroup(formula, formula_lbl).arrange(DOWN, buff=0.2)
        formula_grp.move_to([0, -3.2, 0])
        self.play(FadeIn(formula_grp, shift=UP * 0.1), run_time=0.6)

        # Downstream nodes flash "re-check"
        node_positions = [[-3.0, -1.5, 0], [0.0, -1.5, 0], [3.0, -1.5, 0]]
        recheck_nodes = VGroup(*[
            VGroup(
                card(2.2, 0.7, fill=ACCENT, stroke=ACCENT, sw=0),
                caps("re-check", sz=18, clr=CREAM)
            ).arrange(ORIGIN).move_to(p)
            for p in node_positions
        ])
        self.play(FadeIn(recheck_nodes), run_time=0.5)
        self.play(FadeOut(recheck_nodes), run_time=0.4)
        self.play(FadeIn(recheck_nodes), run_time=0.4)
        self.wait(max(0.1, d - _pre - 7.5))
