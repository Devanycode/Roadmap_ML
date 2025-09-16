# Tabla de multiplicar con bucle while que no excede de 25
def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:   # Se especifica que el multiplicador va hasta 5
        result = number * multiplier 
        if  result > 25:
            break    # Si el resultado es mayor a 25 se termina el bucle
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
multiplication_table(3)
multiplication_table(5)
multiplication_table(7)
# No se tiene que usar la función print porque ya está dentro de la función 
# Solamente hay que asignarle un valor desde afuera y ya se imprimirá el resultado