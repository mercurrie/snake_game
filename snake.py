from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # create_snake creates square snake objects
    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_fragment = Turtle(shape="square")
            snake_fragment.penup()
            snake_fragment.color("white")
            snake_fragment.goto(position)
            self.segments.append(snake_fragment)

    # snake_move starts at the tail and moves each snake fragment towards the position of the next fragment
    def snake_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    # sets heading of snake to north
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # sets heading of snake to south
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # sets heading of snake to west
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # sets heading of snake to east
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
