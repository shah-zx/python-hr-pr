# Bsics of file input and output 

# Hard disk  , RAM 

# r -  for reading - default
# , w - writing files , x - create file if it does'nt exists , a - append , t - "Text mode"  b - "binary mode" , + mode - for updation ( read and write)


f = open("F:\Python Programs\Learnig path\shahnawaz.txt" , "rt")   # Openin the file in read mode 

# Reading the file :

content = f.read(5)   # This will read 5 first characters 
print(content)
f.close()

for line in content:
    




