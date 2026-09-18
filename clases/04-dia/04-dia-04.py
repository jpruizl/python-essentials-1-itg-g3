# Ej.1 - intercambiar o revertir el orden de la lista

miLista = [1, 2, 3, 4, 5]

print(miLista)

miLista[0], miLista[4] = miLista[4], miLista[0]
miLista[1], miLista[3] = miLista[3], miLista[1]

print(miLista)

print()
print()

# Ej.2 - intercambiar elementos con for en una lista
miLista = [1, 2, 3, 4, 5, 6, 7]

print(miLista)
longitud = len(miLista)

for i in range(longitud // 2):
    miLista[i], miLista[longitud -i -1] = miLista[longitud -i -1], miLista[i]

print(miLista)

print()