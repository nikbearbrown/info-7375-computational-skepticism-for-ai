"""ACT VIII · Five things a supervisor does (B38-B43)   ACT IX · The fluency trap (B44-B49)

Cast, Act VIII: the FIVE SLOTS. B38 stands them up empty; B39-B42 show one small five-dot strip (top right) whose lit dot
marks which capacity is on screen; B43 lights all five and converges them on one decision.
Cast, Act IX: NODES and ARROWS (output -> confidence -> evaluation), a pair of sliders, a gate with a missing check.
Numbers on screen: only "5%" (spoken in B42, the chapter's own example), tagged "illustrative". No people tokens.
"""


def a5_card(w, h, color=DIM, sw=4, r=0.2):
    return RoundedRectangle(width=w, height=h, corner_radius=r, fill_opacity=0, stroke_color=color, stroke_width=sw)


def a5_ghost_lines(cx, cy, w, n=3, gap=0.3, color=GHOST):
    """n ghost text lines (the shape of prose, no words) centred on (cx, cy)."""
    return VGroup(*[Line([cx - w / 2, cy + (n - 1) * gap / 2 - i * gap, 0], [cx + w / 2 - (0.6 if i == n - 1 else 0), cy + (n - 1) * gap / 2 - i * gap, 0],
                         color=color, stroke_width=5) for i in range(n)])


def a5_strip(active):
    """Five small dots, top right. Dots before `active` are done (ghost), `active` is lit (terracotta), the rest outline."""
    out = VGroup()
    for i in range(5):
        x = 2.4 + 0.8 * i
        if i == active:
            d = Circle(radius=0.19, fill_color=TERRA, fill_opacity=1, stroke_color=TERRA, stroke_width=2)
        elif i < active:
            d = Circle(radius=0.19, fill_color=GHOST, fill_opacity=1, stroke_color=DIM, stroke_width=3)
        else:
            d = Circle(radius=0.19, fill_opacity=0, stroke_color=DIM, stroke_width=3)
        out.add(d.move_to([x, 3.0, 0]))
    return out


def a5_title(s):
    return T(s, 40).move_to([-3.6, 3.0, 0])


def a5_dial(cx, cy, band_frac, needle_frac):
    """Semicircle dial. Returns (base, band, needle_at_up, pivot, angle_to_rotate)."""
    c = np.array([cx, cy, 0.0])
    base = Arc(radius=1.5, start_angle=PI, angle=-PI, color=GHOST, stroke_width=16).move_arc_center_to(c)
    band = Arc(radius=1.5, start_angle=PI, angle=-PI * band_frac, color=INK, stroke_width=16).move_arc_center_to(c)
    needle = Line(c, c + np.array([0, 1.3, 0]), color=INK, stroke_width=7)
    pivot = Dot(c, radius=0.13, color=INK)
    return base, band, needle, pivot, PI * (0.5 - needle_frac), c


# ═════════════════════════════ ACT VIII ═════════════════════════════

class B38_FiveSlots(Scene):
    def construct(self):
        head = T("The supervisor", 40).move_to([0, 2.7, 0])
        base = Line([-5.9, -1.9, 0], [5.9, -1.9, 0], color=GHOST, stroke_width=5)
        self.add(head, base)
        xs = [-4.6, -2.3, 0.0, 2.3, 4.6]
        slots = [a5_card(1.9, 2.2, DIM, 5).move_to([x, 0.1, 0]) for x in xs]
        self.play(LaggedStart(*[Create(s) for s in slots], lag_ratio=0.25), run_time=1.5)
        until(self, "Capacities", lead=0.2)
        until(self, "things a person can do", lead=0.1)
        holes = [DashedVMobject(Circle(radius=0.55, color=DIM, stroke_width=4).move_to([x, 0.1, 0]), num_dashes=14, dashed_ratio=0.55) for x in xs]
        self.play(LaggedStart(*[Create(h) for h in holes], lag_ratio=0.15), run_time=0.9)
        until(self, "There are five", lead=0.45)
        nums = [T(str(i + 1), 44).move_to([x, -1.4, 0]) for i, x in enumerate(xs)]
        self.play(LaggedStart(*[FadeIn(n) for n in nums], lag_ratio=0.1), run_time=0.6)
        dot = Dot([xs[4] + 0.75, 1.0, 0], radius=0.13, color=TERRA)
        self.play(GrowFromCenter(dot), run_time=0.3)
        done(self)


