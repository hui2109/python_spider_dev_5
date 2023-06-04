"""
way: AES
key: ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl
把key拿去算md5，得到16个字节
iv: ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4
把iv拿去算md5，得到16个字节
mode: CBC
"""

import base64
import json
import time
from hashlib import md5

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

url = 'https://dict.youdao.com/webtranslate'
time = int(time.time() * 1000)
obj = md5()
obj.update(f'client=fanyideskweb&mysticTime={time}&product=webfanyi&key=fsdsogkndfokasodnaso'.encode('utf-8'))
sign = obj.hexdigest()
# print(sign)

word = input('输入想查询的单词: ')
data = {
    'i': word,
    'from': 'auto',
    'to': '',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': sign,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': str(time),
    'keyfrom': 'fanyi.web'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Referer': 'https://fanyi.youdao.com/',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1547736371.5531156; OUTFOX_SEARCH_USER_ID=-1328728229@218.194.27.203'
}
resp = requests.post(url, data=data, headers=headers)
# print(resp.text)  # 返回加密的base64字符串
# 将base64字符串中的'_'替换成'/'，'-'替换成'+'
result = resp.text.replace('_', '/').replace('-', '+')

obj1 = md5()
obj1.update('ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'.encode('utf-8'))
key = obj1.digest()

obj2 = md5()
obj2.update('ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'.encode('utf-8'))
iv = obj2.digest()

aes = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)
mi_bs = base64.b64decode(result)
ming_bs_pad = aes.decrypt(mi_bs)
ming_bs = unpad(ming_bs_pad, 16)
ming = ming_bs.decode('utf-8')
print(json.loads(ming))
