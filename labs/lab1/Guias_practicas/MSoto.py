# ====== Guía Práctica 1 ======

def ejercicio_1_1():
    print("\n----- Ejecutando Ejercicio 1 -----")

    numero = int(input("Ingresa tu número de terminos: "))

    if numero <= 0:
        print("Su numero debe ser entero positivo.")
    else:
        a = 0
        b = 1
        i = 0 #Contador

        while i < numero:
            print(f"Resultado serie {a}\n")
            x = a + b #Temporal
            a = b #Término base
            b = x #Siguiente término
            i = i + 1


def ejercicio_2_1():
    print("\n----- Ejecutando Ejercicio 2 -----")

    numero = int(input("Ingresa el número a calcular: "))

    if numero <= 0:
        print("Su número debe ser entero positivo.")
    else:
        x = 1 #Resultado Temporal
        for i in range(1, numero + 1):
            x = x*i #Mult factorial
            print(f"Factorial de {i} es {x}")


def ejercicio_3_1():
    print("\n----- Ejecutando Ejercicio 3 -----")

    numero = int(input("Ingresa el número a calcular: "))

    while numero <= 0:
        print("Su número debe ser entero positivo.")
        numero = int(input("Ingrese un número válido: "))

    x = 1 #Resultado Temporal
    for i in range(1, numero + 1):
        x = x*i #Mult factorial
        print(f"Factorial de {i} es {x}")


def ejercicio_4_1():
    print("\n----- Ejecutando Ejercicio 4 -----")

    conexion = int(input("Seleccione el tipo de conexión (1 = serie, 2 = paralelo): "))

    if conexion != 1 and conexion != 2:
        print("Error, no ingresaste un número válido.")
    else:
        cantidad = int(input("Ingrese la cantidad de resistencias: "))

        if cantidad <= 0:
            print("Error, el valor de cantidad debe ser un número entero positivo.")
        else:
            valores = []

            for i in range(1, cantidad + 1):
                r_actual = float(input(f"Ingrese valor de la resistencia {i}: "))

                while r_actual <= 0:
                    print("El valor de la resistencia debe ser mayor a 0")
                    r_actual = float(input(f"Ingrese un valor válido de la resistencia {i}: "))

                valores.append(r_actual)

            print(f"Valores de resistencia guardados: {valores}")

    if conexion == 1:
        resistencia_total = sum(valores)
        print(f"La resistencia total en serie es: {resistencia_total} Ohms")
    
    else:
        resis_paralelo = 1 / sum(1/r for r in valores)
        print(f"La resistencia total en paralelos es: {resis_paralelo} Ohms")

# ====== Guía Práctica 2 ======

def ejercicio_1_2():
    print("\n----- Ejecutando Ejercicio 1 -----")

    inicio = 10.0
    final = 12.0
    cant_decimales = 1
    cant_numeros = 10

    import random
    voltajes = [round(random.uniform(inicio,final),cant_decimales) for _ in range(cant_numeros)]


    def analizar_voltajes(voltajes):

        maximo = max(voltajes)
        minimo = min(voltajes)
        promedio = sum(voltajes)/len(voltajes)
        valormax = 12
        menores = [x for x in voltajes if x < valormax]

        return maximo, minimo, promedio, menores

    a,b,c,d = analizar_voltajes(voltajes)

    def estado_bateria(promedio):
        if promedio >= 12.2:
            return "Batería en buen estado."
        elif 11.8 < promedio < 12.19:
            return "Batería en descarga."
        else:
            return "Batería crítica."
    
    estado = estado_bateria(c)

    print("Los voltajes medidos son:",voltajes ,"\nEl valor de voltaje máximo es:",a , "\nEl valor de voltaje mínimo es:",b ,"\nEl voltaje promedio es:",c , "\nLos valores de voltaje menores a 12[V] son:",d, "\nEstado de la batería:", estado)


def ejercicio_2_2():
    print("\n----- Ejecutando Ejercicio 2 -----")

    dispositivos = {
        "Router_1": {"ip": "192.168.1.1", "estado": "activo", "trafico_mbps": 120},
        "Switch_1": {"ip": "192.168.1.2", "estado": "activo", "trafico_mbps": 80},
        "AP_1": {"ip": "192.168.1.3", "estado": "inactivo", "trafico_mbps": 0},
        "Servidor_1": {"ip": "192.168.1.10", "estado": "activo", "trafico_mbps": 250}
    }  

    def contar_activos(red):
        contador = 0
        for nombre, datos in red.items():
            if datos["estado"].lower() == "activo":
                contador +=1

        return contador
    
    total_activos = contar_activos(dispositivos)
    print(f"Hay {total_activos} dispositivos activos.")

    def trafico_total(red):
        trafico = 0
        for datos in red.values():
            if datos["estado"].lower() == "activo":
                trafico += datos["trafico_mbps"]
            
        return trafico
    
    trafico_mbps = trafico_total(dispositivos)
    print(f"El tráfico total es de: {trafico_mbps}.")

    def buscar_inactivos(red):
        equipos_inactivos = []
        for nombre, datos in red.items():
            if datos["estado"].lower() == "inactivo":
                equipos_inactivos.append(nombre)

        return equipos_inactivos
    
    inactivos = buscar_inactivos(dispositivos)
    print(f"Los dispositivos inactivos son: {inactivos}.")

    def mayor_trafico(red):
        disp_mayor_trafico = ""
        valor_trafico = -1
        for nombre, datos in red.items():
            if datos["estado"].lower() == "activo":
                trafico_actual = datos["trafico_mbps"]

                if trafico_actual > valor_trafico:
                    valor_trafico = trafico_actual
                    disp_mayor_trafico = nombre

        return disp_mayor_trafico, valor_trafico
    
    dispositivo = mayor_trafico(dispositivos)
    print(f"El dispositivo con mayor tráfico y su respectivo valor es: {dispositivo}.")
    
