from tkinter import *

FONT = ("Times New Roman", 12)
PADX_DISTANCE = 30

"""
# Formas de modificar o configurar las propiedades de algo que hemos creado
my_label["text"] = "New Text"
my_label.config(text= "New Text")
"""

def calculate_clicked():
    miles_to_km = round(float(miles_input.get()) * 1.609, 2)   # Fórmula para conversión de millas a km
    result_conversion["text"] = miles_to_km

# Window 
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=70)    # Esta ventana escalará de manera que quepa todo lo que pondremos ahí, pero tendrá un tamaño mínimo 
window.config(padx=20, pady=20)

# First Row


# Entrada de millas 
miles_input = Entry(width= 10, font= FONT, justify= "center")
miles_input.grid(column=1, row=0, padx=PADX_DISTANCE, pady=0)
# Mile text
miles_text = Label(text= "Miles", font= FONT)
miles_text.grid(column=2, row=0)


# Second Row

# text
equal_text = Label(text= "is equal to", font= FONT)
equal_text.grid(column=0, row=1, padx= PADX_DISTANCE, pady=0)
# resultado de la conversión
result_conversion = Label(text= 0, font= FONT)
result_conversion.grid(column=1, row=1, padx=PADX_DISTANCE, pady=0)
# Km text
km_text = Label(text= "Km", font= FONT)
km_text.grid(column=2, row=1)


# Third Row 

# Calculate button
calculate_button = Button(text= "Calculate", font= FONT, command=calculate_clicked)
calculate_button.grid(column=1, row=2)






window.mainloop()    # Esto permite que la ventana no se cierre