# Listas

# Ej.1 - Sintaxis de listas
numeros = [10, 5, 7, 2, 1]

# Ej.2 - definiendo listas
string = ['palabra', 'animal', 'cadena']
numEnteros = [17, 123]
numDecimales = [15.34, 45.98, 1112.34]
valBooleanos = [True, False]
listaChar = ['a']
vacia = [ ]

# Ej.3 - listas mixtas - únicas en Python
listaMixta = ['String', 100, 'C', True, 125.54]

# Ej.4 - print() para visualizar contenido de las listas
print(string)
print(numEnteros)
print(numDecimales)
print(valBooleanos)
print(listaChar)
print(vacia)

print(type(string))
print(type(valBooleanos))

print()

# Ej.5 accediendo a la lista
numeros = [17, 125, 50]

print(numeros[1]) # 125
print(numeros[0]) # 17
print(numeros[2]) # 50

print()

# Ej.6 sustituyendo valores en la lista
numeros = [10, 5, 7, 2, 1]
print('contenido de la lista original', numeros)

numeros[0] = 111
print('Nuevo contenido en la lista', numeros)

print()

# Ej.7 copiando el valor de un elemento a otro
numeros = [10, 5, 7, 2, 1]
print('contenido de la lista original', numeros)

numeros[1] = numeros[4]
print('Nuevo contenido en la lista', numeros)

print()

# Ej.8 función len
listaNew = [25, 18.6, 3243, 332, 1, 0]

print('la lonigitud de la lista es:', len(listaNew))

print()

# Ej.9 del para eliminar elementos en una lista
autos = ['chevrolet', 'toyota', 'dodge']
print('lista original', autos)

del autos[1] #toyota
print('lista nueva', autos)

print()

# Ej.10 no podemos tener acceso a un elemento eliminado
numList = [10, 5, 18, 36, 6]

print(numList[4])

del numList[4]

# print(numList[4])

print()



# Ej.11 - indices negativos
listaNegativos = [115, 265, 48, 98]

print(listaNegativos[-1])
print(listaNegativos[-2])

# Extra - implemntación lista mixta
tarjetaHabiente = ['Diego', 'Lima', 36, 5000, 2.55, "A", True]
# Diego = nombre del tarjeta habiente
# Lima = apellido del tarjeta habiente
# 36 = edad del tarjeta habiente
# 5000 = límite de crédito
# 2.55 = interes
# A = tipo de cliente
# True = cliente activo
