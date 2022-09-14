from lxml import etree
import re

tree = etree.HTML(open('../00_素材箱/广州二手房.html', 'r', True, 'utf-8').read())
house_data_list = []

house_title = tree.xpath('//h4[@class="house-title"]/a/text()')
house_name = tree.xpath('//p[@class="house-name"]/a/text()')
house_type = tree.xpath('//p[@class="house-name"]/span[2]/text()')
house_size = tree.xpath('//p[@class="house-name"]/span[4]/text()')

house_floor = tree.xpath('//p[@class="house-txt"]/span[1]/text()')
house_orientation = tree.xpath('//p[@class="house-txt"]/span[2]/text()')
house_decoration = tree.xpath('//p[@class="house-txt"]/span[3]/text()')
house_age = tree.xpath('//p[@class="house-txt"]/span[4]/text()')

house_region1 = tree.xpath('//p[@class="house-txt"]/a[1]/text()')
house_region2 = tree.xpath('//p[@class="house-txt"]/a[2]/text()')
_house_location = tree.xpath('//div[@class="item-info fl"]/p[@class="house-txt"][2]/text()')

total_price = tree.xpath('//p[@class="price-nub cRed"]/span[2]/text()')
_price_per_unit = tree.xpath('//p[@class="price-txt"]/text()')
_neighborhood_average_price = tree.xpath('//p[@class="price-txtB"]/text()')

# 下面开始处理字符串
house_location = []
for i in _house_location:
    t1 = i.strip()
    if t1 != '' and t1 != '-':
        house_location.append(t1)

price_per_unit = []
for j in _price_per_unit:
    t2 = j.strip()
    match1 = re.search(r'(\d+)元/平', t2)
    price_per_unit.append(match1.group(1)+'元/平')

neighborhood_average_price = []
for k in _neighborhood_average_price:
    t3 = k.strip()
    match2 = re.search(r'(\d+)元/平', t3)
    neighborhood_average_price.append(match2.group(1)+'元/平')

house_region = []
for i in range(len(house_region1)):
    region = house_region1[i] + '-' + house_region2[i]
    house_region.append(region)

# 开始写入数据
for i in range(len(house_title)):
    house_data_list.append([{'简介': house_title[i]},
                            {'小区名': house_name[i]},
                            {'户型': house_type[i]},
                            {'大小': house_size[i]},
                            {'楼层': house_floor[i]},
                            {'朝向': house_orientation[i]},
                            {'装修': house_decoration[i]},
                            {'房龄': house_age[i]},
                            {'地区': house_region[i]},
                            {'地址': house_location[i]},
                            {'总价': total_price[i]+'万'},
                            {'单价': price_per_unit[i]},
                            {'小区均价': neighborhood_average_price[i]}])

print(house_data_list)
