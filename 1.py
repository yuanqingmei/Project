def mysum(*args):
    i = 0
    for x in args:
        i += x
        print(x)
    return i
print(mysum(1, 2, 3, 4)) # 10
print(mysum(10, 20, 30)) # 60