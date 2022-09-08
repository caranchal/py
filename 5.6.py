list1 = []
for i in range (8):
    list1.append(1 if i % 2 == 0 else 0)
print(list1)
list2 = [1 if i % 2 == 0 else 0 for i in range(8)]
print(list2)
