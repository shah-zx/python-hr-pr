# from curses.ascii import islower, isupper


# n = input()

# for i in n:
#     if (i.isupper):
#         print(i.tolower())
#     else:
#         print(i.toupper())
        
        
        
# print(n)


def print_full_name(first, last):
    # Write your code here
    return f"Hello {first}{last}! You just delved into python."

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)