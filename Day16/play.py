
from turtle import  Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.fd(100)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
# my_screen.canvwidth(300)
my_screen.exitonclick()