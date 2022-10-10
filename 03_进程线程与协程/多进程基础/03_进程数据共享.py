from multiprocessing import Process

# 全局变量在进程中 不能共享
num = 10


def run():
    print("我是子进程的开始")
    global num
    num += 1
    print(num)
    print("我是子进程的结束")


if __name__ == "__main__":
    # 在创建子进程时对全局变量做了一个备份,父进程中num变量与子线程中的num不是一个变量
    p = Process(target=run)
    p.start()
    p.join()

    # run()

    print(num)
