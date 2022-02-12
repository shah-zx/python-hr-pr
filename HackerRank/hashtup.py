# i = int(input())
# tup = ()

# for n in i:
#    h =  int(input())
#    tup.append(h)
   
# print(hash(tup))

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    k = hash(integer_list)
    print(k)
    print(type(integer_list))
    
    
    