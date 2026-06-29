import numpy as np

# One dimension
array1 = np.array([32,65,87,98])
print(array1)

# Two dimension
array2 = np.array([[32,65,87,98],[32,45,78,27]])
print(array2)

'''
Operations
'''
w= np.array([[3,7],[5,10]])

p= np.array([[5,6],[3,1]])

print("Adding 2 to every element: \n", w + 2)

#Array sum

print("Array sum:\n", w + p)

#Sum of all array eledents

print("sum of all array elements:", w.sum())

'''
Type
'''

array3 = np.array([32, 65, 87, 98])
print(type(array3))
print(array3.dtype)

'''
Function
'''

