# --- Datos para el Ejercicio 1 (Diccionarios) ---
red_esp8266 = {
    "Nodo_Tanque": {"ip": "192.168.1.10", "estado": "activo", "salida_dac": 3000},
    "Nodo_Motor": {"ip": "192.168.1.11", "estado": "falla", "salida_dac": 0},
    "Nodo_Valvula": {"ip": "192.168.1.12", "estado": "inactivo", "salida_dac": 150},
    "Nodo_Caldera": {"ip": "192.168.1.13", "estado": "activo", "salida_dac": 4000},
}

#Gestión de Nodos de Control:

def auditar_red(nodos):
    # la cantidad total de nodos registrados.
    total_nodos = len(nodos)
    
    # lista con las direcciones IP de los nodos que están en estado "falla" o "inactivo"
    ips_problema = []
    
    # acumuladores para el promedio de salida_dac de nodos activos
    suma_dac = 0
    nodos_activos = 0

    for nombre, datos in nodos.items():
        if datos["estado"] in ["falla", "inactivo"]:
            ips_problema.append(datos["ip"])
        # El valor promedio de la "salida_dac", considerando solo los nodos en estado "activo"
        elif datos["estado"] == "activo":
            suma_dac += datos["salida_dac"]
            nodos_activos += 1

    promedio_dac = suma_dac / nodos_activos if nodos_activos > 0 else 0

    return total_nodos, ips_problema, promedio_dac


# Llama a la función, guarda los valores de retorno en variables separadas
# e imprímelos con un formato claro
total, ips_revision, promedio = auditar_red(red_esp8266)

print(f"Total de nodos registrados: {total}")
print(f"IPs que requieren revisión (falla/inactivo): {ips_revision}")
print(f"Promedio de salida DAC (nodos activos): {promedio:.2f}")