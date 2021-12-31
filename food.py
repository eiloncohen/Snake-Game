import turtle
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.setposition(random_x, random_y)
        self.set_food_position()

    def check_if_eaten(self, snake, score):
        if int(self.distance(snake.snake_body[0])) <= 20:
            self.set_food_position()
            piece = snake.add_new_piece()
            piece.hideturtle()
            snake.snake_body.append(piece)
            snake.move()
            piece.showturtle()
            score.update_score()

    def set_food_position(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.setposition(random_x, random_y)