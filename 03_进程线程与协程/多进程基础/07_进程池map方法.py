import time
from multiprocessing import Pool
import requests
from requests.exceptions import ConnectionError


def scrape(url):
    try:
        print(requests.get(url))
    except ConnectionError:
        print('Error Occurred ', url)
    finally:
        print('URL', url, ' Scraped')
        time.sleep(5)


if __name__ == '__main__':
    pool = Pool(processes=3)
    urls = [
        'https://www.baidu.com',
        'https://www.meituan.com/',
        'https://blog.csdn.net/',
        'https://xxxyxxx.net'
    ]

    # 有一个链接列表，map函数可以遍历每个URL，然后对其分别执行scrape方法
    pool.map(scrape, urls)
