# Pool类：进程池类
from multiprocessing import Pool
import time
import random
import multiprocessing


def run(index):
    print('CPU number:' + str(multiprocessing.cpu_count()))
    print("子进程 %d 启动" % index)
    t1 = time.time()
    time.sleep(random.random() * 5 + 2)
    t2 = time.time()
    print("子进程 %d 结束，耗时：%.2f" % (index, t2 - t1))


if __name__ == "__main__":
    print("启动主进程……")

    # 创建进程池对象
    # 由于pool的默认值为CPU的核心数，假设有4个核心，至少需要5个子进程才能看到效果
    # Pool()中的值表示可以同时执行进程的数量
    pool = Pool(2)
    for i in range(1, 7):
        # 创建子进程，并将子进程放到进程池中统一管理
        pool.apply_async(run, args=(i,))

    # 等待子进程结束
    # 关闭进程池：在关闭后就不能再向进程池中添加进程了
    # 进程池对象在调用join之前必须先关闭进程池
    pool.close()
    # pool对象调用join，主进程会等待进程池中的所有子进程结束才会继续执行主进程
    pool.join()

    print("结束主进程……")
