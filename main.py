from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import json
import time
data_file = open('constants.json')
CONSTANTS = json.load(data_file)


def play_game():
    # Create screen, set dimensions and color
    screen = Screen()
    screen.setup(CONSTANTS["SCREEN_WIDTH"], CONSTANTS["SCREEN_HEIGHT"])
    screen.bgcolor(CONSTANTS["SCREEN_COLOR"])
    screen.title(CONSTANTS["GAME_TITLE"])
    screen.tracer(CONSTANTS["ANIMATION_OFF"])

    # Create snake and food object
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    # Allow screen to listen to user inputs
    screen.listen()
    screen.onkey(snake.up, CONSTANTS["UP_ARROW"])
    screen.onkey(snake.down, CONSTANTS["DOWN_ARROW"])
    screen.onkey(snake.right, CONSTANTS["RIGHT_ARROW"])
    screen.onkey(snake.left, CONSTANTS["LEFT_ARROW"])

    game_is_on = True

    # While loop to continue updating screen after snake moves
    while game_is_on:
        screen.update()
        time.sleep(CONSTANTS["SLEEP_TIME"])
        snake.snake_move()

        # Detect collision with food
        if snake.head.distance(food) < CONSTANTS["FOOD_COLLISION"]:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > CONSTANTS["RIGHT_COLLISION"] or snake.head.xcor() < CONSTANTS["LEFT_COLLISION"] or \
                snake.head.ycor() > CONSTANTS["TOP_COLLISION"] or snake.head.ycor() < CONSTANTS["BOTTOM_COLLISION"]:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < CONSTANTS["TAIL_COLLISION"]:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    play_game()
