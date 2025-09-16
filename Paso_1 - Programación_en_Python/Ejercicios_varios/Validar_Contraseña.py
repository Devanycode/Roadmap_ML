"""Validar Contraseña"""
import random 

alfabeto = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z']

def sugerir_contraseñas():
    ejemplo = str(random.randint(0, 9)) + random.choice(alfabeto).upper()
    for x in range(6):
        ejemplo += random.choice(alfabeto)
    return ejemplo

def contraseña_valida():
    contraseña_correcta = False
    while not contraseña_correcta:
        numeros = 0
        print("Contraseña sugerida: ", end="")
        print(sugerir_contraseñas())
        contraseña = input("Ingrese su contraseña. ")
        for caracter in contraseña:
            if caracter.isnumeric():
                numeros += 1
        if len(contraseña) < 8:
            print("Su contraseña debe tener 8 o más carácteres.")
        elif contraseña.lower() == contraseña:
            print("Su contraseña debe tener al menos 1 mayúscula.")
        elif numeros == 0:
            print("Su contraseña debe contener al menos 1 número.")
        else:
            return f"Su contraseña <{contraseña}> es válida."
            contraseña_correcta = True 

print(contraseña_valida())