import numpy as np

def comparar_rendimiento(datos: list) -> dict:
    matriz = np.array(datos)

    nombres_unicos = np.unique(matriz[:, 1])

    resultados = {}

    for nombre in nombres_unicos:
        mascara = matriz[:, 1] == nombre
        filas_robot = matriz[mascara]

        col_bateria = filas_robot[:, 4].astype(float)
        col_basura = filas_robot[:, 5].astype(float)

# --- Consumo de batería ---
        bateria_final = col_bateria[-1]
        consumo_bateria = 100.0 - bateria_final
        
# --- Basura total ---
        basura_total = col_basura[-1]

# --- Eficiencia ---
        if consumo_bateria == 0:
            eficiencia = 0.0
        else:
            eficiencia = basura_total / consumo_bateria

        resultados[nombre] = {
            'consumo_bateria': float(consumo_bateria),
            'basura_total': float(basura_total),
            'eficiencia': float(eficiencia)
        }

    return resultados
