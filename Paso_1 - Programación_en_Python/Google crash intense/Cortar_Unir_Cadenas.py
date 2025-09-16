# Cortar y Unir Cadenas

"""Cortar Cadenas"""
string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”

# Prints “” 
print(string1[55:]) # Cuando el Indice va más allá del final de la cadena se imprime una cadena vacía

# Prints “Earthlings” again
print(string1[-10:])    # El Indice va hacia atrás, el Indice Final va hacia la derecha (Normal)

"""Uso de Stride"""
# Prints “Getns atlns”
print(string1[0::2]) # Los dobles dos puntos sirven para decir que se contará desde cero y el paso será de 2 en 2

# Prints “sgnilhtraE ,sgniteerG”
print(string1[::-1])
print(string1[5::-1])   #print iteerG, empieza en el caracter 5 y va yéndose de uno en uno hacia atrás (El cero)


"""Unir Cadenas"""
# Prints “Hello world”
print("Hello" + " " + "world") 

# Para Concatenar los elementos de una lista también se puede hacer esto
greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world", mediante el .join unimos los valores de la lista con un espacio
# Al usar .join() especificamos el carácter con el que uniremos una lista

