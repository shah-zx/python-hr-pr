from curses.ascii import islower, isupper


n = input()

for i in n:
    if (i.isupper):
        print(i.tolower())
    else:
        print(i.toupper())
        
        
        
print(n)

