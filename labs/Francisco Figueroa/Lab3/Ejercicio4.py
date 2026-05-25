import random
import time
import numpy as np

# Cantidad de elementos
N = 5_000_000

# 1. Crear lista clásica de Python con números aleatorios
lista_python = [random.random() for _ in range(N)]

# 2. Crear array NumPy desde los mismos datos (comparación justa, mismos valores)
array_numpy = np.array(lista_python)

# 3. Cuadrado de cada elemento con Python puro (list comprehension)
inicio_py = time.time()
cuadrados_py = [x**2 for x in lista_python]
fin_py = time.time()

tiempo_py = fin_py - inicio_py

# 4. Cuadrado vectorizado con NumPy (operación aplicada al array completo en C)
inicio_np = time.time()
cuadrados_np = array_numpy ** 2  # NumPy opera sobre todos los elementos a la vez
fin_np = time.time()

tiempo_np = fin_np - inicio_np

# 5. Imprimir resultados y comparación
print(f"Tiempo Python puro  : {tiempo_py:.4f} s")
print(f"Tiempo NumPy        : {tiempo_np:.6f} s")

if tiempo_np > 0:
    print(f"NumPy fue {tiempo_py / tiempo_np:.2f}x más rápido")