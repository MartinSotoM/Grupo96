from abc import ABC, abstractmethod

# Ejercicio 3 – Abstracción: Plantilla para Motores

# En una fábrica hay diferentes tipos de motores. Todos deben poder moverse,
# pero mecánicamente lo hacen de forma distinta. La clase abstracta Motor actúa
# como plantilla obligatoria: si una clase hija no implementa moverse(), el programa da error.

# 2. Clase abstracta Motor: define la interfaz sin implementación concreta
class Motor(ABC):
    @abstractmethod
    def moverse(self):
        pass    # @abstractmethod impide instanciar Motor directamente

# 3. Clases concretas que heredan de Motor e implementan su versión de moverse()
class MotorPasoAPaso(Motor):
    def moverse(self):
        print("Moviendo por pasos...")

class Servomotor(Motor):
    def moverse(self):
        print("Moviendo a un ángulo exacto...")

# 4. Lista con ambos motores: el for llama moverse() polimórficamente en cada uno
lista_motores = [MotorPasoAPaso(), Servomotor()]

for motor in lista_motores:
    motor.moverse()