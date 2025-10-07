"""

with open("./Input/Letters/starting_letter.txt", "r") as file:
    first_line = file.readline()    # Leemos sólo la primera línea para modificar el nombre
    after_lines = file.readlines()  # Como ya leyó la primera línea, leerá sólo de ahí en adelante
    lines_text = "".join(after_lines)   # Unimos todas las líneas menos la primera en una cadena de texto 

lines_text = lines_text.replace("Angela", "Devany")   # Reemplazo el nombre de mi maestra por el mío

with open("./Input/Names/invited_names.txt", "r") as guests:
    names = guests.readlines()  # Leemos todas las líneas 

    # Vamos a llamar a cada nombre que haya creando una carta personalizado para cada uno
    for name in range(len(names)):
        
        # Como los nombres vienen con saltos de línea, se los quitamos
        guest = names[name].strip()
        # Poner el nombre del invitado en la carta reemplazando el "name"
        name_guest = first_line.replace("[name]", f"{guest}") 
        # Unir toda la carta
        letter = name_guest + lines_text
        # Nombre personalizado del archivo que vamos a crear
        letter_name = "letter_for_" + names[name].strip() + ".txt"

        # Creación de la carta personalizada 
        with open(f"./Output/ReadyToSend/{letter_name}", mode= "w") as invitation:            
            invitation.write(letter)
"""

# Nueva versión
with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    
with open("Input/Names/invited_names.txt") as guests:
    names = guests.readlines()

for name in names:
    name = name.strip()    # Quitamos los saltos de línea de los nombres
    new_letter = letter.replace("[name]", f"{name}").replace("Angela", "Devany")
    letter_name = f"letter__for_{name}"
    with open(f"Output/ReadyToSend/{letter_name}", mode= "w") as letter_names:
        letter_names.write(new_letter)

