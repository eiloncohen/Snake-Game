from turtle import Turtle

HEIGHT = 250
WIDTH = 0

class ScoreBored(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.color("white")
        self.penup()
        self.setposition(WIDTH, HEIGHT)
        self.hideturtle()
        self.write(f"Score: {self.counter}", move=False, align='center', font=("Verdana", 30, "normal"))

    def update_score(self):
        self.clear()
        self.counter += 1
        self.write(f"Score: {self.counter}", move=False, align='center', font=("Verdana", 30, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over.", move=False, align='center', font=("Verdana", 30, "normal"))

    def choose_level_game(self, level):
        if level == "easy":
            return 0.2
        elif level == "medium":
            return 0.1
        elif level == "hard":
            return 0.07
        elif level == "expert":
            return 0.04
        else:
            raise Exception("wrong level! enter level again")
