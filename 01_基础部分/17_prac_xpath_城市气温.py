from lxml import etree

tree = etree.HTML(open('../00_素材箱/匹配天气.html', 'r', True, 'utf-8').read())
conMidtab = tree.xpath('//div[@class="hanml"]/div[@class="conMidtab"][1]')
tables = conMidtab[0].xpath('./div[@class="conMidtab2"]/table')
weather_info_list = []

for table in tables:
    trs = table.xpath('.//tr')
    for tr in trs[2:]:
        tds = tr.xpath('./td')
        if tr == trs[2]:
            city = tds[1].xpath('./a/text()')[0]
            high_temp = tds[4].xpath('./text()')[0]
        else:
            city = tds[0].xpath('./a/text()')[0]
            high_temp = tds[3].xpath('./text()')[0]
        weather_info_list.append({'city': city, 'high_tem': high_temp})

print(weather_info_list)
