from bs4 import BeautifulSoup

soup = BeautifulSoup(open('../00_素材箱/三国演义.html', 'r', True, 'utf-8'), 'lxml')
book_title_list = soup.select('.book-mulu>ul>li>a')
with open('../00_素材箱/爬取三国演义.html', 'w', True, 'utf-8') as f:
    for t in book_title_list:
        text = t.string
        href = t['href']
        url = 'https://www.shicimingju.com/' + href
        f.write("<a href=%s  target='_blank'>%s</a>" % (url, text) + '<br />\n')
