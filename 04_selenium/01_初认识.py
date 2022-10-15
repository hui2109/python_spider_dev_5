from selenium.webdriver import Chrome

driver = Chrome()
driver.get('https://www.baidu.com')
print(driver.page_source)
