def append1(a,b=[]):
    for i in range(5):
        b.append(a)
    print(b)
    return b

def append2(a,b=None):
    if b is None:
        b = []
    for i in range(5):
        b.append(a)
    print(b)
    return b

def append3(a,b=[]):
    b = list(b)
    for i in range(5):
        b.append(a)
    print(b)
    return b

append1(1,[])
append1(1)
print(append1(2))

append2(1,[])
append2(1)
print(append2(2))

append3(1,[])
append3(1)
print(append3(2))