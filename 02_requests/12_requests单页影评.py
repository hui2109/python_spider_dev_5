import requests
from lxml import etree

"""
1. 抓取单页影评
2. 抓取单页 展开的影评
3. 抓取单页当前影评的详情页
4. 抓取多页 展开的影评及详情页
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
    movie_cover = main.xpath('.//a[@class="subject-img"]/img/@src')[0]
    review_short = main.xpath('.//div[@class="short-content"]/text()')[0].rstrip('(').strip()

    review_info.append({'影评标题': review_title, '影评封面': movie_cover, '影评短内容': review_short})

print(review_info)
