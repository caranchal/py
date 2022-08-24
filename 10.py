arr2 = [1,2,3]
arr3 = [f"user{i}" for i in range(8) if i % 2 ==0] #четные числа
print(arr3)
arr4 = [i for i in arr3 if i!="user1" and i!="user7"]#условие где в ответе не может быть пользователя 1 и пользователя 7
print(arr4)
print(len(arr2))#f
print(max(arr2))
print(min(arr2))
print(sum(arr2))
print(sorted(arr2))#сортировка списка
arr2.append(12)#добавления числа в список
arr2.insert(0, "admin")#добавление элемента в определёный индекс списка
print(arr2)
arr3.extend(arr4)#добавления списка в список
print(arr3)
arr3.clear()#очистка списка
print(arr3)