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
