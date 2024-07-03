# windows下首先应该锁定参数
import os

if os.name == 'nt':
    from functools import partial
    import subprocess

    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import requests
from urllib.parse import urlencode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

search_url = 'https://api.birdreport.cn/front/record/activity/search'
data = {
    "city": "",
    "ctime": "",
    "district": "",
    "endTime": "",
    "limit": "20",
    "mode": "0",
    "outside_type": "0",
    "page": "5",
    "pointname": "",
    "province": "青海省",
    "serial_id": "",
    "startTime": "",
    "state": "",
    "taxonid": "",
    "taxonname": "",
    "username": ""
}
url_data = urlencode(data)

with open('./js解密.js', 'r', 1, 'utf-8') as f:
    js_code = execjs.compile(f.read())
jiemi_result = js_code.call('fn', url_data)
timestamp = jiemi_result['timestamp']
requestId = jiemi_result['requestId']
post_data = jiemi_result['post_data']
sign = jiemi_result['sign']
original = jiemi_result['original']

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Requestid': requestId,
    'Sign': sign,
    'Timestamp': str(timestamp),
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    # 为什么这里要写Content-Type？
    # 因为正常情况下，post请求发送form data，数据是字典形式，而这里是加密格式，所以要指定Content-Type
}

response = requests.post(search_url, data=post_data, headers=headers)
encrypted_data = response.json()['data']


# 对返回的数据进行解密
def decrypt(mi_str):
    mi_bs = base64.b64decode(mi_str)
    aes = AES.new(key=b"3583ec0257e2f4c8195eec7410ff1619", mode=AES.MODE_CBC, iv=b"d93c0d5ec6352f20")
    ming_bs_pad = aes.decrypt(mi_bs)
    ming_bs = unpad(ming_bs_pad, 16)
    ming = ming_bs.decode('utf-8')
    return ming


print(decrypt(encrypted_data))
