from turtle import Turtle
import json
data_file = open('constants.json')
CONSTANTS = json.load(data_file)


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[CONSTANTS["HEAD_SEGMENT"]]

    # create_snake  calls add_segment() at to create snake
    def create_snake(self):
        for position in CONSTANTS["STARTING_POSITIONS"]:
            self.add_segment(position)

    # add_segment() creates Turtle object called snake_fragment and appends to fragment list
    def add_segment(self, position: tuple):
        snake_fragment = Turtle(CONSTANTS["SNAKE_SHAPE"])
        snake_fragment.penup()
        snake_fragment.color(CONSTANTS["SNAKE_COLOR"])
        snake_fragment.goto(position)
        snake_fragment.speed(CONSTANTS["SNAKE_SPEED"])
        self.segments.append(snake_fragment)

    # snake_move() starts at the tail and moves each snake fragment towards the position of the next fragment
    def snake_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(CONSTANTS["MOVE_DISTANCE"])

    # clear list of snake segments and creates a new snake
    def reset(self):
        for seg in self.segments:
            seg.goto(CONSTANTS["DEAD_SNAKE_RELOCATION"])
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[CONSTANTS["HEAD_SEGMENT"]]

    # extend() calls add segment
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # sets heading of snake to north
    def up(self):
        if self.head.heading() != CONSTANTS["DOWN"]:
            self.head.setheading(CONSTANTS["UP"])

    # sets heading of snake to south
    def down(self):
        if self.head.heading() != CONSTANTS["UP"]:
            self.head.setheading(CONSTANTS["DOWN"])

    # sets heading of snake to east
    def right(self):
        if self.head.heading() != CONSTANTS["LEFT"]:
            self.head.setheading(CONSTANTS["RIGHT"])

    # sets heading of snake to west
    def left(self):
        if self.head.heading() != CONSTANTS["RIGHT"]:
            self.head.setheading(CONSTANTS["LEFT"])
