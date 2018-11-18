def sum1(numbs):
    s = 0
    for i in range(len(numbs)):
        s += numbs[i]
        print(s)
    return s

def sum2(numbs):
    s = 0
    for x in numbs:
        s += x
    return s

def is_in(x,list1):          #用于检查在一个表里是否存在某个元素
    for y in list1:
        if y == x:
            return True
    return False

def count(x,list1):           #用于检查某个元素在一个表里出现的次数
    n = 0
    for y in list1:
        if y == x:
            n += 1
    return n

list1 = list(range(10))
a = sum1(list1)
b = sum2(list1)

print(a,b,list1)

print(is_in(10,list1))

print(count(10,list1))