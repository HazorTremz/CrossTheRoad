from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-270,250)
        self.level = 1
        self.update()

    def update(self):
        self.write(f"Level:{self.level}",font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(-80,0)
        self.write("Game Over",font=FONT)


