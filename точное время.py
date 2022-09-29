import time
def decorate(func):
    print("*"*6, func(),  "*"*6, sep = "\n")



def timer():

    return time.ctime()
decorate(timer)



