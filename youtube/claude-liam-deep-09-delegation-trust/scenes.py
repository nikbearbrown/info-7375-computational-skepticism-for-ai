"""scenes.py — Manim scenes for claude-liam-deep-09-delegation-trust
("It Runs Beautifully. Nobody's Watching.").

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent per scene).
No slant=ITALIC on multi-word text (Pango collapses spaces).
Eight Manim body beats: A1M A2M A3M A4M A4M2 A5M A6M A6M2.
"""
from manim import *
import json, pathlib, numpy as np
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass


# ── Palette ────────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")   # terracotta — ONE accent per scene
SOFT  = ManimColor("#7B7563")
GHOST = ManimColor("#B8B3A2")
CARD  = ManimColor("#FFFFFF")
OK    = ManimColor("#5B7A4E")   # green for "good" states
WARN  = ManimColor("#A04040")   # muted red for "bad" / broken states

config.background_color = BG

# ── Duration table ─────────────────────────────────────────────────────────────
DUR = {k: 12.0 for k in ["A1M","A2M","A3M","A4M","A4M2","A5M","A6M","A6M2",
                           "A2V","A4V"]}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 12.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _lbl(text, size=36, color=None, weight=None):
    kw = {"font_size": size, "color": color or INK}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw, font='EB Garamond')


def _cite(text, size=13):
    return Text(text, font_size=size, color=SOFT, font='EB Garamond')


def _wait_out(self, used, total, min_hold=0.3):
    remaining = max(min_hold, total - used)
    self.wait(remaining)


