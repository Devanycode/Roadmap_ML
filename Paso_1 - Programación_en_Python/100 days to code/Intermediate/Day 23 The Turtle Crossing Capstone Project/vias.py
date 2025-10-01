from turtle import Turtle
from car_manager import MIN_POSITION_Y, INTERVAL_POSITION

# Inicio de creación de vía
START_X = -300     # HEIGHT_SCREEN / 2 * -1 + 20
# Tamaño de cada línea
FORWARD_SIZE = 15



class Vias(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.coordinatex = START_X
        self.coordinatey = MIN_POSITION_Y - 10    # Se le resta 10 que es la mitad del ancho de un coche
        self.goto(x= self.coordinatex, y= self.coordinatey)

    def creation_pathways(self):
        for y in range(15):
            for x in range(20):
                self.pendown()
                self.forward(FORWARD_SIZE)
                self.penup()
                self.forward(FORWARD_SIZE)
            self.coordinatey += 40
            self.goto(x= self.coordinatex, y= self.coordinatey)
            
            

