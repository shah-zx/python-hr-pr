p = int(input())
n = int(input())


# Method 1 :

# tmp = p
# p  = n
# n = tmp

# Method 2 :

n = n + p
p = n - p
n = n - p


print(p)
print(n)


