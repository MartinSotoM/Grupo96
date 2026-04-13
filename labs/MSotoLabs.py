import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import time

#LABORATORIO 1

def ejercicio_1_1():
    print("\n----- Ejecutando Ejercicio 1 -----")

    voltaje = float(input("Ingresa un valor de voltaje (en voltios):"))
    corriente = float(input("Ingresa un valor de corriente (en amperios):"))

    resistencia = voltaje/corriente
    p_disipada = voltaje * corriente

    print(f"La resistencia tiene un valor de: {resistencia} Ohms. \nLa potencia disipada tiene un valor de: {p_disipada} Watts")

    if p_disipada > 1000:
        print("¡Peligro! Alta disipación de potencia detectada.")
    else:
        print("Operación en rangos seguros.")


def ejercicio_2_1():
    print("\n----- Ejecutando Ejercicio 2 -----")

    v_inicial = float(input("Ingrese un valor de voltaje inicial:"))
    v_min = float(input("Ingrese un valor de voltaje mínimo de operación:"))
    horas = 0

    while v_inicial > v_min:
        v_inicial *= 0.97
        horas += 1

    print(f"Pasaron {horas} horas antes de que el banco de baterías requiriera una recarga.")


def ejercicio_3_1():
    print("\n----- Ejecutando Ejercicio 3 -----")

    while True:
        print("\n--- Menú de Conversión de Unidades ---")
        print("1. Convertir miliamperios (mA) a amperios (A).")
        print("2. Convertir microfaradios (µF) a faradios (F).")
        print("3. Convertir kiloohmios (kΩ) a ohmios (Ω).")
        print("4. Salir")

        conversion = input("Selecciona una opción: ")

        if conversion == "1":
            print("Convirtiendo...")
        elif conversion == "2":
            print("Convirtiendo...")
        elif conversion == "3":
            print("Convirtiendo...")
        elif conversion == "4":
            print("Volviendo atrás...")
            break
        else:
            print("Error: opción inválida.")


def ejercicio_4_1():
    print("\n----- Ejecutando Ejercicio 4 -----")

    while True:
        temperatura = float(input("Ingrese una lectura de temperatura (en grados Celsius):"))

        if 20 <= temperatura <= 45:
            print("Estado normal.")
        elif 45 < temperatura <= 75:
            print("Advertencia: Encendiendo ventiladores auxiliares.")
        elif temperatura > 75:
            print("¡Peligro Crítico! Apagando servidor de emergencia")
            break
        else:
            print("Error: opción inválida.")

#LABORATORIO 2

def ejercicio_1_2():
    print("\n----- Ejecutando Ejercicio 1 -----")

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
    print(f"El total de nodos registrados es: {nod_reg}. \nLa lista de los nodos en estado falla o inactivo es: {ip_fallasORinact} \nEl promedio de la salida_dac es: {prom_salidaDAC}.")


def ejercicio_2_2():
    print("\n----- Ejecutando Ejercicio 2 -----")

    coords_x = [2 , 8 , 8 , 2]
    coords_y = [1 , 1 , 5 , 5]

    def evaluar_zona_poligono(x, y):
        ancho = max(x) - min(x)
        alto = max(y) - min(y)

        area = ancho*alto

        x_centro = (max(x) + min(x))/2
        y_centro = (max(y) + min(y))/2

        centro = (x_centro, y_centro)

        return area, centro
    
    area_BoundBox, tupla_centro = evaluar_zona_poligono(coords_x, coords_y)
    print(f"El área calculada es de: {area_BoundBox}. \nEl centro del polígono de análisis es: {tupla_centro}.")


def ejercicio_3_2():
    print("\n----- Ejecutando Ejercicio 3 -----")

    angulos_prueba = (45 , 90 , -30 , 15)
    configuracion_robot = {" velocidad ": 50 ," torque_max ": 120 ," herramienta ": " pinza "
    }

    def calibrar_robot(*args, **kwargs):
        ang_total = 0
        artic_mov = 0

        for angulo in args:
            ang_total += angulo
            artic_mov += 1
        
        print(f"Hay {artic_mov} articulaciones moviéndose {ang_total} grados.")

        for nombre, datos in kwargs.items():
            if nombre == "torque_max" and datos > 100:
                print("Peligro de sobrecarga.")
            
            print(f"Las configuraciones recibidas son: ({nombre}: {datos})")

        return
    
    calibrar_robot(*angulos_prueba, **configuracion_robot)

