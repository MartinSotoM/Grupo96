# Desafío: Monitoreo de Temperatura en Datacenter

while True:
    try:
        # 1. Solicitar lectura de temperatura
        temperatura = float(input("Ingrese la temperatura actual (en °C): "))

        # 2. Estado normal
        if 20 <= temperatura <= 45:
            print("Estado normal")
        
        # 3. Advertencia
        elif 45 < temperatura <= 75:
            print("Advertencia: Encendiendo ventiladores auxiliares")
        
        # 4. Peligro Crítico
        elif temperatura > 75:
            print("¡Peligro Crítico! Apagando servidor de emergencia")
            break  # Salida inmediata del ciclo
            
        else:
            print("Temperatura fuera de rango operativo (muy baja).")

    except ValueError:
        print("Por favor, ingrese un número válido.")