import pandas as pd
import os

# En este ejercicio, se carga un CSV con datos incompletos, se limpian los NaN y se calcula un promedio por alumno

# directorio donde está el script, independiente desde dónde se ejecute
carpeta_script = os.path.dirname(os.path.abspath(__file__))

# 1. Cargar el archivo CSV usando ruta absoluta construida desde el script
ruta_csv = os.path.join(carpeta_script, "notas_alumnos.csv")
df_notas = pd.read_csv(ruta_csv)
print(f"Filas antes de limpiar: {len(df_notas)}")

# 2. Eliminar filas con valores nulos para evitar promedios erróneos
# usar nueva variable preserva df_notas original para comparación
df_limpio = df_notas.dropna()
print(f"Filas después de limpiar: {len(df_limpio)}")

# 3. Calcular promedio aritmético entre las dos evaluaciones parciales
# promedio = (Parcial_1 + Parcial_2) / 2
df_limpio["Promedio"] = (df_limpio["Parcial_1"] + df_limpio["Parcial_2"]) / 2

# 4. Imprimir el DataFrame limpio con promedios
print(f"\nRegistro de notas (limpio):\n{df_limpio.to_string(index=False)}")