# ─────────────────────────────────────────────────────────────────────────────
#  A1M — Responsibility Trace
#  Two identical pipelines side by side; an accountability arrow traced through
#  each. Team 1's arrow dead-ends at an undefined "reviews" node (terracotta).
#  Team 2's arrow lands on a named human node.
# ─────────────────────────────────────────────────────────────────────────────
class A1M_ResponsibilityTrace(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A1M"]
        used = 0.0

        # Title
        title = _lbl("Who Is Responsible?", size=36, weight="BOLD").move_to([0, 3.2, 0])
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # Column headers
        h1 = _lbl("TEAM 1", size=36, color=SOFT, weight="BOLD").move_to([-3.4, 2.5, 0])
        h2 = _lbl("TEAM 2", size=36, color=SOFT, weight="BOLD").move_to([3.4, 2.5, 0])
        self.play(FadeIn(h1), FadeIn(h2), run_time=0.25)
        used += 0.25

        # Pipeline nodes — left side (Team 1)
        node_names_1 = ["AI", "Score", "Officer", "reviews"]
        node_names_2 = ["AI", "Score", "Officer", "Named Human"]
        ys = [1.6, 0.6, -0.4, -1.4]
        x1, x2 = -3.4, 3.4

        def _node(x, y, label, accent=False):
            clr = INK  # always INK border/text for contrast compliance
            box = RoundedRectangle(width=2.4, height=0.52, corner_radius=0.12,
                                   stroke_color=clr, stroke_width=1.8,
                                   fill_color=BG, fill_opacity=1.0).move_to([x, y, 0])
            txt = _lbl(label, size=36, color=INK).move_to([x, y, 0])
            return VGroup(box, txt)

        nodes1 = VGroup(*[_node(x1, y, n) for n, y in zip(node_names_1, ys)])
        nodes2 = VGroup(*[_node(x2, y, n) for n, y in zip(node_names_2, ys)])

        # Draw shared nodes first (AI, Score, Officer)
        for i in range(3):
            self.play(FadeIn(nodes1[i]), FadeIn(nodes2[i]), run_time=0.22)
            used += 0.22

        # Arrows between shared nodes
        def _arr(x, y_start, y_end, color=None):
            return Arrow(
                [x, y_start - 0.3, 0], [x, y_end + 0.3, 0],
                buff=0, color=color or GHOST, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.2,
            )

        arrs1 = VGroup(*[_arr(x1, ys[i], ys[i+1]) for i in range(2)])
        arrs2 = VGroup(*[_arr(x2, ys[i], ys[i+1]) for i in range(2)])
        self.play(FadeIn(arrs1), FadeIn(arrs2), run_time=0.3)
        used += 0.3

        # Fourth node: accountability arrow traces down
        # Team 1 — dead-end arrow + "reviews" node in terracotta + X
        arr1_final = _arr(x1, ys[2], ys[3], color=WARN)
        self.play(Create(arr1_final), run_time=0.4)
        used += 0.4

        n1_dead = _node(x1, ys[3], "reviews", accent=True)
        self.play(FadeIn(n1_dead), run_time=0.3)
        used += 0.3

        # Question mark / dead-end indicator
        qmark = _lbl("? undefined", size=36, color=INK).move_to([x1, ys[3] - 0.7, 0])
        self.play(FadeIn(qmark), run_time=0.3)
        used += 0.3

        # Team 2 — arrow lands on Named Human (good, terracotta for contrast)
        arr2_final = _arr(x2, ys[2], ys[3], color=OK)
        self.play(Create(arr2_final), run_time=0.4)
        used += 0.4

        n2_good = _node(x2, ys[3], "Named Human")
        n2_good[0].set_stroke(color=INK)
        n2_good[1].set_color(INK)
        self.play(FadeIn(n2_good), run_time=0.3)
        used += 0.3

        # Verdict labels
        dead_lbl = _lbl("dead-ends at a word", size=36, color=INK).move_to([x1, -2.5, 0])
        lands_lbl = _lbl("lands on a person", size=36, color=INK).move_to([x2, -2.5, 0])
        self.play(FadeIn(dead_lbl), FadeIn(lands_lbl), run_time=0.35)
        used += 0.35

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A2M — Testable Handoff
#  Top: "reasonable result / human reviews" fans into 5 behavior branches.
#  Bottom: "score 0–1, accept/re-score/override, 4 codes" collapses to one row.
#  Terracotta on the one auditable row.
# ─────────────────────────────────────────────────────────────────────────────
class A2M_TestableHandoff(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A2M"]
        used = 0.0

        # Title
        title = _lbl("Testable vs Untestable Handoff", size=36, weight="BOLD").move_to([0, 3.2, 0])
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # ── UNTESTABLE (top half) ─────────────────────────────────────────────
        untestable_hdr = _lbl("UNTESTABLE", size=36, color=INK, weight="BOLD").move_to([0, 2.4, 0])
        self.play(FadeIn(untestable_hdr), run_time=0.25)
        used += 0.25

        # Root box
        root_box = RoundedRectangle(width=4.0, height=0.52, corner_radius=0.12,
                                    stroke_color=SOFT, stroke_width=1.5,
                                    fill_color=BG, fill_opacity=1.0).move_to([0, 1.7, 0])
        root_txt = _lbl("reasonable result / human reviews", size=28, color=SOFT).move_to([0, 1.7, 0])
        root = VGroup(root_box, root_txt)
        self.play(FadeIn(root), run_time=0.3)
        used += 0.3

        # Five fan branches
        branch_labels = ["waves through", "spot-checks 1", "re-reads twice", "checks domain", "escalates all"]
        branch_xs = np.linspace(-5.0, 5.0, 5)
        branch_y = 0.3

        for i, (label, bx) in enumerate(zip(branch_labels, branch_xs)):
            arr = Arrow([0, 1.4, 0], [bx, branch_y + 0.3, 0],
                        buff=0, color=GHOST, stroke_width=1.5,
                        max_tip_length_to_length_ratio=0.3)
            lbl = _lbl(label, size=28, color=SOFT).move_to([bx, branch_y - 0.15, 0])
            self.play(Create(arr), FadeIn(lbl), run_time=0.22)
            used += 0.22

        no_fact = _lbl("no fact of the matter", size=36, color=INK).move_to([0, -0.35, 0])
        self.play(FadeIn(no_fact), run_time=0.3)
        used += 0.3

        # ── TESTABLE (bottom half) ────────────────────────────────────────────
        sep = Line([-6.0, -0.8, 0], [6.0, -0.8, 0], color=GHOST, stroke_width=1.5)
        self.play(Create(sep), run_time=0.25)
        used += 0.25

        testable_hdr = _lbl("TESTABLE", size=36, color=INK, weight="BOLD").move_to([0, -1.2, 0])
        self.play(FadeIn(testable_hdr), run_time=0.25)
        used += 0.25

        # Three condition fragments
        cond_y = -1.85
        conditions = ["score 0–1", "accept / re-score / override", "one of four codes"]
        cond_xs = [-3.8, 0.0, 3.8]
        cond_objs = VGroup(*[_lbl(c, size=28, color=SOFT).move_to([x, cond_y, 0])
                              for c, x in zip(conditions, cond_xs)])
        self.play(FadeIn(cond_objs), run_time=0.35)
        used += 0.35

        # Converge to one log row (terracotta — the ONE accent)
        conv_arrs = VGroup(*[Arrow([x, cond_y - 0.25, 0], [0, -2.85, 0],
                                   buff=0, color=GHOST, stroke_width=1.5,
                                   max_tip_length_to_length_ratio=0.3)
                              for x in cond_xs])
        self.play(FadeIn(conv_arrs), run_time=0.3)
        used += 0.3

        log_box = RoundedRectangle(width=4.8, height=0.52, corner_radius=0.12,
                                   stroke_color=INK, stroke_width=2.0,
                                   fill_color=BG, fill_opacity=1.0).move_to([0, -3.2, 0])
        log_txt = _lbl("one auditable log row", size=36, color=INK, weight="BOLD").move_to([0, -3.2, 0])
        self.play(FadeIn(log_box), FadeIn(log_txt), run_time=0.35)
        used += 0.35

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A3M — Broken vs Unsupervised
#  Two horizontal pipelines. "Broken" halts at a red gap. "Unsupervised" flows
#  smoothly while a silent error propagates; terracotta on downstream harm.
# ─────────────────────────────────────────────────────────────────────────────
class A3M_BrokenVsUnsupervised(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A3M"]
        used = 0.0

        # Title
        title = _lbl("Broken vs Unsupervised", size=36, weight="BOLD").move_to([0, 3.2, 0])
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # ── BROKEN pipeline (top) ─────────────────────────────────────────────
        row_broken = 1.4
        row_uns    = -0.8

        hdr_b = _lbl("BROKEN (items 1-4 missing)", size=36, color=INK, weight="BOLD").move_to([-1.5, row_broken + 0.85, 0])
        hdr_u = _lbl("UNSUPERVISED (items 5-8 missing)", size=36, color=INK, weight="BOLD").move_to([-0.7, row_uns + 0.85, 0])
        self.play(FadeIn(hdr_b), FadeIn(hdr_u), run_time=0.3)
        used += 0.3

        def _pipeline_nodes(y, n=4, gap_at=None):
            nodes = VGroup()
            xs = np.linspace(-5.5, 2.0, n)
            for i, x in enumerate(xs):
                clr = WARN if (gap_at is not None and i == gap_at) else GHOST
                box = RoundedRectangle(width=1.6, height=0.5, corner_radius=0.1,
                                       stroke_color=clr, stroke_width=1.5,
                                       fill_color=BG, fill_opacity=1.0).move_to([x, y, 0])
                nodes.add(box)
            return nodes, xs

        # Broken pipeline nodes + gap
        nodes_b, xs_b = _pipeline_nodes(row_broken, gap_at=2)
        for i in range(2):
            arr = Arrow([xs_b[i] + 0.85, row_broken, 0], [xs_b[i+1] - 0.85, row_broken, 0],
                        buff=0, color=GHOST, stroke_width=2,
                        max_tip_length_to_length_ratio=0.25)
            self.play(FadeIn(nodes_b[i]), Create(arr), run_time=0.22)
            used += 0.22

        # Red gap / X — the pipeline halts here
        x_gap = xs_b[2]
        gap_x = RoundedRectangle(width=1.6, height=0.5, corner_radius=0.1,
                                  stroke_color=WARN, stroke_width=2.5,
                                  fill_color=BG, fill_opacity=1.0).move_to([x_gap, row_broken, 0])
        gap_lbl = _lbl("MISSING", size=36, color=INK, weight="BOLD").move_to([x_gap, row_broken, 0])
        halt_lbl = _lbl("HALT", size=36, color=INK, weight="BOLD").move_to([x_gap + 1.5, row_broken + 0.55, 0])
        self.play(FadeIn(gap_x), FadeIn(gap_lbl), FadeIn(halt_lbl), run_time=0.4)
        used += 0.4

        # ── UNSUPERVISED pipeline (bottom) ────────────────────────────────────
        nodes_u, xs_u = _pipeline_nodes(row_uns, n=5)

        # All 5 nodes flow smoothly
        for i in range(4):
            arr = Arrow([xs_u[i] + 0.85, row_uns, 0], [xs_u[i+1] - 0.85, row_uns, 0],
                        buff=0, color=GHOST, stroke_width=2,
                        max_tip_length_to_length_ratio=0.25)
            self.play(FadeIn(nodes_u[i]), Create(arr), run_time=0.18)
            used += 0.18
        self.play(FadeIn(nodes_u[4]), run_time=0.18)
        used += 0.18

        # Silent error token appears at node 2, propagates downstream
        err_token = Circle(radius=0.18, fill_color=INK, stroke_width=0, fill_opacity=0.9)
        err_token.move_to([xs_u[2], row_uns + 0.4, 0])
        err_lbl = _lbl("error", size=36, color=INK).next_to(err_token, UP, buff=0.05)
        self.play(FadeIn(err_token), FadeIn(err_lbl), run_time=0.3)
        used += 0.3

        # Propagate to the right (toward downstream user)
        self.play(
            err_token.animate.move_to([xs_u[4], row_uns + 0.4, 0]),
            err_lbl.animate.move_to([xs_u[4], row_uns + 0.72, 0]),
            run_time=0.9, rate_func=rate_functions.linear
        )
        used += 0.9

        # Downstream harm — terracotta
        harm_box = RoundedRectangle(width=2.2, height=0.52, corner_radius=0.12,
                                    stroke_color=INK, stroke_width=2.0,
                                    fill_color=BG, fill_opacity=1.0).move_to([4.8, row_uns, 0])
        harm_txt = _lbl("harmed user", size=36, color=INK).move_to([4.8, row_uns, 0])
        harm_arr = Arrow([xs_u[4] + 0.85, row_uns, 0], [4.8 - 1.2, row_uns, 0],
                          buff=0, color=INK, stroke_width=2.0,
                          max_tip_length_to_length_ratio=0.25)
        self.play(Create(harm_arr), FadeIn(harm_box), FadeIn(harm_txt), run_time=0.4)
        used += 0.4

        # Verdict spark-line
        spark = _lbl("Broken announces. Unsupervised runs quietly.",
                     size=36, color=INK).move_to([0, -2.4, 0])
        self.play(FadeIn(spark), run_time=0.35)
        used += 0.35

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A4M — Reversibility Gate
#  Reversible actions (draft) flow freely. Irreversible (delete/send/wire)
#  arrive at a closed gate that only a human hand opens. Contrast: VOTE vs GATE.
#  Terracotta on the gate.
# ─────────────────────────────────────────────────────────────────────────────
class A4M_ReversibilityGate(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A4M"]
        used = 0.0

        # Title
        title = _lbl("Gate, Not Vote", size=36, weight="BOLD").move_to([0, 3.2, 0])
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # ── REVERSIBLE lane (top) ─────────────────────────────────────────────
        rev_y = 1.3

        rev_hdr = _lbl("REVERSIBLE  (high error rate OK)", size=36, color=INK).move_to([-1.8, rev_y + 0.55, 0])
        self.play(FadeIn(rev_hdr), run_time=0.25)
        used += 0.25

        draft_box = RoundedRectangle(width=1.8, height=0.5, corner_radius=0.12,
                                     stroke_color=SOFT, stroke_width=1.5,
                                     fill_color=BG, fill_opacity=1.0).move_to([-5.0, rev_y, 0])
        draft_txt = _lbl("draft", size=36, color=SOFT).move_to([-5.0, rev_y, 0])
        open_gate = Rectangle(width=0.2, height=0.9,
                               fill_color=GHOST, fill_opacity=0.6, stroke_width=0,
                               ).move_to([0.0, rev_y, 0])  # open = narrow
        pass_arrow = Arrow([-3.9, rev_y, 0], [1.2, rev_y, 0],
                           buff=0, color=OK, stroke_width=2.5,
                           max_tip_length_to_length_ratio=0.2)
        self.play(FadeIn(draft_box), FadeIn(draft_txt), run_time=0.25)
        used += 0.25
        self.play(FadeIn(open_gate), Create(pass_arrow), run_time=0.35)
        used += 0.35

        # ── IRREVERSIBLE lane (bottom) ────────────────────────────────────────
        irrev_y = -0.8

        irrev_hdr = _lbl("IRREVERSIBLE  (gate required)", size=36, color=INK).move_to([-2.0, irrev_y + 0.8, 0])
        self.play(FadeIn(irrev_hdr), run_time=0.25)
        used += 0.25

        actions = ["DELETE", "SEND", "WIRE"]
        action_xs = [-4.8, -3.2, -1.6]
        for label, ax in zip(actions, action_xs):
            ab = RoundedRectangle(width=1.4, height=0.5, corner_radius=0.1,
                                  stroke_color=INK, stroke_width=1.5,
                                  fill_color=BG, fill_opacity=1.0).move_to([ax, irrev_y, 0])
            at = _lbl(label, size=36, color=INK).move_to([ax, irrev_y, 0])
            self.play(FadeIn(ab), FadeIn(at), run_time=0.2)
            used += 0.2

        # Closed gate
        gate_bar = Rectangle(width=0.25, height=1.1,
                              fill_color=INK, fill_opacity=0.9, stroke_width=0
                              ).move_to([0.0, irrev_y, 0])
        gate_lbl = _lbl("GATE", size=96, color=INK, weight="BOLD").move_to([0.0, irrev_y - 0.75, 0])
        self.play(FadeIn(gate_bar), FadeIn(gate_lbl), run_time=0.35)
        used += 0.35

        # Human hand icon opens the gate
        human_head = Circle(radius=0.2, fill_color=INK, stroke_width=0, fill_opacity=0.85)
        human_body = Rectangle(width=0.35, height=0.5, fill_color=INK, stroke_width=0, fill_opacity=0.85)
        human = VGroup(human_head, human_body).arrange(DOWN, buff=0.04).move_to([1.0, irrev_y, 0])
        open_lbl = _lbl("human opens", size=36, color=INK).move_to([1.8, irrev_y + 0.6, 0])
        self.play(FadeIn(human), FadeIn(open_lbl), run_time=0.35)
        used += 0.35

        self.play(gate_bar.animate.shift(UP * 0.8), run_time=0.45)
        used += 0.45

        # VOTE vs GATE contrast
        sep = Line([-6.0, -1.5, 0], [6.0, -1.5, 0], color=GHOST, stroke_width=1.2)
        self.play(Create(sep), run_time=0.2)
        used += 0.2

        vote_lbl = _lbl("VOTE — AI can win", size=36, color=SOFT).move_to([-2.8, -1.9, 0])
        gate2_lbl = _lbl("GATE — human must open", size=36, color=INK).move_to([2.8, -1.9, 0])
        vs_lbl = _lbl("vs", size=36, color=SOFT).move_to([0, -1.9, 0])
        self.play(FadeIn(vote_lbl), FadeIn(vs_lbl), FadeIn(gate2_lbl), run_time=0.35)
        used += 0.35

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A4M2 — Three Buckets
#  Sub-task tokens fall through 5 questions and sort into AI / human-only /
#  hybrid bins. Emitted artifact = "documented justification" card (not a
#  verdict stamp). Terracotta on "documented justification".
# ─────────────────────────────────────────────────────────────────────────────
class A4M2_ThreeBuckets(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A4M2"]
        used = 0.0

        # Title
        title = _lbl("Three Buckets", size=36, weight="BOLD").move_to([0, 3.2, 0])
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # Five filter questions as boxes in a column
        questions = [
            "Verification cost — cheap to check?",
            "Stakes — cost of being wrong?",
            "Distribution match — in-distribution?",
            "Reversibility — can it be undone?",
            "Audit trail — reviewable trace?",
        ]
        q_xs = np.linspace(-4.0, 4.0, 5)
        q_y = 1.5
        q_boxes = VGroup()
        for label, qx in zip(questions, q_xs):
            box = RoundedRectangle(width=2.3, height=0.6, corner_radius=0.12,
                                   stroke_color=GHOST, stroke_width=1.2,
                                   fill_color=BG, fill_opacity=1.0).move_to([qx, q_y, 0])
            # Wrap long labels
            words = label.split(" — ")
            t1 = _lbl(words[0], size=28, color=INK).move_to([qx, q_y + 0.12, 0])
            t2 = _lbl(words[1] if len(words) > 1 else "", size=28, color=SOFT).move_to([qx, q_y - 0.15, 0])
            q_boxes.add(VGroup(box, t1, t2))

        self.play(FadeIn(q_boxes), run_time=0.5)
        used += 0.5

        # Sub-task token falls through filter
        token = Circle(radius=0.18, fill_color=INK, stroke_width=0, fill_opacity=0.9).move_to([0, 2.0, 0])
        token_lbl = _lbl("sub-task", size=28, color=SOFT).next_to(token, UP, buff=0.15)
        self.play(FadeIn(token), FadeIn(token_lbl), run_time=0.25)
        used += 0.25
        self.play(token.animate.move_to([0, 0.4, 0]),
                  token_lbl.animate.move_to([0, 0.72, 0]),
                  run_time=0.5, rate_func=rate_functions.smooth)
        used += 0.5

        # Three bins at the bottom
        bin_labels = ["AI", "HUMAN-ONLY", "HYBRID"]
        bin_xs = [-3.5, 0.0, 3.5]
        bin_y = -1.1
        for bl, bx in zip(bin_labels, bin_xs):
            b_box = Rectangle(width=2.6, height=0.7,
                               fill_color=GHOST, fill_opacity=0.25,
                               stroke_color=GHOST, stroke_width=1.5).move_to([bx, bin_y, 0])
            b_txt = _lbl(bl, size=36, color=INK, weight="BOLD").move_to([bx, bin_y, 0])
            self.play(FadeIn(b_box), FadeIn(b_txt), run_time=0.18)
            used += 0.18

        # Token drops into HYBRID bin — land below the label text, not on it
        self.play(token.animate.move_to([bin_xs[2], bin_y - 0.25, 0]),
                  token_lbl.animate.move_to([bin_xs[2], bin_y + 0.55, 0]),
                  run_time=0.45)
        used += 0.45

        # The emitted artifact card
        just_box = RoundedRectangle(width=4.2, height=0.62, corner_radius=0.14,
                                    stroke_color=INK, stroke_width=2.2,
                                    fill_color=BG, fill_opacity=1.0).move_to([0, -2.3, 0])
        just_txt = _lbl("documented justification", size=36, color=INK, weight="BOLD").move_to([0, -2.3, 0])
        not_stamp = _lbl("not a verdict stamp", size=28, color=SOFT).move_to([0, -2.9, 0])
        self.play(FadeIn(just_box), FadeIn(just_txt), run_time=0.35)
        used += 0.35
        self.play(FadeIn(not_stamp), run_time=0.25)
        used += 0.25

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A5M — Riskiest Handoffs
#  6-step chain. The two AI→human seams (3→4 and 5→6) glow terracotta.
#  At seam 3→4, a qualifier token drops unless a human catch icon intercepts it.
# ─────────────────────────────────────────────────────────────────────────────
class A5M_RiskHandoffs(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A5M"]
        used = 0.0

        # Title
        title = _lbl("The Riskiest Handoffs", size=36, weight="BOLD").move_to([0, 3.2, 0])
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # 6-step chain
        steps = [
            ("1", "HUMAN\ntaxonomy", INK),
            ("2", "AI\nparse", GHOST),
            ("3", "AI\nextract", GHOST),
            ("4", "HUMAN\naudit", INK),
            ("5", "AI\nformat", GHOST),
            ("6", "HUMAN\nsign-off", INK),
        ]
        xs = np.linspace(-5.0, 5.0, 6)
        chain_y = 1.0
        node_objs = VGroup()

        for i, (num, label, clr) in enumerate(steps):
            box = RoundedRectangle(width=1.65, height=0.9, corner_radius=0.12,
                                   stroke_color=clr, stroke_width=1.8,
                                   fill_color=BG, fill_opacity=1.0).move_to([xs[i], chain_y, 0])
            t1 = _lbl(num, size=36, color=INK, weight="BOLD").move_to([xs[i], chain_y + 0.22, 0])
            lines = label.split("\n")
            t2 = _lbl(lines[0], size=28, color=INK).move_to([xs[i], chain_y - 0.05, 0])
            t3 = _lbl(lines[1] if len(lines) > 1 else "", size=28, color=INK).move_to([xs[i], chain_y - 0.28, 0])
            node_objs.add(VGroup(box, t1, t2, t3))

        self.play(FadeIn(node_objs), run_time=0.5)
        used += 0.5

        # Arrows between steps
        for i in range(5):
            arr = Arrow([xs[i] + 0.80, chain_y, 0], [xs[i+1] - 0.80, chain_y, 0],
                        buff=0, color=GHOST, stroke_width=2.0,
                        max_tip_length_to_length_ratio=0.3)
            self.play(Create(arr), run_time=0.15)
            used += 0.15

        # Highlight the two risky seams (3→4 and 5→6) in terracotta
        seam_y_offset = 0.65
        for seam_i in [2, 4]:  # 0-indexed: seam 3→4 is index 2→3, seam 5→6 is index 4→5
            seam_mid_x = (xs[seam_i] + xs[seam_i + 1]) / 2
            glow = Rectangle(width=xs[seam_i+1] - xs[seam_i] - 0.4, height=1.2,
                              fill_color=SOFT, fill_opacity=0.18, stroke_width=0
                              ).move_to([seam_mid_x, chain_y, 0])
            seam_lbl = _lbl("RISK", size=36, color=INK, weight="BOLD").move_to([seam_mid_x, chain_y + seam_y_offset, 0])
            self.play(FadeIn(glow), FadeIn(seam_lbl), run_time=0.3)
            used += 0.3

        # At seam 3→4: qualifier drops out of the stream
        seam34_x = (xs[2] + xs[3]) / 2
        qualifier = RoundedRectangle(width=2.0, height=0.42, corner_radius=0.1,
                                     stroke_color=INK, stroke_width=1.5,
                                     fill_color=BG, fill_opacity=1.0).move_to([seam34_x, chain_y + 1.2, 0])
        q_txt = _lbl("on the training set only", size=36, color=INK).move_to([seam34_x, chain_y + 1.2, 0])
        drop_arrow = Arrow([seam34_x, chain_y + 0.95, 0], [seam34_x - 0.2, chain_y - 1.2, 0],
                           buff=0, color=INK, stroke_width=1.8,
                           max_tip_length_to_length_ratio=0.3)
        self.play(FadeIn(qualifier), FadeIn(q_txt), run_time=0.3)
        used += 0.3
        self.play(Create(drop_arrow), run_time=0.35)
        used += 0.35

        # Human catch icon intercepts
        catch_head = Circle(radius=0.2, fill_color=OK, stroke_width=0, fill_opacity=0.9)
        catch_body = Rectangle(width=0.35, height=0.48, fill_color=OK, stroke_width=0, fill_opacity=0.9)
        catch = VGroup(catch_head, catch_body).arrange(DOWN, buff=0.04).move_to([seam34_x + 1.0, chain_y - 1.0, 0])
        catch_lbl = _lbl("catch", size=36, color=INK).next_to(catch, RIGHT, buff=0.15)
        self.play(FadeIn(catch), FadeIn(catch_lbl), run_time=0.3)
        used += 0.3

        # Spark line
        spark = _lbl("Both riskiest handoffs are AI to human.", size=36, color=INK).move_to([0, -2.6, 0])
        self.play(FadeIn(spark), run_time=0.3)
        used += 0.3

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A6M — Calibration
#  Horizontal axis: undertrust | calibrated | overtrust.
#  Two curves: reliance and actual reliability. Match region lit terracotta.
#  Mismatch zones labeled with their failure modes.
# ─────────────────────────────────────────────────────────────────────────────
class A6M_Calibration(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A6M"]
        used = 0.0

        # Title
        title = _lbl("Calibrated Trust", size=36, weight="BOLD").move_to([0, 3.2, 0])
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # Axis
        ax_left = -5.8
        ax_right = 5.8
        ax_y = 0.0

        axis = Arrow([ax_left, ax_y, 0], [ax_right, ax_y, 0],
                     buff=0, color=INK, stroke_width=2.5,
                     max_tip_length_to_length_ratio=0.04)
        self.play(Create(axis), run_time=0.4)
        used += 0.4

        # Zone labels
        zone_data = [
            (ax_left + 1.2,   "UNDERTRUST", SOFT,  "lose value"),
            (0.0,             "CALIBRATED", INK,   ""),
            (ax_right - 1.2,  "OVERTRUST",  SOFT,  "accept errors"),
        ]
        for x, lbl, clr, sub in zone_data:
            t = _lbl(lbl, size=36, color=INK, weight="BOLD").move_to([x, ax_y + 0.65, 0])
            self.play(FadeIn(t), run_time=0.25)
            used += 0.25
            if sub:
                st = _lbl(sub, size=28, color=INK).move_to([x, ax_y + 1.1, 0])
                self.play(FadeIn(st), run_time=0.2)
                used += 0.2

        # Dividers
        for x in [-2.3, 2.3]:
            divider = DashedLine([x, ax_y - 0.5, 0], [x, ax_y + 1.8, 0], color=GHOST, stroke_width=1.5)
            self.play(Create(divider), run_time=0.2)
            used += 0.2

        # Two curves: reliance (lower dashed) and actual reliability (solid)
        # Simple approximation: sigmoid-ish curves along the axis

        def _curve_points(x_start, x_end, y_start, y_end, n=40):
            xs = np.linspace(x_start, x_end, n)
            # Simple linear for clarity
            ys = np.linspace(y_start, y_end, n)
            return [np.array([xs[i], ax_y - 1.0 - ys[i] * 1.5, 0]) for i in range(n)]

        # Reliability curve (what the AI actually gets right) — flat-ish
        rel_pts = [np.array([ax_left + i * (ax_right - ax_left) / 39, ax_y - 1.6, 0]) for i in range(40)]
        rel_curve = VMobject(stroke_color=INK, stroke_width=2.5)
        rel_curve.set_points_smoothly(rel_pts)

        # Reliance curve (how often human accepts) — starts low, rises, then overshoots
        def _reliance_y(t):  # t in [0,1]
            # low undertrust zone, rises in calibrated zone, overshoots in overtrust
            if t < 0.33:
                return -0.4 * (1 - t / 0.33)  # below reliability
            elif t < 0.67:
                return 0.0  # matches reliability (calibrated zone)
            else:
                return 0.3 * (t - 0.67) / 0.33  # above reliability (overtrust)

        n = 40
        rel_a_pts = []
        for i in range(n):
            t = i / (n - 1)
            x = ax_left + t * (ax_right - ax_left)
            y = ax_y - 1.6 + _reliance_y(t) * 2.0
            rel_a_pts.append(np.array([x, y, 0]))

        rel_a_curve = VMobject(stroke_color=SOFT, stroke_width=2.0, stroke_opacity=0.8)
        rel_a_curve.set_points_smoothly(rel_a_pts)

        curve_lbl_rel  = _lbl("actual reliability", size=28, color=INK).move_to([0.0, ax_y - 1.35, 0])
        curve_lbl_rela = _lbl("human reliance", size=28, color=SOFT).move_to([-3.5, ax_y - 2.3, 0])

        self.play(Create(rel_curve), run_time=0.45)
        used += 0.45
        self.play(Create(rel_a_curve), run_time=0.45)
        used += 0.45
        self.play(FadeIn(curve_lbl_rel), FadeIn(curve_lbl_rela), run_time=0.3)
        used += 0.3

        # Match region — calibrated zone
        match_rect = Rectangle(width=4.6, height=0.08,
                                fill_color=SOFT, fill_opacity=0.25, stroke_width=0
                                ).move_to([0.0, ax_y - 1.6, 0])
        self.play(FadeIn(match_rect), run_time=0.3)
        used += 0.3

        match_lbl = _lbl("reliance matches reliability", size=36, color=INK).move_to([0.0, ax_y - 2.5, 0])
        self.play(FadeIn(match_lbl), run_time=0.3)
        used += 0.3

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A6M2 — Override Arithmetic
#  Write-on two fractions: 14/200 ≈ 7% and 6/40 ≈ 15%.
#  A point lands in "overtrust" on the calibration axis.
#  Terracotta on the gap between the two rates. Labeled illustrative.
# ─────────────────────────────────────────────────────────────────────────────
class A6M2_OverrideArithmetic(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A6M2"]
        used = 0.0

        # Title
        title = _lbl("Reading the Audit Trail", size=36, weight="BOLD").move_to([0, 3.2, 0])
        illustrative = _lbl("illustrative worked case", size=28, color=SOFT).move_to([0, 2.7, 0])
        self.play(FadeIn(title), FadeIn(illustrative), run_time=0.3)
        used += 0.3

        # Two fractions
        frac1_top = _lbl("14", size=40, color=INK, weight="BOLD").move_to([-3.0, 1.2, 0])
        frac1_line = Line([-4.0, 0.5, 0], [-2.0, 0.5, 0], color=INK, stroke_width=2.5)
        frac1_bot = _lbl("200", size=40, color=INK, weight="BOLD").move_to([-3.0, -0.2, 0])
        frac1_result = _lbl("7% override rate", size=36, color=SOFT).move_to([-3.0, -1.0, 0])
        frac1_lbl = _lbl("overrides", size=36, color=SOFT).move_to([-3.0, 1.9, 0])

        frac2_top = _lbl("6", size=40, color=INK, weight="BOLD").move_to([3.0, 1.2, 0])
        frac2_line = Line([2.0, 0.5, 0], [4.0, 0.5, 0], color=INK, stroke_width=2.5)
        frac2_bot = _lbl("40", size=40, color=INK, weight="BOLD").move_to([3.0, -0.2, 0])
        frac2_result = _lbl("15% error rate", size=36, color=INK).move_to([3.0, -1.0, 0])
        frac2_lbl = _lbl("sampled errors", size=36, color=INK).move_to([3.0, 1.9, 0])

        self.play(FadeIn(frac1_lbl), run_time=0.2)
        self.play(FadeIn(frac1_top), run_time=0.25)
        self.play(Create(frac1_line), run_time=0.2)
        self.play(FadeIn(frac1_bot), run_time=0.25)
        self.play(FadeIn(frac1_result), run_time=0.25)
        used += 1.15

        self.play(FadeIn(frac2_lbl), run_time=0.2)
        self.play(FadeIn(frac2_top), run_time=0.25)
        self.play(Create(frac2_line), run_time=0.2)
        self.play(FadeIn(frac2_bot), run_time=0.25)
        self.play(FadeIn(frac2_result), run_time=0.25)
        used += 1.15

        # Gap annotation — terracotta (the ONE accent)
        gap_arr = DoubleArrow(
            [-1.8, -1.0, 0], [1.8, -1.0, 0],
            buff=0, color=INK, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.2,
        )
        gap_lbl = _lbl("GAP = overtrust", size=36, color=INK, weight="BOLD").move_to([0, -1.7, 0])
        self.play(Create(gap_arr), run_time=0.35)
        self.play(FadeIn(gap_lbl), run_time=0.3)
        used += 0.65

        # Mini calibration axis at bottom showing where the point lands
        ax_left, ax_right, ax_y = -5.5, 5.5, -2.8
        axis = Arrow([ax_left, ax_y, 0], [ax_right, ax_y, 0],
                     buff=0, color=INK, stroke_width=2.0,
                     max_tip_length_to_length_ratio=0.04)
        self.play(Create(axis), run_time=0.3)
        used += 0.3

        for x, lbl, clr in [(-3.5, "UNDERTRUST", SOFT), (0, "CALIBRATED", SOFT), (3.5, "OVERTRUST", INK)]:
            t = _lbl(lbl, size=28, color=INK).move_to([x, ax_y + 0.5, 0])
            self.play(FadeIn(t), run_time=0.18)
            used += 0.18

        # Point drops into OVERTRUST zone
        point = Dot([3.5, ax_y, 0], radius=0.22, color=INK)
        point.move_to([3.5, ax_y + 1.5, 0])
        self.play(point.animate.move_to([3.5, ax_y, 0]),
                  run_time=0.45, rate_func=rate_functions.smooth)
        used += 0.45

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A2V — Unglamour Procedure
#  Two-column: interpretive words (reviews / reasonable / appropriate) on the
#  left with terracotta rings; arrows to their testable replacements on the
#  right. Spark: "Nobody gets promoted for this. It's the entire difference."
# ─────────────────────────────────────────────────────────────────────────────
class A2V_UnglamourProcedure(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR.get("A2V", 17.0)
        used = 0.0

        title = _lbl("Circle Every Interpretive Word. Replace It.", size=36, weight="BOLD").move_to([0, 3.2, 0])
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        hdr_l = _lbl("INTERPRETIVE",       size=36, color=SOFT, weight="BOLD").move_to([-4.2, 2.4, 0])
        hdr_r = _lbl("TESTABLE CRITERION", size=36, color=INK,  weight="BOLD").move_to([3.5,  2.4, 0])
        self.play(FadeIn(hdr_l), FadeIn(hdr_r), run_time=0.3)
        used += 0.3

        rows = [
            ("reviews",     "verify explanation · run checklist · record 1 of 4 codes"),
            ("reasonable",  "score > 0.7 on in-distribution sample"),
            ("appropriate", "passes 5-item policy checklist · with doc reference"),
        ]
        row_ys = [1.5, 0.1, -1.3]

        for (word, criterion), y in zip(rows, row_ys):
            w_box = RoundedRectangle(width=2.5, height=0.58, corner_radius=0.14,
                                     stroke_color=INK, stroke_width=2.5,
                                     fill_color=BG, fill_opacity=1.0).move_to([-4.2, y, 0])
            w_txt = _lbl(word, size=36, color=INK).move_to([-4.2, y, 0])
            arr = Arrow([-2.8, y, 0], [-0.8, y, 0],
                        buff=0, color=GHOST, stroke_width=2.0,
                        max_tip_length_to_length_ratio=0.28)
            c_txt = _lbl(criterion, size=28, color=INK).move_to([3.5, y, 0])

            self.play(FadeIn(w_box), FadeIn(w_txt), run_time=0.25)
            self.play(Create(arr), FadeIn(c_txt), run_time=0.38)
            used += 0.63

        sep = Line([-6.5, -2.3, 0], [6.5, -2.3, 0], color=GHOST, stroke_width=1.2)
        self.play(Create(sep), run_time=0.2)
        used += 0.2

        spark1 = _lbl("Nobody gets promoted for this.", size=36, color=SOFT).move_to([0, -2.8, 0])
        spark2 = _lbl("It's the entire difference.", size=36, color=INK).move_to([0, -3.3, 0])
        self.play(FadeIn(spark1), run_time=0.3)
        self.play(FadeIn(spark2), run_time=0.3)
        used += 0.6

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A4V — Verification Cost Pressure
#  X-axis: verification cost. Y-axis: pressure to accept without checking.
#  Rising terracotta curve. Green cheaply-verifiable zone on left; terracotta
#  danger zone on right. Spark: "The pressure to wave them through is structural."
# ─────────────────────────────────────────────────────────────────────────────
class A4V_VerificationCostPressure(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR.get("A4V", 18.0)
        used = 0.0

        title = _lbl("Verification Cost — Economics of Attention", size=36, weight="BOLD").move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        ax_xl, ax_xr = -5.0, 5.5
        ax_yb, ax_yt = -1.4, 2.2

        x_axis = Arrow([ax_xl, ax_yb, 0], [ax_xr + 0.2, ax_yb, 0],
                       buff=0, color=INK, stroke_width=2.5,
                       max_tip_length_to_length_ratio=0.04)
        y_axis = Arrow([ax_xl, ax_yb, 0], [ax_xl, ax_yt + 0.2, 0],
                       buff=0, color=INK, stroke_width=2.5,
                       max_tip_length_to_length_ratio=0.04)
        x_lbl  = _lbl("verification cost",  size=36, color=INK).move_to([1.8, ax_yb - 0.48, 0])
        y_lbl1 = _lbl("pressure to accept", size=36, color=INK).move_to([ax_xl - 1.25, 0.55, 0])
        y_lbl2 = _lbl("without checking",   size=36, color=INK).move_to([ax_xl - 1.25, 0.10, 0])

        self.play(Create(x_axis), Create(y_axis), run_time=0.4)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl1), FadeIn(y_lbl2), run_time=0.3)
        used += 0.7

        zone_h = ax_yt - ax_yb
        cheap_w = 3.2
        cheap_zone = Rectangle(
            width=cheap_w, height=zone_h,
            fill_color=OK, fill_opacity=0.12, stroke_width=0
        ).move_to([ax_xl + cheap_w / 2, (ax_yb + ax_yt) / 2, 0])
        cheap_l1 = _lbl("cheaply",    size=36, color=INK).move_to([ax_xl + cheap_w / 2, ax_yt - 0.35, 0])
        cheap_l2 = _lbl("verifiable", size=36, color=INK).move_to([ax_xl + cheap_w / 2, ax_yt - 0.73, 0])
        self.play(FadeIn(cheap_zone), FadeIn(cheap_l1), FadeIn(cheap_l2), run_time=0.3)
        used += 0.3

        danger_w = 2.8
        danger_zone = Rectangle(
            width=danger_w, height=zone_h,
            fill_color=SOFT, fill_opacity=0.12, stroke_width=0
        ).move_to([ax_xr - danger_w / 2, (ax_yb + ax_yt) / 2, 0])
        danger_l1 = _lbl("expensive to", size=36, color=INK).move_to([ax_xr - danger_w / 2, ax_yt - 0.35, 0])
        danger_l2 = _lbl("verify",        size=36, color=INK).move_to([ax_xr - danger_w / 2, ax_yt - 0.73, 0])
        self.play(FadeIn(danger_zone), FadeIn(danger_l1), FadeIn(danger_l2), run_time=0.3)
        used += 0.3

        n = 50
        curve_pts = []
        for i in range(n):
            t = i / (n - 1)
            x = ax_xl + t * (ax_xr - ax_xl)
            y = ax_yb + (t ** 1.8) * (ax_yt - ax_yb)
            curve_pts.append(np.array([x, y, 0]))

        curve = VMobject(stroke_color=INK, stroke_width=3.5)
        curve.set_points_smoothly(curve_pts)
        self.play(Create(curve), run_time=0.9)
        used += 0.9

        wave_lbl = _lbl("wave through", size=36, color=INK, weight="BOLD").move_to([ax_xr - 0.3, ax_yt + 0.55, 0])
        wave_arr = Arrow([ax_xr - 0.3, ax_yt + 0.35, 0], [ax_xr - 0.3, ax_yt + 0.05, 0],
                         buff=0, color=INK, stroke_width=1.8,
                         max_tip_length_to_length_ratio=0.4)
        self.play(FadeIn(wave_lbl), Create(wave_arr), run_time=0.35)
        used += 0.35

        sep = Line([-6.5, -2.1, 0], [6.5, -2.1, 0], color=GHOST, stroke_width=1.2)
        self.play(Create(sep), run_time=0.2)
        used += 0.2

        spark = _lbl("The pressure to wave them through is structural.", size=36, color=INK).move_to([0, -2.65, 0])
        self.play(FadeIn(spark), run_time=0.3)
        used += 0.3

        _wait_out(self, used, total)
