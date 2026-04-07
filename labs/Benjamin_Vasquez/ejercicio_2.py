voltaje = float(input("Ingrese el voltaje actual: "))
voltaje_min = float(input("Ingrese el voltaje mínimo: "))

horas = 0
while 0.97*voltaje > voltaje_min:
    voltaje = voltaje * 0.97
    horas = horas + 1
print("El voltaje se mantendrá por", horas, "horas.") 
print("El voltaje final es de", voltaje, "voltios.")
    
