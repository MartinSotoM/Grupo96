# En este ejercicio, se valida el ángulo de un servomotor antes de moverlo físicamente

def mover_servo(angulo):
    try:
        # 1. Verificar que el tipo sea entero — float causaría problemas en el controlador
        if not isinstance(angulo, int):
            raise TypeError(f"Se esperaba int, se recibió {type(angulo).__name__}")

        # 2. Verificar que el ángulo esté dentro del rango físico del servo [0°, 180°]
        assert 0 <= angulo <= 180, f"Ángulo {angulo}° fuera del rango permitido [0, 180]"

        # 3. Si las validaciones pasan, mover el servo
        print(f"  Moviendo servo a {angulo}°")

    except TypeError as e:
        print(f"  [TypeError]                  {e}")

    except AssertionError as e:
        # AssertionError implica que el hardware podría dañarse — se etiqueta como fallo físico
        print(f"  [Fallo de seguridad hardware] {e}")

    finally:
        # Se ejecuta siempre, incluso si hubo excepción — señal de seguridad del hardware
        print(f"  Estado del motor: Standby\n")


# 4. Probar los tres escenarios posibles
mover_servo(90)       # caso válido
mover_servo(200)      # ángulo fuera de rango
mover_servo(45.5)     # tipo incorrecto