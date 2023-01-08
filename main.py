import time
from turtle import Turtle, Screen
from snake import Snake

# Create screen, set dimensions and color
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

# Allow screen to listen to user inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
# While loop to continue updating screen after snake moves
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.snake_move()


screen.exitonclick()
