my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
 
new_list = []
 
for number in my_list:
    if number not in new_list:
        new_list.append(number)
 
my_list = new_list
 
print("La lista con elementos únicos:")
print(my_list)
 
 