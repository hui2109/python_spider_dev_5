from lxml import etree

tree = etree.HTML(open('../00_素材箱/大学排名.html', 'r', True, 'utf-8').read())

rank_home = tree.xpath('//tr[@class="odd"]/td[1]/center/text() | //tr[@class="even"]/td[1]/center/text()')
rank_outdoor = tree.xpath('//tr[@class="odd"]/td[2]/center/text() | //tr[@class="even"]/td[2]/center/text()')
uni_name = tree.xpath('//tr[@class="odd"]/td[3]/a/text() | //tr[@class="even"]/td[3]/a/text()')

university_info = {}
for i in range(len(rank_home)):
    university_info[uni_name[i]] = [{'国内排名': rank_home[i]},
                                    {'世界排名': rank_outdoor[i]}]

print(university_info)
