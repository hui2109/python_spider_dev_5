import multiprocessing

queue = multiprocessing.Queue()  # 创建 队列，特点：先进先出


# 如果在子进程 和主进程 之间 都压入了数据 那么在主进程 和 子进程 获取的就是 对方的数据
def fun(myque):
    # print(id(myque)) #获取当前的队列的存储地址  依然是拷贝了一份
    print(id(myque))
    myque.put(['a', 'b', 'c'])  # 在子进程里面压入数据
    print("子进程获取", myque.get())  # 获取队列里面的值
    print("子Queue大小", myque.qsize())  # 获取队列里面值的数量


if __name__ == '__main__':
    print(id(queue))
    queue.put([1, 2, 3, 4, 5])  # 将列表压入队列  如果主进程也压入了数据 那么在主进程取的就是在主进程压入的数据 而不是子进程的
    p = multiprocessing.Process(target=fun, args=(queue,))
    p.start()
    p.join()
    print("主进程获取", queue.get())  # 在主进程进行获取
    print("主Queue大小", queue.qsize())  # 获取队列里面值的数量
    # print("主进程获取", queue.get())  # 在主进程进行获取
    print("主进程获取", queue.get(block=True, timeout=100))  # 在主进程进行获取
