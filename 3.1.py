def bad():
    raise ZeroDivisionError#симулирует ошибку
try:
    bad()
except ArithmeticError:
    print("a-a-a-a-a-a-a-a-")
print("end")