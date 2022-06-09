from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("cyan")
        self.penup()
        self.setheading(90)
        self.pace = 0.2
        self.refresh()


    def refresh(self):
        self.goto(STARTING_POSITION)
        self.pace *= 0.9

    def move(self):
        self.forward(MOVE_DISTANCE)