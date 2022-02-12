for i in range(1001):
    num = i
    sum = 0
    n = len(str(i))
    while(i!=0):
        l = i % 10
        sum = sum + l ** n
        i // 10
    if(num == sum):
        print("Armstrong")
    else:
        print("Nope")
        
        
        
        
    

















# if(Arm(m) == m):
#     print("Armstrong number")
# else:
#     print("Nope")
    
    
