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

    fact = int(input("Ingresa el número a calcular: "))

    if fact <= 0:
        print("Su número debe ser entero positivo.")
    else:
        c = 1 #Resultado Temporal
        for j in range(1, fact + 1):
            c = c*j #Mult factorial
            print(f"Factorial de {j} es {c}")


def menu():
    while True:
        print("\n--- MENÚ DE EJERCICIOS ---")
        print("1. Ejecutar Ejercicio 1")
        print("2. Ejecutar Ejercicio 2")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, vuelve a intentarlo.")

if __name__ == "__main__":
    menu()
