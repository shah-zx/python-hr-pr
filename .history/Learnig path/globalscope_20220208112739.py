# Global scope :

from ast import Global


l = 100


def func1(n):
    # Now if we want to change the value of global var  , then :
    global l
    # l = 9   # Local variable    first the program will try to find the local variable then the global variable
    l += 90    # changing the val of global var
    print(l)
    print(n, "I am func1")


func1("hello there")
# The local variable is not accessible outside the fucntion
