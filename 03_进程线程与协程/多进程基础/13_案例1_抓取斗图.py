import os.path
import random
import re
import time
import requests
import multiprocessing
from lxml import etree
import urllib.request as req


def get_image_url(url, pages):
    session = requests.Session()
    session.headers[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    response = session.get(url)

    tree = etree.HTML(response.content.decode('utf-8'))
    image_urls = tree.xpath('//img[@referrerpolicy="no-referrer"]/@data-original')

    for i in range(1, len(image_urls) // 2 + 1):
        image_url = image_urls[i - 1]

        prefix = multiprocessing.current_process().name + f'_第{pages}页_' + str(i)
        suffix = re.search(r'\.[a-z]{3,4}$', image_url).group(0)
        if suffix != '.null':
            image_name = prefix + suffix
        else:
            image_name = prefix + '.jpg'

        if not os.path.exists('../00_素材箱/斗图网'):
            os.makedirs('../00_素材箱/斗图网')
        req.urlretrieve(image_url, f'../00_素材箱/斗图网/{image_name}')

        time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    # try:
    #     t1 = time.time()
    #     pool = multiprocessing.Pool(2)
    #     for i in range(1, 4):
    #         url = f'https://www.pkdoutu.com/photo/list/?page={i}'
    #         pool.apply_async(get_image_url, args=(url, i))
    #     pool.close()
    #     pool.join()
    #
    #     t2 = time.time()
    #     print('斗图网的图片爬取完毕', '耗时：', string(t2 - t1))
    # except Exception as e:
    #     print(e)

    t1 = time.time()
    pool = multiprocessing.Pool(2)
    for i in range(1, 4):
        url = f'https://www.pkdoutu.com/photo/list/?page={i}'
        pool.apply_async(get_image_url, args=(url, i))
    pool.close()
    pool.join()

    t2 = time.time()
    print('斗图网的图片爬取完毕', '耗时：', str(t2 - t1))
