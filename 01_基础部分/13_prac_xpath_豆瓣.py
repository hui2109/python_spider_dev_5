from lxml import etree

# 获取书籍标题及简介，构造为一个字典
book_title_intro_dict = {}
tree = etree.HTML(open('../00_素材箱/豆瓣.html', 'r', True, 'utf-8').read())
book_title = tree.xpath('//div[@class="detail-frame"]/h2/a/text()')
book_intro = tree.xpath('//div[@class="detail-frame"]/p[last()]/text()')

for i in range(len(book_title)):
    book_title_intro_dict[book_title[i]] = book_intro[i].strip()

print(book_title_intro_dict)

# 获取图像链接并写入文件
with open('../00_素材箱/image_xpath.html', 'w', True, 'utf-8') as f:
    for src in tree.xpath('//a[@class="cover"]/img/@src'):
        f.write('<img src=' + str(src) + '/>\n')
