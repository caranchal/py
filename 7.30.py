def ncht(x,y):
    lst = [i for i in range(x,y+1) if not i % 2 == 0 ]
    return lst
a = int(input('от'))
b = int(input("до"))
result = ncht(a, b)
print(result)