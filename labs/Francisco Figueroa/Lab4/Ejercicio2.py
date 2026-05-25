import pandas as pd

# En este ejercicio, se aplican operaciones vectorizadas sobre columnas y se filtran filas con condiciones lógicas

# 1. Crear el DataFrame desde el diccionario entregado en el enunciado
datos_juegos = {
    "Juego":                ["Cyberpunk 2077", "Minecraft", "Hollow Knight", "FIFA 24"],
    "Precio_Base":          [40000, 15000, 7500, 45000],
    "Descuento_Porcentaje": [50, 0, 20, 10]
}
df_juegos = pd.DataFrame(datos_juegos)

# 2. Calcular precio final de forma vectorizada (sin ciclos for)
# precio_final = precio_base - (precio_base * descuento / 100)
monto_descuento = df_juegos["Precio_Base"] * (df_juegos["Descuento_Porcentaje"] / 100)
df_juegos["Precio_Final"] = df_juegos["Precio_Base"] - monto_descuento

# 3. Filtrar juegos en oferta (precio final < 20000 CLP)
# separar la máscara facilita depuración y re-uso
filtro_oferta = df_juegos["Precio_Final"] < 20000
juegos_en_oferta = df_juegos[filtro_oferta]

# 4. Mostrar resultado
print("Juegos con Precio_Final < 20.000 CLP:")
print(juegos_en_oferta.to_string(index=False))