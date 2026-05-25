# Ejercicio 3: Abstracción y Polimorfismo – Actuadores Industriales

from abc import ABC, abstractmethod

# En este ejercicio, se define un contrato abstracto para motores y se demuestra polimorfismo

# 1. Clase abstracta: define la interfaz obligatoria para todo motor
class Motor(ABC):
    def __init__(self, id_motor):
        self.id_motor = id_motor

    @abstractmethod
    def accionar(self):
        pass  # cada subclase DEBE implementar su propio comportamiento

# 2. Implementaciones concretas con movimiento específico de cada tipo
class MotorPasoAPaso(Motor):
    def accionar(self):
        print(f"  [{self.id_motor}] Motor paso a paso: girando en pasos de 1.8°")

class Servomotor(Motor):
    def accionar(self):
        print(f"  [{self.id_motor}] Servomotor: posicionando eje a 90°")

# 3. Lista de producción: polimorfismo en acción
if __name__ == "__main__":
    linea_produccion = [
        MotorPasoAPaso("NEMA-17"),
        Servomotor("SG90"),
    ]

    print("Iniciando secuencia de control:")
    for actuador in linea_produccion:
        actuador.accionar()  # misma llamada, comportamiento distinto según tipo real