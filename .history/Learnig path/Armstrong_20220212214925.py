import math


def Arm(g):
    for i in range(g):
    
    sum = 0
    n = len(str(g))
    while(g!=0):
        l = g % 10
        sum += l ** n
        return sum
    

m = int(input())

print(nod(m))















# if(Arm(m) == m):
#     print("Armstrong number")
# else:
#     print("Nope")
    
    
