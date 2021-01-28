import random
from turtle import Turtle,Screen




tim = Turtle()

colors = ["red", "orange", "blue",  "yellow", "purple","coral"]
directions = [0,90,180,270]


for _ in range(300):
    tim.begin_fill()
    if tim.filling():
        tim.pensize(10)
        tim.color(random.choice(colors))
        tim.fd(30)
        tim.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()

