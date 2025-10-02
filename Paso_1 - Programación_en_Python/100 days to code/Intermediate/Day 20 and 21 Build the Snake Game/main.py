from turtle import Screen
from random import randint
from snake import Snake
from food import Food
from scoreboard import Scoreboard, GameOver
import time

# Creación de la pantalla 
screen = Screen()
screen.setup(width= 600, height= 600)   # tamaño de la pantalla pxl
screen.bgcolor("DarkSeaGreen2")
screen.title("My Snake game")
screen.tracer(0)   # Para el delay


# Llamada a objetos 
snake = Snake()
food = Food()
score = Scoreboard()
score.update_scoreboard()
game_over = GameOver()  # Se puede usar cuando el juego no es infinito
screen.update()

# Cuando el juego no es infinito
def game_over_calls():
    """Cuando se acaba el juego se llama a estas funciones para imprimir
    el Game Over en pantalla, para actualizar el highscore y para finalizar
    el bucle que hacía a la serpiente moverse infinitamente"""
    game_over.lose()
    score.new_highscore()

def game_lose_continue_calls():
    snake.restart_snake_body()
    snake.snake_move()
    score.new_highscore()

# CONTROLES
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")


# Inicio del juego
snake_start = True
while snake_start:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()    # Movimiento infinito de la serpiente

    # DETECT COLLISION
    # With food
    if snake.head.distance(food) < 15:
        food.tp()
        snake.new_body()
        score.increase_score()
    
    # With wall
    if snake.head.xcor() > 298 or snake.head.xcor() < -298:
        # game_over_calls()
        # snake_start = False
        game_lose_continue_calls()
    if snake.head.ycor() > 300 or snake.head.ycor() < -300:
        # game_over_calls()
        # snake_start = False
        game_lose_continue_calls()
    # With body
    for part in snake.body[1:]:
        if snake.head.distance(part) < 10:
            # game_over_calls()
            # snake_start = False
            game_lose_continue_calls()


screen.exitonclick()
