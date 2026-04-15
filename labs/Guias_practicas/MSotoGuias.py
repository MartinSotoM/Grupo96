import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import sys

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


def ejercicio_5_1():
    print("\n----- [AVISO] El Ejercicio 5 utiliza una herramienta de terminal independiente  -----")

    parser = argparse.ArgumentParser(description = "Calculadora Resistencias Equivalentes")
    parser.add_argument("--tipo", type = str, required = True, choices = ["serie", "paralelo"], help = "Indica el tipo de conexión")
    parser.add_argument("--resistencias", type = float, nargs = "+", required = True, help = "Valores de las resistencias")
    args = parser.parse_args()

    for r in args.resistencias:
        if r <= 0:
            print("ERROR: todos los valores de resistencia deben ser mayores a 0.")
            sys.exit(1)
    
    if args.tipo == "serie":
        resis_total_s = sum(args.resistencias)
        print(f"La resistencia equivalente en serie es de: {resis_total_s:.2f} Ohms.")
    elif args.tipo == "paralelo":
        resis_total_p = 1 / sum(1/r for r in args.resistencias)
        print(f"La resistencia equivalente en paralelo es de: {resis_total_p:.2f} Ohms.")

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
    print("\n----- Ejecutando Ejercicio 3 -----")

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
    print(f"La potencia trifásica total de la instalación es: {pot_trif_total:.2f}[W]. \nLa carga con mayor potencia es: {carga_mayor_pot}. \nLas cargas con factor de potencia menor a 0.80 son: {lista_cargas_menores}")


def ejercicio_4_2():
    print("\n----- Ejecutando Ejercicio 4 -----")

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
    
    def evaluar_varias_estaciones(**kwargs):
        reporte_red = {}

        for nombre_est2, datos_est in kwargs.items():
            nom, est, lista_f = evaluar_estacion(nombre_est2, datos_est)

            reporte_red[nom] = {"estado": est, "fallas": lista_f}

        return reporte_red
    
    def generar_reporte(resumen):
        estaciones_evaluadas = list(resumen.keys())
        cantidad_criticas = 0
        max_fallas = -1
        peor_estacion = ""

        for nombre, info, in resumen.items():
            if info["estado"] == "Crítico":
                cantidad_criticas += 1

            num_fallas_actual = len(info["fallas"])
            if num_fallas_actual > max_fallas:
                max_fallas = num_fallas_actual
                peor_estacion = nombre

        return estaciones_evaluadas, cantidad_criticas, peor_estacion
    
    diccionario_resumen = evaluar_varias_estaciones(**estaciones)
    lista_estados, total_criticas, est_peor = generar_reporte(diccionario_resumen)

    print(f"Estaciones evaluadas: {lista_estados} \nTotal en estado crítico: {total_criticas} \nEstación con más fallas: {est_peor}")

# ====== Guía Práctica 3 ======

def ejercicio_1_3():
    print("\n----- Ejecutando Ejercicio 1 -----")

    t = np.linspace(0, 10, 500)
    matriz_mov = np.array([2 * np.sin(t), 2 * np.cos(t), 0.5 * t])

    x = matriz_mov[0, :]
    y = matriz_mov[1, :]
    z = matriz_mov[2, :]

    plt.subplot(3, 1, 1)
    plt.plot(t, x, color = "r")
    plt.title("Gráfico Coordenadas X")

    plt.subplot(3, 1, 2)
    plt.plot(t, y, color = "b")
    plt.title("Gráfico Coordenadas Y")

    plt.subplot(3, 1, 3)
    plt.plot(t, z, color = "g")
    plt.title("Gráfico Coordenadas Z")

    plt.show()


def ejercicio_2_3():
    print("\n----- Ejecutando Ejercicio 2 -----")

    t = np.linspace(0, 0.2, 1000)
    m = np.cos(2 * np.pi * 5 * t)
    c = np.sin(2 * np.pi * 100 * t)

    s = (1 + 0.8 * m) * c

    plt.plot(t, m, color = "b", linestyle = "--", label = "Señal Moduladora m(t)")
    plt.plot(t, s, color = "r", label = "Señal Modulada s(t)")
    plt.legend(loc = "upper right")
    plt.title("Superposición Señales")

    plt.show()


