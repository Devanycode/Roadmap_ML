import numpy as np

one_dimensional_array = np.array([10, 12])
# print(one_dimensional_array)

# Otra forma de crear arrays
c = np.arange(1, 20, 3)    # comienza en 1, va hasta 20-1, cuenta de 3 en 3 (igual que un range)
# print(c)

# Una forma de hacer un array con una cantidad determinada de valores
# Los valores se separan por la misma diferencia entre sí hasta llegar al número mayor en la cantidad de valores especificada
lin_spaced_arr = np.linspace(0, 100, 5, dtype=int)
# print(lin_spaced_arr)

# Crear Arrays multidimensionales
two_dim_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(two_dim_arr)


# Multidimensional array using reshape()

# 1-D array 
one_dim_arr = np.array([1, 2, 3, 4, 5, 6])

multi_dim_arr = np.reshape(
                one_dim_arr,
               (2,3) # dimensions of the new array
              )
# print(multi_dim_arr)

# ATRIBUTOS ndarray
# .ndim (dimensiones)
# .shape (su forma en filas, columnas)
# .size (cantidad de elementos)


# OPERACIONES MATEMÁTICAS
arr_1 = np.array([2, 4, 6])
arr_2 = np.array([1, 3, 5])

addition = arr_1 + arr_2
# print(addition)

subtraction = arr_1 - arr_2
# print(subtraction)

multiplication = arr_1 * arr_2
# print(multiplication)

# Por escalar
vector = np.array([1, 2])
arr_scalar = vector * 1.6
# print(arr_scalar)

# INDEXING AND SLICING

# Unidimensional
# Seleccionar el tercer elemento en el array
a = ([1, 2, 3, 4, 5])
# print(a[2])

# Indexing on a 2-D array
two_dim = np.array(([1, 2, 3],
          [4, 5, 6], 
          [7, 8, 9]))
          
# Tercera fila, 2 columna
# print(two_dim[2][1])

# SLICING SYNTAX
# array[start:end:step]
# 
# print(a[1:5:2])

sliced_arr_1 = two_dim[0:2]
# Cuando son matrices multidimensionales también se parten, empezando por las filas, y luego las columnas
# print 
# array([[1, 2, 3],
#       [4, 5, 6]])

# MEJOR FORMA PARA HACER SLICING EN LUGAR DE [][][][][]
sliced_two_dim_cols = two_dim[:,1]    # row, column Indicas lo que quieres de las filas y de las columnas
# print(sliced_two_dim_cols)



matriz = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

# Dividimos en 2 partes iguales
partes = np.vsplit(matriz, 2)

# print(partes[0]) # Columnas 0 y 1
# print(partes[1]) # Columnas 2 y 3


# También se puede apilar (stack) o por el contrario cortar (split) una matriz
a1 = np.array([[1,1], 
               [2,2]])
a2 = np.array([[3,3],
              [4,4]])

# De esta forma apilamos de forma vertical
vert_stack = np.vstack((a1, a2))
print(vert_stack)
# De esta forma apilamos de forma horizontal
horz_stack = np.hstack((a1, a2))
print(horz_stack)

print(np.vsplit(vert_stack, 2)[1])
print(np.hsplit(horz_stack, 2)[0])