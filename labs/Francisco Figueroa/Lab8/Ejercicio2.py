import pandas as pd

# Ejercicio 2 – Repaso de Pandas: Filtro de Inventario
# Se trabaja con un inventario de componentes electrónicos almacenado en un diccionario.
# Se convierte a DataFrame y se filtra para identificar los componentes con stock crítico
# (menos de 10 unidades), los cuales deben ser repuestos en bodega.

datos = {
    "Componente": ["Arduino", "Resistencia 1k", "Capacitor", "Motor DC"],
    "Stock":      [5, 500, 120, 3]
}

# 1. Convertir el diccionario en un DataFrame estructurado
df_inventario = pd.DataFrame(datos)

# 2. Filtro lógico: stock crítico = menos de 10 unidades disponibles
stock_critico = df_inventario["Stock"] < 10  # devuelve una serie de True/False
df_critico = df_inventario[stock_critico]    # selecciona solo las filas True

# 3. Mostrar los componentes que necesitan reposición
print("--- Componentes con Stock Crítico ---")
print(df_critico.to_string(index=False))