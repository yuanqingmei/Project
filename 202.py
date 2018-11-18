def accum(list1, init=0):
    nsum = init
    for x in list1:
        nsum += x
    return nsum

def accum1(list1, init=0, num = -1):   #累加一个表里前num项的值，参数num为-1时表示全累加
    nsum = init
    if num == -1:
        num = len(list1)
    for i in range(num):
        # print(i)
        nsum += list1[i]
    return nsum

a = accum([1,2,3])
b = accum([5,7,10],a)
print(a,b)

l1 = [x for x in range(100)]
print(l1)
c = accum1(l1,3)
print(c)
d = accum1(l1,10, 6)
print(d)
e = accum1(l1,num = 6)
print(e)
f = accum1(l1)
print(f)