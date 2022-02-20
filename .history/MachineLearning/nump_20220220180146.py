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
arr = np.array(lis)
print(type(array))

# This is the conversion of list to array

aa = array([1, 2, 3, 4, 5])


print(arr.shape)  # One d array

# arr.reshape()
li1 = [1, 2, 3, 4, 5]
li2 = [6, 7, 8, 9, 1]
li3 = [3, 4, 5, 6, 1, ]

np.array(li1, li2, li3)

