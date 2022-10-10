import threading

Lock = threading.Lock()
i = 1


def fun1():
    global i
    if Lock.acquire():  # 判断是否上锁  锁定成功
        for x in range(1000000):
            i += x
            i -= x
        Lock.release()
    print('fun1-----', i)


def fun2():
    global i
    if Lock.acquire():  # 判断是否上锁  锁定成功
        for x in range(1000000):
            i += x
            i -= x
        Lock.release()
    print('fun2----', i)


t1 = threading.Thread(target=fun1)

t2 = threading.Thread(target=fun2)

t1.start()
t2.start()

t1.join()
t2.join()

print('mian----', i)