def ejercicio_3_2():
    cargas = [
    {"nombre": "Motor_1", "voltaje": 400, "corriente": 12, "fp": 0.86},
    {"nombre": "Bomba_1", "voltaje": 400, "corriente": 8, "fp": 0.82},
    {"nombre": "Compresor_1", "voltaje": 400, "corriente": 15, "fp": 0.90},
    {"nombre": "Ventilador_1", "voltaje": 400, "corriente": 5, "fp": 0.78}
]

    def calcular_potencia(voltaje, corriente, fp):
        raiz3 = 3**(1/2)

        return raiz3*voltaje*corriente*fp
    
    def procesar_cargas(lista_cargas):
        for equipo in lista_cargas:
            nombre = equipo["nombre"]
            v = equipo["voltaje"]
            i = equipo["corriente"]
            fp = equipo["fp"]

            pot_indiv = calcular_potencia(v, i, fp)
            equipo["potencia"] = round(pot_indiv,2)
        
        return
    
    procesar_cargas(cargas)

    def resumen_cargas(lista_cargas):
        pot_total = 0
        nombre_mayor = ""
        pot_temp = -1
        lista_menor = []
        fp_minimo = 0.80

        for equipo in lista_cargas:
            pot_actual = equipo["potencia"]
            fp_actual = equipo["fp"]
            nombre = equipo["nombre"]

            if pot_actual > pot_temp:
                nombre_mayor = nombre
                pot_temp = pot_actual

            if fp_actual < fp_minimo:
                lista_menor.append(nombre)

            pot_total += pot_actual

        return pot_total, nombre_mayor, lista_menor
    
    pot_trif_total, carga_mayor_pot, lista_cargas_menores = resumen_cargas(cargas)
    print(f"La potencia trifásica total de la instalación es: {pot_trif_total:.2f}[W]. \n La carga con mayor potencia es: {carga_mayor_pot}. \n Las cargas con factor de potencia menor a 0.80 son: {lista_cargas_menores}")

def ejercicio_4_2():
    estaciones = {
    "EST_01": {"temperatura": 42, "voltaje": 48.5, "senal": -67, "enlace": "ok"},
    "EST_02": {"temperatura": 55, "voltaje": 46.8, "senal": -81, "enlace": "ok"},
    "EST_03": {"temperatura": 39, "voltaje": 44.9, "senal": -75, "enlace": "caido"},
    "EST_04": {"temperatura": 61, "voltaje": 47.2, "senal": -88, "enlace": "ok"}
}

    def evaluar_estacion(nombre, datos):
        fallas = []

        if datos["temperatura"] > 50:
            fallas.append("Temperatura > 50° ")
        if datos["voltaje"] < 46.0:
            fallas.append("Voltaje < 46.0 [V]")
        if datos["senal"] < -80:
            fallas.append("Señal < -80 dBm")
        if datos["enlace"] != "ok":
            fallas.append("Enlace distinto de OK")

        estado = "Crítico" if len(fallas) > 0 else "Normal"

        return nombre, estado, fallas
    
    nombre_est, estado_est, lista_fallas = evaluar_estacion("EST_02", estaciones["EST_02"]) #EST-02 es la estación de prueba
    print(f"\n El estado de la estación {nombre_est} es {estado_est}, sus fallas son: {lista_fallas}.")
    
    #def evaluar_varias_estaciones(**estaciones):

       # return

    #def generar_reporte(resumen):

        #return est_evaluadas, num_criticas, mas_fallas
    
   # estaciones_ev, criticas, mayor_fallas = generar_reporte(estaciones)
    #print(f"Las estaciones evaluadas fueron: {estaciones_ev}. \n El número de estaciones críticas es: {criticas}. \n La estación con más fallas es: {mayor_fallas}.")

def menu_guia_1():
    while True:
        print("\n----- MENÚ DE GUÍA 1 -----")
        print("1. Ejecutar Ejercicio 1")
        print("2. Ejecutar Ejercicio 2")
        print("3. Ejecutar Ejercicio 3")
        print("4. Ejecutar Ejercicio 4")
        print("0. Volver atrás")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1_1()
        elif opcion == "2":
            ejercicio_2_1()
        elif opcion == "3":
            ejercicio_3_1()
        elif opcion == "4":
            ejercicio_4_1()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


def menu_guia_2():
    while True:
        print("\n----- MENÚ DE GUÍA 2 -----")
        print("1. Ejecutar Ejercicio 1")
        print("2. Ejecutar Ejercicio 2")
        print("3. Ejecutar Ejercicio 3")
        print("4. Ejecutar Ejercicio 4")
        print("0. Volver atrás")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1_2()
        elif opcion == "2":
            ejercicio_2_2()
        elif opcion == "3":
            ejercicio_3_2()
        elif opcion == "4":
            ejercicio_4_2()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


def menu_principal():
    while True:
        print("\n===== MENÚ DE GUÍAS PRÁCTICAS =====")
        print("1. Ir a Guía 1")
        print("2. Ir a Guía 2")
        print("0. Salir del programa")

        guia = input("Selecciona una guía: ")

        if guia == "1":
            menu_guia_1()
        elif guia == "2":
            menu_guia_2()
        elif guia == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()