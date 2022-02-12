import time


initial = time.time()
k = 0

while k < 0:
    print("Hello")
    k += 1
    print("The time it took is ", time.time() - initial)

for i in range(45):
    print("Hi")
    print("The time it took is ", time.time() - initial)