class B39_Twitch(Scene):
    def construct(self):
        title, strip = a5_title("Plausibility auditing"), a5_strip(0)
        cloud = Circle(radius=2.0, color=DIM, stroke_width=5).move_to([-1.9, -0.35, 0])
        spots = [(-2.6, 0.2), (-1.5, 0.7), (-2.2, -0.6), (-1.1, -0.1), (-1.9, -1.2), (-0.8, -0.9), (-2.7, 0.9), (-1.6, 0.0), (-1.4, -1.6)]
        dots = VGroup(*[Dot([x, y, 0], radius=0.1, color=BAR2) for x, y in spots])
        k_l = T("known world", 36, DIM).move_to([-1.9, -2.75, 0])
        self.add(title, strip, cloud, dots, k_l)
        until(self, "the kind of thing that could be true", lead=0.3)
        o_l = T("score", 36).move_to([3.9, 0.95, 0])
        out = Dot([5.0, 0.35, 0], radius=0.2, color=INK)
        self.play(FadeIn(out), FadeIn(o_l), run_time=0.3)
        self.play(out.animate.move_to([2.3, -0.35, 0]), run_time=0.9)
        until(self, "feels a twitch", lead=0.2)
        for dx in (-0.16, 0.32, -0.32, 0.16):
            self.play(out.animate.shift(RIGHT * dx), run_time=0.09)
        ring1 = Circle(radius=0.5, color=INK, stroke_width=6).move_to(out.get_center())
        ring2 = Circle(radius=0.85, color=DIM, stroke_width=4).move_to(out.get_center())
        mark = Dot([2.3, 0.62, 0], radius=0.1, color=TERRA)
        t_l = T("twitch", 38).move_to([4.6, -1.35, 0])
        self.play(Create(ring1), run_time=0.3)
        self.play(Create(ring2), GrowFromCenter(mark), FadeIn(t_l), run_time=0.4)
        done(self)


class B40_TwoQuestions(Scene):
    def construct(self):
        title, strip = a5_title("Problem formulation"), a5_strip(1)
        q1 = a5_card(4.8, 1.5, INK, 6).move_to([-2.4, 1.0, 0])
        q1t = T("Which category?", 40).move_to([-2.4, 1.0, 0])
        q2 = a5_card(4.8, 1.5, DIM, 4).move_to([-2.4, -1.2, 0])
        q2t = T("Life-threatening?", 40, DIM).move_to([-2.4, -1.2, 0])
        self.add(title, strip, q1, q1t)
        box1 = Square(side_length=1.0, color=DIM, stroke_width=5).move_to([2.0, 1.0, 0])
        self.add(box1)
        until(self, "The triage system answered", lead=0.2)
        self.play(Create(check(2.0, 1.0, 0.3, INK, 10)), run_time=0.5)
        a1 = T("answered", 38).move_to([4.5, 1.0, 0])
        self.play(FadeIn(a1), run_time=0.3)
        until(self, "The clinical question was", lead=0.4)
        self.play(FadeIn(q2t), Create(DashedVMobject(q2.copy(), num_dashes=26, dashed_ratio=0.55)), run_time=0.7)
        box2 = Square(side_length=1.0, color=DIM, stroke_width=5).move_to([2.0, -1.2, 0])
        self.play(Create(box2), run_time=0.4)
        until(self, "never asked", lead=0.4)
        a2 = T("never asked", 38).move_to([4.6, -1.2, 0])
        gap = Dot([2.0, -1.2, 0], radius=0.14, color=TERRA)
        self.play(FadeIn(a2), GrowFromCenter(gap), run_time=0.4)
        done(self)


