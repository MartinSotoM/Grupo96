#Laboratorio 2

#Ejercicio 1
def ejercicio_1():
    red_esp8266 = {
        "Nodo_Tanque": {"ip": "192.168.1.10", "estado": "activo", "salida_dac": 3000} ,
        "Nodo_Motor": {"ip": "192.168.1.11", "estado": "falla", "salida_dac": 0} ,
        "Nodo_Valvula": {"ip": "192.168.1.12", "estado": "inactivo", "salida_dac": 150} ,
        "Nodo_Caldera": {"ip": "192.168.1.13", "estado": "activo", "salida_dac": 4000}
        }

    def auditar_red(nodos):
        ip_fallas = []
        nodos_totales = 0
        nodos_activos = 0
        prom_sal = 0

        for nombre, datos in nodos.items():
            nom_ip = datos["ip"]
            est_actual = datos["estado"]
            sal_dac = datos["salida_dac"]

            if est_actual == "falla" or est_actual == "inactivo":
                ip_fallas.append(nom_ip)

            if est_actual == "activo":
                prom_sal += sal_dac
                nodos_activos += 1

            nodos_totales += 1

        prom_sal = prom_sal/nodos_activos

        return ip_fallas, nodos_totales, prom_sal

    ip_fallasORinact, nod_reg, prom_salidaDAC = auditar_red(red_esp8266)
    print(f"El total de nodos registrados es: {nod_reg}. \n La lista de los nodos en estado falla o inactivo es: {ip_fallasORinact} \n El promedio de la salida_dac es: {prom_salidaDAC}.")

def menu_lab2():
    while True:
        print("\n----- MENÚ DE LABORATORIO 2 -----")
        print("1. Ejecutar Ejercicio 1")
        print("2. Ejecutar Ejercicio 2")
        print("3. Ejecutar Ejercicio 3")
        print("0. Volver atrás")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_lab2()