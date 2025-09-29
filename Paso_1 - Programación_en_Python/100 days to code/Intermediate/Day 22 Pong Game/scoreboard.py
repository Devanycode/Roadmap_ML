from turtle import Turtle
from plataformas import Plataform

SCORE_SIZE = 35
ALIGMENT = "center"
FONT = ('Garamond', SCORE_SIZE, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pc_score = 0
        self.user_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x= 0, y= 250)
        self.score()

    def score(self):
        """Muestra la puntuación del usuario y del sistema en la parte superior
        de la pantalla"""
        self.clear()
        self.write(arg= f"{self.user_score}   {self.pc_score}", align= ALIGMENT, font= FONT)

    def game_over(self):
        game_over = self.clone()
        game_over.goto(x= 0, y= 0)
        game_over.write(arg= "GAME OVER", align= ALIGMENT, font= FONT)
    
    def user_win(self):
        user_win = self.clone()
        user_win.goto(x= 0, y= 0)
        user_win.write(arg= "Congratulations. You Win", align= ALIGMENT, font= FONT)

    def separator(self):
        """Separador en forma de líneas verticales con espacios entre sí
        que separa la pantalla en dos mitades: la del usuario y la del sistema"""
        separator = Turtle(shape= "square")
        separator.color("white")
        separator.resizemode("user")
        separator.hideturtle()
        separator.left(90)
        separator.pensize(3)
        separator.penup()
        separator.goto(x= 0, y= -300)
        for x in range(0,30):
            separator.pendown()
            separator.forward(10)
            separator.penup()
            separator.forward(10)
    
        



        


