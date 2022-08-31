def number():
    chislo = list(range(a,b))
    chislo = [i*i for i in range 8 if i % 2 !=0]
    return chislo
    a = int(input("от"))
    b = int(input("до"))
    result = number(a, b)
    print(result)
