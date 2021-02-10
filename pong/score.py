from turtle import Turtle
P1_ALIGNMENT = (-200, 250)
P2_ALIGNMENT = (200, 250)
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self, player):
        super().__init__()
        self.score = 0
        self.player = player
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        if self.player == "1":
            self.goto(P1_ALIGNMENT)
            self.write(f"P1: {self.score}", align="center", font=FONT)
        else:
            self.goto(P2_ALIGNMENT)
            self.write(f"P2: {self.score}", align="center", font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)