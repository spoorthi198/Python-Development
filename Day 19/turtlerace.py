from turtle import Turtle,Screen
import random
colors = ["red","violet","blue","orange","yellow","coral"]

y_pos = [-70,-40,-10,20,50,80]
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)
print(all_turtles)
user_bet = screen.textinput(title="Turtle color",prompt="Which Turtle do you bet the race?")
print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")









screen.exitonclick()