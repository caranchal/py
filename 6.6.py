# lambda param: exp
one = lambda : 3
x2 = lambda x: x*x
pwr = lambda x, y: x*y


for i in range(-4,2):
    print(x2(i))
    print(pwr(i,one()))
