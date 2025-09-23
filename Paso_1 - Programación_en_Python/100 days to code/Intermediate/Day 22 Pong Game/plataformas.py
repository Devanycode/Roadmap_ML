from turtle import Turtle
from pelota import Pong

USER_X = -293
PC_X = 285

class Plataform(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.resizemode("user")
        self.left(90)
        self.turtlesize(stretch_wid= 0.5, stretch_len= 3)
        self.pc_plataform = self.clone()
        self.user_plataform()
        self.system_plataform()
    
    def user_plataform(self):
        self.goto(x= USER_X, y= 0)
        

    def system_plataform(self):
        self.pc_plataform.goto(x= PC_X, y= 0)

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)

