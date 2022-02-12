d1 = {}
print(type(d1))
# key value pairs
d2 = {"Shahnawaz" : "GHRIBM" , "Hamza" : "IIITD" , "Rahul" : "CU"}
 
 # Accessing the values through the keys :
 
# priint(d2["Hamza"])
         
# Dictionary in dictonary

d2 = {"Shahnawaz" : "GHRIBM" , "Hamza" : {"1" : "IITB" , "2" : "IITK" , "3" : "IIITD" , "4" : "NITJ"} , "Rahul" : "CU"}

# print(d2["Hamza"]["DTU"])

# Keys are immutable

# We can add items to this tuple as well 

# d2["Shital"] = "IITB"

# print(d2)

# Removing from tuple

# del d2["Rahul"]

# print(d2)

# print(d2["Hamza"]["4"])

# print(d2.copy()) 

d4 = d2   # d4 is a pointer to d2 and any change done in d4 will reflect in d2

del d4["Rahul"]

d2.update({"Harry" : "DTU"})

print(d2)

d2.keys()

d2.items()


# A simple program :

print("-------------Welcome to JOSAA-------------")

print("You have four choices (1-4) - please choose one")

Preferences = {"1" : "IITB" , "2" : "IITK" , "3" : "IIITD" , "4" : "NITK"}








          

