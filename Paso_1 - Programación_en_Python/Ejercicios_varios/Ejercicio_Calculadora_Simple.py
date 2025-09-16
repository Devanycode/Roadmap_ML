# Calculadora simple
num1 = int(input("Ingrese un número "))
num2 = int(input("Ingrese otro número "))
operacion = input("Ingrese uno de los siguientes símbolos: +  -  *  /  ")
if operacion == "+":
    print("La suma de los dos valores es " + str(num1 + num2))
elif operacion == "-":
    print("La resta del primer número por el segundo es " + str(num1 - num2))
elif operacion == "*":
    print("La multiplicación de los dos números que ingresó es " + str(num1 * num2))
elif operacion == "/":
    if num2 == 0:
        print("El segundo número es cero, y no se puede dividir por cero")
    else:
        print("La división entre el primer número y el segundo es " + str(num1 / num2))
else:
    print("No ingresó uno de los símbolos de operación sugeridos, intente de nuevo.")