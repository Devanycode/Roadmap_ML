import colorgram
from PIL import Image
from turtle import Turtle, Screen
from random import choice

"""
image = Image.open('Paso_1 - Programación_en_Python/100 days to code/Intermediate/Day 18 Turtle GUI/image.jpg')

rgb_colors = []
colors = colorgram.extract(image, 30)

for color in range(30):
    first_color = colors[color]
    rgb = first_color.rgb
    rgb_colors.append((rgb.r, rgb.g, rgb.b))

print(rgb_colors)
"""

color_list = [
    (26, 14, 20), (15, 17, 25), (237, 127, 61), (156, 100, 28), (109, 203, 180), (130, 166, 189),
    (217, 216, 81), (35, 85, 125), (207, 133, 138), (185, 9, 126), (98, 183, 52), (22, 90, 70), 
    (103, 86, 94), (225, 132, 20), (230, 168, 161), (217, 102, 62), (69, 116, 86), (189, 220, 26)
    ]

timmy = Turtle()
timmy.hideturtle()  # No quiero que se vea la tortuga 
timmy.speed("fastest")
timmy.teleport(x= -225, y= -225) # Quiero que mi tortuga empiece ahí

screen = Screen()
screen.colormode(255)


for y in range(1, 11):     # Coordenada en y
    for x in range(1, 11):   # Coordenada en x
        timmy.pendown()
        timmy.color(choice(color_list))  # Color aleatorio entre la lista de rgb
        timmy.begin_fill()  # Se llama antes de dibujar y rellenar una forma
        timmy.dot(20)       # Dibuja un punto circular con el tamaño específicado
        timmy.end_fill()    # Rellena una forma dibujada 
        timmy.penup()
        timmy.forward(50)
    timmy.teleport(x=-225, y= -225 + (y * 50))


screen.exitonclick()

