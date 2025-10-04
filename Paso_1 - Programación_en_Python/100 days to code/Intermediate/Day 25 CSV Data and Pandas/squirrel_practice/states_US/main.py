from draw_module import Draw
import pandas
from screen_size import SCREEN_X, SCREEN_Y
from turtle import Turtle, Screen

IMAGE = "blank_states_img.gif"
STATES_DATA_CSV = "50_states.csv"

screen = Screen()
screen.setup(SCREEN_X, SCREEN_Y)
screen.title("U.S. States Game")
screen.tracer(0)
screen.addshape(IMAGE)  # Esto permite que podamos usar esta imagen para darle forma a la tortuga
# Creamos una tortuga con la nueva forma que agregamos 
turtle = Turtle(shape= IMAGE)

# Instancias de Draw
drawing_state = Draw()
drawing_score = Draw()


# Leemos el archivo que contiene la información de los estados y su ubicación en x/y
states_data = pandas.read_csv(STATES_DATA_CSV)
# Creamos una lista que contiene todos los valores de la columna 'state'
states_data_list = states_data.state.to_list()
# Número de total de estados
num_states = len(states_data_list)
number_states_guessed = 0
guessed_states = []

def score():
    """Pone en pantalla la puntuación del usuario"""
    drawing_score.write_score(current_score= f"{number_states_guessed}/{num_states}")



while len(guessed_states) < num_states:
    score()
    screen.update()
    # Pide al usuario que ingrese un estado y hacemos que la primera letra sea mayúscula y las demás minúsculas porque es el formato de los estados
    try: 
        answer_state = screen.textinput(title= "Guess the State", prompt= "What's another state's name?").title()
    except AttributeError:
        break

    if answer_state == "Exit":
        break

    if answer_state in states_data_list and answer_state not in guessed_states:
        state_row = states_data[states_data.state == answer_state]    # Encontramos la fila 
        drawing_state.write_state(xcor=int(state_row.x), ycor= int(state_row.y), name_state= answer_state)
        # Se agrega a la lista para que no se pueda sumar puntos repitiendo estados ya mencionados
        guessed_states.append(answer_state)
        number_states_guessed += 1    # Aumentamos el valor de estados adivinados
        drawing_score.write_score(current_score= f"{number_states_guessed}/{num_states}")

# Generar CSV de estados faltantes si no se completaron todos
missing_states = [state for state in states_data_list if state not in guessed_states]
if missing_states:
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")    
        



