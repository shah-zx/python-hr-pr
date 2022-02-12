def Leap(n):
    if n % 4 == 0 & n % 100 == 0  & n % 400 == 0:
        print("True")
    else:
        print("False")


n = int(input())
Leap(n)
