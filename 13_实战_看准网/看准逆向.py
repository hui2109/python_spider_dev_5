"""
url: https://www.kanzhun.com/search?cityCode=42&industryCodes=&pageNum=1&query=%E6%93%8D%E4%BD%9C%E5%91%98&type=4
iv: SIRLYcZQuXXhpYmQ (随机的)
key: G$$QawckGfaLB97r
mode: CBC
base64字符串: 将'/'替换成'_', 将'+'替换成'-', 将'='替换成'~'
b: 替换后的base64字符串
kiv: iv
"""
import base64
import json

import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

send_params = {"query": "操作员", "cityCode": "42", "industryCodes": "", "pageNum": 1, "limit": 15}
send_params_str = json.dumps(send_params)

# 加密
aes = AES.new(key='G$$QawckGfaLB97r'.encode('utf-8'), iv='SIRLYcZQuXXhpYmQ'.encode('utf-8'), mode=AES.MODE_CBC)
ming_bytes = send_params_str.encode('utf-8')
ming_bytes_pad = pad(ming_bytes, 16)
mi_bytes = aes.encrypt(ming_bytes_pad)
mi = base64.b64encode(mi_bytes).decode()
b = mi.replace('/', '_').replace('+', '-').replace('=', '~')
kiv = 'SIRLYcZQuXXhpYmQ'
# print(mi_replace)

# 发送请求
url = 'https://www.kanzhun.com/api_to/search/salary.json'
params = {
    'b': b,
    'kiv': kiv
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers, params=params)
# print(response.text)  # 成功获取加密的响应数据

# 解密
aes = AES.new(key='G$$QawckGfaLB97r'.encode('utf-8'), iv='SIRLYcZQuXXhpYmQ'.encode('utf-8'), mode=AES.MODE_CBC)
ciphertext = response.text
mi_bytes = base64.b64decode(ciphertext)
mi_bytes_pad = aes.decrypt(mi_bytes)
ming_bytes = unpad(mi_bytes_pad, 16)
ming = ming_bytes.decode('utf-8')
print(json.loads(ming))
