# windows下首先应该锁定参数
import os

if os.name == 'nt':
    from functools import partial
    import subprocess

    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import requests
import json

url = 'https://custominfo.cebpubservice.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
ciphertext = response.text.strip('"')
# print(ciphertext)

with open('逆向代码.js', 'r', True, 'utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
result = js.call('decryptByDES', ciphertext)
# print(type(result))
print(json.loads(result))
