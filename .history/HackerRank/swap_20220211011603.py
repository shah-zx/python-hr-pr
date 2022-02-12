from curses.ascii import islower, isupper


n = input()

for i in n:
    if (i.isupper):
        print(islower(i))
    else:
        print(isupper(i))
        
        
        
print(n)

