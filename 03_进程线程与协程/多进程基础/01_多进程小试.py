import time
from multiprocessing import Process


def run1(name):
    while 1:
        print("%s is a good man" % name)
        time.sleep(1)


def run2():
    while 1:
        print("lucky is a nice man")
        time.sleep(1)


if __name__ == "__main__":
    # 程序启动时的进程称为主进程(父进程)

    # 创建进程并启动
    p = Process(target=run1, args=("lucky",))
    p.start()
    # 主进程执行run2()函数
    run2()
