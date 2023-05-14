import base64
import json

import requests
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

"""
https://ctbpsp.com/#/
该网站使用DES加密，参数如下：
key: 1qaz@wsx3e
mode: ECB (不需要iv)
base64处理
"""

# 发送请求，获得响应数据
url = 'https://custominfo.cebpubservice.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers=headers)
ciphertext = resp.text.replace('"', '')
# print(ciphertext)

# 解密
# 秘钥超过了10位，取前8位即可
des = DES.new(key='1qaz@wsx3e'[:8].encode('utf-8'), mode=DES.MODE_ECB)
mi_bytes = base64.b64decode(ciphertext)
mi_bytes_pad = des.decrypt(mi_bytes)
ming_bytes = unpad(mi_bytes_pad, 8)
ming = ming_bytes.decode('utf-8')
print(json.loads(ming))
