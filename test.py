from turtle import Screen,Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=600, height=600)


for i in range(10):
    cars_range = [-random.randint(0, 240), random.randint(0, 240)]
    car = Turtle(shape="square")
    car.color(random.choice(COLORS))
    car.shapesize(stretch_wid=1,stretch_len=2)
    car.penup()
    car.setheading(180)
    car.goto(280,random.choice(cars_range))
    car.forward(5)


screen.exitonclick()