import random

n = random.randint(0,1)
print(n)

rnumber = random.random()
print(rnumber)

li = ["aaj tak" , "sony" , "CN" , "pogo"]

choice = random.choice(li)

print(choice)



print("----------------Welcome to Nawaz's world -----------------")


nos = [1,2,3,4,5,6]

print("In this game : 1) You will roll the dice 2) If the number on the dice is even you will move 2 steps and if odd then 1 step")

print("Roll the dice")

n = int (input())
count = 0
for n in nos:
    while n != 50:
        
         if(n % 2 == 0):
            count +=2
    else: count+=1


print("----------------Thank you !!----------------------------")
