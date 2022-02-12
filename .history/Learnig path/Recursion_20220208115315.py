# Recursion is when a function calls itself only inside the function :

def Fact(n):
    if n == 1:
        return 1
    else:
        return n * Fact(n - 1)