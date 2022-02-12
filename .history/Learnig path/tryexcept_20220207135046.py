num1 = input()
num2 = input()

try:
    print("The addition of the two numbers is : "  , int(num1) + int(num2))
except Exception as e :
    print("This is the important line")
    
# Try and except handles the error  ,  as if the user enters some wrong inputs , the code will not stop , the nesxt block of code will exceute


