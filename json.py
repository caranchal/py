import ujson
strok = "string"
integ = 123456
spis = [1,2,3,4]

firstDict = {"first": strok, "second": integ, "third": spis}
print(firstDict)
dumpJs = ujson.dumps(firstDict)
print(dumpJs)
secondDict = ujson.loads(dumpJs)
print(secondDict)
with open("upload.json", "w") as upJS:
    ujson.dump(secondDict, upJS)
