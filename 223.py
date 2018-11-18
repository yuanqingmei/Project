def fib(n):
    fibs = {0:0,1:1}     #初始字典，前两项是  fibs[0]=0 和 fibs[1]=1
    def fib0(k):
        if k in fibs:
            return fibs[k]
        fibs[k] = fib0(k-2) + fib0(k-1)
        return fibs[k]
    return fib0(n)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(10))
print(fib(50))
print(fib(100))
print(fib(200))
print(fib(1000))
print(fib(1968))     #只能计算到1968，而计算到1969时，报错