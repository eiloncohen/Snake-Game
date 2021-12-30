import turtle
from snake import Snake, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

new_snake = Snake()
screen.listen()
screen.onkey(new_snake.up,"Up")
screen.onkey(new_snake.down,"Down")
screen.onkey(new_snake.left,"Left")
screen.onkey(new_snake.right,"Right")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    new_snake.move()


screen.exitonclick()



