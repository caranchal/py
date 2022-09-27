from os import strerror
import string
try:
    symbols = 0
    lines = 0
    s = open("C:/Users/Мк/Desktop/text.txt", "rt", encoding="UTF-8")
    for line in s:
        lines += 1
        symbols += len(line.strip('\n'))


    print("количество строк:",lines)
    print("количество символов:", symbols)
except IOError as err:
    print("I/O eror occured", strerror(err.errno))
