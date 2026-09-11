print('Estilos de variables')

print('snake_case')
mi_variable = 10
color_auto_nuevos = 'Rojo'

print('Pascal Case')
MiVariable = 10
ColorAutoNuevos = 'Rojo'

print('camelCase')
miVariable = 10
colorAutoNuevos = 'Rojo'

print('skewer-case, no permitido en Python')
# mi-variable = 10
# color-auto-nuevos = 'Rojo'

print('SCREAMING_SNAKE_CASE')
print('constantes')
MIVARIABLE = 10
COLORAUTONUEVOS = 'Rojo'

print('nocase')
mivariable = 10
colorautonuevos = 'Rojo'

print('fuckHeCase')
malaspalabras = 10

print('SPongeBob Case')
firulais = 10
miprincesabella = 15
eldiaquenaci = 'Rojo'


print('Variables')

variable = 1
balance_general = 1000.0
nombre_cliente = 'Juan Ruiz'
clasificacion = 'A'  
estado = True
print(variable)
print(balance_general)
print(nombre_cliente)
print(clasificacion)
print(estado)

print(type(variable))
print(type(balance_general))
print(type(nombre_cliente))
print(type(clasificacion))
print(type(estado))

print("Python dara un error si se usa una variable que no exista")
var = 1
print(var)
#print(Var)  # variable no creada

print("Case Sensitive demostracion")
a = 150
A = 100
print(a)
print(A)
print("El saldo pendiente es: ", A)

print("Tipos de variables")
numEntero = 115
numDecimal = 12.68
varCaracter = 'a'
varCadena = 'esto es una cadena'
bandera = True

edad = 45
print(edad)
print(type(edad))
edad = "edad"
print(edad)
print(type(edad))

print("otra forma de asignar variables en una sola linea")
A, B, C = 15, 64.25, "string"
print(A)
print(B)
print(C)
print(type(A))
print(type(B))
print(type(C))

print("otra forma de desplegar la salida en pantalla es:")
print(A, B, C)

print("otra manera de utilizar una salida es:")
print("La variable varCadena tiene el valor de: ", varCadena)

print("podemos asignar en una linea, un mismo valor a diferentes variables")
a = b = c = "todas son tipo cadena"
print(a)
print(b)
print(c)

print("podemos realizar calculos con nuestras variables")
numero1 = 55
numero2 = 60
sumNum1Num2 = numero1 + numero2
print("El resultado de sumar numero1 + numero2 es: ", sumNum1Num2)

print("Sustituir el valor de una variable")
var1 = 65
print(var1)
var1 = 25.50
print(var1)
var1 = "cambios"
print(var1)

print("Que hara esta salida")
var = 100
var = 200 + 300
print(var)

print("Realicemos un script para calcular el promedio de 5 notas, de un estudiante")
print("desplegar su nombre y su promedio")
nombreEstudiante = "Iker Salvador"
nota1 = 65.50
nota2 = 75
nota3 = 90.4
nota4 = 85
nota5 = 92.3

print("opcion 1 - resolucion")
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print("El promedio del alumno ", nombreEstudiante, " es: ", promedio)

print("opcion 2 - resolucion")
print("El promedio del alumno", nombreEstudiante, " es: ", (nota1 + nota2 + nota3 + nota4 + nota5) / 5)
print("Que diferencia tienen, no creo la variable promedio")



print("cosas que no podemos hacer con las variables")
varString = "soy una cadena"
varNumero = 25
#print(varString + varNumero)
print("no son del mismo tipo, no pueden procder a la concatenacioni u operacion")



print("ejemplos finales con variables")
miNombre = "Juan Pablo"
miApellido = "Ruiz"
miEdad = 48
miNacimiento = 1974
miTitulo = "Ingeniero en Sistemas"

print("Me llamo", miNombre, "Mi apellido es", miApellido, "Tengo", miEdad, "Naci en", miNacimiento, "soy", miTitulo)
