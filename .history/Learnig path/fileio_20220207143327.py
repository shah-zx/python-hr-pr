# Bsics of file input and output 

# Hard disk  , RAM 

# r -  for reading - default
# , w - writing files , x - create file if it does'nt exists , a - append , t - "Text mode"  b - "binary mode" , + mode - for updation ( read and write)


f = open("F:\Python Programs\Learnig path\shahnawaz.txt" , "rt")   # Openin the file in read mode 

# Reading the file :

# content = f.read()   # This will read 5 first characters 
# print(content)
# f.close()


# Reading the files using readline()

print(f.readline())

print(f.readline())



# We can read the lines as :

for line in f:
    print(line , end = " ")


f.close()



