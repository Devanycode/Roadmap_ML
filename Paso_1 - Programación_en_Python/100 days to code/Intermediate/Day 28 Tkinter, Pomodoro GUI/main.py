from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

FONT_NAME = "Courier"
TIMER_FONT_SIZE = 35
WIDTH_BUTTONS = 15


WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BREAK_COUNT = 0    # Esta variable comienza en 0 porque aún no hemos tomado ningún descanso
FOCUS_COUNT = 0

TIMER = None

MARKS = ""    # Aquí se irá concatenando los check marks según completemos tiempo de focus


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global MARKS
    global FOCUS_COUNT 
    global BREAK_COUNT
    global TIMER
    MARKS = ""
    FOCUS_COUNT = 0
    BREAK_COUNT = 0
    check_marks.config(text= MARKS)
    timer_title.config(text= "Timer", fg= GREEN)
    TIMER = window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def focus_timer():
    global FOCUS_COUNT
    FOCUS_COUNT += 1
    timer_title.config(text= "FOCUS", fg= GREEN)
    minutes = WORK_MIN
    seconds = 0
    count_down(minutes, seconds)

def break_timer():
    global MARKS
    global BREAK_COUNT
    BREAK_COUNT += 1
    MARKS += "✓"
    check_marks.config(text=MARKS)    

    if BREAK_COUNT % 4 != 0:    # Porque al cuarto descanso se hace un descanso largo   
        timer_title.config(text="Short Break", fg=PINK)
        time_break = SHORT_BREAK_MIN
        seconds = 0
    else:
        timer_title.config(text="Long Break", fg=RED)
        time_break = LONG_BREAK_MIN
        seconds = 0
    count_down(time_break, seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(minut, sec):
    canvas.itemconfig(timer_text, text=f"{minut:02}:{sec:02}")
    if minut == 0 and sec == 0:
        if FOCUS_COUNT > BREAK_COUNT:   # Significa que hay que descansar
            break_timer()
            return
        else:   # Significa que ya se descansó
            focus_timer()
            return
    if sec == 0:
        sec = 60
        minut -= 1
    global TIMER
    TIMER = window.after(1000, count_down, minut, sec - 1)

# ---------------------------- UI SETUP ------------------------------- #

# Pantalla
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=120, pady=70, bg=YELLOW)

# Los canvas son buenos para agregar imágenes que se pueden superponer
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)    # La mitad de los valores, porque queremos que esté en el centro de la pantalla
timer_text = canvas.create_text(101, 135, text="00:00", fill="white", font=(FONT_NAME, TIMER_FONT_SIZE, "bold"))


# UI SETUP
# tomato canvas
canvas.grid(column=1, row=1)

# Labels
timer_title = Label(text="Timer", fg= GREEN, bg= YELLOW, font=(FONT_NAME, TIMER_FONT_SIZE, "bold"), pady= 20)
timer_title.grid(column=1, row=0)

check_marks = Label(text= MARKS, fg= GREEN, bg= YELLOW, font= (FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=4)

# buttons
start_button = Button(text="Start", width=WIDTH_BUTTONS, command=focus_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", width=WIDTH_BUTTONS, command= reset_timer)
reset_button.grid(column=2, row=3)




window.mainloop()