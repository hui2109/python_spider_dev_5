import multiprocessing

from test1 import PrintNumber


def runner():
    process_pool = multiprocessing.Pool(3)
    test = PrintNumber(12)
    process_pool.apply_async(test.run_task, args=())

    process_pool.close()
    process_pool.join()


if __name__ == "__main__":
    runner()
