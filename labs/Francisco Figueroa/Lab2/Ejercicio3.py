# --- Datos para el Ejercicio 3 (Tuplas y Diccionarios) ---
# Puedes desempaquetar esta tupla en *args
angulos_prueba = (45, 90, -30, 15)

#Calibración de Brazo Robótico

# Puedes desempaquetar este diccionario en **kwargs
configuracion_robot = {
    "velocidad": 50,
    "torque_max": 120,
    "herramienta": "pinza"}

# 1. Desarrolla una función llamada calibrar_robot(*args, **kwargs)
def calibrar_robot(*args, **kwargs):
    # 2. *args: sumar ángulos y contar articulaciones en movimiento
    desplazamiento_total = sum(args)
    print(f"Articulaciones en movimiento: {len(args)}")
    print(f"Desplazamiento total en grados: {desplazamiento_total}")

    # 3. y 4. **kwargs: advertencia si torque_max > 100, resto tabular
    print("\nConfiguraciones recibidas:")
    for clave, valor in kwargs.items():
        if clave == "torque_max" and valor > 100:
            print(f"  !!! Peligro de sobrecarga: torque_max = {valor}")
        else:
            print(f"  {clave} : {valor}")

# 5. Ejecuta la función usando el operador de desempaquetado
calibrar_robot(*angulos_prueba, **configuracion_robot)