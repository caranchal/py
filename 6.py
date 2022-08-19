import string
import random
a = string.ascii_letters
b = string.ascii_lowercase#маленькие буквы
c = string.ascii_uppercase#большие буквы
d = string.digits#числовые символы
e = string.punctuation
f = string.whitespace#все разделительные знаки
g = string.printable
UserPass = "".join(random.sample((string.printable + string.digits + string.ascii_letters), 12))
print(UserPass)
