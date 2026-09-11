""" 
kilometros = float(input("Kilómetros recorridos: "))
litros = float(input("Litros de combustible gastados: "))
print()
consumo = kilometros / litros
print()
print("El consumo por kilómetro es de: ", consumo)
"""

# solución 2
kilo = float(input ('eprintntre los kilometros recorrido:    '))
consumo = float(input ('litros de combustibles:    '))
consumo = kilo/consumo
print ()
print (consumo)
 

print('-' * 20)

"""
Cree un programa para evaluar si una persona cumple distintos requisitos
para optar a una beca de tecnología. El programa debe solicitar el nombre, 
la edad, el promedio académico, si posee computadora y si tiene conexión 
a internet. Luego, debe mostrar si la persona tiene la edad mínima requerida
de 18 si alcanza el promedio mínimo de 80 puntos, si cuenta con los 
recursos tecnológicos necesarios para estudiar y si puede participar 
en una actividad especial para estudiantes con promedio de 90 puntos o más 
o con 25 años o menos. El programa no debe tomar decisiones ni mostrar 
mensajes diferentes según el resultado; únicamente debe imprimir 
los resultados de cada evaluación como True o False
"""

# solución 1
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
promedio = float(input("Ingrese su promedio: "))
computadora = int(input("Ingrese 1 si posee computadora, 0 si no posee computadora: "))
internet = int(input("Ingrese 1 si tiene internet, 0 si no tiene internet: "))
print(edad >= 18 and promedio >= 80 and computadora == 1 and internet == 1)

# solución 2
name = (input ('entre su nombre:    '))
print (name)
edad = (input ('la edad:    '))
print (edad)
prom = float(input ('entre el promedio:    '))
print (prom)
computadora = (input ('tiene computadora:    '))
print (computadora)
internet = (input ('internet:    '))
print(internet)
edadmin = (edad >= 18 and prom >= 80) and computadora == 'si' and internet == 'si'
print (edadmin)


# solución 3
# datos input
nombre = input("Nombre: ")
edad = int(input("Edad: "))
promedio = float(input("Promedio Académico: "))
# boolean
computadora = input("¿Tienes Computadora? Si/No: ")
conexión = input("¿Tienes Conexión? Si/No: ")
# decisiones
edadmin = edad >= 18
promemin = promedio >= 80
recursos = (computadora == "si") and (conexión == "si")
actividad = (promedio >= 90) or (edad <= 25)
#salida
print("Resultados")   # 20 93.25 si no 
print("Edad minima requerida: ", edadmin) # True
print("Promedio minimo de: ", promemin) # True
print("¿Cuenta con los recursos necesarios?: ", recursos) # False
print("¿Puede participar de la actividad?: ", actividad) # True



