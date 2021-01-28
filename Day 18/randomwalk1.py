import random
import turtle as t
from turtle import  Turtle,Screen


t.colormode(255)

tim = Turtle()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color= (r, g, b)
    return random_color

#colors = ["red", "orange", "blue",  "yellow", "purple","coral"]
directions = [0,90,180,270]


for _ in range(300):
    tim.pensize(10)
    #(r,g,b) = random_color()
    tim.color(random_color())
    tim.fd(30)
    tim.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()

