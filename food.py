from turtle import Turtle
import random
import json
data_file = open('constants.json')
CONSTANTS = json.load(data_file)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(CONSTANTS["FOOD_SHAPE"])
        self.color(CONSTANTS["FOOD_COLOR"])
        self.penup()
        self.shapesize(CONSTANTS["FOOD_WIDTH"], CONSTANTS["FOOD_HEIGHT"])
        self.speed(CONSTANTS["FOOD_SPAWN_SPEED"])
        self.refresh()

    # Generates a random location for the food
    def refresh(self):
        random_x = random.randint(CONSTANTS["SCREEN_BOUND_MIN"], CONSTANTS["SCREEN_BOUND_MAX"])
        random_y = random.randint(CONSTANTS["SCREEN_BOUND_MIN"], CONSTANTS["SCREEN_BOUND_MAX"])
        self.goto(random_x, random_y)
