import requests
from lxml import etree

url = 'https://cang.cngold.org/c/2022-06-14/c8152503.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
tree = etree.HTML(response.content.decode('utf-8'))
table = tree.xpath('//table[@border="1"]')[0]
td = table.xpath('.//td/text()')[3:]
table_dict = {}

for i in range(0, len(td), 3):
    table_dict[td[i]] = [
        {'品相': td[i + 1]},
        {'价格': td[i + 2]}
    ]

print(table_dict)
