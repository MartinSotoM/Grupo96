import pandas as pd

# En este ejercicio, se crea un DataFrame desde un diccionario y se inspeccionan sus propiedades estructurales

# 1. Crear el diccionario con 4 canciones favoritas
datos_playlist = {
    "Cancion":      ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Comfortably Numb"],
    "Artista":      ["Queen",             "Led Zeppelin",       "Eagles",           "Pink Floyd"],
    "Duracion_seg": [354,                 482,                  391,                382]
}

# 2. Convertir el diccionario en un DataFrame (equivalente a una tabla 2D)
df_playlist = pd.DataFrame(datos_playlist)

# 3. Imprimir propiedades estructurales del DataFrame
print(f"Dimensiones del DataFrame (filas, columnas): {df_playlist.shape}")
print(f"\nTipos de datos por columna:\n{df_playlist.dtypes}")