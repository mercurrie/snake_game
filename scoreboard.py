from turtle import Turtle
import json
data_file = open('constants.json')
CONSTANTS = json.load(data_file)
data_file = open('high_score.json')
old_score = json.load(data_file)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = CONSTANTS["STARTING_SCORE"]
        self.high_score = {"high_score": old_score["high_score"]}
        self.color(CONSTANTS["SCOREBOARD_COLOR"])
        self.penup()
        self.goto(CONSTANTS["SCOREBOARD_POSITION"])
        self.hideturtle()
        self.update_scoreboard()

    # writes score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score['high_score']}"
                   , align=CONSTANTS["SCOREBOARD_ALIGNMENT"], font=CONSTANTS["SCOREBOARD_FONT"])

    # Writes game over on screen
    # def game_over(self):
    #     self.goto(CONSTANTS["GAME_OVER_POSITION"])
    #     self.write(f"Game Over", align=CONSTANTS["SCOREBOARD_ALIGNMENT"], font=CONSTANTS["SCOREBOARD_FONT"])

    # Increases score and refreshes the text
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score["high_score"]:
            self.high_score["high_score"] = self.score
        self.score = 0
        self.update_scoreboard()
        with open('high_score.json', 'w') as f:
            json.dump(self.high_score, f)
