computers = ("HP","MacBook","DELL","Lenovo")
print(type(computers))

print(list(computers))

#Delete
# del computers
# print(computers)

#Update
list1 = list(computers)
list1.append("Acer")
computers = tuple(list1)
print(computers)

#Concatenate
num = (12,34,56,67)
print(num + computers)