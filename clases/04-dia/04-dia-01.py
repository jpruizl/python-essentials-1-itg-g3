# listas continuación

# Ej.12 - método append()
numeros = [125, 98, 78, 94]
print('la longitud es:', len(numeros))
print('la lista original es:', numeros)

numeros.append(4)

print('la longitud es:', len(numeros))
print('la nueva lista original es:', numeros)

print()
print()

# Ej.13 - método append()
listaLetras = ['uno', 'dos']
print(listaLetras)

listaLetras.append('tres')
listaLetras.append('cuatro')
print(listaLetras)

print()
print()

# Ej.14 - método insert()
transportes = ['auto', 'moto', 'barco']
print(transportes)

transportes.insert(-1, 'tren')
print(transportes)

print()
print()

# Ej.15 - método insert()
newLista = [58, 25.6, 90, 35]
print(newLista)

newLista.insert(3,60)
# insert puede agregar elemento al final de una lista
# mas no siendo la mejor práctica a realizar.
print(newLista)

print()
print()

# Ej.16 - agregar elementos y declarar una lista vacia
my_list = []


my_list.append(0)

for i in range(5):
    my_list.append(i + 1)

print(my_list)

print()
print()

# Ej.17 - lista vacia cargar elementos por insert()
my_list2 = []

for i in range(5):
    my_list2.insert(0, i+1)

print(my_list2)

print()