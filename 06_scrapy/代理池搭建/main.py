import multiprocessing
import time

from available_ip import main
from get_ip import HGetIp
from test_ip import HTestIp


def runner():
    pool = multiprocessing.Pool(3)
    pool.apply_async(main, args=())
    pool.apply_async(HTestIp().main, args=())
    pool.apply_async(HGetIp().main, args=())

    pool.close()
    pool.join()


if __name__ == '__main__':
    runner()
