from bs4 import BeautifulSoup

# 获取书籍标题及简介，构造为一个字典
book_title_intro_dict = {}
soup = BeautifulSoup(open('../00_素材箱/豆瓣.html', 'r', True, 'utf-8'), 'lxml')
for div in soup.select('div.detail-frame'):
    book_title_intro_dict[div.h2.a.string] = list(div.find_all('p')[2].stripped_strings)[0]
print(book_title_intro_dict)

# 获取图像链接并写入文件
file = open('../00_素材箱/image.html', 'w', True, 'utf-8')
for div in soup.select('div.detail-frame'):
    for img in div.parent.select('a.cover img'):
        file.write('<img src='+img['src']+'/>\n')
file.close()
