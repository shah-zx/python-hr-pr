# Global scope :

l = 100

def func1(n):
    l = 9   # Local variable
    print(l)
    print(n , "I am func1")
    
func1("hello there")

