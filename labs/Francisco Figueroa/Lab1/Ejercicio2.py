#Ejercicio 2:  Descarga de un Banco de Baterías:
"""
Escribe un programa que simule la caída de voltaje de un banco de baterías 
a lo largo del tiempo utilizando un ciclo while 
"""
#Lo puse con float para poner decimales.
V_inicial = float(input("Ingrese el voltaje inicial del banco de baterías: "))
V_minimo = float(input("Ingrese el voltaje mínimo de operación del banco de baterías: "))

hora= 0 #contador de horas, parte en 0
while V_inicial > V_minimo:
    hora += 1
    V_inicial *= 0.97 #decae un 3%
    
print(f"El banco de baterías logró entregar {hora} horas de energía antes de requerir recarga.")
