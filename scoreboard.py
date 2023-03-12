from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as h_score:
            self.high_score = int(h_score.read())
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as h_score:
                h_score.write(str(self.high_score))
        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.home()
    #     self.write("Game over.", move=False, align=ALIGNMENT, font=FONT)
