import time
from turtle import Screen
from player import Player
from vias import Vias
from car_manager import CarManager
from scoreboard import Scoreboard

# Tamaño de pantalla
WIDTH_SCREEN = 600
HEIGHT_SCREEN = 600
# Distancia de colisión
DISTANCE_COLLISION = 30
# Ubicación de la meta en Y
GOAL_Y = 280

# CREACIÓN DE LA PANTALLA
screen = Screen()
screen.setup(width= WIDTH_SCREEN, height= HEIGHT_SCREEN)
screen.bgcolor("gray10")
screen.title("Crossing Capstone Game.")
screen.tracer(0)
# Simulación de Vías 
pathway = Vias()
pathway.creation_pathways()


# Llamada a objetos 
turtle = Player()
scoreboard = Scoreboard()
car = CarManager()

# Eventos de movimiento de la tortuga
screen.listen()
screen.onkey(fun= turtle.turtle_movement, key= "Up")
screen.onkey(fun= turtle.turtle_movement, key= "w")

# Inicio del juego
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.random_cars()
    car.move_cars()
    screen.update()
    
    # Se sube de nivel y aumenta dificultad cuando llegamos a la meta
    if turtle.ycor() >= GOAL_Y:
        scoreboard.score_level_up()
        turtle.level_up()
        car.increase_difficulty()

    # Si detectamos colisión con los coches se acaba el juego
    for car_obj in car.cars:
        if turtle.distance(car_obj) < DISTANCE_COLLISION:
            scoreboard.game_over()
            game_is_on = False
    



# TODO 0: Puedo hacer la simulación de las vías de una carretera 



screen.exitonclick()