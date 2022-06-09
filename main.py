import random
import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_level = Scoreboard()
moving_cars = CarManager()
screen.listen()
screen.onkey(fun=player.move,key="Up")

game_is_on = True
while game_is_on:

    time.sleep(player.pace)
    screen.update()
    moving_cars.move()
    for car in moving_cars.cars:
        if car.distance(player) < 19:
            game_is_on = False
            game_level.game_over()
    if moving_cars.cars[len(moving_cars.cars)-1].xcor() < random.randint(180,220):
        moving_cars.generator()

    if player.ycor() > FINISH_LINE_Y:
        player.refresh()
        game_level.level_up()

screen.exitonclick()