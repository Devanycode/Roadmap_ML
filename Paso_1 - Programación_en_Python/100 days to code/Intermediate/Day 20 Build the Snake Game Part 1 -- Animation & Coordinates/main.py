from turtle import Turtle, Screen
from random import randint
from snake import Snake
import time

# Creación de la pantalla 
screen = Screen()
screen.setup(width= 600, height= 600)   # tamaño de la pantalla pxl
screen.bgcolor("DarkSeaGreen2")
screen.title("My Snake game")
screen.tracer(0)   # Para el delay

snake = Snake()
screen.update()




food = Turtle(shape= "circle")
food.color("DarkSalmon")
food.penup()
food.shapesize(0.5)
food_location = food.teleport(randint(-280, 280), randint(-280,280))






# Funciones para el movimiento de la cabeza de la serpiente


# Hay que establecer que no se mueva al mismo lugar donde está ni hacia atrás

screen.listen()
screen.onkey(fun= snake.move_up, key= "Up")
screen.onkey(fun= snake.move_up, key= "w")
screen.onkey(fun= snake.move_down, key= "Down")
screen.onkey(fun= snake.move_down, key= "s")
screen.onkey(fun= snake.move_left, key= "Left")
screen.onkey(fun= snake.move_left, key= "a")
screen.onkey(fun= snake.move_right, key= "Right")
screen.onkey(fun= snake.move_right, key= "d")


snake_start = True
while snake_start:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

screen.exitonclick()