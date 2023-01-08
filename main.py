from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My Snake Game")
x_position = 0
for i in range(0, 3):
    snake = Turtle(shape="square")
    snake.penup()
    snake.color("white")
    snake.goto(x_position, 0)
    x_position -= 20
screen.exitonclick()
