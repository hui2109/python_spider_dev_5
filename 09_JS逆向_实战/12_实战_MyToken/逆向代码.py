"""
诀窍：多尝试在加密函数中传入'123456'，会省不少力气！！
思路：
time + "9527" + time.substr(0, 6) --> 算md5
"""
import time
import requests
from hashlib import md5

url = 'https://api.mytokenapi.com/ticker/currencylistforall'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
ti = str(int(time.time() * 1000))
temp = ti + "9527" + ti[:6]
obj = md5()
obj.update(temp.encode('utf-8'))
code = obj.hexdigest()

params = {
    'pages': '3,1',
    'sizes': '100,100',
    'subject': 'market_cap',
    'language': 'en_US',
    'timestamp': ti,
    'code': code,
    'platform': 'web_pc',
    'v': '0.1.0',
    'legal_currency': 'USD',
    'international': '1'
}
resp = requests.get(url=url, params=params, headers=headers)
print(resp.text)
