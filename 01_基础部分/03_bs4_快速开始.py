from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "lxml")
print(type(soup))
print(soup.prettify())

print('--------------------')

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent)
print(soup.title.parent.name)

print('--------------------')

for link in soup.find_all('a'):
    print(link.get('id'))
    print(link.get('href'))

print('--------------------')

# 获取HTML文档中所有的文字内容
print(soup.get_text())
