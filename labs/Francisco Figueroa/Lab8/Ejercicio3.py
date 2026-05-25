# Ejercicio 3 – Repaso de POO: Clases y Encapsulamiento
# Se modela una batería recargable usando POO con encapsulamiento.
# La carga es un atributo privado que solo puede modificarse mediante métodos controlados,
# evitando que código externo asigne valores inválidos como negativos o mayores a 100.

class Bateria:

    def __init__(self, marca):
        self.marca = marca
        self.__carga = 100  # privada: solo accesible desde dentro de la clase

    def usar_bateria(self, gasto):
        # Restar el gasto y asegurar que no baje de 0 (límite físico real)
        self.__carga -= gasto
        if self.__carga <= 0:  # <= cubre el caso exacto de quedar en 0
            self.__carga = 0
            print("¡Batería agotada!")

    def ver_carga(self):
        return self.__carga  # expone el valor sin permitir modificarlo directamente


# ── Prueba del sistema ──
bateria_robot = Bateria("LiPo-Max")

print(f"Carga inicial:         {bateria_robot.ver_carga()} %")

bateria_robot.usar_bateria(40)
print(f"Después de gastar 40%: {bateria_robot.ver_carga()} %")

bateria_robot.usar_bateria(80)  # activa la protección → queda en 0
print(f"Después de gastar 80%: {bateria_robot.ver_carga()} %")