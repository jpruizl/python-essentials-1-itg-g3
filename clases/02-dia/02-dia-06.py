# conversión de tipos de datos str

"""
num1 = float(input('Ingrese num1: '))
num2 = float(input('Ingrese num2: '))
suma = num1 + num2  
# print('La suma es:' + suma) No permitido
"""
print()

# solución con str() para concatenar
num1 = float(input('Ingrese num1: '))
num2 = float(input('Ingrese num2: '))
suma = num1 + num2

print('La suma es:' + str(suma))

print()

edad = 25
print('Mi edad es de ' + str(edad) + ' años')

print('Hola' + 'Mundo')

print('Hola' + str(2026))

print()

# Otros ejemplos
numerica = 100
numerica2 = str(numerica)

print(type(numerica))
print(type(numerica2))

print()

valor = 150
valor2 = float(valor)

valor3 = 225.60
valor4 = int(valor3)

print(type(valor))
print(type(valor2))
print(type(valor3))
print(type(valor4))

print(valor4)
