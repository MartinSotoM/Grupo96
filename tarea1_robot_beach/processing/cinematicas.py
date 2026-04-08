import numpy as np

# Nueva pose
def calcular_movimiento(x, y, theta, v, omega, dt = 0.1):
    v_segura = np.clip(v, -0.8, 0.8)
    omega_segura = np.clip(omega, -0.6, 0.6)
    
    x_nuevo = x + v_segura * np.cos(theta) * dt
    y_nuevo = y + v_segura * np.sin(theta) * dt
    theta_nuevo = theta + omega_segura * dt

    return (x_nuevo, y_nuevo, theta_nuevo)

# Distancia Euclidiana
def distancia_al_objetivo(x, y, x_meta, y_meta):
    return float(np.sqrt((x_meta - x)**2 + (y_meta - y)**2))

# Arreglos de Trayectoria
def calcular_error_seguimiento(x_real, y_real, x_ideal, y_ideal):
    largo_minimo = min(len(x_real), len(x_ideal))
    
    xr = x_real[:largo_minimo]
    yr = y_real[:largo_minimo]
    xi = x_ideal[:largo_minimo]
    yi = y_ideal[:largo_minimo]
    
    errores = np.sqrt((xr - xi)**2 + (yr - yi)**2)
    
    return errores