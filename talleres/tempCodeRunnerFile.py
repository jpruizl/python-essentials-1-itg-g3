# Solicitar información al usuario
cliente = input('Ingrese el nombre del cliente: ')
fecha = input('Ingrese la fecha de la factura: ')

# Inicializar variables
subtotal = 0
total = 0

# Imprimir encabezado de la factura
print('\n===========================')
print('       FACTURA DE VENTA      ')
print('=============================')
print('Cliente:', cliente)
print('Fecha:', fecha)
print('=============================')

# Ciclo repetitivo para agregar productos
while True:
    producto = input('Ingrese el nombre del producto (o "fin" para terminar): ')
    if producto == 'fin':
        break

    precio = float(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad de productos: '))

    subtotal_item = precio * cantidad
    print(producto, ' x ', cantidad, ' =$ ', subtotal_item)

    subtotal += subtotal_item

# calcular el impuesto y total
impuesto = subtotal * 0.16
total = subtotal + impuesto

# formato pie de factura
print('=============================')
print('Subtotal: $', subtotal)
print('Impuesto (16%): $', impuesto)
print('Total a pagar: $', total)
print('=============================')
