class Elem:
    #узлы связаного списка
    def __init__(self,item):
        self.item = item
        self.nextItem = None

class Node:
    #связаный список
    def __init__(self):
        self.head = None

    def append(self,newItem):
        newItem = Elem(newItem)
        if self.head is None:
            self.head = newItem
            return self
        lastElem = self.head
        while lastElem.nextItem:
            lastElem = lastElem.nextItem#прописываем ссылки
        lastElem.nextItem = newItem

    def __contains__(self,item):
        lastElem = self.head
        while lastElem:
            if item == lastElem.item:
                return True
        else:
            lastElem = lastElem.nextItem
            return False
    def __getitem__(self,itemIndex):
        lastElem = self.head
        elemIndex = 0
        while elemIndex < itemIndex:
            elemIndex += 1
            lastElem = lastElem.nextItem
            return lastElem.item
    def remove(self,rmItem):
        headItem = self.head
        if headItem.item == rmItem:
            self.head = headItem.nextItem
            headItem = None
            return
        curenItem = self.head
        while curenItem.nextItem:
            if curenItem.nextItem == rmItem:
                temp = curenItem.nextItem
                curenItem.nextItem = temp.nextItem
                del temp
                return
            curenItem = curenItem.nextItem
obj1 = Node()
obj1.append(1)
obj1.append(2)
obj1.append(3)
print(obj1.__contains__(6))
print(obj1.__getitem__(1))
obj1.remove(2)
print(obj1.__contains__(2))
obj1.remove(1)
print(obj1.__contains__(2))