class B41_FourOptions(Scene):
    def construct(self):
        title, strip = a5_title("Tool orchestration"), a5_strip(2)
        task = a5_card(3.0, 1.7, DIM, 6).move_to([-4.35, -0.1, 0])
        task_t = T("Sub-problem", 36).move_to([-4.35, -0.1, 0])
        self.add(title, strip, task, task_t)
        labels = ["AI model", "A person", "Second model", "No tool yet"]
        ys = [1.55, 0.35, -0.85, -2.05]
        cards, texts, arrows = [], [], []
        until(self, "An AI, a person", lead=0.3)
        for i in range(4):
            c = a5_card(3.6, 0.95, DIM, 4).move_to([2.5, ys[i], 0])
            t = T(labels[i], 38).move_to([2.5, ys[i], 0])
            a = Arrow([-2.75, -0.1, 0], [0.55, ys[i], 0], buff=0, color=DIM, stroke_width=4, tip_length=0.18)
            cards.append(c); texts.append(t); arrows.append(a)
            if i < 3:
                self.play(Create(a), Create(c), FadeIn(t), run_time=0.45)
        until(self, "the hardest call of all", lead=0.3)
        self.play(Create(arrows[3]), Create(cards[3]), FadeIn(texts[3]), run_time=0.5)
        until(self, "Saying we should not deploy", lead=0.3)
        ring = a5_card(3.9, 1.2, INK, 8).move_to([2.5, ys[3], 0])
        spark = Dot([4.55, ys[3] + 0.55, 0], radius=0.13, color=TERRA)
        self.play(Create(ring), GrowFromCenter(spark), arrows[3].animate.set_color(INK).set_stroke(width=7), run_time=0.6)
        done(self)


class B42_SameNumber(Scene):
    def construct(self):
        title, strip = a5_title("Interpretive judgment"), a5_strip(3)
        hero = T("5%", 76).move_to([0, 1.95, 0])
        b1, band1, n1, p1, ang1, c1 = a5_dial(-3.2, -0.5, 0.45, 0.2)
        b2, band2, n2, p2, ang2, c2 = a5_dial(3.2, -0.5, 0.08, 0.2)
        l1 = T("Spam filter", 40).move_to([-3.2, -1.4, 0])
        l2 = T("Cancer screen", 40).move_to([3.2, -1.4, 0])
        cap = T("illustrative", 32, DIM).move_to([0, -3.0, 0])
        self.add(title, strip, hero, b1, b2, l1, l2, cap)
        self.play(Create(band1), Create(band2), run_time=0.5)
        until(self, "A five percent false-positive rate", lead=0.2)
        self.play(FadeIn(n1), FadeIn(p1), FadeIn(n2), FadeIn(p2), run_time=0.3)
        self.play(Rotate(n1, angle=ang1, about_point=c1), Rotate(n2, angle=ang2, about_point=c2), run_time=0.9)
        until(self, "suits a spam filter", lead=0.2)
        self.play(Create(check(-3.2, -2.25, 0.34, INK, 10)), run_time=0.5)
        until(self, "catastrophic", lead=0.3)
        x1 = Line([2.85, -1.95, 0], [3.55, -2.65, 0], color=INK, stroke_width=10)
        x2 = Line([2.85, -2.65, 0], [3.55, -1.95, 0], color=INK, stroke_width=10)
        self.play(Create(x1), Create(x2), run_time=0.5)
        done(self)


