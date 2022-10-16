import random
import time

import pymysql
import requests
from lxml import etree


def get_content(url):
    content_response = session.get(url)
    content_tree = etree.HTML(content_response.content.decode('utf-8'))
    title = content_tree.xpath('//article/h1/text()')[0].replace('"', '')
    authors = ', '.join(content_tree.xpath('//article/div[@class="wz_info"]/span[3]/text()')[0].split('：')[1:]).replace(
        '"', '')
    time = content_tree.xpath('//article/div[@class="wz_info"]/span[4]/text()')[0].split('：')[1].replace('"', '')
    content = ''
    for i in content_tree.xpath('//article/div[@class="content"]//text()'):
        if i.strip() != '':
            _i = i.strip().replace('"', '')
            content = content + _i + '\n\n'

    read_url = 'https://www.3dst.cn/e/public/ViewClick/?classid=8&id=1203&addclick=1'
    read_response = session.get(read_url)
    read_number = read_response.content.decode('utf-8').split('\'')[1].replace('"', '')

    return title, authors, time, read_number, content


def write_into_db(data):
    title, authors, time, read_number, content = data
    try:
        sql = f'insert into 励志文章 values(null, "{title}", "{authors}", "{time}", {read_number},"{content}")'
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()


db = pymysql.connect(user='root', password='182182aA', host='localhost', port=3306, charset='utf8', database='test1')
cursor = db.cursor()

session = requests.Session()
session.headers[
    'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
url = 'https://www.3dst.cn/t/lizhigushi/'

response = session.get(url)
tree = etree.HTML(response.content.decode('utf-8'))
href_list = tree.xpath('//li[@class="blogs_list"]/a/@href')
for href in href_list:
    data = get_content(href)
    write_into_db(data)
    time.sleep(random.randint(1, 5))
cursor.close()
db.close()
