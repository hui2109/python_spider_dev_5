"""
思路：
{
    "x-access-token": "",
    "x-appid": "pc",
    "x-client-info": "pc",
    "x-client-version": "1.2.0",
    "x-sign": x,
    "x-t": time,
    "x-v": "1.0.0",
    "x-ver": "1.1",
}
x: ["/v1/user/login", "1.0.0", "pc", "DHz@uEun&k^LtqbhYqUN5wetfaO8p2", time, "", "pc", "1.2.0", w].join("|")  --> 算md5
w: "{"username":"13688012108","password":"MvEnq3xczYfh","sms_login":0}"
"""
import json
import time

import requests
from hashlib import md5

ti = str(round(time.time()))
data = {
    'username': "13267891011",
    'password': "dasasasddasds",
    'sms_login': 0
}
w = json.dumps(data, separators=(',', ':'))
temp = "|".join([
    "/v1/user/login",
    "1.0.0",
    "pc",
    "DHz@uEun&k^LtqbhYqUN5wetfaO8p2",
    ti,
    "",
    "pc",
    "1.2.0",
    w
])
obj = md5()
obj.update(temp.encode('utf-8'))
sign = obj.hexdigest()

url = 'https://www.hengyirong.com/api/v1/user/login'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'X-Access-Token': '',
    'X-Appid': 'pc',
    'X-Client-Info': 'pc',
    'X-Client-Version': '1.2.0',
    'X-Sign': sign,
    'X-T': ti,
    'X-V': '1.0.0',
    'X-Ver': '1.1',
}

# 这个地方天坑！
# requests的post方法，传参json时，会自动把你的字典转换为json字符串，但不会采用最通用的方式（也就是会加空格）
# resp = requests.post(url=url, json=data, headers=headers)
resp = requests.post(url=url, data=w, headers=headers)
print(resp.json())
