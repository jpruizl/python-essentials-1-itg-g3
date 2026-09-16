# Ciclos repetitivos

# Ej.1

n = 5  # números primos a sumar
suma = 0  # la acumulación o sumatoria de los n numeros primos
i = 1  # el contador (las veces que va repitiendo el ciclo)

while i <= 5:
    suma += i  # suma = suma + i
    i += 1

print('la suma de los primeros', n, 'numeros es:', suma)
print()
print(f'La suma de los primeros {n} numeros naturales es {suma}')

print('el valor de mi contador finaliza siendo:', i)

print()
print()


# Ej.2
numeroSecreto = int(input('Ingresa un número a adivinar (entre 1 y 20): '))
adivinado = False
intentos = 0

while not adivinado:
    intento = int(input('Adivina el número (entre 1 y 20): '))
    intentos += 1

    if intento == numeroSecreto:
        print('Felicidades adivinistae, en', intentos, 'intentos')
        adivinado = True
    elif intento < numeroSecreto:
        print('El número secreto es mayor')
    else:
        print('el número es menor')

print('Gracias por usar nuestro software de diversión')


# Ej.3
i = 1

while i <= 10:
    j = 1
    print('Tabla del', i)
    while j <= 10:
        resultado = i * j
        print(i, ' X ', j, '=', resultado)
        j += 1
    print()
    i += 1



# Ej.4
i = 1

while i <= 5:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1




# Ej.5 Tablero de Ajedrez
tamanio = 8

fila = 1
while fila <= tamanio:
    columna = 1
    while columna <= tamanio:
        if (fila + columna) % 2 == 0:
            print('■', end=' ')
        else: 
            print('□', end=' ')
        columna += 1
    print()
    fila += 1
    