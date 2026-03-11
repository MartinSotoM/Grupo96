def ejercicio_1():
    print("\n--- Ejecutando Ejercicio 1 ---")

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


def ejercicio_2():
    print("\n--- Ejecutando Ejercicio 2 ---")

    numero = int(input("Ingresa el número a calcular: "))

    if numero <= 0:
        print("Su número debe ser entero positivo.")
    else:
        x = 1 #Resultado Temporal
        for i in range(1, numero + 1):
            x = x*i #Mult factorial
            print(f"Factorial de {i} es {x}")


def ejercicio_3():
    print("\n--- Ejecutando Ejercicio 3 ---")

    numero = int(input("Ingresa el número a calcular: "))

    while numero <= 0:
        print("Su número debe ser entero positivo.")
        numero = int(input("Ingrese un número válido: "))

        x = 1 #Resultado Temporal
        for i in range(1, numero + 1):
            x = x*i #Mult factorial
            print(f"Factorial de {i} es {x}")


def ejercicio_4():
    print("\n--- Ejecutando Ejercicio 4 ---")

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



def menu():
    while True:
        print("\n--- MENÚ DE EJERCICIOS ---")
        print("1. Ejecutar Ejercicio 1")
        print("2. Ejecutar Ejercicio 2")
        print("3. Ejecutar Ejercicio 3")
        print("4. Ejecutar Ejercicio 4")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, vuelve a intentarlo.")

if __name__ == "__main__":
    menu()
