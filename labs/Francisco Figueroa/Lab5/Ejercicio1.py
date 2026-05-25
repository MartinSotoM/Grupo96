# En este ejercicio, se parsea una trama de texto con formato ID:Valor proveniente de un sensor

def procesar_trama(trama):
    try:
        # 1. Separar la trama con el delimitador ':' y extraer el valor
        partes = trama.split(':')
        valor = float(partes[1])  # IndexError si no hay índice 1, ValueError si no es numérico

        print(f"  ID     : {partes[0]}")
        print(f"  Valor  : {valor}")
        return valor

    except IndexError:
        # Ocurre cuando la trama llega sin delimitador ':'
        print(f"  [IndexError]  Trama incompleta, no se encontró el delimitador ':'")

    except ValueError:
        # Ocurre cuando el campo Valor no puede convertirse a float
        print(f"  [ValueError]  El dato '{partes[1]}' no es un valor numérico válido")

    except Exception as e:
        # Captura cualquier otro error no previsto — siempre al final
        print(f"  [Error inesperado]  {e}")


# 2. Probar con distintos casos para cubrir cada excepción
print("--- Trama válida ---")
procesar_trama("TEMP:23.5")

print("\n--- Sin delimitador ---")
procesar_trama("TEMP23.5")

print("\n--- Valor no numérico ---")
procesar_trama("TEMP:veintitres")