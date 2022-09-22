import requests
from lxml import etree
import random
import time

'''
https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

rank = 0
movie_info = []

# 设置要抓取的页数
for i in range(0, 10):
    url = f'https://movie.douban.com/top250?start={i * 25}&filter='
    response = requests.get(url, headers=headers)
    tree = etree.HTML(response.content.decode('utf-8'))

    movie_title = tree.xpath('//div[@class="hd"]/a/span[1]/text()')
    for j in movie_title:
        rank += 1
        movie_info.append({'电影排名': rank, '电影名称': j})

    print(movie_info)

    time.sleep(random.randint(1, 5))
