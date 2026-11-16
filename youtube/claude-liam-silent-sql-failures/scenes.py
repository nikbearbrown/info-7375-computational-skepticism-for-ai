"""scenes.py — Manim scenes for claude-liam-silent-sql-failures
("It Ran Clean. It Was Wrong." — Professor Bear reviews Zhenhao's project)

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757 (ONE accent per scene).
No slant=ITALIC on multi-word text (Pango collapses spaces).
Eight body beats: A1M A2M A3M A3M2 A4M A5M A5M2 A6M
"""
from manim import *
import json, pathlib, numpy as np

# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)
try:
    _Mx = MarkupText
    MarkupText = lambda *a, font="EB Garamond", **k: _Mx(*a, font=font, **k)
except NameError:
    pass

# ── Palette ────────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")   # terracotta — ONE accent per scene
SOFT  = ManimColor("#7B7563")
GHOST = ManimColor("#B8B3A2")
OK    = ManimColor("#5B7A4E")   # green for correct / good states
WARN  = ManimColor("#8B3A3A")   # muted red for bad states

config.background_color = BG

# ── Duration table ─────────────────────────────────────────────────────────────
DUR = {k: 13.0 for k in [
    "A1M", "A2M", "A3M", "A3M2", "A4M", "A5M", "A5M2", "A6M"
]}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 13.0)
        for b in _BS["beats"]
    })
except Exception:
    pass


def _lbl(text, size=36, color=None, weight=None):
    kw = {"font_size": size, "color": color or INK}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


def _sub(text, size=28, color=None):
    return Text(text, font_size=size, color=color or SOFT)


def _wait_out(self, used, total, min_hold=0.3):
    remaining = max(min_hold, total - used)
    self.wait(remaining)


def _rule(width=10.0, color=None, stroke=1.5):
    return Line(LEFT * width / 2, RIGHT * width / 2,
                color=color or GHOST, stroke_width=stroke)


