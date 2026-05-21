import math

# === ATRIBUTOS Y ENCAPSULAMIENTO ===
class RobotBase:
    def __init__(self, nombre: str, capacidad_carga: float, x_inicial=0.0, y_inicial=0.0, yaw_inicial=0.0):
        self.__nombre = nombre
        self.__capacidad_carga = capacidad_carga
        self.__bateria = 100.0
        self.__pos_x = x_inicial
        self.__pos_y = y_inicial
        self.__yaw = yaw_inicial
        self.__basura_recolectada = 0.0
        self.__step_dt = 0.1
        
        self.target_x = 5.0
        self.target_y = 5.0

    def get_nombre(self):
        return self.__nombre

    def get_bateria(self):
        return self.__bateria

    def get_pos_x(self):
        return self.__pos_x

    def get_pos_y(self):
        return self.__pos_y

    def get_yaw(self):
        return self.__yaw

    def get_basura_recolectada(self):
        return self.__basura_recolectada
    

    def _actualizar_pose(self, x, y, yaw):
        self.__pos_x = x
        self.__pos_y = y
        self.__yaw = yaw

    def _reducir_bateria(self, cantidad):
        self.__bateria -= cantidad
        if self.__bateria < 0:
            self.__bateria = 0.0

    def _recolectar_basura(self, cantidad):
        espacio_disponible = self.__capacidad_carga - self.__basura_recolectada
        
        if cantidad > espacio_disponible:
            self.__basura_recolectada += espacio_disponible
        else:
            self.__basura_recolectada += cantidad

# === MÉTODOS ESTÁTICOS ===

    @staticmethod
    def calc_dist_to_goal(pos_x, pos_y, target_x, target_y):
        return math.sqrt((target_x - pos_x)**2 + (target_y - pos_y)**2)

    @staticmethod
    def calc_yaw_error(pos_x, pos_y, yaw, target_x, target_y):
        theta_meta = math.atan2(target_y - pos_y, target_x - pos_x)
        
        err = theta_meta - yaw
        
        err_norm = (err + math.pi) % (2 * math.pi) - math.pi
        
        return err_norm

# === SIMULACIÓN CINEMÁTICA ===

    def step(self, v, w):
        if self.__bateria <= 0:
            return (0.0, True)

        yaw_nuevo = self.__yaw + w * self.__step_dt
        yaw_nuevo = (yaw_nuevo + math.pi) % (2 * math.pi) - math.pi

        x_nuevo = self.__pos_x + v * math.cos(yaw_nuevo) * self.__step_dt
        y_nuevo = self.__pos_y + v * math.sin(yaw_nuevo) * self.__step_dt

        self._actualizar_pose(x_nuevo, y_nuevo, yaw_nuevo)

        distancia = self.calc_dist_to_goal(self.__pos_x, self.__pos_y, self.target_x, self.target_y)
        error_angular = self.calc_yaw_error(self.__pos_x, self.__pos_y, self.__yaw, self.target_x, self.target_y)

        reward = -distancia - abs(error_angular)

        llegamos = False
        if distancia < 0.5:
            llegamos = True
            reward += 100.0

        return (reward, llegamos)

# === MÉTODOS ABSTRACTOS ===

    def mover(self):
        raise NotImplementedError("[ERROR ARCHITECTURE] Las clases hijas deben implementar el método mover().")

    def limpiar(self):
        raise NotImplementedError("[ERROR ARCHITECTURE] Las clases hijas deben implementar el método limpiar().")
