from turtle import Turtle

ALIGMENT = "center"
FONT = ('Garamond', 20, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("LightYellow1")
        self.goto(x= 0, y= 270)

    def update_scoreboard(self):
        self.write(arg= f"Score : {self.score}", align= ALIGMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

class GameOver(Scoreboard):
    def __init__(self):
        super().__init__()
        self.home()
    
    def lose(self):
        self.write(arg= "Game Over", align= ALIGMENT, font= FONT)


