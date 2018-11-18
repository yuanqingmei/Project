def rev(list1):              #反转表中元素的函数
    if not isinstance(list1, list):
        return
    for i in range(len(list1)//2):
        list1[i],list1[-i-1]=list1[-i-1],list1[i]

a1 = [x for x in range(7)]
a2 = [x for x in range(10)]

print("Original:", a1)
rev(a1)
print("After rev:", a1)

print("Original:", a2)

rev(a2)
print("After rev:", a2)