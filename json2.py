import bz2
import gzip
import ujson as json
class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
class Test2:
    __slots__ = ["a", "b"]
    def __init__(self,a,b):
        self.a = a
        self.b = b
def to_json(obj):
    if isinstance(obj, Test):
        result = obj.__dict__
        result["className"] = obj.__class__.__name__
        return result

obj1 = Test(123,"asd")
print(obj1.__dict__)
obj2 = json.dumps(obj1)
with open("test1.json", "w", encoding="utf-8")as fh:
    fh.write(json.dump(obj1, default = to_json, ensure_ascii= False, indent=4))
newObj = json.dumps(obj1, default = to_json, indent = 4)
obj2 = json.loads(newObj)
print(obj2)
compress = bz2.compress(obj2)
