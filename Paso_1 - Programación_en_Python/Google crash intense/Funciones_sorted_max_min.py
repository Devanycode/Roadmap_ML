### Funciones sorted, max i min

# Sorted (Ordenar una lista) 
# Siempre lo hace de menor a mayor
# Toma primero en cuenta los números y luego las letras
# No modifica la lista original, sino que devuelve una nueva lista ordenada
lista = [12, 2, 32, 19, 57, 22, 14] #Lista desordenada
print(sorted(lista)) #Ordena la lista de menor a mayor

# Max (carácter más grande de una lista)
# Min (carácter más pequeño de una lista)
## Ambos pueden hacerlo con una cadena de texto
## Y devuelven el valor según el orden alfabético
print(max(lista))
print(min(lista))