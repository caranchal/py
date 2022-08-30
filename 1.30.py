import random
for name in dir(random):
    print(name, end="\n")
def f(x):
    return x * 2
print((f(2)))
print(f("str"))
def f(*args):
    return args
print((f(2,3,4, "dfgdfgdfg")))
print(f("str"))
def f(**kwargs):
    return kwargs
print(f(a=2, b=3,c=4))

