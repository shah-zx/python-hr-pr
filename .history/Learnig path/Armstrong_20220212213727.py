import math

def nod(n):
    count = 0
    while(n != 0):
        ld = n % 10
        count +1
        return count

def Arm(g):
    sum = 0
    while(g!=0):
        l = g % 10
        sum += pow(l , nod(g))
        




m = int(input())
