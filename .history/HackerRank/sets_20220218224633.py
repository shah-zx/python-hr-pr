s = set([])
u = int(input())


for i in range(1, u):
    j = int(input())
    s.add(j)

sum = 0
for n in s:
    sum = sum + n

rem = sum / u
print(rem)
