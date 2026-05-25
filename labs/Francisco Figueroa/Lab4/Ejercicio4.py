import pandas as pd
import matplotlib.pyplot as plt

# En este ejercicio, se cargan datos de ventas desde un CSV y se grafican tendencias mensuales con líneas superpuestas

# 1. Cargar el archivo CSV con el registro mensual de ventas
df_ventas = pd.read_csv("ventas_tienda.csv")

# 2. Definir el lienzo antes de graficar para controlar el tamaño de salida
plt.figure(figsize=(9, 5))

# 3. Graficar las ventas de Laptops y Smartphones en el mismo lienzo
# label es necesario para que plt.legend() identifique cada línea
plt.plot(df_ventas["Mes"], df_ventas["Laptops"],     color="steelblue",  label="Laptops",     marker="o")
plt.plot(df_ventas["Mes"], df_ventas["Smartphones"], color="darkorange", label="Smartphones", marker="s")

# 4. Configurar elementos visuales del gráfico
plt.title("Evolución de Ventas Mensuales")
plt.xlabel("Mes del Año")
plt.ylabel("Unidades Vendidas")
plt.legend()

# linestyle y alpha suavizan la grilla para que no compita con los datos
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()