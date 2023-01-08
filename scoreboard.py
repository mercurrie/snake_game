from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # writes score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Writes game over on screen
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    # Increases score and refreshes the text
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
