import os
import matplotlib.pyplot as plt

def plot_metricas(diccionario_experimentos, ambiente, ruta):

    # Filtrado
    datos_ppo = {}
    datos_ppo_mask = {}

    for exp_id, datos in diccionario_experimentos.items():
        if datos["ambiente"] == ambiente and datos["ruta"] == ruta:
            if datos["politica"] == "PPO":
                datos_ppo = datos
            elif datos["politica"] == "PPO-Mask":
                datos_ppo_mask = datos

    # Gráficos

    metricas = ["ISE", "IAE", "ITSE", "ITAE"]
    
    for i, metrica in enumerate(metricas, start = 1):
        plt.subplot(1, 4, i)
        
        valor_ppo = datos_ppo.get(metrica) or 0 # Blindaje
        valor_mask = datos_ppo_mask.get(metrica) or 0
        
        plt.bar(["PPO", "PPO-Mask"], [valor_ppo, valor_mask], color = ["#146fb1", "#d00e0e"])
        plt.title(f"Métrica: {metrica}")

    # Automatización

    carpeta_destino = "resultados_graficos"
    os.makedirs(carpeta_destino, exist_ok = True)
    
    nombre_archivo = f"metricas_{ambiente}_{ruta}.png"
    ruta_final = os.path.join(carpeta_destino, nombre_archivo)
    
    plt.savefig(ruta_final, dpi = 300)
    plt.close()


def plot_lidar(angulos, distancias, distancias_norm):

    # Visión Humana
    plt.subplot(1, 2, 1, title = "¿A qué distancia están los objetos?")
    plt.scatter(angulos, distancias)
    plt.xlabel("Ángulo de giro (0-360°)")
    plt.ylabel("Distancia detectada (m)")
    plt.grid(True)

    # Visión Máquina
    plt.subplot(1, 2, 2, title = "Datos Normalizados (Lo que procesa la IA)")
    plt.plot(angulos, distancias_norm)
    plt.xlabel("Sectores del sensor")
    plt.ylabel("Valor (0.0 a 1.0)")
    plt.grid(True)

    # Guardado
    carpeta_destino = "resultados_graficos"
    os.makedirs(carpeta_destino, exist_ok = True) 
    
    ruta_final = os.path.join(carpeta_destino, "simulacion_lidar.png")
    
    plt.savefig(ruta_final, dpi = 300)
    plt.close()


def plot_trayectorias(x_ppo, y_ppo, x_mask, y_mask, waypoints, nombre):

    plt.plot(x_ppo, y_ppo, color = 'b', linewidth = 2, alpha = 0.7, label = "Trayectoria PPO")
    plt.plot(x_mask, y_mask, color = 'r', linestyle = '--', linewidth = 2, label = "Trayectoria PPO-Mask")
    
    wx = [punto[0] for punto in waypoints]
    wy = [punto[1] for punto in waypoints]
    
    plt.scatter(wx, wy, color = 'black', marker = 's', s = 80, label = 'Waypoints (Metas)', zorder = 5)
    plt.axis("equal")
    plt.title(f"Comparación de Navegación: Ruta {nombre.capitalize()}")
    plt.xlabel("Posición X (metros)")
    plt.ylabel("Posición Y (metros)")
    plt.grid(True)
    plt.legend(loc='best')
    
    carpeta_destino = "resultados_graficos"
    os.makedirs(carpeta_destino, exist_ok = True) 
    
    ruta_final = os.path.join(carpeta_destino, f"trayectoria_{nombre}.png")
    
    plt.savefig(ruta_final, dpi = 300, bbox_inches = 'tight')
    plt.close()
