def print_names(a,b,c,d):
    print(a,b,c,d)
    
print_names("hamza" , "shanu" , "rahul" , "saurav") 

# In the above given function if we pass more than the given args then it will throw error :

# For that purpose we can use args :

def print_name(*args):
    print(*args)
    
    
    
har = ["hamza" , "shanu" , "rahul" , "saurav" , "shivam" , "kailash"]
print_names(*har)


