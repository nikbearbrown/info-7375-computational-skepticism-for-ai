"""scenes.py — claude-liam-cs-06-agent-said-done (STD retrofit)
Topic: Agentic AI — completion signal ≠ world state verification
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
        l1 = serif("The agent said it was done.", sz=60, clr=INK)
        l2 = serif("The email still existed.", sz=60, clr=CRIMSON)
        for l in [l1, l2]: self.play(FadeIn(l, shift=UP*0.1), run_time=0.6)
        l1.move_to([0, 0.7, 0]); l2.move_to([0, -0.3, 0])
        VGroup(l1, l2).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        u = Line(l2.get_left()+DOWN*0.18, l2.get_right()+DOWN*0.18, color=ACCENT, stroke_width=4)
        self.play(GrowFromPoint(u, u.get_left()), run_time=0.5)
        self.wait(max(0.01, d - 2.5))

class B02_AgentReportMismatch(Scene):
    def construct(self):
        d = dur("B02")
        eyebrow = caps("agent report vs world state", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        # Two panels
        for i, (title, content, color) in enumerate([
            ("AGENT REPORT", '"Email deleted successfully.\nTask complete."', TEAL),
            ("ACTUAL WORLD STATE", "Email still present in\nserver mailbox", CRIMSON),
        ]):
            bg = card(4.5, 3.0, fill=WHITE, stroke=color, sw=2.5).move_to([(i*2-1)*2.8, 0, 0])
            title_lbl = Text(title, font="Montserrat", font_size=26, color=color, weight=BOLD)
            content_lbl = serif(content, sz=30, clr=INK)
            grp = VGroup(title_lbl, content_lbl).arrange(DOWN, buff=0.3).move_to(bg.get_center())
            self.play(FadeIn(VGroup(bg, grp), shift=RIGHT*0.1), run_time=0.5)
        vs = Text("≠", font="Helvetica", font_size=80, color=CRIMSON).move_to(ORIGIN)
        self.play(FadeIn(vs), run_time=0.4)
        note = serif("The agent generated its own completion signal.", sz=34, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 8.0))

class B04_ActionVsWorldStateGap(Scene):
    def construct(self):
        d = dur("B04")
        eyebrow = caps("action executed ≠ world state changed", sz=26, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        steps = [
            ("Agent executes action", "send DELETE command", TEAL),
            ("Command confirmed", "server returns 200 OK", TEAL),
            ("Agent generates report", '"Done"', MUTE),
            ("World state check", "Email still exists on backup server", CRIMSON),
        ]
        for i, (step, detail, color) in enumerate(steps):
            bg = card(8.0, 0.9, fill=WHITE, stroke=color, sw=1.5).move_to([0, 1.5 - i*1.0, 0])
            s = Text(step, font="Montserrat", font_size=26, color=color, weight=BOLD)
            d_lbl = serif(detail, sz=26, clr=INK)
            row = VGroup(s, d_lbl).arrange(RIGHT, buff=0.5).move_to(bg.get_center())
            self.play(FadeIn(VGroup(bg, row), shift=RIGHT*0.1), run_time=0.35)
        note = serif("A completion signal is not a world-state measurement.", sz=34, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))

class B05_ScopeVsCompletionGap(Scene):
    def construct(self):
        d = dur("B05")
        eyebrow = caps("narrow scope vs full task — the model mismatch", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        left = card(4.0, 3.5, fill=WHITE, stroke=TEAL, sw=2).move_to([-3.0, 0, 0])
        right = card(4.0, 3.5, fill=WHITE, stroke=CRIMSON, sw=2).move_to([3.0, 0, 0])
        left_lbl = Text("AGENT MODEL\nOF TASK", font="Montserrat", font_size=24, color=TEAL, weight=BOLD)
        left_lbl.move_to(left.get_center() + UP*0.8)
        left_items = VGroup(*[serif(t, sz=24, clr=INK) for t in ["Delete from inbox", "Mark as deleted", "Return 200 OK"]])
        left_items.arrange(DOWN, buff=0.25).move_to(left.get_center() + DOWN*0.3)
        right_lbl = Text("ACTUAL TASK\nSCOPE", font="Montserrat", font_size=24, color=CRIMSON, weight=BOLD)
        right_lbl.move_to(right.get_center() + UP*0.8)
        right_items = VGroup(*[serif(t, sz=24, clr=INK) for t in ["Delete from inbox", "Delete from backup", "Delete from logs", "Purge all traces"]])
        right_items.arrange(DOWN, buff=0.25).move_to(right.get_center() + DOWN*0.3)
        for o in [left, left_lbl, left_items, right, right_lbl, right_items]:
            self.play(FadeIn(o), run_time=0.3)
        note = serif("Agent's task model was narrower than the actual requirement.", sz=32, clr=CRIMSON).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))

class B07_TwoTrackDivergenceAnimation(Scene):
    """TERRACOTTA MOMENT"""
    def construct(self):
        d = dur("B07")
        eyebrow = caps("agent world model vs actual world — diverge silently", sz=20, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        # Two parallel tracks diverging
        x_start, x_end = -6.0, 6.0
        y_agent, y_world = 1.0, -1.0
        # Start together, then diverge
        agent_line_1 = Line([x_start, 0, 0], [0, 0, 0], color=TEAL, stroke_width=4)
        world_line_1 = Line([x_start, 0, 0], [0, 0, 0], color=CRIMSON, stroke_width=4, stroke_opacity=0.6)
        self.play(Create(agent_line_1), Create(world_line_1), run_time=0.7)
        agent_lbl = caps("AGENT'S WORLD MODEL", sz=20, clr=TEAL).move_to([-4, 0.4, 0])
        self.play(FadeIn(agent_lbl), run_time=0.3)
        # Diverge
        agent_line_2 = Line([0, 0, 0], [x_end, y_agent, 0], color=TEAL, stroke_width=4)
        world_line_2 = Line([0, 0, 0], [x_end, y_world, 0], color=CRIMSON, stroke_width=4)
        world_lbl = caps("ACTUAL WORLD STATE", sz=20, clr=CRIMSON).move_to([3.5, y_world - 0.4, 0])
        self.play(Create(agent_line_2), Create(world_line_2), FadeIn(world_lbl), run_time=1.2)
        # TERRACOTTA moment: accent arrow showing the gap
        gap_arrow = DoubleArrow([x_end - 0.5, y_world + 0.1, 0], [x_end - 0.5, y_agent - 0.1, 0],
                                  color=ACCENT, stroke_width=4, buff=0.05)
        gap_lbl = caps("GAP", sz=24, clr=ACCENT).next_to(gap_arrow, RIGHT, buff=0.2)
        self.play(GrowArrow(gap_arrow), FadeIn(gap_lbl), run_time=0.5)
        agent_check = caps("agent: 'email deleted'", sz=20, clr=TEAL).move_to([3.5, y_agent + 0.4, 0])
        world_check = caps("world: 'email exists'", sz=20, clr=CRIMSON).move_to([3.5, y_world - 0.45, 0])
        self.play(FadeIn(agent_check), FadeIn(world_check), run_time=0.5)
        note = serif("Silent divergence — no error raised, no warning logged.", sz=34, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))

class B08_StructuralCauseMapping(Scene):
    def construct(self):
        d = dur("B08")
        eyebrow = caps("structural cause — completion criterion was state-free", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        wrong = serif("WRONG: completion = command confirmed", sz=40, clr=CRIMSON).move_to([0, 1.0, 0])
        right = serif("RIGHT: completion = world state verified", sz=40, clr=TEAL).move_to([0, -0.2, 0])
        self.play(FadeIn(wrong, shift=RIGHT*0.1), run_time=0.5)
        u = Line(wrong.get_left()+DOWN*0.18, wrong.get_right()+DOWN*0.18, color=CRIMSON, stroke_width=5)
        self.play(GrowFromPoint(u, u.get_left()), run_time=0.4)
        self.play(FadeIn(right, shift=UP*0.1), run_time=0.5)
        note = serif("'Done' must mean world-state confirmed, not action-dispatched.", sz=34, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))

class B09_PostActionVerificationRequirement(Scene):
    def construct(self):
        d = dur("B09")
        eyebrow = caps("post-action verification — read back the world state", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        steps = [
            "Execute the action",
            "Wait for operation to complete",
            "READ BACK: query world state independently",
            "Compare: expected state vs measured state",
            "Only then: report 'done'",
        ]
        for i, step in enumerate(steps):
            color = TEAL if i == 2 else (ACCENT if i == 4 else INK)
            lbl = serif(step, sz=38, clr=color).move_to([0, 1.5 - i*0.8, 0])
            self.play(FadeIn(lbl, shift=RIGHT*0.1), run_time=0.35)
        note = serif("Verification must be independent of the agent's own output.", sz=32, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))

class B10_SilentDivergenceRisk(Scene):
    def construct(self):
        d = dur("B10")
        eyebrow = caps("agent world model can drift silently over time", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        # Drift visualization: straight agent model vs drifting world
        axes = Axes(x_range=[0, 10, 2], y_range=[-2, 2, 1], x_length=9, y_length=4,
                    axis_config={"color": INK, "stroke_width": 2})
        axes.move_to([0, -0.3, 0])
        x_lbl = caps("actions over time", sz=18, clr=MUTE).next_to(axes.x_axis, DOWN, buff=0.3)
        self.play(Create(axes), FadeIn(x_lbl), run_time=0.6)
        agent_line = axes.plot(lambda x: 0, x_range=[0, 9.9], color=TEAL, stroke_width=3)
        world_line = axes.plot(lambda x: -0.3 * x + 0.2 * math.sin(x), x_range=[0, 9.9], color=CRIMSON, stroke_width=3)
        self.play(Create(agent_line), run_time=0.5)
        self.play(Create(world_line), run_time=0.8)
        lbl_a = caps("AGENT'S MODEL (static)", sz=18, clr=TEAL).move_to([3.5, 0.7, 0])
        lbl_w = caps("ACTUAL WORLD (drifting)", sz=18, clr=CRIMSON).move_to([3.5, -2.0, 0])
        self.play(FadeIn(lbl_a), FadeIn(lbl_w), run_time=0.4)
        note = serif("Each action increases the gap — silently.", sz=36, clr=INK).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(max(0.01, d - 7.5))

class B11_DesignRequirementWorldState(Scene):
    def construct(self):
        d = dur("B11")
        eyebrow = caps("design requirement — explicit world-state criteria", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        items = [
            "Completion criteria: defined in world-state terms",
            "Verification step: built into every agentic action",
            "Out-of-band check: independent of agent's own output",
            "Failure mode: document what 'partial completion' looks like",
        ]
        for i, item in enumerate(items):
            num = serif(f"{i+1}.", sz=40, clr=MUTE)
            txt = serif(item, sz=34, clr=INK)
            row = VGroup(num, txt).arrange(RIGHT, buff=0.3).move_to([0, 1.3 - i*0.85, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.4)
        note = serif("The agent's report is evidence — not the final word.", sz=34, clr=ACCENT).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(max(0.01, d - 7.5))

class B12_CloudCostAgentExample(Scene):
    def construct(self):
        d = dur("B12")
        eyebrow = caps("cloud cost agent — reports savings that aren't there", sz=20, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.4)
        events = [
            ("Agent tasked", "Reduce idle resource spend by 30%", INK),
            ("Agent executes", "Scales down 47 instances", TEAL),
            ("Agent reports", '"$8,400/month saved. Done."', TEAL),
            ("Reality check (3 weeks later)", "Instances auto-restarted by scheduled jobs", CRIMSON),
            ("Actual savings", "$0 — spend returned to baseline", CRIMSON),
        ]
        for i, (event, detail, color) in enumerate(events):
            ev_lbl = Text(event, font="Montserrat", font_size=24, color=color, weight=BOLD)
            det_lbl = serif(detail, sz=24, clr=INK)
            row = VGroup(ev_lbl, det_lbl).arrange(RIGHT, buff=0.4).move_to([0, 1.8 - i*0.88, 0])
            self.play(FadeIn(row, shift=RIGHT*0.1), run_time=0.3)
        note = serif("No world-state verification after the fact — none built in.", sz=30, clr=CRIMSON).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(note, shift=UP*0.1), run_time=0.4)
        self.wait(max(0.01, d - 9.0))
