import random

from robot_base import RobotBase

# === ROBOT TRES RUEDAS ===
class RobotTresRuedas(RobotBase):
    def __init__(self, nombre, radio_rueda):
        super().__init__(nombre, 20.0)
        self.radio_rueda = radio_rueda
        self.ruedas_calibradas = False

    def calibrar_giro(self):
        print(f"[{self.get_nombre()}] Calibrando triciclo con ruedas de {self.radio_rueda}cm.")
        self.ruedas_calibradas = True

    def mover(self):
        return self.step(v=0.8, w=0.2)

    def limpiar(self):
        self._reducir_bateria(2.0)
        basura = random.uniform(0.5, 1.5)
        self._recolectar_basura(basura)

# === ROBOT ORUGA ===
class RobotOruga(RobotBase):
    def __init__(self, nombre, tension_oruga):
        super().__init__(nombre, 50.0)
        self.tension_oruga = tension_oruga

    def ajustar_tension(self):
        print(f"[{self.get_nombre()}] Ajustando tension de las orugas al {self.tension_oruga}%.")

    def mover(self):
        return self.step(v=0.3, w=0.8)

    def limpiar(self):
        self._reducir_bateria(4.5)
        basura = random.uniform(2.0, 4.0)
        self._recolectar_basura(basura)

# === ROBOT DRON ===
class RobotDron(RobotBase):
    def __init__(self, nombre, altura_maxima):
        super().__init__(nombre, 5.0)
        self.altura_maxima = altura_maxima
        self.en_vuelo = False

    def despegar(self):
        print(f"[{self.get_nombre()}] Despegando hasta {self.altura_maxima} metros de altura.")
        self.en_vuelo = True

    def mover(self):
        if self.en_vuelo:
            return self.step(v=2.5, w=1.0)
        else:
            return (0.0, False)

    def limpiar(self):
        if self.en_vuelo:
            self._reducir_bateria(3.0)
            basura = random.uniform(0.1, 0.4)
            self._recolectar_basura(basura)
