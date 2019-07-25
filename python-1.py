def recursive_func(key):
    if key==1 or key==0:
        return 1
    else:
        return key * recursive_func(key-1)


temp = int(input())

print(recursive_func(temp))