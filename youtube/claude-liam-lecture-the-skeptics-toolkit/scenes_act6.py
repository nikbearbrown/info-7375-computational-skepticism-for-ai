"""ACT X · Skepticism as a team practice  (B50-B55, all Manim)

One cast for the act: outlined cards, round check-circles, a post/gate on a track, and ONE terracotta dot (the thing that
slips through, the gap, the failure). Nothing is a person. Numbers on screen: none (all schematic); the only quoted
words are the report line in B53, taken from the Agents of Chaos paper (factcheck/PRIMARIES.md).
"""


def a10_post(x, y, color=INK):
    """A gate post: a vertical bar with a cross-bar on top."""
    return VGroup(Line([x, y - 0.55, 0], [x, y + 0.55, 0], color=color, stroke_width=8),
                  Line([x - 0.3, y + 0.55, 0], [x + 0.3, y + 0.55, 0], color=color, stroke_width=8))


def a10_chk(x, y, r=0.32, color=INK):
    """A check inside a ring."""
    return VGroup(Circle(radius=r, color=color, stroke_width=5).move_to([x, y, 0]),
                  check(x, y + 0.02, 0.17, color, 6))


def a10_card(x, y, w, h, color=DIM, sw=4):
    return RoundedRectangle(width=w, height=h, corner_radius=0.2, fill_opacity=0, stroke_color=color, stroke_width=sw).move_to([x, y, 0])


def a10_env(x, y, w=1.1, h=0.74, color=INK, sw=5):
    """An envelope: outline plus the V flap."""
    return VGroup(Rectangle(width=w, height=h, stroke_color=color, stroke_width=sw, fill_opacity=0).move_to([x, y, 0]),
                  Line([x - w / 2, y + h / 2, 0], [x, y - 0.02, 0], color=color, stroke_width=sw),
                  Line([x + w / 2, y + h / 2, 0], [x, y - 0.02, 0], color=color, stroke_width=sw))


def a10_cross(x, y, s=0.22, color=INK, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w))


# ── B50 · one checkpoint vs the moves built into the workflow ────────────────────────────────────────────────
class B50_Fragile(Scene):
    def construct(self):
        y1, y2 = 1.2, -1.6
        tr1 = Line([-5.7, y1, 0], [5.7, y1, 0], color=DIM, stroke_width=5)
        lab1 = T("one checkpoint", 34).move_to([-4.0, y1 + 1.0, 0])
        post1 = a10_post(0.8, y1)
        self.add(tr1, lab1, post1)
        a = Dot([-4.6, y1, 0], radius=0.2, color=BAR1)
        bad = Dot([-3.0, y1, 0], radius=0.2, color=TERRA)
        self.play(GrowFromCenter(a), GrowFromCenter(bad), run_time=0.5)
        self.play(a.animate.move_to([0.8, y1, 0]), run_time=0.8)
        ck1 = a10_chk(0.8, y1 + 1.1)
        self.play(Create(ck1), run_time=0.4)
        self.play(a.animate.move_to([5.0, y1, 0]), run_time=0.8)
        until(self, "It depends", lead=0.3)
        self.play(post1.animate.set_color(GHOST), FadeOut(ck1), run_time=0.5)
        miss = T("missed", 34).move_to([0.8, y1 - 1.0, 0])
        self.play(FadeIn(miss), run_time=0.3)
        until(self, "remembering", lead=0.8)
        self.play(bad.animate.move_to([4.2, y1, 0]), run_time=1.0)
        until(self, "Durable teams", lead=0.3)
        tr2 = Line([-5.7, y2, 0], [5.7, y2, 0], color=DIM, stroke_width=5)
        lab2 = T("built in", 34).move_to([-4.6, y2 + 1.0, 0])
        xs = [-2.4, 0.4, 3.2]
        posts = [a10_post(x, y2) for x in xs]
        cks = [a10_chk(x, y2 + 1.1) for x in xs]
        self.play(Create(tr2), FadeIn(lab2), *[Create(p) for p in posts], run_time=0.5)
        a2 = Dot([-5.0, y2, 0], radius=0.2, color=BAR1)
        bad2 = Dot([-5.6, y2, 0], radius=0.2, color=TERRA)
        self.play(GrowFromCenter(a2), GrowFromCenter(bad2), run_time=0.3)
        self.play(a2.animate.move_to([5.0, y2, 0]), LaggedStart(*[Create(c) for c in cks], lag_ratio=0.35),
                  bad2.animate.move_to([-3.2, y2, 0]), run_time=1.2)
        ring = Circle(radius=0.36, color=INK, stroke_width=5).move_to([-3.2, y2, 0])
        self.play(Create(ring), run_time=0.3)
        done(self)


