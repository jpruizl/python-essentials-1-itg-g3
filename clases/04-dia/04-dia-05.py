# ordenamiento método burbuja
"""
# Ej.1
my_list = [8, 10, 6, 2, 4]

print('lista original:', my_list)

for i in range(len(my_list) -1): # necesitamos (5-1) comparaciones
    if my_list[i] > my_list[i + 1]: # comparando elementos adyacentes
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        # Si terminamos aquí, tenemos el intercambio de elemntos

print('lista ordenada burbuja:', my_list)

print()

# Ej.2 - solución completa para el ordenamiento burbuja
my_list = [8, 10, 6, 2, 4]

print('lista original:', my_list)

estado = True

while estado:
    estado = False
    for i in range(len(my_list) -1):
        if my_list[i] > my_list[i + 1]:
            estado = True
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print('Lista ordenada por burbuja:', my_list)

print()
print()

# Ej.3 - solución interactiva de ordenamiento burbuja

my_list = []
estado = True

num = int(input('¿Cuantos elementos deseas ordenar o ingresar?: '))

for i in range(num):
    val = int(input('Ingresa un elemento de la lista: '))
    my_list.append(val)

print('Lista sin ordenar:', my_list)

while estado:
    estado = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i+1]:
            estado = True
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print('Lista ordenada burbuja:', my_list)

print()


# Ej.4 ordenamiento burbuja por método sort()
my_list = [8, 10, 6, 2, 4]
print('lista original:', my_list)

my_list.sort()

print('Lista ordenada por método sort():', my_list)

print()
"""

# Ej.5 - método reverse()

lst = [5, 3, 1, 2, 4]
print('lista original:', lst)

lst.reverse()

print('Lista invertida:', lst)
