import time
from multiprocessing import Process


def run1():
    for i in range(7):
        print("lucky is a good man")
        time.sleep(1)


def run2(name, word):
    for i in range(5):
        print("%s is a %s man" % (name, word))
        time.sleep(1)


if __name__ == "__main__":
    t1 = time.time()

    # 主进程主要做的是调度相关的工作，一般不负责具体业务逻辑
    # 创建两个进程分别执行run1、run2
    p1 = Process(target=run1)
    p2 = Process(target=run2, args=("lucky", "cool"))

    # 启动两个进程
    p1.start()
    p2.start()

    # 等待两个子进程执行完毕
    p1.join()
    p2.join()

    # 查看耗时
    t2 = time.time()
    print("耗时：%.2f" % (t2 - t1))
