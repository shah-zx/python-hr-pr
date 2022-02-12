# Recursion is when a function calls itself only inside the function :

def Fact(n):
    if n == 1 | n == 0:
        return 1
    else:
        return n * Fact(n - 1)
    

print("Enter your number")
y  =int(input())
print(Fact(y))

# Finding out the factorial of a given number 