def ejercicio_3_3():
    print("\n----- Ejecutando Ejercicio 3 -----")

    t = np.linspace(0, 0.06, 100)
    faseA = 311 * np.sin(2 * np.pi * 50 * t)
    faseB = 311 * np.sin(2 * np.pi * 50 * t - (2 * np.pi / 3))
    faseC = 311 * np.sin(2 * np.pi * 50 * t + (2 * np.pi / 3))

    plt.subplot(1, 2, 1)
    plt.plot(t, faseA, color = "r", label = "Fase A")
    plt.plot(t, faseB, color = "b", label = "Fase B")
    plt.plot(t, faseC, color = "g", label = "Fase C")
    plt.legend(loc = "upper left")
    plt.title("Gráfica de las Tres Fases Superpuestas")

    plt.subplot(1, 2, 2)
    plt.plot(t, faseA + faseB + faseC)
    plt.ylim(-50, 50)
    plt.title("Gráfica de la Suma de las Tres Fases")

    plt.show()


def ejercicio_4_3():
    print("\n----- Ejecutando Ejercicio 4 -----")

    t = np.linspace(0, 2, 800)
    v_ideal = 3.3 * (1 - np.exp(-2 * t))
    ruido = np.random.normal(0, 0.2, len(t))
    s_medida = v_ideal + ruido

    plt.plot(t, s_medida, color = "grey", label = "Señal Ruidosa")
    plt.plot(t, v_ideal, color = "r", label = "Señal Ideal")
    plt.legend(loc = "lower right")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Voltaje [V]")

    plt.show()

# ====== Guía Práctica 4 ======

def ejercicio_1_4():
    print("\n----- Ejecutando Ejercicio 1 -----")

    sensor = pd.read_csv("sensor_datos.csv")
    sensor = sensor.dropna()
    sensor["Potencia_W"] = sensor["voltaje"] * sensor["corriente"]
    sensor["Alerta_Humedad"] = sensor["humedad"] > 70

    plt.plot(sensor["fecha"], sensor["Potencia_W"], label = "Potencia_W", color = "b")
    plt.plot(sensor["fecha"], sensor["temperatura"], label = "Temperatura", color = "r")
    plt.grid(True)
    plt.xticks(rotation = 90)
    plt.show()


def ejercicio_2_4():
    print("\n----- Ejecutando Ejercicio 2 -----")

    sensor = pd.read_csv("calidad_aire.csv")
    print("Los parámetros del archivo son:")
    print(sensor.shape)
    print(sensor.dtypes)
    print(sensor.describe())

    media_T = np.mean(sensor["temperatura"])
    print(f"\nLa media (con el comando mean) de la temperatura es: {media_T:.5f}")

    sensor_filtrado = sensor[sensor["pm25"] > 35]

    sensor.to_csv("alerta_aire.csv", index = False, sep = ";", encoding = "utf-8")


def ejercicio_3_4():
    print("\n----- Ejecutando Ejercicio 3 -----")

    consumo = pd.read_csv("consumo_energia.csv")
    print(consumo.iloc[4:15, :])

    corr_consumo_costo = consumo["consumo_kwh"].corr(consumo["costo_clp"])
    print(f"\nLa correlación entre el consumo y el costo es: {corr_consumo_costo:.2f}, lo que no tiene sentido, ya que al consumir más energía el costo debería ser mayor y así cumplir con una correlación cercana al 1, en nuestro caso los valores son arbitrarios, por momentos con un consumo mayor el costo es menor que al consumir menos energía.")

    prom_consumo = np.mean(consumo["consumo_kwh"])

    dias_ahorro = consumo[consumo["consumo_kwh"] < prom_consumo]
    dias_ahorro.to_json("ahorro_energetico.json", orient = "records", force_ascii = False)

    plt.plot(consumo["fecha"], consumo["consumo_kwh"], color = "g", marker = "x")
    plt.title("Evolución del Consumo Energético")
    plt.xlabel("Fecha")
    plt.ylabel("Consumo (kWh)")
    plt.xticks(rotation = 90)
    plt.show()


