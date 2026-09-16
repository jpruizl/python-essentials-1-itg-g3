# break y continue

"""
# ej.1 - break
for i in range(1, 6):
    if i == 3:
        break
    print('dentro del bucle', i)
print('fuera del bucle')

print()


# Ej.2 - continue
for i in range(1, 6):
    if i == 3:
        continue
    print('dentro del bucle', i)
print('fuera del bucle')



# Ej.3 - continue

print('un bucle para saltar los numeros pares')

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

"""

# Ej.4 - break

print('un bucle for para detener la ejecución')
print('cuando se encuentre un número especifico')

numeros = 1,2,3,4,5,6,7,8,9,10

for numero in numeros:
    if numero == 6:
        print('se encontro el número 6')
        break
    print(numero)
