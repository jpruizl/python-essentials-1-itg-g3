# Ej.1 intercambio de variables

variable1 = 1
variable2 = 2

variable2 = variable1
variable1 = variable2

print(variable1)
print(variable2)

print()

# Ej.2 intercambio de valores con una variable auxiliar
variable1 = 1
variable2 = 2

auxiliar = variable1

variable1 = variable2
variable2 = auxiliar

print(variable1)
print(variable2)

print()
print()

# Ej.3 - forma optima de Python
variable1 = 1
variable2 = 2

print(variable1)
print(variable2)

print() 

variable1, variable2 = variable2, variable1

print(variable1)
print(variable2)

print()