from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('pong')
screen.tracer()

l_pad = Paddle((-350,0))


r_pad = Paddle((350,0))

ball = Ball()

score = Scoreboard()

ball.pu()

screen.listen()
screen.onkey(key='w',fun=l_pad.go_up)
screen.onkey(key='s',fun=l_pad.go_down)
screen.onkey(key='u',fun=r_pad.go_up)
screen.onkey(key='d',fun=r_pad.go_down)




is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball .ycor() < -280:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_pad)<50 and ball.xcor() >320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # right paddle misses the ball
    if ball.xcor() > 380:

        ball.reset_ball()
        score.l_point()



    # left  paddle misses the ball
    if ball.xcor() < -380:

        ball.reset_ball()
        score.r_point()



screen.exitonclick()


