n = int(input())
if n % 2 == 1:
    print("Weird")
elif n >= 2 & n <= 5 & n % 2 == 0:
    print("Not Weird")
elif n >= 6 & n <= 20 & n % 2 == 0:
    print("Weird")
elif n > 20 & n % 2 == 0:
    print("Not Weird")
    pass

    