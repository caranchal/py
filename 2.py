number = int(input("число"))
a = 0
b = 0
while number > 0:
	if number % 2 == 0:
		a += 1
	else:b +=1
	number = number // 10
print(f"чётные: {a} нечётные: {b}")