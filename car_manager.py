from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.generator()


    def generator(self):

        for i in range(random.randint(1,5)):
            cars_range = [-random.randrange(0, 240,random.randint(2,60)), random.randrange(0, 240,random.randint(2,60))]
            car = Turtle(shape="square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.setheading(180)
            car.goto(280,random.choice(cars_range))
            car.forward(STARTING_MOVE_DISTANCE)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)








