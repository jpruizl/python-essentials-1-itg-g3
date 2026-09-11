# Estructuras condicionales
"""
# Ej.3 - uso de if-else-elif
x = 5
y = 7

if x < y:
    print(x, "es menor que", y)
elif x > y:
    print(y, "es mayot que", y)
else:
    print(x, '&', y, 'son iguales')
print('el programa siempre pasa por aqui')

print()


# Ej.3b
temperatura = float(input('Ingresa Temperatura (rango de 10 a 40): '))

if temperatura <= 10:
    print('Hace mucho frio')
    print('Debes abrigarte, lleva una sudadera')
elif temperatura <= 20:
    print('Hace un poco de frio')
    print('Debes llevar una sudadera fresca')
    print('puede que la necesites')
elif temperatura <= 30:
    print('Hace un clima agradable')
    print('No requieres llevar sudadera')
else:
    print('Hace mucho calor')
print('el programa siempre pasa por aqui')
"""
print()

#Ej. 3c- uso de if-else-elif
numero = int(input('Ingresa un numero de -10 a 10: '))

if numero % 2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')
print('el programa siempre pasa por aqui')

if numero > 0:
    print('El numero es positivo')
elif numero < 0:
    print('El numero es negativo')
else:
    print('el numer es cero')
print('el programa siempre pasa por aqui')

