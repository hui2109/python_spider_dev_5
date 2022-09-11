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

# 标签（tag）
soup1 = BeautifulSoup('<b class="boldest">Extremely bold</b>', "lxml")
tag = soup1.b
print(type(tag))

print('--------------------')

soup2 = BeautifulSoup(html_doc, 'lxml')
print(soup2.body.b)
print(soup2.body.b.name)
print(soup2.a.attrs)
print(soup2.a['class'])

print('--------------------')

# NavigableString（字符串）
print(soup2.a.string)
print(type(tag.string))

print('--------------------')

# BeautifulSoup
print(soup2.name)
print(type(soup2.name))
print(soup2.attrs)
print(type(soup2.attrs))

print('--------------------')

# 注释（Comment）
html_doc1='<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>'
soup3 = BeautifulSoup(html_doc1, 'lxml')
print(soup3.a.string)
print(type(soup3.a.string))

