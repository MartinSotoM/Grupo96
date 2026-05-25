# Ejercicio 2: Herencia y Métodos – Instrumentación de Laboratorio

# En este ejercicio, se modela una jerarquía de instrumentos con herencia y métodos estáticos

# 1. Clase padre con atributos base y método estático de validación
class Instrumento:
    def __init__(self, marca):
        self.marca = marca
        self.estado = "Apagado"  # estado inicial seguro por defecto

    def encender(self):
        self.estado = "Encendido"
        print(f"  [{self.marca}] Equipo encendido")

    # 2. Método estático: no necesita self, es una utilidad de la clase
    @staticmethod
    def validar_voltaje(voltaje):
        return voltaje <= 220  # True si es seguro, False si hay riesgo de sobrecarga

# 3. Clase hija que extiende Instrumento con atributos propios del osciloscopio
class Osciloscopio(Instrumento):
    def __init__(self, marca, canales):
        super().__init__(marca)  # inicializa marca y estado desde el padre
        self.canales = canales

    # 4. Método propio: solo opera si el equipo está encendido
    def medir_senal(self):
        if self.estado == "Encendido":
            print(f"  [{self.marca}] Midiendo señal en {self.canales} canales...")
        else:
            print(f"  [{self.marca}] Error: equipo apagado, no se puede medir")

if __name__ == "__main__":
    voltaje_red = 300
    print(f"¿Voltaje {voltaje_red}V seguro?: {Instrumento.validar_voltaje(voltaje_red)}")

    osciloscopio_lab = Osciloscopio("Tektronix", 4)
    osciloscopio_lab.medir_senal()   # intento sin encender
    osciloscopio_lab.encender()
    osciloscopio_lab.medir_senal()