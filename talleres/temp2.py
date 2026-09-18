beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range(2):    
    nombre = input("Agrega un miembro de la banda: ")   
    beatles.append(nombre) 


del beatles[4] #-1
del beatles[3] #-1

beatles.insert(0, "Ringo Starr")
print(len(beatles))

print(beatles)
