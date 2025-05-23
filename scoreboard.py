from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("White")
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", align="center", font=("Arial", 21, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 21, "normal"))

