from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("DarkSalmon")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.speed("fastest")
        self.tp()
    
    def tp(self):
        self.teleport(randint(-280, 280), randint(-280,280))