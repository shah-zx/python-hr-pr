import math



for i in range(g):
    num = i
    sum = 0
    n = len(str(g))
    while(i!=0):
        l = i % 10
        sum += l ** n
        i // 10
    if(num == sum):
        print("Armstrong")
    else:
        print("Nope")
        
        
        
        
    

















# if(Arm(m) == m):
#     print("Armstrong number")
# else:
#     print("Nope")
    
    
