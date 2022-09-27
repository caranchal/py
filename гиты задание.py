import random
class Teacher:
    def __init__(self, a, schoolboy):
        self.a = a
        self.schoolboy = list(schoolboy)
    def __setitem__(self, key, value):
        last = key + 1 - len(self.schoolboy)
        self.schoolboy.extend([None]*last)
class SchoolBoy:
    def __init__(self,a,knowledge):
        self.a = a
        self.knowledge = knowledge
    def __delitem__(self, key):
        self.pop(random.randrange(len(colvoSchoolboy)))
        del self.knowledge[key]

knowledge = SchoolBoy("предметы", ["литература", "физра", "математика", "русский", "физика"])
colvoSchoolboy = Teacher("ученики", ["лера", "даша", "максим", "егор", "богдан"])
print(colvoSchoolboy.schoolboy)
print(colvoSchoolboy.knowledge)