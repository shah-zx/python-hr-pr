d1 = {}
print(type(d1))
# key value pairs
d2 = {"Shahnawaz" : "GHRIBM" , "Hamza" : "IIITD" , "Rahul" : "CU"}
 
 # Accessing the values through the keys :
 
# priint(d2["Hamza"])
         
# Dictionary in dictonary

d2 = {"Shahnawaz" : "GHRIBM" , "Hamza" : {"IIITD" : "1" , "NITK" : "2" , "DTU" : "3" , "NSUT" : "4"} , "Rahul" : "CU"}
# print(d2["Hamza"]["DTU"])

# Keys are immutable

# We can add items to this tuple as well 

d2["Shital"] = "IITB"

print(d2)

# Removing from tuple

del d2["Rahul"]

print(d2)

print(d2["Hamza"][4])

          

