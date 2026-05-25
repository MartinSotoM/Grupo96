import matplotlib.pyplot as plt

# Diccionario con los resultados de la encuesta
encuesta = {'Python': 45, 'C++': 28, 'C': 15, 'Java': 12, 'Rust': 8}

# 1. Extraer dinámicamente llaves y valores del diccionario
lenguajes = list(encuesta.keys())
votos     = list(encuesta.values())

# 2. Crear gráfico de barras con colores representativos por lenguaje
colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
plt.bar(lenguajes, votos, color=colores)

# 3. Título, etiquetas de ejes y grilla en Y para facilitar la lectura
plt.title('Lenguaje de Programación Favorito - EIE 434')
plt.xlabel('Lenguaje')
plt.ylabel('Cantidad de votos')
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()