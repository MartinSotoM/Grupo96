# Ejercicio 1 – Encapsulamiento: Termostato Seguro

# Estás programando un termostato para una casa. Si alguien ingresa una 
# temperatura muy loca (como 100 grados), el aire acondicionado podría romperse. 
# Hay que proteger esa variable.

# 1. Clase Termostato con constructor que recibe el nombre de la habitación
class Termostato:
    def __init__(self, habitacion):
        self.habitacion = habitacion    # atributo público
        self.__temperatura = 20         # 2. atributo PRIVADO, valor inicial 20

    # 3. Getter: devuelve el valor actual de __temperatura
    def ver_temperatura(self):
        return self.__temperatura

    # 4. Setter con validación: solo acepta valores entre 15 y 30
    def cambiar_temperatura(self, nuevo_valor):
        if 15 <= nuevo_valor <= 30:
            self.__temperatura = nuevo_valor
        else:
            print("Error: Temperatura no permitida")


# --- Prueba ---
t = Termostato("Sala")
print(t.ver_temperatura())      # → 20  (valor inicial)
t.cambiar_temperatura(25)
print(t.ver_temperatura())      # → 25  (cambio válido)
t.cambiar_temperatura(100)      # → Error: Temperatura no permitida
print(t.ver_temperatura())      # → 25  (sin cambio)