def ejercicio_4_4():
    print("\n----- Ejecutando Ejercicio 4 -----")

    motor = pd.read_csv("motor_dc.csv")
    motor = motor.drop_duplicates()

    prom_temperatura = motor["temperatura_motor"].mean()
    motor["temperatura_motor"] = motor["temperatura_motor"].fillna(prom_temperatura)

    corriente_nominal = motor["corriente_a"].mean()
    motor_fallas = motor[(motor["velocidad_rpm"] < 100) & (motor["corriente_a"] > corriente_nominal)]
    print(f"Las posibles fallas del motor son: {motor_fallas}")

    plt.plot(motor["tiempo_s"], motor["temperatura_motor"])
    plt.title("Temperatura del Motor DC")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Temperatura (°C)")
    plt.tight_layout()
    plt.show()

# ====== Guía Práctica 5 ======

def ejercicio_1_5():
    print("\n----- Ejecutando Ejercicio 5 -----")

    def limpiar_datos(lecturas):
        datos = []

        for dato in lecturas:
            try:
                flotante = float(dato)
                datos.append(flotante)

            except (ValueError, TypeError):
                print(f"Error al convertir: {dato} / Entrada inválida")

        if len(datos) > 0:
            promedio = np.mean(datos)
        else:
            promedio = 0.0
            
        return promedio

    lista_prueba = [22.5, "23.1", "Error", None, 21.8, " "]

    limpieza = limpiar_datos(lista_prueba)
    print(f"\nEl promedio de las temperaturas válidas es: {limpieza:.2f}")


def ejercicio_2_5():
    print("\n----- Ejecutando Ejercicio 2 -----")
    
    def calcular_eficiencia(p_salida, p_entrada):
        assert p_salida >= 0 and p_entrada >= 0, "Las potencias no pueden ser negativas"

        try: 
            eficiencia = (p_salida / p_entrada) * 100
            return f"{eficiencia:.2f}%"
        
        except ZeroDivisionError:
            print("Error: Motor apagado o sin consumo")

    prueba = [(150, 200), (100, 0), (-50, 100)]

    for salida, entrada in prueba:
        print(f"\nTesteando motor -> Salida: {salida}W | Entrada: {entrada}W")

        try:
            resultado = calcular_eficiencia(salida, entrada)
            print(f"Resultado: {resultado}")

        except AssertionError as error_capturado:
            print(f"Alerta de Sistema: {error_capturado}")
        

def ejercicio_3_5():
    print("\n----- Ejecutando Ejercicio 3 -----")
    calibracion = {"temp": [1.02, 0.98, 1.04, 1.01], "hum": [1.05, 0.99, 1.02], "presion": [1.0, 0.99, 1.01, 0.98]}

    sensor = input("Ingresa el nombre del sensor a consultar:")
    fc = int(input("Ingresa el factor de calibración a revisar:"))


def ejercicio_4_5():
    print("\n----- Ejecutando Ejercicio 4 -----")

# ====== Guía Práctica 6 ======

def ejercicio_1_6():
    print("\n----- Ejecutando Ejercicio 1 -----")

    class Instrumento:
        unidad_estandar = "SI"

        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        @staticmethod
        def convertir_a_base(valor_mili):
            return valor_mili / 1000
        
    class Osciloscopio(Instrumento):
        def __init__(self, marca, modelo):
            super().__init__(marca, modelo)

            self.v_div = 1.0

        def actualizar_v_div(self, nuevo_v_div):
            self.v_div = nuevo_v_div
            
        def imprimir_config(self):
            print(f"Configuración Actual: {self.marca} | {self.modelo} | {self.v_div} |{self.unidad_estandar}")

    mi_osciloscopio = Osciloscopio("Tektronix", "TBS1052B")
    mi_osciloscopio.imprimir_config()
    mi_osciloscopio.actualizar_v_div(5.0)
    print("\n[ACTUALIZANDO PARÁMETROS]")
    mi_osciloscopio.imprimir_config()

    lectura_mili = 500
    lectura_base = Osciloscopio.convertir_a_base(lectura_mili)
    print(f"\n[CONVERSIÓN] Lectura de {lectura_mili}[mV] convertida a base: {lectura_base} [V]")


def ejercicio_2_6():
    print("\n----- Ejecutando Ejercicio 2 -----")


def ejercicio_3_6():
    print("\n----- Ejecutando Ejercicio 3 -----")


