def print_formatted(number):
    # your code goes here
    for i in range(0,number+1):
        print(i)
        print(oct(i))
        print(hex(i))
        print(bin(i))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)