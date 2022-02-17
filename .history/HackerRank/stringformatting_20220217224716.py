def print_formatted(number):
    # your code goes here
    for i in range(0, number+1):
        print(i, end=" ")
        print(oct(i), end=" ")
        print(hex(i), end=" ")
        print(bin(i))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
