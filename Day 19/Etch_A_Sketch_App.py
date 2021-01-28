from turtle import Turtle,Screen
import turtle as tt



def forward():
    tim.fd(10)

def backward():
    tim.backward(10)

def clockwise():
    tim.lt(10)


def clear():
    tim.clear()
    tim.pu()

    tim.home()
    tim.pd()


def anti_clock():
    tim.rt(10)


tim = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key="w",fun=forward)
screen.onkey(key="s",fun=backward)
screen.onkey(key="c",fun=clockwise)
screen.onkey(key="d",fun=clear)
screen.onkey(key="a",fun=anti_clock)
screen= tt.exitonclick()







