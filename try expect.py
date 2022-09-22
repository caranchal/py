def printExeption(thisClass, attach = 0):
    if attach > 0:
        print("|" * (attach - 1), end = "")
    if attach > 0:
        print("+---", end="")
    print(thisClass.__name__)
    for sub in thisClass.__subclasses__():
        printExeption(sub, attach + 1)
printExeption(BaseException)