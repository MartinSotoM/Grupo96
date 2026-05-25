import numpy as np
import matplotlib.pyplot as plt

# En este ejercicio, se utilizarán arreglos paramétricos para dibujar la serie de Fibonacci

# 1. Solicitar coeficientes 'n' al usuario para construir la espiral
n = int(input('Ingrese los coeficientes n que desea utilizar para construir la espiral (entre 6-12): '))

# 2. Generar una lista con los primeros n términos de la serie de Fibonacci
# Empezamos desde [1, 1] en lugar de [0, 1] para evitar un arco de radio 0
serie_fibo = [1, 1]

# Como ya tenemos 2 términos, iteramos desde el tercer término hasta n
for i in range(2, n):
    # Sumamos el último [-1] y el penúltimo [-2] término de la lista
    siguiente_termino = serie_fibo[-1] + serie_fibo[-2]
    # Lo agregamos a nuestra serie
    serie_fibo.append(siguiente_termino)

# (Opcional) Imprimir para verificar que se generó bien
print(f"Serie generada: {serie_fibo}")

# 3. Dibujar los cuartos de círculo con funciones trigonométricas de NumPy
fig, ax = plt.subplots()

# Centro inicial del primer arco y ángulo de inicio (en grados, convertimos con np.radians)
cx, cy = 0.0, 0.0
angulo = 0  # se incrementa 90° en cada iteración

for i in range(n):
    r = serie_fibo[i]  # radio del arco = término actual de Fibonacci

    # Cuarto de círculo: arco de 90° desde el ángulo actual
    theta = np.linspace(np.radians(angulo), np.radians(angulo + 90), 100)

    # Ecuaciones paramétricas del arco
    x = cx + r * np.cos(theta)
    y = cy + r * np.sin(theta)
    ax.plot(x, y, 'b', lw=2)

    # Actualizar el centro para el siguiente arco
    # El desplazamiento usa la diferencia (r_actual - r_siguiente) proyectada
    # sobre la dirección del extremo del arco (angulo + 90°)
    if i < n - 1:
        r_siguiente = serie_fibo[i + 1]
        angulo_fin = np.radians(angulo + 90)
        cx += (r - r_siguiente) * np.cos(angulo_fin)
        cy += (r - r_siguiente) * np.sin(angulo_fin)

    # Rotar 90° para el próximo arco
    angulo += 90

# 4. Ajustes visuales
ax.set_aspect('equal')  # proporción simétrica, equivalente a plt.axis('equal')
ax.grid(True, linestyle='--', alpha=0.6)
plt.title(f'Espiral de Fibonacci ({n} coeficientes)')
plt.show()