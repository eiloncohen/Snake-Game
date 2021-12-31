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
        self.head = self.snake_body[0]
        self.head.color("red")

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
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def if_own_collision_happend(self):
        for piece in range(1, len(self.snake_body) - 1, 1):
            if self.head.distance(self.snake_body[piece]) < 10:
                return True
        return False
