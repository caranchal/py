from os import strerror
import string
try:
    lines = 0
    s = open("C:/Users/Мк/Desktop/text.txt", "rt", encoding="UTF-8")
    for line in s:
        lines += 1

    print("количество строк",lines)
except IOError as err:
    print("I/O eror occured", strerror(err.errno))
