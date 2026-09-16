# ciclos repetitivos
# uso de for

# ej.1
for i in range(10):
    print('el valor de i es actualmente:', i)

print()

# ej.2
for i in range(2, 8):
    print('el valor de i es actualmente:', i)

print()


# ej.3
mensaje = "Estoy en Curso de Python"

for caracter in mensaje:
    print(caracter)

print()


# ej.4
numeros = 1,2,3,4,5

for numero in numeros:
    print(numero)


print()


# Ej.5
for multiplicando in range (1, 11):
    print('Tabla del', multiplicando)
    for multiplicador in range(1, 11):
        resultado = multiplicando * multiplicador
        print(multiplicando, ' x ', multiplicador, '=', resultado)

print()


# Ej.6
for i in range(0, 11, 3):
    print(i)
