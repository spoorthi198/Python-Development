from turtle import Turtle, Screen

turtle_the_timmy = Turtle()
turtle_the_timmy.shape("turtle")
turtle_the_timmy.color("turquoise")

# turtle_the_timmy.fd(100)
# turtle_the_timmy.rt(90)
# turtle_the_timmy.fd(100)
# turtle_the_timmy.lt(270)
# turtle_the_timmy.fd(100)
# turtle_the_timmy.rt(90)
# turtle_the_timmy.fd(100)

for _ in range(4):
    turtle_the_timmy.fd(100)
    turtle_the_timmy.lt(90)





screen = Screen()
screen.exitonclick()
