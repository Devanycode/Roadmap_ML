from turtle import Turtle
from plataformas import Plataform

SCORE_SIZE = 35
ALIGMENT = "center"
FONT = ('Garamond', SCORE_SIZE, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pc_score = 0
        self.user_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x= 0, y= 250)
        self.score()

    def score(self):
        self.clear()
        self.write(arg= f"{self.user_score}   {self.pc_score}", align= ALIGMENT, font= FONT)
    
    def separator(self):
        separator = Turtle(shape= "square")
        separator.color("white")
        separator.resizemode("user")
        separator.hideturtle()
        separator.left(90)
        separator.pensize(3)
        separator.penup()
        separator.goto(x= 0, y= -300)
        for x in range(0,30):
            separator.pendown()
            separator.forward(10)
            separator.penup()
            separator.forward(10)
    
        



        


