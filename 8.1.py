def f(b):
    b = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            b = b+1
        if (b <= 0):
            print("число простое")
        else:
            print("число не простое")
        return b
a = int(input("число"))
print(f(4))