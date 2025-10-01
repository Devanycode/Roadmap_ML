from turtle import Turtle

INITIAL_LIVES = 3
VEL_SNAKE = 20
MOVE_SNAKE = {"UP": "90", "DOWN": 270, "LEFT": 180, "RIGHT": 0}
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.body = []
        self.snake_body()    # Llama al método del cuerpo de la tortuga apenas se menciona la clase
        self.head = self.body[0]

    def snake_body(self):
        # Cuadrito del cuerpo de la tortuga predeterminado
        tim = Turtle(shape= "square")
        tim.penup()     # Que no deje rastro cuando camina 
        tim.fillcolor("DarkSlateGray")  # Color de la serpiente
        tim.goto(x= 0, y= 0)    # Se ubica en el centro de la pantalla
        tim.setheading(0)   # Empieza mirando hacia la derecha
        self.body.append(tim)    # La cabeza de la tortuga se llama tim
        for lives in range(1, INITIAL_LIVES):   # Se crean cuadritos según las vidas iniciales
            body_part = tim.clone()   # Se crea una copia de tim por cada parte del cuerpo
            body_part.setx(-20 * lives)
            self.body.append(body_part)
            self.head = self.body[0]
        
    def new_body(self):
        self.body.append(self.body[-1].clone())    # Se añade una copia exacta de la cola a la lista

    def snake_move(self):
        for body_part in range(len(self.body) - 1, 0, -1):
            x = self.body[body_part - 1].xcor()
            y = self.body[body_part - 1].ycor()
            self.body[body_part].goto(x, y)
        self.head.forward(VEL_SNAKE)    # La cabeza avanza y las demás la siguen

    def restart_snake_body(self):
        for body in self.body:
            body.hideturtle()
        self.body.clear()
        self.snake_body()
    

    def move_up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def move_down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def move_left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def move_right(self):
        if self.body[0].heading() != LEFT:
           self.body[0].setheading(RIGHT)
