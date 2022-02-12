def minus(x, y): return x - y    # A shortcut fo writing the fumction


print(minus(7, 4))


def a_first(a):
    return a[1]


a = [[1, 4][5, 6][7, 8]]

a.sort(key=a_first)

print(a)
