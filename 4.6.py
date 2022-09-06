list1 = []
for i in range (8):
    list1.append(i ** 10)

list2 = [i ** 10 for i in range(8)]

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
print(list2)
print(list1)