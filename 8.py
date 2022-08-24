import re
login = input("введите свой логин:")
password = input("введите пароль:")
while True:
    if password != re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$'):
        print("")
        break
    else:
        print("ненадёжный пароль")
        return password







