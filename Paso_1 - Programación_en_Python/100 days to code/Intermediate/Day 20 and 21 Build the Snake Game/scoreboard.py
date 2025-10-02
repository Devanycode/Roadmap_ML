from turtle import Turtle

ALIGMENT = "center"
FONT = ('Garamond', 20, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore_history.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("LightYellow1")
        self.goto(x= 0, y= 270)

    def update_scoreboard(self):
        self.clear()
        self.write(arg= f"Score : {self.score}  High Score: {self.highscore}",
        align= ALIGMENT, font= FONT)

    def new_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore_history.txt", mode= "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()




"""Si quiero jugar con game over puedo usar esto, pero para un juego 
infinito no es necesario"""
class GameOver(Scoreboard):
    def __init__(self):
        super().__init__()
        self.home()
    
    def lose(self):
        self.write(arg= "Game Over", align= ALIGMENT, font= FONT)





