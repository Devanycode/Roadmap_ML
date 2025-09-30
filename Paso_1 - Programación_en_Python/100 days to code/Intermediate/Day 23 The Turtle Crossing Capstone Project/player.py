from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
HEADING_ORIENTATION = 90    # Norte
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("aquamarine4")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(HEADING_ORIENTATION)

    def turtle_movement(self):
        """Es el objeto función que se usa para que la tortuga camine hacia adelante
        cuando presionamos la tecla elegida"""
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        """Cuando la tortuga llegó a la parte final de la carrera vuelve a estar
        en la posición inicial"""
        self.goto(STARTING_POSITION)