class B43_OneDecision(Scene):
    def construct(self):
        title = T("Executive integration", 40).move_to([-3.6, 3.0, 0])
        names = ["Plausibility", "Formulation", "Tools", "Judgment", "Integration"]
        ys = [1.9, 0.95, 0.0, -0.95, -1.9]
        self.add(title)
        until(self, "combining tools", lead=0.2)
        nodes, labs = [], []
        for i in range(5):
            n = Circle(radius=0.34, fill_color=TERRA, fill_opacity=1, stroke_color=TERRA, stroke_width=2).move_to([-3.1, ys[i], 0])
            nodes.append(n)
            labs.append(T(names[i], 36).move_to([-5.0, ys[i], 0]))
        self.play(LaggedStart(*[FadeIn(VGroup(n, l)) for n, l in zip(nodes, labs)], lag_ratio=0.25), run_time=1.3)
        until(self, "one decision", lead=0.2)
        box = a5_card(3.0, 1.5, INK, 7).move_to([3.5, 0, 0])
        box_t = T("Decision", 40).move_to([3.5, 0, 0])
        arrows = [Arrow([-2.6, ys[i], 0], [1.85, ys[i] * 0.35, 0], buff=0, color=DIM, stroke_width=4, tip_length=0.16) for i in range(5)]
        self.play(Create(box), FadeIn(box_t), run_time=0.5)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.15), run_time=1.2)
        until(self, "Somewhere the buck must stop", lead=0.2)
        pole = Line([3.5, 0.75, 0], [3.5, 1.75, 0], color=INK, stroke_width=6)
        flag = Polygon([3.5, 1.75, 0], [4.4, 1.5, 0], [3.5, 1.25, 0], fill_color=GHOST, fill_opacity=1, stroke_color=INK, stroke_width=4)
        owner = Dot([3.5, 1.75, 0], radius=0.13, color=TERRA)
        o_l = T("owner", 36).move_to([5.3, 1.5, 0])
        self.play(Create(pole), Create(flag), GrowFromCenter(owner), FadeIn(o_l), run_time=0.6)
        until(self, "you have found a gap", lead=0.3)
        hole = DashedVMobject(Circle(radius=0.34, color=DIM, stroke_width=5).move_to([-3.1, ys[2], 0]), num_dashes=12, dashed_ratio=0.55)
        g_l = T("gap", 40).move_to([-0.6, 0.0, 0])
        self.play(FadeOut(nodes[2]), FadeOut(arrows[2]), Create(hole), FadeIn(g_l), run_time=0.7)
        done(self)


# ═════════════════════════════ ACT IX ═════════════════════════════

