def mysum(*args):
    s = 0
    for x in args:
        print(x)
        s += x
    return s

#a = 1,2,3,4,5,6,7,8,9
a = range(100)
print(mysum(*a))
mysum(1,2,3,4,5,6)

