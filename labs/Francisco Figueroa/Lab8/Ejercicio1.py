import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1 – Repaso de NumPy y Matplotlib: Señal Senoidal
# Se simula la lectura de un sensor de corriente alterna utilizando arreglos de NumPy.
# La señal senoidal representa una onda AC y se grafica con Matplotlib para su análisis visual.

# 1. Crear el arreglo de tiempo: 100 puntos entre 0 y 10 segundos
t = np.linspace(0, 10, 100)  # equivalente a linspace(0,10,100) en MATLAB

# 2. Calcular la señal senoidal sobre todo el arreglo (vectorizado, sin for)
y = np.sin(t)  # np.sin opera elemento a elemento: y[i] = sin(t[i])

# 3. Graficar la señal con etiquetas y grilla para facilitar la lectura
plt.plot(t, y, color='blue')
plt.title("Señal Senoidal – Simulación de Sensor AC")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()