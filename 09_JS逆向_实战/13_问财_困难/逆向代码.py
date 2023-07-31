# 监测UA，使用navigator.userAgent的值，即
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
# 把Jn抠出来了

# windows下首先应该锁定参数
import os

if os.name == 'nt':
    from functools import partial
    import subprocess

    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import requests
import json

with open('./抠问财.js', 'r', 1, 'utf-8') as f:
    js_code = execjs.compile(f.read())
v = js_code.call('fn')
print(v)

robot_url = 'http://www.iwencai.com/customized/chart/get-robot-data'
data = {
    "source": "Ths_iwencai_Xuangu",
    "version": "2.0",
    "query_area": "",
    "block_list": "",
    "add_info": {"urp": {"scene": 1, "company": 1, "business": 1}, "contentType": "json", "searchInfo": True},
    "question": "黄金股",
    "perpage": 50,
    "page": 1,
    "secondary_intent": "stock",
    "log_info": {"input_type": "click"},
    "rsh": "Ths_iwencai_Xuangu_o9bhp1vutan86hj8x304qlafek8iafzy"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Cookie': f'v={v}',
    'Hexin-V': v
}

response = requests.post(robot_url, data=json.dumps(data, separators=(',', ':')), headers=headers)
print(response.json())
