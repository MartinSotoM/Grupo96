# Ejercicio 1: Encapsulamiento y Seguridad – Termostato Inteligente

# En este ejercicio, se implementa encapsulamiento para proteger el estado interno de un termostato

# 1. Clase Termostato con atributo privado de temperatura
class Termostato:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.__temperatura = 20  # privado: evita modificación directa desde afuera

    # 2. Getter: expone el valor sin dar acceso al atributo privado
    def get_temperatura(self):
        return self.__temperatura

    # 3. Setter con validación: actúa como filtro de seguridad del sistema
    def set_temperatura(self, valor):
        if 15 <= valor <= 30:
            self.__temperatura = valor
            print(f"  [{self.ubicacion}] Temperatura ajustada a {self.__temperatura}°C")
        else:
            print(f"  [{self.ubicacion}] Error: {valor}°C fuera del rango seguro (15–30°C)")

# 4. Demostración del encapsulamiento en acción
if __name__ == "__main__":
    termostato_sala = Termostato("Sala de Reuniones")

    print(f"Temperatura inicial:  {termostato_sala.get_temperatura()}°C")
    termostato_sala.set_temperatura(24)   # modificación válida
    termostato_sala.set_temperatura(50)   # valor inválido: bloqueado
    print(f"Temperatura actual:   {termostato_sala.get_temperatura()}°C")