#LABORATORIO 3

def ejercicio_1_3():
    print("\n----- Ejecutando Ejercicio 1 -----")

    numero = int(input("Ingrese la cantidad de coeficientes (se recomienda entre 6 y 12):"))
    lista = []

    if numero <= 0:
        print("Su numero debe ser entero positivo.")
    else:
        a = 0
        b = 1

        for _ in range(numero):
            lista.append(a)
            x = a + b #Temporal
            a = b #Término base
            b = x #Siguiente término
    
    radios = [r for r in lista if r > 0]
    xc, yc = 0, 0
    angulo = 0

    for i in range(len(radios)):
        r = radios[i]

        theta  = np.linspace(angulo, angulo + np.pi/2, 100)
        x_arco = xc + r * np.cos(theta)
        y_arco = yc + r * np.sin(theta)

        plt.plot(x_arco, y_arco, "b-", linewidth = 2)

        if i < len(radios) - 1:
            r_next = radios[i + 1]
            angulo_final = angulo + np.pi/2

            xc = xc + (r - r_next) * np.cos(angulo_final)
            yc = yc + (r - r_next) * np.sin(angulo_final)

        angulo += np.pi/2

    plt.axis("equal")
    plt.title("Espiral de Fibonacci")
    plt.show()


def ejercicio_2_3():
    print("\n----- Ejecutando Ejercicio 2 -----")

    encuesta = {"Python": 45 , "C++": 28 , "C": 15 , "Java": 12 , "Rust": 8}

    lenguajes = list(encuesta.keys())
    votos = list(encuesta.values())

    colores_representativos = ['#FFD43B', "#0D426B", '#A8B9CC', "#980e0e", '#DEA584']
    
    plt.bar(lenguajes, votos, color = colores_representativos)
    plt.title("Encuesta de Lenguajes de Programación")
    plt.xlabel("Lenguajes de Programación")
    plt.ylabel("Cantidad de Votos")
    plt.show()


def ejercicio_3_3():
    print("\n----- Ejecutando Ejercicio 3 -----")

    N = 100
    matriz1 = [[random.random() for _ in range(N)] for _ in range(N)]
    matriz2 = [[random.random() for _ in range(N)] for _ in range(N)]
    matriz_g = [[0.0 for _ in range(N)] for _ in range(N)]

    A_np = np.array(matriz1)
    B_np = np.array(matriz2)

    inicio_p = time.time()
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                matriz_g[i][j] += matriz1[i][k] * matriz2[k][j]
                
    fin_p = time.time()
    tiempo_p = fin_p - inicio_p

    inicio_np = time.time()
    
    matriz_gNP = A_np @ B_np
    
    fin_np = time.time()
    tiempo_np = fin_np - inicio_np

    print(f"Tiempo Python Puro: {tiempo_p:.4f} segundos")
    print(f"Tiempo NumPy:  {tiempo_np:.4f} segundos")

    if tiempo_np == 0:
        tiempo_np = 0.0001

    aceleracion = tiempo_p / tiempo_np
    print(f"\nNumPy fue {aceleracion:.2f} veces más rápido.")


def ejercicio_4_3():
    print("\n----- Ejecutando Ejercicio 4 -----")

    N = 5_000_000
    lista_nativa = [random.random() for _ in range(N)]
    arreglo_numpy = np.random.rand(N)

    inicio_nativo = time.time()
    
    lista_cuadrado = [x**2 for x in lista_nativa] 
    
    fin_nativo = time.time()
    tiempo_nativo = fin_nativo - inicio_nativo

    inicio_numpy = time.time()
    
    arreglo_cuadrado = arreglo_numpy ** 2 
    
    fin_numpy = time.time()
    tiempo_numpy = fin_numpy - inicio_numpy

    print(f"Tiempo Python Puro (List Comprehension): {tiempo_nativo:.4f} segundos")
    print(f"Tiempo NumPy (Vectorizado): {tiempo_numpy:.4f} segundos")
    
    if tiempo_numpy == 0: 
        tiempo_numpy = 0.0001
        
    aceleracion = tiempo_nativo / tiempo_numpy
    print(f"\nNumPy es {aceleracion:.2f} veces más rápido")

#LABORATORIO 4

