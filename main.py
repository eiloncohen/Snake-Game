import turtle
from snake import Snake, Screen
from food import Food
from scoreboard import ScoreBored
import time


# initialize
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
scoreboard = ScoreBored()
total_score = 0
screen.tracer(0)

new_snake = Snake()
screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")
screen.screensize(300,300)
food = Food()
game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_snake.move()
    xcor_head_snake = new_snake.snake_body[0].xcor()
    ycor_head_snake = new_snake.snake_body[0].ycor()
    if xcor_head_snake < -280 or xcor_head_snake > 280 or ycor_head_snake < -280 or ycor_head_snake > 280 or new_snake.if_own_collision_happend():
        scoreboard.game_over()
        game_is_on = False


    food.check_if_eaten(new_snake, scoreboard)

screen.exitonclick()



