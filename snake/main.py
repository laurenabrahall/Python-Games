from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score

# Screen Setup
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake V1")

# Create game elements
snake = Snake()
food = Food()
score = Score()

# Keystroke behaviour
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()

# Game State
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    # Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
