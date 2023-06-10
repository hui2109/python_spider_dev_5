# https://www.endata.com.cn/BoxOffice/BO/Year/index.html
# windows下首先应该锁定参数
import json
import os

if os.name == 'nt':
    from functools import partial
    import subprocess

    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import requests

url = 'https://www.endata.com.cn/API/GetData.ashx'
data = {
    'year': '2022',
    'MethodName': 'BoxOffice_GetYearInfoData'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
response = requests.post(headers=headers, url=url, data=data)
mi_str = response.text

with open('混淆代码.js', 'r', True, 'utf-8') as f:
    js_code = f.read()

js = execjs.compile(js_code)
result = js.call('fn', mi_str)
print(json.loads(result))
