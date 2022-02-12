li = ["hary" , "shahnawaz" , "amte" , "pc"]
for it in li:
    print(it)

# List of list iteration 
    
li2 = [["lary" , 10] ,["hary" , 3] , ["mary" , 5] , ["tary" , 2]]    
for item , lollypop in li2:
    print(item ,  "eats this much lolly : "  ,lollypop)
    
    
# Converting the dictionary to a list and then iterating over it 

dict1 = dict(li2)    
for item in dict1.items():   # Gives both key and values 
    print(item)
    
for item in dict1:   # Gives keys only 
    print(item)
    
    
# A simple program :

print("------------- Welcome to lollypop eating competition----------------")
print("Enter the lollypops you ate")
n = int(input())
