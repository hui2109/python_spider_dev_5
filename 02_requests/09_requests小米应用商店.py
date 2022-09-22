import requests
from lxml import etree

url = 'https://app.mi.com/catTopList/0?page=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
tree = etree.HTML(response.content.decode('utf-8'))
app_list = tree.xpath('//ul[@class="applist"]//h5/a/@href | //ul[@class="applist"]//h5/a/text()')
app_dict = {}

for i in range(0, len(app_list), 2):
    link = app_list[i]
    app_name = app_list[i + 1]
    rank = int(i / 2 + 1)
    app_dict[app_name] = {
        '排名': rank,
        '链接': 'https://app.mi.com/'+link
    }

print(app_dict)
