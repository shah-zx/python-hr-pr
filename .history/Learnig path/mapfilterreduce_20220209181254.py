from math import sqrt


li = ["12", "16", "90"]

# for i in range(len(li)):
#     li[i] = int(li[i])


# li[1] += 1

# print(li[1])

# The above code could be done by mapping as


def square(x):
    return x * x


def cube(y):
    return y * y * y


num = [square, cube]

for i in range(5):
    sq = list(map(lambda x: x(i), num))
    print(sq)
    

def fun(d) : return sqrt(d)

print(fun(d))






