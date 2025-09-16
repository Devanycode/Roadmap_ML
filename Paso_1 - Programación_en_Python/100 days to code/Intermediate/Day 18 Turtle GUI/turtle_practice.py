from turtle import Turtle, Screen
from random import choice, randint



timmy = Turtle()
timmy.shape("turtle")

def random_rgb():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255) 
    return r, g, b

angles = [90, 180, 270, 360]
timmy.hideturtle()
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)


"""
angle = 0


for x in range(72):
    timmy.pencolor(random_rgb())
    timmy.circle(75, 360)
    angle += 5
    timmy.setheading(angle)
"""

"""
timmy.pensize(15) 


for _ in range(200):    
    timmy.pencolor(random_rgb())
    timmy.forward(20)
    timmy.right(choice(angles))
"""



"""
for x in range(3,11):
    timmy.color(choice(colours))
    for y in range(x):
        timmy.forward(100)
        angle = 360 / x
        timmy.right(angle)
    """



screen = Screen()
screen.exitonclick()
