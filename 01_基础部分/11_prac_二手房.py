from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open('../00_素材箱/广州二手房.html', 'r', True, 'utf-8'), 'lxml')
house_data_list = []
for clearfix in soup.select('div.esfRoomlists > div.house-item.house-itemB.clearfix'):
    title = clearfix.h4.a.string

    house_name = clearfix.select('div.item-info.fl > p.house-name > a')[0].string
    house_type = clearfix.select('div.item-info.fl > p.house-name > span')[1].string
    house_size = clearfix.select('div.item-info.fl > p.house-name > span')[3].text

    house_floor = clearfix.select('div.item-info.fl > p.house-txt > span')[0].string
    house_orientation = clearfix.select('div.item-info.fl > p.house-txt > span')[1].string
    house_decoration = clearfix.select('div.item-info.fl > p.house-txt > span')[2].string
    house_age = clearfix.select('div.item-info.fl > p.house-txt > span')[3].string

    house_region1 = clearfix.select('div.item-info.fl > p.house-txt')[1].select('a')[0].string
    house_region2 = clearfix.select('div.item-info.fl > p.house-txt')[1].select('a')[1].string
    house_region = house_region1 + '-' + house_region2
    _house_location = clearfix.select('div.item-info.fl > p.house-txt')[1].text

    total_price = clearfix.select('div.item-pricearea.fr > p.price-nub.cRed > span')[1].string + '万'
    _price_per_unit = clearfix.select('div.item-pricearea.fr > p.price-txt')[0].string
    _neighborhood_average_price = clearfix.select('div.item-pricearea.fr > p.price-txtB')[0].string

    # 下面开始处理字符串
    house_location = re.search(r'\xa0(.+)\n', _house_location).group(1)
    price_per_unit = re.search(r'(\d+)元/平\n', _price_per_unit).group(1) + '元/平'
    neighborhood_average_price = re.search(r'(\d+)元/平\n', _neighborhood_average_price).group(1) + '元/平'
    house_data_list.append([{'简介': title},
                            {'小区名': house_name},
                            {'户型': house_type},
                            {'大小': house_size},
                            {'楼层': house_floor},
                            {'朝向': house_orientation},
                            {'装修': house_decoration},
                            {'房龄': house_age},
                            {'地区': house_region},
                            {'地址': house_location},
                            {'总价': total_price},
                            {'单价': price_per_unit},
                            {'小区均价': neighborhood_average_price}])

print(house_data_list)
