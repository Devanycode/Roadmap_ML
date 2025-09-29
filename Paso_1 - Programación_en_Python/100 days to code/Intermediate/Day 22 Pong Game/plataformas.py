from turtle import Turtle
from pelota import Pong

USER_X = -380
PC_X = 380
VEL_USER = 25
VEL_PC = 15     # Puedo elegir una dificultad en base a esto

class Plataform(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.resizemode("user")
        self.left(90)
        self.turtlesize(stretch_wid= 0.8, stretch_len= 4)
        self.pc_plataform = self.clone()
        self.user_plataform()
        self.system_plataform()
    
    def user_plataform(self):
        """Posición inicial de la plataforma del usuario"""
        self.goto(x= USER_X, y= 0)
        
    def system_plataform(self):
        """Posición inicial de la plataforma del sistema"""
        self.pc_plataform.goto(x= PC_X, y= 0)


    def move_up(self):
        """Función que ejecuta el movimiento del usuario hacia arriba"""
        self.setheading(90)
        self.forward(VEL_USER)

    def move_down(self):
        """Función que ejecuta el movimiento del usuario hacia abajo"""
        self.setheading(270)
        self.forward(VEL_USER)

    def pc_move_up(self):
        """Seguimiento de la plataforma a la pelota si está arriba en Y"""
        self.pc_plataform.setheading(90)
        self.pc_plataform.forward(VEL_PC)

    def pc_move_down(self):
        """Seguimiento de la plataforma a la pelota si está abajo en Y"""
        self.pc_plataform.setheading(270)
        self.pc_plataform.forward(VEL_PC)