# ── B51 · three insert points; "nobody" is the undefended gap ────────────────────────────────────────────────
class B51_InsertPoints(Scene):
    def construct(self):
        xs = [-4.4, -1.5, 1.4, 4.3]
        ys = -0.9
        cy = 1.0
        segs = VGroup(*[Line([xs[i] + 0.45, ys, 0], [xs[i + 1] - 0.45, ys, 0], color=DIM, stroke_width=5) for i in range(3)])
        circs = VGroup(*[Circle(radius=0.45, color=DIM, stroke_width=5).move_to([x, ys, 0]) for x in xs])
        names = ["ship", "run", "review", "act"]
        labs = VGroup(*[T(n, 40).move_to([x, -1.9, 0]) for n, x in zip(names, xs)])
        self.add(segs, circs, labs)
        tops = ["checklist", "monitoring", "handoff"]

        def stem(x):
            return Line([x, cy - 0.75, 0], [x, ys + 0.45, 0], color=DIM, stroke_width=5)

        def top_lab(t, x):
            return T(t, 40).move_to([x, 2.4, 0])

        # 1 checklist
        c1 = a10_card(xs[0], cy, 1.9, 1.5, INK)
        c1_in = VGroup(check(xs[0] - 0.55, cy + 0.36, 0.22, INK, 6), Line([xs[0] - 0.3, cy + 0.36, 0], [xs[0] + 0.6, cy + 0.36, 0], color=DIM, stroke_width=5),
                       Line([xs[0] - 0.62, cy - 0.02, 0], [xs[0] + 0.6, cy - 0.02, 0], color=DIM, stroke_width=5),
                       Line([xs[0] - 0.62, cy - 0.4, 0], [xs[0] + 0.6, cy - 0.4, 0], color=DIM, stroke_width=5))
        self.play(Create(c1), Create(c1_in), Create(stem(xs[0])), FadeIn(top_lab(tops[0], xs[0])), run_time=0.6)
        # 2 monitoring
        until(self, "Put the falsification conditions", lead=0.25)
        c2 = a10_card(xs[1], cy, 1.9, 1.5, INK)
        zz = [(-0.7, -0.25), (-0.35, 0.2), (0.0, -0.1), (0.35, 0.3), (0.7, 0.0)]
        c2_in = VGroup(*[Line([xs[1] + zz[i][0], cy + zz[i][1], 0], [xs[1] + zz[i + 1][0], cy + zz[i + 1][1], 0], color=INK, stroke_width=5) for i in range(4)])
        self.play(Create(c2), Create(c2_in), Create(stem(xs[1])), FadeIn(top_lab(tops[1], xs[1])), run_time=0.6)
        # 3 handoff
        until(self, "Put the shift questions", lead=0.25)
        c3 = a10_card(xs[2], cy, 1.9, 1.5, INK)
        c3_in = VGroup(Circle(radius=0.22, color=INK, stroke_width=5).move_to([xs[2] - 0.55, cy, 0]),
                       Circle(radius=0.22, color=INK, stroke_width=5).move_to([xs[2] + 0.55, cy, 0]),
                       Line([xs[2] - 0.33, cy, 0], [xs[2] + 0.33, cy, 0], color=INK, stroke_width=5))
        self.play(Create(c3), Create(c3_in), Create(stem(xs[2])), FadeIn(top_lab(tops[2], xs[2])), run_time=0.6)
        # the question walks the line
        until(self, "For each capacity", lead=0.2)
        ring = Circle(radius=0.64, color=INK, stroke_width=6).move_to([xs[0], ys, 0])
        self.play(Create(ring), run_time=0.4)
        until(self, "by whom", lead=0.3)
        self.play(ring.animate.move_to([xs[1], ys, 0]), run_time=0.4)
        until(self, "seeing what", lead=0.3)
        self.play(ring.animate.move_to([xs[2], ys, 0]), run_time=0.4)
        until(self, "nobody", lead=0.5)
        self.play(ring.animate.move_to([xs[3], ys, 0]), run_time=0.4)
        c4 = a10_card(xs[3], cy, 1.9, 1.5, GHOST, 5)
        q_dot = Dot([xs[3], cy, 0], radius=0.2, color=TERRA)
        self.play(Create(c4), GrowFromCenter(q_dot), FadeIn(top_lab("nobody", xs[3])), run_time=0.5)
        gap = T("undefended gap", 40).move_to([3.8, -2.7, 0])
        self.play(FadeIn(gap), run_time=0.4)
        done(self)


