s = set([])
u = int(input())


for i in range(0, u):
    j = int(input())
    s.add(j)

sum = 0
d = s.len()
count = 0

for n in s:
    sum = sum + n
    count = count + 1

rem = sum / d
print(rem)
