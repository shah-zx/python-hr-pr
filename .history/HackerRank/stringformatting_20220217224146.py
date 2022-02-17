def print_formatted(number):
    # your code goes here
for i in range(0,number):
    print(number)
    print(oct(number))
    print(hex(number))
    print(bin(number))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)