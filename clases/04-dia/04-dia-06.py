# alias en las listas

a = [1, 2, 3]
b = a

print('lista original a:', a)
print('Lista original b:', b)

print()

b[0] = 5

print('lista original a:', a)
print('Lista original b modificada:', b)

# viceversa

a[0] = 10

print()
print('lista original a moidificada:', a)
print('Lista original b:', b)