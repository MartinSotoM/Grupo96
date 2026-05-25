import random
import time
import numpy as np

# Tamaño de las matrices
N = 100

# 1. Crear matrices con listas anidadas (Python puro)
A_lista = [[random.random() for _ in range(N)] for _ in range(N)]
B_lista = [[random.random() for _ in range(N)] for _ in range(N)]

# 2. Crear las versiones equivalentes como arrays de NumPy
A_np = np.array(A_lista)
B_np = np.array(B_lista)

# 3. Multiplicación clásica con tres ciclos for anidados
# Inicializamos la matriz resultado en 0.0 (float, porque acumulamos productos reales)
C_lista = [[0.0] * N for _ in range(N)]

inicio_py = time.time()
for i in range(N):
    for j in range(N):
        for k in range(N):
            # Definición estándar del producto matricial: C[i][j] = Σ A[i][k] * B[k][j]
            C_lista[i][j] += A_lista[i][k] * B_lista[k][j]
fin_py = time.time()

tiempo_py = fin_py - inicio_py

# 4. Multiplicación con NumPy (vectorizada, ejecutada en C internamente)
inicio_np = time.time()
C_np = A_np @ B_np  # equivalente a np.dot(A_np, B_np)
fin_np = time.time()

tiempo_np = fin_np - inicio_np

# 5. Imprimir resultados y comparación
print(f"Tiempo Python puro : {tiempo_py:.4f} s")
print(f"Tiempo NumPy       : {tiempo_np:.6f} s")

if tiempo_np > 0:
    print(f"NumPy fue {tiempo_py / tiempo_np:.2f}x más rápido")