# While para contar del 1 al 10
contador_ascendente = 1
while contador_ascendente <= 10:
    print(contador_ascendente, end = " ")
    contador_ascendente += 1
# Para detenerse si un número es múltiplo de 4 
print() # Para que el siguiente bloque de código aparezca en una línea diferente
def multiplo_cuatro(x):
    while not x % 4 == 0:
        print(x, end = " ")
        x += 1
multiplo_cuatro(5)