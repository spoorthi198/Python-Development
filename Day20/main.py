from turtle import Screen
from snakeproperties import Snake
from food import Food
from scoreboard import Score


import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer()

snake = Snake()
foodie = Food()
score1 = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(1)
    snake.move()

    # detect collision with food
    if snake.head.distance(foodie) < 15:
        foodie.refresh()
        snake.extend()
        score1.increase_score()
        score1.update_scoreboard()
    # detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score1.game_over()
    # detect collision with wall
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score1.game_over()


screen.exitonclick()

