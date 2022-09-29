def decor_func(func):
    def wrap():
        print("начинаем обёртку")
        print(f"оборачиваем функцию{func}")
        print("выполняем оборачивание функции")
        func()
        print("выходим из обёртки")
    return wrap
@decor_func
def fircs_func():
    print("первая функция")
fircs_func()