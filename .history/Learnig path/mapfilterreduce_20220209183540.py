from math import sqrt
from tkinter import Y


li = ["12", "16", "90"]

# for i in range(len(li)):
#     li[i] = int(li[i])


# li[1] += 1

# print(li[1])

# The above code could be done by mapping as


def square(x):
    return x * x


def cube(y):
    return y * y * y


num = [square, cube]

for i in range(5):
    sq = list(map(lambda x: x(i), num))
    print(sq)
    

def fun(d) : return sqrt(d)

print(fun(49))


l = [1,2,3,4,5,6,7,8,9]

def is_greater_than_5(num):
    if(num > 5):
        return num
    
    
gr_than = list(filter(is_greater_than_5 , l))
print(gr_than)

# Reduce :

list2 = [1,2,3,4,5]


lr = list(filter(lambda x , y : x + y , list2))


    





