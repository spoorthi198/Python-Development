from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape()
        self.pu()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.goto(-100, 200)
        self.write(f'{self.l_score}', align="center", font=("Arial", 24, "normal"))
        self.goto(100, 200)
        self.write(f'{self.r_score}', align="center", font=("Arial", 24, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_score()