class B44_TwoCards(Scene):
    def construct(self):
        head = T("Botspeak", 40).move_to([0, 3.0, 0])
        c1 = a5_card(3.0, 1.9, INK, 6).move_to([-4.5, 0.5, 0])
        t1 = T("Strategic\ndelegation", 38).move_to([-4.5, 0.5, 0])
        self.add(head)
        until(self, "Strategic delegation", lead=0.3)
        ai = a5_card(1.8, 1.3, DIM, 5).move_to([0, 0.5, 0])
        ai_t = T("AI", 42).move_to([0, 0.5, 0])
        a_out = Arrow([-2.95, 0.5, 0], [-1.0, 0.5, 0], buff=0, color=INK, stroke_width=6, tip_length=0.2)
        self.play(Create(c1), FadeIn(t1), run_time=0.5)
        self.play(Create(a_out), Create(ai), FadeIn(ai_t), run_time=0.6)
        until(self, "Critical evaluation", lead=0.5)
        c2 = a5_card(3.0, 1.9, INK, 6).move_to([4.5, 0.5, 0])
        t2 = T("Critical\nevaluation", 38).move_to([4.5, 0.5, 0])
        a_in = Arrow([1.0, 0.5, 0], [2.95, 0.5, 0], buff=0, color=INK, stroke_width=6, tip_length=0.2)
        self.play(Create(a_in), Create(c2), FadeIn(t2), run_time=0.6)
        until(self, "criteria you set before", lead=0.3)
        sheet = a5_card(1.7, 1.4, DIM, 4).move_to([4.5, -2.1, 0])
        lines = a5_ghost_lines(4.5, -2.1, 1.1, 3, 0.3, DIM)
        s_l = T("set first", 36, DIM).move_to([1.9, -2.1, 0])
        up = Arrow([4.5, -1.35, 0], [4.5, -0.55, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.16)
        self.play(Create(sheet), Create(lines), FadeIn(s_l), Create(up), run_time=0.7)
        done(self)


class B45_TwoSteps(Scene):
    def construct(self):
        xs = [-4.5, 0.0, 4.5]
        nodes = [Circle(radius=0.85, color=INK if i == 0 else DIM, stroke_width=6 if i == 0 else 5).move_to([xs[i], 1.1, 0]) for i in range(3)]
        wave = ParametricFunction(lambda t: np.array([xs[0] + t, 1.1 + 0.28 * np.sin(t * 5.2), 0]), t_range=[-0.55, 0.55], color=INK, stroke_width=6)
        self.add(nodes[0], wave)
        l1 = T("Fluent\noutput", 36).move_to([xs[0], -0.55, 0])
        self.add(l1)
        until(self, "the more confident you are in the output", lead=0.4)
        a1 = Arrow([-3.5, 1.1, 0], [-1.0, 1.1, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)
        self.play(Create(a1), Create(nodes[1]), run_time=0.7)
        g1 = Arc(radius=0.5, start_angle=PI, angle=-PI * 0.8, color=INK, stroke_width=7).move_arc_center_to([xs[1], 0.95, 0])
        self.play(Create(g1), FadeIn(T("Confidence\nin answer", 36).move_to([xs[1], -0.55, 0])), run_time=0.6)
        until(self, "Then that confidence raises", lead=0.3)
        a2 = Arrow([1.0, 1.1, 0], [3.5, 1.1, 0], buff=0, color=INK, stroke_width=9, tip_length=0.3)
        tdot = Dot([2.25, 1.75, 0], radius=0.15, color=TERRA)
        self.play(Create(a2), Create(nodes[2]), GrowFromCenter(tdot), run_time=0.7)
        g2 = Arc(radius=0.5, start_angle=PI, angle=-PI * 0.9, color=INK, stroke_width=7).move_arc_center_to([xs[2], 0.95, 0])
        g2b = Arc(radius=0.3, start_angle=PI, angle=-PI * 0.9, color=DIM, stroke_width=6).move_arc_center_to([xs[2], 0.95, 0])
        self.play(Create(g2), Create(g2b), FadeIn(T("Confidence\nin judgment", 36).move_to([xs[2], -0.55, 0])), run_time=0.6)
        until(self, "any answer of the same shape", lead=0.4)
        sq = [Square(side_length=0.8, color=DIM, stroke_width=5).move_to([-1.5 + 1.5 * i, -2.45, 0]) for i in range(3)]
        lab = T("same shape", 36, DIM).move_to([4.2, -2.45, 0])
        self.play(LaggedStart(*[Create(s) for s in sq], lag_ratio=0.25), FadeIn(lab), run_time=0.8)
        self.play(LaggedStart(*[Create(check(-1.5 + 1.5 * i, -2.45, 0.22, INK, 8)) for i in range(3)], lag_ratio=0.3), run_time=0.9)
        done(self)


class B46_FormContent(Scene):
    def construct(self):
        head = T("Independent", 40).move_to([-3.6, 3.0, 0])
        # two sliders (left)
        tr1 = Line([-5.9, 1.5, 0], [-1.7, 1.5, 0], color=BAR1, stroke_width=8)
        tr2 = Line([-5.9, -0.5, 0], [-1.7, -0.5, 0], color=BAR1, stroke_width=8)
        k1 = Dot([-3.8, 1.5, 0], radius=0.22, color=INK)
        k2 = Dot([-3.8, -0.5, 0], radius=0.22, color=INK)
        n1 = T("Form", 40).move_to([-3.8, 2.2, 0])
        n2 = T("Content", 40).move_to([-3.8, 0.2, 0])
        e1a, e1b = T("plain", 32, DIM).move_to([-5.3, 0.85, 0]), T("fluent", 32, DIM).move_to([-2.3, 0.85, 0])
        e2a, e2b = T("wrong", 32, DIM).move_to([-5.3, -1.15, 0]), T("right", 32, DIM).move_to([-2.3, -1.15, 0])
        # plane (right)
        plane = Square(side_length=3.6, color=DIM, stroke_width=5).move_to([3.6, 0, 0])
        vx = Line([3.6, -1.8, 0], [3.6, 1.8, 0], color=GHOST, stroke_width=4)
        hx = Line([1.8, 0, 0], [5.4, 0, 0], color=GHOST, stroke_width=4)
        self.add(head, tr1, tr2, n1, n2, e1a, e1b, e2a, e2b, k1, k2, plane, vx, hx)
        until(self, "Form and content are independent", lead=0.2)
        self.play(k1.animate.move_to([-2.4, 1.5, 0]), run_time=0.7)
        self.play(k2.animate.move_to([-5.0, -0.5, 0]), run_time=0.7)
        until(self, "AI broke that link", lead=0.3)
        self.play(k1.animate.move_to([-5.0, 1.5, 0]), k2.animate.move_to([-2.4, -0.5, 0]), run_time=0.8)
        until(self, "maximally fluent and maximally wrong", lead=1.0)
        self.play(k1.animate.move_to([-2.4, 1.5, 0]), k2.animate.move_to([-5.0, -0.5, 0]), run_time=0.8)
        pt = Dot([4.9, -1.2, 0], radius=0.2, color=TERRA)
        ring = Circle(radius=0.45, color=INK, stroke_width=6).move_to([4.9, -1.2, 0])
        c_l = T("fluent, wrong", 36).move_to([3.6, -2.45, 0])
        self.play(GrowFromCenter(pt), Create(ring), FadeIn(c_l), run_time=0.6)
        done(self)


class B47_MissingCheck(Scene):
    def construct(self):
        report = a5_card(4.6, 1.8, DIM, 6).move_to([-3.6, 0.55, 0])
        q = T("Email account RESET\ncompleted", 34).move_to([-3.6, 0.55, 0])
        r_l = T("report", 36).move_to([-3.6, 2.0, 0])
        self.add(report, q, r_l)
        src = T("Shapira et al., 2026", 32, DIM).move_to([0, -3.0, 0])
        self.add(src)
        until(self, "fluent and well formed", lead=0.3)
        path = Line([-1.2, 0.55, 0], [2.2, 0.55, 0], color=DIM, stroke_width=5)
        gate = DashedVMobject(Circle(radius=0.65, color=DIM, stroke_width=5).move_to([0.2, 0.55, 0]), num_dashes=16, dashed_ratio=0.55)
        g_l = T("no check", 36, DIM).move_to([0.2, 1.75, 0])
        world = a5_card(2.4, 1.8, DIM, 6).move_to([4.7, 0.55, 0])
        w_l = T("world", 36).move_to([4.7, 2.0, 0])
        env = VGroup(Rectangle(width=1.2, height=0.8, color=INK, stroke_width=5),
                     Line([-0.6, 0.4, 0], [0, 0.0, 0], color=INK, stroke_width=5), Line([0, 0.0, 0], [0.6, 0.4, 0], color=INK, stroke_width=5)).move_to([4.7, 0.55, 0])
        self.play(Create(path), Create(gate), FadeIn(g_l), run_time=0.7)
        self.play(Create(world), FadeIn(w_l), Create(env), run_time=0.7)
        until(self, "The prose did the checking", lead=0.3)
        pulse = Dot([-1.2, 0.55, 0], radius=0.17, color=TERRA)
        self.play(FadeIn(pulse), run_time=0.15)
        self.play(pulse.animate.move_to([2.2, 0.55, 0]), run_time=1.1)
        until(self, "not let fluency do epistemic work", lead=0.5)
        still = T("still there", 36).move_to([4.7, -1.1, 0])
        self.play(FadeIn(still), Indicate(env, color=INK, scale_factor=1.15), run_time=0.7)
        done(self)


class B48_OrderOfOperations(Scene):
    def construct(self):
        head = T("Order", 40).move_to([0, 3.0, 0])
        self.add(head)
        n1, n2, n3 = [T(s, 46).move_to([x, 2.0, 0]) for s, x in zip("123", (-4.6, -0.6, 3.5))]
        crit = a5_card(2.8, 1.9, INK, 6).move_to([-4.6, 0.2, 0])
        crit_l = a5_ghost_lines(-4.6, 0.2, 1.6, 3, 0.32, DIM)
        c_t = T("criterion", 36).move_to([-4.6, -1.4, 0])
        self.add(n1)
        until(self, "write down what a wrong answer would look like", lead=0.6)
        body = RoundedRectangle(width=0.8, height=0.6, corner_radius=0.08, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([-3.6, 0.9, 0])
        shackle = Arc(radius=0.22, start_angle=0, angle=PI, color=INK, stroke_width=6).move_arc_center_to([-3.6, 1.18, 0])
        self.play(Create(crit), Create(crit_l), FadeIn(c_t), run_time=0.6)
        self.play(Create(body), Create(shackle), run_time=0.4)
        until(self, "Then read it", lead=0.3)
        a1 = Arrow([-3.0, 0.2, 0], [-1.9, 0.2, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.18)
        out = a5_card(2.0, 1.9, DIM, 5).move_to([-0.6, 0.2, 0])
        out_l = a5_ghost_lines(-0.6, 0.2, 1.2, 3, 0.32, GHOST)
        o_t = T("output", 36).move_to([-0.6, -1.4, 0])
        self.play(FadeIn(n2), Create(a1), Create(out), Create(out_l), FadeIn(o_t), run_time=0.8)
        until(self, "record pass, fail, or unknown", lead=0.5)
        a2 = Arrow([0.6, 0.2, 0], [1.6, 0.2, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.18)
        self.play(FadeIn(n3), Create(a2), run_time=0.4)
        for i, s in enumerate(["pass", "fail", "unknown"]):
            p = a5_card(2.6, 0.8, INK if s == "unknown" else DIM, 5).move_to([3.5, 1.0 - 1.0 * i, 0])
            t = T(s, 38).move_to([3.5, 1.0 - 1.0 * i, 0])
            self.play(Create(p), FadeIn(t), run_time=0.4)
        done(self)


class B49_Diverge(Scene):
    def construct(self):
        title = T("Where they part", 40).move_to([-3.6, 3.0, 0])
        ax = Arrow([-5.6, -2.3, 0], [5.8, -2.3, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)
        ay = Arrow([-5.6, -2.3, 0], [-5.6, 2.4, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)
        fam = T("familiar", 36, DIM).move_to([-4.1, -2.85, 0])
        edge = T("edge cases", 36, DIM).move_to([4.1, -2.85, 0])
        cap = T("schematic", 32, DIM).move_to([-4.2, 2.45, 0])
        self.add(title, ax, ay, fam, edge, cap)
        until(self, "learn to produce outputs that resemble correct ones", lead=0.5)

        def res(t):                 # resemblance stays high
            return np.array([t, 1.5 - 0.1 * (t + 5.0) / 10.0, 0])

        def cor(t):                 # correctness tracks it, then falls away at the edge
            f = 1.5 - 0.1 * (t + 5.0) / 10.0
            drop = 3.1 / (1.0 + np.exp(-(t - 2.2) * 2.2))
            return np.array([t, f - drop, 0])

        c_res = ParametricFunction(res, t_range=[-5.0, 5.0], color=INK, stroke_width=8)
        c_cor = ParametricFunction(cor, t_range=[-5.0, 5.0], color=BAR1, stroke_width=8)
        self.play(Create(c_res), Create(c_cor), run_time=2.6)
        r_l = T("sounds right", 36).move_to([-1.3, 2.2, 0])
        k_l = T("is right", 36, DIM).move_to([-3.3, -0.35, 0])
        self.play(FadeIn(r_l), FadeIn(k_l), run_time=0.4)
        until(self, "Where resemblance and correctness come apart", lead=0.4)
        gap = dim_arrow([5.15, 1.0, 0], [5.15, -1.45, 0], INK, 6)
        spark = Dot([5.15, -1.95, 0], radius=0.13, color=TERRA)
        self.play(Create(gap), GrowFromCenter(spark), run_time=0.6)
        done(self)
