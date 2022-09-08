from os import strerror
import shutil
try:
    s = open("C:/Users/Мк/Desktop/text.txt", "rt", encoding="UTF-8")
    s.readline()
    s.write(1)
    shutil.copyfile('text.txt', "text1.txt")
except IOError as err:
    print("I/O error", strerror(err.errno))
    print(char)



