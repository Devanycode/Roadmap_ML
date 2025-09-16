# Entendiendo ciclo for 
x = 1
for i in range(5):   # i es una variable temporal, no necesariamente se usa dentro del bucle
    print(x)
    x += 1

"""También sirve para recorrer listas"""
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends: # friend es una variable temporal, que recorre uno por uno cada elemento de la lista
    print("Hi " + friend)
for i in friends:   # usar la i sería lo mismo que usar cualquier otra variable temporal 
    print("Hi " + i) 

"""En caso de queramos imprimir solamente el resultado final sin necesidad de imprimirlos todos"""
product = 1
for i in range(1,10):
   product = product * 1 
print(product)  # Imprime el resultado final del producto sin necesidad de imprimir cada paso

def to_celsius(x):
  return (x-32)*5/9
"""Se puede especificar de cuanto en cuanto se incrementa el número en el ciclo for"""
for x in range(0,101,10): # el 10 es la distancia entre cada número, en este caso de 10 en 10
                        # A esto se le llama "step" o paso
  print(x, to_celsius(x)) # Aquí contará de 0 a 100 aplicando la función to_celsius a cada número
# range(start, stop, step) # start es el número inicial, stop es el número final (no incluido), step es el incremento
