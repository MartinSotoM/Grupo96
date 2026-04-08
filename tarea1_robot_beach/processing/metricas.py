import numpy as np

# Cálculos
def calcular_IAE(errores, dt):
    return float(np.sum(np.abs(errores)) * dt)

def calcular_ISE(errores, dt):
    return float(np.sum(errores**2) * dt)

def calcular_ITAE(errores, dt):
    ti = np.arange(len(errores)) * dt
    return float(np.sum(ti * np.abs(errores)) * dt)

def calcular_ITSE(errores, dt):
    ti = np.arange(len(errores)) * dt
    return float(np.sum(ti * (errores**2)) * dt)

# Función agrupadora
def calcular_todas_las_metricas(errores, dt):
    resultados = {
        "ISE": round(calcular_ISE(errores, dt), 2),
        "IAE": round(calcular_IAE(errores, dt), 2),
        "ITSE": round(calcular_ITSE(errores, dt), 2),
        "ITAE": round(calcular_ITAE(errores, dt), 2)
    }
    return resultados

# Reducción del error
def calcular_mejora(valor_ppo, valor_mask):
    assert valor_ppo != 0, "El valor base (PPO) no puede ser cero, imposible calcular mejora."
    
    mejora = ((valor_ppo - valor_mask) / valor_ppo) * 100
    return round(mejora, 2)
