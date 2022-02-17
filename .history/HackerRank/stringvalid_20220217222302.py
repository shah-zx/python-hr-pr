if __name__ == '__main__':
    s = input()
    
print(any([(s.isalnum() for i in s)]))
print(any([(s.isalpha() for i in s)]))
print(any([(s.isdigit() for i in s)]))
print(any([(s.islower() for i in s)]))
print(any([(s.isupper() for i in s)]))
