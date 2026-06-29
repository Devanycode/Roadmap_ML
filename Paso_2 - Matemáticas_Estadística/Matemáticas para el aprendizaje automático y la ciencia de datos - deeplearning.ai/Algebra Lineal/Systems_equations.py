import numpy as np
import matplotlib.pyplot as plt
from utils import plot_lines

# Creación de matrices A y b (resultados)
A = np.array([[-1, 3],
              [3, 2]], dtype='float32')
print(f"shape of A: {A.shape}")

b = np.array([7, 1], dtype='float32')    # Aunque estos sean los resultados, pueden quedar en una sola fila, sin necesidad de crear muchas
print(f"shape of b: {b.shape}")


# LINALG
# Resolver Sistema
x = np.linalg.solve(A, b)
# print(f"Solution: {x}")

# Hallar determinante 
d = np.linalg.det(A)
# print(f"Determinant of matrix A: {d:.2f}")

A_system = np.hstack((A, b.reshape(2, 1)))
# print(A_system)
# plot_lines(A_system)


# SISTEMAS SIN SOLUCION 
A_2 = np.array([[-1, 3],
                [3, -9]], dtype='float32')

b_2 = np.array([7, 1], dtype='float32')

d_2 = np.linalg.det(A_2)
print(f"Determinant of matrix A_2: {d_2:.2f}")    # 0.00

try:
    x_2 = np.linalg.solve(A_2, b_2)
except np.linalg.LinAlgError as err:
    print(f"Error: {err}")


