from numpy import array
import numpy as np
my_str = "Shahnawaz123"

print(my_str.istitle())
print(my_str.endswith('3'))
print(my_str.isalpha())
print(my_str.isalnum())
print(my_str.lower())
print(my_str.upper())
print(my_str.isascii())


lis = [1, 2, 3, 4]
# arr = np.array(lis)
print(type(array))

# This is the conversion of list to array

aa = array([1, 2, 3, 4, 5])


# print(arr.shape)  # One d array

# arr.reshape()

li1 = [1, 2, 3, 4, 5]
li2 = [6, 7, 8, 9, 1]
li3 = [3, 4, 5, 6, 1]

arr = np.array([li1, li2, li3])  # Making a 2d array
# print(arr.shape)

# arr.reshape(5,3)
# print(arr.shape)

# print(arr.reshape(5,3))

print(arr)

# Changing the shape of the array 

# Indexing :

# a = ([1,2,3,4,5])

# print(a[2])

print(arr[:,:2])  # Accessing the elements of the columns 

print(arr[0:2]) # Accessing the elements of the row 

print(arr[0:2 ,0:2])  # Accessing the elements of both the rows and cols 

print(arr[1:,3:]) 

li4 = [1,2,3,4,5]
li5 = [2,3,4,5,6]
li6 = [9,7,6,8,9]

w = np.array([li4 , li5 , li6])




















