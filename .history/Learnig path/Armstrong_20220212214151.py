import math

def nod(n):
    
    while(n != 0):
        count = 0
        ld = n % 10
        count +1
        n /= 10
        return count

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
    
    
