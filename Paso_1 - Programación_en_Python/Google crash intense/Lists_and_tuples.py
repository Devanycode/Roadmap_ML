# Iterar sobre listas y tuplas
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
caracteres = 0
for animal in animals:
    caracteres += len(animal)  # Obtenemos la longitud de cada cadena que hay en la lista 
print("Total characters: {}, Average length: {}".format(caracteres, caracteres/len(animals))) # Devolvemos la cantidad y también el promedio

# Función enumerate para devolver valores de una lista acompañado de su índice
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners, start=1):  # La función denumarete devuelve una tupla para cada elemento de la lista
    print("{} - {}".format(index , person))

# Unión en buen formato de correos electrónicos 
def full_emails(people):    # Una variable también puede ser una lista o tupla 
    resultado = []
    for email, name in people:  # Desempaquetamos los valores de las tuplas en dos variables (ya que sabemos que son dos)
        resultado.append(f"{name} <{email}>")
    return resultado
# Esto funciona si nos dan una lista en la que sus valores son tuplas ordenadas de dos variables 
print(full_emails([("alex@example.com", "Alex Diego"),("shay@example.com", "Shay Brandt")]))
# print ['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']

# Función para crear una lista a partir de los índices pares de otra lista
def skip_elements(elements):
	lista = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			lista.append(element)
	return lista

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']