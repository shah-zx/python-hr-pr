li = []
i = int(input())

for n in range(0 , i):
    cmd = input().split()
    if(cmd[0] == 'insert'):
        li.insert(cmd[1] , cmd[2])
    elif(cmd[0] == 'append'):
        li.append(cmd[1])
    
















# li.append(2)
# li.append(12)
# li.append(22)
# li.append(20)
# li.append(24)

# li.insert(0, 1)

# li.sort()

# li.pop()
# print(li)

