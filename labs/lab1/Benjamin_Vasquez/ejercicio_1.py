Voltaje = int(input("Ingrese el voltaje: "))
corriente = int(input("Ingrese la corriente: "))

R = Voltaje / corriente
P = Voltaje * corriente

print("La resistencia es: ", R)

if P > 1000:
    print("La potencia es: ", P)
    print("¡Peligro! Alta disipación de potencia detectada.")
elif P <= 1000:
    print("La potencia es: ", P)
    print("Operación en rangos seguros..")   