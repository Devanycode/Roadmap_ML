# Romper bucles infinitos en while loops
x=0
while x % 2 == 0:
    x = x / 2
    # Si bien el ciclo funcionaría para los números pares positivos y negativos
    # Este bucle es infinito porque x siempre será 0, por lo tanto, no se romperá.

"""Maneras de romper un bucle infinito en while loops:"""
if x != 0:
    while x % 2 == 0:
        x = x / 2
# Otra forma de romper el bucle infinito
while x != 0 and x % 2 == 0:
    x = x / 2
# Otra forma de romper el bucle infinito
while x % 2 == 0:
    if x == 0:
        break  # En caso de que x sea 0, se rompe el bucle (aunque fuera infinito sin esto)
    x = x / 2 # Pero si x no es 0, el bucle se ejecutará normalmente y se ignorará el break
