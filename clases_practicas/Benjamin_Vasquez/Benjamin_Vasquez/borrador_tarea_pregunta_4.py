import numpy as np
# pregunta a)

def calcular_IAE(errores, dt):
       errores = np.array(errores)
       return np.sum(np.abs(errores)) * dt


def calcular_ISE(errores, dt):
       errores = np.array(errores)
       return np.sum(errores**2) * dt


def calcular_ITAE(errores, dt):
       errores = np.array(errores)
       t = np.arange(len(errores)) * dt
       return np.sum(t * np.abs(errores)) * dt


def calcular_ITSE(errores, dt):
       errores = np.array(errores)
       t = np.arange(len(errores)) * dt
       return np.sum(t * (errores**2)) * dt

# pregunta b)

def calcular_todas_las_metricas(errores,dt):
       resultados = {"IAE": float(round(calcular_IAE(errores,dt),2))  , 
                   "ISE": float(round(calcular_ISE(errores,dt),2))    , 
                    "ITAE": float(round(calcular_ITAE(errores,dt),2)) , 
                     "ITSE": float(round(calcular_ITSE(errores,dt),2))}
       return resultados

# pregunta c)

def calcular_mejora(valor_ppo, valor_mask):
       if valor_ppo == 0:
              return 0     # en caso de que el valor PPO sea cero, no se puede calcular la mejora porcentual
       return ((valor_ppo - valor_mask) / valor_ppo) * 100
   