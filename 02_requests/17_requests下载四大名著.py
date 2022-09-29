import os.path
import random
import ssl
import time

import requests
from lxml import etree

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context


def get_html(_url, _headers):
    response = requests.get(_url, headers=_headers)
    return etree.HTML(response.content.decode(response.apparent_encoding))


def get_book_name_url(_tree):
    book_name_url_dict = dict()

    book_urls = _tree.xpath('//div[@class="book-item"]/h3/a/@href')
    book_names = _tree.xpath('//div[@class="book-item"]/h3/a/text()')

    for i in range(len(book_urls)):
        book_name_url_dict[book_names[i]] = 'https://www.shicimingju.com' + book_urls[i]

    return book_name_url_dict


def get_mulu_tile_url(_book_name_url_dict: dict, _headers):
    mulu_tile_url_list = list()

    for book_name, book_url in _book_name_url_dict.items():
        if not os.path.exists(f'../00_素材箱/四大名著/{book_name}'):
            os.makedirs(f'../00_素材箱/四大名著/{book_name}')

        tree = get_html(book_url, _headers)
        mulu_urls = tree.xpath('//div[@class="book-mulu"]//a/@href')
        mulu_titles = tree.xpath('//div[@class="book-mulu"]//a/text()')

        for j in range(len(mulu_urls)):
            mulu_tile_url_list.append({
                book_name: {
                    mulu_titles[j]: 'https://www.shicimingju.com/' + mulu_urls[j]
                }
            })

    return mulu_tile_url_list


def get_content(_mulu_tile_url_list, _headers):
    for k in _mulu_tile_url_list:
        for book_name, mulu in k.items():
            for mulu_title, mulu_url in mulu.items():
                tree = get_html(mulu_url, _headers)
                chapter_content = tree.xpath('//div[@class="chapter_content"]//text()')
                with open(f'../00_素材箱/四大名著/{book_name}/{mulu_title}.txt', 'w', True, 'utf-8') as f:
                    for p in chapter_content:
                        para = str(p).strip()
                        f.write(para + '\n\n')
                    print(f'{book_name}中{mulu_title}下载完毕！')
                time.sleep(random.randint(1, 5))


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    root_url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'

    tree = get_html(root_url, headers)
    book_dict = get_book_name_url(tree)
    mulu_list = get_mulu_tile_url(book_dict, headers)
    get_content(mulu_list, headers)


if __name__ == '__main__':
    main()
