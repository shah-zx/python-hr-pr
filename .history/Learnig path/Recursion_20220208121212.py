# Recursion is when a function calls itself only inside the function :

# def Fact(n):
#     if n == 1 | n == 0:
#         return 1
#     else:
#         return n * Fact(n - 1)
    

# print("Enter your number")
# y  =int(input())
# print(Fact(y))

# Finding out the factorial of a given number 

def Fab(n):
    if n ==0 | n == 1:
        return 1
    return Fab(n-1) + Fab(n-2)


print("Enter your number")
y  =int(input())
print(Fab(y))


