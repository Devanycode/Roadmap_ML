"""Calculadora con Funciones"""
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicación(a, b):
    return a * b 
def división(a, b):
    return a / b 

calculadora_encendida = True
while calculadora_encendida == True:
    num1 = float(input("Ingrese un número cualquiera:  "))
    num2 = float(input("Ingrese otro número cualquiera:  "))
    operación = input("Escriba 'suma', 'resta', 'multiplicación', 'división' según la operación que quiera realizar  ")
    if operación == 'suma':
        print(suma(num1, num2))
    elif operación == 'resta':
        print(resta(num1, num2))
    elif operación == 'multiplicación':
        print(multiplicación(num1, num2))
    elif operación == 'división':
        print(división(num1, num2))

    continuar = input("Si quiere realizar otro cálculo escriba 'si' si quiere terminar escriba 'no'. ")
    if continuar == 'no':
        calculadora_encendida = False
    print("\n"*3)

print("Ha finalizado su cálculo")
