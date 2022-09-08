from os import strerror
try:
    count = 0
    s = open("C:/Users/Мк/Desktop/text.txt", "rt", encoding="UTF-8")
    char = s.read(1)
    while char != "":
        print(char, end="")
        count += 1
        char = s.read(1)
    s.close()
    print("\n\nсимволов файле", count)
except IOError as err:
    print("I/O eror occured", strerror(err.errno))
