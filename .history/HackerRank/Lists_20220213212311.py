x = int(input())
y = int(input())
z = int(input())
n = int(input())


li = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if(x + y + z) != n:
                li.append([i,j,k])
            else:
                pass
            

print(li)


