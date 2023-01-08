from turtle import Turtle
import random


class Food:

    def __init__(self):
        self.create_food()

    @staticmethod
    def create_food():
        food = Turtle(shape="circle")
        food.color("teal")
        food.penup()
        food.shapesize(stretch_wid=.5, stretch_len=.5)
        food.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        food.goto(random_x, random_y)