def ejercicio_1_4():
    print("\n----- Ejecutando Ejercicio 1 -----")
    datos_canciones = {"Cancion": ["Buenaventura y Caney", "La Bomba", "Sopa de Caracol", "El Cuarto de Tula"], "Artista": ["Andres Cepeda", "Azul Azul", "Banda Blanca", "Buena Vista Social Club"], "Duracion_seg": [371, 123, 293, 445]}
    canciones = pd.DataFrame(datos_canciones)
    
    print("Propiedades estructurales del DataFrame:")
    print(canciones.shape)
    print("Tipos de datos de columnas:")
    print(canciones.dtypes)


def ejercicio_2_4():
    print("\n----- Ejecutando Ejercicio 2 -----")
    datos_juegos = {"Juego": ["Cyberpunk 2077", "Minecraft", "Hollow Knight", "FIFA24"] ,"Precio_Base": [40000 , 15000 , 7500 , 45000] ,"Descuento_Porcentaje": [50 , 0 , 20 , 10]}
    datos = pd.DataFrame(datos_juegos)

    datos["Precio_Final"] = datos["Precio_Base"] - datos["Precio_Base"] * (datos["Descuento_Porcentaje"] / 100)
    juegos_oferta = datos[datos["Precio_Final"] < 20000]

    print(juegos_oferta)


def ejercicio_3_4():
    print("\n----- Ejecutando Ejercicio 3 -----")
    notas = pd.read_csv("notas_alumnos.csv")
    notas_limpias = notas.dropna()

    notas_limpias["Promedio"] = (notas_limpias["Parcial_1"] + notas_limpias["Parcial_2"]) / 2

    print("El DataFrame resultante es:")
    print(notas_limpias)


def ejercicio_4_4():
    print("\n----- Ejecutando Ejercicio 4 -----")
    reg_ventas = pd.read_csv("ventas_tienda.csv")

    plt.plot(reg_ventas["Mes"], reg_ventas["Laptops"], color = "r", label = "Laptops")
    plt.plot(reg_ventas["Mes"], reg_ventas["Smartphones"], color = "b", label = "Smartphones")
    plt.title("Registro Mensual de Ventas")
    plt.ylabel("Ventas")
    plt.xlabel("Mes")
    plt.legend()
    plt.grid(True)
    plt.show()

#LABORATORIO 5

def ejercicio_1_5():
    print("\n----- Ejecutando Ejercicio 1 -----")

    def procesar_trama(trama):
        try:
            partes = trama.split(':')

            id_sensor = partes[0].strip()
            valor = float(partes[1].strip())
        
            print(f"[ÉXITO] Sensor: {id_sensor} | Valor: {valor}")
            return id_sensor, valor

        except IndexError:
            print(f"[ERROR] Trama incompleta. Falta el delimitador ':'. Trama recibida: '{trama}'")
        
        except ValueError:
            print(f"[ERROR] Dato corrupto. El valor no es un número. Trama recibida: '{trama}'")
        
        except Exception as e:
            print(f"[ERROR CRÍTICO] Falla técnica no prevista: {e}")

    print("--- Iniciando Pruebas de Telemetría ---")
    procesar_trama("TEMP:25.4")
    procesar_trama("VOLTAJE_BAJO")
    procesar_trama("PRESION:Basura")


def ejercicio_2_5():
    print("\n----- Ejecutando Ejercicio 2 -----")

    def mover_servo(angulo):
        try:
            if not isinstance(angulo, int):
                raise TypeError("ERROR: El ángulo no es un valor entero.")
            
            assert 0 <= angulo <= 180, "ERROR: Ángulo fuera del rango permitido."
            
            print(f"[MECÁNICA] Moviendo servo a {angulo}° de forma segura.")

        finally:
            print("Estado del motor: Standby\n")

    #mover_servo(90)
    #mover_servo(200)
    #mover_servo("90")
    #mover_servo(45.5)


def ejercicio_3_5():
    print("\n----- Ejecutando Ejercicio 3 -----")

    sensores = {"temp": [22.5, 23.1, 22.8], "presion": [1013, 1015],"humedad": []}

    try:
        nombre = input("Ingrese un sensor a analizar:")
        datos_sensor = sensores[nombre]

        prom = sum(datos_sensor) / len(datos_sensor)
        print(f"[ÉXITO] El promedio del sensor '{nombre}' es: {prom:.2f}")

    except KeyError:
        print("ERROR: Ese sensor no existe en el diccionario.")

    except ZeroDivisionError:
        print("ERROR: La lista del sensor esta vacía.")

    finally:
        print("Consulta de sensor finalizada.")


