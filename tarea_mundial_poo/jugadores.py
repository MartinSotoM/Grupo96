# === Clase Padre ===
class Jugador:
    def __init__(self, nombre, edad, altura, dorsal):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dorsal = dorsal

# --- Métodos Obligatorios ---
    def correr(self):
        return f"{self.nombre} (Dorsal {self.dorsal}) está corriendo por la cancha."

    def mostrar_rol(self):
        return "Soy un jugador de futbol."

# --- Métodos inventados ---
    def calentar(self):
        return f"[{self.nombre}] está realizando trabajo físico y táctico de alta intensidad para entrar a la cancha."

    def celebrar_gol(self):
        return f"[{self.nombre}] está celebrando eufóricamente mirando a la grada."

# === Clases Hijas ===
class Portero(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, atajadas, reflejos):
        super().__init__(nombre, edad, altura, dorsal)
        self.atajadas = atajadas
        self.reflejos = reflejos

    def atajar(self):
        return f"{self.nombre} se lanza y realiza una atajada espectacular. (Atajadas totales: {self.atajadas})"

    def saque_largo(self):
        return f"{self.nombre} realiza un saque largo buscando el contragolpe rápido."

    def mostrar_rol(self):
        return "Portero"


class Defensa(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, balones_recuperados, duelos_ganados):
        super().__init__(nombre, edad, altura, dorsal)
        self.balones_recuperados = balones_recuperados
        self.duelos_ganados = duelos_ganados

    def marcar(self):
        return f"{self.nombre} se barre con precisión y recupera el balón."

    def despejar(self):
        return f"{self.nombre} revienta el balón lejos del área de peligro."

    def mostrar_rol(self):
        return "Defensa"


class Mediocampista(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, asistencias, pases_completados):
        super().__init__(nombre, edad, altura, dorsal)
        self.asistencias = asistencias
        self.pases_completados = pases_completados

    def dar_pase(self):
        return f"{self.nombre} filtra un pase milimétrico rompiendo líneas."

    def organizar_juego(self):
        return f"{self.nombre} pide el balón para dictar el ritmo del mediocampo."

    def mostrar_rol(self):
        return "Mediocampista"


class Delantero(Jugador):
    def __init__(self, nombre, edad, altura, dorsal, goles, tiros_al_arco):
        super().__init__(nombre, edad, altura, dorsal)
        self.goles = goles
        self.tiros_al_arco = tiros_al_arco

    def patear_al_arco(self):
        return f"{self.nombre} saca un misil al arco rival. ¡Peligro de gol!"

    def desmarcarse(self):
        return f"{self.nombre} arrastra la marca y crea un espacio letal en la defensa."

    def mostrar_rol(self):
        return "Delantero"
    