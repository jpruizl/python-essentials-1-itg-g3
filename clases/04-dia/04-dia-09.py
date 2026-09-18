# listas anidadas

# ej.1
lista = ['hola', 2.0, 5, [10, 20], True]
# total de elementos = 7 o 5
print(len(lista))
print()

print('elemento 1:', lista[0])
print('elemento 2:', lista[1])
print('elemento 3:', lista[2])
print('elemento 4:', lista[3])
print('elemento 5:', lista[4])
print('elemento 6:', lista[3][0])
print('elemento 7:', lista[3][1])

print()

# Ej.2
tarjetaHabiente = [['nombre','apellido',40,'pais','direccion',55871124],
                    [100_000_00, 70_000, 30_000, 25_000, 0.11, 0],
                    [True, 'A']]

print(tarjetaHabiente)

# si el sueldo supera 15,000.00
# y el cliente debe estar activo

if tarjetaHabiente[1][3] > 15000.00:
    if tarjetaHabiente[2][0] == True:
        print('sueldo del tarjeta habiente es:', tarjetaHabiente[1][3])
        print('estado del tarjeta habiente', tarjetaHabiente[2][0])
        print('cliente apto a nueva tarjeta')
        print('llamar al cliente por su apellido y es:', tarjetaHabiente[0][1])
        print('el número de telefono es:', tarjetaHabiente[0][5])
    else:
        print('no es apto a tarjeta')

