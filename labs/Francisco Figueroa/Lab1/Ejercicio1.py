
# ejercicio1:
#Ingrese los valores de voltaje (V) y corriente(I)
V = int(input('Ingrese los valores de voltaje (V): ')) #tiene que ser con int, ya que es un numero con letras
I = int(input('Ingrese valores de corriente (I): '))

R = V/I
print(f'La resistencia es de: "{R}" (ohm)')

#potencia:
print("/////////")
P= V*I
if (P>1000):
    print(f'La potencia disipada es de: "{P}" (Watts)')
    print("¡Peligro! Alta disipación de potencia detectada.")
else:
    print(f'La potencia disipada es de: "{P}" (Watts)')
    print("Operación en rangos seguros.")