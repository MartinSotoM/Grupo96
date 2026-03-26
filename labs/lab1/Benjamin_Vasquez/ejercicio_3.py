while True:
    print('menu intecactivo eliga una de estas 4 opciones:')
    print('1. Convertir miliamperios (mA) a amperios (A)')
    print('2. Convertir microfaradios (μF) a faradios (F)')
    print('3. Convertir kiloohmios (kΩ) a ohmios (Ω)')
    print('4. Salir')
    opcion = input('Ingrese el número de la opción deseada: ')
    if opcion == '1':
        miliamperios = float(input('Ingrese el valor en miliamperios (mA): '))
        amperios = miliamperios / 1000
        print(f'{miliamperios} mA son equivalentes a {amperios} A.')
        
    elif opcion == '2':
        microfaradios = float(input('Ingrese el valor en microfaradios (μF): '))
        faradios = microfaradios / 1e6
        print(f'{microfaradios} μF son equivalentes a {faradios} F.')
        
    elif opcion == '3':
        kiloohmios = float(input('Ingrese el valor en kiloohmios (kΩ): '))
        ohmios = kiloohmios * 1000
        print(f'{kiloohmios} kΩ son equivalentes a {ohmios} Ω.')
        
    elif opcion == '4':
        print('Saliendo del programa. ¡Hasta luego!')
        break
    else:
        print('Opción no válida. Por favor, ingrese un número del 1 al 4.')