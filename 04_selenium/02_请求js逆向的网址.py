from selenium.webdriver import Chrome

url = 'https://www.linovelib.com/novel/2547/123015.html'
driver = Chrome()
driver.get(url)
with open('../00_素材箱/book.html', 'w', True, 'utf-8') as f:
    f.write(driver.page_source)
