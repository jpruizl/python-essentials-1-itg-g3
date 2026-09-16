# estructuras condicionales

# Ej.4 - condicionales anidados
x = 5
y = 7

if x == y:
    print(x, '&', y, 'son iguales')
else:
    if x < y:
        print(x, 'es menor que', y)
    else:
        print(x, 'es mayor que', y)
print('el programa siempre pasa por aqui')

print()


# Ej.5
nota = 92

if nota >= 60:
    if nota >= 90:
        print('Excelente trabajo')
    elif nota >= 80:
        print('Muy buen trabajo')
    else:
        print('Buen trabajo')
else:
    print('Necesitas mejorar tu aprendizaje')
print('el programa siempre pasa por aqui')

print()

# if's anidados
x = 5
y = 6

if x >= 3:
    if y == 6:
        if (x + y) > 0:
            print('se cumplieron todas las condiciones')
print('el programa siempre pasa por aqui')
