# n = int(input())

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
ws = 0
for i in student_marks[query_name]:
    ws = ws + i
    print("{0:.2f}".format(ws/3))





