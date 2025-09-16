# Anidar funciones for 
"""Hacer un dominó"""
for derecha in range(7): # la posición derecha en el dominó, va de 0 a 6
    for izquierda in range(derecha, 7): # la posición izquierda también va de 0 a 6, pero empieza en la posición que indique la derecha 
        print("[", derecha, "|", izquierda, "]", end=" ") # se usa end para que no salte de línea sino que separa por un espacio
    print() # Esto imprime un salto de línea, creando una nueva línea de salida