def ejercicio_4_6():
    print("\n----- Ejecutando Ejercicio 4 -----")


def menu_guia_1():
    while True:
        print("\n----- MENÚ DE GUÍA 1 -----")
        print("1. Ejecutar Ejercicio 1 / Serie de Fibonacci")
        print("2. Ejecutar Ejercicio 2 / Serie de Factoriales")
        print("3. Ejecutar Ejercicio 3 / Validación de Entrada")
        print("4. Ejecutar Ejercicio 4 / Cálculo de Resistencia Total en Serie o en Paralelo")
        print("5. Ejecutar Ejercicio 5 / DESAFIO !!")
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
        elif opcion == "5":
            ejercicio_5_1()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")


def menu_guia_2():
    while True:
        print("\n----- MENÚ DE GUÍA 2 -----")
        print("1. Ejecutar Ejercicio 1 / Análisis de Mediciones de Sensores Eléctricos")
        print("2. Ejecutar Ejercicio 2 / Registro de Dispositivos en una Red de Telecomunicaciones")
        print("3. Ejecutar Ejercicio 3 / Cálculo de Potencia en Cargas Trifásicas")
        print("4. Ejecutar Ejercicio 4 / Sistema de Monitoreo de Estaciones Remotas")
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
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")


def menu_guia_3():
    while True:
        print("\n----- MENÚ DE GUÍA 3 -----")
        print("1. Ejecutar Ejercicio 1 / Análisis de Señales de Sensores en un Brazo Robótico")
        print("2. Ejecutar Ejercicio 2 / Modulación de Amplitud (AM) en Telecomunicaciones")
        print("3. Ejecutar Ejercicio 3 / Análisis de un Sistema Eléctrico Trifásico")
        print("4. Ejecutar Ejercicio 4 / Filtrado de Ruido en una Señal Electrónica")
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


def menu_guia_4():
    while True:
        print("\n----- MENÚ DE GUÍA 4 -----")
        print("1. Ejecutar Ejercicio 1 / Sensor Ambiental - Limpieza y Transformación")
        print("2. Ejecutar Ejercicio 2 / Calidad del Aire - Estadísticas y Resumen")
        print("3. Ejecutar Ejercicio 3 / Consumo Energético - Correlación y Slicing")
        print("4. Ejecutar Ejercicio 4 / Motor DC - Detección de Anomalías")
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


def menu_guia_5():
    while True:
        print("\n----- MENÚ DE GUÍA 5 -----")
        print("1. Ejecutar Ejercicio 1 / Estación Meteorológica - Validación de Datos Seriales")
        print("2. Ejecutar Ejercicio 2 / Control de Motores - Operaciones Críticas y Aserciones")
        print("3. Ejecutar Ejercicio 3 / Calibración de Sensores - Accesos seguros y Gráficos")
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


def menu_guia_6():
    while True:
        print("\n----- MENÚ DE GUÍA 6 -----")
        print("1. Ejecutar Ejercicio 1 / Instrumentación Electrónica - El Laboratorio de Medición")
        print("2. Ejecutar Ejercicio 2 / ")
        print("3. Ejecutar Ejercicio 3 / ")
        print("4. Ejecutar Ejercicio 4 / ")
        print("0. Volver atrás")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1_6()
        elif opcion == "2":
            ejercicio_2_6()
        elif opcion == "3":
            ejercicio_3_6()
        elif opcion == "4":
            ejercicio_4_6()
        elif opcion == "0":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")


def menu_principal():
    while True:
        print("\n===== MENÚ DE GUÍAS PRÁCTICAS =====")
        print("1. Ir a Guía 1")
        print("2. Ir a Guía 2")
        print("3. Ir a Guía 3")
        print("4. Ir a Guía 4")
        print("5. Ir a Guía 5")
        print("6. Ir a Guía 6")
        print("0. Salir del programa")

        guia = input("Selecciona una guía: ")

        if guia == "1":
            menu_guia_1()
        elif guia == "2":
            menu_guia_2()
        elif guia == "3":
            menu_guia_3()
        elif guia == "4":
            menu_guia_4()
        elif guia == "5":
            menu_guia_5()
        elif guia == "6":
            menu_guia_6()
        elif guia == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()