def poly(x):
    return 2*x ** 2 - 4*x - 2
def printf(args, fun):
    for i in args:
        print(f"(",i,")=",fun(i), sep="")
if __name__ == "__main__":
    printf([i for i in range(-5,5)],poly)
    printf([i for i in range(-5, 5)], lambda i: 2*i ** 2 - 4*i - 2)
