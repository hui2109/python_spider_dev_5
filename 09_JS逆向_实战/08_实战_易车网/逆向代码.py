"""
思路：
X-City-Id: 2501
X-Ip-Address: 60.255.85.128
X-Platform: pc
X-Sign: "cid=" + cid + "&param=" + "{"cityId":"2501","serialId":"1661"}" + "19DDD1FBDFF065D3A4DA777D2D7A81EC" + 时间戳  --> 算md5
x-user-guid: 随机值 "f8053557-0350-41bf-90ef-eba41c9abb10"
"""
import json
import time
from hashlib import md5

import requests

url = 'https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param'
temp_data = {
    "cityId": "2501",
    "serialId": "1661"
}
ti = str(int(time.time() * 1000))

con = "cid=" + '508' + "&param=" + json.dumps(temp_data,
                                              separators=(',', ':')) + "19DDD1FBDFF065D3A4DA777D2D7A81EC" + ti
obj = md5()
obj.update(con.encode('utf-8'))
sign = obj.hexdigest()

timestamp = ti
user_guid = "f8053557-0350-41bf-90ef-eba41c9abb10"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-City-Id': '2501',
    'X-Ip-Address': '60.255.85.128',
    'X-Platform': 'pc',
    'X-Sign': sign,
    'X-Timestamp': timestamp,
    'X-User-Guid': user_guid
}
params = {
    'cid': '508',
    'param': json.dumps(temp_data, separators=(',', ':'))
}
resp = requests.get(url=url, params=params, headers=headers)
with open('data.json', 'w', 1, 'utf-8') as f:
    f.write(resp.text)
