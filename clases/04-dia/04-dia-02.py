# listas - continuación

# Ej.18 - recorriendo una lista por for
colores = ['rojo', 'negro', 'verde', 'azul', 10]

print(colores)
print(type(colores))

print()

for color in colores:
    print('el color es:', color)
    print(type(color))

print()
print()

# Ej.19 - recorriendo una lista while
animales = ['aves', 'reptiles', 'anfibios', 'salvajes']

i = 0
while i < 4:
    print(animales[i])
    i = i + 1

print()
print()

# Ej.20 - recorriendo una lista while y len()
utEscolares = ['lapiz', 'crayon', 'regla', 'marcador', 'lapicero']

i = 0
while i < len(utEscolares):
    print('el util escolar es:', utEscolares[i])
    i = i + 1


print()
print()

# Ej.21 - sumar los elementos de una lista
listaSumar = [25, 10, 5, 15, 1]
total = 0

for i in range(len(listaSumar)):
    total += listaSumar[i]

print('total es:', total)

print()
print()

# Ej.22- otra manera de resolver el anterior
listaSumar = [25, 10, 5, 15, 1]
total = 0

for i in listaSumar:
    total += i

print('el total es:', total)
print()