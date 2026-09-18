# clonación de listas
"""
a = [1, 2, 3]
b = a[:]

print('lista original a:', a)
print('lista original b:', b)

print()

b[0] = 5

print('lista original a:', a)
print('lista original b modificada:', b)

print()

# Ej.2 - rebanadas de una lista con operadorde segmento [:]

my_list = [32, 55, 23, 19, 4]
print('my_list:', my_list)

new_list = my_list[1:3]
print('new_list', new_list)  # 55, 23

print()

# Ej.3 
my_list = [32, 55, 23, 19, 4]
print('my_list:', my_list)

new_list = my_list[2:-1]
print('new_list', new_list)

print()

# Ej.4
my_list = [32, 55, 23, 19, 4]
print('my_list:', my_list)

new_list = my_list[:3]
print('new_list:', new_list)

print()


# Ej.5
my_list = [32, 55, 23, 19, 4, 10]
print('my_list:', my_list)

new_list = my_list[3:]
print('new_list:', new_list)

print()


# Ej.6 elmininado rebandas con del
my_list = [10, 8, 6, 4, 2]
print('my_list:', my_list)

del my_list[1:3]

print(my_list)

print()
"""

# Ej.7 eliminando todos los elementos de la lista
my_list = [10, 8, 6, 4, 2]
print('my_list:', my_list)

del my_list[:]
print('my_list:', my_list)

print()

# Ej.8 eliminando la lista con del
my_list = [10, 8, 6, 4, 2]
print('my_list:', my_list)

del my_list

print('my_list:', my_list)

print()