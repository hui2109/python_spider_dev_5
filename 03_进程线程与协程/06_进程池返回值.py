from multiprocessing import Pool
import time


def function(index):
    print('Start process: ', index)
    time.sleep(2)
    print('End process', index)
    return index


if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in range(4):
        result = pool.apply_async(function, (i,))
        # 获取每个子进程的返回值，注意：这样来获取每个进程的返回值 那么就会变成单进程
        # 主进程在这里被阻塞了
        print(result.get())
    print("Started processes")
    pool.close()
    pool.join()
    print("Subprocess done.")
