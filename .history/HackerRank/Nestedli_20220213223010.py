from cv2 import sort


u = int(input())

li = []
grade = []


for i in range(0, u):
    n = input()
    it = float(input())
    li.append([n, it])
    grade.append(it)

sorted(set(grade))    # Soritng our grade list

k = (grade[1])
name = []
for val in li:
    if(k == val[1]):
        name.append(val[0])

print(name)
name.sort()
print(name)
for nm in name:
    print(nm)
