from screen_size import SCREEN_X, SCREEN_Y
from turtle import Turtle

SCORE_CORX = (SCREEN_X / 2 * -1) + 20
SCORE_CORY = SCREEN_Y / 2 - 50
SCORE_FONT = ("Garamond", 30, "normal")

class Draw(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, xcor, ycor, name_state):
        self.goto(x= xcor, y= ycor)
        self.write(arg= name_state)

    def write_score(self, current_score):
        self.clear()
        self.goto(SCORE_CORX, SCORE_CORY)
        self.write(arg= current_score, align= "left", font= SCORE_FONT)
        

