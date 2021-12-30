from turtle import *

LOCATIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        for i in range(3):
            tim = self.add_new_piece()
            tim.setposition(LOCATIONS[i])
            self.snake_body.append(tim)

    def add_new_piece(self):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        return tim

    def move(self):
        for location in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[location-1].xcor()
            new_y = self.snake_body[location-1].ycor()
            self.snake_body[location].setposition(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

