import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# xcor=300
cars = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()

    # when turtle reaches finish line
    if player.ycor() >= 280:
        cars.level_up()
        score.inc_level()
        player.refresh()
        # SLEEP *= 0.9

    # if the turtle collides with a car
    for car in cars.all_cars:
        if car.distance(player) < 25:
            score.game_over()
            game_is_on = False

screen.exitonclick()
