def time_stamp(iters):
    def decor(func):
        import time
        def wrap(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                retVal = func(*args, **kwargs)
                end = time.time()
                timeReg = end - start
                timeReg = float("{:.2f}".format(timeReg))
                print(f"время выполнения запроса:{timeReg} секунд(ы)")
                total += timeReg
            print("среднее время выполнения запроса:{} секунд(ы)".format(total/iters))
            return retVal
        return wrap
    return decor
@time_stamp(20)
def get_webPage(url):
    import requests
    webPage = requests.get(url)
    return webPage.text

web = get_webPage("https://google.com")
print(web)