from turtle import Turtle

LEVEL_SIZE = 24
FONT = ("Garamond", LEVEL_SIZE, "normal")
LEVEL_POSITION = (-275, 230)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("AliceBlue")
        self.goto(LEVEL_POSITION)
        self.write(arg= f"Level: {self.level}", align= "left", font= FONT)        

    def score_level_up(self):
        """Cuando la tortuga llega a la meta, se aumenta el número de nivel que se muestra en pantalla"""
        self.clear()
        self.level += 1
        self.write(arg= f"Level: {self.level}", align= "left", font= FONT)

    def game_over(self):
        """Cuando la tortuga choca con un coche se pierde el juego
        y se pone "GAME OVER" en el centro de la pantalla"""
        game_over = self.clone()
        game_over.goto(x= 0, y= 0)
        game_over.write(arg= "GAME OVER", align= "center", font= FONT)
