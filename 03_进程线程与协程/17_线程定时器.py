import threading


def go():
    print("我走了")


# t = threading.Timer(秒数,函数名)
t = threading.Timer(3, go)
t.start()
print('我是主线程的代码')
