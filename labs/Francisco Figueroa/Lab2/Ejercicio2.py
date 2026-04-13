# --- Datos para el Ejercicio 2 (Listas) ---
coords_x = [2, 8, 8, 2]
coords_y = [1, 1, 5, 5]

#Geometría de zonas de análisis:

# 1. Define una función llamada evaluar_zona_poligono(coords_x, coords_y)
def evaluar_zona_poligono(coords_x, coords_y):
    # 2. Bounding Box: ancho y alto
    ancho = max(coords_x) - min(coords_x)
    alto = max(coords_y) - min(coords_y)

    # Área de la caja delimitadora (ancho x alto)
    area = ancho * alto

    # Tupla con el centro geométrico aproximado (Xcentro, Ycentro)
    centro = ((max(coords_x) + min(coords_x)) / 2, (max(coords_y) + min(coords_y)) / 2)

    return area, centro


# 3. Prueba la función pasando las listas coords_x y coords_y,
# imprime el área calculada y el centro del polígono de análisis
area, centro = evaluar_zona_poligono(coords_x, coords_y)

print(f"Área de la zona de análisis: {area}")
print(f"Centro del polígono de análisis: {centro}")