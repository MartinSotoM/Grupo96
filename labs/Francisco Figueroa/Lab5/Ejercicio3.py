# En este ejercicio, se consulta el promedio de lecturas de sensores almacenadas en un diccionario

def consultar_sensor():
    sensores = {
        'temp'    : [22.5, 23.1, 22.8],
        'presion' : [1013, 1015],
        'humedad' : []               # lista vacía para probar ZeroDivisionError
    }

    try:
        # 1. Solicitar nombre del sensor al usuario
        nombre_sensor = input("Ingrese el nombre del sensor a consultar ('temp', 'presion', 'humedad'): ")

        # 2. Acceder al diccionario — KeyError si la clave no existe
        lecturas = sensores[nombre_sensor]

        # 3. Calcular el promedio — ZeroDivisionError si la lista está vacía
        promedio = sum(lecturas) / len(lecturas)  # promedio = Σ x_i / n

        print(f"  Sensor   : {nombre_sensor}")
        print(f"  Lecturas : {lecturas}")
        print(f"  Promedio : {promedio:.2f}")

    except KeyError:
        # El sensor consultado no existe en el diccionario
        print(f"  [KeyError]           El sensor '{nombre_sensor}' no existe en el sistema")

    except ZeroDivisionError:
        # El sensor existe pero no tiene lecturas registradas
        print(f"  [ZeroDivisionError]  El sensor '{nombre_sensor}' no tiene lecturas disponibles")

    finally:
        # Se imprime siempre, independientemente del resultado de la consulta
        print("  Consulta de sensor finalizada")


if __name__ == "__main__":
    consultar_sensor()