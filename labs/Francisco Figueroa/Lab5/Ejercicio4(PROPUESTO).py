import math

# En este ejercicio, se calcula la magnitud de impedancia |Z| a partir de R y X ingresados por el usuario

def calcular_impedancia():
    try:
        # 1. Solicitar resistencia R y reactancia X — ValueError si el input no es numérico
        resistencia = float(input("Ingrese la Resistencia R [Ω]: "))
        reactancia  = float(input("Ingrese la Reactancia  X [Ω]: "))

    except ValueError:
        # Captura entradas como letras o cadenas vacías
        print("  [ValueError]  Los valores ingresados deben ser numéricos")

    else:
        # 2. El bloque 'else' solo se ejecuta si el bloque 'try' no lanzó ninguna excepción
        # |Z| = sqrt(R² + X²)
        magnitud_impedancia = math.sqrt(resistencia**2 + reactancia**2)

        print(f"\n  R        : {resistencia:.2f} Ω")
        print(f"  X        : {reactancia:.2f} Ω")
        print(f"  |Z|      : {magnitud_impedancia:.4f} Ω")


if __name__ == "__main__":
    calcular_impedancia()