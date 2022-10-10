import time
import threading


def run1():
    # 获取线程名字
    print("启动%s子线程……" % threading.current_thread().name)
    for i in range(5):
        print("lucky is a good man")
        time.sleep(1)


def run2(name, word):
    print("启动%s子线程……" % threading.current_thread().name)
    for i in range(5):
        print("%s is a %s man" % (name, word))
        time.sleep(1)


if __name__ == "__main__":
    t1 = time.time()
    # 主进程中默认有一个线程，称为主线程(父线程)
    # 主线程一般作为调度而存在，不具体实现业务逻辑

    # 创建子线程
    # name参数可以设置线程的名称，如果不设置按顺序设置为Thread-n
    th1 = threading.Thread(target=run1, name="th1")
    th2 = threading.Thread(target=run2, args=("lucky", "nice"), name='th2')

    # 启动
    th1.start()
    th2.start()

    # 等待子线程结束
    th1.join()
    th2.join()

    t2 = time.time()
    print("耗时：%.2f" % (t2 - t1))
