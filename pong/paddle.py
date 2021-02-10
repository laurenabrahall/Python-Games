from turtle import Turtle

STARTING_POSITIONS = [(-350, 0), (350, 0)]
UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.start_position = start_position
        self.create_paddle()

    def create_paddle(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(self.start_position)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
