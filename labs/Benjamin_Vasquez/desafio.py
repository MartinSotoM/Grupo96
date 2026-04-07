print('monitoreao de temperatura')
while True:
    temp = int(input('ingrese la temperatura: '))
    if 20<temp <= 45:
        print("Estado normal")
    elif 45< temp <= 75:
        print("Advertencia: Encendiendo ventiladores auxiliares")
    elif temp > 75:
        print("¡Peligro Crítico! Apagando servidor de emergencia")
        break
