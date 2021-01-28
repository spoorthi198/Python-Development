import colorgram
import random
from turtle import Turtle,Screen
import turtle as tt
tim = Turtle()

# Extract 6 colors from an image.
colors = colorgram.extract('hirst.gif', 30)
colors_list =[(222, 152, 103), (233, 237, 240),
 (128, 172, 199), (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157),
 (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70), (142, 86, 60),
 (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75),
 (213, 222, 213), (1, 98, 119),(54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]

tt.colormode(255)
tim.setheading(225)
tim.pu()
tim.hideturtle()
tim.fd(300)
tim.setheading(0)
tim.speed("fastest")

num_of_dot = 100
for dot_count in range(1,num_of_dot+1):
    clr=random.choice(colors_list)
    tim.dot(20, clr)
    tim.fd(50)
    if dot_count %10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

# rgb_colors = []
# def extract_color():
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r,g,b)
#         rgb_colors.append(new_color)
#     print(rgb_colors)
#
#
# extract_color()

screen = tt.Screen()
screen.exitonclick()