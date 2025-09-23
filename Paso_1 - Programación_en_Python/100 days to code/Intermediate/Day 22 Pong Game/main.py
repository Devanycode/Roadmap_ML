from turtle import Turtle, Screen
from plataformas import Plataform
from scoreboard import Scoreboard
from pelota import Pong
import time

# Creación de la pantalla
screen = Screen()
# screen.screensize(canvheight= 700, canvwidth= 700)
screen.setup(height= 600, width= 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Llamada de objetos
plataform = Plataform()
score = Scoreboard()
score.separator()
pong = Pong()


screen.listen()
screen.onkey(fun= plataform.move_up, key= "Up")
screen.onkey(fun= plataform.move_down, key= "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    pong.move_pong()
    if pong.ycor() > plataform.pc_plataform.ycor():
        plataform.pc_plataform.setheading(90)
        plataform.pc_plataform.forward(10)
    if pong.ycor() < plataform.pc_plataform.ycor():
        plataform.pc_plataform.setheading(270)
        plataform.pc_plataform.forward(10)

    # Detect collision with wall
    if pong.ycor() > 290 or pong.ycor() < -290:
        pong.setheading(360 - pong.heading())

    if pong.xcor() > 295:
        score.user_score += 1
        score.score()
        pong.goto(0, 0)
        
    if pong.xcor() < -295:
        score.pc_score += 1
        score.score()
        pong.goto(0, 0)
    
    



        

        











screen.exitonclick()