def ejercicio_4_5():
    print("\n----- Ejecutando Ejercicio 4 -----")


def menu_lab1():
    while True:
        print("\n----- MENÚ DE LABORATORIO 1 -----")
        print("1. Ejecutar Ejercicio 1 / Ley de Ohm y Alerta de Potencia")
        print("2. Ejecutar Ejercicio 2 / Descarga de un Banco de Baterías")
        print("3. Ejecutar Ejercicio 3 / Menú de Conversión de Unidades")
        print("4. Ejecutar Ejercicio 4 / DESAFÍO: Monitoreo de Temperatura Datacenter")
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
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")


def menu_lab2():
    while True:
        print("\n----- MENÚ DE LABORATORIO 2 -----")
        print("1. Ejecutar Ejercicio 1 / Gestión de Nodos de Control")
        print("2. Ejecutar Ejercicio 2 / Geometría de Zonas de Análisis")
        print("3. Ejecutar Ejercicio 3 / Calibración de Brazo Robótico")
        print("0. Volver atrás")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1_2()
        elif opcion == "2":
            ejercicio_2_2()
        elif opcion == "3":
            ejercicio_3_2()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")


def menu_lab3():
    while True:
        print("\n----- MENÚ DE LABORATORIO 3 -----")
        print("1. Ejecutar Ejercicio 1 / Espiral de Fibonacci")
        print("2. Ejecutar Ejercicio 2 / Encuesta de Lenguajes de Programación")
        print("3. Ejecutar Ejercicio 3 / Multiplicación de Matrices")
        print("4. Ejecutar Ejercicio 4 / Benchmark de Rendimiento: Operaciones Vectorizadas")
        print("0. Volver atrás")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1_3()
        elif opcion == "2":
            ejercicio_2_3()
        elif opcion == "3":
            ejercicio_3_3()
        elif opcion == "4":
            ejercicio_4_3()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")


def menu_lab4():
    while True:
        print("\n----- MENÚ DE LABORATORIO 4 -----")
        print("1. Ejecutar Ejercicio 1 / Gestor de Playlist Musical")
        print("2. Ejecutar Ejercicio 2 / Tienda de Videojuegos: Operaciones y Filtros")
        print("3. Ejecutar Ejercicio 3 / Registro de Notas: Limpieza de CSV")
        print("4. Ejecutar Ejercicio 4 / Ventas Mensuales: Visualización con Matplotlib")
        print("0. Volver atrás")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1_4()
        elif opcion == "2":
            ejercicio_2_4()
        elif opcion == "3":
            ejercicio_3_4()
        elif opcion == "4":
            ejercicio_4_4()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")


def menu_lab5():
    while True:
        print("\n----- MENÚ DE LABORATORIO 5 -----")
        print("1. Ejecutar Ejercicio 1 / Sistema de Telemetría: Parsing de Trama")
        print("2. Ejecutar Ejercicio 2 / Control de Brazo Robótico: Validaciones Físicas")
        print("3. Ejecutar Ejercicio 3 / Sistema de Monitoreo: Diccionarios y Divisiones")
        print("4. Ejecutar Ejercicio 4 / ")
        print("0. Volver atrás")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1_5()
        elif opcion == "2":
            ejercicio_2_5()
        elif opcion == "3":
            ejercicio_3_5()
        elif opcion == "4":
            ejercicio_4_5()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")


def menu_principal():
    while True:
        print("\n===== MENÚ DE LABORATORIOS =====")
        print("1. Ir a Laboratorio 1")
        print("2. Ir a Laboratorio 2")
        print("3. Ir a Laboratorio 3")
        print("4. Ir a Laboratorio 4")
        print("5. Ir a Laboratorio 5")
        print("0. Salir del programa")

        guia = input("Selecciona un laboratorio: ")

        if guia == "1":
            menu_lab1()
        elif guia == "2":
            menu_lab2()
        elif guia == "3":
            menu_lab3()
        elif guia == "4":
            menu_lab4()
        elif guia == "5":
            menu_lab5()
        elif guia == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()