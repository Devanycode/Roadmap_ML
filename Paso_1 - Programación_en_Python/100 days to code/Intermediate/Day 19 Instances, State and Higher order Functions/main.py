"""
timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def move_right():
    timmy.right(10)

def move_left():
    timmy.left(10)

def clear_screen():
    screen.resetscreen()

screen.listen()    # Para que comience a escuchar la interacción con el usuario (Inicializar evento)
screen.onkey(fun= move_forwards, key= "w")
screen.onkey(fun= move_backwards, key= "s")
screen.onkey(fun= move_right, key= "d")
screen.onkey(fun= move_left, key= "a")
screen.onkey(fun= clear_screen , key= "c")
screen.exitonclick()
"""
from turtle import Turtle, Screen
from random import randint

# Almacenar los usuarios que apostarán
count_users = 10
while count_users > 6:   # El número máximo de usuarios es de 6
    count_users = int(input("How many users will play? (máx.6) "))
    if count_users > 6:
        print("Type a correct number")
    
users_play = []

is_race_on = False
screen = Screen()

for number_user in range(count_users):
    user = input(f"(User{number_user + 1}) Type your name: ")
    users_play.append(user)

register_bets = {}
for user in users_play:
    user_bet = screen.textinput(
        title= f"Make your bet {user}", 
        prompt= "Who will win the race? Enter a colour:\n(red, orange, yellow, green, blue, purple)"
    )
    register_bets[user] = user_bet


screen.title("Welcome to the run of turtles")
screen.setup(width= 500, height= 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]    # Colores del arcoíris
names = ["tim", "tom"]
turtles_list = []

for name in names:
    turtle = Turtle(shape= "turtle")
    turtle.turtle_name = name
    turtles_list.append(turtle)

coordenaday = 0
for turtle in turtles_list:
    turtle.color(colors[coordenaday])
    turtle.penup()
    turtle.goto(x= -225, y= -100 + (coordenaday * 40))
    coordenaday += 1

if register_bets:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        # Como la tortuga es de 40z40 queremos que llegue a la meta cuando pasó la mitad de su cuerpo
        if turtle.xcor() >= 230:   # 230 es la meta 
            for key, value in register_bets.items():
                if value == turtle.pencolor():
                    print(f"You Win {key}. The {turtle.pencolor()} turtle is the winner.")
                    is_race_on = False
                    break
                else:
                    print(f"You Lose. The {turtle.pencolor()} turtle is the winner.")
                    is_race_on = False
                    break
        random_distance = randint(0,10)
        turtle.forward(random_distance)
    
screen.exitonclick()


