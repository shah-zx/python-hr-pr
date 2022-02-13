from cv2 import sort


u = int(input())

li = []
grade = []


for i in range(0,u):
    n = input()
    it = float(input())
    li.append([n , it])
    grade.append(it)

sorted(set(grade))    # Soritng our grade list

k = (grade[1])

for it in li:
    if(it == k):
        print(n)
        
        
        




    


    