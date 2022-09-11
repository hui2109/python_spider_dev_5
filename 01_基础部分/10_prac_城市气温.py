from bs4 import BeautifulSoup

soup = BeautifulSoup(open('../00_素材箱/匹配天气.html', 'r', True, 'utf-8'), 'lxml')
weather_info_list = []
for conMidtab2 in soup.select('div.hanml > div.conMidtab')[0].select('div.conMidtab2'):
    # 索引为2的元素单独提取信息
    tr = conMidtab2.select('table > tr')[2]
    city = tr.select('td')[1].a.string
    high_tem = tr.select('td')[4].string
    weather_info_list.append({'city': city, 'high_tem': high_tem})

    for tr in conMidtab2.select('table > tr')[3:]:
        city = tr.select('td')[0].a.string
        high_tem = tr.select('td')[3].string
        weather_info_list.append({'city': city, 'high_tem': high_tem})

print(weather_info_list)
