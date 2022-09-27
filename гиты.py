class TestClass:
    def __init__(self, a, lists):
        self.a = a
        self.lists = list(lists)
    def __getitem__(self, item):
        return self.lists[item]
    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("индекс должен быть целым числом")
        if key >= len(self.lists):
            last = key + 1 - len(self.lists)
            self.lists.extend([None]*last)

        self.lists[key] = value
        def __delitem__(self, key):
            del self.lists[key]

obj1 = TestClass("объект", [1,2,3,4,5,6])
print(obj1.lists[0])
obj1[2] = 9
print(obj1[2])
print(obj1.lists)
del obj1[3]
print(obj1.lists)