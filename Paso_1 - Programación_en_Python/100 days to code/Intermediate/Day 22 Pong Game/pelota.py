from turtle import Turtle
from random import randrange

VEL_PONG = 3
VEL_SLEEP = 0.1
PONG_FORWARD = 20

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.time_sleep = VEL_SLEEP
        self.goto(0, 0)
        self.shape("circle")
        self.color("white")
        self.setheading(randrange(start= 20, stop= 340, step= 15))
        self.turtlesize(stretch_len= 0.8 , stretch_wid= 0.8)
        self.penup()
        self.speed(VEL_PONG)

    def move_pong(self):
        """Simplemente representa los pasos que avanza cada vez la pelota"""
        self.forward(PONG_FORWARD)

    def increase_speed(self):
        """Aumenta la velocidad de la pelota gradualmente para mayor desafío.
        Aunque tiene un límite para evitar juego imposible."""
        if self.time_sleep > 0.023:
            self.time_sleep *= 0.9

    def reset_speed(self):
        """Reestablece la velocidad de la pelota a la velocidad inicial"""
        self.time_sleep = VEL_SLEEP

    def reboot(self):
        """Cuando se gana un punto la pelota desaparece y vuelve a empezar en el centro
        apuntando hacia otro lugar aleatorio"""
        self.goto(x= 0, y= 0)
        self.setheading(randrange(start= 20, stop= 340, step= 15))
    



    
