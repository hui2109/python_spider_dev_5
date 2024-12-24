import requests
import base64
import execjs
from urllib.parse import urlencode
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


# 发送加密请求
request_data = {
    "page": 3,
    "limit": 20,
    "taxonid": "",
    "startTime": "",
    "endTime": "",
    "province": "青海省",
    "city": "",
    "district": "",
    "pointname": "",
    "username": "",
    "serial_id": "",
    "ctime": "",
    "taxonname": "",
    "state": "",
    "mode": "0",
    "outside_type": 0
}
request_data = urlencode(request_data)
print(request_data)

f = open("中国鸟.js", mode="r", encoding="utf-8")
js_code = f.read()
js = execjs.compile(js_code)
result = js.call("get_data", request_data)
request_data = result[0]
uuid = result[2]
timestamp = str(result[1])
e = result[-1]


obj = md5()
s = e + str(uuid) + timestamp
obj.update(s.encode("utf-8"))
sign = obj.hexdigest()

headers = {
    "sign": sign,
    "timestamp": timestamp,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "requestId": uuid,
    # "Referer": "http://www.birdreport.cn/",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
url = "https://api.birdreport.cn/front/record/activity/search"

response = requests.post(url=url, data=request_data, headers=headers)

res = response.json().get("data")


# 响应解密：使用AES解密
key = '3583ec0257e2f4c8195eec7410ff1619'
iv = 'd93c0d5ec6352f20'

aes = AES.new(key=key.encode("utf8"), iv=iv.encode("utf-8"), mode=AES.MODE_CBC)
res = base64.b64decode(res)
ming = unpad(aes.decrypt(res), 16).decode("utf-8")
print(ming)
