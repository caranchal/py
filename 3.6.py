def powof2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *=2

for v in powof2(10):
    print(v)
list1 = [x for x in powof2(10)]
print(list)
list2 = list(powof2(10))
print(list2)


def Fib(n):
    p1 = p2 = 1
    for i in range(n):
        if i in [0,1]:
            yield 1
        else:
            n = p1 + p2
            p2,p1 = p1 , n
            yield n
fibsChels = list(Fib(10))
print(fibsChels)