# ── B52 · before run / during run / before action ────────────────────────────────────────────────────────────
class B52_ThreeCheckpoints(Scene):
    def construct(self):
        xs = [-3.9, 0.0, 3.9]
        line = Line([-5.8, 2.0, 0], [5.8, 2.0, 0], color=DIM, stroke_width=5)
        phases = ["before run", "during run", "before action"]
        plabs = VGroup(*[T(p, 34).move_to([x, 2.65, 0]) for p, x in zip(phases, xs)])
        self.add(line, plabs)
        pdots = [Dot([x, 2.0, 0], radius=0.14, color=INK) for x in xs]
        # 1 lock the prediction
        body = RoundedRectangle(width=1.3, height=1.0, corner_radius=0.15, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([xs[0], 0.45, 0])
        shackle = Arc(radius=0.4, start_angle=0, angle=PI, color=INK, stroke_width=5).move_to([xs[0], 1.4, 0])
        key = Dot([xs[0], 0.45, 0], radius=0.1, color=INK)
        self.play(GrowFromCenter(pdots[0]), Create(body), Create(shackle), run_time=0.5)
        self.play(shackle.animate.move_to([xs[0], 1.15, 0]), GrowFromCenter(key), run_time=0.4)
        p_lab = T("prediction", 34).move_to([xs[0], -0.55, 0])
        self.add(p_lab)
        # 2 keep the record
        until(self, "Keep the record", lead=0.3)
        self.play(GrowFromCenter(pdots[1]), run_time=0.3)
        rec = []
        for i, yy in enumerate([1.0, 0.55, 0.1]):
            ln = Line([xs[1] - 0.9, yy, 0], [xs[1] + 0.5 + 0.2 * (i % 2), yy, 0], color=DIM, stroke_width=6)
            dt = Dot([xs[1] - 1.1, yy, 0], radius=0.09, color=INK)
            rec.append(VGroup(dt, ln))
            self.play(Create(ln), GrowFromCenter(dt), run_time=0.3)
        r_lab = T("record", 34).move_to([xs[1], -0.55, 0])
        self.add(r_lab)
        # 3 a named check of the actual state
        until(self, "Before action", lead=0.3)
        self.play(GrowFromCenter(pdots[2]), run_time=0.3)
        scard = a10_card(xs[2] + 0.1, 0.55, 1.7, 1.2, DIM)
        lens = Circle(radius=0.5, color=INK, stroke_width=6).move_to([xs[2] - 0.2, 0.75, 0])
        handle = Line([xs[2] + 0.16, 0.39, 0], [xs[2] + 0.62, -0.05, 0], color=INK, stroke_width=8)
        self.play(Create(scard), Create(lens), Create(handle), run_time=0.6)
        s_lab = T("actual state", 34).move_to([xs[2], -0.55, 0])
        self.add(s_lab)
        # ledger
        until(self, "Keep the original prediction", lead=0.3)
        led = a10_card(0.0, -2.2, 7.0, 1.9, DIM)
        t1 = T("predicted", 34).move_to([-2.4, -1.85, 0])
        l1 = Line([0.2, -1.85, 0], [1.9, -1.85, 0], color=INK, stroke_width=6)
        self.play(Create(led), FadeIn(t1), Create(l1), run_time=0.6)
        until(self, "append what you observed", lead=0.3)
        t2 = T("observed", 34).move_to([-2.4, -2.6, 0])
        l2 = Line([0.2, -2.6, 0], [1.4, -2.6, 0], color=INK, stroke_width=6)
        dt2 = Dot([1.7, -2.6, 0], radius=0.12, color=TERRA)
        self.play(FadeIn(t2), Create(l2), GrowFromCenter(dt2), run_time=0.5)
        until(self, "never rewrite", lead=0.3)
        arr = Arrow([2.8, -2.55, 0], [2.8, -1.85, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.18)
        xx = a10_cross(2.8, -2.2)
        nr = T("no rewrite", 34).move_to([4.75, -2.2, 0])
        self.play(Create(arr), Create(xx), FadeIn(nr), run_time=0.5)
        done(self)


# ── B53 · Ash: the four tiles return as the running case ────────────────────────────────────────────────────
class B53_AshReturns(Scene):
    def construct(self):
        xs = [-4.35, -1.45, 1.45, 4.35]
        y0 = 0.3
        heads = ["ASKED", "DID", "REPORTED", "STATE"]
        subs = ["delete email", "local reset", "reset\ncompleted", "email\nstill there"]
        tiles = [a10_card(x, y0, 2.6, 2.6, DIM) for x in xs]
        hl = [T(h, 34).move_to([x, 2.6, 0]) for h, x in zip(heads, xs)]
        sl = [T(s, 32).move_to([x, -2.0, 0]) for s, x in zip(subs, xs)]
        # icons
        i_ask = a10_env(xs[0], y0)
        scr = Rectangle(width=1.4, height=0.9, stroke_color=DIM, stroke_width=5, fill_opacity=0).move_to([xs[1], y0 + 0.2, 0])
        base = Line([xs[1] - 0.8, y0 - 0.45, 0], [xs[1] + 0.8, y0 - 0.45, 0], color=DIM, stroke_width=6)
        ghost = a10_env(xs[1], y0 + 0.2, 0.7, 0.46, GHOST, 4)
        i_did = VGroup(scr, base, ghost)
        i_rep = check(xs[2] - 0.2, y0 + 0.1, 0.55, INK, 12)
        srv1 = Rectangle(width=1.5, height=0.7, stroke_color=DIM, stroke_width=5, fill_opacity=0).move_to([xs[3], y0 + 0.55, 0])
        srv2 = Rectangle(width=1.5, height=0.7, stroke_color=DIM, stroke_width=5, fill_opacity=0).move_to([xs[3], y0 - 0.3, 0])
        env_in = a10_env(xs[3], y0 + 0.55, 0.66, 0.44, INK, 4)
        i_state = VGroup(srv1, srv2, env_in)
        icons = [i_ask, i_did, i_rep, i_state]
        for k in range(4):
            self.play(Create(tiles[k]), Create(icons[k]), FadeIn(hl[k]), FadeIn(sl[k]), run_time=0.5)
            self.wait(0.15)
        until(self, "true about the local machine", lead=0.2)
        self.play(tiles[1].animate.set_stroke(INK, 8), tiles[2].animate.set_stroke(INK, 8), run_time=0.4)
        until(self, "false about the system", lead=0.6)
        gap = dim_arrow([1.45, 1.78, 0], [4.35, 1.78, 0], color=INK)
        mark = a10_cross(2.9, 1.78, 0.2, INK, 7)
        t_dot = Dot([5.1, 1.25, 0], radius=0.2, color=TERRA)
        self.play(tiles[3].animate.set_stroke(INK, 8), Create(gap), Create(mark), GrowFromCenter(t_dot), run_time=0.5)
        # the running case: a lens sweeps the four tiles
        until(self, "running case", lead=0.1)
        lens = VGroup(Circle(radius=0.75, color=INK, stroke_width=6).move_to([xs[0], y0, 0]),
                      Line([xs[0] + 0.53, y0 - 0.53, 0], [xs[0] + 0.95, y0 - 0.95, 0], color=INK, stroke_width=8))
        self.play(Create(lens), run_time=0.4)
        ticks = []
        for k in (1, 2, 3):
            self.play(lens.animate.shift(RIGHT * (xs[k] - xs[k - 1])), run_time=0.7)
            ticks.append(Dot([xs[k], -1.2, 0], radius=0.1, color=INK))
            self.play(GrowFromCenter(ticks[-1]), run_time=0.15)
        done(self)


# ── B54 · three failures compressed; the capacities that catch them ──────────────────────────────────────────
class B54_ThreeFailures(Scene):
    def construct(self):
        xs = [-3.9, 0.0, 3.9]
        cy = 0.9
        labs = ["correct, harmful", "fluent, wrong", "success, nothing"]
        cards = [a10_card(x, cy, 3.4, 2.4, DIM) for x in xs]
        ll = [T(t, 34).move_to([x, 2.55, 0]) for t, x in zip(labs, xs)]
        # 1 correct + harmful
        tri = Polygon([xs[0] + 0.8, cy + 0.6, 0], [xs[0] + 0.35, cy - 0.3, 0], [xs[0] + 1.25, cy - 0.3, 0], color=INK, stroke_width=6)
        bang = Line([xs[0] + 0.8, cy + 0.2, 0], [xs[0] + 0.8, cy - 0.05, 0], color=INK, stroke_width=6)
        c1 = VGroup(check(xs[0] - 0.9, cy, 0.4, INK, 10), tri, bang)
        # 2 fluent + wrong
        c2 = VGroup(*[Line([xs[1] - 1.3, cy + dy, 0], [xs[1] + 0.1 + dl, cy + dy, 0], color=DIM, stroke_width=6)
                      for dy, dl in ((0.5, 0.2), (0.0, 0.0), (-0.5, 0.15))], a10_cross(xs[1] + 1.1, cy, 0.25, INK, 9))
        # 3 success + nothing
        empty = Rectangle(width=0.9, height=0.9, stroke_color=GHOST, stroke_width=5, fill_opacity=0).move_to([xs[2] + 0.85, cy, 0])
        c3 = VGroup(check(xs[2] - 0.9, cy, 0.4, INK, 10), empty)
        reveal = [(cards[0], c1, ll[0]), (cards[1], c2, ll[1]), (cards[2], c3, ll[2])]
        until(self, "AI can be technically", lead=0.1)
        self.play(Create(cards[0]), Create(c1), FadeIn(ll[0]), run_time=0.6)
        until(self, "It can be fluent", lead=0.3)
        self.play(Create(cards[1]), Create(c2), FadeIn(ll[1]), run_time=0.6)
        until(self, "It can report", lead=0.3)
        self.play(Create(cards[2]), Create(c3), FadeIn(ll[2]), run_time=0.6)
        # the net of capacities
        until(self, "The capacities", lead=0.2)
        net_y = -1.6
        net = Line([-5.6, net_y, 0], [5.6, net_y, 0], color=DIM, stroke_width=5)
        stakes = VGroup(*[Dot([x, net_y, 0], radius=0.14, color=INK) for x in (-5.4, -1.95, 1.95, 5.4)])
        self.play(Create(net), LaggedStart(*[GrowFromCenter(s) for s in stakes], lag_ratio=0.25), run_time=0.9)
        drops = [Dot([x, cy - 1.45, 0], radius=0.2, color=TERRA) for x in xs]
        self.play(*[GrowFromCenter(d) for d in drops], run_time=0.3)
        self.play(*[d.animate.move_to([d.get_center()[0], net_y + 0.28, 0]) for d in drops], run_time=0.8, rate_func=ease_in)
        until(self, "supervisory", lead=0.2)
        sup = T("supervisory, human", 34).move_to([0.0, -2.6, 0])
        self.play(FadeIn(sup), run_time=0.4)
        done(self)


# ── B55 · the open question: trust anyway? ──────────────────────────────────────────────────────────────────
def a10_scale(th, px=-1.8, py=0.7, L=2.3, drop=1.0):
    """Balance at tilt th (>0: left pan down, i.e. checking heavier). Pans hang level."""
    lx, ly = px - L * np.cos(th), py - L * np.sin(th)
    rx, ry = px + L * np.cos(th), py + L * np.sin(th)
    beam = Line([lx, ly, 0], [rx, ry, 0], color=INK, stroke_width=8)
    parts = [beam]
    for ex, ey in ((lx, ly), (rx, ry)):
        py_ = ey - drop
        parts.append(Line([ex, ey, 0], [ex - 0.5, py_, 0], color=DIM, stroke_width=4))
        parts.append(Line([ex, ey, 0], [ex + 0.5, py_, 0], color=DIM, stroke_width=4))
        parts.append(Polygon([ex - 0.6, py_, 0], [ex + 0.6, py_, 0], [ex + 0.4, py_ - 0.3, 0], [ex - 0.4, py_ - 0.3, 0],
                             color=INK, stroke_width=5))
    return VGroup(*parts)


class B55_TrustAnyway(Scene):
    def construct(self):
        px, py = -1.8, 0.7
        post = Line([px, py, 0], [px, -1.5, 0], color=DIM, stroke_width=8)
        foot = Line([px - 0.8, -1.5, 0], [px + 0.8, -1.5, 0], color=DIM, stroke_width=8)
        pivot = Dot([px, py, 0], radius=0.14, color=INK)
        title = T("trust anyway?", 40).move_to([px, 2.95, 0])
        l_lab = T("cost of checking", 34).move_to([px - 2.3, -2.2, 0])
        r_lab = T("cost of error", 34).move_to([px + 2.3, -2.2, 0])
        sc = a10_scale(0.0)
        self.add(post, foot, pivot, title)
        self.play(Create(sc), run_time=0.6)
        self.play(FadeIn(l_lab), FadeIn(r_lab), run_time=0.4)
        until(self, "checking costs", lead=0.3)
        self.play(Transform(sc, a10_scale(0.2)), run_time=0.7)
        until(self, "than being wrong", lead=0.3)
        self.play(Transform(sc, a10_scale(-0.2)), run_time=0.7)
        until(self, "Bear has no clean answer", lead=0.0)
        self.play(Transform(sc, a10_scale(0.05)), run_time=0.6)
        # what would change my mind: a schematic where confidence tracks truth
        until(self, "And he would change", lead=0.2)
        head = T("change my mind", 34).move_to([4.2, 2.35, 0])
        ax_x = Line([2.6, -0.9, 0], [5.8, -0.9, 0], color=DIM, stroke_width=5)
        ax_y = Line([2.6, -0.9, 0], [2.6, 1.8, 0], color=DIM, stroke_width=5)
        pts = [(2.6, -0.3), (3.4, 0.3), (4.2, 0.1), (5.0, 0.9), (5.8, 1.3)]
        truth = VGroup(*[Line([pts[i][0], pts[i][1], 0], [pts[i + 1][0], pts[i + 1][1], 0], color=INK, stroke_width=7) for i in range(4)])
        conf = VGroup(*[Line([pts[i][0], pts[i][1] + 0.3, 0], [pts[i + 1][0], pts[i + 1][1] + 0.3, 0], color=BAR1, stroke_width=7) for i in range(4)])
        cap = T("tracks truth", 34).move_to([4.2, -1.45, 0])
        sch = T("schematic", 32, DIM).move_to([4.2, -2.1, 0])
        self.play(FadeIn(head), Create(ax_x), Create(ax_y), run_time=0.5)
        self.play(Create(truth), run_time=0.7)
        self.play(Create(conf), run_time=0.7)
        self.play(FadeIn(cap), FadeIn(sch), run_time=0.4)
        done(self)
