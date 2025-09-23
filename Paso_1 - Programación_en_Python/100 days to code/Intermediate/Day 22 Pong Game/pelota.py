from turtle import Turtle
from random import randint



class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 0)
        self.shape("square")
        self.color("white")
        self.setheading(randint(140, 210))
        self.turtlesize(stretch_len= 0.8 , stretch_wid= 0.8)
        self.penup()
        self.speed("normal")

    def move_pong(self):
        self.forward(20)
    



    
