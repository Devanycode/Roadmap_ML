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


snake = Snake()
food = Food()
score = Scoreboard()
score.update_scoreboard()
game_over = GameOver()
screen.update()

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


snake_start = True
while snake_start:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.tp()
        snake.new_body()
        score.increase_score()
    
    # Detect collision with wall
    if snake.head.xcor() > 298 or snake.head.xcor() < -298:
        game_over.lose()
        snake_start = False
    if snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_over.lose()
        snake_start = False
    for part in snake.body[1:]:
        if snake.head.distance(part) < 10:
            game_over.lose()
            snake_start = False
        

screen.exitonclick()
