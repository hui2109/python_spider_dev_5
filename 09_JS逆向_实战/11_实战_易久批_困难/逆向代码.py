# windows下首先应该锁定参数
import os

if os.name == 'nt':
    from functools import partial
    import subprocess

    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import json
from hashlib import sha1
import hmac

import time
import requests


def get_sdata():
    r = "f940c9e2_a930_4869_8759_16f9d9e9005f"
    o = time.time()  # current_time
    a = 1686372265.583  # local_init_time
    c = 1686372266  # server_init_time
    i = c + (o - a)

    i = str(i).split(".")[0]
    u = json.dumps(data, separators=(',', ':'))
    obj = sha1()
    obj.update(u.encode('utf-8'))
    s = obj.hexdigest()
    l = 'POST' + "/himalaya-ApiService-UA2/user/login" + s
    f = i
    p = hmac.new(f.encode('utf-8'), (i + r + l).encode('utf-8'), sha1).hexdigest()

    return {
        'x-sign-nonce': r,
        'x-sign-timestamp': i,
        'x-sign': p,
    }


url = 'https://www.yijiupi.com/himalaya-ApiService-UA2/user/login'
# data要用来算md5，所以是有顺序的，必须是这个顺序
data = {
    "appCode": "ShoppingMallPC",
    "appVersion": "4",
    "deviceId": "dbd147700df5664f539753fce991b3c9",
    "deviceType": 3,
    "mobileNo": "13258371999",
    "password": "44445555",
    "cityId": "701",
    "userClassId": 1,
    "userDisplayClass": 0,
    "addressId": ""
}

temp = get_sdata()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'X-Sign': temp['x-sign'],
    'X-Sign-Nonce': temp['x-sign-nonce'],
    'X-Sign-Timestamp': temp['x-sign-timestamp'],
    'X-Sign-Version': '1.0',
    'Security-Token': '',
    'Device-Series': data['deviceId']
}
resp = requests.post(url=url, headers=headers, data=json.dumps(data, separators=(',', ':')))
print(resp.json())
