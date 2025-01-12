import os
import random
import ssl
import time
import urllib.request as req

import requests
from lxml import etree

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context


def get_html(url: str, headers: dict, cookies: dict):
    response = requests.get(url, headers=headers, cookies=cookies)
    # print(response.content.decode('utf-8'))
    return etree.HTML(response.content.decode('gbk'))


def write_image(tr, headers, cookies):
    tree = tr
    detail_url = tree.xpath('//ul[@class="clearfix"]//a/@href')[1:-1]
    image_name = tree.xpath('//ul[@class="clearfix"]//a//img/@alt')

    image_detail_url_name = dict()

    for i in range(len(detail_url)):
        image_detail_url_name[image_name[i]] = 'https://pic.netbian.com' + detail_url[i]

    for k, v in image_detail_url_name.items():
        detail_tree = get_html(v, headers, cookies)
        srcs = detail_tree.xpath('//div[@class="photo-pic"]//img/@src')
        for src in srcs:
            image_url = 'https://pic.netbian.com' + src

            if not os.path.exists('../00_素材箱/彼岸图网'):
                os.mkdir('../00_素材箱/彼岸图网')

            if not os.path.exists(f'../00_素材箱/彼岸图网/{k}.jpg'):  # 没有图片时才写入
                image_response = requests.get(image_url, headers=headers, cookies=cookies)
                with open(f'../00_素材箱/彼岸图网/{k}.jpg', 'wb') as file:
                    file.write(image_response.content)

                print(f'图片【{k}】下载成功！')
                time.sleep(random.randint(1, 5))


def main():
    pages = input('请输入您想爬取的页数（按 q+回车 退出）：')

    if pages == 'q':
        print('您已成功退出！')
        return None

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    cookies = {
        'cf_clearance': "LJVeDiSAleCNVrWK2hTVdG88gaNaqEOnP7Lm99Ocov8-1736690601-1.2.1.1-Rw0vNJuyFCwOX89SdilDcWzETWsvtKGw57qlGfLct115bhleRnG46Hyu7X6nQ7vi7IuxGaW1RkQlthqVAC_iZRQt5EGFEk__T4XE0YZlJ3YsRnJI46ZdRJSd4SjlfPoqW.LtSHjDIHSrP0i6lLW3zRjrO4.ZQ70YeCF1daKGkiEOiyk_0Mw6G8JV.X7C01C6c8JmK_3H2KKyw7UEYTsDDzO3FKXK1KW7VhNVUsN3oK.XlhuymKEatHnT6eyUZUoaY4eLrMs2TlU.g2foBlhtsK.bCUGvSBXWywUw3.6NQC8_08cs7z.LP7dPhbZ3szkp3BBNJcUG8L7g0US5qeJLvw"
    }  # 会过期！

    for i in range(1, int(pages) + 1):
        if i != 1:
            url = f'https://pic.netbian.com/index_{i}.html'
        else:
            url = 'https://pic.netbian.com/index.html'

        tr = get_html(url, headers, cookies)

        print(f'开始下载第{i}页的内容')
        write_image(tr, headers, cookies)
        print(f'第{i}页内容下载完毕！')

    main()


if __name__ == '__main__':
    main()
