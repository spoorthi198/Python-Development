import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
score = Scoreboard()

player = Player()
screen.listen()
screen.onkey(player.go_up,"Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    # detect collision between the car

    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False

            score.game_over()

    # detect finish line
    if player.is_on_finish_line():
        player.go_to_start_line()
        car.level_up
        score.update_score
        score.increase_level()

screen.exitonclick()