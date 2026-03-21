#voltjajes = [12.6 , 12.4 , 12.3 , 12.1 , 11.9 , 11.8 , 11.6 , 11.4]
import random
voltajes = [ round ( random.uniform ( 10 , 20 ) , 2 ) for _ in range ( 10 ) ]

def analizar_voltajes(voltajes) :
    maximo = max(voltajes)
    minimo = min(voltajes)
    promedio = sum(voltajes)/len(voltajes)
    cantidad_bajos = 0
    for voltajes in voltajes:
        if voltajes < 12:
            cantidad_bajos = cantidad_bajos+1

    return maximo,minimo,promedio,cantidad_bajos
a,b,c,d=analizar_voltajes(voltajes)   

print("voltaje maximo:",a ,"voltaje minimo:",b,"voltaje promedio:",c, "cantidad de voltajes bajos:",d)

def estado_bateria(voltajes):
    promedio = sum(voltajes)/len(voltajes)
    for voltajes in voltajes:
        if promedio >= 12.2:
            estado_bat = "Batería en buen estado"
        if 11.8<promedio<12.9:
            estado_bat = "Batería en descarga" 
        if promedio<11.8:
            estado_bat = "Batería crítica"
    return estado_bat
estado_bat = estado_bateria(voltajes)
print(estado_bat)