# ─────────────────────────────────────────────────────────────────────────────
#  A1M — UTXO Balance
#  Three outputs arrive at an address; two marked SPENT, one UNSPENT.
#  SQL SUM = 10.0 (gross, terracotta) vs UTXO balance = 2.0 (green).
# ─────────────────────────────────────────────────────────────────────────────
class A1M_UTXOBalance(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A1M"]
        used = 0.0

        title = _lbl("UTXO: Gross vs Balance", size=36, weight="BOLD").to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # Address node on the right
        addr_box = RoundedRectangle(width=2.8, height=0.8, corner_radius=0.15,
                                    color=INK, fill_color=BG, fill_opacity=1,
                                    stroke_width=2).move_to([3.2, 0.5, 0])
        addr_lbl = _lbl("Address", size=30, color=INK).move_to(addr_box)
        addr_grp = VGroup(addr_box, addr_lbl)

        # Output arrows: 5 BTC, 3 BTC, 2 BTC arriving from left
        arrow_data = [
            ("5.0 BTC", [-4.5, 1.8, 0], [1.8, 0.8, 0], True),   # SPENT
            ("3.0 BTC", [-4.5, 0.5, 0], [1.8, 0.5, 0], True),   # SPENT
            ("2.0 BTC", [-4.5, -0.8, 0], [1.8, 0.2, 0], False),  # UNSPENT
        ]

        arrows = VGroup()
        labels = VGroup()
        spent_marks = VGroup()

        for (val, start, end, is_spent) in arrow_data:
            color = GHOST if is_spent else INK
            arr = Arrow(start, end, color=color, stroke_width=2.5,
                        tip_length=0.2, buff=0.05)
            lbl = _lbl(val, size=28, color=color).move_to(
                [(start[0] + end[0]) / 2, start[1] + 0.25, 0]
            )
            arrows.add(arr)
            labels.add(lbl)
            if is_spent:
                mid = [(start[0] + end[0]) / 2, start[1], 0]
                cross = Text("SPENT", font_size=22, color=GHOST,
                             font="EB Garamond").move_to([mid[0], start[1] - 0.25, 0])
                spent_marks.add(cross)

        self.play(FadeIn(addr_grp), run_time=0.3)
        used += 0.3
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],
                              *[FadeIn(l) for l in labels], lag_ratio=0.2), run_time=1.2)
        used += 1.2
        self.play(FadeIn(spent_marks), run_time=0.5)
        used += 0.5

        # Rule
        rule = _rule(9.5).move_to([0, -1.4, 0])
        self.play(Create(rule), run_time=0.3)
        used += 0.3

        # Two result boxes: SQL gross vs UTXO balance
        sql_box = Rectangle(width=3.8, height=1.4, color=ACC, stroke_width=2,
                             fill_color=BG, fill_opacity=1).move_to([-2.5, -2.4, 0])
        sql_lbl = _lbl("SQL: SUM(all)", size=28, color=ACC).move_to(sql_box.get_center() + UP * 0.25)
        sql_val = _lbl("= 10.0 BTC", size=34, color=ACC, weight="BOLD").move_to(sql_box.get_center() + DOWN * 0.2)
        sql_tag = _sub("GROSS RECEIVED", size=24, color=ACC).next_to(sql_box, DOWN, buff=0.1)

        utxo_box = Rectangle(width=3.8, height=1.4, color=OK, stroke_width=2,
                              fill_color=BG, fill_opacity=1).move_to([2.5, -2.4, 0])
        utxo_lbl = _lbl("UTXO: SUM(unspent)", size=28, color=OK).move_to(utxo_box.get_center() + UP * 0.25)
        utxo_val = _lbl("= 2.0 BTC", size=34, color=OK, weight="BOLD").move_to(utxo_box.get_center() + DOWN * 0.2)
        utxo_tag = _sub("CURRENT BALANCE", size=24, color=OK).next_to(utxo_box, DOWN, buff=0.1)

        self.play(
            FadeIn(sql_box), FadeIn(sql_lbl), FadeIn(sql_val), FadeIn(sql_tag),
            run_time=0.5
        )
        used += 0.5
        self.play(
            FadeIn(utxo_box), FadeIn(utxo_lbl), FadeIn(utxo_val), FadeIn(utxo_tag),
            run_time=0.5
        )
        used += 0.5

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A2M — Two-Path Disagreement Diagram
#  Question → SQL path → 10.0 BTC; Question → RPC path → 2.0 BTC.
#  Comparison: 10.0 ≠ 2.0 → FLAG (terracotta).
# ─────────────────────────────────────────────────────────────────────────────
class A2M_TwoPathDiagram(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A2M"]
        used = 0.0

        title = _lbl("Two Paths — One Question", size=36, weight="BOLD").to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # Question bubble at top center
        q_box = RoundedRectangle(width=5.5, height=0.9, corner_radius=0.2,
                                  color=INK, fill_color=BG, fill_opacity=1,
                                  stroke_width=2).move_to([0, 2.0, 0])
        q_lbl = _lbl("Balance of 1A1zP1... ?", size=30, color=INK).move_to(q_box)
        self.play(FadeIn(q_box), FadeIn(q_lbl), run_time=0.4)
        used += 0.4

        # SQL path (left branch)
        sql_path_arr = Arrow([0, 2.0, 0], [-3.5, 0.4, 0], color=SOFT, stroke_width=2,
                              tip_length=0.2, buff=0.35)
        sql_path_lbl = _sub("SQL path", size=26, color=SOFT).move_to([-2.2, 1.4, 0])

        db_box = Rectangle(width=2.8, height=0.8, color=SOFT, stroke_width=2,
                            fill_color=BG, fill_opacity=1).move_to([-3.5, 0.0, 0])
        db_lbl = _lbl("Database", size=28, color=SOFT).move_to(db_box)

        sql_res_arr = Arrow([-3.5, -0.45, 0], [-3.5, -1.3, 0], color=ACC, stroke_width=2,
                             tip_length=0.2, buff=0.05)
        sql_res = _lbl("10.0 BTC", size=34, color=ACC, weight="BOLD").move_to([-3.5, -1.7, 0])
        sql_tag = _sub("(gross received)", size=24, color=ACC).move_to([-3.5, -2.15, 0])

        # RPC path (right branch)
        rpc_path_arr = Arrow([0, 2.0, 0], [3.5, 0.4, 0], color=SOFT, stroke_width=2,
                              tip_length=0.2, buff=0.35)
        rpc_path_lbl = _sub("RPC path", size=26, color=SOFT).move_to([2.2, 1.4, 0])

        node_box = Rectangle(width=2.8, height=0.8, color=SOFT, stroke_width=2,
                              fill_color=BG, fill_opacity=1).move_to([3.5, 0.0, 0])
        node_lbl = _lbl("Live Node", size=28, color=SOFT).move_to(node_box)

        rpc_res_arr = Arrow([3.5, -0.45, 0], [3.5, -1.3, 0], color=OK, stroke_width=2,
                             tip_length=0.2, buff=0.05)
        rpc_res = _lbl("2.0 BTC", size=34, color=OK, weight="BOLD").move_to([3.5, -1.7, 0])
        rpc_tag = _sub("(current balance)", size=24, color=OK).move_to([3.5, -2.15, 0])

        self.play(
            GrowArrow(sql_path_arr), FadeIn(sql_path_lbl),
            GrowArrow(rpc_path_arr), FadeIn(rpc_path_lbl),
            run_time=0.5
        )
        used += 0.5
        self.play(
            FadeIn(db_box), FadeIn(db_lbl),
            FadeIn(node_box), FadeIn(node_lbl),
            run_time=0.4
        )
        used += 0.4
        self.play(
            GrowArrow(sql_res_arr), FadeIn(sql_res), FadeIn(sql_tag),
            GrowArrow(rpc_res_arr), FadeIn(rpc_res), FadeIn(rpc_tag),
            run_time=0.5
        )
        used += 0.5

        # Comparison / FLAG
        flag_box = RoundedRectangle(width=4.5, height=0.9, corner_radius=0.2,
                                     color=ACC, stroke_width=3,
                                     fill_color=BG, fill_opacity=1).move_to([0, -2.8, 0])
        flag_lbl = _lbl("10.0 ≠ 2.0  →  FLAG", size=32, color=ACC, weight="BOLD").move_to(flag_box)

        self.play(FadeIn(flag_box), FadeIn(flag_lbl), run_time=0.5)
        used += 0.5

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A3M — Semantic Mismatch
#  Central word BALANCE; two branches showing SQL vs UTXO interpretation.
#  Terracotta gap line labeled "domain model gap".
# ─────────────────────────────────────────────────────────────────────────────
class A3M_SemanticMismatch(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A3M"]
        used = 0.0

        badge = _sub("TYPE 1", size=26, color=ACC).to_corner(UL, buff=0.35)
        self.play(FadeIn(badge), run_time=0.2)
        used += 0.2

        # Central word
        center_word = _lbl("\"balance\"", size=48, weight="BOLD").move_to([0, 2.2, 0])
        self.play(FadeIn(center_word), run_time=0.4)
        used += 0.4

        # Left branch: SQL/Accounting
        left_arr = Arrow([0, 2.0, 0], [-3.2, 0.6, 0], color=SOFT, stroke_width=2,
                          tip_length=0.2, buff=0.35)
        left_box = RoundedRectangle(width=3.6, height=2.0, corner_radius=0.15,
                                     color=SOFT, stroke_width=1.5,
                                     fill_color=BG, fill_opacity=1).move_to([-3.2, -0.6, 0])
        left_hdr = _lbl("In SQL / Accounting", size=26, color=SOFT).move_to([-3.2, 0.2, 0])
        left_val = _lbl("SUM(all outputs)", size=28, color=INK).move_to([-3.2, -0.55, 0])
        left_num = _lbl("= 10.0 BTC", size=32, color=INK, weight="BOLD").move_to([-3.2, -1.2, 0])

        # Right branch: UTXO
        right_arr = Arrow([0, 2.0, 0], [3.2, 0.6, 0], color=SOFT, stroke_width=2,
                           tip_length=0.2, buff=0.35)
        right_box = RoundedRectangle(width=3.6, height=2.0, corner_radius=0.15,
                                      color=SOFT, stroke_width=1.5,
                                      fill_color=BG, fill_opacity=1).move_to([3.2, -0.6, 0])
        right_hdr = _lbl("In Bitcoin / UTXO", size=26, color=SOFT).move_to([3.2, 0.2, 0])
        right_val = _lbl("SUM(unspent only)", size=28, color=INK).move_to([3.2, -0.55, 0])
        right_num = _lbl("= 2.0 BTC", size=32, color=OK, weight="BOLD").move_to([3.2, -1.2, 0])

        self.play(
            GrowArrow(left_arr), GrowArrow(right_arr),
            FadeIn(left_box), FadeIn(right_box),
            run_time=0.5
        )
        used += 0.5
        self.play(
            FadeIn(left_hdr), FadeIn(left_val), FadeIn(left_num),
            FadeIn(right_hdr), FadeIn(right_val), FadeIn(right_num),
            run_time=0.5
        )
        used += 0.5

        # Gap line + label
        gap_line = Line([-1.4, -0.6, 0], [1.4, -0.6, 0], color=ACC, stroke_width=4)
        gap_lbl = _lbl("domain model gap", size=28, color=ACC).move_to([0, -2.0, 0])
        gap_sub = _sub("right syntax, wrong model", size=26, color=ACC).move_to([0, -2.6, 0])

        self.play(Create(gap_line), run_time=0.4)
        used += 0.4
        self.play(FadeIn(gap_lbl), FadeIn(gap_sub), run_time=0.3)
        used += 0.3

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A3M2 — Null Swallowing
#  Table: 5.0, NULL, 2.0 → SUM silently skips NULL.
#  Second scenario: all NULL → SUM=0 (labeled "no data looks like zero").
# ─────────────────────────────────────────────────────────────────────────────
class A3M2_NullSwallowing(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A3M2"]
        used = 0.0

        badge = _sub("TYPE 4", size=26, color=ACC).to_corner(UL, buff=0.35)
        title = _lbl("Null Swallowing", size=36, weight="BOLD").to_edge(UP, buff=0.4)
        self.play(FadeIn(badge), FadeIn(title), run_time=0.3)
        used += 0.3

        # Scenario 1: table with NULL
        table_x = -3.0
        col_hdr = _lbl("value", size=30, color=SOFT, weight="BOLD").move_to([table_x, 1.5, 0])
        rows_data = [("5.0 BTC", INK), ("NULL", GHOST), ("2.0 BTC", INK)]
        rows = VGroup()
        for i, (val, col) in enumerate(rows_data):
            y = 0.7 - i * 0.9
            row_bg = Rectangle(width=2.5, height=0.7, color=GHOST, stroke_width=0.8,
                                fill_color=BG, fill_opacity=1).move_to([table_x, y, 0])
            row_lbl = _lbl(val, size=30, color=col).move_to([table_x, y, 0])
            rows.add(VGroup(row_bg, row_lbl))

        self.play(FadeIn(col_hdr), LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.15),
                  run_time=0.7)
        used += 0.7

        # SUM arrow → result
        sum_arr = Arrow([table_x, -1.55, 0], [table_x, -2.3, 0], color=INK,
                         stroke_width=2.5, tip_length=0.2)
        sum_lbl = _lbl("SUM", size=30, color=INK).next_to(sum_arr, LEFT, buff=0.1)
        sum_result = _lbl("7.0 BTC", size=36, color=INK, weight="BOLD").move_to([table_x, -2.8, 0])

        self.play(GrowArrow(sum_arr), FadeIn(sum_lbl), run_time=0.4)
        used += 0.4
        self.play(FadeIn(sum_result), run_time=0.3)
        used += 0.3

        # NULL annotation
        null_note = _sub("NULL skipped silently", size=26, color=GHOST).move_to([table_x, -3.3, 0])
        self.play(FadeIn(null_note), run_time=0.3)
        used += 0.3

        # Vertical rule
        v_rule = Line([0.2, 2.0, 0], [0.2, -3.5, 0], color=GHOST, stroke_width=1.5)
        self.play(Create(v_rule), run_time=0.2)
        used += 0.2

        # Scenario 2: all NULLs → SUM = 0
        sc2_x = 3.2
        col_hdr2 = _lbl("value", size=30, color=SOFT, weight="BOLD").move_to([sc2_x, 1.5, 0])
        rows2_data = [("NULL", GHOST), ("NULL", GHOST), ("NULL", GHOST)]
        rows2 = VGroup()
        for i, (val, col) in enumerate(rows2_data):
            y = 0.7 - i * 0.9
            row_bg = Rectangle(width=2.5, height=0.7, color=GHOST, stroke_width=0.8,
                                fill_color=BG, fill_opacity=1).move_to([sc2_x, y, 0])
            row_lbl = _lbl(val, size=30, color=col).move_to([sc2_x, y, 0])
            rows2.add(VGroup(row_bg, row_lbl))

        self.play(FadeIn(col_hdr2), LaggedStart(*[FadeIn(r) for r in rows2], lag_ratio=0.15),
                  run_time=0.6)
        used += 0.6

        sum_arr2 = Arrow([sc2_x, -1.55, 0], [sc2_x, -2.3, 0], color=INK,
                          stroke_width=2.5, tip_length=0.2)
        sum_result2 = _lbl("0.0 BTC", size=36, color=ACC, weight="BOLD").move_to([sc2_x, -2.8, 0])
        no_data_lbl = _lbl("no data looks like zero", size=26, color=ACC).move_to([sc2_x, -3.35, 0])

        self.play(GrowArrow(sum_arr2), run_time=0.3)
        used += 0.3
        self.play(FadeIn(sum_result2), run_time=0.3)
        used += 0.3
        self.play(FadeIn(no_data_lbl), run_time=0.3)
        used += 0.3

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A4M — Tier Ladder
#  Four steps rising left to right; Tier 3 highlighted in terracotta.
# ─────────────────────────────────────────────────────────────────────────────
class A4M_TierLadder(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A4M"]
        used = 0.0

        title = _lbl("Four Tiers of Difficulty", size=36, weight="BOLD").to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        tiers = [
            ("TIER 1", "Count txns in block X", "0 domain assumptions", INK),
            ("TIER 2", "Total ever sent to address X", "1 concept", INK),
            ("TIER 3", "Current balance of X", "UTXO state-tracking", ACC),
            ("TIER 4", "Balance excl. change outputs", "multi-hop", INK),
        ]

        step_w = 3.0
        step_h = 1.0
        step_xs = [-4.5, -1.5, 1.5, 4.5]
        step_ys = [-2.0, -1.0, 0.0, 1.0]

        steps = VGroup()
        for i, ((tier, task, note, color), x, y) in enumerate(zip(tiers, step_xs, step_ys)):
            fill = ManimColor("#FDF0E8") if color == ACC else BG
            box = Rectangle(width=step_w, height=step_h,
                            color=color, stroke_width=2 if color == ACC else 1.5,
                            fill_color=fill, fill_opacity=1).move_to([x, y, 0])
            t_lbl = _lbl(tier, size=24, color=color, weight="BOLD").move_to([x, y + 0.2, 0])
            t_task = _sub(task, size=20, color=color if color == ACC else INK).move_to([x, y - 0.05, 0])
            t_note = _sub(note, size=18, color=color if color == ACC else SOFT).move_to([x, y - 0.3, 0])
            steps.add(VGroup(box, t_lbl, t_task, t_note))

        self.play(LaggedStart(*[FadeIn(s) for s in steps], lag_ratio=0.15), run_time=1.0)
        used += 1.0

        # Staircase connector lines
        for i in range(len(tiers) - 1):
            x1, y1 = step_xs[i] + step_w / 2, step_ys[i]
            x2, y2 = step_xs[i + 1] - step_w / 2, step_ys[i + 1]
            conn = Line([x1, y1, 0], [x2, y2, 0], color=GHOST, stroke_width=1.5)
            self.play(Create(conn), run_time=0.15)
            used += 0.15

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A5M — Self-Consistency Fail
#  Model emits 5 samples; all return 10.0 BTC (gross). Agreement ✓ but ALL WRONG.
# ─────────────────────────────────────────────────────────────────────────────
class A5M_SelfConsistencyFail(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A5M"]
        used = 0.0

        title = _lbl("Strategy 2: Self-Consistency", size=34, weight="BOLD").to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # Model box at center-top
        model_box = RoundedRectangle(width=2.4, height=1.0, corner_radius=0.15,
                                      color=INK, fill_color=BG, fill_opacity=1,
                                      stroke_width=2).move_to([0, 1.6, 0])
        model_lbl = _lbl("LLM", size=32, weight="BOLD").move_to(model_box)
        self.play(FadeIn(model_box), FadeIn(model_lbl), run_time=0.3)
        used += 0.3

        # 5 output arrows + boxes — offset boxes further so no arrow passes through text
        angles = [-70, -35, 0, 35, 70]
        out_grp = VGroup()
        for i, ang in enumerate(angles):
            rad = ang * PI / 180
            end_x = 3.8 * np.sin(rad)
            end_y = 1.6 - 2.8 * np.cos(rad)
            # Arrow stops short of the box center (buff=0); we manually point to box edge
            box_half_h = 0.325
            dir_y = end_y - 1.6
            dir_len = np.sqrt(end_x ** 2 + dir_y ** 2) + 1e-6
            tip_x = end_x - end_x / dir_len * (box_half_h + 0.05)
            tip_y = end_y - dir_y / dir_len * (box_half_h + 0.05)
            arr = Arrow([0, 1.6, 0], [tip_x, tip_y, 0], color=SOFT, stroke_width=2,
                         tip_length=0.18, buff=0.55)
            res_box = RoundedRectangle(width=1.8, height=0.65, corner_radius=0.1,
                                        color=GHOST, fill_color=BG, fill_opacity=1,
                                        stroke_width=1.5).move_to([end_x, end_y, 0])
            res_lbl = _lbl("10.0 BTC", size=24, color=INK).move_to(res_box)
            out_grp.add(VGroup(arr, res_box, res_lbl))

        self.play(LaggedStart(*[FadeIn(g) for g in out_grp], lag_ratio=0.1), run_time=0.8)
        used += 0.8

        # Agreement check
        agree = _lbl("5 / 5 agree", size=30, color=OK).move_to([0, -2.1, 0])
        self.play(FadeIn(agree), run_time=0.3)
        used += 0.3

        # ALL WRONG
        wrong = _lbl("ALL WRONG", size=44, color=ACC, weight="BOLD").move_to([0, -2.85, 0])
        caption = _sub("consistent agreement on a wrong answer", size=26, color=ACC).move_to([0, -3.3, 0])
        self.play(FadeIn(wrong), run_time=0.4)
        used += 0.4
        self.play(FadeIn(caption), run_time=0.3)
        used += 0.3

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A5M2 — Synthetic DB
#  Table: 3 outputs, 2 SPENT, 1 UNSPENT.
#  Gross received = 10.0; current balance = 2.0.
#  Query returns 10.0 → BUG CAUGHT (terracotta).
# ─────────────────────────────────────────────────────────────────────────────
class A5M2_SyntheticDB(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A5M2"]
        used = 0.0

        title = _lbl("Strategy 3: Synthetic DB", size=34, weight="BOLD").to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # Table
        col_w = [1.2, 1.8, 2.0]
        headers = ["Output", "Spent", "Value"]
        rows = [
            ("1", "YES", "5.0 BTC"),
            ("2", "YES", "3.0 BTC"),
            ("3", "NO", "2.0 BTC"),
        ]

        t_x = -2.0
        t_y_start = 1.6

        header_grp = VGroup()
        for j, (hdr, w) in enumerate(zip(headers, col_w)):
            x = t_x + sum(col_w[:j]) + w / 2 - sum(col_w) / 2
            cell_bg = Rectangle(width=w, height=0.65, color=INK, stroke_width=1.5,
                                 fill_color=BG, fill_opacity=1).move_to([x, t_y_start, 0])
            cell_lbl = _lbl(hdr, size=26, color=INK, weight="BOLD").move_to([x, t_y_start, 0])
            header_grp.add(VGroup(cell_bg, cell_lbl))

        self.play(FadeIn(header_grp), run_time=0.3)
        used += 0.3

        rows_grp = VGroup()
        for i, (out_id, spent, val) in enumerate(rows):
            y = t_y_start - (i + 1) * 0.75
            spent_color = GHOST if spent == "YES" else INK
            cell_vals = [out_id, spent, val]
            for j, (cell_val, w) in enumerate(zip(cell_vals, col_w)):
                x = t_x + sum(col_w[:j]) + w / 2 - sum(col_w) / 2
                col = GHOST if spent == "YES" else (OK if j == 2 else INK)
                cell_bg = Rectangle(width=w, height=0.65, color=GHOST, stroke_width=0.8,
                                     fill_color=BG, fill_opacity=1).move_to([x, y, 0])
                cell_lbl = _lbl(cell_val, size=26, color=col).move_to([x, y, 0])
                rows_grp.add(VGroup(cell_bg, cell_lbl))

        self.play(LaggedStart(*[FadeIn(r) for r in rows_grp], lag_ratio=0.1), run_time=0.7)
        used += 0.7

        # Two arrows to result boxes
        gross_arr = Arrow([-1.0, -0.8, 0], [-3.5, -1.8, 0], color=ACC, stroke_width=2,
                           tip_length=0.18, buff=0.05)
        gross_box = Rectangle(width=2.8, height=0.9, color=ACC, stroke_width=2,
                               fill_color=BG, fill_opacity=1).move_to([-3.5, -2.4, 0])
        gross_lbl = _lbl("10.0 BTC", size=32, color=ACC, weight="BOLD").move_to([-3.5, -2.4, 0])
        gross_tag = _sub("GROSS RECEIVED", size=22, color=ACC).move_to([-3.5, -3.0, 0])

        bal_arr = Arrow([-1.0, -0.8, 0], [1.0, -1.8, 0], color=OK, stroke_width=2,
                         tip_length=0.18, buff=0.05)
        bal_box = Rectangle(width=2.8, height=0.9, color=OK, stroke_width=2,
                             fill_color=BG, fill_opacity=1).move_to([1.0, -2.4, 0])
        bal_lbl = _lbl("2.0 BTC", size=32, color=OK, weight="BOLD").move_to([1.0, -2.4, 0])
        bal_tag = _sub("CURRENT BALANCE", size=22, color=OK).move_to([1.0, -3.0, 0])

        self.play(
            GrowArrow(gross_arr), GrowArrow(bal_arr),
            FadeIn(gross_box), FadeIn(gross_lbl), FadeIn(gross_tag),
            FadeIn(bal_box), FadeIn(bal_lbl), FadeIn(bal_tag),
            run_time=0.6
        )
        used += 0.6

        # Query returns 10.0 → BUG CAUGHT
        bug_box = RoundedRectangle(width=3.2, height=0.8, corner_radius=0.15,
                                    color=ACC, stroke_width=3,
                                    fill_color=BG, fill_opacity=1).move_to([4.0, -2.4, 0])
        bug_lbl = _lbl("BUG CAUGHT", size=28, color=ACC, weight="BOLD").move_to(bug_box)
        bug_arr = Arrow([gross_box.get_right()[0], -2.4, 0], [bug_box.get_left()[0] - 0.1, -2.4, 0],
                         color=ACC, stroke_width=2, tip_length=0.18, buff=0.05)

        self.play(GrowArrow(bug_arr), FadeIn(bug_box), FadeIn(bug_lbl), run_time=0.4)
        used += 0.4

        _wait_out(self, used, total)


# ─────────────────────────────────────────────────────────────────────────────
#  A6M — Calibration By Tier
#  Reliability diagram: x=stated confidence, y=actual accuracy.
#  Tier 1 near diagonal (green); Tier 3 above diagonal = overconfident (terracotta).
# ─────────────────────────────────────────────────────────────────────────────
class A6M_CalibrationByTier(Scene):

    def construct(self):
        self.camera.background_color = BG
        total = DUR["A6M"]
        used = 0.0

        title = _lbl("Calibration By Tier", size=36, weight="BOLD").to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.3)
        used += 0.3

        # Axes — raised center to keep tick labels and x_lbl inside safe area
        ax = Axes(
            x_range=[0, 1, 0.25],
            y_range=[0, 1, 0.25],
            x_length=7.0,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2,
                          "tick_size": 0.08, "numbers_to_include": [0.25, 0.5, 0.75, 1.0]},
            tips=False,
        ).move_to([0.3, 0.1, 0])

        ax.get_axis(0).set_color(INK)
        ax.get_axis(1).set_color(INK)

        x_lbl = _sub("Stated Confidence", size=26, color=INK).next_to(ax, DOWN, buff=0.3)

        self.play(Create(ax), FadeIn(x_lbl), run_time=0.6)
        used += 0.6

        # Perfect calibration diagonal (dashed)
        diag = ax.plot(lambda x: x, x_range=[0, 1], color=GHOST, stroke_width=2)
        diag_dash = DashedVMobject(diag, num_dashes=20, equal_lengths=False)
        # Place label below the diagonal line to avoid "label on curve" detection
        diag_lbl = _sub("perfect calibration", size=20, color=GHOST).next_to(
            ax.c2p(0.55, 0.38), DOWN, buff=0.08)
        self.play(Create(diag_dash), FadeIn(diag_lbl), run_time=0.4)
        used += 0.4

        # Tier 1 line (well-calibrated, near diagonal, slight underconfidence)
        t1_pts = [(0.1, 0.12), (0.3, 0.31), (0.5, 0.48), (0.7, 0.69), (0.9, 0.88)]
        t1_coords = [ax.c2p(x, y) for x, y in t1_pts]
        t1_curve = VMobject(color=OK, stroke_width=3)
        t1_curve.set_points_as_corners(t1_coords)
        t1_lbl = _sub("Tier 1", size=26, color=OK).next_to(ax.c2p(0.9, 0.88), RIGHT, buff=0.05)

        self.play(Create(t1_curve), FadeIn(t1_lbl), run_time=0.5)
        used += 0.5

        # Tier 3 line (overconfident at high confidence: high confidence, lower accuracy)
        t3_pts = [(0.1, 0.16), (0.3, 0.38), (0.5, 0.42), (0.7, 0.44), (0.9, 0.50)]
        t3_coords = [ax.c2p(x, y) for x, y in t3_pts]
        t3_curve = VMobject(color=ACC, stroke_width=3)
        t3_curve.set_points_as_corners(t3_coords)
        t3_lbl = _sub("Tier 3", size=26, color=ACC).next_to(ax.c2p(0.9, 0.50), RIGHT, buff=0.05)

        self.play(Create(t3_curve), FadeIn(t3_lbl), run_time=0.5)
        used += 0.5

        # Shade gap between Tier 3 and diagonal at high confidence
        shade_pts = [ax.c2p(0.7, 0.44), ax.c2p(0.9, 0.50),
                     ax.c2p(0.9, 0.90), ax.c2p(0.7, 0.70)]
        shade = Polygon(*shade_pts, color=ACC, fill_color=ACC, fill_opacity=0.12,
                         stroke_width=0)
        self.play(FadeIn(shade), run_time=0.3)
        used += 0.3

        # Annotation
        cliff_lbl = _lbl("overconfident on Tier 3", size=28, color=ACC).move_to([3.5, -2.8, 0])
        self.play(FadeIn(cliff_lbl), run_time=0.3)
        used += 0.3

        _wait_out(self, used, total)
