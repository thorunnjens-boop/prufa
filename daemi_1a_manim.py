"""Manim Community: Dæmi 1a — flatarmál milli ferla.
Keyrsla: manim -pqh daemi_1a_manim.py Daemi1A
Engin talsetning er innbyggð; biðtímar henta til að bæta henni við.
"""
from manim import *

config.background_color = "#101725"


class Daemi1A(Scene):
    def construct(self):
        title = Text("Dæmi 1a – Flatarmál milli ferla", font_size=33, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))

        # 1. Teiknum bæði föllin.
        axes = Axes(
            x_range=[-4.2, 3.2, 1],
            y_range=[-5, 8.5, 2],
            x_length=7.0,
            y_length=4.5,
            tips=False,
            axis_config={"color": GREY_B},
        ).shift(LEFT * 2.55 + DOWN * 0.35)
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        line = axes.plot(lambda x: x + 1, x_range=[-4, 3], color=BLUE_C)
        parabola = axes.plot(lambda x: 7 - x*x, x_range=[-3.65, 3], color=ORANGE)
        line_tag = MathTex(r"y=x+1", color=BLUE_C, font_size=32).to_corner(DR).shift(UP * 1.1)
        para_tag = MathTex(r"y=7-x^2", color=ORANGE, font_size=32).next_to(line_tag, UP, buff=0.25)
        graph_group = VGroup(axes, axis_labels, line, parabola)
        self.play(Create(axes), FadeIn(axis_labels))
        self.play(Create(line), Write(line_tag))
        self.play(Create(parabola), Write(para_tag))
        self.wait(1)

        # 2. Finnum skurðpunktana í hægri dálki.
        heading = Text("1. Skurðpunktar", font_size=27).move_to(RIGHT * 3.3 + UP * 2.10)
        calculations = [
            r"x+1=7-x^2",
            r"x^2+x-6=0",
            r"(x+3)(x-2)=0",
            r"x=-3 \quad\text{eða}\quad x=2",
        ]
        eqs = VGroup(*[MathTex(s, font_size=30) for s in calculations])
        eqs.arrange(DOWN, buff=0.28, aligned_edge=LEFT).next_to(heading, DOWN, buff=0.32)
        eqs.shift(RIGHT * (0.45 - eqs.get_right()[0]))
        self.play(Write(heading))
        for eq in eqs:
            self.play(Write(eq), run_time=1.15)
            self.wait(0.4)

        dots = VGroup(
            Dot(axes.c2p(-3, -2), color=YELLOW, radius=0.09),
            Dot(axes.c2p(2, 3), color=YELLOW, radius=0.09),
        )
        dot_labels = VGroup(
            MathTex(r"(-3,-2)", font_size=26).next_to(dots[0], DOWN + LEFT, buff=0.15),
            MathTex(r"(2,3)", font_size=26).next_to(dots[1], RIGHT, buff=0.15),
        )
        self.play(FadeIn(dots), Write(dot_labels))
        self.wait(1)

        # 3. Prófum x=0 og litum flatarmálið.
        self.play(FadeOut(eqs), FadeOut(heading))
        heading2 = Text("2. Efra fall – neðra fall", font_size=26).move_to(RIGHT * 3.35 + UP * 2.10)
        test1 = MathTex(r"x=0:\quad 7-0^2=7", font_size=30)
        test2 = MathTex(r"x=0:\quad 0+1=1", font_size=30)
        verdict = MathTex(r"7-x^2 > x+1", font_size=34, color=YELLOW)
        right_group = VGroup(test1, test2, verdict).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        right_group.next_to(heading2, DOWN, buff=0.45)
        right_group.shift(RIGHT * (0.55 - right_group.get_right()[0]))
        self.play(Write(heading2), Write(test1))
        self.play(Write(test2))
        self.play(Write(verdict))
        shaded = axes.get_area(parabola, x_range=[-3, 2], bounded_graph=line,
                               color=TEAL, opacity=0.47)
        self.play(FadeIn(shaded), run_time=1.6)
        self.wait(1.5)

        # 4. Eftir myndrænu skýringuna fær heildunin allan skjáinn.
        self.play(FadeOut(VGroup(graph_group, shaded, dots, dot_labels,
                                 line_tag, para_tag, heading2, right_group)), run_time=0.8)
        heading3 = Text("3. Reiknum flatarmálið", font_size=32).next_to(title, DOWN, buff=0.35)
        self.play(Write(heading3))
        math_lines = [
            r"A=\int_{-3}^{2}\left[(7-x^2)-(x+1)\right] \,dx",
            r"A=\int_{-3}^{2}(6-x-x^2)\,dx",
            r"A=\left[6x-\frac{x^2}{2}-\frac{x^3}{3}\right]_{-3}^{2}",
            r"A=\left(12-2-\frac{8}{3}\right)-\left(-18-\frac{9}{2}+9\right)",
            r"A=\frac{22}{3}+\frac{27}{2}",
            r"A=\frac{44+81}{6}",
            r"A=\frac{125}{6}",
        ]
        # Ein lína í einu á skjánum, með fyrri línu fyrir ofan.
        current = None
        for i, latex in enumerate(math_lines):
            new = MathTex(latex, font_size=38 if i < 4 else 45)
            if new.width > 12.2:
                new.scale_to_fit_width(12.2)
            new.move_to(ORIGIN + DOWN * 0.1)
            if current is None:
                self.play(Write(new), run_time=2)
            else:
                previous = current.copy().scale(0.65).set_opacity(0.55)
                previous.move_to(UP * 1.05)
                self.play(Transform(current, previous), FadeIn(new, shift=UP * 0.15), run_time=1.0)
                self.play(FadeOut(current), run_time=0.35)
            current = new
            self.wait(1.25)

        answer_box = SurroundingRectangle(current, color=YELLOW, buff=0.22)
        self.play(Create(answer_box), current.animate.set_color(YELLOW))
        self.wait(3)
