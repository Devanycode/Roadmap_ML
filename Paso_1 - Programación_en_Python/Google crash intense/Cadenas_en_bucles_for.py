# Bucles for en Cadenas 

nombre = "Samuel"   # definimos la cadena
for i in nombre:
    print("La siguiente letra es:",i) # i recorrerá cada término que tenga la cadena y parará cuando llegue al último término.

"""Imprimirá lo siguiente"""
# La siguiente letra es: S
# La siguiente letra es: a
# La siguiente letra es: m
# La siguiente letra es: u
# La siguiente letra es: e
# La siguiente letra es: l

# se puede hacer lo mismo con un While
saludo = "Hello"
indice = 0
while indice < len(saludo): # len(saludo) indica el número total de carácteres que tiene la cadena
    print(saludo[indice])   # Indica la posición que imprimirá de la cadena 
    indice += 1

# Podemos hacer lo mismo con un troceado, y es más específico la cantidad de carácteres que queremos imprimir cada vez
while indice < len(saludo): 
    print(saludo[indice:indice+1])   # Esto quiere decir [inicio:fin], esto siempre imprimirá una cadena de texto que podemos decidir su tamaño
    indice += 1

