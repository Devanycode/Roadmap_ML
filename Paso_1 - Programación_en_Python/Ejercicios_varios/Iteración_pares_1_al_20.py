# Iteración de pares entre 1 y 20 usando for
print([x for x in range(1,21) if x % 2 == 0]) # Quería probar con algo comprimido
# Llegar a la misma respuesta sin compresion
for x in range(1,21):
    if x % 2 == 0:
        print(x, end = " ") 