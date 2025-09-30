from turtle import Turtle
from random import randrange, randint, choice

# Caracteríscias del coche 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
ORIENTATION = 180   # Se moverá hacia la izquierda
# Movimiento
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4
# Tamaño del coche
STRETCH_WID = 1
STRETCH_LEN = 1.8
# Posición y separación
START_X = 310
MIN_POSITION_Y = -240
MAX_POSITION_Y = 260
INTERVAL_POSITION = 20
# Probabilidad de cantidad de aparición de coches
INITIAL_PROBABILITY = 7.5   # Si un número aleatorio entre 0 y 10 es mayor a este se crea un coche nuevo



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.car_probability = INITIAL_PROBABILITY
        self.cars = []

    def random_cars(self):
        """Esta función crea un coche nuevo cuando valor aleatorio entre 0 y 10
        es mayor al parámetro 'car_probability', con una ubicación y color
        aleatorios, comenzando siempre a la derecha de la pantalla."""
        if randint(0,10) > self.car_probability:
            car = Turtle(shape= "square")
            car.setheading(ORIENTATION)
            car.shapesize(stretch_wid= STRETCH_WID, stretch_len= STRETCH_LEN)    
            car.color(choice(COLORS))
            car.penup()

            # Para que la ubicación sea aleatoria cada vez entre este rango dado
            start_y = randrange(MIN_POSITION_Y, MAX_POSITION_Y, INTERVAL_POSITION)  
            car.goto(x= START_X, y= start_y)
            self.cars.append(car)

    def move_cars(self):
        """Esta función le da movimiento a los coches."""
        for car in self.cars:
            car.forward(self.move_distance)

    def increase_difficulty(self):
        """Cuando se sube de nivel incrementa la velocidad de los coches
         y la probabilidad de que sean creados, también elimina los que 
         habían en pantalla"""
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
        self.move_distance += MOVE_INCREMENT
        self.car_probability *= 0.96




