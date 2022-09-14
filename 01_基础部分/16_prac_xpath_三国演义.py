from lxml import etree

tree = etree.HTML(open('../00_素材箱/三国演义.html', 'r', True, 'utf-8').read())
text = tree.xpath('//div[@class="book-mulu"]/ul/li/a/text()')
link = tree.xpath('//div[@class="book-mulu"]/ul/li/a/@href')

with open('../00_素材箱/爬取三国演义_xpath.html', 'w', True, 'utf-8') as f:
    for i in range(len(text)):
        url = 'https://www.shicimingju.com/' + link[i]
        f.write("<a href=%s  target='_blank'>%s</a>" % (url, text[i]) + '<br />\n')
