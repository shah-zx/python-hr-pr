
import imp

import math

n = int(input())
p = int(input())

for i in range(n, p+1):
    if(i > 1):
        for num in range(2, n):
            if(i % num == 0):
                break
    else:
        print(i)
        
        
        
