import matplotlib.pyplot as plt
import numpy as np

def graficar_recoleccion_vs_bateria(resultados: dict):
# --- Nombres Robots ---
    nombres = list(resultados.keys())
# --- Listas paralelas ---
    basura = [resultados[robot]['basura_total'] for robot in nombres]
    bateria = [resultados[robot]['consumo_bateria'] for robot in nombres]
# --- Gráfico de barras agrupadas ---
    x = np.arange(len(nombres))
    ancho = 0.35

    fig, ax = plt.subplots()
# --- Estilo Obligatorio ---
    rects1 = ax.bar(x - ancho/2, basura, ancho, label='Basura Recolectada (kg)', color='green')
    rects2 = ax.bar(x + ancho/2, bateria, ancho, label='Batería Consumida (%)', color='red')

    ax.set_title('Rendimiento: Recolección vs Consumo Energético')
    ax.set_ylabel('Cantidad')
    ax.set_xticks(x)
    ax.set_xticklabels(nombres)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()
    