# Verificación de un número primo
print("Vamos a verificar si el número que ingresa es un número primo")
numero = int(input("Ingrese un número entero "))
primo = 0
numero_entero = 0
if numero == 0:
    numero = int(input("Su número es cero, Ingrese otro número "))
for x in range(1,numero+1):
    if numero % x == 0:
        primo += 1
if primo == 2:
    print("Su número es primo")
else:
    print("Su número no es primo")