p = int(input())
n = int(input())


# Method 1 :

# tmp = p
# p  = n
# n = tmp

# Method 2 :

n = n + p   # n = 6 , p = 5 : 6 + 5 = 11
p = n - p   # p = 11 - 5 = 6
n = n - p   # n = 11 - 6 = 5


print(p)
print(n)


