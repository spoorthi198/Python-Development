from turtle import Turtle



FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(-260,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Level = {self.level}', align='Left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME_OVER',align= 'center',font=FONT )
