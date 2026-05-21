# menú interactivo utilizando un ciclo while y múltiples sentencias elif que permita 
# al usuario realizar conversiones rápidas de unidades utilizadas en electrónica.

while True:
    #Menú:
    print("|| Menú de Conversión de Unidades: ||")
    print("-------------------------------------")
    print(f"1. Convertir miliamperios (mA) a amperios (A).")
    print(f"2. Convertir microfaradios (µF) a faradios (F).")
    print(f"3. Convertir kiloohmios (kΩ) a ohmios (Ω).")
    print(f"4. Salir")

    opcion = int(input("Eliga unas de las opciones que aparecen: "))

    if opcion == 1:
        ma = float(input("Ingrese el valor en mA: "))
        print(f"--> {ma} equivalen a {ma / 1000} A")

    elif opcion == 2:
        uf = float(input("Ingrese el valor en uF: "))
        print(f"--> {uf} equivalen a {uf*1e-6} (F).")

    elif opcion == 3:
        kohm = float(input("Ingrese el valor en kOhm: "))
        print(f"--> {kohm} equivalen a {kohm*1e3} (ohmios).")

    elif opcion == 4:
        print(f"Saliendo del programa...")

        break #Termina el ciclo y sale del menú

    else:
        print("Opción no válida. Por favor, ingresa un número entre 1 y 4.")