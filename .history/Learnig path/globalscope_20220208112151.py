# Global scope :

l = 100

def func1(n):
    l = 9   # Local variable    first the program will try to find the local variable then the global variable 
    print(l)
    print(n , "I am func1")
    
func1("hello there")



