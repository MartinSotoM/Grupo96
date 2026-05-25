# Ejercicio 2 – Polimorfismo: Tipos de Sensores

# En un laboratorio tienes distintos sensores. Todos sirven para medir, pero cada
# uno entrega resultados diferentes. El polimorfismo permite usar la misma orden
# medir() para todos, sin importar qué tipo de sensor sea.

# 1. Clase padre Sensor con método base
class Sensor:
    def medir(self):
        print("Midiendo datos base...")

# 2. Clase hija SensorTemperatura: sobreescribe medir()
class SensorTemperatura(Sensor):
    def medir(self):
        print("Midiendo temperatura en grados Celsius")

# 3. Clase hija SensorLuz: también sobreescribe medir()
class SensorLuz(Sensor):
    def medir(self):
        print("Midiendo nivel de luz en Lux")

# 4. Función externa que llama medir() sin importar qué tipo de sensor reciba
def iniciar_medicion(sensor_cualquiera):
    sensor_cualquiera.medir()   # polimorfismo: cada objeto ejecuta su propia versión


# --- Prueba ---
sensor_temp     = SensorTemperatura()
sensor_luz      = SensorLuz()
sensor_generico = Sensor()          # también probamos la clase base

print("--- Prueba 1 ---")
iniciar_medicion(sensor_temp)       # → Midiendo temperatura en grados Celsius

print("\n--- Prueba 2 ---")
iniciar_medicion(sensor_luz)        # → Midiendo nivel de luz en Lux

print("\n--- Prueba 3 (Sensor Base) ---")
iniciar_medicion(sensor_generico)   # → Midiendo datos base...