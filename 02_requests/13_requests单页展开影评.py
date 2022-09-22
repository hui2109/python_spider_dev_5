import requests
from lxml import etree
import random
import time

"""
1. 抓取单页影评
2. 抓取单页 展开的影评
3. 抓取单页当前影评的详情页
4. 抓取多页 展开的影评及详情页
https://movie.douban.com/j/review/14659381/full
https://movie.douban.com/j/review/14661497/full
"""

url = 'https://movie.douban.com/review/best/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
tree = etree.HTML(response.content.decode('utf-8'))
review_info = []

mains = tree.xpath('//div[@class="main review-item"]')
for main in mains:
    review_title = main.xpath('.//h2/a/text()')[0]
    review_id = main.xpath('.//div[contains(@id,"review_")]/@data-rid')[0]

    lr_url = f'https://movie.douban.com/j/review/{review_id}/full'
    lr_response = requests.get(lr_url, headers=headers)
    html = lr_response.json()['html']
    review_info.append({'影评标题': review_title, '影评长内容': html})
    time.sleep(random.randint(1, 5))

print(review_info)
