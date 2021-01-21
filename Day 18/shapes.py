from turtle import  Turtle, Screen
import random

tim = Turtle()



def draw_shape(num_of_side):
    angle= 360/num_of_side
    for _ in range(num_of_side):
        tim.fd(100)
        tim.lt(angle)


for _ in range(3,11):
    draw_shape(_)
    color=random.choice(["red","green","orange","yellow","pink","coral"])
    tim.color(color)

# for _ in range (10):
#     tim.fd(100)
#     tim.lt(36)
# for _ in range(9):
#     tim.fd(100)
#     tim.lt(40)
# for _ in range (8):
#     tim.fd(100)
#     tim.lt(45)
# for _ in range (7):
#     tim.fd(100)
#     tim.lt(51)
# for _ in range (6):
#     tim.fd(100)
#     tim.lt(60)
# for _ in range (5):
#     tim.fd(100)
#     tim.lt(72)
# for _ in range (4):
#     tim.fd(100)
#     tim.lt(90)
# for _ in range(3):
#     tim.fd(100)
#     tim.lt(120)




screen = Screen()
screen.exitonclick()
