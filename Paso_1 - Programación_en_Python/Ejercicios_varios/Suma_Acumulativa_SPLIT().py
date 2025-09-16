# Suma acumulativa
numeros = input("Ingrese números números enteros usando espacios entre sí ")    # Si no están separados por espacios dará error
lista = [int(x) for x in numeros.split()]
acumulacion = 0
for i in range(len(lista)):
    acumulacion += lista[i]
print(f"La suma total entre todos los números de su lista es {acumulacion}") # Uso de f"{}" para imprimir textos sin usar str()
