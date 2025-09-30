from turtle import Turtle, Screen
from plataformas import Plataform
from scoreboard import Scoreboard
from pelota import Pong
from random import randint
import time


# Creación de la pantalla
screen = Screen()
# screen.screensize(canvheight= 700, canvwidth= 700)
screen.setup(height= 600, width= 800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Llamada de objetos
plataform = Plataform()
score = Scoreboard()
score.separator()
pong = Pong()

def user_point():
    score.user_score += 1
    score.score()
    pong.reboot()

def pc_point():
    score.pc_score += 1
    score.score()
    pong.reboot()


screen.listen()
screen.onkey(fun= plataform.move_up, key= "Up")
screen.onkey(fun= plataform.move_down, key= "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(pong.time_sleep)
    pong.move_pong()

    # Seguimiento automático de la plataforma del sistema
    if pong.ycor() > plataform.pc_plataform.ycor():
        plataform.pc_move_up()
    if pong.ycor() < plataform.pc_plataform.ycor():
        plataform.pc_move_down()

    # Detect collision with wall
    if pong.ycor() > 290 or pong.ycor() < -290:
        pong.setheading(360 - pong.heading())

    # Aumentar puntuación (Colisión pared horizontal)
    # USUARIO
    if pong.xcor() > 400:
        user_point()
        pong.reset_speed()
        
    # SISTEMA
    if pong.xcor() < -400:
        pc_point()
        pong.reset_speed()
        

    # Detectar colisión con las plataformas
    # USUARIO
    if pong.distance(plataform) < 50 and pong.xcor() > -390:
        if pong.ycor() > plataform.ycor():
            pong.setheading(randint(10, 70))
        if pong.ycor() < plataform.ycor():
            pong.setheading(randint(290, 350))
        else:
            pong.setheading(randint(320, 400))
        pong.increase_speed()
        
    # SISTEMA
    if pong.distance(plataform.pc_plataform) < 50 and pong.xcor() < 390:
        if pong.ycor() > plataform.pc_plataform.ycor():
            pong.setheading(randint(110, 170))
        if pong.ycor() < plataform.pc_plataform.ycor():
            pong.setheading(randint(190, 250))
        else:
            pong.setheading(randint(140, 220))
        pong.increase_speed()
    
    if score.user_score == 6:
        score.user_win()
        break

    if score.pc_score == 6:
        score.game_over()
        break
        
    

    
# Hacer que los rebotes sean físicos y no aleatorios
# Puedo hacer el juego pvp o pve
# Hacer que la IA sea imperfecta 
# Puedo hacer que aumente la dificultad después de 3 puntos
# Hacer que las plataformas no se salgan del tablero


screen.exitonclick()