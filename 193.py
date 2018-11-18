from time import time
from random import random
def test1(n):
    t = time()
    rands = []
    for i in range(n):
        rands = rands + [random()]
    print("Test1:",str(time()-t) + "s")

def test2(n):
    t = time()
    rands = []
    for i in range(n):
        rands.insert(0,random())
    print("Test2:",str(time()-t) + "s")

def test3(n):
    t = time()
    rands = []
    for i in range(n):
        rands.append(random())
    print("Test3:",str(time()-t) + "s")

def test4(n):
    t = time()
    rands = [random() for i in range(n)]
    print("Test4:",str(time()-t) + "s")

test1(100000)
test2(100000)
test3(100000)
test4(100000)