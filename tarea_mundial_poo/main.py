import os
import pandas as pd
from jugadores import Portero, Defensa, Mediocampista, Delantero

def main():

# === Creación de la Selección ===
    pais_elegido = "Francia"
    
    print("=============================================")
    print(f" SIMULADOR DE CAMPEÓN DEL MUNDO: {pais_elegido.upper()} 2026")
    print("=============================================\n")

# --- Jugadores Titulares ---
    jugadores_titulares = [
        Portero("Mike Maignan", 30, 1.91, 16, 115, 92),
        
        Defensa("Jules Koundé", 27, 1.80, 5, 88, 120),
        Defensa("William Saliba", 25, 1.92, 4, 102, 145),
        Defensa("Dayot Upamecano", 27, 1.86, 17, 95, 130),
        Defensa("Lucas Digne", 32, 1.78, 22, 65, 90),
        
        Mediocampista("Aurélien Tchouaméni", 26, 1.88, 8, 15, 1200),
        Mediocampista("Adrien Rabiot", 31, 1.88, 14, 25, 1050),
        Mediocampista("Ousmane Dembélé", 29, 1.78, 11, 40, 850),
        Mediocampista("Michael Olise", 24, 1.84, 7, 18, 500),
        
        #Considerando a los extremos Dembelé y Olise como "mediocampistas" por las bandas para así tener el 1-4-4-2
        Delantero("Kylian Mbappé", 27, 1.78, 10, 85, 210),
        Delantero("Bradley Barcola", 23, 1.86, 20, 12, 45)
    ]

# --- Uso de Métodos ---
    print("--- ACCIONES EN LA CANCHA ---")
    print(jugadores_titulares[0].correr())           # Método heredado
    print(jugadores_titulares[0].atajar())           # Método propio del Portero
    print(jugadores_titulares[9].calentar())         # Método inventado heredado
    print(jugadores_titulares[9].patear_al_arco())   # Método propio del Delantero
    print("\n")

# --- Polimorfismo ---
    print("--- ROLES TÁCTICOS DEL EQUIPO ---")
    for jugador in jugadores_titulares:
        print(f"{jugador.nombre} - {jugador.mostrar_rol()}")

# === Uso de Pandas y Exportación a CSV ===
# --- Data Frame ---
    datos_equipo = []
    for jugador in jugadores_titulares:
        datos_equipo.append({
            "Pais": pais_elegido,
            "Dorsal": jugador.dorsal,
            "Nombre": jugador.nombre,
            "Edad": jugador.edad,
            "Altura_m": jugador.altura,
            "Posicion": jugador.mostrar_rol()
        })
        
    df = pd.DataFrame(datos_equipo)
    
# --- Requisitos de Consola ---
    print("1. TABLA COMPLETA DEL EQUIPO:")
    print(df.to_string(index=False))
    
    edad_promedio = df['Edad'].mean()
    print(f"\n2. Edad promedio del equipo: {edad_promedio:.1f} años")
    
    altura_max = df['Altura_m'].max()
    print(f"3. Altura máxima del equipo: {altura_max} metros")
    
    print("\n4. Cantidad de jugadores por posición:")
    print(df['Posicion'].value_counts().to_string())
    
    print("\n5. Promedio de edad por posición:")
    print(df.groupby('Posicion')['Edad'].mean().to_string())
    
# --- Exportación ---
    os.makedirs('output', exist_ok=True) 
    
    nombre_archivo = f"titulares_{pais_elegido.lower()}.csv"
    ruta_archivo = os.path.join('output', nombre_archivo)
    
    df.to_csv(ruta_archivo, index=False)
    print(f"\n[ÉXITO] Base de datos exportada en: {ruta_archivo}")

if __name__ == "__main__":
    main()