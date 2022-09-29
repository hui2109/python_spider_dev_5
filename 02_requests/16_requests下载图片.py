import os
import random
import ssl
import time
import urllib.request as req

import requests
from lxml import etree

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context


def get_html(ul: str, hs: dict):
    response = requests.get(ul, headers=hs)
    return etree.HTML(response.content.decode('gbk'))


def write_image(tr, hs):
    tree = tr
    detail_url = tree.xpath('//ul[@class="clearfix"]//a/@href')
    image_name = tree.xpath('//ul[@class="clearfix"]//a//img/@alt')

    image_detail_url_name = dict()

    for i in range(len(detail_url)):
        image_detail_url_name[image_name[i]] = 'https://pic.netbian.com' + detail_url[i]

    for k, v in image_detail_url_name.items():
        detail_tree = get_html(v, hs)
        srcs = detail_tree.xpath('//div[@class="photo-pic"]//img/@src')
        for src in srcs:
            image_url = 'https://pic.netbian.com' + src

            if not os.path.exists('../00_素材箱/彼岸图网'):
                os.mkdir('../00_素材箱/彼岸图网')

            if not os.path.exists(f'../00_素材箱/彼岸图网/{k}.jpg'):  # 没有图片时才写入
                req.urlretrieve(image_url, f'../00_素材箱/彼岸图网/{k}.jpg')
                print(f'图片【{k}】下载成功！')
                time.sleep(random.randint(1, 5))


def main():
    pages = input('请输入您想爬取的页数（按 q+回车 退出）：')

    if pages == 'q':
        print('您已成功退出！')
        return None

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    for i in range(1, int(pages) + 1):
        if i != 1:
            url = f'https://pic.netbian.com/index_{i}.html'
        else:
            url = 'https://pic.netbian.com/index.html'

        tr = get_html(url, headers)

        print(f'开始下载第{i}页的内容')
        write_image(tr, headers)
        print(f'第{i}页内容下载完毕！')

    main()


if __name__ == '__main__':
    main()
