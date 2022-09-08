def maceclosure(param):
    loc = param
    def power(p):
        return p ** loc# возведение в степень
    return power
fkwadr = maceclosure(2)#возведение в квадрат
fcub = maceclosure(3)#возведение в куб
for i in range(6):#количество чисел
    print(i, fkwadr(i), fcub(i))
