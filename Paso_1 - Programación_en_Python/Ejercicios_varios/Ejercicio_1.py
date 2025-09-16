"""Ejercicio 1"""
# Pide al Usuario 5 números e imprime la suma total solo de los positivos
print("A continuación ingrese 5 números enteros")
a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))
d = int(input("Número 4: "))
e = int(input("Número 5: "))
lista_numeros = [a,b,c,d,e]
sumatoria = 0
for i in range(5):
    if lista_numeros[i] > 0:
        sumatoria += lista_numeros[i]
print(sumatoria)
