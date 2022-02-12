import math


def Arm(g):
    sum = 0
    while(g!=0):
        l = g % 10
        sum += pow(l , nod(g))
        return sum
    

m = int(input())

print(nod(m))















# if(Arm(m) == m):
#     print("Armstrong number")
# else:
#     print("Nope")
    
    
