from lxml import etree

with open('../00_素材箱/豆瓣.html', 'r', True, 'utf-8') as f:
    tree = etree.HTML(f.read())
all_a = tree.xpath('//a')

print(etree.tostring(all_a[0], encoding='utf-8').decode('utf-8'))
