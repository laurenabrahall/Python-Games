from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

PLAYER_1_START = (-350, 0)
PLAYER_2_START = (350, 0)

# Screen Setup
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong V1")

# Game elements
p1_paddle = Paddle(PLAYER_1_START)
p2_paddle = Paddle(PLAYER_2_START)
ball = Ball()
p1_score = Score(player="1")
p2_score = Score(player="2")


# Keystroke event handling
screen.listen()
screen.onkey(p1_paddle.up, "w")
screen.onkey(p1_paddle.down, "s")
screen.onkey(p2_paddle.up, "Up")
screen.onkey(p2_paddle.down, "Down")

# Game State
game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect paddle collision
    if (ball.distance(p2_paddle) < 50 and ball.xcor() > 320) or (ball.distance(p1_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect ball miss
    if ball.xcor() > 380:
        ball.reset()
        p1_score.increase()
    if ball.xcor() < -380:
        ball.reset()
        p2_score.increase()

screen.exitonclick()