for x in (n**2 for n in range(100)):
    if x % 11 ==0:
        print(x)

list2 = [x for x in range(200) if x % 7 ==x % 19 +3]
print(list2)

print([[1 if i ==j else 0 for i in range(10)] for j in range(10)])

print(tuple(i**2 + j for i in range(1,5) for j in range(1,i)))

for z in range(1,1):
    print(z)