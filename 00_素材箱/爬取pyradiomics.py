import pymysql
import requests
from lxml import etree

db = pymysql.connect(user='root', password='182182aA', host='localhost', port=3306, charset='utf8', database='test1')
cursor = db.cursor()

url = 'https://pyradiomics.readthedocs.io/en/latest/features.html'
session = requests.Session()
session.headers[
    'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

response = session.get(url)
tree = etree.HTML(response.content.decode('utf-8'))
method_names = tree.xpath('//div[@class="section"]/h2/text()')
sections = tree.xpath('//div[@class="section" and contains(@id, "module")]')
mf_dict = {}

for i in range(len(sections)):
    feature_names = sections[i].xpath('.//dd/p/strong/text()')
    for names in feature_names:
        try:
            sql = f'insert into feature values("{method_names[i]}","{names}")'
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

cursor.close()
db.close()
