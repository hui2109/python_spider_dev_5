import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# opt = Options()
# opt.add_argument("--headless")
# opt.add_argument('--disable-gpu')
# driver = Chrome(options=opt)

driver = Chrome()
url = 'https://www.zhipin.com/web/geek/job?query=&city=101270100'
driver.get(url)
time.sleep(10)
with open('../00_素材箱/boss_直聘.html', 'w', True, 'utf-8') as f:
    f.write(driver.page_source)
