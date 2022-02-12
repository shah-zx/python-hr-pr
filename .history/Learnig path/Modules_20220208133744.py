from itertools import count
import random

# n = random.randint(0,1)
# print(n)

# rnumber = random.random()
# print(rnumber)

# li = ["aaj tak" , "sony" , "CN" , "pogo"]

# choice = random.choice(li)

# print(choice)



print("----------------Welcome to Nawaz's world -----------------")


nos = random.randint(1,6)

print("In this game : 1) You will roll the dice 2) If the number on the dice is even you will move 2 steps and if odd then 1 step")

print("Roll the dice")

n = 1
while n != 50:
    print("The number came is " , nos)        
    if(nos % 2 == 0):
            n +=2
    else: n+=1


print("----------------Thank you !!----------------------------")
