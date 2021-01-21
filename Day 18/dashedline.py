from turtle import Turtle,Screen

tim = Turtle()

for _ in range(10):
    tim.fd(10)
    tim.pu()
    tim.fd(10)
    tim.pd()
    

scr = Screen()
scr.exitonclick()