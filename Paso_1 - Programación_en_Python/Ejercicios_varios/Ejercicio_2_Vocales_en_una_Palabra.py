# Ejercicio diferenciador de vocales
vocales = ['a','e','i','o','u','A','E','I','O','U']
palabra = str(input("Ingrese una palabra cualquiera "))
contador = 0
for letra in range(0,len(palabra)):
    for i in range(0,10):
        if palabra[letra:letra+1] == vocales[i]:
            contador += 1
print("En su palabra hay " + str(contador) + " vocales.")

# Solución simplificada con ayuda
contador = 0
for letra in palabra:
    if letra.lower() in "aeiou":    # podemos usar el in en un if en lugar de == para comparar con un valor que haya en una cadena en lugar de comparar caracter por caracter
        contador += 1               # de esa manera nos ahorramos el crear una lista con todos los valores y de compararlos uno por uno
print("En su palabra hay " + str(contador) + " vocales")
