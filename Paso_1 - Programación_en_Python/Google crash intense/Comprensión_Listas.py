""" Comprensión de listas """

# Hacer una lista con los múltiplos de 7 
multiplos = [x*7 for x in range(1,11)]  # El valor de la derecha es el que determina que valores se agregarán
# Los resultados que se agreguen serán modificados por el valor de la izquierda
print(multiplos)
# print [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
z = [x for x in range(0,101) if x % 3 == 0] # de nuevo lo de la derecha decide qué sale, lo de la izquierda lo modifica o lo imprime simple como en este caso
print(z)
# print [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]