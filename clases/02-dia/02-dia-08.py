# Estructuras condicionales

# Ej.1 - el uso de if
print("Ej.1")

x = -6

if x > 0:
    print('x es positivo')
print("Aqui continua el programa")

print()

# Ej.1b - uso de if
print("Ej.1b")

edad = 21

if edad >= 18:
    print("Eres mayor de edad")
print('El programa siempre pasa por aqui')

print()

# Ej.1c - uso de if
print('Ej.1c')

usuario = "admin"
password = "secreta123"

if usuario == 'admin' and password == 'secreta123':
    print('Bienvenido a nuestro programa')
    print('Ahora puedes usar nuestra solucion')
print('El programa siempre pasa por aqui')

print()

# Ej.1d - uso de if
print('Ej.1d')

sueldo = 9000
tipoCliente = "A"
saldoMin = 500
mora = 3  # representa días de atraso

"""
Criterios:
1. Sueldo debe ser mayor de 10000
2. Tipo de cliente debe ser A
3. Debe cumplir criterios 1 y 2 si o si.
4. Saldo minimo debe ser mayor o igual a 1000
5. mora debe ser mayor o igual a 3
6. puede cumplir cualquiera de los dos criterios 4 y 5
7. Debe cumplir con los criterios del 3 y 6
"""

if (sueldo >= 10000 and tipoCliente == "A") and (saldoMin >= 1000 or mora >= 3):
    print('Tarjeta habiente apto a nueva tarjeta de credito')
    print('Debes llamar al tarjeta habiente, para indicarle proceso')
    print('Solicitar lugar de entrega')
print("Gracias por usar nuestras soluciones de software")


print()

# Ej.1e
print("Ej.1e")

bandera = True

if not bandera:
    print('Dime que fue verdadero')
print('El programa siempre pasa por aqui')

