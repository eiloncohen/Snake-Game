import turtle
from snake import Snake, Screen
from food import Food
from scoreboard import ScoreBored
import time


# initialize the screen game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

level = screen.textinput("Snake Game", "Please enter a difficulty level: (easy/medium/hard/expert)")

scoreboard = ScoreBored()
total_score = 0

screen.tracer(0)

# create the snake obj and connect the events of keys to him
new_snake = Snake()
screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")
screen.screensize(300,300)

# create food obj and ready to start the game.
food = Food()
game_is_on = True
level_time_waiting = scoreboard.choose_level_game(level)

while game_is_on:
    time.sleep(level_time_waiting)
    screen.update()
    # move method is responsible on snake movement behavior
    new_snake.move()

    # check if collision happened (with the tail of the snake or with the wall)
    xcor_head_snake = new_snake.snake_body[0].xcor()
    ycor_head_snake = new_snake.snake_body[0].ycor()
    if xcor_head_snake < -280 or xcor_head_snake > 280 or ycor_head_snake < -280 or ycor_head_snake > 280 or new_snake.if_own_collision_happend():
        scoreboard.game_over()
        game_is_on = False

    # check if snake ate the food
    food.check_if_eaten(new_snake, scoreboard)

screen.exitonclick()



