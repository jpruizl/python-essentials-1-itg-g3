# Ejercicios de listas

# extend() exitiende la lista con los datos adicionales
num1 = [1, 2, 3]
otros_numeros = [4, 5, 6]

num1.extend(otros_numeros)

print(num1)

print()

# remove() eliminar el primer elemento de la lista con esa coincidencia
nombres2 = ['juan', 'maria', 'carlos']

nombres2.remove('maria')

print(nombres2)

print()

# pop() elimina y devuelve el elemento en la posición especificada
# o el último elemento si no se proporciona ninguna posición
num3 = [1, 2, 3, 4, 5]

elemento_eliminado = num3.pop(2)

print(num3)
print(elemento_eliminado)

print()

# index() delvueve la posición del primer eleento encontrado
num3 = [1, 2, 3, 4, 5]

posicion = num3.index(3)

print(posicion)

print()

# count() devuelve el número de veces que aparece el eleento en la lista
nu4 = [10, 3, 5, 3, 20, 15, 3, 8, 3]

cantidad = nu4.count(3)

print(cantidad)

print()

# clear() elimina todos los elementos de la lista
nu4 = [10, 3, 5, 3, 20, 15, 3, 8, 3]

nu4.clear()

print(nu4)

print()

# trucos con listas
# reversión rápida con slicing
numEnt = [1, 2, 3, 4, 5]

numeros_invertidos = numEnt[::-1]

print(numeros_invertidos)

print()

# copiar lista con copy()
lista = [1, 2, 3]

copia_lista = lista.copy()

print(copia_lista)

print()

# unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista_combinada = lista1 + lista2

print(lista_combinada)

print()

# crear una lista con valores repetidos
repeticiones = 3

numeros =[0] * repeticiones
print(numeros)

print()

# zip() combina elementos de dos o más listas convierte a tuplas
names = ['juan', 'maria', 'carlos']
edades = [30, 25, 35]

for nombre, edad in zip(names, edades):
    print(f'Nombre: {nombre}, Edad: {edad}')

print()

# unir múltiples listas en una sola
lista1 = [1,2,3]
lista2 = [4,5,6]

lista_combinada = [*lista1, *lista2]

print(lista_combinada)

print()